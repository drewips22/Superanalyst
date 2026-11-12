"""Collect public historical ESPN schedules into an auditable local research corpus."""
import argparse
import concurrent.futures
import gzip
import hashlib
import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://site.api.espn.com/apis/site/v2/sports/soccer"
STANDINGS = "https://site.web.api.espn.com/apis/v2/sports/soccer"
LEAGUES = ("uefa.champions", "eng.1", "esp.1", "ger.1", "ita.1", "fra.1",
           "por.1", "ned.1", "bel.1", "tur.1", "sco.1")

def request_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Superanalyst private historical research", "Accept-Encoding": "gzip"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                blob = response.read()
                if response.headers.get("Content-Encoding") == "gzip" or blob[:2] == b"\x1f\x8b":
                    blob = gzip.decompress(blob)
            return json.loads(blob), hashlib.sha256(blob).hexdigest()
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
            time.sleep(1 + attempt)

def write_json(path, value):
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, allow_nan=False, separators=(",", ":"))
        handle.write("\n")

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def find_teams(value):
    found = {}
    if isinstance(value, dict):
        team = value.get("team")
        if isinstance(team, dict) and team.get("id"):
            found[str(team["id"])] = team.get("displayName", team.get("name"))
        for child in value.values():
            found.update(find_teams(child))
    elif isinstance(value, list):
        for child in value:
            found.update(find_teams(child))
    return found

def integer_score(competitor):
    value = competitor["score"]
    value = value.get("value", value.get("displayValue")) if isinstance(value, dict) else value
    numeric = float(value)
    if not numeric.is_integer() or numeric < 0:
        raise ValueError("invalid historical score")
    return int(numeric)

def normalize_event(event, schedule_url, fetched_at):
    comp = event["competitions"][0]
    status = comp.get("status", {}).get("type", {})
    league = event.get("league", {})
    slug = league.get("slug", "")
    if not status.get("completed") or "friendly" in slug.lower():
        return None
    home = next(r for r in comp["competitors"] if r["homeAway"] == "home")
    away = next(r for r in comp["competitors"] if r["homeAway"] == "away")
    kick = datetime.fromisoformat(event["date"].replace("Z", "+00:00"))
    normal = comp.get("status", {}).get("period") == 2
    venue = comp.get("venue", {})
    return {"match_id": str(event["id"]), "kickoff_at": kick.isoformat(),
        "available_proxy_at": (kick + timedelta(hours=4)).isoformat(),
        "availability_is_proxy": True, "scope": "90m" if normal else None,
        "home_id": str(home["team"]["id"]), "home": home["team"].get("displayName"),
        "away_id": str(away["team"]["id"]), "away": away["team"].get("displayName"),
        "home_goals": integer_score(home) if normal else None,
        "away_goals": integer_score(away) if normal else None,
        "competition": slug, "competition_name": league.get("name"),
        "season_start_year": event.get("season", {}).get("year"),
        "phase": event.get("seasonType", {}).get("name"),
        "phase_id": event.get("seasonType", {}).get("type"),
        "neutral": comp.get("neutralSite", False),
        "venue": venue.get("fullName"), "venue_city": venue.get("address", {}).get("city"),
        "venue_country": venue.get("address", {}).get("country"),
        "source_url": f'https://www.espn.com/soccer/match/_/gameId/{event["id"]}',
        "schedule_source_url": schedule_url, "retrieved_at": fetched_at,
        "normal_time_verification": "status period 2" if normal else None}

def cached_standings(item):
    season, league, cache = item
    path = cache / f"standings-{league}-{season}.json"
    if path.exists():
        return read(path)
    url = f"{STANDINGS}/{league}/standings?season={season}"
    raw, sha = request_json(url)
    result = {"season": season, "league": league, "source_url": url,
              "retrieved_at": datetime.now(timezone.utc).isoformat(),
              "source_sha256": sha, "teams": find_teams(raw)}
    write_json(path, result)
    return result

def cached_schedule(item):
    season, team_id, cache = item
    path = cache / f"schedule-{team_id}-{season}.json"
    if path.exists():
        return read(path)
    url = f"{API}/all/teams/{team_id}/schedule?season={season}&limit=200"
    raw, sha = request_json(url)
    fetched = datetime.now(timezone.utc).isoformat()
    rows = [normalize_event(e, url, fetched) for e in raw.get("events", [])]
    result = {"team_id": team_id, "season": season, "source_url": url,
              "retrieved_at": fetched, "source_sha256": sha,
              "matches": [r for r in rows if r is not None]}
    write_json(path, result)
    return result

