"""Behavioral checks; synthetic examples do not establish real-match accuracy."""
import copy
import json
import math
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import beta_engine as e
from vendor import portable

POLICY = {'id': 'test_p55', 'min_probability': .55, 'winner_priority': None}


def values(h=.60, d=.25, yes=.52, over=.53):
    return {'1x2': {'H': h, 'D': d, 'A': 1 - h - d}, 'btts': yes,
            'total_2_5': {'over': over, 'under': 1 - over}}


def main_row():
    return {'targets': {'1x2': {'pick': 'H', 'confidence': 'low'},
                        'btts': {'pick': None, 'confidence': None},
                        'total_2_5': {'pick': 'under', 'confidence': 'medium'}},
            'focus_target': 'total_2_5'}


def synthetic_package(fit_day):
    model = {'spec': {'form_window': None}, 'intercept': math.log(1.1),
             'attack': {'A': .3, 'B': -.2}, 'defense': {'A': -.1, 'B': .2},
             'competition': {'Test': 0.0}, 'home_advantage': .2,
             'latest_training_date': (fit_day - timedelta(days=3)).isoformat()}
    calibrators = {
        '1x2': {'target': '1x2', 'parameters': {'inverse_temperature': 1., 'home_bias': 0., 'draw_bias': 0.}},
        'btts': {'target': 'btts', 'parameters': {'intercept': 0., 'slope': 1.}},
        'over_2_5': {'target': 'over_2_5', 'parameters': {'intercept': 0., 'slope': 1.}}}
    return {'created_at': (datetime.now(timezone.utc) - timedelta(days=1)).isoformat(),
            'refit_as_of_date': fit_day.isoformat(), 'date_guard_days': 3,
            'fitted_models': {'test': model},
            'target_recipes': {t: {'model_id': 'test', 'calibrator': cal} for t, cal in calibrators.items()},
            'training_latest_by_team': {t: {'date': (fit_day - timedelta(days=3)).isoformat()} for t in ('A', 'B')}}


def synthetic_inputs():
    now = datetime.now(timezone.utc)
    as_of = now - timedelta(seconds=1)
    histories = {side: [{'id': f'{side}-{i}', 'date': (as_of.date() - timedelta(days=10 + i)).isoformat(),
                         'gf': 1, 'ga': i % 2, 'scope': '90m'} for i in range(5)] for side in ('home', 'away')}
    f = {'match_id': 'synthetic-test', 'home_key': 'A', 'away_key': 'B',
         'competition_key': 'Test', 'neutral': False, 'kickoff_at': (now + timedelta(days=1)).isoformat(),
         'history': histories, 'main': main_row()}
    audit = {team: {'complete': True, 'source_urls': ['https://example.invalid/synthetic'],
                    'checked_at': as_of.isoformat(), 'latest_match_id': histories[side][0]['id']}
             for team, side in [('A', 'home'), ('B', 'away')]}
    return {'synthetic': True, 'as_of': as_of.isoformat(), 'fixtures': [f], 'history_audit': audit}


class Decisions(unittest.TestCase):
    def test_distribution_identities_known_cases(self):
        p = portable.goal_probabilities(0, 0)
        self.assertEqual(p, {'1x2': [0., 1., 0.], 'btts': 0., 'over_2_5': 0.})
        q = portable.goal_probabilities(1.2, 1.2)
        self.assertAlmostEqual(q['1x2'][0], q['1x2'][2], places=14)
        self.assertAlmostEqual(q['btts'], (1 - math.exp(-1.2)) ** 2, places=14)

    def test_null_observation_at_all_exact_ties(self):
        out = e.decide(values(1/3, 1/3, .5, .5), POLICY)
        self.assertIsNone(out['focus'])
        self.assertTrue(all(r['pick'] is None for r in out['targets'].values()))

    def test_weak_events_are_diagnostics_not_active_picks(self):
        out = e.decide(values(.40, .30, .52, .53), POLICY)
        self.assertEqual(out['raw_directions']['1x2'], 'H')
        self.assertIsNone(out['focus'])
        self.assertIsNone(out['targets']['1x2']['pick'])

    def test_winner_priority_is_explicit_and_cannot_promote_weak_winner(self):
        p = values(.60, .20, .70, .65)
        self.assertEqual(e.decide(p, POLICY)['focus']['target'], 'btts')
        priority = dict(POLICY, winner_priority=.60)
        self.assertEqual(e.decide(p, priority)['focus']['target'], '1x2')
        self.assertEqual(e.decide(values(.58, .20, .70, .65), priority)['focus']['target'], 'btts')

    def test_invalid_probabilities_rejected(self):
        for bad in (float('nan'), float('inf'), -0.01, 1.01, True):
            p = values(); p['btts'] = bad
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                e.decide(p, POLICY)
        p = values(); p['1x2']['H'] = .9
        with self.assertRaises(ValueError): e.decide(p, POLICY)

    def test_hybrid_never_mutates_main_or_creates_main_observation_pick(self):
        main = main_row(); original = copy.deepcopy(main)
        out = e.hybrid_decide(main, values(yes=.9, over=.7), POLICY)
        self.assertEqual(main, original)
        self.assertIsNone(out['targets']['btts']['pick'])
        self.assertIsNone(out['targets']['total_2_5']['pick'])
        self.assertEqual(out['focus']['target'], '1x2')
        self.assertEqual(out['source_main_targets'], original['targets'])

    def test_hybrid_preserves_supported_original_focus(self):
        out = e.hybrid_decide(main_row(), values(.75, .15, over=.4), POLICY)
        self.assertEqual(out['focus']['target'], 'total_2_5')
        self.assertEqual(out['focus_reason'], 'retain_supported_main_focus')

    def test_mc_raw_labels_reproducible_and_decisions_independent_of_samples(self):
        first = e.monte_carlo(1.2, .8, 'synthetic', 'test', 10000)
        self.assertEqual(first, e.monte_carlo(1.2, .8, 'synthetic', 'test', 10000))
        self.assertTrue(first['raw_uncalibrated_scenarios_only'])
        self.assertLess(abs(first['probabilities']['btts'] - portable.goal_probabilities(1.2, .8)['btts']), .025)
        inputs = synthetic_inputs()
        package = synthetic_package(e.timestamp(inputs['as_of']).date())
        with_mc = e.make_snapshot(package, inputs, POLICY, include_mc=True)
        no_mc = e.make_snapshot(package, inputs, POLICY, include_mc=False)
        self.assertEqual(with_mc['rows'][0]['decision'], no_mc['rows'][0]['decision'])
        self.assertEqual(with_mc['rows'][0]['hybrid'], no_mc['rows'][0]['hybrid'])

    def test_opponent_strength_and_home_advantage_change_rates(self):
        model = synthetic_package(datetime.now(timezone.utc).date())['fitted_models']['test']
        home = portable.rates(model, 'A', 'B', 'Test', False)
        neutral = portable.rates(model, 'A', 'B', 'Test', True)
        self.assertGreater(home[0], neutral[0])
        self.assertEqual(home[1], neutral[1])
        model['defense']['B'] += .3
        self.assertGreater(portable.rates(model, 'A', 'B', 'Test', False)[0], home[0])


