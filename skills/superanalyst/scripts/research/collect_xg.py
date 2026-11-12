"""Aggregate normal-time StatsBomb Open Data for an explicitly separate xG study."""
import argparse
import concurrent.futures
import hashlib
import io
import json
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

from collect_history import request_json, write_json, read

RAW = "https://raw.githubusercontent.com/statsbomb/open-data/master"

def aggregate(match, cache):
    path = cache / f'{match["match_id"]}.json'
    if path.exists():
        return read(path)
    mid = str(match["match_id"])
    url = f"{RAW}/data/events/{mid}.json"
    events, sha = request_json(url)
    home, away = str(match["home_team"]["home_team_id"]), str(match["away_team"]["away_team_id"])
    stats = {tid: {"xg": 0., "npxg": 0., "set_piece_xg": 0., "shots": 0,
                   "goals_76_plus": 0, "goal_events": 0} for tid in (home, away)}
    for e in events:
        if e.get("period") not in (1, 2):
            continue
        tid = str(e.get("team", {}).get("id"))
        if tid not in stats:
            continue
        shot = e.get("shot")
        if shot is not None:
            xg = float(shot["statsbomb_xg"])
            stats[tid]["xg"] += xg
            stats[tid]["shots"] += 1
            if shot.get("type", {}).get("name") != "Penalty":
                stats[tid]["npxg"] += xg
            if e.get("play_pattern", {}).get("name") in ("From Corner", "From Free Kick", "From Throw In"):
                stats[tid]["set_piece_xg"] += xg
            if shot.get("outcome", {}).get("name") == "Goal":
                stats[tid]["goal_events"] += 1
                stats[tid]["goals_76_plus"] += e.get("period") == 2 and e.get("minute", 0) >= 75
        if e.get("type", {}).get("name") == "Own Goal Against":
            beneficiary = away if tid == home else home
            stats[beneficiary]["goal_events"] += 1
            stats[beneficiary]["goals_76_plus"] += e.get("period") == 2 and e.get("minute", 0) >= 75
    # Historical local kick-off timezone is not guaranteed in this open export.
    # Date-only rows use next UTC midnight for result availability; forecasts use
    # the previous day's UTC midnight. This deliberately avoids invented precision.
    day = datetime.fromisoformat(match["match_date"]).replace(tzinfo=timezone.utc)
    row = {"match_id": "statsbomb-" + mid, "kickoff_at": day.isoformat(),
        "time_precision": "calendar_date", "available_proxy_at": (day + timedelta(days=1)).isoformat(),
        "availability_is_proxy": True, "scope": "90m", "home_id": "sb-" + home,
        "away_id": "sb-" + away, "home": match["home_team"]["home_team_name"],
        "away": match["away_team"]["away_team_name"], "home_goals": match["home_score"],
        "away_goals": match["away_score"], "competition": match["competition"]["competition_name"],
        "season_start_year": 2015, "neutral": False,
        "source_url": url, "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "source_sha256": sha, "xg_provider": "StatsBomb Open Data",
        "xg_definition": "published pre-shot statsbomb_xg; 90m, includes penalties; original model version unverified",
        "home_statistics": stats[home], "away_statistics": stats[away],
        "goal_event_score_verified": (stats[home]["goal_events"], stats[away]["goal_events"]) == (match["home_score"], match["away_score"])}
    write_json(path, row)
    return row

def collect(output, workers):
    output.mkdir(parents=True, exist_ok=True)
    cache = output / "cache"
    cache.mkdir(exist_ok=True)
    matches, sources = [], []
    for cid in (2, 12):
        url = f"{RAW}/data/matches/{cid}/27.json"
        data, sha = request_json(url)
        if len(data) != 380:
            raise ValueError("expected full 2015/16 league season")
        matches.extend(data)
        sources.append({"url": url, "sha256": sha, "n": len(data)})
    rows, errors = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        jobs = {pool.submit(aggregate, m, cache): m["match_id"] for m in matches}
        for i, future in enumerate(concurrent.futures.as_completed(jobs), 1):
            try:
                rows.append(future.result())
            except Exception as exc:
                errors.append({"match_id": jobs[future], "error": str(exc)})
            if i % 100 == 0:
                print(json.dumps({"completed": i, "errors": len(errors)}), flush=True)
    destination = output / "matches.jsonl"
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        for row in sorted(rows, key=lambda r: (r["kickoff_at"], r["match_id"])):
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    write_json(output / "manifest.json", {"provider": "StatsBomb Open Data", "sources": sources,
        "n": len(rows), "errors": errors, "dataset_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "goal_event_mismatches": [r["match_id"] for r in rows if not r["goal_event_score_verified"]],
        "note": "Auxiliary male domestic study, EPL and Serie A 2015/16; not modern UCL. Current exported xG versions and original publication dates are not point-in-time verified.",
        "attribution_url": "https://github.com/hudl/open-data"})
    print(json.dumps({"complete": len(rows), "errors": errors}), flush=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    collect(args.output, args.workers)
