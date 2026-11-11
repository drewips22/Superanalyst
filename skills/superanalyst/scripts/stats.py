"""Descriptive football statistics and an explicitly uncalibrated Poisson calculator."""

import argparse
import json
import math
from datetime import datetime
from pathlib import Path


def timestamp(value, name):
    if not isinstance(value, str):
        raise ValueError(f"{name} must be an ISO 8601 string with timezone")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{name} must be ISO 8601") from exc
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError(f"{name} must include a timezone")
    return result


def number(value, name, low=0, high=None, integer=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number")
    if not math.isfinite(value) or value < low or (high is not None and value > high):
        raise ValueError(f"{name} is outside the supported range")
    if integer and not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    return value


def required_text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be nonempty text")
    return value


def metric(values):
    known = [value for value in values if value is not None]
    return {"n": len(known), "total": sum(known) if known else None,
            "mean": sum(known) / len(known) if known else None}


def summarize(payload):
    """Select the most recent five eligible matches, then report oldest first."""
    team = required_text(payload.get("team"), "team")
    as_of = timestamp(payload.get("as_of"), "as_of")
    synthetic = payload.get("synthetic")
    if not isinstance(synthetic, bool):
        raise ValueError("synthetic must be explicitly true or false")
    rows = payload.get("matches")
    if not isinstance(rows, list):
        raise ValueError("matches must be a list")
    eligible, excluded, seen = [], [], set()
    for row in rows:
        match_id = required_text(row.get("match_id"), "match_id")
        if match_id in seen:
            raise ValueError(f"duplicate match_id: {match_id}")
        seen.add(match_id)
        kickoff = timestamp(row.get("kickoff_at"), "kickoff_at")
        if row.get("status") != "completed" or row.get("competitive") is not True:
            excluded.append({"match_id": match_id, "reason": "not completed competitive match"})
            continue
        finished = timestamp(row.get("finished_at"), "finished_at")
        available = timestamp(row.get("available_at"), "available_at")
        if not kickoff < finished <= available:
            raise ValueError(f"invalid event/availability chronology: {match_id}")
        if finished > as_of or available > as_of:
            excluded.append({"match_id": match_id, "reason": "not available by as_of"})
            continue
        if row.get("scope") != "90m":
            raise ValueError(f"scores and metrics must use 90m scope: {match_id}")
        if row.get("venue") not in {"home", "away", "neutral"}:
            raise ValueError(f"invalid venue: {match_id}")
        for field in ("opponent", "competition", "source_url"):
            required_text(row.get(field), field)
        for field in ("goals_for", "goals_against"):
            number(row.get(field), field, integer=True)
        for field in ("shots", "shots_on_target", "goals_for_76_plus", "goals_against_76_plus"):
            if row.get(field) is not None:
                number(row[field], field, integer=True)
        for field in ("xg_for", "xg_against"):
            if row.get(field) is not None:
                number(row[field], field)
        if row.get("possession_pct") is not None:
            number(row["possession_pct"], "possession_pct", high=100)
        if row.get("shots") is not None and row.get("shots_on_target") is not None:
            if row["shots_on_target"] > row["shots"]:
                raise ValueError("shots_on_target cannot exceed shots")
        for late, total in (("goals_for_76_plus", "goals_for"),
                            ("goals_against_76_plus", "goals_against")):
            if row.get(late) is not None and row[late] > row[total]:
                raise ValueError(f"{late} cannot exceed {total}")
        if row.get("xg_for") is not None or row.get("xg_against") is not None:
            required_text(row.get("xg_provider"), "xg_provider")
            required_text(row.get("xg_definition"), "xg_definition")
        eligible.append((kickoff, row))
    eligible.sort(key=lambda pair: (pair[0], pair[1]["match_id"]))
    chosen = [row for _, row in eligible[-5:]]
    if not chosen:
        raise ValueError("no completed competitive matches available before as_of")
    providers = {(row["xg_provider"], row["xg_definition"])
                 for row in chosen
                 if row.get("xg_for") is not None or row.get("xg_against") is not None}
    if len(providers) > 1:
        raise ValueError("mixed xG providers/definitions; harmonize or analyze separately")
    n = len(chosen)
    results, points, xgd = [], [], []
    for row in chosen:
        gf, ga = row["goals_for"], row["goals_against"]
        result = "W" if gf > ga else "L" if gf < ga else "D"
        results.append(result)
        points.append({"W": 3, "D": 1, "L": 0}[result])
        xgd.append(row["xg_for"] - row["xg_against"]
                   if row.get("xg_for") is not None and row.get("xg_against") is not None
                   else None)
    summaries = {key: metric([row.get(key) for row in chosen]) for key in
                 ("goals_for", "goals_against", "xg_for", "xg_against", "shots",
                  "shots_on_target", "possession_pct", "goals_for_76_plus", "goals_against_76_plus")}
    summaries["xgd_paired"] = metric(xgd)
    trend = None
    if n == 5:
        trend = {"method": "newest three mean minus oldest two mean; descriptive only",
                 "ppg_delta": sum(points[2:]) / 3 - sum(points[:2]) / 2,
                 "xgd_delta": (sum(xgd[2:]) / 3 - sum(xgd[:2]) / 2)
                 if all(value is not None for value in xgd) else None}
    clean = sum(row["goals_against"] == 0 for row in chosen)
    no_goal = sum(row["goals_for"] == 0 for row in chosen)
    btts = sum(row["goals_for"] > 0 and row["goals_against"] > 0 for row in chosen)
    return {"team": team, "synthetic": synthetic, "as_of": payload["as_of"],
            "n": n, "window_complete": n == 5, "order": "oldest_to_newest",
            "selected_matches": chosen, "excluded": excluded,
            "older_eligible_not_selected": max(0, len(eligible) - 5),
            "xg_series": list(next(iter(providers))) if providers else None,
            "results": results, "wins": results.count("W"), "draws": results.count("D"),
            "losses": results.count("L"), "points": sum(points), "ppg": sum(points) / n,
            "metrics": summaries,
            "historical_clean_sheet": {"count": clean, "n": n, "rate": clean / n},
            "historical_failed_to_score": {"count": no_goal, "n": n, "rate": no_goal / n},
            "historical_btts": {"count": btts, "n": n, "rate": btts / n},
            "descriptive_trend": trend,
            "note": "Historical rates are not calibrated probabilities for the next fixture."}


def poisson_pmf(rate, tail_tolerance=1e-12):
    # Bound is numerical, not a football assumption. Recursion is stable on this range.
    number(rate, "goal rate", high=100)
    values = [math.exp(-rate)]
    while math.fsum(values) < 1 - tail_tolerance:
        values.append(values[-1] * rate / len(values))
        if len(values) > 1000:
            raise ValueError("Poisson tail did not converge")
    return values


def poisson_forecast(home_rate, away_rate):
    hp, ap = poisson_pmf(home_rate), poisson_pmf(away_rate)
    grid = [(h, a, ph * pa) for h, ph in enumerate(hp) for a, pa in enumerate(ap)]
    mass = math.fsum(p for _, _, p in grid)
    probabilities = {
        "home": math.fsum(p for h, a, p in grid if h > a) / mass,
        "draw": math.fsum(p for h, a, p in grid if h == a) / mass,
        "away": math.fsum(p for h, a, p in grid if h < a) / mass,
    }
    top = sorted(grid, key=lambda item: (-item[2], item[0], item[1]))[:5]
    return {"model": "independent_poisson_calculator_v0.1.0", "calibrated": False,
            "home_rate": home_rate, "away_rate": away_rate,
            "p_1x2": probabilities,
            "p_btts": -math.expm1(-home_rate) * -math.expm1(-away_rate),
            "p_clean_sheet_home": math.exp(-away_rate),
            "p_clean_sheet_away": math.exp(-home_rate),
            "p_nil_nil": math.exp(-home_rate - away_rate),
            "top_scores": [{"home_goals": h, "away_goals": a, "probability": p / mass}
                           for h, a, p in top],
            "omitted_tail_mass": max(0.0, 1 - mass),
            "note": "1X2/top scores normalized on adaptive grid. Rates supplied externally; no fitted model or calibration."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    summary = commands.add_parser("summary", help="summarize up to five eligible matches")
    summary.add_argument("input", type=Path)
    poisson = commands.add_parser("poisson", help="calculate from explicitly supplied goal rates")
    poisson.add_argument("--home-rate", type=float, required=True)
    poisson.add_argument("--away-rate", type=float, required=True)
    args = parser.parse_args()
    try:
        if args.command == "summary":
            result = summarize(json.loads(args.input.read_text(encoding="utf-8-sig")))
        else:
            result = poisson_forecast(args.home_rate, args.away_rate)
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    main()
