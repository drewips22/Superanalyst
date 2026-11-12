"""Reproduce the nine-match historical cohort; prediction never opens outcomes."""
import argparse
import hashlib
import json
import math
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

CASE = Path(__file__).resolve().parent
ROOT = CASE.parents[1]
sys.path.insert(0, str(ROOT / "skills/superanalyst/scripts"))
from stats import number, poisson_forecast, required_text, timestamp
from evaluate import evaluate

MODEL = "last5-goals-mean-poisson-experimental-v1"
FREEZE_FILES = ("experiment.json", "fixtures.json", "features.json", "run.py",
                "predictions.json", "analysis-before-result.md",
                "../../skills/superanalyst/scripts/stats.py",
                "../../skills/superanalyst/scripts/evaluate.py")

def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_new(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False, allow_nan=False)
        handle.write("\n")

def summarize(team, as_of, target_ids):
    rows = sorted(team["matches"], key=lambda r: r["match_date"])
    if len(rows) != 5 or len({r["match_id"] for r in rows}) != 5:
        raise ValueError("exactly five distinct historical matches required")
    for row in rows:
        if row["match_id"] in target_ids:
            raise ValueError("target fixture cannot enter features")
        if row.get("kickoff_at"):
            if timestamp(row["kickoff_at"], "history kickoff") + timedelta(hours=4) > as_of:
                raise ValueError("historical match must finish before cutoff")
        elif date.fromisoformat(row["match_date"]) >= as_of.date():
            raise ValueError("date-only history must precede cutoff date")
        if row.get("scope") != "90m" or row.get("competitive") is not True:
            raise ValueError("competitive normal-time history required")
        required_text(row.get("source_url"), "history source")
        for key in ("goals_for", "goals_against"):
            number(row[key], key, integer=True)
        for key in ("shots", "shots_on_target", "xg_for", "xg_against"):
            if row.get(key) is not None:
                number(row[key], key)
    gf = sum(r["goals_for"] for r in rows)
    ga = sum(r["goals_against"] for r in rows)
    results = ["W" if r["goals_for"] > r["goals_against"] else
               "L" if r["goals_for"] < r["goals_against"] else "D" for r in rows]
    points = [{"W": 3, "D": 1, "L": 0}[v] for v in results]
    shots = [r["shots"] for r in rows if r.get("shots") is not None]
    comparable = len(shots) == 5 and len({r.get("statistics_provider") for r in rows}) == 1
    late = [r for r in rows if r.get("late_goal_coverage")]
    return {"team": team["team"], "gf": gf, "ga": ga, "gf_mean": gf / 5, "ga_mean": ga / 5,
            "results_oldest_first": results, "ppg": sum(points) / 5,
            "ppg_latest3_minus_previous2": sum(points[2:]) / 3 - sum(points[:2]) / 2,
            "scored_games": sum(r["goals_for"] > 0 for r in rows),
            "conceded_games": sum(r["goals_against"] > 0 for r in rows),
            "clean_sheets": sum(r["goals_against"] == 0 for r in rows),
            "btts_games": sum(r["goals_for"] > 0 and r["goals_against"] > 0 for r in rows),
            "shots_n": len(shots), "shots_mean_available": sum(shots) / len(shots) if shots else None,
            "shots_complete_comparable": comparable,
            "shots_provider": rows[0].get("statistics_provider") if comparable else None,
            "xg_n": sum(r.get("xg_for") is not None and r.get("xg_against") is not None for r in rows),
            "late_goal_n": len(late),
            "goals_for_76_plus_available": sum(r["goals_for_76_plus"] for r in late) if late else None,
            "goals_against_76_plus_available": sum(r["goals_against_76_plus"] for r in late) if late else None}

