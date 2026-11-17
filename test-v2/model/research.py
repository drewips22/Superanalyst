"""Select focus rules chronologically, then grade the later historical block.

Reuses a previously reviewed, frozen national-team study. This is an auditable
historical reanalysis, not a newly blind test and not a prospective forecast.
"""
import argparse
import math
import random
from collections import defaultdict
from pathlib import Path

from beta_engine import (TARGETS, CLASSES, choose_focus, decide, directions,
                         event_probability, read, sha, utcnow, write_new)
from vendor import portable

HERE = Path(__file__).resolve().parent
KEY = {'1x2': '1x2', 'btts': 'btts', 'total_2_5': 'over_2_5'}


def code_hashes():
    return {str(p.relative_to(HERE)): sha(p) for p in sorted(HERE.rglob('*'))
            if p.is_file() and p.suffix in ('.py', '.json') and '__pycache__' not in p.parts
            and 'examples' not in p.parts and 'tests' not in p.parts}


def probabilities(row, selection, calibration, variant):
    out = {}
    for t in TARGETS:
        key = KEY[t]
        mid = 'pooled5' if variant == 'pooled5' else selection['selected'][key]
        value = row['probabilities'][mid][key]
        if variant == 'calibrated':
            value = portable.calibrate(value, calibration['calibrators'][key])
        if t == '1x2':
            out[t] = dict(zip(CLASSES, value))
        elif t == 'total_2_5':
            out[t] = {'over': value, 'under': 1 - value}
        else:
            out[t] = value
    return out


def actual(row):
    return {'1x2': CLASSES[row['actual']['1x2']], 'btts': bool(row['actual']['btts']),
            'total_2_5': 'over' if row['actual']['over_2_5'] else 'under'}


def focus_score(records):
    active = [r for r in records if r['focus'] is not None]
    correct = sum(r['focus']['pick'] == r['actual'][r['focus']['target']] for r in active)
    return {'considered': len(records), 'issued': len(active), 'correct': correct,
            'coverage': len(active) / len(records) if records else None,
            'accuracy': correct / len(active) if active else None,
            'correct_per_considered_fixture': correct / len(records) if records else None,
            'by_target': {t: {'issued': sum(r['focus']['target'] == t for r in active),
                              'correct': sum(r['focus']['target'] == t and
                                             r['focus']['pick'] == r['actual'][t] for r in active)}
                          for t in TARGETS}}


def probability_loss(p, y, t):
    clip = lambda q: min(1 - 1e-15, max(1e-15, q))
    if t == '1x2':
        return {'brier': sum((p[t][c] - int(y[t] == c)) ** 2 for c in CLASSES),
                'log_loss': -math.log(clip(p[t][y[t]]))}
    q = p[t] if t == 'btts' else p[t]['over']
    label = int(y[t]) if t == 'btts' else int(y[t] == 'over')
    return {'brier': (q - label) ** 2,
            'log_loss': -label * math.log(clip(q)) - (1 - label) * math.log(clip(1 - q))}


def probability_scores(records):
    out = {}
    for t in TARGETS:
        losses = [probability_loss(r['probabilities'], r['actual'], t) for r in records]
        active = [(directions(r['probabilities'])[t], r['actual'][t]) for r in records]
        active = [(p, y) for p, y in active if p is not None]
        bins = defaultdict(list)
        labels = CLASSES if t == '1x2' else ('yes',)
        for r in records:
            for c in labels:
                if t == '1x2':
                    q, y = r['probabilities'][t][c], int(r['actual'][t] == c)
                else:
                    q = r['probabilities'][t] if t == 'btts' else r['probabilities'][t]['over']
                    y = int(r['actual'][t]) if t == 'btts' else int(r['actual'][t] == 'over')
                bins[c, min(9, int(q * 10))].append((q, y))
        out[t] = {'n': len(records),
                  **{m: sum(r[m] for r in losses) / len(losses) if losses else None
                     for m in ('log_loss', 'brier')},
                  'unthresholded_direction_issued': len(active),
                  'unthresholded_direction_accuracy': sum(p == y for p, y in active) / len(active) if active else None,
                  'reliability': {c: [{'bin': [i / 10, (i + 1) / 10], 'n': len(bins[c, i]),
                                      'mean_probability': sum(q for q, _ in bins[c, i]) / len(bins[c, i]) if bins[c, i] else None,
                                      'frequency': sum(y for _, y in bins[c, i]) / len(bins[c, i]) if bins[c, i] else None}
                                     for i in range(10)] for c in labels}}
    return out


