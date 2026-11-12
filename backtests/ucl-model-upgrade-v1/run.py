"""Prepare, validate, freeze held-out predictions, then grade an explicit UCL experiment."""
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
RESEARCH=ROOT/"skills/superanalyst/scripts/research"
sys.path.insert(0,str(RESEARCH))
sys.path.insert(0,str(RESEARCH.parent))
from features import build_features,target_ucl,timestamp
from coordinates import load as load_coordinates
from models import fit,predict_rates,baseline_rates
from scoring import evaluate,paired_month_interval
from stats import poisson_forecast

FROZEN_CODE=("run.py","experiment.json","../../skills/superanalyst/scripts/research/features.py",
    "../../skills/superanalyst/scripts/research/models.py","../../skills/superanalyst/scripts/research/scoring.py",
    "../../skills/superanalyst/scripts/research/collect_history.py","../../skills/superanalyst/scripts/research/coordinates.py",
    "../../skills/superanalyst/scripts/stats.py")
BASELINE="goals_last5_baseline"

def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_new(path,value):
    with path.open("x",encoding="utf-8",newline="\n") as handle:
        json.dump(value,handle,ensure_ascii=False,allow_nan=False,indent=2)
        handle.write("\n")

def load_data(data_dir):
    return [json.loads(line) for line in (data_dir/"matches.jsonl").read_text(encoding="utf-8").splitlines()]

def prepare(case_dir,data_dir):
    if (case_dir/"input-manifest.json").exists():
        raise ValueError("inputs already frozen")
    rows=load_data(data_dir)
    coords=load_coordinates(data_dir/"geography/coordinates.json")
    feature_map=build_features(rows,coords)
    with (data_dir/"features.json").open("w",encoding="utf-8",newline="\n") as handle:
        json.dump(feature_map,handle,ensure_ascii=False,separators=(",",":"),allow_nan=False)
    counts=defaultdict(int)
    coverage=defaultdict(lambda:{"considered":0,"eligible":0,"cold_start":0})
    for row in rows:
        if target_ucl(row):
            season=str(row["season_start_year"])
            counts[season]+=1
            coverage[season]["considered"]+=1
            f=feature_map[row["match_id"]]
            complete=min(f[s]["windows"]["5"]["n"] for s in ("home","away"))>=5
            coverage[season]["eligible" if complete else "cold_start"]+=1
    expected={"2020":125,"2021":125,"2022":125,"2023":125,"2024":189,"2025":189}
    if dict(counts)!=expected:
        raise ValueError(f"incomplete UCL target coverage: {dict(counts)}")
    write_new(case_dir/"input-manifest.json",{
        "created_at":datetime.now(timezone.utc).isoformat(),"mode":"retrospective_reconstruction",
        "point_in_time_verified":False,"n_corpus_matches":len(rows),"target_counts":dict(counts),
        "coverage":dict(coverage),"unresolved_normal_time":sum(r["scope"]!="90m" for r in rows),
        "data_files_sha256":{name:digest(data_dir/name) for name in ("matches.jsonl","manifest.json","features.json","geography/coordinates.json")},
        "code_sha256":{name:digest(case_dir/name) for name in FROZEN_CODE},
        "note":"All selected phase fixtures are included; historical source versions and availability proxies are not verified pre-match archives. No claims of a fully blind historical test."})
    return {"action":"prepared","n_corpus":len(rows),"target_counts":dict(counts),"coverage":dict(coverage)}

def verify_inputs(case_dir,data_dir):
    manifest=read(case_dir/"input-manifest.json")
    for name,expected in manifest["code_sha256"].items():
        if digest(case_dir/name)!=expected:
            raise ValueError("frozen code changed: "+name)
    for name,expected in manifest["data_files_sha256"].items():
        if digest(data_dir/name)!=expected:
            raise ValueError("frozen local data changed: "+name)
    return manifest