def flags(home, away, forecast):
    shots_known = (home["shots_complete_comparable"] and away["shots_complete_comparable"]
                   and home["shots_provider"] == away["shots_provider"]
                   and home["shots_provider"] is not None)
    return {
        "both_scored_ge4of5": min(home["scored_games"], away["scored_games"]) >= 4,
        "both_conceded_ge4of5": min(home["conceded_games"], away["conceded_games"]) >= 4,
        "both_low_clean_sheet": max(home["clean_sheets"], away["clean_sheets"]) <= 1,
        "one_high_clean_sheet": max(home["clean_sheets"], away["clean_sheets"]) >= 3,
        "both_historical_btts_majority": min(home["btts_games"], away["btts_games"]) >= 3,
        "away_model_favourite": max(forecast["p_1x2"], key=forecast["p_1x2"].get) == "away",
        "both_shots_12_to_15": all(12 <= s["shots_mean_available"] <= 15 for s in (home, away)) if shots_known else None}

def calculate(experiment, fixtures, features, created):
    if experiment["model_version"] != MODEL or any(experiment["numerical_adjustments"].values()):
        raise ValueError("preserve the specified unadjusted baseline")
    expected_rule = {"home": "(home_team_GF_last5/5 + away_team_GA_last5/5)/2",
                     "away": "(away_team_GF_last5/5 + home_team_GA_last5/5)/2"}
    if experiment["rate_rule"] != expected_rule:
        raise ValueError("unsupported rate rule")
    as_of = timestamp(experiment["as_of"], "as_of")
    if features["as_of"] != experiment["as_of"]:
        raise ValueError("inconsistent cutoff")
    target_ids = {f["match_id"] for f in fixtures}
    if len(fixtures) != 9 or len(target_ids) != 9:
        raise ValueError("cohort requires the nine distinct selected fixtures")
    teams = {t["team_id"]: t for t in features["teams"]}
    predictions = []
    for fixture in fixtures:
        home = summarize(teams[fixture["home_id"]], as_of, target_ids)
        away = summarize(teams[fixture["away_id"]], as_of, target_ids)
        home_rate = (home["gf_mean"] + away["ga_mean"]) / 2
        away_rate = (away["gf_mean"] + home["ga_mean"]) / 2
        forecast = poisson_forecast(home_rate, away_rate)
        total = home_rate + away_rate
        over = 1 - math.exp(-total) * (1 + total + total * total / 2)
        predictions.append({**fixture, "prediction_id": experiment["experiment_id"] + "-" + fixture["match_id"],
            "competition": "UEFA Champions League 2026/27", "model_version": MODEL,
            "mode": "retrospective_reconstruction", "synthetic": False, "scope": "90m",
            "as_of": experiment["as_of"], "reconstructed_at": created,
            "horizon": "common-cutoff-T-5h45-to-8h", "features_available_at": None,
            "point_in_time_verified": False,
            "reconstruction_notes": "Results exposed in user image/search/dynamic preview headers; reconstructed now from historical pages without archived original versions. Deterministic goal-only baseline unchanged; not a blind or pre-kickoff forecast.",
            "decision": "predict", "analysis_status": "provisional", "calibrated": False,
            "goal_rates": {"home": home_rate, "away": away_rate},
            "p_1x2": forecast["p_1x2"], "p_btts": forecast["p_btts"], "p_over_2_5": over,
            "pick_1x2": max(forecast["p_1x2"], key=forecast["p_1x2"].get),
            "pick_btts": forecast["p_btts"] >= .5, "pick_over_2_5": over >= .5,
            "p_clean_sheet_home": forecast["p_clean_sheet_home"],
            "p_clean_sheet_away": forecast["p_clean_sheet_away"],
            "top_scores": forecast["top_scores"], "home_summary": home, "away_summary": away,
            "pattern_flags": flags(home, away, forecast), "result": None})
    evaluate(predictions)
    return predictions

