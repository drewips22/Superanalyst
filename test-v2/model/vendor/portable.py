"""Portable research inference for the frozen national-team v1 package.

Python standard library only. This calculator does not collect live information
or publish operational forecasts. Target probabilities have separate calibrators.
"""
import argparse
import json
import math
from datetime import date
from pathlib import Path


def goal_probabilities(home_rate, away_rate):
    """Compute the independent Poisson marginals without Monte Carlo error."""
    def poisson(rate):
        values = [math.exp(-rate)]
        for k in range(1, 121):
            values.append(values[-1] * rate / k)
        return values

    home, away = poisson(home_rate), poisson(away_rate)
    hwin = awin = draw = hcum = acum = 0.0
    for h, a in zip(home, away):
        hwin += h * acum
        awin += a * hcum
        draw += h * a
        hcum += h
        acum += a
    mass = hcum * acum
    total = home_rate + away_rate
    return {
        "1x2": [hwin / mass, draw / mass, awin / mass],
        "btts": (-math.expm1(-home_rate)) * (-math.expm1(-away_rate)),
        "over_2_5": 1 - math.exp(-total) * (1 + total + total * total / 2),
    }


def calibrate(probability, recipe):
    params = recipe["parameters"]
    if recipe["target"] == "1x2":
        logits = [params["inverse_temperature"] * math.log(max(1e-15, p))
                  for p in probability]
        logits[0] += params["home_bias"]
        logits[1] += params["draw_bias"]
        pivot = max(logits)
        values = [math.exp(v - pivot) for v in logits]
        return [v / sum(values) for v in values]
    p = min(1 - 1e-12, max(1e-12, probability))
    z = params["intercept"] + params["slope"] * math.log(p / (1 - p))
    return 1 / (1 + math.exp(-z))


def rates(model, home, away, competition, neutral, bounds=(0.05, 12)):
    if model["spec"].get("form_window") is not None:
        raise ValueError("This portable calculator supports only the selected no-form recipes")
    if home == away:
        raise ValueError("Teams must differ")
    if any(team not in model["attack"] or team not in model["defense"]
           for team in (home, away)):
        raise ValueError("Unknown team; a new fit is required")
    if competition not in model["competition"]:
        raise ValueError("Unknown competition; a new fit is required")
    values = []
    for team, opponent, is_home in ((home, away, True), (away, home, False)):
        value = (model["intercept"] + model["attack"][team] +
                 model["defense"][opponent] + model["competition"][competition])
        if is_home and not neutral:
            value += model["home_advantage"]
        values.append(min(bounds[1], max(bounds[0], math.exp(value))))
    return values


def diagnostic(package, home, away, competition, neutral, as_of, match_date):
    cutoff, match = date.fromisoformat(as_of), date.fromisoformat(match_date)
    if cutoff < date.fromisoformat(package["refit_as_of_date"]):
        raise ValueError("Package trained after requested cutoff; historical use would leak information")
    if match <= cutoff:
        raise ValueError("Date-only diagnostic requires a match date after the cutoff")
    result = {}
    for target, recipe in package["target_recipes"].items():
        model = package["fitted_models"][recipe["model_id"]]
        hr, ar = rates(model, home, away, competition, neutral)
        raw = goal_probabilities(hr, ar)[target]
        result[target] = {"model_id": recipe["model_id"], "raw": raw,
                          "calibrated": calibrate(raw, recipe["calibrator"]),
                          "goal_rates": [hr, ar]}
    return {
        "mode": "research_score_diagnostic_not_operational_forecast",
        "home": home, "away": away, "competition": competition,
        "match_date": match_date, "as_of_date": as_of, "neutral": neutral,
        "data_latest_date": package["data_latest_date"],
        "data_age_days": (cutoff - date.fromisoformat(package["data_latest_date"])).days,
        "model_package_version": package["model_package_version"],
        "probabilities": result,
        "requires_current_checks": ["fixture and kickoff", "all intervening matches",
                                    "XI and injuries", "coaching and squad changes"],
        "scope": "90 minutes plus stoppage time",
        "warning": package["joint_distribution_warning"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, required=True)
    for name in ("home", "away", "competition", "as-of", "match-date"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--neutral", action="store_true")
    args = parser.parse_args()
    package = json.loads(args.package.read_text(encoding="utf-8"))
    print(json.dumps(diagnostic(package, args.home, args.away, args.competition,
                                args.neutral, args.as_of, args.match_date),
                     indent=2, ensure_ascii=False, allow_nan=False))


if __name__ == "__main__":
    main()
