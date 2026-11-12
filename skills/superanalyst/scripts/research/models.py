"""Regularized Poisson attack/defense models with causal optional covariates."""
import math
import numpy as np
from scipy.optimize import minimize
from features import timestamp, columns, numeric_features

RATE_BOUNDS = (.02, 12.)

def objective(theta, attack, defense, competition, home_flag, y, weights, features,
              team_count, competition_count, use_home, penalty):
    nt, nc = team_count, competition_count
    pos_c = 1 + 2*nt
    pos_h = pos_c + nc
    pos_f = pos_h + (1+nc if use_home else 0)
    eta = theta[0] + theta[1+attack] + theta[1+nt+defense] + theta[pos_c+competition]
    if use_home:
        eta = eta + home_flag*(theta[pos_h]+theta[pos_h+1+competition])
    if features.shape[1]:
        eta = eta + features @ theta[pos_f:]
    mean = np.exp(eta)
    scale = weights.sum()
    value = (np.dot(weights,mean-y*eta) + .5*np.dot(penalty,theta**2))/scale
    residual = weights*(mean-y)
    grad = penalty*theta
    grad[0] += residual.sum()
    grad[1:1+nt] += np.bincount(attack,weights=residual,minlength=nt)
    grad[1+nt:pos_c] += np.bincount(defense,weights=residual,minlength=nt)
    grad[pos_c:pos_h] += np.bincount(competition,weights=residual,minlength=nc)
    if use_home:
        grad[pos_h] += np.dot(residual,home_flag)
        grad[pos_h+1:pos_f] += np.bincount(competition,weights=residual*home_flag,minlength=nc)
    if features.shape[1]:
        grad[pos_f:] += features.T @ residual
    return value,grad/scale

def fit(rows, feature_map, variant, cutoff, specification, previous=None):
    if not rows:
        raise ValueError("empty training sample")
    cutoff_dt = timestamp(cutoff)
    if any(timestamp(r["available_proxy_at"]) > cutoff_dt for r in rows):
        raise ValueError("training includes information after fit cutoff")
    teams = sorted({r[k] for r in rows for k in ("home_id","away_id")})
    competitions = sorted({r["competition"] for r in rows})
    ti,ci = {v:i for i,v in enumerate(teams)},{v:i for i,v in enumerate(competitions)}
    attack,defense,comp,flags,y,weights,features = [],[],[],[],[],[],[]
    for row in rows:
        age = (cutoff_dt-timestamp(row["available_proxy_at"])).total_seconds()/86400
        weight = .5**(age/specification["recency_half_life_days"])
        feature = feature_map[row["match_id"]]
        for side,other in (("home","away"),("away","home")):
            attack.append(ti[row[side+"_id"]])
            defense.append(ti[row[other+"_id"]])
            comp.append(ci[row["competition"]])
            flags.append(float(side == "home" and not row.get("neutral")))
            y.append(row[side+"_goals"])
            weights.append(weight)
            features.append(numeric_features(feature,side,variant,row))
    nt,nc,nf=len(teams),len(competitions),len(columns(variant))
    use_home = "home" in variant
    pos_c=1+2*nt
    pos_h=pos_c+nc
    pos_f=pos_h+(1+nc if use_home else 0)
    size=pos_f+nf
    initial=np.zeros(size)
    initial[0]=math.log(max(.1,sum(y)/len(y)))
    if previous:
        initial[0]=previous["intercept"]
        for tid,i in ti.items():
            initial[1+i]=previous["attack"].get(tid,0.)
            initial[1+nt+i]=previous["defense"].get(tid,0.)
        for league,i in ci.items():
            initial[pos_c+i]=previous["competition_offsets"].get(league,0.)
            if use_home:
                initial[pos_h+1+i]=previous.get("home_offsets",{}).get(league,0.)
        if use_home:
            initial[pos_h]=previous.get("home_global",0.)
        for i,name in enumerate(columns(variant)):
            initial[pos_f+i]=previous.get("numeric_coefficients",{}).get(name,0.)
    regularization=specification["regularization"]
    penalty=np.zeros(size)
    penalty[1:pos_c]=regularization["team_parameters"]
    penalty[pos_c:pos_h]=regularization["competition_parameters"]
    if use_home:
        penalty[pos_h+1:pos_f]=regularization["competition_parameters"]
    penalty[pos_f:]=regularization["numeric_features"]
    arrays = (np.asarray(attack),np.asarray(defense),np.asarray(comp),np.asarray(flags),
              np.asarray(y),np.asarray(weights),np.asarray(features,dtype=float).reshape(len(y),nf))
    result=minimize(objective,initial,args=(*arrays,nt,nc,use_home,penalty),jac=True,
        method="L-BFGS-B",bounds=[(-3.,3.)]*size,
        options={"maxiter":350,"ftol":1e-10,"gtol":1e-7,"maxls":30})
    theta=result.x
    return {"variant":variant,"trained_at_cutoff":cutoff,"training_matches":len(rows),
        "latest_training_available_proxy_at":max(r["available_proxy_at"] for r in rows),
        "intercept":float(theta[0]),
        "attack":{tid:float(theta[1+i]) for tid,i in ti.items()},
        "defense":{tid:float(theta[1+nt+i]) for tid,i in ti.items()},
        "competition_offsets":{league:float(theta[pos_c+i]) for league,i in ci.items()},
        "home_global":float(theta[pos_h]) if use_home else 0.,
        "home_offsets":{league:float(theta[pos_h+1+i]) for league,i in ci.items()} if use_home else {},
        "numeric_coefficients":{name:float(theta[pos_f+i]) for i,name in enumerate(columns(variant))},
        "optimization":{"success":bool(result.success),"message":str(result.message),
                        "iterations":int(result.nit),"objective":float(result.fun),
                        "max_abs_gradient":float(np.max(np.abs(result.jac)))},
        "rate_bounds":list(RATE_BOUNDS),"unknown_team_policy":"zero regularized attack/defense offset; report cold starts"}

def predict_rates(model,row,feature):
    rates=[]
    unclipped=[]
    for side,other in (("home","away"),("away","home")):
        eta=model["intercept"]+model["competition_offsets"].get(row["competition"],0.)
        eta+=model["attack"].get(row[side+"_id"],0.)+model["defense"].get(row[other+"_id"],0.)
        if side == "home" and not row.get("neutral"):
            eta+=model["home_global"]+model["home_offsets"].get(row["competition"],0.)
        values=numeric_features(feature,side,model["variant"],row)
        eta+=sum(value*model["numeric_coefficients"][name] for name,value in zip(columns(model["variant"]),values))
        raw=math.exp(eta)
        unclipped.append(raw)
        rates.append(min(RATE_BOUNDS[1],max(RATE_BOUNDS[0],raw)))
    return {"home":rates[0],"away":rates[1],"clipped":rates!=unclipped}

def baseline_rates(feature,window=5):
    home,away=feature["home"]["windows"][str(window)],feature["away"]["windows"][str(window)]
    if min(home["n"],away["n"]) < 5:
        return None
    return {"home":(home["gf"]+away["ga"])/2,"away":(away["gf"]+home["ga"])/2,"clipped":False}