def analysis(predictions, features):
    teams = {t["team_id"]: t for t in features["teams"]}
    lines = ["# Analisis yang dibekukan sebelum tahap penilaian", "",
        "Sembilan laga pada **5 November 2026 WIB / 4 November Eropa**. Cutoff informasi **4 November 19.00 WIB (12:00 UTC)**. Dibuat sekarang sebagai rekonstruksi; hasil sudah terekspos, jadi bukan uji buta. Halaman historis tidak memiliki arsip versi asli yang lengkap.", "",
        "Model tetap: λ kandang = (GF kandang lima laga + GA tandang lima laga)/10; λ tandang simetris. Gol Poisson independen; tanpa bobot tambahan untuk kandang, cedera, motivasi, H2H, xG, atau pasar. Ambang BTTS/Over 2,5 adalah 50%; 1X2 memilih peluang terbesar. Semua angka provisional dan belum terkalibrasi.", "",
        "Prediksi memakai lima laga kompetitif seluruh kompetisi, 90 menit + injury time. Adu penalti tidak dihitung sebagai kemenangan 90 menit. Rekaman skor target tidak dibaca oleh jalur prediksi.", "",
        "## Batas cakupan", ""]
    lines += ["- " + note for note in features["quality_notes"]]
    lines += ["", "Dua flag `both_conceded_ge4of5` dan `both_low_clean_sheet` ekuivalen secara matematis pada jendela lima laga; jangan menghitungnya sebagai dua bukti terpisah. Gol menit akhir bukan ukuran intensitas pressing/tembakan.", ""]
    for p in predictions:
        ctx = features["contexts"][p["match_id"]]
        lines += [f'## {p["home"]} — {p["away"]}', "", "### Data", ""]
        for side in ("home", "away"):
            s = p[side + "_summary"]
            lines += [f'**{p[side]}**. Urutan tertua → terbaru; skor dari sudut tim.', "",
                "| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |",
                "| --- | --- | --- | --- | --- | --- | --- |"]
            for r in teams[p[side + "_id"]]["matches"]:
                shots = "N/A" if r.get("shots") is None else f'{r["shots"]:g}'
                lines.append(f'| {r["match_date"]} | {r["opponent"]} | {r["venue"]} | {r["goals_for"]}–{r["goals_against"]} | {shots} | N/A | [data]({r["source_url"]}) |')
            mean = "N/A" if s["shots_mean_available"] is None else f'{s["shots_mean_available"]:.1f}'
            lines += ["", f'GF **{s["gf"]}**; GA/laga **{s["ga_mean"]:.2f}**; hasil **{"-".join(s["results_oldest_first"])}**; PPG **{s["ppg"]:.2f}**. Clean sheet **{s["clean_sheets"]}/5**; BTTS **{s["btts_games"]}/5**. Tembakan rerata {mean} (cakupan {s["shots_n"]}/5); xG {s["xg_n"]}/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya {s["ppg_latest3_minus_previous2"]:+.2f}; ini tren hasil, bukan tren xG.', "",
                f'Gol 76–90+: cetak {s["goals_for_76_plus_available"]}, kebobolan {s["goals_against_76_plus_available"]}; hanya {s["late_goal_n"]}/5 laga dengan event lengkap.', ""]
        lines += ["### Pola dan konteks sebelum cutoff", "", ctx["h2h_and_venue_context"], ""]
        if ctx["preview_source"]:
            lines += [f'[UEFA, {ctx["published_date"]}]({ctx["preview_source"]}).', ""]
        for n in ctx["news"]:
            lines += [f'{n["summary"]} [Laporan, pembaruan {n["latest_reported_update"]}]({n["source_url"]}).', ""]
        if not ctx["news"]:
            lines += ["Ketersediaan pemain belum terverifikasi dari versi berita yang lolos cutoff; tidak diasumsikan skuad lengkap.", ""]
        if ctx.get("news_exclusion"):
            lines += [ctx["news_exclusion"], ""]
        lines += ["Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.", "",
                  "Flag yang ditetapkan sebelum penilaian: `" + json.dumps(p["pattern_flags"], ensure_ascii=False) + "`.", "",
                  "### Keputusan provisional", "",
                  f'1 **{p["p_1x2"]["home"]:.1%}** / X **{p["p_1x2"]["draw"]:.1%}** / 2 **{p["p_1x2"]["away"]:.1%}**; pilihan **{p["pick_1x2"]}**. BTTS **{p["p_btts"]:.1%}** ({"ya" if p["pick_btts"] else "tidak"}); Over 2,5 **{p["p_over_2_5"]:.1%}** ({"ya" if p["pick_over_2_5"] else "tidak"}).', "",
                  f'λ {p["goal_rates"]["home"]:.2f}–{p["goal_rates"]["away"]:.2f}. Estimasi clean sheet laga ini {p["p_clean_sheet_home"]:.1%} / {p["p_clean_sheet_away"]:.1%}; berbeda dari frekuensi historis di atas.', "",
                  "Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.", ""]
    return "\n".join(lines) + "\n"