def select_targets(rows,feature_map,seasons):
    return [row for row in rows if target_ucl(row) and row["season_start_year"] in seasons
        and min(feature_map[row["match_id"]][s]["windows"]["5"]["n"] for s in ("home","away"))>=5]

def training_rows(rows,cutoff,window_days):
    end=timestamp(cutoff)
    start=end-timedelta(days=window_days)
    return [r for r in rows if r["scope"]=="90m" and start<=timestamp(r["available_proxy_at"])<=end]

def prediction(row,feature,rates,variant,fit_key=None):
    p=poisson_forecast(rates["home"],rates["away"])
    total=rates["home"]+rates["away"]
    return {"match_id":row["match_id"],"home":row["home"],"away":row["away"],
        "kickoff_at":row["kickoff_at"],"as_of":feature["as_of"],"season_start_year":row["season_start_year"],
        "phase":row["phase"],"variant":variant,"fit_key":fit_key,
        "mode":"retrospective_reconstruction","point_in_time_verified":False,"scope":"90m",
        "goal_rates":{"home":rates["home"],"away":rates["away"]},"rate_clipped":rates["clipped"],
        "p_1x2":p["p_1x2"],"p_btts":p["p_btts"],
        "p_over_2_5":1-math.exp(-total)*(1+total+total**2/2),
        "history_ids":{side:feature[side]["windows"]["20"]["ids"] for side in ("home","away")},
        "travel_proxy_known":all(feature[s]["travel_city_distance_km"] is not None for s in ("home","away")),
        "calibrated":False,"result":None}

def forecast(rows,feature_map,targets,variants,spec,progress_path):
    blocks=defaultdict(list)
    for row in targets:
        blocks[row["kickoff_at"][:7]].append(row)
    outputs={variant:[] for variant in variants}
    models,previous={},{}
    for month,block in sorted(blocks.items()):
        cutoff=min(feature_map[r["match_id"]]["as_of"] for r in block)
        train=training_rows(rows,cutoff,spec["training_window_days"])
        for variant in variants:
            if variant.startswith("goals_last"):
                window=10 if variant=="goals_last10" else 20 if variant=="goals_last20" else 5
                for row in block:
                    f=feature_map[row["match_id"]]
                    outputs[variant].append(prediction(row,f,baseline_rates(f,window),variant))
            else:
                key=variant+"@"+month
                model=fit(train,feature_map,variant,cutoff,spec,previous.get(variant))
                if not model["optimization"]["success"]:
                    raise ValueError("fit did not converge: "+key+" "+model["optimization"]["message"])
                models[key]=model
                previous[variant]=model
                for row in block:
                    f=feature_map[row["match_id"]]
                    outputs[variant].append(prediction(row,f,predict_rates(model,row,f),variant,key))
        print(json.dumps({"month":month,"fixtures":len(block),"training_matches":len(train),"variants":len(variants)}),flush=True)
        # Progress contains counts only; final predictions are written once later.
        progress_path.write_text(json.dumps({"last_completed_month":month,"n_models":len(models)}),encoding="utf-8")
    return outputs,models

