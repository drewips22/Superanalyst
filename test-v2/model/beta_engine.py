"""Separate experimental decisions; never imports outcomes or edits the main model.

Inference needs only Python's standard library. Fitting uses the frozen research
implementation in vendor/national_models.py. Each calibrated marginal retains
its own recipe; Monte Carlo below always describes a RAW recipe, not a joint
distribution of the three calibrated targets.
"""
import copy
import hashlib
import json
import math
import random
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from vendor import portable

TARGETS = ('1x2', 'btts', 'total_2_5')
CLASSES = ('H', 'D', 'A')
EPS = 1e-12
VERSION = 'superanalyst-beta-v2.0.0-experimental'
HYBRID_VERSION = 'superanalyst-hybrid-beta-v1.0.0-experimental'


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def timestamp(value):
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError('Timestamp must include a timezone')
    return parsed


def sha(path):
    with Path(path).open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_new(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False, allow_nan=False)
        handle.write('\n')


def validate_probabilities(values):
    if set(values) != set(TARGETS) or set(values['1x2']) != set(CLASSES):
        raise ValueError('All three target probabilities are required')
    if set(values['total_2_5']) != {'over', 'under'}:
        raise ValueError('Both total-goal sides are required')
    flat = [*values['1x2'].values(), values['btts'], *values['total_2_5'].values()]
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or
           not math.isfinite(v) or not 0 <= v <= 1 for v in flat):
        raise ValueError('Probabilities must be finite and between zero and one')
    if abs(sum(values['1x2'].values()) - 1) > 1e-10:
        raise ValueError('1X2 probabilities must sum to one')
    if abs(sum(values['total_2_5'].values()) - 1) > 1e-10:
        raise ValueError('Over and Under probabilities must sum to one')


def event_probability(values, target, pick):
    if pick is None:
        return None
    if target == 'btts':
        if type(pick) is not bool:
            raise ValueError('BTTS direction must be boolean')
        return values['btts'] if pick else 1 - values['btts']
    if target not in ('1x2', 'total_2_5') or pick not in values[target]:
        raise ValueError('Unknown target direction')
    return values[target][pick]


def directions(values):
    validate_probabilities(values)
    ranked = sorted(CLASSES, key=lambda c: -values['1x2'][c])
    return {
        '1x2': None if values['1x2'][ranked[0]] - values['1x2'][ranked[1]] <= EPS else ranked[0],
        'btts': None if abs(values['btts'] - .5) <= EPS else values['btts'] > .5,
        'total_2_5': None if abs(values['total_2_5']['over'] - .5) <= EPS else
                     ('over' if values['total_2_5']['over'] > .5 else 'under'),
    }


def choose_focus(values, picks, policy):
    minimum = policy['min_probability']
    if not isinstance(minimum, (int, float)) or not .5 <= minimum <= 1:
        raise ValueError('Invalid focus policy threshold')
    eligible = [t for t in TARGETS if picks.get(t) is not None and
                event_probability(values, t, picks[t]) + EPS >= minimum]
    priority = policy['winner_priority']
    if priority is not None and '1x2' in eligible and picks['1x2'] in ('H', 'A') and \
            event_probability(values, '1x2', picks['1x2']) + EPS >= priority:
        focus = '1x2'
    else:
        focus = max(eligible, key=lambda t: event_probability(values, t, picks[t])) if eligible else None
    return ({'target': focus, 'pick': picks[focus],
             'probability': event_probability(values, focus, picks[focus])} if focus else None)


def decide(values, policy):
    """Keep below-threshold directions as diagnostics; publish null active picks."""
    raw = directions(values)
    targets = {}
    for target, pick in raw.items():
        p = event_probability(values, target, pick)
        active = p is not None and p + EPS >= policy['min_probability']
        targets[target] = {'pick': pick if active else None,
                           'status': 'experimental' if active else 'observe',
                           'probability': p,
                           'reason': 'passes_frozen_threshold' if active else
                                     ('exact_direction_tie' if pick is None else 'below_frozen_threshold')}
    active = {t: v['pick'] for t, v in targets.items()}
    return {'raw_directions': raw, 'targets': targets,
            'focus': choose_focus(values, active, policy), 'focus_policy_id': policy['id']}


