import copy
import json
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "superanalyst" / "scripts"))
from evaluate import calibration, evaluate


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.rows = [json.loads(line) for line in
                     (ROOT / "examples" / "predictions.synthetic.jsonl").read_text().splitlines()]

    def test_known_scores_and_coverage(self):
        group = evaluate(self.rows)["groups"][0]
        self.assertEqual(group["considered"], 5)
        self.assertEqual(group["predicted"], 4)
        self.assertEqual(group["abstained"], 1)
        self.assertEqual(group["unresolved"], 2)
        self.assertEqual(group["scored"], 3)
        self.assertAlmostEqual(group["prediction_coverage"], .8)
        self.assertAlmostEqual(group["brier_1x2"], (.38 + .54 + .375) / 3)
        self.assertAlmostEqual(group["brier_btts"], (.16 + .0625 + .16) / 3)
        self.assertAlmostEqual(group["log_loss_1x2"], -(math.log(.5) * 2 + math.log(.4)) / 3)

    def test_temporal_leaks_are_rejected(self):
        for field, value in [("recorded_at", "2026-10-01T12:00:00Z"),
                             ("features_available_at", "2026-10-01T11:31:00Z"),
                             ("as_of", "2026-10-01T12:01:00Z")]:
            with self.subTest(field=field):
                row = copy.deepcopy(self.rows[0])
                row[field] = value
                with self.assertRaisesRegex(ValueError, "require features"):
                    evaluate([row])

    def test_probabilities_not_repaired_silently(self):
        for p in [{"home": .7, "draw": .3, "away": .2},
                  {"home": -.1, "draw": .5, "away": .6},
                  {"home": float("nan"), "draw": .3, "away": .2}]:
            row = copy.deepcopy(self.rows[0])
            row["p_1x2"] = p
            with self.subTest(p=p), self.assertRaises(ValueError):
                evaluate([row])

    def test_duplicate_ids_or_snapshots_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate prediction_id"):
            evaluate([self.rows[0], self.rows[0]])
        duplicate = copy.deepcopy(self.rows[0])
        duplicate["prediction_id"] = "revision"
        with self.assertRaisesRegex(ValueError, "duplicate match"):
            evaluate([self.rows[0], duplicate])

    def test_different_horizons_models_and_synthetic_flags_stay_separate(self):
        rows = [self.rows[0]]
        for field, value in [("horizon", "other-horizon"), ("model_version", "other-model"),
                             ("synthetic", False), ("competition", "other-competition")]:
            row = copy.deepcopy(self.rows[0])
            row["prediction_id"] = f"other-{field}"
            row[field] = value
            rows.append(row)
        groups = evaluate(rows)["groups"]
        self.assertEqual(len(groups), 5)
        self.assertTrue(all(g["scored"] == 1 for g in groups))

    def test_pending_and_abstention_do_not_become_losses(self):
        group = evaluate(self.rows[3:])["groups"][0]
        self.assertEqual(group["scored"], 0)
        self.assertIsNone(group["brier_1x2"])
        self.assertIsNone(group["brier_btts"])

    def test_abstention_cannot_smuggle_predictions_into_scores(self):
        row = copy.deepcopy(self.rows[3])
        row["p_btts"] = .8
        with self.assertRaisesRegex(ValueError, "abstentions"):
            evaluate([row])

    def test_zero_and_one_probabilities_have_finite_log_loss(self):
        row = copy.deepcopy(self.rows[0])
        row["p_1x2"] = {"home": 0, "draw": 1, "away": 0}
        row["p_btts"] = 0
        group = evaluate([row])["groups"][0]
        self.assertEqual(group["brier_1x2"], 2)
        self.assertEqual(group["brier_btts"], 1)
        self.assertTrue(math.isfinite(group["log_loss_1x2"]))

    def test_calibration_boundaries_account_for_all_predictions(self):
        bins = calibration([(0, 0), (.1, 1), (.99, 0), (1, 1)])
        self.assertEqual(sum(b["n"] for b in bins), 4)
        self.assertEqual(bins[0]["n"], 1)
        self.assertEqual(bins[1]["n"], 1)
        self.assertEqual(bins[9]["n"], 2)
        self.assertAlmostEqual(bins[9]["observed_rate"], .5)

    def test_result_scope_and_score_validation(self):
        for field, value in [("scope", "120m"), ("home_goals", True),
                             ("away_goals", -1), ("finished_at", "2026-09-01T00:00:00Z")]:
            row = copy.deepcopy(self.rows[0])
            row["result"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                evaluate([row])


if __name__ == "__main__":
    unittest.main()