def verify_frozen(case_dir):
    manifest = read(case_dir / "frozen-inputs.json")
    if set(manifest["sha256"]) != set(FREEZE_FILES):
        raise ValueError("unexpected frozen file set")
    for name, expected in manifest["sha256"].items():
        if digest(case_dir / name) != expected:
            raise ValueError(f"frozen file changed: {name}; start a new experiment")
    return manifest

def predict(case_dir):
    if any((case_dir / n).exists() for n in ("predictions.json", "frozen-inputs.json", "analysis-before-result.md")):
        raise ValueError("prediction already exists; start a new experiment")
    exp, fixtures, features = [read(case_dir / n) for n in ("experiment.json", "fixtures.json", "features.json")]
    created = datetime.now(timezone.utc).isoformat()
    predictions = calculate(exp, fixtures, features, created)
    write_new(case_dir / "predictions.json", predictions)
    with (case_dir / "analysis-before-result.md").open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(analysis(predictions, features))
    write_new(case_dir / "frozen-inputs.json", {"frozen_at": created,
        "sha256": {n: digest(case_dir / n) for n in FREEZE_FILES},
        "note": "Frozen before grading during reconstruction; not evidence of a blind pre-match forecast."})
    return {"action": "frozen", "n": len(predictions), "predictions": [
        {k: p[k] for k in ("home", "away", "p_1x2", "p_btts", "p_over_2_5", "pick_1x2")} for p in predictions]}