def validate(case_dir,data_dir):
    verify_inputs(case_dir,data_dir)
    if (case_dir/"selection.json").exists():
        raise ValueError("validation selection already frozen")
    spec=read(case_dir/"experiment.json")
    rows=load_data(data_dir)
    features=read(data_dir/"features.json")
    targets=select_targets(rows,features,spec["validation_seasons_start_year"])
    outputs,models=forecast(rows,features,targets,spec["candidates"],spec,case_dir/"validation-progress.json")
    outcomes={r["match_id"]:r for r in targets}
    metrics={name:evaluate(preds,outcomes) for name,preds in outputs.items()}
    selection={"1x2":min(metrics,key=lambda v:(metrics[v]["log_loss_1x2"],metrics[v]["brier_1x2"])),
        "btts":min(metrics,key=lambda v:(metrics[v]["brier_btts"],metrics[v]["log_loss_btts"])),
        "over_2_5":min(metrics,key=lambda v:(metrics[v]["brier_over_2_5"],metrics[v]["log_loss_over_2_5"]))}
    write_new(case_dir/"validation-predictions.json",outputs)
    write_new(case_dir/"validation-models.json",models)
    write_new(case_dir/"validation-evaluation.json",metrics)
    write_new(case_dir/"selection.json",{"created_at":datetime.now(timezone.utc).isoformat(),
        "selected":selection,"n_validation":len(targets),
        "validation_seasons":spec["validation_seasons_start_year"],
        "frozen_sha256":{name:digest(case_dir/name) for name in ("validation-predictions.json","validation-models.json","validation-evaluation.json","input-manifest.json")},
        "note":"Variant choice uses validation only. Separate target models; no assertion of a common joint goal distribution when variants differ."})
    return {"action":"validation_selected","selected":selection,"n":len(targets),
        "metrics":{v:{k:metrics[v][k] for k in ("log_loss_1x2","brier_1x2","brier_btts","brier_over_2_5")} for v in metrics}}

def predict_test(case_dir,data_dir):
    verify_inputs(case_dir,data_dir)
    if (case_dir/"test-predictions.json").exists():
        raise ValueError("held-out predictions already frozen")
    spec=read(case_dir/"experiment.json")
    selection=read(case_dir/"selection.json")
    for name,expected in selection["frozen_sha256"].items():
        if digest(case_dir/name)!=expected:
            raise ValueError("frozen validation changed")
    rows=load_data(data_dir)
    features=read(data_dir/"features.json")
    targets=select_targets(rows,features,spec["test_seasons_start_year"])
    variants=sorted({BASELINE,*selection["selected"].values()})
    outputs,models=forecast(rows,features,targets,variants,spec,case_dir/"test-progress.json")
    write_new(case_dir/"test-predictions.json",outputs)
    write_new(case_dir/"test-models.json",models)
    write_new(case_dir/"test-freeze.json",{"created_at":datetime.now(timezone.utc).isoformat(),
        "n":len(targets),"variants":variants,
        "sha256":{name:digest(case_dir/name) for name in ("test-predictions.json","test-models.json","selection.json")},
        "note":"Predictions frozen before grading; history and fitted weights are chronologically gated, but sources are retrospective and historical outcomes may already be generally known."})
    return {"action":"held_out_predictions_frozen","n":len(targets),"variants":variants}

