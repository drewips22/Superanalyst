"""Separate chronological study of prior-game StatsBomb xG and goals."""
import argparse
import hashlib
import json
import math
import sys
from collections import defaultdict
from datetime import datetime,timedelta,timezone
from pathlib import Path

CASE=Path(__file__).resolve().parent
ROOT=CASE.parents[1]
SCRIPTS=ROOT/"skills/superanalyst/scripts"
sys.path.insert(0,str(SCRIPTS))
sys.path.insert(0,str(SCRIPTS/"research"))
from stats import poisson_forecast
from scoring import evaluate

def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_new(path,value):
    with path.open("x",encoding="utf-8",newline="\n") as handle:
        json.dump(value,handle,ensure_ascii=False,indent=2,allow_nan=False)
        handle.write("\n")

def feature_snapshots(rows):
    history=defaultdict(list)
    ordered=sorted(rows,key=lambda r:(r["kickoff_at"],r["match_id"]))
    available=sorted(rows,key=lambda r:(r["available_proxy_at"],r["match_id"]))
    pointer=0
    features={}
    for target in ordered:
        cutoff=(datetime.fromisoformat(target["kickoff_at"])-timedelta(days=1)).isoformat()
        while pointer<len(available) and available[pointer]["available_proxy_at"]<=cutoff:
            row=available[pointer]
            pointer+=1
            history[row["home_id"]].append(row)
            history[row["away_id"]].append(row)
        result={"match_id":target["match_id"],"as_of":cutoff,"home":{},"away":{}}
        for side in ("home","away"):
            tid=target[side+"_id"]
            for window in (5,10):
                past=history[tid][-window:]
                n=len(past)
                gf=ga=xf=xa=0.
                for row in past:
                    own="home" if row["home_id"]==tid else "away"
                    opp="away" if own=="home" else "home"
                    gf+=row[own+"_goals"]
                    ga+=row[opp+"_goals"]
                    xf+=row[own+"_statistics"]["xg"]
                    xa+=row[opp+"_statistics"]["xg"]
                result[side][str(window)]={"n":n,"gf":gf/n if n else None,"ga":ga/n if n else None,
                    "xg_for":xf/n if n else None,"xg_against":xa/n if n else None,"history_ids":[r["match_id"] for r in past]}
        features[target["match_id"]]=result
    return features

def predict(row,f,window,alpha,name):
    home,away=f["home"][str(window)],f["away"][str(window)]
    h=((1-alpha)*(home["gf"]+away["ga"])+alpha*(home["xg_for"]+away["xg_against"]))/2
    a=((1-alpha)*(away["gf"]+home["ga"])+alpha*(away["xg_for"]+home["xg_against"]))/2
    p=poisson_forecast(h,a)
    total=h+a
    return {"match_id":row["match_id"],"kickoff_at":row["kickoff_at"],"as_of":f["as_of"],
        "competition":row["competition"],"variant":name,"home":row["home"],"away":row["away"],
        "p_1x2":p["p_1x2"],"p_btts":p["p_btts"],"p_over_2_5":1-math.exp(-total)*(1+total+total**2/2),
        "goal_rates":{"home":h,"away":a},"mode":"retrospective_reconstruction",
        "point_in_time_verified":False,"result":None}

def validation(case_dir,data_dir):
    if (case_dir/"selection.json").exists():
        raise ValueError("selection already frozen")
    spec=read(case_dir/"experiment.json")
    rows=[json.loads(s) for s in (data_dir/"matches.jsonl").read_text(encoding="utf-8").splitlines()]
    if len(rows)!=760 or len({r["match_id"] for r in rows})!=760:
        raise ValueError("complete unique two-league corpus required")
    features=feature_snapshots(rows)
    eligible=[r for r in rows if min(features[r["match_id"]][s]["5"]["n"] for s in ("home","away"))>=5]
    target=[r for r in eligible if spec["validation_dates"][0]<=r["kickoff_at"][:10]<spec["validation_dates"][1]]
    outcomes={r["match_id"]:r for r in rows}
    outputs,metrics={},{}
    for window in spec["windows"]:
        for alpha in spec["xg_mix_weights"]:
            name=f"goals{window}-alpha{alpha:g}"
            outputs[name]=[predict(r,features[r["match_id"]],window,alpha,name) for r in target]
            metrics[name]=evaluate(outputs[name],outcomes)
    selected={"1x2":min(metrics,key=lambda v:(metrics[v]["log_loss_1x2"],metrics[v]["brier_1x2"])),
        "btts":min(metrics,key=lambda v:(metrics[v]["brier_btts"],metrics[v]["log_loss_btts"])),
        "over_2_5":min(metrics,key=lambda v:(metrics[v]["brier_over_2_5"],metrics[v]["log_loss_over_2_5"]))}
    write_new(case_dir/"features.json",features)
    write_new(case_dir/"validation-predictions.json",outputs)
    write_new(case_dir/"validation-evaluation.json",metrics)
    write_new(case_dir/"selection.json",{"selected":selected,"n":len(target),
        "created_at":datetime.now(timezone.utc).isoformat(),"corpus_sha256":digest(data_dir/"matches.jsonl"),
        "sha256":{name:digest(case_dir/name) for name in ("run.py","experiment.json","features.json","validation-predictions.json","validation-evaluation.json","../../skills/superanalyst/scripts/research/scoring.py","../../skills/superanalyst/scripts/stats.py")}})
    return {"action":"auxiliary_validation_selected","n":len(target),"selected":selected}

