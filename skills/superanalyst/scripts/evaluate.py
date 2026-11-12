"""Score forecasts and explicitly labeled historical reconstructions separately."""

import argparse
import json
import math
from pathlib import Path
from datetime import date

from stats import number, required_text, timestamp


EPSILON = 1e-15
LABELS = ("home", "draw", "away")


def log_loss(probability_of_outcome):
    return -math.log(min(1 - EPSILON, max(EPSILON, probability_of_outcome)))


def calibration(pairs):
    bins = [[] for _ in range(10)]
    for probability, observed in pairs:
        bins[min(9, int(probability * 10))].append((probability, observed))
    return [{"lower": i / 10, "upper": (i + 1) / 10,
             "upper_inclusive": i == 9, "n": len(values),
             "mean_probability": sum(p for p, _ in values) / len(values) if values else None,
             "observed_rate": sum(y for _, y in values) / len(values) if values else None}
            for i, values in enumerate(bins)]


def validate(row):
    for field in ("prediction_id", "match_id", "model_version", "horizon", "competition"):
        required_text(row.get(field), field)
    if row.get("scope") != "90m":
        raise ValueError("only 90m outcomes are supported")
    if not isinstance(row.get("synthetic"), bool):
        raise ValueError("synthetic must be explicitly true or false")
    as_of = timestamp(row.get("as_of"), "as_of")
    kickoff = timestamp(row.get("kickoff_at"), "kickoff_at")
    mode = row.get("mode", "forecast")
    if mode == "forecast":
        recorded = timestamp(row.get("recorded_at"), "recorded_at")
        available = timestamp(row.get("features_available_at"), "features_available_at")
        if not available <= as_of <= recorded < kickoff:
            raise ValueError("require features_available_at <= as_of <= recorded_at < kickoff_at")
        if row.get("reconstructed_at") is not None:
            raise ValueError("forecast must not contain reconstructed_at")
    elif mode == "retrospective_reconstruction":
        if row.get("recorded_at") is not None:
            raise ValueError("reconstruction must not masquerade as recorded_at forecast")
        rebuilt = timestamp(row.get("reconstructed_at"), "reconstructed_at")
        if not as_of < kickoff <= rebuilt:
            raise ValueError("require as_of < kickoff_at <= reconstructed_at")
        if not isinstance(row.get("point_in_time_verified"), bool):
            raise ValueError("reconstruction must state point_in_time_verified")
        required_text(row.get("reconstruction_notes"), "reconstruction_notes")
        if row.get("features_available_at") is not None:
            available = timestamp(row["features_available_at"], "features_available_at")
            if available > as_of:
                raise ValueError("reconstruction features_available_at exceeds as_of")
    else:
        raise ValueError("invalid evaluation mode")
    decision = row.get("decision")
    if decision not in {"predict", "observe", "insufficient_data"}:
        raise ValueError("invalid decision")
    if decision == "predict":
        probs = row.get("p_1x2")
        if not isinstance(probs, dict) or set(probs) != set(LABELS):
            raise ValueError("p_1x2 must contain exactly home, draw, away")
        for label in LABELS:
            number(probs[label], f"p_1x2.{label}", high=1)
        if not math.isclose(sum(probs.values()), 1, rel_tol=0, abs_tol=1e-8):
            raise ValueError("1X2 probabilities must sum to one")
        number(row.get("p_btts"), "p_btts", high=1)
    else:
        required_text(row.get("reason"), "reason for abstention")
        if row.get("p_1x2") is not None or row.get("p_btts") is not None:
            raise ValueError("abstentions must not contain prediction probabilities")
    result = row.get("result")
    if result is not None:
        if not isinstance(result, dict) or result.get("status") != "completed":
            raise ValueError("result must be null or a completed 90m result")
        if result.get("scope") != "90m":
            raise ValueError("result must use 90m scope")
        number(result.get("home_goals"), "home_goals", integer=True)
        number(result.get("away_goals"), "away_goals", integer=True)
        if result.get("finished_at") is not None:
            if timestamp(result["finished_at"], "finished_at") <= kickoff:
                raise ValueError("finished_at must be after kickoff")
        elif mode == "retrospective_reconstruction":
            # Preserve actual evidence precision instead of fabricating a full-time timestamp.
            completed = date.fromisoformat(required_text(result.get("completed_date_utc"), "completed_date_utc"))
            if completed < kickoff.date():
                raise ValueError("completed_date_utc cannot precede kickoff date")
        else:
            raise ValueError("forecast result requires finished_at")
        required_text(result.get("source_url"), "result.source_url")


