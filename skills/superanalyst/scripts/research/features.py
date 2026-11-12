"""Causal features: every history update is gated by an explicit cutoff."""
import math
from collections import defaultdict
from datetime import datetime, timedelta

def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("timezone required")
    return result

def main_ucl_phase(row):
    phase = (row.get("phase") or "").lower()
    return row.get("competition") == "uefa.champions" and ("group" in phase or "league phase" in phase)

def target_ucl(row):
    phase = (row.get("phase") or "").lower()
    return (row.get("competition") == "uefa.champions" and row.get("scope") == "90m"
            and "qual" not in phase and bool(phase)
            and any(part in phase for part in ("group", "league phase", "round of 16", "quarter", "semifinal", "semi-final", "final", "knockout")))

def distance_km(origin, destination):
    if origin is None or destination is None:
        return None
    lat1, lon1 = map(math.radians, origin)
    lat2, lon2 = map(math.radians, destination)
    q = math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2
    return 6371.0088 * 2 * math.asin(min(1., math.sqrt(q)))

def summarize(rows, team_id, window, prior):
    selected = rows[-window:]
    gf = [r["home_goals"] if r["home_id"] == team_id else r["away_goals"] for r in selected]
    ga = [r["away_goals"] if r["home_id"] == team_id else r["home_goals"] for r in selected]
    n = len(selected)
    return {"n": n, "gf": sum(gf)/n if n else None, "ga": sum(ga)/n if n else None,
            "attack_form": math.log((sum(gf)+5*prior)/(n+5)/prior),
            "defense_form": math.log((sum(ga)+5*prior)/(n+5)/prior),
            "ids": [r["match_id"] for r in selected]}

def build_features(rows, coordinates=None, horizon_hours=24):
    coordinates = coordinates or {}
    history, score_history = defaultdict(list), defaultdict(list)
    home_venues = {}
    total_goals, total_sides = 0., 0
    competition_totals = defaultdict(lambda: [0., 0])
    dated = sorted([(timestamp(r["available_proxy_at"]), r) for r in rows if r.get("scope") == "90m"], key=lambda item: (item[0], item[1]["match_id"]))
    result, pointer = {}, 0
    ordered = sorted(rows, key=lambda r: (timestamp(r["kickoff_at"]), r["match_id"]))
    for target in ordered:
        kickoff = timestamp(target["kickoff_at"])
        as_of = kickoff - timedelta(hours=horizon_hours)
        while pointer < len(dated) and dated[pointer][0] <= as_of:
            available, past = dated[pointer]
            pointer += 1
            for tid in (past["home_id"], past["away_id"]):
                history[tid].append(past)
                if past["scope"] == "90m":
                    score_history[tid].append(past)
            if not past.get("neutral") and past.get("venue_city") and past.get("venue_country"):
                home_venues[past["home_id"]] = (past["venue_city"], past["venue_country"])
            if past["scope"] == "90m":
                total_goals += past["home_goals"] + past["away_goals"]
                total_sides += 2
                competition_totals[past["competition"]][0] += past["home_goals"] + past["away_goals"]
                competition_totals[past["competition"]][1] += 2
        total, n = competition_totals[target["competition"]]
        global_prior = total_goals / total_sides if total_sides else 1.4
        prior = (total + 100*global_prior)/(n+100)
        sides = {}
        destination = coordinates.get((target.get("venue_city"), target.get("venue_country")))
        for side in ("home", "away"):
            tid = target[side+"_id"]
            past = score_history[tid]
            observed = history[tid]
            last = max(observed, key=lambda r: r["kickoff_at"]) if observed else None
            rest = (kickoff-timestamp(last["kickoff_at"])).total_seconds()/86400 if last else None
            congestion = sum(timestamp(r["kickoff_at"]) >= kickoff-timedelta(days=14) for r in observed)
            pair = [r for r in past if {r["home_id"],r["away_id"]} == {target["home_id"],target["away_id"]}
                    and timestamp(r["kickoff_at"]) >= as_of-timedelta(days=1096)]
            net = sum((r["home_goals"]-r["away_goals"]) * (1 if r["home_id"] == tid else -1) for r in pair)
            phase = [r for r in past if main_ucl_phase(r) and r.get("season_start_year") == target.get("season_start_year")]
            points = sum(3 if (r["home_goals"]-r["away_goals"]) * (1 if r["home_id"] == tid else -1) > 0 else
                         1 if r["home_goals"] == r["away_goals"] else 0 for r in phase)
            origin_key = home_venues.get(tid)
            origin = coordinates.get(origin_key) if origin_key else None
            trip = distance_km(origin, destination)
            sides[side] = {"windows": {str(w): summarize(past,tid,w,prior) for w in (5,10,20)},
                "rest_days": rest, "covered_matches_last14_days": congestion,
                "travel_city_distance_km": trip, "home_venue_observed": origin_key,
                "h2h_prior_count": len(pair), "h2h_shrunk_goal_difference": net/(len(pair)+5)/2,
                "phase_games": len(phase), "phase_points_per_game": points/len(phase) if phase else None,
                "latest_history_available_proxy_at": max((r["available_proxy_at"] for r in observed),default=None)}
        result[target["match_id"]] = {"match_id": target["match_id"], "as_of": as_of.isoformat(),
                                     "prior_goal_mean": prior, **sides}
    return result

