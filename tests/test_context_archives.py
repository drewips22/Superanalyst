import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"skills/superanalyst/scripts/research"))
from context import absence_snapshot,lineup_at_cutoff,market_comparison,decimal_odds_probabilities,diagnose_result

class ContextArchiveTests(unittest.TestCase):
    def setUp(self):
        self.cutoff="2026-11-04T12:00:00Z"
        self.player={"match_id":"m","team_id":"A","player_id":"p","status":"out",
            "source_url":"https://example.invalid/synthetic-announcement","announced_at":"2026-11-03T18:00:00Z",
            "expected_minutes_if_available":80,"minutes_reference_cutoff":"2026-11-02T00:00:00Z"}

    def test_later_announcement_does_not_enter_earlier_snapshot(self):
        future=dict(self.player,player_id="future",announced_at="2026-11-04T17:00:00Z")
        result=absence_snapshot([self.player,future],self.cutoff,"m")
        self.assertEqual(result["teams"]["A"]["known_unavailable"],["p"])
        self.assertEqual(len(result["excluded"]),1)
        self.assertIsNone(result["win_probability_adjustment"])

    def test_missing_role_minutes_are_unknown_not_zero(self):
        self.player["expected_minutes_if_available"]=None
        result=absence_snapshot([self.player],self.cutoff,"m")
        self.assertIsNone(result["teams"]["A"]["expected_unavailable_minutes"])

    def test_role_reference_from_future_rejected(self):
        self.player["minutes_reference_cutoff"]="2026-11-05T00:00:00Z"
        with self.assertRaises(ValueError):
            absence_snapshot([self.player],self.cutoff,"m")

    def test_actual_lineup_after_cutoff_cannot_leak(self):
        lineup={"official":True,"source_url":"https://example.invalid/synthetic-lineup",
                "announced_at":"2026-11-04T17:00:00Z","player_ids":list(range(11))}
        self.assertIsNone(lineup_at_cutoff(lineup,self.cutoff))

    def test_three_quotes_from_one_source_are_not_three_independent_sources(self):
        base={"match_id":"m","provider":"one","independence_group":"underlying-one",
            "contract":"home_win","scope":"90m","observed_at":"2026-11-04T11:59:00Z",
            "source_url":"https://example.invalid/synthetic-quote","probability":.5,"bid":.49,"ask":.51,"depth":20}
        report=market_comparison([base,dict(base),dict(base)],self.cutoff,"m","home_win")
        self.assertEqual(report["independent_sources"],1)
        self.assertFalse(report["comparison_complete"])
        self.assertFalse(report["inside_information_confirmed"])

    def test_closing_or_different_contract_quotes_excluded(self):
        quote={"match_id":"m","provider":"one","independence_group":"one","contract":"home_win",
               "scope":"90m","observed_at":"2026-11-04T17:44:00Z","source_url":"https://example.invalid/synthetic-quote"}
        self.assertFalse(market_comparison([quote],self.cutoff,"m","home_win")["eligible_quotes"])

    def test_margin_removed_probabilities_sum_to_one(self):
        result=decimal_odds_probabilities({"home":2,"draw":3,"away":4})
        self.assertAlmostEqual(sum(result["normalized_probabilities"].values()),1)
        self.assertGreater(result["overround"],0)

    def test_luck_annotation_does_not_change_or_exclude_result(self):
        p={"p_1x2":{"home":.233,"draw":.209,"away":.558}}
        result=diagnose_result(p,{"home_goals":3,"away_goals":2},"user suspects luck")
        self.assertEqual(result["luck_status"],"unverified")
        self.assertEqual(result["actual_1x2"],"home")
        self.assertFalse(result["excluded_from_evaluation"])
        self.assertIsNone(result["prediction_adjustment"])
