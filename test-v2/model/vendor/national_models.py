"""Independent Poisson team strengths; new national-team study, no UCL parameters."""
import math
from datetime import date
import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp, expit

def candidates(protocol):
    base=[{"id":f"pooled{n}","kind":"pooled","window":n} for n in protocol["window_baselines"]]
    return base+[dict(s,kind="strength") for s in protocol["strength_models"]]
def form_vector(feature,side,other,window):
    if window is None:
        return []
    own=feature[side]["windows"]; opp=feature[other]["windows"]
    out=[]
    for small,large,measure in ((own[str(window)],own["30"],"gf"),(opp[str(window)],opp["30"],"ga")):
        if small["gf"] is None or large["gf"] is None:
            out.append(0.0)
        else:
            out.append(math.log((small[measure]+0.5)/(large[measure]+0.5)))
    return out
def objective(theta,arrays,nt,nc,penalty):
    attack,defense,comp,home,goals,weights,x=arrays
    pc=1+2*nt; ph=pc+nc; pf=ph+1
    eta=theta[0]+theta[1+attack]+theta[1+nt+defense]+theta[pc+comp]+home*theta[ph]
    if x.shape[1]:
        eta=eta+x@theta[pf:]
    mu=np.exp(eta)
    value=np.dot(weights,mu-goals*eta)+0.5*np.dot(penalty,theta*theta)
    residual=weights*(mu-goals)
    grad=penalty*theta
    grad[0]+=residual.sum()
    grad[1:1+nt]+=np.bincount(attack,weights=residual,minlength=nt)
    grad[1+nt:pc]+=np.bincount(defense,weights=residual,minlength=nt)
    grad[pc:ph]+=np.bincount(comp,weights=residual,minlength=nc)
    grad[ph]+=np.dot(residual,home)
    if x.shape[1]:
        grad[pf:]+=x.T@residual
    scale=weights.sum()
    return value/scale,grad/scale
def fit(rows,features,spec,cutoff_ordinal,protocol,previous=None):
    guard=protocol["history_guard_days"]
    training=[r for r in rows if r["ordinal"]<=cutoff_ordinal-guard
              and r["ordinal"]>=cutoff_ordinal-round(365.25*protocol["training_lookback_years"])
              and (r["competitive"] or spec.get("include_friendlies"))]
    if not training:
        raise ValueError("No training data before cutoff")
    assert max(r["ordinal"] for r in training)<=cutoff_ordinal-guard
    teams=sorted({r[s] for r in training for s in ("home","away")})
    comps=sorted({r["competition"] for r in training})
    ti={t:i for i,t in enumerate(teams)}; ci={c:i for i,c in enumerate(comps)}
    attack=[]; defense=[]; competition=[]; homes=[]; goals=[]; weights=[]; matrix=[]
    fw=spec.get("form_window"); nf=0 if fw is None else 2
    for r in training:
        w=0.5**((cutoff_ordinal-r["ordinal"])/spec["half_life_days"])
        f=features[r["match_id"]]
        assert f["history_cutoff_ordinal"]<=r["ordinal"]-guard
        for side,other in (("home","away"),("away","home")):
            attack.append(ti[r[side]]); defense.append(ti[r[other]])
            competition.append(ci[r["competition"]]); homes.append(float(side=="home" and not r["neutral"]))
            goals.append(r[side+"_goals"]); weights.append(w)
            matrix.append(form_vector(f,side,other,fw))
    nt,nc=len(teams),len(comps)
    pc=1+2*nt; ph=pc+nc; pf=ph+1; size=pf+nf
    initial=np.zeros(size); initial[0]=math.log(max(.1,sum(goals)/len(goals)))
    if previous:
        initial[0]=previous["intercept"]; initial[ph]=previous["home_advantage"]
        for team,index in ti.items():
            initial[1+index]=previous["attack"].get(team,0)
            initial[1+nt+index]=previous["defense"].get(team,0)
        for c,index in ci.items():
            initial[pc+index]=previous["competition"].get(c,0)
        initial[pf:]=previous.get("form_coefficients",[])
    penalty=np.zeros(size)
    penalty[1:pc]=protocol["fixed_regularization"]["team"]
    penalty[pc:ph]=protocol["fixed_regularization"]["competition"]
    penalty[pf:]=protocol["fixed_regularization"]["form"]
    arrays=(np.asarray(attack),np.asarray(defense),np.asarray(competition),np.asarray(homes),
            np.asarray(goals),np.asarray(weights),np.asarray(matrix).reshape(len(goals),nf))
    bounds=[(-3.,3.)]*size; bounds[0]=(-2.5,2.5); bounds[ph]=(-1.5,1.5)
    result=minimize(objective,initial,args=(arrays,nt,nc,penalty),jac=True,method="L-BFGS-B",
                    bounds=bounds,options={"maxiter":500,"ftol":1e-10,"gtol":1e-7,"maxls":35})
    if not result.success or not np.isfinite(result.fun):
        raise ValueError(f'Optimizer failed for {spec["id"]}: {result.message}')
    theta=result.x
    return {"id":spec["id"],"spec":spec,"trained_before":date.fromordinal(cutoff_ordinal).isoformat(),
            "training_matches":len(training),"latest_training_date":max(r["date"] for r in training),
            "training_weight_sum":float(sum(weights)/2),
            "intercept":float(theta[0]),"attack":{t:float(theta[1+j]) for t,j in ti.items()},
            "defense":{t:float(theta[1+nt+j]) for t,j in ti.items()},
            "competition":{c:float(theta[pc+j]) for c,j in ci.items()},
            "home_advantage":float(theta[ph]),"form_coefficients":[float(v) for v in theta[pf:]],
            "optimization":{"success":bool(result.success),"iterations":int(result.nit),
                            "objective":float(result.fun),"max_abs_gradient":float(np.max(np.abs(result.jac)))}}