class Recording(unittest.TestCase):
    def test_success_is_synthetic_and_results_are_empty(self):
        inputs = synthetic_inputs(); before = copy.deepcopy(inputs)
        package = synthetic_package(e.timestamp(inputs['as_of']).date())
        out = e.make_snapshot(package, inputs, POLICY, include_mc=False)
        self.assertEqual(inputs, before)
        self.assertTrue(out['synthetic'])
        self.assertIsNone(out['rows'][0]['result_90m'])
        self.assertIn('recorded_at', out)
        self.assertFalse(out['rows'][0]['one_joint_score_distribution'])

    def test_missing_completeness_audit_forces_observation(self):
        inputs = synthetic_inputs(); inputs.pop('history_audit')
        out = e.make_snapshot(synthetic_package(e.timestamp(inputs['as_of']).date()), inputs, POLICY, include_mc=False)
        row = out['rows'][0]
        self.assertIsNone(row['decision']['focus'])
        self.assertIsNone(row['hybrid']['focus'])
        self.assertTrue(row['quality_issues'])

    def test_future_audit_or_history_is_rejected(self):
        for kind in ('audit', 'history', 'availability'):
            inputs = synthetic_inputs()
            if kind == 'audit': inputs['history_audit']['A']['checked_at'] = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()
            elif kind == 'history': inputs['fixtures'][0]['history']['home'][0]['date'] = '2999-01-01'
            else: inputs['fixtures'][0]['history']['home'][0]['available_at'] = '2999-01-01T00:00:00+00:00'
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                e.make_snapshot(synthetic_package(e.timestamp(inputs['as_of']).date()), inputs, POLICY, include_mc=False)

    def test_rejects_post_kickoff_forecast_and_outcome_input(self):
        for kind in ('past_kickoff', 'outcome', 'duplicate_fixture', 'model_future_training'):
            inputs = synthetic_inputs(); package = synthetic_package(e.timestamp(inputs['as_of']).date())
            if kind == 'past_kickoff': inputs['fixtures'][0]['kickoff_at'] = '2000-01-01T00:00:00+00:00'
            elif kind == 'outcome': inputs['fixtures'][0]['result_90m'] = [2, 0]
            elif kind == 'duplicate_fixture': inputs['fixtures'].append(copy.deepcopy(inputs['fixtures'][0]))
            else: package['fitted_models']['test']['latest_training_date'] = '2999-01-01'
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                e.make_snapshot(package, inputs, POLICY, include_mc=False)

    def test_stale_fit_or_missing_eligible_score_forces_observation(self):
        for kind in ('stale_fit', 'missing_history'):
            inputs = synthetic_inputs(); package = synthetic_package(e.timestamp(inputs['as_of']).date())
            if kind == 'stale_fit':
                package['refit_as_of_date'] = (e.timestamp(inputs['as_of']).date() - timedelta(days=5)).isoformat()
                package['fitted_models']['test']['latest_training_date'] = (e.timestamp(inputs['as_of']).date() - timedelta(days=8)).isoformat()
            else: package['training_latest_by_team'] = {}
            out = e.make_snapshot(package, inputs, POLICY, include_mc=False)
            self.assertIsNone(out['rows'][0]['decision']['focus'])

    def test_immutable_file_and_timezone_boundaries(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'snapshot.json'
            e.write_new(p, {'x': 1})
            with self.assertRaises(FileExistsError): e.write_new(p, {'x': 2})
            self.assertEqual(e.read(p), {'x': 1})
        with self.assertRaises(ValueError): e.timestamp('2026-11-17T10:00:00')

    def test_shared_reverse_game_is_counted_once_and_conflict_rejected(self):
        inputs = synthetic_inputs(); f = inputs['fixtures'][0]
        h, a = f['history']['home'], f['history']['away']
        a[0] = dict(h[0], gf=h[0]['ga'], ga=h[0]['gf'])
        out = e.last5_sensitivity(h, a, inputs['as_of'])
        self.assertEqual(out['unique_matches'], 9)
        self.assertEqual(len(out['runs']), 9)
        self.assertFalse(out['historical_scores_removed_from_model'])
        a[0]['gf'] += 1
        with self.assertRaises(ValueError): e.last5_sensitivity(h, a, inputs['as_of'])


if __name__ == '__main__':
    unittest.main()
