import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def tank_plan(bedrooms):
    if not (bedrooms > 0):
        return {"error": "the bedroom count must be positive"}
    extra = max(0, math.ceil(bedrooms) - 3) * 250
    tank = 1000 + extra
    if bedrooms <= 3: verdict = "a standard tank"
    elif bedrooms <= 5: verdict = "an upsized tank"
    else: verdict = "a big-house tank"
    return {"tank": tank, "verdict": verdict}

def pump_plan(people, tankGal):
    if not (people > 0) or not (tankGal > 0):
        return {"error": "the household and the tank must be positive"}
    years = round1(tankGal / 3 / (people * 40))
    if years < 2: verdict = "a tight schedule"
    elif years <= 4: verdict = "a normal schedule"
    else: verdict = "a relaxed schedule"
    return {"years": years, "verdict": verdict}

def riser_plan(depthCm):
    if not (depthCm > 0):
        return {"error": "the bury depth must be positive"}
    if depthCm <= 5:
        return {"error": "the lid already sits at or above grade"}
    riser = round1(depthCm - 5)
    if riser < 20: verdict = "a stub riser"
    elif riser <= 60: verdict = "a standard riser"
    else: verdict = "a deep dig"
    return {"riser": riser, "verdict": verdict}

def render_tank(r, bedrooms):
    return ("A house with " + plural(bedrooms, "bedroom") + " asks a labeled " + fmt(r["tank"])
            + " gallon tank - " + r["verdict"] + ".")

def render_pump(r, people, tankGal):
    return ("A household of " + fmt(people) + " on a labeled " + fmt(tankGal) + " gallon tank pumps about every "
            + plural(r["years"], "year") + " - " + r["verdict"] + ".")

def render_riser(r, depthCm):
    return ("A lid buried " + fmt(depthCm) + " cm takes a labeled " + fmt(r["riser"])
            + " cm riser to reach grade - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[4],[1],[0],[3],[5],[6],[2],[7],[2.5],[10]]:
    add("tankPlan", tank_plan, render_tank, a)
for a in [[4,1250],[2,1000],[0,1250],[4,0],[6,1000],[1,1500],[3,1000],[5,1250],[8,1000],[2,750]]:
    add("pumpPlan", pump_plan, render_pump, a)
for a in [[45],[70],[0],[3],[5],[25],[15],[60],[65],[42.5]]:
    add("riserPlan", riser_plan, render_riser, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
