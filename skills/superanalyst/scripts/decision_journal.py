"""Record and reuse qualitative decisions with real timestamps and explicit revisions.

This is an audit helper, not a prediction model. The frozen v0.4.2 validator
and scorer stay unchanged. All file output uses exclusive creation.
"""
import argparse
import copy
import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

import forecast_archive

TARGETS = ('1x2', 'btts', 'total_2_5')
KINDS = ('new_information', 'lineup_confirmation', 'data_correction', 'reassessment', 'scope_change')


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def digest(value):
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return hashlib.sha256(encoded.encode('utf-8')).hexdigest()


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def check_inputs(inputs, forecast):
    cutoff = forecast_archive.timestamp(forecast['as_of'])
    if inputs.get('as_of') != forecast['as_of']:
        raise ValueError('Input cutoff must equal forecast cutoff')
    if inputs.get('profile') not in ('competitive', 'friendly'):
        raise ValueError('Declare competitive or friendly profile')
    if not inputs.get('facts') or not isinstance(inputs['facts'], dict):
        raise ValueError('Archive the actual input facts')
    sources = inputs.get('sources', [])
    if not sources or len({s['id'] for s in sources}) != len(sources):
        raise ValueError('Sources need distinct IDs')
    for source in sources:
        if not nonblank(source['id']) or not source.get('url', '').startswith(('https://', 'http://')):
            raise ValueError('Source needs ID and direct URL')
        retrieved = forecast_archive.timestamp(source['retrieved_at'])
        if retrieved > cutoff:
            raise ValueError('Source retrieved after cutoff')
        if source.get('available_at') is not None:
            available = forecast_archive.timestamp(source['available_at'])
            if available > retrieved:
                raise ValueError('Source availability follows retrieval')
    for row in forecast['forecasts']:
        if not nonblank(row.get('analysis_method')):
            raise ValueError('Keep the analysis method explicit')
        if row.get('result_90m') is not None:
            raise ValueError('Target results belong in a separate outcome file')
        if 'focus_target' not in row:
            raise ValueError('Declare focus_target, including null when there is no focus')
        focus = row['focus_target']
        if focus is not None and (focus not in TARGETS or row['targets'][focus]['pick'] is None):
            raise ValueError('Focus must name a published target')
    flags = []
    if inputs['profile'] == 'friendly':
        contexts = inputs.get('friendly_context', {})
        if set(contexts) != {r['match_id'] for r in forecast['forecasts']}:
            raise ValueError('Friendly context must cover exactly the forecast matches')
        for mid, context in contexts.items():
            for side in ('home', 'away'):
                team = context[side]
                if type(team.get('recent_friendlies_reviewed')) is not bool:
                    raise ValueError('Explicitly record whether recent friendlies were reviewed')
                if not nonblank(team.get('history_representativeness')):
                    raise ValueError('Explain history age, opponent and squad/coach relevance')
                if team.get('lineup_status') not in ('official', 'projected', 'unavailable'):
                    raise ValueError('Declare lineup status for each team')
                latest = team.get('last_competitive_at')
                age = None if latest is None else (cutoff - forecast_archive.timestamp(latest)).days
                if age is not None and age < 0:
                    raise ValueError('Competitive history cannot come from after cutoff')
                flags.append({'match_id': mid, 'team': side, 'competitive_history_age_days': age,
                              'recent_friendlies_reviewed': team['recent_friendlies_reviewed'],
                              'lineup_status': team['lineup_status']})
            rules = context['substitution_rules']
            if rules.get('status') not in ('verified', 'unknown'):
                raise ValueError('Substitution rules must be verified or unknown')
            if rules['status'] == 'verified':
                if rules.get('source_id') not in {s['id'] for s in sources}:
                    raise ValueError('Verified substitution rules need a source')
                if type(rules.get('maximum')) is not int or rules['maximum'] < 0:
                    raise ValueError('Verified substitution limit must be a nonnegative integer')
            elif rules.get('maximum') is not None:
                raise ValueError('Unknown substitution limit remains null')
    return flags


