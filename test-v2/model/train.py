"""Refit separate national-team beta recipes; never update frozen model packages."""
import argparse
import copy
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

# Use existing research libraries only when explicitly supplied by the caller.
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
if os.environ.get('SUPERANALYST_RESEARCH_LIBS'):
    sys.path.insert(0, os.environ['SUPERANALYST_RESEARCH_LIBS'])

from beta_engine import VERSION, read, sha, timestamp, utcnow, write_new
from vendor import national_models


def load_rows(path):
    with Path(path).open(encoding='utf-8') as handle:
        return [json.loads(line) for line in handle if line.strip()]


def merge_rows(base, updates):
    merged = {}
    for r in [*base, *updates]:
        r = copy.deepcopy(r)
        if r.get('scope') != '90m' or type(r.get('neutral')) is not bool or \
                type(r.get('competitive')) is not bool:
            raise ValueError('Training requires explicit normal-time/venue/competition scope')
        if not r.get('source_url') or not r.get('normal_time_verification'):
            raise ValueError('Training score requires source and normal-time provenance')
        if any(type(r[k]) is not int or r[k] < 0 for k in ('home_goals', 'away_goals')):
            raise ValueError('Invalid training goals')
        if r['home'] == r['away']:
            raise ValueError('Teams must differ')
        r['ordinal'] = date.fromisoformat(r['date']).toordinal()
        key = (r['date'], r['home'], r['away'])
        if key in merged:
            previous = merged[key]
            fields = ('home_goals', 'away_goals', 'competition', 'neutral', 'competitive')
            if any(r[k] != previous[k] for k in fields):
                raise ValueError(f'Conflicting archived result: {key}')
            continue
        merged[key] = r
    rows = sorted(merged.values(), key=lambda r: (r['date'], r['match_id']))
    if len({r['match_id'] for r in rows}) != len(rows):
        raise ValueError('Match ID collision across distinct training fixtures')
    return rows


def refit(base_path, template_path, original_protocol_path, cutoff, output, updates_path=None):
    as_of = date.fromisoformat(cutoff)
    created = utcnow()
    if as_of > timestamp(created).date():
        raise ValueError('Fit date cannot be in the future')
    protocol = read(original_protocol_path)
    template = read(template_path)
    updates = load_rows(updates_path) if updates_path else []
    rows = merge_rows(load_rows(base_path), updates)
    # No-form selected recipes never read a form vector. Still enforce the
    # original date-only availability guard for every training feature.
    features = {r['match_id']: {'history_cutoff_ordinal': r['ordinal'] - protocol['history_guard_days']}
                for r in rows}
    models = {}
    for mid, spec in template['specs'].items():
        if spec.get('form_window') is not None:
            raise ValueError('This version supports the frozen selected no-form recipes only')
        models[mid] = national_models.fit(rows, features, spec, as_of.toordinal(), protocol)
    used = [r for r in rows if as_of.toordinal() - round(365.25 * protocol['training_lookback_years']) <= r['ordinal'] <=
            as_of.toordinal() - protocol['history_guard_days']]
    latest_by_team = {}
    for r in used:
        if r['competitive']:
            for team in (r['home'], r['away']):
                latest_by_team[team] = {k: r[k] for k in ('date', 'home', 'away', 'home_goals', 'away_goals')}
    package = {
        'model_package_version': VERSION, 'created_at': created,
        'refit_as_of_date': cutoff, 'data_latest_date': max(r['date'] for r in used),
        'date_guard_days': protocol['history_guard_days'],
        'specs': copy.deepcopy(template['specs']), 'fitted_models': models,
        'target_recipes': copy.deepcopy(template['target_recipes']),
        'base_template_sha256': sha(template_path), 'base_data_sha256': sha(base_path),
        'updates_sha256': sha(updates_path) if updates_path else None,
        'original_research_protocol_sha256': sha(original_protocol_path),
        'status': 'experimental_requires_current_team_history_audit',
        'point_in_time_verified': False,
        'training_rows_in_lookback': len(used),
        'training_latest_by_team': latest_by_team,
        'unique_updates_supplied': len(updates),
        'updates_in_training_window': sum(as_of.toordinal() - round(365.25 * protocol['training_lookback_years']) <=
                                         date.fromisoformat(r['date']).toordinal() <= as_of.toordinal() - protocol['history_guard_days'] for r in updates),
        'latest_observed_matches': max(r['date'] for r in rows),
        'partial_update_warning': 'Updates are an explicit supplied subset, not proof the global corpus is complete. Verify all intervening history of both teams before any forecast.',
        'missing_context': ['player minutes', 'XI', 'injuries', 'coaching changes', 'xG', 'market'],
        'joint_distribution_warning': 'Calibrated marginals use separate recipes/calibrators; raw MC is not their joint score distribution.',
        'operational_main_changed': False,
    }
    write_new(output, package)
    return {'output': str(output), 'fit_date': cutoff, 'latest_training_date': package['data_latest_date'],
            'training_counts': {mid: m['training_matches'] for mid, m in models.items()},
            'optimization': {mid: m['optimization'] for mid, m in models.items()}}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-data', type=Path, required=True)
    p.add_argument('--base-package', type=Path, required=True)
    p.add_argument('--base-protocol', type=Path, required=True)
    p.add_argument('--updates', type=Path)
    p.add_argument('--as-of-date', required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    print(json.dumps(refit(a.base_data, a.base_package, a.base_protocol, a.as_of_date,
                           a.output, a.updates), indent=2))


if __name__ == '__main__':
    main()