def pooled_rate(f,n,home_direction):
    values={}
    for side in ("home","away"):
        field="gf" if ((side=="home")==home_direction) else "ga"
        for obs in f[side]["history"][-n:]:
            if obs["match_id"] in values:
                assert values[obs["match_id"]]==obs[field]
            values[obs["match_id"]]=obs[field]
    if not values:
        raise ValueError("No pooled observations")
    return sum(values.values())/len(values)
def rates(spec,model,row,feature,protocol):
    low,high=protocol["rate_bounds"]
    if spec["kind"]=="pooled":
        h=pooled_rate(feature,spec["window"],True)
        a=pooled_rate(feature,spec["window"],False)
        return [min(high,max(low,h)),min(high,max(low,a))],False
    out=[]; cold=False
    for side,other in (("home","away"),("away","home")):
        cold|=row[side] not in model["attack"] or row[other] not in model["defense"]
        eta=model["intercept"]+model["attack"].get(row[side],0)+model["defense"].get(row[other],0)
        eta+=model["competition"].get(row["competition"],0)
        if side=="home" and not row["neutral"]:
            eta+=model["home_advantage"]
        z=form_vector(feature,side,other,spec.get("form_window"))
        eta+=sum(x*b for x,b in zip(z,model["form_coefficients"]))
        out.append(min(high,max(low,math.exp(eta))))
    return out,cold
def distribution(home,away):
    # 120 covers the locked maximum mean 12 with negligible omitted mass.
    h=np.empty(121); a=np.empty(121)
    h[0]=math.exp(-home); a[0]=math.exp(-away)
    for k in range(1,121):
        h[k]=h[k-1]*home/k; a[k]=a[k-1]*away/k
    grid=np.outer(h,a); mass=grid.sum()
    win=float(np.tril(grid,-1).sum()/mass)
    draw=float(np.trace(grid)/mass)
    loss=float(np.triu(grid,1).sum()/mass)
    btts=(-math.expm1(-home))*(-math.expm1(-away))
    total=home+away
    over=1-math.exp(-total)*(1+total+total*total/2)
    return {"1x2":[win,draw,loss],"btts":btts,"over_2_5":over}
