import copy
import math
import sys
import unittest
from datetime import datetime,timedelta,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"skills/superanalyst/scripts/research"))
from features import build_features,distance_km,target_ucl,numeric_features
from scoring import evaluate,paired_month_interval

def match(mid,day,home="A",away="B",hg=1,ag=0):
    start=datetime(2023,1,1,tzinfo=timezone.utc)+timedelta(days=day)
    return {"match_id":str(mid),"kickoff_at":start.isoformat(),
        "available_proxy_at":(start+timedelta(hours=4)).isoformat(),"scope":"90m",
        "home_id":home,"away_id":away,"home":home,"away":away,
        "home_goals":hg,"away_goals":ag,"competition":"uefa.champions",
        "phase":"Group Stage","season_start_year":2023,"neutral":False,
        "venue_city":home+" City","venue_country":"Example"}

class CausalResearchFeaturesTests(unittest.TestCase):
    def test_target_and_future_goals_do_not_change_own_features(self):
        rows=[match(i,i*4) for i in range(8)]
        initial=build_features(rows)
        rows[5]["home_goals"]=99
        rows[6]["away_goals"]=88
        changed=build_features(rows)
        for i in range(6):
            self.assertEqual(initial[str(i)],changed[str(i)])
        self.assertNotEqual(initial["7"],changed["7"])

    def test_late_availability_and_non_normal_scores_excluded(self):
        rows=[match(1,0),match(2,4),match(3,8)]
        rows[0]["available_proxy_at"]="2023-02-01T00:00:00+00:00"
        rows[1]["scope"]="120m"
        f=build_features(rows)["3"]
        self.assertEqual(f["home"]["windows"]["5"]["n"],0)
        self.assertIsNone(f["home"]["rest_days"])

    def test_outlier_is_preserved_in_rolling_history(self):
        rows=[match(i,i*4,hg=7 if i==4 else 1) for i in range(6)]
        f=build_features(rows)["5"]
        self.assertEqual(f["home"]["windows"]["5"]["gf"],11/5)
        self.assertEqual(f["home"]["windows"]["5"]["ids"],["0","1","2","3","4"])

    def test_missing_coordinates_are_not_a_zero_kilometre_trip(self):
        f=build_features([match(1,0),match(2,4)])["2"]
        self.assertIsNone(f["home"]["travel_city_distance_km"])
        self.assertEqual(distance_km((0,0),(0,0)),0)
        self.assertAlmostEqual(distance_km((0,0),(0,1)),111.195,places=2)
        self.assertIsNone(distance_km(None,(0,0)))

    def test_observed_home_city_comes_from_prior_games(self):
        rows=[match(1,0,"A","B"),match(2,4,"B","A")]
        coords={("A City","Example"):(0,0),("B City","Example"):(0,1)}
        f=build_features(rows,coords)["2"]
        self.assertAlmostEqual(f["away"]["travel_city_distance_km"],111.195,places=2)
        self.assertIsNone(f["home"]["travel_city_distance_km"])

    def test_phase_points_do_not_include_target(self):
        f=build_features([match(1,0,hg=2,ag=0),match(2,4,hg=0,ag=9)])["2"]
        self.assertEqual(f["home"]["phase_points_per_game"],3)
        self.assertEqual(f["away"]["phase_points_per_game"],0)
        self.assertEqual(f["home"]["h2h_prior_count"],1)

    def test_qualifiers_not_selected_as_main_cohort(self):
        row=match(1,0)
        self.assertTrue(target_ucl(row))
        row["phase"]="Qualifying - Playoff Round"
        self.assertFalse(target_ucl(row))
        row["phase"]="Knockout Round Playoffs"
        self.assertTrue(target_ucl(row))

    def test_feature_builder_does_not_depend_on_input_order(self):
        rows=[match(i,i*4) for i in range(8)]
        self.assertEqual(build_features(rows),build_features(list(reversed(rows))))

class ResearchScoringTests(unittest.TestCase):
    def setUp(self):
        self.p={"match_id":"x","kickoff_at":"2024-09-01T18:00:00Z",
            "p_1x2":{"home":.233,"draw":.209,"away":.558},"p_btts":.64,"p_over_2_5":.66}
        self.y={"x":{"home_goals":3,"away_goals":2}}

    def test_favourite_losing_remains_an_error_with_finite_proper_score(self):
        report=evaluate([self.p],self.y)
        self.assertEqual(report["n"],1)
        self.assertEqual(report["correct_1x2"],0)
        self.assertAlmostEqual(report["log_loss_1x2"],-math.log(.233))

    def test_invalid_probabilities_and_duplicate_predictions_rejected(self):
        with self.assertRaises(ValueError):
            evaluate([self.p,self.p],self.y)
        changed=copy.deepcopy(self.p)
        changed["p_btts"]=-.1
        with self.assertRaises(ValueError):
            evaluate([changed],self.y)

    def test_paired_identical_models_have_zero_interval(self):
        result=paired_month_interval([self.p],[self.p],self.y,"log_loss_1x2",100)
        self.assertEqual(result["percentile_95_interval"],[0,0])

    def test_paired_comparisons_require_the_same_cohort(self):
        with self.assertRaises(ValueError):
            paired_month_interval([self.p],[],self.y,"log_loss_1x2",100)
