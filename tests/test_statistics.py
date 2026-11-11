import copy
import json
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "superanalyst" / "scripts"))
from stats import poisson_forecast, summarize


class HistoryTests(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads((ROOT / "examples" / "team-history.synthetic.json").read_text())

    def test_latest_five_have_correct_totals_and_denominators(self):
        result = summarize(self.payload)
        self.assertEqual(result["selected_matches"][0]["match_id"], "synthetic-history-2")
        self.assertEqual(result["n"], 5)
        self.assertEqual(result["metrics"]["goals_for"]["total"], 8)
        self.assertAlmostEqual(result["metrics"]["goals_against"]["mean"], .8)
        self.assertEqual(result["metrics"]["xg_for"]["n"], 4)
        self.assertAlmostEqual(result["metrics"]["xg_for"]["mean"], 1.6)
        self.assertAlmostEqual(result["metrics"]["xgd_paired"]["mean"], .75)
        self.assertAlmostEqual(result["historical_btts"]["rate"], .6)
        self.assertEqual(result["points"], 10)
        self.assertIsNone(result["descriptive_trend"]["xgd_delta"])

    def test_input_order_does_not_change_chosen_window(self):
        expected = summarize(self.payload)
        self.payload["matches"].reverse()
        self.assertEqual(summarize(self.payload), expected)

    def test_late_publication_excluded_even_when_match_finished(self):
        self.payload["matches"][-1]["available_at"] = "2026-12-01T00:00:00Z"
        result = summarize(self.payload)
        ids = [row["match_id"] for row in result["selected_matches"]]
        self.assertNotIn("synthetic-history-6", ids)
        self.assertIn("synthetic-history-1", ids)
        self.assertEqual(len(result["excluded"]), 1)

    def test_future_fixture_result_is_not_used(self):
        future = copy.deepcopy(self.payload["matches"][-1])
        future.update(match_id="future", kickoff_at="2026-12-01T12:00:00Z",
                      finished_at="2026-12-01T14:00:00Z", available_at="2026-12-01T15:00:00Z")
        self.payload["matches"].append(future)
        self.assertEqual(summarize(self.payload)["metrics"]["goals_for"]["total"], 8)

    def test_short_history_reports_actual_n_without_five_game_trend(self):
        self.payload["matches"] = self.payload["matches"][-2:]
        result = summarize(self.payload)
        self.assertEqual(result["n"], 2)
        self.assertFalse(result["window_complete"])
        self.assertIsNone(result["descriptive_trend"])
        self.assertAlmostEqual(result["metrics"]["goals_for"]["mean"], 2.5)

    def test_all_missing_xg_is_null_and_zero_remains_known(self):
        for row in self.payload["matches"]:
            row.update(xg_for=None, xg_against=None)
        result = summarize(self.payload)
        self.assertEqual(result["metrics"]["xg_for"]["n"], 0)
        self.assertIsNone(result["metrics"]["xg_for"]["mean"])
        self.payload["matches"][-1]["xg_for"] = 0
        result = summarize(self.payload)
        self.assertEqual(result["metrics"]["xg_for"], {"n": 1, "total": 0, "mean": 0})

    def test_xgd_uses_only_paired_matches(self):
        self.payload["matches"][-1]["xg_for"] = None
        result = summarize(self.payload)
        self.assertEqual(result["metrics"]["xgd_paired"]["n"], 3)
        self.assertAlmostEqual(result["metrics"]["xgd_paired"]["mean"], (.9 - .2 + 1.4) / 3)

    def test_mixed_xg_sources_are_rejected(self):
        self.payload["matches"][-1]["xg_provider"] = "DifferentProvider"
        with self.assertRaisesRegex(ValueError, "mixed xG"):
            summarize(self.payload)

    def test_invalid_data_are_rejected(self):
        for field, value in [("goals_for", -1), ("goals_for", True),
                             ("xg_for", float("nan")), ("scope", "120m"),
                             ("shots_on_target", 100), ("goals_for_76_plus", 100)]:
            with self.subTest(field=field, value=value):
                payload = copy.deepcopy(self.payload)
                payload["matches"][-1][field] = value
                with self.assertRaises(ValueError):
                    summarize(payload)

    def test_naive_timestamps_and_duplicates_are_rejected(self):
        self.payload["as_of"] = "2026-11-01T10:00:00"
        with self.assertRaisesRegex(ValueError, "timezone"):
            summarize(self.payload)
        self.payload["as_of"] += "+07:00"
        self.payload["matches"].append(self.payload["matches"][-1])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            summarize(self.payload)

    def test_no_competitive_matches_is_explicit_error(self):
        for row in self.payload["matches"]:
            row["competitive"] = False
        with self.assertRaisesRegex(ValueError, "no completed"):
            summarize(self.payload)


class PoissonTests(unittest.TestCase):
    def test_clean_sheets_follow_opponents_scoring_rate(self):
        result = poisson_forecast(1.6, 1.2)
        self.assertAlmostEqual(result["p_clean_sheet_home"], math.exp(-1.2))
        self.assertAlmostEqual(result["p_clean_sheet_away"], math.exp(-1.6))
        inclusion_exclusion = (1 - result["p_clean_sheet_home"] - result["p_clean_sheet_away"]
                               + result["p_nil_nil"])
        self.assertAlmostEqual(result["p_btts"], inclusion_exclusion)

    def test_probability_mass_and_tail(self):
        for h, a in [(0, 0), (1.6, 1.2), (8, 10), (100, 100)]:
            with self.subTest(h=h, a=a):
                result = poisson_forecast(h, a)
                self.assertAlmostEqual(sum(result["p_1x2"].values()), 1)
                self.assertLess(result["omitted_tail_mass"], 2.1e-12)
                self.assertTrue(0 <= result["p_btts"] <= 1)

    def test_team_swap_reverses_win_probabilities(self):
        original, swapped = poisson_forecast(1.6, .8), poisson_forecast(.8, 1.6)
        self.assertAlmostEqual(original["p_1x2"]["home"], swapped["p_1x2"]["away"])
        self.assertAlmostEqual(original["p_1x2"]["draw"], swapped["p_1x2"]["draw"])
        self.assertAlmostEqual(original["p_btts"], swapped["p_btts"])

    def test_zero_rates_have_deterministic_nil_nil(self):
        result = poisson_forecast(0, 0)
        self.assertEqual(result["p_1x2"], {"home": 0, "draw": 1, "away": 0})
        self.assertEqual(result["p_btts"], 0)
        self.assertEqual(result["p_nil_nil"], 1)

    def test_invalid_rates_fail(self):
        for rate in [-1, float("inf"), float("nan"), True, 101]:
            with self.subTest(rate=rate), self.assertRaises(ValueError):
                poisson_forecast(rate, 1)


if __name__ == "__main__":
    unittest.main()
