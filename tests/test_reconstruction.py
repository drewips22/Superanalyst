import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "backtests" / "ucl-2025-final"
sys.path.insert(0, str(ROOT / "skills" / "superanalyst" / "scripts"))
spec = importlib.util.spec_from_file_location("ucl_final_case", CASE / "run.py")
case = importlib.util.module_from_spec(spec)
spec.loader.exec_module(case)


class ReconstructionTests(unittest.TestCase):
    def setUp(self):
        self.experiment = json.loads((CASE / "experiment.json").read_text())
        self.features = json.loads((CASE / "features.json").read_text())

    def test_goal_rule_and_normal_time_history(self):
        result = case.calculate_prediction(self.experiment, self.features, "2026-11-12T00:00:00Z")
        self.assertEqual(result["home_summary"]["gf"], 13)
        self.assertEqual(result["away_summary"]["gf"], 10)
        self.assertEqual(result["away_summary"]["results_oldest_first"], ["W", "D", "W", "D", "W"])
        self.assertEqual(result["goal_rates"], {"home": 1.8, "away": 1.5})
        self.assertIsNone(result["result"])

    def test_xg_context_does_not_silently_change_goal_only_baseline(self):
        initial = case.calculate_prediction(self.experiment, self.features, "2026-11-12T00:00:00Z")
        changed = copy.deepcopy(self.features)
        changed["home_team"]["matches"][0]["xg_for"] = 20
        recalculated = case.calculate_prediction(self.experiment, changed, "2026-11-12T00:00:00Z")
        self.assertEqual(initial["p_1x2"], recalculated["p_1x2"])
        self.assertEqual(initial["p_btts"], recalculated["p_btts"])

    def test_future_and_extra_time_features_are_rejected(self):
        for field, value in [("match_date", "2025-05-31"), ("scope", "120m")]:
            features = copy.deepcopy(self.features)
            features["away_team"]["matches"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                case.calculate_prediction(self.experiment, features, "2026-11-12T00:00:00Z")

    def test_existing_snapshot_cannot_be_overwritten(self):
        temporary_root = (ROOT / "runs" / "test-temp").resolve()
        temporary_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary_root) as folder:
            self.assertTrue(Path(folder).resolve().is_relative_to(temporary_root))
            path = Path(folder) / "frozen.json"
            case.write_new(path, {"p": .6})
            with self.assertRaises(FileExistsError):
                case.write_new(path, {"p": .9})
            self.assertEqual(json.loads(path.read_text()), {"p": .6})


if __name__ == "__main__":
    unittest.main()