def columns(variant):
    names = []
    if "form" in variant:
        names += ["attack_form", "defense_form"]
    if "rest" in variant:
        names += ["rest_gap", "congestion_gap", "rest_missing"]
    if "h2h" in variant:
        names += ["h2h"]
    if "travel" in variant:
        names += ["own_trip", "opponent_trip", "travel_missing"]
    if "motivation" in variant:
        names += ["own_phase_ppg", "opponent_phase_ppg", "phase_need_gap", "phase_missing"]
    return names

def numeric_features(feature, side, variant, target):
    own = feature[side]
    opp = feature["away" if side == "home" else "home"]
    window = "5" if "form5" in variant else "20" if "form20" in variant else "10"
    values = {"attack_form": own["windows"][window]["attack_form"],
              "defense_form": opp["windows"][window]["defense_form"],
              "rest_gap": (min(14, own["rest_days"] or 7)-min(14, opp["rest_days"] or 7))/7,
              "congestion_gap": (own["covered_matches_last14_days"]-opp["covered_matches_last14_days"])/4,
              "rest_missing": float(own["rest_days"] is None or opp["rest_days"] is None),
              "h2h": max(-2., min(2., own["h2h_shrunk_goal_difference"]))}
    trips = [own["travel_city_distance_km"], opp["travel_city_distance_km"]]
    values.update(own_trip=math.log1p(trips[0])/math.log(8001) if trips[0] is not None else 0.,
                  opponent_trip=math.log1p(trips[1])/math.log(8001) if trips[1] is not None else 0.,
                  travel_missing=float(any(v is None for v in trips)))
    applies = target["competition"] == "uefa.champions"
    missing = applies and (own["phase_points_per_game"] is None or opp["phase_points_per_game"] is None)
    own_ppg = own["phase_points_per_game"] if own["phase_points_per_game"] is not None else 1.5
    opp_ppg = opp["phase_points_per_game"] if opp["phase_points_per_game"] is not None else 1.5
    rounds = 8 if target.get("season_start_year",0) >= 2024 else 6
    own_need = min(1,own["phase_games"]/rounds)*(1-own_ppg/3)
    opp_need = min(1,opp["phase_games"]/rounds)*(1-opp_ppg/3)
    values.update(own_phase_ppg=(own_ppg-1.5)/1.5 if applies else 0.,
                  opponent_phase_ppg=(opp_ppg-1.5)/1.5 if applies else 0.,
                  phase_need_gap=own_need-opp_need if applies else 0., phase_missing=float(missing))
    return [values[name] for name in columns(variant)]
