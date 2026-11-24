"""Kasus sintetis untuk pemeriksaan penyandingan jurnal."""

import copy
import unittest
from unittest.mock import patch

from compare import LINEUPS, MODEL_UTAMA, compare, journal

EARLY = "2099-01-01T10:00:00Z"
LATE = "2099-01-01T11:00:00Z"
KICKOFF = "2099-01-01T12:00:00Z"


def target(pick):
    return {
        "pick": pick, "confidence": "medium", "status": "provisional",
        "supporting_evidence": ["Bukti sintetis"], "contradicting_evidence": [],
    }


def forecast_row(name):
    return {
        "match_id": name, "kickoff_at": KICKOFF, "analysis_method": MODEL_UTAMA,
        "focus_target": "1x2",
        "targets": {"1x2": target("H"), "btts": target(False), "total_2_5": target("under")},
    }


def source(source_id, seen):
    return {"id": source_id, "url": f"https://example.org/{source_id}",
            "available_at": seen, "retrieved_at": seen}


def pair(*, include_other=True):
    names = ["contoh-a", "contoh-b", "contoh-c"]
    early = {"schema_version": "qualitative-forecast-v2", "as_of": EARLY,
             "forecasts": [forecast_row(name) for name in names]}
    old_inputs = {"as_of": EARLY, "profile": "competitive",
                  "facts": {"synthetic": True}, "sources": [source("preview", EARLY)]}
    with patch.object(journal, "utc_now", return_value=EARLY):
        before = journal.build_record(early, old_inputs)

    late, new_inputs = copy.deepcopy(early), copy.deepcopy(old_inputs)
    late["as_of"] = new_inputs["as_of"] = LATE
    new_inputs["sources"].append(source("official", LATE))
    new_inputs["facts"][LINEUPS] = {
        name: {"home_source_id": "official", "away_source_id": "official"} for name in names
    }
    late["forecasts"][0]["targets"]["1x2"] = target("A")
    late["forecasts"][1]["targets"]["btts"] = {
        "pick": None, "confidence": None, "status": "observasi", "abstain_reason": "Contoh",
        "supporting_evidence": [], "contradicting_evidence": [],
    }
    changes = []
    for name, key in (("contoh-a", "1x2"), ("contoh-b", "btts")):
        changes.append({
            "match_id": name, "target": key, "kind": "lineup_confirmation",
            "reason": "Perubahan sintetis", "source_ids": ["official"],
            "lineup_delta": [{"team": "Kandang", "player": "Pemain contoh", "expected": "starter",
                              "confirmed": "cadangan", "impact": "Peran berubah"}],
        })
    if not include_other:
        late["forecasts"].pop()
        del new_inputs["facts"][LINEUPS]["contoh-c"]
        changes.append({"match_id": "contoh-c", "target": "scope", "kind": "scope_change",
                        "reason": "Gelombang lain"})
    with patch.object(journal, "utc_now", return_value=LATE):
        after = journal.build_record(late, new_inputs, before, {"changes": changes})
    return before, after


def outcome(name, home, away):
    return {"match_id": name, "status": "completed", "scope": "90m",
            "home_goals": home, "away_goals": away}


class ComparisonTests(unittest.TestCase):
    def test_counts_focus_revisions_and_btts_observation(self):
        before, after = pair()
        report = compare(before, after, [outcome("contoh-a", 0, 1), outcome("contoh-b", 1, 1)])
        self.assertEqual(report["laga_selesai"], 2)
        self.assertEqual(report["target"]["focus"]["salah_menjadi_benar"], 1)
        self.assertEqual(report["target"]["focus"]["dinilai_kedua_versi"], 2)
        self.assertEqual(report["target"]["btts"]["pilihan_awal"], 3)
        self.assertEqual(report["target"]["btts"]["pilihan_xi"], 2)
        self.assertEqual(report["target"]["btts"]["pilihan_menjadi_observasi"], 1)
        self.assertEqual(report["target"]["btts"]["dinilai_kedua_versi"], 1)
        self.assertEqual(len(report["revisi_xi"]), 2)

    def test_counts_false_revision_without_scoring_unconfirmed_match(self):
        before, after = pair(include_other=False)
        report = compare(before, after, [outcome("contoh-a", 2, 0), outcome("contoh-c", 2, 0)])
        self.assertEqual((report["laga_awal"], report["laga_dengan_xi"], report["laga_selesai"]),
                         (3, 2, 1))
        self.assertEqual(report["target"]["focus"]["benar_menjadi_salah"], 1)
        self.assertEqual(report["target"]["focus"]["dinilai_kedua_versi"], 1)
        self.assertEqual(len(report["revisi_xi"]), 2)

    def test_keeps_unfinished_separate_and_rejects_unpaired_journal(self):
        before, after = pair()
        self.assertEqual(compare(before, after, [])["target"]["focus"]["dinilai_kedua_versi"], 0)
        other_before, _ = pair()
        with self.assertRaisesRegex(ValueError, "merujuk langsung"):
            compare(other_before, after, [])