def labels(r):
    h,a=r["home_goals"],r["away_goals"]
    return {"1x2":0 if h>a else 1 if h==a else 2,
            "btts":int(h>0 and a>0),"over_2_5":int(h+a>2)}
def losses(prob,actual,target):
    if target=="1x2":
        p=np.clip(np.asarray(prob,dtype=float),1e-15,1-1e-15)
        p/=p.sum(axis=1,keepdims=True)
        y=np.asarray(actual,dtype=int)
        log=-np.log(p[np.arange(len(y)),y])
        one=np.eye(3)[y]
        brier=np.square(p-one).sum(axis=1)
        acc=(np.argmax(p,axis=1)==y)
    else:
        p=np.clip(np.asarray(prob,dtype=float),1e-15,1-1e-15)
        y=np.asarray(actual,dtype=int)
        log=-(y*np.log(p)+(1-y)*np.log1p(-p))
        brier=np.square(p-y)
        acc=(p>=.5)==y
    return {"log_loss":log,"brier":brier,"accuracy":acc.astype(float)}
def metrics(prob,actual,target):
    if not actual:
        return {"n":0,"log_loss":None,"brier":None,"accuracy":None}
    scores=losses(prob,actual,target)
    return {"n":len(actual),**{k:float(np.mean(v)) for k,v in scores.items()}}
def fit_calibrator(prob,actual,target):
    y=np.asarray(actual,dtype=int)
    if target=="1x2":
        logp=np.log(np.clip(np.asarray(prob),1e-15,1))
        def fun(theta):
            invtemp,bh,bd=theta
            z=invtemp*logp+np.array([bh,bd,0])
            q=np.exp(z-logsumexp(z,axis=1,keepdims=True))
            loss=-np.log(np.clip(q[np.arange(len(y)),y],1e-15,1)).sum()
            residual=q-np.eye(3)[y]
            penalty=.5*((invtemp-1)**2+bh*bh+bd*bd)
            grad=np.array([np.sum(residual*logp)+(invtemp-1),residual[:,0].sum()+bh,residual[:,1].sum()+bd])
            return (loss+penalty)/len(y),grad/len(y)
        opt=minimize(fun,np.array([1.,0.,0.]),jac=True,method="L-BFGS-B",bounds=[(.5,2),(-2,2),(-2,2)])
        params={"inverse_temperature":float(opt.x[0]),"home_bias":float(opt.x[1]),"draw_bias":float(opt.x[2])}
    else:
        p=np.clip(np.asarray(prob),1e-12,1-1e-12); x=np.log(p/(1-p))
        def fun(theta):
            b,s=theta; z=b+s*x; q=expit(z)
            loss=np.logaddexp(0,z).sum()-np.dot(y,z)+.5*(b*b+(s-1)**2)
            residual=q-y
            grad=np.array([residual.sum()+b,np.dot(residual,x)+(s-1)])
            return loss/len(y),grad/len(y)
        opt=minimize(fun,np.array([0.,1.]),jac=True,method="L-BFGS-B",bounds=[(-2,2),(.2,3)])
        params={"intercept":float(opt.x[0]),"slope":float(opt.x[1])}
    if not opt.success:
        raise ValueError("Calibration optimizer failed")
    return {"target":target,"n":len(y),"parameters":params,"optimization_success":bool(opt.success)}
def calibrate(prob,calibrator):
    params=calibrator["parameters"]
    if calibrator["target"]=="1x2":
        z=params["inverse_temperature"]*np.log(np.clip(np.asarray(prob),1e-15,1))
        z+=np.array([params["home_bias"],params["draw_bias"],0])
        return (np.exp(z-logsumexp(z))).tolist()
    p=min(1-1e-12,max(1e-12,float(prob)))
    return float(expit(params["intercept"]+params["slope"]*math.log(p/(1-p))))

