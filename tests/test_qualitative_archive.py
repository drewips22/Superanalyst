import copy
import importlib.util
import unittest
from pathlib import Path

path=Path(__file__).resolve().parents[1]/'skills/superanalyst/scripts/forecast_archive.py'
spec=importlib.util.spec_from_file_location('forecast_archive',path)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

def fixture():
    def picked(pick):return {'pick':pick,'confidence':'medium','status':'provisional','supporting_evidence':['Synthetic evidence'],'contradicting_evidence':[],'abstain_reason':None}
    observe={'pick':None,'confidence':None,'status':'observasi','supporting_evidence':[],'contradicting_evidence':['Synthetic conflicting evidence'],'abstain_reason':'Insufficient support'}
    return {'schema_version':'qualitative-forecast-v2','as_of':'2026-01-01T10:00:00Z','recorded_at':'2026-01-01T10:00:00Z','forecasts':[{'match_id':'synthetic-1','kickoff_at':'2026-01-01T20:00:00Z','score_scenario':[1,1],'probabilities':None,'targets':{'1x2':picked('H'),'btts':picked(True),'total_2_5':observe}}]}

class QualitativeArchiveTests(unittest.TestCase):
    def test_grade_keeps_abstention_and_does_not_edit_input(self):
        data=fixture();original=copy.deepcopy(data)
        result=module.grade(data,[{'match_id':'synthetic-1','scope':'90m','status':'completed','home_goals':2,'away_goals':1}])
        self.assertEqual(result['metrics']['1x2']['correct'],1)
        self.assertEqual(result['metrics']['btts']['correct'],1)
        self.assertEqual(result['metrics']['total_2_5']['evaluated'],0)
        self.assertEqual(data,original)
    def test_rejects_forecast_after_kickoff(self):
        data=fixture();data['recorded_at']='2026-01-01T21:00:00Z'
        with self.assertRaises(ValueError):module.validate(data)
    def test_rejects_new_source_after_cutoff(self):
        data=fixture();data['forecasts'][0]['source_retrieved_at']=['2026-01-01T11:00:00Z']
        with self.assertRaises(ValueError):module.validate(data)
    def test_does_not_allow_draw_to_hide_behind_observation(self):
        data=fixture();data['forecasts'][0]['targets']['1x2'].update(pick='D',status='observasi')
        with self.assertRaises(ValueError):module.validate(data)
    def test_integer_is_not_a_boolean_btts_pick(self):
        data=fixture();data['forecasts'][0]['targets']['btts']['pick']=1
        with self.assertRaises(ValueError):module.validate(data)
    def test_duplicate_match_and_non_90m_outcome_are_rejected(self):
        data=fixture();data['forecasts'].append(copy.deepcopy(data['forecasts'][0]))
        with self.assertRaises(ValueError):module.validate(data)
        with self.assertRaises(ValueError):module.grade(fixture(),[{'match_id':'synthetic-1','scope':'120m','status':'completed','home_goals':2,'away_goals':1}])
