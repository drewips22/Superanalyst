"""Bandingkan keputusan Model Utama sebelum dan sesudah XI resmi."""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "skills/superanalyst/scripts"))
import decision_journal as journal
from forecast_archive import timestamp

MODEL_UTAMA = "qualitative_superanalyst_national_team_pilot_v1"
LINEUPS = "lineup_confirmations"


def verify_pair(before, after):
    journal.validate_record(before)
    journal.validate_record(after)
    if after["previous_sha256"] != before["sha256"]:
        raise ValueError("Jurnal XI harus merujuk langsung ke jurnal awal")
    early, late = before["forecast"], after["forecast"]
    early_cutoff = timestamp(early["as_of"])
    if timestamp(late["as_of"]) <= early_cutoff or (
        timestamp(after["recorded_at"]) <= timestamp(before["recorded_at"])
    ):
        raise ValueError("Versi XI harus dicatat sesudah versi awal")
    old_rows = {row["match_id"]: row for row in early["forecasts"]}
    new_rows = {row["match_id"]: row for row in late["forecasts"]}
    if not new_rows or not new_rows.keys() <= old_rows.keys():
        raise ValueError("Pakai laga dari jurnal awal")
    if any(row["analysis_method"] != MODEL_UTAMA for row in (*old_rows.values(), *new_rows.values())):
        raise ValueError("Kedua versi harus memakai metode Model Utama")
    old_inputs, new_inputs = before["inputs"], after["inputs"]
    if old_inputs["profile"] != new_inputs["profile"]:
        raise ValueError("Profil pertandingan harus sama")
    old_facts, new_facts = old_inputs["facts"], new_inputs["facts"]
    if LINEUPS in old_facts or old_facts != {k: v for k, v in new_facts.items() if k != LINEUPS}:
        raise ValueError("Salin fakta awal dan tambahkan hanya konfirmasi XI")
    confirmations = new_facts.get(LINEUPS, {})
    if set(confirmations) != set(new_rows):
        raise ValueError("Isi sumber XI resmi untuk setiap laga dalam versi XI")
    sources = {source["id"]: source for source in new_inputs["sources"]}
    valid_sources = {}
    for match_id, entry in confirmations.items():
        if set(entry) != {"home_source_id", "away_source_id"}:
            raise ValueError(f"Isi sumber XI kandang dan tandang: {match_id}")
        ids = set(entry.values())
        for source_id in ids:
            source = sources.get(source_id)
            if not source or not source["available_at"] or timestamp(source["available_at"]) <= early_cutoff:
                raise ValueError(f"Perlu sumber XI yang tersedia sesudah cutoff awal: {match_id}")
        valid_sources[match_id] = ids
    changes = journal.differences(early, late)
    if changes != after["changes"]:
        raise ValueError("Daftar perubahan berbeda dari isi kedua jurnal")
    journal.check_review(changes, after["review"], after["inputs"], early)
    for item in after["review"]["changes"]:
        if item["target"] == "scope":
            continue
        if item["target"] == "kickoff_at" or item["kind"] != "lineup_confirmation":
            raise ValueError("Perbandingan ini hanya menguji dampak XI resmi")
        if not set(item["source_ids"]) <= valid_sources[item["match_id"]]:
            raise ValueError("Gunakan sumber XI yang terdaftar untuk laga yang direvisi")
    return old_rows, new_rows


def selection(row, target):
    key = row["focus_target"] if target == "focus" else target
    return None if key is None else row["targets"][key]["pick"]


def correctness(graded_row, forecast_row, target):
    if not graded_row["resolved"]:
        return None
    key = forecast_row["focus_target"] if target == "focus" else target
    return graded_row["correct"].get(key)


def count_pair(values):
    paired = [(old, new) for old, new in values if old is not None and new is not None]
    return {
        "dinilai_kedua_versi": len(paired),
        "benar_awal": sum(old for old, _ in paired),
        "benar_xi": sum(new for _, new in paired),
        "salah_menjadi_benar": sum(not old and new for old, new in paired),
        "benar_menjadi_salah": sum(old and not new for old, new in paired),
    }


def compare(before, after, outcomes):
    old_rows, new_rows = verify_pair(before, after)
    if any(result["match_id"] not in old_rows for result in outcomes):
        raise ValueError("Hasil harus merujuk ke laga dalam jurnal awal")
    old_grade = {row["match_id"]: row for row in journal.grade(before, outcomes)["rows"]}
    new_grade = {row["match_id"]: row for row in journal.grade(after, outcomes)["rows"]}
    report = {}
    for target in (*journal.TARGETS, "focus"):
        resolved_pairs = [
            (correctness(old_grade[mid], old_rows[mid], target), correctness(new_grade[mid], row, target))
            for mid, row in new_rows.items()
        ]
        picks = [(selection(old_rows[mid], target), selection(row, target)) for mid, row in new_rows.items()]
        report[target] = {
            "pilihan_awal": sum(old is not None for old, _ in picks),
            "pilihan_xi": sum(new is not None for _, new in picks),
            "observasi_menjadi_pilihan": sum(old is None and new is not None for old, new in picks),
            "pilihan_menjadi_observasi": sum(old is not None and new is None for old, new in picks),
            **count_pair(resolved_pairs),
        }
    return {
        "eksperimen": "model-utama-xi-resmi-v1",
        "jurnal_awal": before["snapshot_id"],
        "jurnal_xi": after["snapshot_id"],
        "laga_awal": len(old_rows),
        "laga_dengan_xi": len(new_rows),
        "laga_selesai": sum(row["resolved"] for row in new_grade.values()),
        "target": report,
        "revisi_xi": [item for item in after["review"]["changes"] if item["target"] != "scope"],
    }


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jurnal_awal", type=Path)
    parser.add_argument("jurnal_xi", type=Path)
    parser.add_argument("--hasil", type=Path, help="daftar hasil resmi 90 menit dan injury time")
    args = parser.parse_args()
    try:
        outcomes = read_json(args.hasil) if args.hasil else []
        report = compare(read_json(args.jurnal_awal), read_json(args.jurnal_xi), outcomes)
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