def score(predictions, outcomes):
    by_id = {r["match_id"]: r for r in outcomes}
    if len(by_id) != len(outcomes) or set(by_id) != {p["match_id"] for p in predictions}:
        raise ValueError("outcomes must match the cohort exactly once")
    rows = [dict(p, result=by_id[p["match_id"]]["result"]) for p in predictions]
    report = evaluate(rows)
    comparisons = []
    for r in rows:
        h, a = r["result"]["home_goals"], r["result"]["away_goals"]
        actual = "home" if h > a else "away" if h < a else "draw"
        lh, la = r["goal_rates"]["home"], r["goal_rates"]["away"]
        comparisons.append({"match_id": r["match_id"], "home": r["home"], "away": r["away"],
            "score": f"{h}-{a}", "actual_1x2": actual, "actual_btts": h > 0 and a > 0,
            "actual_over_2_5": h + a >= 3, "correct_1x2": r["pick_1x2"] == actual,
            "correct_btts": r["pick_btts"] == (h > 0 and a > 0),
            "correct_over_2_5": r["pick_over_2_5"] == (h + a >= 3),
            "exact_score_probability": math.exp(-lh-la) * lh**h / math.factorial(h) * la**a / math.factorial(a)})
    report["comparisons"] = comparisons
    report["pick_hits"] = {k: sum(r["correct_" + k] for r in comparisons) for k in ("1x2", "btts", "over_2_5")}
    report["p_over_2_5_metrics"] = {
        "brier": sum((p["p_over_2_5"] - c["actual_over_2_5"])**2 for p, c in zip(predictions, comparisons))/len(predictions),
        "log_loss": sum(-math.log(max(1e-15, p["p_over_2_5"] if c["actual_over_2_5"] else 1-p["p_over_2_5"])) for p, c in zip(predictions, comparisons))/len(predictions)}
    uniform = [dict(r, p_1x2={"home": 1/3, "draw": 1/3, "away": 1/3}, p_btts=.5) for r in rows]
    keys = ("brier_1x2", "log_loss_1x2", "brier_btts", "log_loss_btts")
    report["uninformed_comparison"] = {k: evaluate(uniform)["groups"][0][k] for k in keys}
    report["uninformed_comparison"].update(brier_over_2_5=.25, log_loss_over_2_5=math.log(2))
    report["patterns"] = {}
    for key in predictions[0]["pattern_flags"]:
        report["patterns"][key] = {}
        for flag_value, label in ((True, "true"), (False, "false"), (None, "unknown")):
            selected = [c for p, c in zip(predictions, comparisons) if p["pattern_flags"][key] is flag_value]
            report["patterns"][key][label] = {"n": len(selected), "match_ids": [c["match_id"] for c in selected],
                "btts_yes": sum(c["actual_btts"] for c in selected),
                "over_2_5_yes": sum(c["actual_over_2_5"] for c in selected),
                "correct_1x2": sum(c["correct_1x2"] for c in selected)}
    return report, rows

def grade(case_dir):
    if any((case_dir / n).exists() for n in ("evaluation.json", "scored-reconstruction.jsonl")):
        raise ValueError("evaluation exists; preserve it")
    manifest = verify_frozen(case_dir)
    report, rows = score(read(case_dir / "predictions.json"), read(case_dir / "outcomes.json"))
    report.update(evaluation_created_at=datetime.now(timezone.utc).isoformat(),
                  outcomes_sha256=digest(case_dir / "outcomes.json"),
                  predictions_sha256=manifest["sha256"]["predictions.json"])
    write_new(case_dir / "evaluation.json", report)
    with (case_dir / "scored-reconstruction.jsonl").open("x", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n")
    return {"action": "graded", "n": len(rows), "hits": report["pick_hits"],
            "metrics": {k: report["groups"][0][k] for k in ("brier_1x2", "log_loss_1x2", "brier_btts", "log_loss_btts")}}

def verify(case_dir):
    verify_frozen(case_dir)
    stored = read(case_dir / "predictions.json")
    rebuilt = calculate(read(case_dir / "experiment.json"), read(case_dir / "fixtures.json"),
                        read(case_dir / "features.json"), stored[0]["reconstructed_at"])
    if stored != rebuilt:
        raise ValueError("predictions do not reproduce")
    if (case_dir / "evaluation.json").exists():
        saved = read(case_dir / "evaluation.json")
        if saved["outcomes_sha256"] != digest(case_dir / "outcomes.json"):
            raise ValueError("outcomes changed")
        scored, rows = score(stored, read(case_dir / "outcomes.json"))
        for key, value in scored.items():
            if saved[key] != value:
                raise ValueError(f"evaluation does not reproduce: {key}")
        archived = [json.loads(line) for line in (case_dir / "scored-reconstruction.jsonl").read_text(encoding="utf-8").splitlines()]
        if rows != archived:
            raise ValueError("scored archive differs")
    return {"action": "verified", "n": len(stored), "reproduced": True}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("predict", "grade", "verify"))
    parser.add_argument("--case-dir", type=Path, default=CASE)
    args = parser.parse_args()
    try:
        print(json.dumps({"predict": predict, "grade": grade, "verify": verify}[args.command](args.case_dir), indent=2, ensure_ascii=False, allow_nan=False))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(2, f"error: {exc}\n")

if __name__ == "__main__":
    main()
