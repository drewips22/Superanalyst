"""Read-only verification of the portable beta-v2 delivery.

Uses frozen rates/quarterly parameters, independently recomputes score losses and
denominators, and never edits a prediction. Full original training data quality
and historical availability are not proved by an arithmetic replay.
"""
import argparse
import hashlib
import json
import math
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'model'))
from beta_engine import decide, fingerprint, hybrid_decide, numerical_probabilities
from vendor import portable


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def sha(path):
    with path.open('rb') as h:
        return hashlib.file_digest(h, 'sha256').hexdigest()


def close(x, y):
    if isinstance(x, dict):
        assert set(x) == set(y)
        for k in x: close(x[k], y[k])
    elif isinstance(x, list):
        assert len(x) == len(y)
        for a, b in zip(x, y): close(a, b)
    elif isinstance(x, (int, float)) and not isinstance(x, bool):
        assert abs(x - y) < 1e-10, (x, y)
    else:
        assert x == y, (x, y)


def metrics(records, key):
    chosen = [r for r in records if r['focuses'][key] is not None]
    correct = sum(r['focuses'][key]['pick'] == r['actual'][r['focuses'][key]['target']] for r in chosen)
    return {'considered': len(records), 'issued': len(chosen), 'correct': correct,
            'coverage': len(chosen) / len(records) if records else None,
            'accuracy': correct / len(chosen) if chosen else None}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-originals', action='store_true')
    args = p.parse_args()
    manifest = read(ROOT / 'bundle-manifest.json')
    for name, expected in manifest['files_sha256'].items():
        assert sha(ROOT / name) == expected, ('bundle file', name)
    selection = read(ROOT / 'artifacts/focus-selection.json')
    for name, expected in selection['code_sha256'].items():
        assert sha(ROOT / 'model' / name.replace('\\', '/')) == expected, ('frozen code', name)
    old_selection = read(ROOT / 'data/base-selection.json')['selected']
    calibration = read(ROOT / 'data/base-calibration.json')['calibrators']
    replay = read(ROOT / 'data/historical-replay-inputs.json')
    evaluation = read(ROOT / 'artifacts/historical-evaluation.json')
    evaluation_by_id = {r['match_id']: r for r in evaluation['rows']}
    protocol = read(ROOT / 'model/protocol.json')
    selection_records = []
    rate_pairs = 0
    for r in replay:
        variants = {v: {} for v in ('pooled5', 'selected_raw', 'calibrated')}
        quarter = f"{r['date'][:4]}-{((int(r['date'][5:7])-1)//3)*3+1:02d}-01"
        for mid, saved in r['probabilities'].items():
            rates = saved['rates']
            if mid != 'pooled5':
                model = read(ROOT / 'data/quarterly-fits' / mid / (quarter + '.json'))
                assert model['latest_training_date'] <= (date.fromisoformat(quarter) - timedelta(days=3)).isoformat()
                expected = []
                for side, other in (('home', 'away'), ('away', 'home')):
                    eta = (model['intercept'] + model['attack'].get(r[side], 0) +
                           model['defense'].get(r[other], 0) + model['competition'].get(r['competition'], 0))
                    if side == 'home' and not r['neutral']: eta += model['home_advantage']
                    expected.append(min(12, max(.05, math.exp(eta))))
                close(expected, rates)
            recomputed = portable.goal_probabilities(*rates)
            for key in ('1x2', 'btts', 'over_2_5'): close(recomputed[key], saved[key])
            rate_pairs += 1
        for t, key in [('1x2', '1x2'), ('btts', 'btts'), ('total_2_5', 'over_2_5')]:
            for v in variants:
                mid = 'pooled5' if v == 'pooled5' else old_selection[key]
                q = r['probabilities'][mid][key]
                if v == 'calibrated': q = portable.calibrate(q, calibration[key])
                variants[v][t] = dict(zip(('H', 'D', 'A'), q)) if t == '1x2' else (
                    {'over': q, 'under': 1 - q} if t == 'total_2_5' else q)
        y = {'1x2': ('H', 'D', 'A')[r['actual']['1x2']], 'btts': bool(r['actual']['btts']),
             'total_2_5': 'over' if r['actual']['over_2_5'] else 'under'}
        if r['date'] <= '2023-12-31':
            selection_records.append({'actual': y, 'variants': variants})
        else:
            saved = evaluation_by_id[r['match_id']]
            close(variants, saved['variants'])
            close(y, saved['actual'])
            close(decide(variants['calibrated'], selection['selected_policy']), saved['decision'])
    assert len(selection_records) == selection['n'] == 410
    candidate_metrics = []
    for candidate in selection['all_candidates']:
        records = [{'actual': r['actual'], 'focuses': {'x': decide(r['variants']['calibrated'], candidate['policy'])['focus']}}
                   for r in selection_records]
        score = metrics(records, 'x')
        for key in score: close(score[key], candidate['metrics'][key])
        candidate_metrics.append((candidate['policy'], score))
    eligible = [(policy, score) for policy, score in candidate_metrics if score['coverage'] >= protocol['minimum_focus_coverage']]
    best = min(eligible, key=lambda r: (-r[1]['accuracy'], -r[1]['coverage'], r[0]['id']))[0]
    assert best == selection['selected_policy']
    for group_name, group in evaluation['groups'].items():
        records = [r for r in evaluation['rows'] if group_name == 'all_UEFA' or
                   (group_name == 'UNL_league_phase' and r['unl_league_phase']) or r['date'].startswith(group_name)]
        assert len(records) == group['n']
        for variant in group['focus_metrics']:
            for key, value in metrics(records, variant).items(): close(value, group['focus_metrics'][variant][key])
        for variant in ('pooled5', 'selected_raw', 'calibrated'):
            for t in ('1x2', 'btts', 'total_2_5'):
                brier = logs = 0.
                for r in records:
                    q, y = r['variants'][variant], r['actual'][t]
                    if t == '1x2':
                        brier += math.fsum((q[t][c] - (c == y)) ** 2 for c in ('H', 'D', 'A'))
                        logs -= math.log(max(1e-15, min(1 - 1e-15, q[t][y])))
                    else:
                        prob = q[t] if t == 'btts' else q[t]['over']
                        label = int(y) if t == 'btts' else int(y == 'over')
                        brier += (prob - label) ** 2
                        prob = max(1e-15, min(1 - 1e-15, prob))
                        logs -= label * math.log(prob) + (1 - label) * math.log(1 - prob)
                expected = group['probability_metrics'][variant][t]
                close(brier / len(records), expected['brier']); close(logs / len(records), expected['log_loss'])
    november = read(ROOT / 'artifacts/november-posthoc-evaluation.json')
    pairs = 0
    samples = 0
    for day in ('2026-11-14', '2026-11-15', '2026-11-16'):
        inputs = read(ROOT / f'artifacts/november-inputs-{day}.json')
        package = read(ROOT / f'artifacts/model-package-{day}.json')
        snapshot = read(ROOT / f'artifacts/november-reconstruction-{day}.json')
        assert snapshot['mode'] == 'retrospective_reconstruction' and 'recorded_at' not in snapshot
        payload = dict(snapshot); sid = payload.pop('snapshot_id')
        assert sid == fingerprint(payload)[:32]
        assert snapshot['input_sha256'] == fingerprint(inputs)
        input_by_id = {f['match_id']: f for f in inputs['fixtures']}
        for r in snapshot['rows']:
            f = input_by_id[r['match_id']]
            numeric = numerical_probabilities(package, f)
            close(numeric['probabilities'], r['probabilities'])
            close(decide(numeric['probabilities'], best), r['decision'])
            close(hybrid_decide(f['main'], numeric['probabilities'], best), r['hybrid'])
            assert r['result_90m'] is None and f['main']['result_90m'] is None
            assert not r['quality_issues']
            assert datetime.fromisoformat(snapshot['reconstructed_at']) > datetime.fromisoformat(f['kickoff_at'])
            samples += sum(mc['samples'] for mc in r['raw_mc_by_recipe'].values())
            pairs += 1
    primary = [r for r in november['rows'] if r['in_original_primary_comparison']]
    for key in ('main', 'beta_v1', 'beta_v2', 'hybrid'):
        for k, value in metrics(primary, key).items(): close(value, november['groups']['primary_original_22']['focus'][key][k])
    protected_path = ROOT / 'artifacts/protected-before.json'
    protected = read(protected_path)['files'] if protected_path.exists() else {}
    if args.check_originals and not protected_path.exists():
        raise ValueError('Original local-path manifest is private; this public copy verifies bundled artifacts only.')
    checked = 0
    if args.check_originals:
        for name, expected in protected.items():
            assert sha(Path(name)) == expected, ('protected original changed', name)
            checked += 1
    result = {'status': 'passed', 'bundle_files_checked': len(manifest['files_sha256']),
              'historical_rows_replayed': len(replay), 'historical_goal_rate_pairs': rate_pairs,
              'selection_rows': len(selection_records), 'evaluation_rows': len(evaluation['rows']),
              'november_reconstructions_replayed': pairs, 'raw_mc_samples_archived': samples,
              'protected_original_files_checked': checked,
              'interpretation': 'Reproducibility and arithmetic checks, not new real-match accuracy evidence.'}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
