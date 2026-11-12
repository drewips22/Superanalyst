import copy
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"skills/superanalyst/scripts/research"))
try:
    import numpy as np
    from models import objective,fit,predict_rates,baseline_rates
except ImportError as exc:
    raise unittest.SkipTest("optional research dependencies unavailable: "+str(exc))
from features import build_features
from test_research_features import match

class ResearchModelTests(unittest.TestCase):
    def test_analytic_gradient_matches_numerical_differences(self):
        nt,nc=2,2
        attack=np.array([0,1,0,1])
        defense=1-attack
        competition=np.array([0,0,1,1])
        home=np.array([1.,0.,1.,0.])
        y=np.array([2.,0.,1.,1.])
        weights=np.array([.7,.7,1.,1.])
        f=np.array([[.1,.2],[.2,.1],[.4,-.1],[-.1,.4]])
        theta=np.linspace(-.15,.2,1+2*nt+nc+1+nc+2)
        penalty=np.ones_like(theta)*2
        args=(attack,defense,competition,home,y,weights,f,nt,nc,True,penalty)
        value,gradient=objective(theta,*args)
        eps=1e-6
        numerical=[]
        for i in range(len(theta)):
            upper,lower=theta.copy(),theta.copy()
            upper[i]+=eps
            lower[i]-=eps
            numerical.append((objective(upper,*args)[0]-objective(lower,*args)[0])/(2*eps))
        np.testing.assert_allclose(gradient,numerical,atol=1e-7,rtol=1e-5)

    def test_future_training_result_is_rejected(self):
        rows=[match(1,0),match(2,4)]
        spec={"recency_half_life_days":365,"regularization":{"team_parameters":10,"competition_parameters":2,"numeric_features":5}}
        with self.assertRaises(ValueError):
            fit(rows,build_features(rows),"team_strength_home","2023-01-03T00:00:00Z",spec)

    def test_neutral_venue_removes_home_term_and_swap_reverses_rates(self):
        rows=[match(1,0),match(2,4,"B","A")]
        fs=build_features(rows)
        model={"variant":"team_strength_home","intercept":0.,"competition_offsets":{},
            "attack":{"A":.5,"B":-.5},"defense":{"A":-.2,"B":.2},
            "home_global":.7,"home_offsets":{},"numeric_coefficients":{}}
        row=dict(rows[1],neutral=True)
        first=predict_rates(model,row,fs["2"])
        row["home_id"],row["away_id"]=row["away_id"],row["home_id"]
        second=predict_rates(model,row,fs["2"])
        self.assertAlmostEqual(first["home"],second["away"])
        self.assertAlmostEqual(first["away"],second["home"])

    def test_baseline_abstains_on_less_than_five_histories(self):
        f=build_features([match(1,0),match(2,4)])["2"]
        self.assertIsNone(baseline_rates(f))

    def test_fitted_strength_learns_a_repeated_advantage(self):
        rows=[match(i,i*4,"A" if i%2==0 else "B","B" if i%2==0 else "A",
                    hg=3 if i%2==0 else 0,ag=0 if i%2==0 else 3) for i in range(24)]
        spec={"recency_half_life_days":365,"regularization":{"team_parameters":10,"competition_parameters":2,"numeric_features":5}}
        fs=build_features(rows)
        model=fit(rows,fs,"team_strength_home","2023-06-01T00:00:00Z",spec)
        self.assertTrue(model["optimization"]["success"])
        rates=predict_rates(model,dict(rows[0],neutral=True),fs["0"])
        self.assertGreater(rates["home"],rates["away"])
