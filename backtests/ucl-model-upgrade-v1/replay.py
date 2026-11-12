"""Replay frozen probabilities and scores from committed model/feature snapshots."""
import importlib.util
import json
from pathlib import Path

CASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("upgrade_case",CASE/"run.py")
case=importlib.util.module_from_spec(spec)
spec.loader.exec_module(case)

def replay(case_dir=CASE):
    manifest=case.read(case_dir/"input-manifest.json")
    for name,expected in manifest["code_sha256"].items():
        if case.digest(case_dir/name)!=expected:
            raise ValueError("original frozen source differs: "+name)
    archived=case.read(case_dir/"forecast-inputs.json")
    checked=0
    for stage in ("validation","test"):
        models=case.read(case_dir/(stage+"-models.json"))
        predictions=case.read(case_dir/(stage+"-predictions.json"))
        for variant,rows in predictions.items():
            for stored in rows:
                item=archived["matches"][stored["match_id"]]
                row,feature=item["fixture"],item["features"]
                if variant.startswith("goals_last"):
                    window=10 if variant=="goals_last10" else 20 if variant=="goals_last20" else 5
                    rates=case.baseline_rates(feature,window)
                else:
                    model=models[stored["fit_key"]]
                    if case.timestamp(model["latest_training_available_proxy_at"])>case.timestamp(feature["as_of"]):
                        raise ValueError("model training extends beyond prediction cutoff")
                    rates=case.predict_rates(model,row,feature)
                rebuilt=case.prediction(row,feature,rates,variant,stored["fit_key"])
                if rebuilt!=stored:
                    raise ValueError("prediction does not reproduce: "+variant+" "+stored["match_id"])
                checked+=1
    selection=case.read(case_dir/"selection.json")
    for name,expected in selection["frozen_sha256"].items():
        if case.digest(case_dir/name)!=expected:
            raise ValueError("selection input changed")
    for name,expected in case.read(case_dir/"test-freeze.json")["sha256"].items():
        if case.digest(case_dir/name)!=expected:
            raise ValueError("test snapshot changed")
    actual=case.read(case_dir/"test-outcomes.json")
    report=case.read(case_dir/"evaluation.json")
    for variant,rows in case.read(case_dir/"test-predictions.json").items():
        if case.evaluate(rows,actual)!=report["pooled"][variant]:
            raise ValueError("held-out scores do not reproduce")
    for variant,rows in case.read(case_dir/"validation-predictions.json").items():
        if case.evaluate(rows,archived["validation_outcomes"])!=case.read(case_dir/"validation-evaluation.json")[variant]:
            raise ValueError("validation scores do not reproduce")
    return {"probabilities_reproduced":checked,"validation_and_test_scores_reproduced":True,
            "note":"Refitting still requires the locally archived full corpus; replay needs only committed target feature/model snapshots."}

if __name__=="__main__":
    print(json.dumps(replay(),ensure_ascii=False,indent=2))