def hybrid_decide(main, values, policy):
    """Read-only consensus overlay. No probability is attributed to the main model."""
    if set(main['targets']) != set(TARGETS):
        raise ValueError('Main input must contain all target records')
    raw = directions(values)
    targets = {}
    for t in TARGETS:
        original = main['targets'][t]['pick']
        p = event_probability(values, t, original)
        if original is None:
            reason = 'main_observation_preserved'
        elif original != raw[t]:
            reason = 'numerical_direction_disagrees'
        elif p + EPS < policy['min_probability']:
            reason = 'below_frozen_threshold'
        else:
            reason = 'main_direction_and_numerical_support_agree'
        active = reason == 'main_direction_and_numerical_support_agree'
        targets[t] = {'pick': original if active else None,
                      'status': 'experimental' if active else 'observe',
                      'supporting_beta_probability': p, 'reason': reason}
    active = {t: row['pick'] for t, row in targets.items()}
    old_focus = main.get('focus_target')
    if old_focus is not None and old_focus not in TARGETS:
        raise ValueError('Invalid main focus')
    if old_focus and main['targets'][old_focus]['pick'] is None:
        raise ValueError('Main focus cannot point to an observation')
    if old_focus and active[old_focus] is not None:
        focus = {'target': old_focus, 'pick': active[old_focus],
                 'probability': event_probability(values, old_focus, active[old_focus])}
        reason = 'retain_supported_main_focus'
    else:
        focus = choose_focus(values, active, policy)
        reason = 'select_from_supported_main_picks' if focus else 'no_supported_main_pick'
    return {'model_version': HYBRID_VERSION, 'source_main_sha256': fingerprint(main),
            'source_main_focus': old_focus, 'source_main_targets': copy.deepcopy(main['targets']),
            'targets': targets, 'focus': focus, 'focus_reason': reason,
            'probabilities_belong_to': VERSION, 'focus_policy_id': policy['id']}


def numerical_probabilities(package, fixture):
    if type(fixture.get('neutral')) is not bool:
        raise ValueError('Neutral venue must be explicitly true or false')
    by_target = {}
    for t in TARGETS:
        key = 'over_2_5' if t == 'total_2_5' else t
        recipe = package['target_recipes'][key]
        model = package['fitted_models'][recipe['model_id']]
        rates = portable.rates(model, fixture['home_key'], fixture['away_key'],
                               fixture['competition_key'], fixture['neutral'])
        raw = portable.goal_probabilities(*rates)[key]
        calibrated = portable.calibrate(raw, recipe['calibrator'])
        by_target[t] = {'recipe_id': recipe['model_id'], 'goal_rates': rates,
                        'raw': raw, 'calibrated': calibrated}
    over = by_target['total_2_5']['calibrated']
    p = {'1x2': dict(zip(CLASSES, by_target['1x2']['calibrated'])),
         'btts': by_target['btts']['calibrated'], 'total_2_5': {'over': over, 'under': 1 - over}}
    validate_probabilities(p)
    return {'probabilities': p, 'by_target': by_target,
            'calibration': 'frozen_2020_2021_not_proven_current',
            'one_joint_score_distribution': False}


def validate_history(home, away, as_of):
    cutoff = timestamp(as_of)
    merged = {}
    for side, history in (('home', home), ('away', away)):
        if len(history) != 5:
            raise ValueError('Exactly five competitive matches per team are required for the diagnostic')
        seen = set()
        for r in history:
            if r['id'] in seen:
                raise ValueError('Duplicate match inside one team history')
            seen.add(r['id'])
            if r.get('scope') != '90m' or r.get('competitive', True) is not True:
                raise ValueError('History must contain competitive normal-time scores')
            goals = (r['gf'], r['ga']) if side == 'home' else (r['ga'], r['gf'])
            if any(type(g) is not int or g < 0 for g in goals):
                raise ValueError('Invalid historical goals')
            if date.fromisoformat(r['date']) >= cutoff.date():
                raise ValueError('Date-only history must precede the cutoff day')
            if r.get('available_at') and timestamp(r['available_at']) > cutoff:
                raise ValueError('History was not available at cutoff')
            value = {'goals': goals, 'date': r['date']}
            if r['id'] in merged and merged[r['id']] != value:
                raise ValueError('Conflicting shared historical match')
            merged[r['id']] = value
    return merged


