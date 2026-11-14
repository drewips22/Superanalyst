import copy
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'skills/superanalyst/scripts'
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location('decision_journal', SCRIPTS / 'decision_journal.py')
journal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(journal)


def fixture():
    def picked(value):
        return {'pick': value, 'confidence': 'medium', 'status': 'provisional',
                'supporting_evidence': ['Synthetic evidence'], 'contradicting_evidence': [], 'abstain_reason': None}
    observe = {'pick': None, 'confidence': None, 'status': 'observasi',
               'supporting_evidence': [], 'contradicting_evidence': [], 'abstain_reason': 'Synthetic uncertainty'}
    f = {'schema_version': 'qualitative-forecast-v2', 'as_of': '2026-01-01T10:00:00Z',
         'recorded_at': '2026-01-01T10:00:00Z', 'forecasts': [
             {'match_id': 'synthetic-1', 'kickoff_at': '2026-01-01T20:00:00Z',
              'analysis_method': 'synthetic-baseline', 'score_scenario': [1, 1], 'focus_target': '1x2',
              'probabilities': None, 'result_90m': None,
              'targets': {'1x2': picked('H'), 'btts': picked(True), 'total_2_5': observe}}]}
    i = {'as_of': f['as_of'], 'profile': 'competitive', 'facts': {'label': 'Synthetic input, not a real match'},
         'sources': [{'id': 'old', 'url': 'https://example.com/preview',
                      'available_at': '2026-01-01T09:00:00Z', 'retrieved_at': '2026-01-01T09:30:00Z'}]}
    return f, i


def record(f, i, previous=None, review=None, now='2026-01-01T10:01:00Z'):
    with patch.object(journal, 'utc_now', return_value=now):
        return journal.build_record(f, i, previous, review)


def later(f, i):
    f, i = copy.deepcopy(f), copy.deepcopy(i)
    f['as_of'] = i['as_of'] = '2026-01-01T11:00:00Z'
    return f, i


def review(target='btts', kind='reassessment', ids=None):
    return {'intentional_reassessment': True, 'changes': [
        {'match_id': 'synthetic-1', 'target': target, 'kind': kind,
         'source_ids': ids or ['old'], 'reason': 'Synthetic explicit review of conflicting evidence'}]}


