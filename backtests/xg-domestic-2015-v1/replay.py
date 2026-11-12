"""Replay the auxiliary mixture predictions without downloading the full event corpus."""
import importlib.util
import json
from pathlib import Path

CASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("auxiliary_case",CASE/"run.py")
case=importlib.util.module_from_spec(spec)
spec.loader.exec_module(case)

def replay():
    selection=case.read(CASE/"selection.json")
    for name,expected in selection["sha256"].items():
        if case.digest(CASE/name)!=expected:
            raise ValueError("auxiliary input changed")
    for name,expected in case.read(CASE/"test-freeze.json")["sha256"].items():
        if case.digest(CASE/name)!=expected:
            raise ValueError("auxiliary test snapshot changed")
    features=case.read(CASE/"features.json")
    outcomes=case.read(CASE/"snapshot-outcomes.json")
    checked=0
    for stage in ("validation","test"):
        for variant,rows in case.read(CASE/(stage+"-predictions.json")).items():
            window,alpha=variant.split("-alpha")
            for stored in rows:
                rebuilt=case.predict(stored,features[stored["match_id"]],int(window[5:]),float(alpha),variant)
                if rebuilt!=stored:
                    raise ValueError("auxiliary prediction does not reproduce")
                checked+=1
            expected=(case.read(CASE/"validation-evaluation.json") if stage=="validation" else case.read(CASE/"evaluation.json")["pooled"])[variant]
            if case.evaluate(rows,outcomes)!=expected:
                raise ValueError("auxiliary scores do not reproduce")
    return {"probabilities_reproduced":checked,"scores_reproduced":True}

if __name__=="__main__":
    print(json.dumps(replay(),indent=2))
