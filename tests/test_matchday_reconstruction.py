import copy
import importlib.util
import json
import math
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "backtests/ucl-2026-11-04"
spec = importlib.util.spec_from_file_location("md4_case", CASE / "run.py")
case = importlib.util.module_from_spec(spec)
spec.loader.exec_module(case)

class MatchdayReconstructionTests(unittest.TestCase):
    def setUp(self):
        self.exp = case.read(CASE / "experiment.json")
        self.fixtures = case.read(CASE / "fixtures.json")
        self.features = case.read(CASE / "features.json")

    def predict(self):
        return case.calculate(self.exp, self.fixtures, self.features, "2026-11-12T03:00:00Z")

    def test_cohort_and_cup_normal_time_scores(self):
        rows = self.predict()
        self.assertEqual(len(rows), 9)
        self.assertTrue(all(r["result"] is None for r in rows))
        self.assertEqual(rows[0]["home_summary"]["gf"], 8)
        self.assertEqual(rows[0]["home_summary"]["ga"], 13)
        self.assertEqual(rows[3]["home_summary"]["clean_sheets"], 3)
        arsenal = next(t for t in self.features["teams"] if t["team"] == "Arsenal")
        cup = next(m for m in arsenal["matches"] if m["match_id"] == "401921835")
        self.assertEqual((cup["goals_for"], cup["goals_against"], cup["scope"]), (1, 1, "90m"))
        self.assertEqual(rows[7]["away_summary"]["results_oldest_first"], ["W", "D", "W", "D", "W"])

    def test_target_and_future_history_rejected(self):
        for update in ({"match_id": self.fixtures[0]["match_id"]},
                       {"kickoff_at": "2026-11-04T11:00:00Z"},
                       {"kickoff_at": None, "match_date": "2026-11-04"},
                       {"scope": "120m"}):
            original = copy.deepcopy(self.features)
            self.features["teams"][0]["matches"][0].update(update)
            with self.subTest(update=update), self.assertRaises(ValueError):
                self.predict()
            self.features = original

    def test_incomplete_history_rejected(self):
        self.features["teams"][0]["matches"].pop()
        with self.assertRaises(ValueError):
            self.predict()

    def test_missing_xg_stays_missing_and_news_does_not_tune_baseline(self):
        before = self.predict()
        for team in self.features["teams"]:
            self.assertTrue(all(m["xg_for"] is None for m in team["matches"]))
        self.features["contexts"] = {}
        after = self.predict()
        self.assertEqual([p["p_1x2"] for p in before], [p["p_1x2"] for p in after])
        self.exp["numerical_adjustments"]["injuries"] = -.22
        with self.assertRaises(ValueError):
            self.predict()

    def test_shot_flag_requires_full_comparable_samples(self):
        rows = self.predict()
        self.assertIsNone(rows[0]["pattern_flags"]["both_shots_12_to_15"])
        home, away = copy.deepcopy(rows[1]["home_summary"]), copy.deepcopy(rows[1]["away_summary"])
        for s in (home, away):
            s.update(shots_mean_available=13, shots_complete_comparable=True, shots_provider="A")
        self.assertTrue(case.flags(home, away, rows[1])["both_shots_12_to_15"])
        away["shots_provider"] = "B"
        self.assertIsNone(case.flags(home, away, rows[1])["both_shots_12_to_15"])

    def test_over_probability_and_redundant_flags(self):
        for p in self.predict():
            total = sum(p["goal_rates"].values())
            self.assertAlmostEqual(p["p_over_2_5"], 1-math.exp(-total)*(1+total+total**2/2))
            self.assertEqual(p["pattern_flags"]["both_low_clean_sheet"], p["pattern_flags"]["both_conceded_ge4of5"])

    def test_snapshot_creation_refuses_overwrite(self):
        temporary_root = ROOT / "runs/test-temp"
        temporary_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary_root) as folder:
            path = Path(folder) / "snapshot.json"
            case.write_new(path, {"x": 1})
            with self.assertRaises(FileExistsError):
                case.write_new(path, {"x": 2})
            self.assertEqual(case.read(path), {"x": 1})

    def test_cohort_rejects_duplicate_or_missing_outcomes(self):
        with self.assertRaises(ValueError):
            case.score(self.predict(), [])

if __name__ == "__main__":
    unittest.main()
