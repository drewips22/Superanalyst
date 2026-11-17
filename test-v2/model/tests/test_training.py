"""Real optimizer and leakage checks using clearly synthetic training scores."""
import copy
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
try:
    import train
except ModuleNotFoundError as exc:
    if exc.name not in ('scipy', 'numpy'):
        raise
    train = None


def rows():
    return [{'match_id': f'synthetic-{i}', 'date': f'2024-{1 + i // 4:02d}-{1 + i % 4:02d}',
             'home': 'A' if i % 2 else 'B', 'away': 'B' if i % 2 else 'A',
             'home_goals': i % 4, 'away_goals': i % 3,
             'scope': '90m', 'neutral': False, 'competitive': True,
             'competition': 'Test', 'source_url': 'https://example.invalid/synthetic',
             'normal_time_verification': 'synthetic_example_not_real_match'} for i in range(24)]


@unittest.skipIf(train is None, 'Fitting requires NumPy/SciPy; inference tests remain standard-library only')
class Training(unittest.TestCase):
    def test_duplicate_and_conflicting_archives(self):
        dataset = rows()
        self.assertEqual(len(train.merge_rows(dataset, [dataset[0]])), len(dataset))
        bad = dict(dataset[0], home_goals=99)
        with self.assertRaises(ValueError): train.merge_rows(dataset, [bad])
        bad = dict(dataset[0], scope='120m')
        with self.assertRaises(ValueError): train.merge_rows([], [bad])

    def test_later_labels_cannot_change_a_prior_fit(self):
        dataset = rows()
        spec = {'id': 'synthetic', 'kind': 'strength', 'half_life_days': 730,
                'form_window': None, 'include_friendlies': False}
        protocol = {'history_guard_days': 3, 'training_lookback_years': 6,
                    'fixed_regularization': {'team': 20, 'competition': 20, 'form': 20}}
        cutoff = date(2024, 5, 1).toordinal()

        def fit(records):
            merged = train.merge_rows(records, [])
            features = {r['match_id']: {'history_cutoff_ordinal': r['ordinal'] - 3} for r in merged}
            return train.national_models.fit(merged, features, spec, cutoff, protocol)

        first = fit(dataset)
        changed = copy.deepcopy(dataset)
        for row in changed:
            if row['date'] >= '2024-05-01':
                row['home_goals'], row['away_goals'] = 12, 11
        second = fit(changed)
        self.assertEqual(first, second)
        self.assertLessEqual(first['latest_training_date'], '2024-04-28')


if __name__ == '__main__':
    unittest.main()