def verify_normal_time(row, cache):
    path = cache / f'normal-time-{row["match_id"]}.json'
    if path.exists():
        return read(path)
    url = f'{API}/{row["competition"]}/summary?event={row["match_id"]}'
    raw, sha = request_json(url)
    competitors = raw["header"]["competitions"][0]["competitors"]
    scores = {}
    for competitor in competitors:
        halves = competitor.get("linescores", [])[:2]
        if len(halves) != 2:
            raise ValueError("normal-time halves unavailable")
        scores[competitor["homeAway"]] = sum(int(r["displayValue"]) for r in halves)
    result = dict(row, home_goals=scores["home"], away_goals=scores["away"], scope="90m",
                  normal_time_verification="first plus second half linescores; ET/shootout excluded",
                  verification_source_url=url, verification_source_sha256=sha)
    write_json(path, result)
    return result

def collect(output, seasons, workers):
    output.mkdir(parents=True, exist_ok=True)
    cache = output / "cache"
    cache.mkdir(exist_ok=True)
    team_seasons, ucl_teams, sources, errors = {}, {}, [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        tasks = {pool.submit(cached_standings, (s, league, cache)): (s, league) for s in seasons for league in LEAGUES}
        for future in concurrent.futures.as_completed(tasks):
            season, league = tasks[future]
            try:
                result = future.result()
                if not result["teams"]:
                    raise ValueError("no teams in standings")
                team_seasons.setdefault(season, {}).update(result["teams"])
                if league == "uefa.champions":
                    ucl_teams[season] = result["teams"]
                sources.append({k: result[k] for k in ("source_url", "retrieved_at", "source_sha256")})
            except Exception as exc:
                errors.append({"season": season, "league": league, "error": str(exc)})
    if any(season not in ucl_teams for season in seasons):
        raise ValueError("UCL participant metadata incomplete")
    print(json.dumps({"stage": "participants", "requests": sum(map(len, team_seasons.values())), "errors": errors}), flush=True)
    merged = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        tasks = {pool.submit(cached_schedule, (s, tid, cache)): (s, tid) for s, teams in team_seasons.items() for tid in teams}
        done = 0
        for future in concurrent.futures.as_completed(tasks):
            season, team_id = tasks[future]
            try:
                result = future.result()
                sources.append({k: result[k] for k in ("source_url", "retrieved_at", "source_sha256")})
                for row in result["matches"]:
                    if not "2020-07-01" <= row["kickoff_at"][:10] < "2026-07-01":
                        continue
                    existing = merged.get(row["match_id"])
                    if existing and any(existing[k] != row[k] for k in ("home_id", "away_id", "home_goals", "away_goals", "kickoff_at")):
                        raise ValueError("conflicting duplicate historical result")
                    merged[row["match_id"]] = row
            except Exception as exc:
                errors.append({"season": season, "team_id": team_id, "error": str(exc)})
            done += 1
            if done % 100 == 0:
                print(json.dumps({"stage": "schedules", "completed": done, "matches": len(merged), "errors": len(errors)}), flush=True)
    unresolved = [r for r in merged.values() if r["scope"] != "90m"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        tasks = {pool.submit(verify_normal_time, row, cache): row["match_id"] for row in unresolved}
        for future in concurrent.futures.as_completed(tasks):
            try:
                row = future.result()
                merged[row["match_id"]] = row
            except Exception as exc:
                errors.append({"match_id": tasks[future], "error": str(exc), "stage": "normal_time"})
    rows = sorted(merged.values(), key=lambda r: (r["kickoff_at"], r["match_id"]))
    destination = output / "matches.jsonl"
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, allow_nan=False, separators=(",", ":")) + "\n")
    manifest = {"retrieved_at": datetime.now(timezone.utc).isoformat(), "sources": sources,
        "matches": len(rows), "seasons": seasons, "ucl_teams": ucl_teams,
        "errors": errors, "unresolved_normal_time": sum(r["scope"] != "90m" for r in rows),
        "dataset_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "availability_note": "Historical schedules retrieved now; kickoff+4h is an explicit availability proxy, not an archived publication timestamp. Coverage is limited to competitions present in the selected teams' public ESPN schedules."}
    write_json(output / "manifest.json", manifest)
    print(json.dumps({"stage": "complete", "matches": len(rows), "errors": len(errors), "unresolved": manifest["unresolved_normal_time"]}), flush=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seasons", default="2020,2021,2022,2023,2024,2025")
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()
    collect(args.output, [int(v) for v in args.seasons.split(",")], args.workers)
