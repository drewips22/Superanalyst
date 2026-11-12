"""Reproduce a labeled retrospective case without reading the target result during prediction."""

import argparse
import hashlib
import json
import math
import sys
from datetime import date, datetime, timezone
from pathlib import Path

CASE = Path(__file__).resolve().parent
ROOT = CASE.parents[1]
sys.path.insert(0, str(ROOT / "skills" / "superanalyst" / "scripts"))
from stats import metric, number, poisson_forecast, required_text, timestamp
from evaluate import evaluate

FREEZE_FILES = ("experiment.json", "features.json", "run.py", "prediction.json", "analysis-before-result.md",
                "../../skills/superanalyst/scripts/stats.py",
                "../../skills/superanalyst/scripts/evaluate.py")

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, value):
    # Exclusive creation prevents accidental replacement of a frozen analysis.
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False, allow_nan=False)
        handle.write("\n")


def summarize_history(team, as_of):
    rows = sorted(team["matches"], key=lambda row: row["match_date"])
    seen = set()
    for row in rows:
        match_date = date.fromisoformat(row["match_date"])
        # These inputs have calendar-date precision; accept only earlier calendar days.
        if match_date >= as_of.date():
            raise ValueError("history match date must be before cutoff date")
        if row["match_id"] in seen:
            raise ValueError("duplicate historical match")
        seen.add(row["match_id"])
        if row.get("competitive") is not True or row.get("scope") != "90m":
            raise ValueError("case requires competitive 90m match data")
        for field in ("goals_for", "goals_against"):
            number(row[field], field, integer=True)
        required_text(row.get("score_source"), "score_source")
    rows = rows[-5:]
    if len(rows) != 5:
        raise ValueError("this experiment requires five real matches per team")
    outcomes = ["W" if r["goals_for"] > r["goals_against"] else
                "L" if r["goals_for"] < r["goals_against"] else "D" for r in rows]
    points = [{"W": 3, "D": 1, "L": 0}[v] for v in outcomes]
    series = {}
    for row in rows:
        if row.get("xg_for") is None or row.get("xg_against") is None:
            continue
        for field in ("xg_for", "xg_against"):
            number(row[field], field)
        name = required_text(row.get("xg_series"), "xg_series")
        series.setdefault(name, []).append(row)
    return {"team": team["name"], "selected_match_ids": [r["match_id"] for r in rows],
            "n": len(rows), "gf": sum(r["goals_for"] for r in rows),
            "ga": sum(r["goals_against"] for r in rows),
            "gf_per_match": sum(r["goals_for"] for r in rows) / 5,
            "ga_per_match": sum(r["goals_against"] for r in rows) / 5,
            "results_oldest_first": outcomes, "ppg": sum(points) / 5,
            "ppg_latest3_minus_previous2": sum(points[2:]) / 3 - sum(points[:2]) / 2,
            "clean_sheets": sum(r["goals_against"] == 0 for r in rows),
            "failed_to_score": sum(r["goals_for"] == 0 for r in rows),
            "btts_matches": sum(r["goals_for"] > 0 and r["goals_against"] > 0 for r in rows),
            "goals_for_76_plus": sum(r["goals_for_76_plus"] for r in rows),
            "goals_against_76_plus": sum(r["goals_against_76_plus"] for r in rows),
            "shots": metric([r.get("shots") for r in rows]),
            "shots_on_target": metric([r.get("shots_on_target") for r in rows]),
            "xg_by_published_series": {name: {
                "n": len(values), "xg_for": metric([r["xg_for"] for r in values]),
                "xg_against": metric([r["xg_against"] for r in values]),
                "xgd": metric([r["xg_for"] - r["xg_against"] for r in values])}
                for name, values in series.items()}}


def calculate_prediction(experiment, features, reconstructed_at):
    as_of = timestamp(experiment["as_of"], "as_of")
    kickoff = timestamp(experiment["fixture"]["kickoff_at"], "kickoff_at")
    if features["as_of"] != experiment["as_of"] or not as_of < kickoff:
        raise ValueError("inconsistent cutoff")
    if experiment["model_version"] != "last5-goals-mean-poisson-experimental-v1":
        raise ValueError("unsupported model; do not silently change a frozen experiment")
    if experiment["fixture"]["venue_type"] != "neutral":
        raise ValueError("this experiment is specified for a neutral venue")
    expected_rules = {
        "home": "(mean(home_team_goals_for_last5) + mean(away_team_goals_against_last5)) / 2",
        "away": "(mean(away_team_goals_for_last5) + mean(home_team_goals_against_last5)) / 2"}
    if experiment["rate_rule"] != expected_rules:
        raise ValueError("rate rule differs from the implemented model")
    if any(experiment["rules"][key] != 0 for key in
           ("home_advantage_adjustment", "injury_adjustment", "motivation_adjustment",
            "h2h_adjustment", "market_adjustment", "xg_adjustment")):
        raise ValueError("this baseline has no additional numerical adjustments")
    home = summarize_history(features["home_team"], as_of)
    away = summarize_history(features["away_team"], as_of)
    home_rate = (home["gf_per_match"] + away["ga_per_match"]) / 2
    away_rate = (away["gf_per_match"] + home["ga_per_match"]) / 2
    forecast = poisson_forecast(home_rate, away_rate)
    return {"prediction_id": experiment["experiment_id"], "match_id": "ucl-2025-2044466",
            "competition": experiment["fixture"]["competition"],
            "model_version": experiment["model_version"], "mode": experiment["mode"],
            "synthetic": False, "scope": "90m", "horizon": "T-31h",
            "as_of": experiment["as_of"], "kickoff_at": experiment["fixture"]["kickoff_at"],
            "reconstructed_at": reconstructed_at,
            "point_in_time_verified": False,
            "reconstruction_notes": "Created now from historical pages; original source versions not archived. This is not a blind test or a forecast recorded in 2025.",
            "features_available_at": None, "decision": "predict", "analysis_status": "provisional",
            "p_1x2": forecast["p_1x2"], "p_btts": forecast["p_btts"],
            "pick_1x2": max(forecast["p_1x2"], key=forecast["p_1x2"].get),
            "pick_btts": forecast["p_btts"] >= .5,
            "goal_rates": {"home": home_rate, "away": away_rate},
            "calibrated": False, "poisson_calculation": forecast,
            "home_summary": home, "away_summary": away,
            "model_inputs": "only the ten historical 90m goal counts; other statistics are descriptive",
            "result": None}