class DecisionJournalTests(unittest.TestCase):
    def test_real_recording_time_replaces_claim_without_mutating_inputs(self):
        f, i = fixture(); original = copy.deepcopy(f)
        r = record(f, i)
        self.assertEqual(r['recorded_at'], '2026-01-01T10:01:00Z')
        self.assertEqual(f, original)
        self.assertTrue(journal.validate_record(r)['valid'])

    def test_late_recording_cannot_claim_pre_kickoff_freeze(self):
        f, i = fixture()
        with self.assertRaises(ValueError):
            record(f, i, now='2026-01-01T20:03:00Z')

    def test_exclusive_output_keeps_original_file(self):
        f, i = fixture(); r = record(f, i)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'nested/journal.json'
            with patch.object(journal, 'utc_now', return_value='2026-01-01T10:02:00Z'):
                saved = journal.write_new(path, r); before = path.read_bytes()
                with self.assertRaises(FileExistsError): journal.write_new(path, r)
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(saved['recorded_at'], '2026-01-01T10:02:00Z')
            self.assertEqual(r['recorded_at'], '2026-01-01T10:01:00Z')

    def test_delayed_save_after_kickoff_is_rejected(self):
        f, i = fixture(); r = record(f, i)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'late.json'
            with patch.object(journal, 'utc_now', return_value='2026-01-01T20:03:00Z'):
                with self.assertRaises(ValueError): journal.write_new(path, r)
            self.assertFalse(path.exists())

    def test_identical_inputs_reuse_exact_decisions_and_timestamp(self):
        f, i = fixture(); r = record(f, i)
        reused = journal.reuse(r, dict(reversed(list(i.items()))))
        self.assertEqual(reused, r['forecast'])
        reused['forecasts'][0]['score_scenario'] = [9, 9]
        self.assertEqual(r['forecast']['forecasts'][0]['score_scenario'], [1, 1])

    def test_changed_input_cannot_silently_reuse_old_snapshot(self):
        f, i = fixture(); r = record(f, i); i['facts']['label'] = 'Different synthetic evidence'
        with self.assertRaises(ValueError): journal.reuse(r, i)

    def test_target_or_confidence_change_needs_review(self):
        f, i = fixture(); old = record(f, i); f, i = later(f, i)
        f['forecasts'][0]['targets']['btts']['confidence'] = 'low'
        with self.assertRaises(ValueError): record(f, i, old, now='2026-01-01T11:01:00Z')

    def test_intentional_reassessment_is_a_separate_snapshot(self):
        f, i = fixture(); old = record(f, i); old_copy = copy.deepcopy(old); f, i = later(f, i)
        f['forecasts'][0]['targets']['btts']['pick'] = False
        r = record(f, i, old, review(), now='2026-01-01T11:01:00Z')
        self.assertEqual(old, old_copy)
        self.assertEqual(r['previous_sha256'], old['sha256'])
        self.assertEqual(r['changes'][0]['before']['pick'], True)
        self.assertEqual(r['changes'][0]['after']['pick'], False)

    def test_reassessment_requires_deliberate_flag(self):
        f, i = fixture(); old = record(f, i); f, i = later(f, i)
        f['forecasts'][0]['targets']['btts']['pick'] = False
        change = review(); change.pop('intentional_reassessment')
        with self.assertRaises(ValueError): record(f, i, old, change, now='2026-01-01T11:01:00Z')

    def test_old_article_retrieved_again_is_not_new_information(self):
        f, i = fixture(); old = record(f, i); f, i = later(f, i)
        i['sources'][0]['retrieved_at'] = '2026-01-01T10:50:00Z'
        f['forecasts'][0]['targets']['btts']['pick'] = False
        with self.assertRaises(ValueError):
            record(f, i, old, review(kind='new_information'), now='2026-01-01T11:01:00Z')

    def test_lineup_change_needs_delta_then_accepts_new_evidence(self):
        f, i = fixture(); old = record(f, i); f, i = later(f, i)
        i['sources'].append({'id': 'xi', 'url': 'https://example.com/official-xi',
                             'available_at': '2026-01-01T10:30:00Z', 'retrieved_at': '2026-01-01T10:40:00Z'})
        f['forecasts'][0]['targets']['btts']['confidence'] = 'low'
        change = review(kind='lineup_confirmation', ids=['xi'])
        with self.assertRaises(ValueError): record(f, i, old, change, now='2026-01-01T11:01:00Z')
        change['changes'][0]['lineup_delta'] = [{'team': 'away', 'player': 'Synthetic striker',
                                               'expected': 'Projected starter', 'confirmed': 'Bench',
                                               'impact': 'Less support for away scoring'}]
        self.assertEqual(len(record(f, i, old, change, now='2026-01-01T11:01:00Z')['changes']), 1)

    def test_after_cutoff_source_is_rejected(self):
        f, i = fixture(); i['sources'][0]['retrieved_at'] = '2026-01-01T10:30:00Z'
        with self.assertRaises(ValueError): record(f, i)

    def test_focus_cannot_point_to_observation(self):
        f, i = fixture(); f['forecasts'][0]['focus_target'] = 'total_2_5'
        with self.assertRaises(ValueError): record(f, i)

    def test_changed_focus_needs_its_own_review(self):
        f, i = fixture(); old = record(f, i); f, i = later(f, i)
        f['forecasts'][0]['focus_target'] = 'btts'
        with self.assertRaises(ValueError): record(f, i, old, now='2026-01-01T11:01:00Z')
        r = record(f, i, old, review(target='focus_target'), now='2026-01-01T11:01:00Z')
        self.assertEqual(r['changes'][0]['before'], '1x2')

    def test_friendlies_require_two_history_views_and_squad_context(self):
        f, i = fixture(); i['profile'] = 'friendly'
        with self.assertRaises(ValueError): record(f, i)
        team = {'last_competitive_at': '2025-01-01T10:00:00Z', 'recent_friendlies_reviewed': True,
                'history_representativeness': 'Old competitive sample; recent synthetic friendlies reviewed separately',
                'lineup_status': 'projected'}
        i['friendly_context'] = {'synthetic-1': {'home': team, 'away': copy.deepcopy(team),
                                               'substitution_rules': {'status': 'unknown', 'maximum': None}}}
        r = record(f, i)
        self.assertEqual(r['context_flags'][0]['competitive_history_age_days'], 365)
        self.assertEqual(r['forecast']['forecasts'][0]['targets'], f['forecasts'][0]['targets'])

    def test_focus_and_coverage_grade_without_hiding_abstentions(self):
        f, i = fixture(); r = record(f, i)
        outcomes = [{'match_id': 'synthetic-1', 'scope': '90m', 'status': 'completed', 'home_goals': 0, 'away_goals': 0}]
        before = copy.deepcopy(r); g = journal.grade(r, outcomes)
        self.assertEqual(g['focus'], {'correct': 0, 'evaluated': 1, 'published': 1})
        self.assertEqual(g['metrics']['total_2_5']['observations'], 1)
        self.assertEqual(g['metrics']['total_2_5']['evaluated'], 0)
        self.assertEqual(g['metrics']['1x2']['considered'], 1)
        self.assertEqual(r, before)

    def test_scope_changes_cannot_silently_remove_a_match(self):
        f, i = fixture(); extra = copy.deepcopy(f['forecasts'][0]); extra['match_id'] = 'synthetic-2'
        f['forecasts'].append(extra); old = record(f, i); f, i = later(f, i); f['forecasts'].pop()
        with self.assertRaises(ValueError): record(f, i, old, now='2026-01-01T11:01:00Z')
        change = {'changes': [{'match_id': 'synthetic-2', 'target': 'scope', 'kind': 'scope_change',
                               'reason': 'Synthetic second match handled in its own snapshot'}]}
        r = record(f, i, old, change, now='2026-01-01T11:01:00Z')
        self.assertEqual(len(old['forecast']['forecasts']), 2)
        self.assertEqual(r['changes'][0]['after'], False)

    def test_method_change_requires_separate_experiment(self):
        f, i = fixture(); old = record(f, i); f, i = later(f, i)
        f['forecasts'][0]['analysis_method'] = 'another-synthetic-model'
        with self.assertRaises(ValueError): record(f, i, old, now='2026-01-01T11:01:00Z')

    def test_checksum_detects_changed_pick(self):
        f, i = fixture(); r = record(f, i)
        r['forecast']['forecasts'][0]['targets']['1x2']['pick'] = 'A'
        with self.assertRaises(ValueError): journal.validate_record(r)

    def test_target_outcomes_cannot_enter_recorded_forecast(self):
        f, i = fixture(); f['forecasts'][0]['result_90m'] = [2, 0]
        with self.assertRaises(ValueError): record(f, i)

    def test_revision_clock_must_move_forward(self):
        f, i = fixture(); old = record(f, i)
        with self.assertRaises(ValueError): record(f, i, old)


if __name__ == '__main__':
    unittest.main()
