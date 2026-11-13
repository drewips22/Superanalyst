"""Validate and grade qualitative forecast snapshots without changing their inputs."""
import argparse
import json
from datetime import datetime
from pathlib import Path

ALLOWED={'1x2':('H','D','A'),'btts':(True,False),'total_2_5':('over','under')}

def timestamp(value):
    dt=datetime.fromisoformat(value.replace('Z','+00:00'))
    if dt.tzinfo is None:raise ValueError('Timestamp requires timezone')
    return dt

def validate(document):
    if document.get('schema_version')!='qualitative-forecast-v2':raise ValueError('Unsupported schema')
    recorded=timestamp(document['recorded_at']);cutoff=timestamp(document['as_of'])
    if cutoff>recorded:raise ValueError('Information cutoff follows recording')
    seen=set()
    for row in document['forecasts']:
        mid=row['match_id']
        if mid in seen:raise ValueError('Duplicate match')
        seen.add(mid)
        if recorded>=timestamp(row['kickoff_at']):raise ValueError('Forecast must precede kickoff')
        for value in row.get('source_retrieved_at',[]):
            if timestamp(value)>cutoff:raise ValueError('Source retrieved after cutoff')
        if row.get('probabilities') is not None:raise ValueError('Qualitative archive does not accept invented probabilities')
        score=row.get('score_scenario')
        if score is not None and (len(score)!=2 or any(type(x) is not int or x<0 for x in score)):
            raise ValueError('Invalid score scenario')
        for key,choices in ALLOWED.items():
            target=row['targets'][key];pick=target['pick'];status=target['status']
            if pick is None:
                if status not in ('observasi','tidak_cukup_data') or not target.get('abstain_reason') or target.get('confidence') is not None:
                    raise ValueError('Abstention needs a reason, observation status and null confidence')
            else:
                if not any(type(pick) is type(x) and pick==x for x in choices):raise ValueError('Invalid target pick')
                if status not in ('provisional','analisis_layak'):raise ValueError('Published pick cannot be observation')
                if target.get('confidence') not in ('low','medium','relatively_strong'):raise ValueError('Invalid qualitative confidence')
                if not target.get('supporting_evidence'):raise ValueError('Pick needs supporting evidence')
            for name in ('supporting_evidence','contradicting_evidence'):
                if not isinstance(target.get(name),list) or any(not isinstance(x,str) or not x.strip() for x in target[name]):
                    raise ValueError('Evidence must be a list of nonblank strings')
    return {'valid':True,'matches':len(seen),'predicted':{k:sum(r['targets'][k]['pick'] is not None for r in document['forecasts']) for k in ALLOWED}}

def grade(document,outcomes):
    checks=validate(document)
    if len({r['match_id'] for r in outcomes})!=len(outcomes):raise ValueError('Duplicate outcome')
    by_id={r['match_id']:r for r in outcomes};rows=[]
    for forecast in document['forecasts']:
        result=by_id.get(forecast['match_id'])
        if result is None:
            rows.append({'match_id':forecast['match_id'],'resolved':False});continue
        if result['scope']!='90m' or result['status']!='completed':raise ValueError('Outcome must be completed normal time')
        h=result['home_goals'];a=result['away_goals']
        if any(type(x) is not int or x<0 for x in (h,a)):raise ValueError('Invalid outcome goals')
        actual={'1x2':'H' if h>a else 'A' if a>h else 'D','btts':h>0 and a>0,'total_2_5':'over' if h+a>2 else 'under'}
        rows.append({'match_id':forecast['match_id'],'resolved':True,'correct':{k:None if forecast['targets'][k]['pick'] is None else forecast['targets'][k]['pick']==actual[k] for k in ALLOWED}})
    metrics={}
    for key in ALLOWED:
        values=[r['correct'][key] for r in rows if r['resolved'] and r['correct'][key] is not None]
        metrics[key]={'correct':sum(values),'evaluated':len(values),'predicted':checks['predicted'][key],'accuracy':sum(values)/len(values) if values else None}
    return {'rows':rows,'metrics':metrics,'note':'Targets share matches; do not treat them as independent samples. No probability metrics.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('validate');p.add_argument('forecast')
    p=sub.add_parser('grade');p.add_argument('forecast');p.add_argument('outcomes')
    args=parser.parse_args()
    document=json.loads(Path(args.forecast).read_text(encoding='utf-8'))
    result=validate(document) if args.command=='validate' else grade(document,json.loads(Path(args.outcomes).read_text(encoding='utf-8')))
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
