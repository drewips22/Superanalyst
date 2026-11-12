"""Validate pre-cutoff announcements/market quotes; diagnose luck without changing labels."""
import math
from collections import defaultdict
from datetime import datetime

def timestamp(value):
    result=datetime.fromisoformat(value.replace("Z","+00:00"))
    if result.tzinfo is None:
        raise ValueError("timezone required")
    return result

def finite(value,low=0,high=None):
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<low or (high is not None and value>high):
        raise ValueError("invalid numeric context value")
    return float(value)

def required_source(record):
    if not isinstance(record.get("source_url"),str) or not record["source_url"].startswith("https://"):
        raise ValueError("source URL required")

def absence_snapshot(records,as_of,match_id):
    cutoff=timestamp(as_of)
    latest={}
    excluded=[]
    for record in records:
        required_source(record)
        announced=timestamp(record["announced_at"])
        if record["match_id"]!=match_id or announced>cutoff:
            excluded.append({"player_id":record.get("player_id"),"reason":"different match or announced after cutoff"})
            continue
        if record["status"] not in {"out","suspended","ineligible","doubtful","available"}:
            raise ValueError("unsupported player status")
        if record.get("expected_minutes_if_available") is not None:
            finite(record["expected_minutes_if_available"],high=90)
            if timestamp(record["minutes_reference_cutoff"])>cutoff:
                raise ValueError("player role estimate uses future data")
        key=(record["team_id"],record["player_id"])
        if key not in latest or timestamp(latest[key]["announced_at"])<announced:
            latest[key]=record
    unavailable=defaultdict(list)
    doubtful=defaultdict(list)
    minutes=defaultdict(float)
    unknown=defaultdict(int)
    for record in latest.values():
        tid=record["team_id"]
        if record["status"] in {"out","suspended","ineligible"}:
            unavailable[tid].append(record["player_id"])
            if record.get("expected_minutes_if_available") is None:
                unknown[tid]+=1
            else:
                minutes[tid]+=record["expected_minutes_if_available"]
        elif record["status"]=="doubtful":
            doubtful[tid].append(record["player_id"])
    teams={r["team_id"] for r in latest.values()}
    return {"as_of":as_of,"match_id":match_id,"eligible_announcements":len(latest),"excluded":excluded,
        "teams":{tid:{"known_unavailable":unavailable[tid],"doubtful":doubtful[tid],
                      "expected_unavailable_minutes":None if unknown[tid] else minutes[tid],
                      "unavailable_with_unknown_role":unknown[tid]} for tid in teams},
        "win_probability_adjustment":None,
        "note":"Structural/time validation only; supplied timestamps still need source evidence. No fixed 22% penalty, no inference of full fitness from missing records, and no assumed probability for doubtful players."}

def lineup_at_cutoff(record,as_of):
    if record is None:
        return None
    required_source(record)
    if timestamp(record["announced_at"])>timestamp(as_of):
        return None
    if record.get("official") is not True or len(record.get("player_ids",[]))!=11 or len(set(record["player_ids"]))!=11:
        raise ValueError("official lineup requires eleven distinct players")
    return record

def decimal_odds_probabilities(odds):
    if set(odds)!={"home","draw","away"}:
        raise ValueError("three-way decimal odds required")
    implied={k:1/finite(v,low=1.000001) for k,v in odds.items()}
    total=sum(implied.values())
    return {"normalized_probabilities":{k:v/total for k,v in implied.items()},
            "overround":total-1,"method":"proportional margin removal; no claim this is the unique fair probability"}

def market_comparison(quotes,as_of,match_id,contract,scope="90m",max_age_minutes=5,min_independent=3):
    cutoff=timestamp(as_of)
    eligible,excluded=[],[]
    for quote in quotes:
        required_source(quote)
        moment=timestamp(quote["observed_at"])
        age=(cutoff-moment).total_seconds()/60
        if quote["match_id"]!=match_id or quote["contract"]!=contract or quote["scope"]!=scope or not 0<=age<=max_age_minutes:
            excluded.append({"provider":quote["provider"],"reason":"different contract/scope/match or non-comparable timestamp"})
            continue
        if not quote.get("independence_group"):
            raise ValueError("source independence group required")
        bid,ask=quote.get("bid"),quote.get("ask")
        if bid is not None and ask is not None:
            finite(bid,high=1)
            finite(ask,high=1)
            if ask<bid:
                raise ValueError("crossed quote")
        if quote.get("probability") is not None:
            finite(quote["probability"],high=1)
        elif bid is None or ask is None:
            excluded.append({"provider":quote["provider"],"reason":"quote price missing"})
            continue
        if quote.get("depth") is not None:
            finite(quote["depth"])
        eligible.append(quote)
    groups={q["independence_group"] for q in eligible}
    return {"eligible_quotes":eligible,"excluded":excluded,"independent_sources":len(groups),
        "comparison_complete":len(groups)>=min_independent,
        "all_liquidity_verified":bool(eligible) and all(q.get("bid") is not None and q.get("ask") is not None and q.get("depth") is not None for q in eligible),
        "inside_information_confirmed":False,
        "note":"Price movement can trigger observation; it cannot establish insider information. Multiple quotes from the same underlying source are not independent sources."}

def diagnose_result(prediction,outcome,user_hypothesis=None,postmatch_xg=None):
    h,a=outcome["home_goals"],outcome["away_goals"]
    actual="home" if h>a else "away" if h<a else "draw"
    probs=prediction["p_1x2"]
    favourite=max(probs,key=probs.get)
    quality_known=postmatch_xg is not None
    if quality_known:
        for side in ("home","away"):
            finite(postmatch_xg[side])
        if postmatch_xg.get("scope")!="90m" or not postmatch_xg.get("provider"):
            raise ValueError("comparable normal-time xG provider required")
    return {"user_hypothesis":user_hypothesis,"actual_1x2":actual,"pre_match_favourite":favourite,
        "favourite_failed_to_win":actual!=favourite,"probability_of_observed_outcome":probs[actual],
        "postmatch_chance_quality_available":quality_known,
        "luck_status":"candidate_explanation_not_causal_proof" if quality_known and actual!=favourite else "unverified",
        "excluded_from_evaluation":False,"result_label_changed":False,
        "prediction_adjustment":None,"postmatch_xg":postmatch_xg,
        "note":"Post-match diagnosis only. It cannot become a pre-match feature for this match or remove a model miss."}
