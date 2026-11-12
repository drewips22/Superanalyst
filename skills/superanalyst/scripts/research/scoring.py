"""Proper scores and paired month-block uncertainty for the same match cohort."""
import math
import random
from collections import defaultdict

EPS=1e-15
LABELS=("home","draw","away")

def loss_values(prediction, outcome):
    h,a=outcome["home_goals"],outcome["away_goals"]
    actual="home" if h>a else "away" if h<a else "draw"
    p=prediction["p_1x2"]
    if set(p)!=set(LABELS) or not math.isclose(sum(p.values()),1,abs_tol=1e-8):
        raise ValueError("invalid 1X2 probabilities")
    if any(not math.isfinite(v) or not 0<=v<=1 for v in [*p.values(),prediction["p_btts"],prediction["p_over_2_5"]]):
        raise ValueError("invalid probability")
    btts=h>0 and a>0
    over=h+a>=3
    return {"log_loss_1x2":-math.log(max(EPS,p[actual])),
        "brier_1x2":sum((p[label]-float(label==actual))**2 for label in LABELS),
        "brier_btts":(prediction["p_btts"]-btts)**2,
        "log_loss_btts":-math.log(max(EPS,prediction["p_btts"] if btts else 1-prediction["p_btts"])),
        "brier_over_2_5":(prediction["p_over_2_5"]-over)**2,
        "log_loss_over_2_5":-math.log(max(EPS,prediction["p_over_2_5"] if over else 1-prediction["p_over_2_5"])),
        "correct_1x2":float(max(p,key=p.get)==actual),
        "correct_btts":float((prediction["p_btts"]>=.5)==btts),
        "correct_over_2_5":float((prediction["p_over_2_5"]>=.5)==over),
        "actual_1x2":actual,"actual_btts":btts,"actual_over_2_5":over}

def evaluate(predictions,outcomes):
    ids=[p["match_id"] for p in predictions]
    if len(ids)!=len(set(ids)):
        raise ValueError("duplicate predicted match")
    values=[loss_values(p,outcomes[p["match_id"]]) for p in predictions]
    keys=("log_loss_1x2","brier_1x2","brier_btts","log_loss_btts",
          "brier_over_2_5","log_loss_over_2_5","correct_1x2","correct_btts","correct_over_2_5")
    result={"n":len(values),**{key:sum(v[key] for v in values)/len(values) if values else None for key in keys}}
    result["outcome_counts"]={label:sum(v["actual_1x2"]==label for v in values) for label in LABELS}
    result["outcome_counts"].update(btts_yes=sum(v["actual_btts"] for v in values),over_2_5_yes=sum(v["actual_over_2_5"] for v in values))
    result["calibration"]={}
    for key,observed in (("p_btts","actual_btts"),("p_over_2_5","actual_over_2_5")):
        bins=[[] for _ in range(10)]
        for p,v in zip(predictions,values):
            bins[min(9,int(p[key]*10))].append((p[key],int(v[observed])))
        result["calibration"][key]=[{"lower":i/10,"upper":(i+1)/10,"n":len(b),
            "mean_probability":sum(p for p,y in b)/len(b) if b else None,
            "observed_rate":sum(y for p,y in b)/len(b) if b else None} for i,b in enumerate(bins)]
    return result

def paired_month_interval(candidate,baseline,outcomes,metric,replicates=2000,seed=1729):
    bm={r["match_id"]:r for r in baseline}
    if set(bm)!={r["match_id"] for r in candidate} or len(bm)!=len(baseline):
        raise ValueError("paired comparison requires identical unique cohorts")
    blocks=defaultdict(list)
    for row in candidate:
        delta=loss_values(row,outcomes[row["match_id"]])[metric]-loss_values(bm[row["match_id"]],outcomes[row["match_id"]])[metric]
        blocks[row["kickoff_at"][:7]].append(delta)
    means=[]
    rng=random.Random(seed)
    values=list(blocks.values())
    for _ in range(replicates):
        selected=[values[rng.randrange(len(values))] for j in values]
        means.append(sum(sum(b) for b in selected)/sum(map(len,selected)))
    means.sort()
    return {"delta_candidate_minus_baseline":sum(sum(b) for b in values)/sum(map(len,values)),
            "percentile_95_interval":[means[int(.025*replicates)],means[min(replicates-1,int(.975*replicates))]],
            "n_month_blocks":len(values),"replicates":replicates,"seed":seed,
            "interpretation":"Negative favors candidate; time-block resampling is descriptive and does not remove data/source/selection uncertainty."}