def verify_inputs(case_dir, manifest):
    if set(manifest["sha256"]) != set(FREEZE_FILES):
        raise ValueError("unexpected frozen file set")
    for filename, expected in manifest["sha256"].items():
        if digest(case_dir / filename) != expected:
            raise ValueError(f"frozen file changed: {filename}; create a new experiment instead")


def predict(case_dir):
    if any((case_dir / name).exists() for name in ("prediction.json", "frozen-inputs.json")):
        raise ValueError("prediction already frozen; use a new experiment directory")
    experiment = read_json(case_dir / "experiment.json")
    features = read_json(case_dir / "features.json")
    created = datetime.now(timezone.utc).isoformat()
    prediction = calculate_prediction(experiment, features, created)
    # Validate mode/time/probabilities before freezing. This path never opens outcome.json.
    evaluate([prediction])
    write_new(case_dir / "prediction.json", prediction)
    write_new(case_dir / "frozen-inputs.json", {
        "frozen_at": created,
        "sha256": {name: digest(case_dir / name) for name in FREEZE_FILES},
        "note": "Frozen during the 2026 reconstruction; not evidence of a pre-2025 forecast."})
    return {"action": "prediction_frozen", "reconstructed_at": created,
            "p_1x2": prediction["p_1x2"], "p_btts": prediction["p_btts"],
            "goal_rates": prediction["goal_rates"]}


def grade(case_dir):
    if any((case_dir / name).exists() for name in ("evaluation.json", "scored-reconstruction.jsonl")):
        raise ValueError("evaluation already exists; preserve the existing record")
    manifest = read_json(case_dir / "frozen-inputs.json")
    verify_inputs(case_dir, manifest)
    prediction = read_json(case_dir / "prediction.json")
    outcome = read_json(case_dir / "outcome.json")
    row = dict(prediction, result=outcome)
    report = evaluate([row])
    h, a = outcome["home_goals"], outcome["away_goals"]
    actual = "home" if h > a else "away" if h < a else "draw"
    actual_btts = h > 0 and a > 0
    rate_h, rate_a = prediction["goal_rates"]["home"], prediction["goal_rates"]["away"]
    exact_score_probability = (math.exp(-rate_h - rate_a) * rate_h ** h / math.factorial(h)
                               * rate_a ** a / math.factorial(a))
    report["comparison"] = {
        "actual_score": f"{h}-{a}", "actual_1x2": actual, "actual_btts": actual_btts,
        "pick_1x2": prediction["pick_1x2"], "correct_1x2": prediction["pick_1x2"] == actual,
        "pick_btts": prediction["pick_btts"], "correct_btts": prediction["pick_btts"] == actual_btts,
        "probability_of_observed_exact_score": exact_score_probability,
        "frozen_prediction_sha256": manifest["sha256"]["prediction.json"]}
    report["evaluation_created_at"] = datetime.now(timezone.utc).isoformat()
    report["outcome_sha256"] = digest(case_dir / "outcome.json")
    write_new(case_dir / "evaluation.json", report)
    with (case_dir / "scored-reconstruction.jsonl").open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n")
    return {"action": "evaluated", **report["comparison"],
            "metrics": {key: report["groups"][0][key] for key in
                        ("brier_1x2", "log_loss_1x2", "brier_btts", "log_loss_btts")}}


def verify(case_dir):
    verify_inputs(case_dir, read_json(case_dir / "frozen-inputs.json"))
    prediction = read_json(case_dir / "prediction.json")
    rebuilt = calculate_prediction(read_json(case_dir / "experiment.json"),
                                   read_json(case_dir / "features.json"), prediction["reconstructed_at"])
    if rebuilt != prediction:
        raise ValueError("recalculated prediction differs from frozen prediction")
    if (case_dir / "evaluation.json").exists():
        stored = read_json(case_dir / "evaluation.json")
        if stored["outcome_sha256"] != digest(case_dir / "outcome.json"):
            raise ValueError("outcome file differs from the evaluated outcome")
        rescored = evaluate([dict(prediction, result=read_json(case_dir / "outcome.json"))])
        if stored["groups"] != rescored["groups"]:
            raise ValueError("evaluation does not reproduce")
    return {"action": "verified", "prediction_reproduced": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("predict", "grade", "verify"))
    parser.add_argument("--case-dir", type=Path, default=CASE,
                        help="use a separate directory for new experiments; existing snapshots are never overwritten")
    args = parser.parse_args()
    try:
        result = {"predict": predict, "grade": grade, "verify": verify}[args.command](args.case_dir)
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    main()