def bootstrap(month_values, replicates, seed):
    buckets = list(month_values.values())
    if not buckets:
        return {'difference': None, 'ci95': None, 'months': 0}
    rng = random.Random(seed)
    samples = []
    for _ in range(replicates):
        drawn = [buckets[rng.randrange(len(buckets))] for _ in buckets]
        samples.append(sum(sum(b) for b in drawn) / sum(len(b) for b in drawn))
    samples.sort()
    return {'difference': sum(sum(b) for b in buckets) / sum(map(len, buckets)),
            'ci95': [samples[int(.025 * (replicates - 1))], samples[int(.975 * (replicates - 1))]],
            'months': len(buckets), 'unit': 'calendar_month', 'replicates': replicates}


def source_audit(source):
    manifest = read(source / 'final-manifest-v1.json')
    for name, digest in manifest['files'].items():
        if sha(source / name) != digest:
            raise ValueError(f'Frozen research output changed: {name}')
    selection = read(source / 'selection-v1.json')
    for name, digest in selection['input_hashes'].items():
        if sha(source / name) != digest:
            raise ValueError(f'Frozen research input changed: {name}')
    calibration = read(source / 'calibration-v1.json')
    if calibration['selection_sha256'] != sha(source / 'selection-v1.json'):
        raise ValueError('Frozen calibration lineage mismatch')
    return selection, calibration


def prepared_rows(source, start, end):
    selection, calibration = source_audit(source)
    saved = read(source / 'test-predictions.json')['rows']
    rows = [r for r in saved if r['primary'] and start <= r['date'] <= end]
    return [{**{k: r[k] for k in ('match_id', 'date', 'home', 'away', 'unl_league_phase')},
             'actual': actual(r), 'variants': {v: probabilities(r, selection, calibration, v)
                                             for v in ('pooled5', 'selected_raw', 'calibrated')}} for r in rows]


def select(source, run):
    protocol = read(HERE / 'protocol.json')
    start, end = protocol['focus_selection_period']
    rows = prepared_rows(source, start, end)
    candidates = []
    for policy in protocol['focus_candidates']:
        records = [{'actual': r['actual'], 'focus': decide(r['variants']['calibrated'], policy)['focus']} for r in rows]
        candidates.append({'policy': policy, 'metrics': focus_score(records)})
    eligible = [c for c in candidates if c['metrics']['coverage'] >= protocol['minimum_focus_coverage']]
    if not eligible:
        raise ValueError('No focus policy meets the locked coverage floor')
    chosen = min(eligible, key=lambda c: (-c['metrics']['accuracy'], -c['metrics']['coverage'], c['policy']['id']))
    record = {'experiment_id': protocol['experiment_id'], 'frozen_at': utcnow(),
              'selection_period': [start, end], 'historical_reanalysis_not_blind': True,
              'n': len(rows), 'selected_policy': chosen['policy'], 'all_candidates': candidates,
              'source_predictions_sha256': sha(source / 'test-predictions.json'),
              'source_calibration_sha256': sha(source / 'calibration-v1.json'),
              'code_sha256': code_hashes(), 'november_2026_used_for_selection': False,
              'later_block_used_for_focus_selection': False}
    write_new(run / 'focus-selection.json', record)
    return record