def differences(previous, current):
    old = {r['match_id']: r for r in previous['forecasts']}
    new = {r['match_id']: r for r in current['forecasts']}
    changes = []
    for mid in sorted(set(old) | set(new)):
        if mid not in old or mid not in new:
            changes.append({'match_id': mid, 'target': 'scope', 'before': mid in old, 'after': mid in new})
            continue
        if old[mid]['kickoff_at'] != new[mid]['kickoff_at']:
            changes.append({'match_id': mid, 'target': 'kickoff_at', 'before': old[mid]['kickoff_at'], 'after': new[mid]['kickoff_at']})
        if old[mid]['analysis_method'] != new[mid]['analysis_method']:
            raise ValueError('A method change needs a separate experiment, not a journal revision')
        for key in (*TARGETS, 'score_scenario', 'focus_target'):
            before, after = old[mid].get(key), new[mid].get(key)
            if key in TARGETS:
                before = {k: old[mid]['targets'][key].get(k) for k in ('pick', 'confidence', 'status')}
                after = {k: new[mid]['targets'][key].get(k) for k in ('pick', 'confidence', 'status')}
            if before != after:
                changes.append({'match_id': mid, 'target': key, 'before': before, 'after': after})
    return changes


def check_review(changes, review, inputs, previous):
    entries = review.get('changes', [])
    pairs = [(e['match_id'], e['target']) for e in entries]
    if len(set(pairs)) != len(pairs) or set(pairs) != {(c['match_id'], c['target']) for c in changes}:
        raise ValueError('Review must explain every changed decision exactly once')
    sources = {s['id']: s for s in inputs['sources']}
    old_cutoff = forecast_archive.timestamp(previous['as_of'])
    for entry in entries:
        kind = entry.get('kind')
        if kind not in KINDS or not nonblank(entry.get('reason')):
            raise ValueError('Each change needs a category and a substantive reason')
        if entry['target'] == 'scope':
            if kind != 'scope_change':
                raise ValueError('Added or removed matches need an explicit scope change')
            continue
        if kind == 'scope_change':
            raise ValueError('Scope change cannot explain a changed target')
        ids = entry.get('source_ids', [])
        if not ids or any(s not in sources for s in ids):
            raise ValueError('Decision revisions need identified source evidence')
        if kind in ('new_information', 'lineup_confirmation'):
            if not any(sources[s].get('available_at') is not None and
                       forecast_archive.timestamp(sources[s]['available_at']) > old_cutoff for s in ids):
                raise ValueError('Old or undated evidence cannot be called new information')
        if kind == 'lineup_confirmation':
            delta = entry.get('lineup_delta', [])
            if not delta or any(not all(nonblank(d.get(k)) for k in ('team', 'player', 'expected', 'confirmed', 'impact')) for d in delta):
                raise ValueError('Lineup revisions need expected/confirmed role and target impact')
        if kind == 'reassessment' and review.get('intentional_reassessment') is not True:
            raise ValueError('Reinterpreting existing evidence must be explicitly intentional')


def validate_record(record):
    if record.get('schema_version') != 'decision-journal-v1':
        raise ValueError('Unsupported journal schema')
    body = {k: v for k, v in record.items() if k != 'sha256'}
    if digest(body) != record.get('sha256') or digest(record['inputs']) != record.get('input_sha256'):
        raise ValueError('Journal or input checksum mismatch')
    if record['recorded_at'] != record['forecast']['recorded_at']:
        raise ValueError('Recording timestamps differ')
    checks = forecast_archive.validate(record['forecast'])
    check_inputs(record['inputs'], record['forecast'])
    return checks