def score_group(rows):
    scored = [r for r in rows if r["decision"] == "predict" and r.get("result") is not None]
    predictions = sum(r["decision"] == "predict" for r in rows)
    resolved = sum(r.get("result") is not None for r in rows)
    ppg = [(timestamp(r["kickoff_at"], "kickoff_at") - timestamp(r["as_of"], "as_of")).total_seconds() / 60
           for r in rows]
    brier_1x2, loss_1x2, brier_btts, loss_btts = [], [], [], []
    pairs = {key: [] for key in (*LABELS, "btts")}
    for row in scored:
        result = row["result"]
        h, a = result["home_goals"], result["away_goals"]
        outcome = "home" if h > a else "away" if h < a else "draw"
        p = row["p_1x2"]
        brier_1x2.append(sum((p[label] - int(label == outcome)) ** 2 for label in LABELS))
        loss_1x2.append(log_loss(p[outcome]))
        observed_btts = int(h > 0 and a > 0)
        btts_p = row["p_btts"]
        brier_btts.append((btts_p - observed_btts) ** 2)
        loss_btts.append(log_loss(btts_p if observed_btts else 1 - btts_p))
        for label in LABELS:
            pairs[label].append((p[label], int(label == outcome)))
        pairs["btts"].append((btts_p, observed_btts))
    average = lambda values: sum(values) / len(values) if values else None
    return {"considered": len(rows), "predicted": predictions,
            "abstained": len(rows) - predictions, "resolved": resolved,
            "unresolved": len(rows) - resolved, "scored": len(scored),
            "prediction_coverage": predictions / len(rows),
            "minutes_before_kickoff": {"min": min(ppg), "max": max(ppg)},
            "brier_1x2": average(brier_1x2), "log_loss_1x2": average(loss_1x2),
            "brier_btts": average(brier_btts), "log_loss_btts": average(loss_btts),
            "calibration": {key: calibration(values) for key, values in pairs.items()}}


def evaluate(rows):
    if not rows:
        raise ValueError("no prediction records")
    groups, ids, match_keys = {}, set(), set()
    for row in rows:
        validate(row)
        if row["prediction_id"] in ids:
            raise ValueError(f"duplicate prediction_id: {row['prediction_id']}")
        ids.add(row["prediction_id"])
        group_key = (row["model_version"], row["horizon"], row["competition"], row["synthetic"],
                     row.get("mode", "forecast"))
        match_key = (*group_key, row["match_id"])
        if match_key in match_keys:
            raise ValueError("duplicate match within model/horizon/competition; select a snapshot before scoring")
        match_keys.add(match_key)
        groups.setdefault(group_key, []).append(row)
    summaries = [{"model_version": key[0], "horizon": key[1], "competition": key[2],
                  "synthetic": key[3], "mode": key[4], **score_group(values)} for key, values in sorted(groups.items())]
    return {"evaluator_version": "0.2.0", "records": len(rows),
            "brier_1x2_convention": "sum of squared errors over three outcomes; range 0 to 2",
            "log_loss_epsilon": EPSILON, "groups": summaries,
            "note": "Scoring only. Timestamp checks do not prove an immutable forecast archive or model quality."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 JSONL, one record per line")
    args = parser.parse_args()
    try:
        rows = []
        for line_number, line in enumerate(args.input.read_text(encoding="utf-8-sig").splitlines(), 1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except ValueError as exc:
                    raise ValueError(f"invalid JSON at line {line_number}: {exc}") from exc
        print(json.dumps(evaluate(rows), ensure_ascii=False, indent=2, allow_nan=False))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    main()