def verify_selection(case_dir,data_dir):
    selection=read(case_dir/"selection.json")
    if digest(data_dir/"matches.jsonl")!=selection["corpus_sha256"]:
        raise ValueError("xG corpus changed")
    for name,expected in selection["sha256"].items():
        if digest(case_dir/name)!=expected:
            raise ValueError("frozen auxiliary input changed: "+name)
    return selection

def predict_test(case_dir,data_dir):
    selection=verify_selection(case_dir,data_dir)
    if (case_dir/"test-predictions.json").exists():
        raise ValueError("test predictions exist")
    spec=read(case_dir/"experiment.json")
    rows=[json.loads(s) for s in (data_dir/"matches.jsonl").read_text(encoding="utf-8").splitlines()]
    features=read(case_dir/"features.json")
    targets=[r for r in rows if spec["test_dates"][0]<=r["kickoff_at"][:10]<spec["test_dates"][1]
             and min(features[r["match_id"]][s]["5"]["n"] for s in ("home","away"))>=5]
    variants={spec["baseline"],*selection["selected"].values()}
    outputs={}
    for variant in sorted(variants):
        w,a=variant.split("-alpha")
        outputs[variant]=[predict(r,features[r["match_id"]],int(w[5:]),float(a),variant) for r in targets]
    write_new(case_dir/"test-predictions.json",outputs)
    write_new(case_dir/"test-freeze.json",{"created_at":datetime.now(timezone.utc).isoformat(),
        "sha256":{name:digest(case_dir/name) for name in ("selection.json","test-predictions.json")},"n":len(targets)})
    return {"action":"auxiliary_test_predictions_frozen","n":len(targets),"variants":sorted(variants)}

def grade(case_dir,data_dir):
    selection=verify_selection(case_dir,data_dir)
    if (case_dir/"evaluation.json").exists():
        raise ValueError("evaluation exists")
    for name,expected in read(case_dir/"test-freeze.json")["sha256"].items():
        if digest(case_dir/name)!=expected:
            raise ValueError("test snapshot changed")
    rows=[json.loads(s) for s in (data_dir/"matches.jsonl").read_text(encoding="utf-8").splitlines()]
    outcomes={r["match_id"]:r for r in rows}
    outputs=read(case_dir/"test-predictions.json")
    pooled={name:evaluate(preds,outcomes) for name,preds in outputs.items()}
    leagues={league:{name:evaluate([p for p in preds if p["competition"]==league],outcomes) for name,preds in outputs.items()}
             for league in sorted({r["competition"] for r in rows})}
    baseline=read(case_dir/"experiment.json")["baseline"]
    decisions={}
    for target,variant in selection["selected"].items():
        key={"1x2":"log_loss_1x2","btts":"brier_btts","over_2_5":"brier_over_2_5"}[target]
        other={"1x2":"brier_1x2","btts":"log_loss_btts","over_2_5":"log_loss_over_2_5"}[target]
        passed=pooled[variant][key]<pooled[baseline][key] and pooled[variant][other]<=pooled[baseline][other] and all(v[variant][key]<v[baseline][key] for v in leagues.values())
        decisions[target]={"selected_variant":variant,"baseline":pooled[baseline][key],"candidate":pooled[variant][key],
                           "auxiliary_gate_passed":passed,"status":"auxiliary domestic evidence only; not a UCL promotion"}
    report={"created_at":datetime.now(timezone.utc).isoformat(),"n":pooled[baseline]["n"],
            "pooled":pooled,"by_league":leagues,"decisions":decisions,
            "scope_note":"2015/16 men's Premier League and Serie A, prior covered league games only; retrospective current xG exports, not point-in-time verified."}
    write_new(case_dir/"evaluation.json",report)
    return {"action":"auxiliary_graded","n":report["n"],"decisions":decisions}

def verify(case_dir,data_dir):
    verify_selection(case_dir,data_dir)
    rows=[json.loads(s) for s in (data_dir/"matches.jsonl").read_text(encoding="utf-8").splitlines()]
    outcomes={r["match_id"]:r for r in rows}
    for name,expected in read(case_dir/"test-freeze.json")["sha256"].items():
        if digest(case_dir/name)!=expected:
            raise ValueError("test snapshot changed")
    if (case_dir/"evaluation.json").exists():
        metrics=read(case_dir/"evaluation.json")["pooled"]
        for name,predictions in read(case_dir/"test-predictions.json").items():
            if evaluate(predictions,outcomes)!=metrics[name]:
                raise ValueError("auxiliary evaluation differs")
    return {"action":"auxiliary_verified"}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command",choices=("validate","predict-test","grade","verify"))
    parser.add_argument("--case-dir",type=Path,default=CASE)
    parser.add_argument("--data-dir",type=Path,default=ROOT/"data/statsbomb-xg-v1")
    args=parser.parse_args()
    actions={"validate":validation,"predict-test":predict_test,"grade":grade,"verify":verify}
    try:
        print(json.dumps(actions[args.command](args.case_dir,args.data_dir),ensure_ascii=False,indent=2,allow_nan=False))
    except (ValueError,KeyError,OSError,TypeError) as exc:
        parser.exit(2,f"error: {exc}\n")