def last5_sensitivity(home, away, as_of):
    merged = validate_history(home, away, as_of)

    def calculation(omit=None):
        obs = [v for k, v in merged.items() if k != omit]
        rates = [sum(v['goals'][i] for v in obs) / len(obs) for i in (0, 1)]
        if any(v > 12 for v in rates):
            raise ValueError('Rate outside original beta diagnostic range')
        raw = portable.goal_probabilities(*rates)
        p = {'1x2': dict(zip(CLASSES, raw['1x2'])), 'btts': raw['btts'],
             'total_2_5': {'over': raw['over_2_5'], 'under': 1 - raw['over_2_5']}}
        return {'rates': rates, 'probabilities': p, 'directions': directions(p)}

    full = calculation()
    runs = [{'omitted_match_id': mid, **calculation(mid)} for mid in sorted(merged)]
    flips = {t: sum(r['directions'][t] != full['directions'][t] for r in runs) for t in TARGETS}
    return {'full': full, 'runs': runs, 'unique_matches': len(merged),
            'direction_flip_counts': flips, 'unstable_targets': [t for t in TARGETS if flips[t]],
            'method': 'leave_one_unique_historical_match_out_no_refill',
            'diagnostic_only': True, 'is_statistical_confidence_interval': False,
            'historical_scores_removed_from_model': False}


def monte_carlo(home_rate, away_rate, match_id, recipe_id, samples=10000):
    if type(samples) is not int or samples < 1:
        raise ValueError('Invalid simulation count')
    if any(not math.isfinite(v) or not 0 <= v <= 12 for v in (home_rate, away_rate)):
        raise ValueError('Invalid goal rates')
    seed = int(hashlib.sha256(f'{VERSION}:{match_id}:{recipe_id}'.encode()).hexdigest()[:16], 16)
    rng = random.Random(seed)

    def draw(rate):
        if rate == 0:
            return 0
        limit, product, count = math.exp(-rate), 1.0, 0
        while product > limit:
            product *= rng.random()
            count += 1
        return count - 1

    scores, outcomes = Counter(), Counter()
    btts = over = 0
    for _ in range(samples):
        h, a = draw(home_rate), draw(away_rate)
        scores[h, a] += 1
        outcomes['H' if h > a else 'D' if h == a else 'A'] += 1
        btts += h > 0 and a > 0
        over += h + a > 2
    return {'seed': seed, 'samples': samples, 'recipe_id': recipe_id,
            'raw_uncalibrated_scenarios_only': True,
            'probabilities': {'1x2': {c: outcomes[c] / samples for c in CLASSES},
                              'btts': btts / samples,
                              'total_2_5': {'over': over / samples, 'under': 1 - over / samples}},
            'most_frequent_scores': [{'home_goals': h, 'away_goals': a, 'count': n}
                                     for (h, a), n in sorted(scores.items(), key=lambda r: (-r[1], r[0]))[:10]]}


def history_audit_issues(fixtures, audit, as_of):
    """Validate supplied provenance; a true flag alone is not outside verification."""
    cutoff = timestamp(as_of)
    issues = {}
    for f in fixtures:
        messages = []
        for side in ('home', 'away'):
            team = f[side + '_key']
            record = audit.get(team, {})
            if record.get('complete') is not True or not record.get('source_urls'):
                messages.append(f'{team}:current_history_completeness_unverified')
                continue
            checked = timestamp(record['checked_at'])
            if checked > cutoff:
                raise ValueError('History audit after information cutoff')
            if cutoff - checked > timedelta(hours=24):
                messages.append(f'{team}:history_audit_older_than_24_hours')
            latest = max(f['history'][side], key=lambda r: (r['date'], r['id']))
            if record.get('latest_match_id') != latest['id']:
                messages.append(f'{team}:history_omits_audited_latest_match')
        issues[f['match_id']] = messages
    return issues