def build_record(forecast, inputs, previous=None, review=None):
    forecast = copy.deepcopy(forecast)
    recorded = utc_now()
    forecast['recorded_at'] = recorded
    forecast_archive.validate(forecast)
    flags = check_inputs(inputs, forecast)
    changes = []
    if previous is not None:
        validate_record(previous)
        if forecast_archive.timestamp(recorded) <= forecast_archive.timestamp(previous['recorded_at']):
            raise ValueError('Revision recording time must follow the previous recording')
        if forecast_archive.timestamp(forecast['as_of']) < forecast_archive.timestamp(previous['forecast']['as_of']):
            raise ValueError('Revision cutoff cannot move backwards')
        changes = differences(previous['forecast'], forecast)
        check_review(changes, review or {}, inputs, previous['forecast'])
    elif review:
        raise ValueError('A revision review needs a previous journal')
    body = {'schema_version': 'decision-journal-v1', 'snapshot_id': uuid.uuid4().hex,
            'recorded_at': recorded, 'input_sha256': digest(inputs),
            'previous_sha256': previous['sha256'] if previous else None,
            'forecast': forecast, 'inputs': copy.deepcopy(inputs),
            'changes': changes, 'review': copy.deepcopy(review or {}),
            'context_flags': flags}
    return {**body, 'sha256': digest(body)}


def reuse(record, inputs):
    validate_record(record)
    if digest(inputs) != record['input_sha256']:
        raise ValueError('Inputs changed; inspect and record a new version instead of reusing')
    return copy.deepcopy(record['forecast'])


def grade(record, outcomes):
    validate_record(record)
    result = forecast_archive.grade(record['forecast'], outcomes)
    rows = {r['match_id']: r for r in result['rows']}
    values = []
    for f in record['forecast']['forecasts']:
        row = rows[f['match_id']]
        if f['focus_target'] is not None and row['resolved']:
            values.append(row['correct'][f['focus_target']])
    for key, metric in result['metrics'].items():
        metric['considered'] = len(rows)
        metric['observations'] = sum(f['targets'][key]['pick'] is None for f in record['forecast']['forecasts'])
        metric['unresolved'] = sum(not row['resolved'] for row in rows.values())
    result['focus'] = {'correct': sum(values), 'evaluated': len(values),
                       'published': sum(f['focus_target'] is not None for f in record['forecast']['forecasts'])}
    return result


def write_new(path, record):
    validate_record(record)
    sealed = copy.deepcopy(record)
    saved_at = utc_now()
    if forecast_archive.timestamp(saved_at) < forecast_archive.timestamp(record['recorded_at']):
        raise ValueError('Saving clock cannot precede record preparation')
    sealed['recorded_at'] = sealed['forecast']['recorded_at'] = saved_at
    sealed['sha256'] = digest({k: v for k, v in sealed.items() if k != 'sha256'})
    validate_record(sealed)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with Path(path).open('x', encoding='utf-8', newline='\n') as handle:
        json.dump(sealed, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write('\n')
    return sealed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('record')
    p.add_argument('forecast'); p.add_argument('inputs'); p.add_argument('--out', required=True)
    p.add_argument('--previous'); p.add_argument('--review')
    p = sub.add_parser('reuse'); p.add_argument('journal'); p.add_argument('inputs')
    p = sub.add_parser('grade'); p.add_argument('journal'); p.add_argument('outcomes')
    args = parser.parse_args()
    def read(path):
        return json.loads(Path(path).read_text(encoding='utf-8'))
    if args.command == 'record':
        record = build_record(read(args.forecast), read(args.inputs),
                              read(args.previous) if args.previous else None,
                              read(args.review) if args.review else None)
        record = write_new(args.out, record)
        result = {'snapshot_id': record['snapshot_id'], 'sha256': record['sha256'],
                  'recorded_at': record['recorded_at'], 'changes': record['changes'], 'output': args.out}
    elif args.command == 'reuse':
        result = reuse(read(args.journal), read(args.inputs))
    else:
        result = grade(read(args.journal), read(args.outcomes))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