def grade(case_dir,data_dir):
    verify_inputs(case_dir,data_dir)
    if (case_dir/"evaluation.json").exists():
        raise ValueError("evaluation already exists")
    spec=read(case_dir/"experiment.json")
    frozen=read(case_dir/"test-freeze.json")
    for name,expected in frozen["sha256"].items():
        if digest(case_dir/name)!=expected:
            raise ValueError("held-out snapshot changed")
    outputs=read(case_dir/"test-predictions.json")
    outcomes={r["match_id"]:r for r in load_data(data_dir)}
    selected=read(case_dir/"selection.json")["selected"]
    pooled={v:evaluate(p,outcomes) for v,p in outputs.items()}
    seasonal={}
    for year in spec["test_seasons_start_year"]:
        seasonal[str(year)]={v:evaluate([p for p in preds if p["season_start_year"]==year],outcomes) for v,preds in outputs.items()}
    primary={"1x2":"log_loss_1x2","btts":"brier_btts","over_2_5":"brier_over_2_5"}
    companion={"1x2":"brier_1x2","btts":"log_loss_btts","over_2_5":"log_loss_over_2_5"}
    decisions={}
    for target,variant in selected.items():
        key,other=primary[target],companion[target]
        pooled_gain=pooled[variant][key]<pooled[BASELINE][key]
        no_companion_regression=pooled[variant][other]<=pooled[BASELINE][other]
        seasons_gain=all(v[variant][key]<v[BASELINE][key] for v in seasonal.values())
        interval=paired_month_interval(outputs[variant],outputs[BASELINE],outcomes,key,
            spec["bootstrap"]["replicates"],spec["bootstrap"]["seed"])
        decisions[target]={"selected_variant":variant,"primary_metric":key,
            "baseline":pooled[BASELINE][key],"candidate":pooled[variant][key],
            "improvement_relative":(pooled[BASELINE][key]-pooled[variant][key])/pooled[BASELINE][key],
            "pooled_improves":pooled_gain,"companion_not_worse":no_companion_regression,
            "each_season_improves":seasons_gain,"promotion_gate_passed":pooled_gain and no_companion_regression and seasons_gain,
            "paired_month_uncertainty":interval,
            "status":"provisional retrospective evidence; requires prospective confirmation"}
    report={"created_at":datetime.now(timezone.utc).isoformat(),"pooled":pooled,"by_season":seasonal,
        "promotion":decisions,"coverage":read(case_dir/"input-manifest.json")["coverage"],
        "prediction_freeze_sha256":digest(case_dir/"test-freeze.json"),
        "rate_clipping_counts":{v:sum(p["rate_clipped"] for p in preds) for v,preds in outputs.items()},
        "limitations":["Retrospective source exports, availability proxies and source coverage are not verified contemporaneous archives.",
            "Covered domestic/cup histories may omit competitions. Rest/congestion use covered fixtures; geographic distance is a city proxy.",
            "No historical role-weighted absence or comparable timestamped market archive available for this cohort; neither factor is claimed tested.",
            "Model selection occurs on one older-format season; held-out seasons use the newer UCL format. Results are reported by season.",
            "No unlucky exclusions: every eligible result is scored. A favorite losing is possible under a valid probability forecast.",
            "xG is evaluated in a distinct 2015/16 domestic study; its result is not transferred to modern UCL without evidence."]}
    write_new(case_dir/"evaluation.json",report)
    write_new(case_dir/"test-outcomes.json",{p["match_id"]:{k:outcomes[p["match_id"]][k] for k in ("home_goals","away_goals","source_url")} for p in outputs[BASELINE]})
    return {"action":"graded","n":pooled[BASELINE]["n"],"promotion":decisions}

def verify(case_dir,data_dir):
    verify_inputs(case_dir,data_dir)
    selection=read(case_dir/"selection.json")
    for name,expected in selection["frozen_sha256"].items():
        if digest(case_dir/name)!=expected:
            raise ValueError("validation checksum changed")
    if (case_dir/"test-freeze.json").exists():
        for name,expected in read(case_dir/"test-freeze.json")["sha256"].items():
            if digest(case_dir/name)!=expected:
                raise ValueError("held-out checksum changed")
    if (case_dir/"evaluation.json").exists():
        outcomes={r["match_id"]:r for r in load_data(data_dir)}
        expected=read(case_dir/"evaluation.json")["pooled"]
        for variant,rows in read(case_dir/"test-predictions.json").items():
            if evaluate(rows,outcomes)!=expected[variant]:
                raise ValueError("scores do not reproduce")
    return {"action":"verified","checksums_and_scores":True}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command",choices=("prepare","validate","predict-test","grade","verify"))
    parser.add_argument("--case-dir",type=Path,default=CASE)
    parser.add_argument("--data-dir",type=Path,default=ROOT/"data/research-v1")
    args=parser.parse_args()
    actions={"prepare":prepare,"validate":validate,"predict-test":predict_test,"grade":grade,"verify":verify}
    try:
        print(json.dumps(actions[args.command](args.case_dir,args.data_dir),ensure_ascii=False,indent=2,allow_nan=False))
    except (ValueError,KeyError,OSError,TypeError) as exc:
        parser.exit(2,f"error: {exc}\n")