def make_snapshot(package, inputs, policy, mode='forecast', include_mc=True):
    """Record one append-only snapshot, with results in a different file entirely."""
    if mode not in ('forecast', 'retrospective_reconstruction'):
        raise ValueError('Unsupported recording mode')
    as_of = timestamp(inputs['as_of'])
    now = timestamp(utcnow())
    if as_of > now:
        raise ValueError('Information cutoff cannot be in the future')
    if date.fromisoformat(package['refit_as_of_date']) > as_of.date():
        raise ValueError('Model fit date is after the requested cutoff')
    fit_day = date.fromisoformat(package['refit_as_of_date'])
    last_allowed = fit_day - timedelta(days=package['date_guard_days'])
    for model in package['fitted_models'].values():
        if date.fromisoformat(model['latest_training_date']) > last_allowed:
            raise ValueError('Training contains scores after its information guard')
    if mode == 'forecast' and timestamp(package['created_at']) > as_of:
        raise ValueError('Package did not exist at the requested forecast cutoff')
    fixtures = inputs['fixtures']
    if not fixtures or len({f['match_id'] for f in fixtures}) != len(fixtures):
        raise ValueError('Fixtures must be nonempty and unique')
    audit_issues = history_audit_issues(fixtures, inputs.get('history_audit', {}), inputs['as_of'])
    output = []
    for f in fixtures:
        kickoff = timestamp(f['kickoff_at'])
        if as_of >= kickoff or (mode == 'forecast' and now >= kickoff):
            raise ValueError('Cannot record a forecast at or after kickoff')
        if mode == 'retrospective_reconstruction' and now < kickoff:
            raise ValueError('Retrospective mode is for past fixtures only')
        if any(f.get(k) is not None for k in ('actual', 'result', 'result_90m', 'home_goals', 'away_goals')):
            raise ValueError('Outcomes must not be provided to the forecast engine')
        diagnostics = last5_sensitivity(f['history']['home'], f['history']['away'], inputs['as_of'])
        numeric = numerical_probabilities(package, f)
        decision = decide(numeric['probabilities'], policy)
        hybrid = hybrid_decide(f['main'], numeric['probabilities'], policy) if f.get('main') else None
        if (as_of.date() - fit_day).days > 3:
            audit_issues[f['match_id']].append('model_refit_older_than_three_days')
        for side in ('home', 'away'):
            team = f[side + '_key']
            eligible = [r for r in f['history'][side] if date.fromisoformat(r['date']) <= last_allowed]
            known = package.get('training_latest_by_team', {}).get(team)
            if eligible and (not known or max(r['date'] for r in eligible) > known['date']):
                audit_issues[f['match_id']].append(f'{team}:model_missing_known_eligible_history')
        if audit_issues[f['match_id']]:
            for record in (decision, hybrid):
                if record is not None:
                    for target in record['targets'].values():
                        target.update(pick=None, status='observe', reason='current_history_audit_required')
                    record['focus'] = None
        simulations = {}
        if include_mc:
            for row in numeric['by_target'].values():
                mid = row['recipe_id']
                if mid not in simulations:
                    simulations[mid] = monte_carlo(*row['goal_rates'], f['match_id'], mid)
        output.append({'match_id': f['match_id'], 'home': f.get('home', f['home_key']),
                       'away': f.get('away', f['away_key']), 'kickoff_at': f['kickoff_at'],
                       **numeric, 'decision': decision, 'hybrid': hybrid,
                       'quality_issues': audit_issues[f['match_id']],
                       'last5_diagnostic': diagnostics, 'raw_mc_by_recipe': simulations,
                       'result_90m': None})
    result = {'schema_version': 'superanalyst-experimental-forecast-v1', 'model_version': VERSION,
              'mode': mode, 'synthetic': bool(inputs.get('synthetic', False)),
              'as_of': inputs['as_of'], 'model_package_sha256': fingerprint(package),
              'input_sha256': fingerprint(inputs), 'focus_policy': copy.deepcopy(policy),
              'scope': '90m', 'main_operational_model_changed': False,
              'history_audit_source': 'supplied_provenance_not_independent_machine_verification',
              'rows': output, 'created_at': now.isoformat()}
    result['recorded_at' if mode == 'forecast' else 'reconstructed_at'] = now.isoformat()
    if mode == 'retrospective_reconstruction':
        if not inputs.get('reconstruction_notes'):
            raise ValueError('Historical reconstruction needs an explicit limitation note')
        result.update(point_in_time_verified=False, reconstruction_notes=inputs['reconstruction_notes'])
    result['snapshot_id'] = fingerprint(result)[:32]
    return result
