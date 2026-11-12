"""Resolve reported venue cities using GeoNames; distance is a proxy, not an itinerary."""
import argparse
import hashlib
import io
import json
import unicodedata
import urllib.request
import zipfile
from pathlib import Path

COUNTRIES = {"England":"GB","Scotland":"GB","Wales":"GB","Northern Ireland":"GB",
    "United Kingdom":"GB","France":"FR","Spain":"ES","Italy":"IT","Germany":"DE",
    "Portugal":"PT","Netherlands":"NL","Belgium":"BE","Turkey":"TR","Türkiye":"TR",
    "Norway":"NO","Denmark":"DK","Sweden":"SE","Finland":"FI","Greece":"GR",
    "Switzerland":"CH","Austria":"AT","Czech Republic":"CZ","Czechia":"CZ",
    "Poland":"PL","Hungary":"HU","Romania":"RO","Serbia":"RS","Croatia":"HR",
    "Slovenia":"SI","Slovakia":"SK","Bulgaria":"BG","Ukraine":"UA","Russia":"RU",
    "Cyprus":"CY","Israel":"IL","Azerbaijan":"AZ","Kazakhstan":"KZ","Belarus":"BY",
    "Malta":"MT","Iceland":"IS","Ireland":"IE","Estonia":"EE","Latvia":"LV","Lithuania":"LT",
    "Bosnia and Herzegovina":"BA","North Macedonia":"MK","Albania":"AL","Kosovo":"XK",
    "United States":"US","USA":"US","Qatar":"QA","Saudi Arabia":"SA","United Arab Emirates":"AE",
    "San Marino":"SM","Luxembourg":"LU","Montenegro":"ME","Moldova":"MD","Armenia":"AM","Georgia":"GE"}

def normalized(value):
    return "".join(c for c in unicodedata.normalize("NFKD",value).casefold() if c.isalnum())

def resolve(matches, output):
    output.mkdir(parents=True, exist_ok=True)
    url = "https://download.geonames.org/export/dump/cities15000.zip"
    archive = output / "cities15000.zip"
    if not archive.exists():
        with urllib.request.urlopen(url, timeout=45) as response:
            archive.write_bytes(response.read())
    wanted = {(r.get("venue_city"),r.get("venue_country")) for r in matches if r.get("venue_city") and r.get("venue_country")}
    by_key, candidates = {}, {}
    for city,country in wanted:
        by_key.setdefault((normalized(city),COUNTRIES.get(country)),[]).append((city,country))
    with zipfile.ZipFile(archive) as zipped:
        with zipped.open("cities15000.txt") as source:
            for raw in source:
                fields = raw.decode("utf-8").rstrip("\n").split("\t")
                if len(fields) < 19:
                    continue
                for alias in set([fields[1],fields[2]] + fields[3].split(",")):
                    for key in by_key.get((normalized(alias),fields[8]),[]):
                        value = {"city":key[0],"country":key[1],"geoname_id":int(fields[0]),
                                 "latitude":float(fields[4]),"longitude":float(fields[5]),
                                 "population":int(fields[14]),"timezone":fields[17]}
                        if key not in candidates or value["population"] > candidates[key]["population"]:
                            candidates[key] = value
    result = {"source_url":url,"source_sha256":hashlib.sha256(archive.read_bytes()).hexdigest(),
        "attribution":"GeoNames, Creative Commons Attribution; https://www.geonames.org/about.html",
        "note":"Current geographic city coordinates applied to previously observed venue city labels; actual itinerary and historical stadium location not verified.",
        "requested":len(wanted),"resolved":len(candidates),"cities":list(candidates.values()),
        "unresolved":[list(k) for k in sorted(wanted) if k not in candidates]}
    with (output/"coordinates.json").open("w",encoding="utf-8",newline="\n") as handle:
        json.dump(result,handle,ensure_ascii=False,indent=2)
        handle.write("\n")
    return result

def load(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    return {(r["city"],r["country"]):(r["latitude"],r["longitude"]) for r in data["cities"]}

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matches",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    rows=[json.loads(s) for s in args.matches.read_text(encoding="utf-8").splitlines()]
    result=resolve(rows,args.output)
    print(json.dumps({"requested":result["requested"],"resolved":result["resolved"]}))