def evaluate(source, run):
    protocol = read(HERE / 'protocol.json')
    selection = read(run / 'focus-selection.json')
    if selection['code_sha256'] != code_hashes():
        raise ValueError('Code changed after focus selection; create a new experiment')
    if selection['source_predictions_sha256'] != sha(source / 'test-predictions.json') or \
            selection['source_calibration_sha256'] != sha(source / 'calibration-v1.json'):
        raise ValueError('Historical source changed after focus selection')
    start, end = protocol['focus_evaluation_period']
    rows = prepared_rows(source, start, end)
    records = []
    for r in rows:
        choices = {}
        for v, p in r['variants'].items():
            # Original beta-v1 issues the top direction without a 50% 1X2 gate.
            d = directions(p)
            active = [t for t in TARGETS if d[t] is not None]
            t = max(active, key=lambda t: event_probability(p, t, d[t])) if active else None
            choices[v] = {'target': t, 'pick': d[t], 'probability': event_probability(p, t, d[t])} if t else None
        decision = decide(r['variants']['calibrated'], selection['selected_policy'])
        choices['beta_v2'] = decision['focus']
        records.append({**r, 'focuses': choices, 'decision': decision})
    report = {'experiment_id': protocol['experiment_id'], 'evaluated_at': utcnow(),
              'mode': 'historical_reanalysis_not_blind', 'period': [start, end], 'n': len(records),
              'focus_selection_sha256': sha(run / 'focus-selection.json'),
              'source_already_reviewed_in_previous_study': True,
              'selected_policy': selection['selected_policy'], 'groups': {}, 'rows': records,
              'automatic_main_promotion': False}
    for name, subset in [('all_UEFA', records), ('UNL_league_phase', [r for r in records if r['unl_league_phase']]),
                         *[(str(y), [r for r in records if r['date'].startswith(str(y))]) for y in (2024, 2025)]]:
        common = [r for r in subset if r['focuses']['beta_v2'] is not None and r['focuses']['pooled5'] is not None]
        delta_focus = defaultdict(list)
        for r in common:
            new, old = r['focuses']['beta_v2'], r['focuses']['pooled5']
            delta_focus[r['date'][:7]].append(int(new['pick'] == r['actual'][new['target']]) -
                                              int(old['pick'] == r['actual'][old['target']]))
        delta_losses = {}
        for t in TARGETS:
            metric = 'log_loss' if t == '1x2' else 'brier'
            buckets = defaultdict(list)
            for r in subset:
                buckets[r['date'][:7]].append(probability_loss(r['variants']['calibrated'], r['actual'], t)[metric] -
                                                probability_loss(r['variants']['pooled5'], r['actual'], t)[metric])
            delta_losses[t] = {'metric': metric, **bootstrap(buckets, protocol['bootstrap']['replicates'], protocol['bootstrap']['seed'])}
        report['groups'][name] = {
            'n': len(subset),
            'probability_metrics': {v: probability_scores([{'actual': r['actual'], 'probabilities': r['variants'][v]}
                                                         for r in subset]) for v in ('pooled5', 'selected_raw', 'calibrated')},
            'focus_metrics': {v: focus_score([{'actual': r['actual'], 'focus': r['focuses'][v]} for r in subset])
                              for v in ('pooled5', 'selected_raw', 'calibrated', 'beta_v2')},
            'focus_same_active_fixtures': {v: focus_score([{'actual': r['actual'], 'focus': r['focuses'][v]} for r in common])
                                          for v in ('pooled5', 'beta_v2')},
            'paired_monthly_focus_accuracy_difference_new_minus_old': bootstrap(delta_focus, protocol['bootstrap']['replicates'], protocol['bootstrap']['seed']),
            'paired_monthly_probability_loss_new_minus_old': delta_losses}
    write_new(run / 'historical-evaluation.json', report)
    return {name: {'n': group['n'], 'focus': group['focus_metrics'],
                   'probability_metrics': {v: {t: {m: scores[m] for m in ('n', 'log_loss', 'brier')}
                                                for t, scores in by_target.items()}
                                           for v, by_target in group['probability_metrics'].items()}}
            for name, group in report['groups'].items()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=('select', 'evaluate'))
    p.add_argument('--source', required=True, type=Path)
    p.add_argument('--run', required=True, type=Path)
    args = p.parse_args()
    # Bootstrap options are namespaced in the protocol, not optimization inputs.
    print(__import__('json').dumps(select(args.source, args.run) if args.phase == 'select'
                                  else evaluate(args.source, args.run), indent=2))


if __name__ == '__main__':
    main()
