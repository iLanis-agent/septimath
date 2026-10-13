(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function tankPlan(bedrooms) {
    if (!(bedrooms > 0)) return { error: "the bedroom count must be positive" };
    var extra = Math.max(0, Math.ceil(bedrooms) - 3) * 250;
    var tank = 1000 + extra;
    var verdict;
    if (bedrooms <= 3) verdict = "a standard tank";
    else if (bedrooms <= 5) verdict = "an upsized tank";
    else verdict = "a big-house tank";
    return { tank: tank, verdict: verdict };
  }

  function pumpPlan(people, tankGal) {
    if (!(people > 0) || !(tankGal > 0)) return { error: "the household and the tank must be positive" };
    var years = round1(tankGal / 3 / (people * 40));
    var verdict;
    if (years < 2) verdict = "a tight schedule";
    else if (years <= 4) verdict = "a normal schedule";
    else verdict = "a relaxed schedule";
    return { years: years, verdict: verdict };
  }

  function riserPlan(depthCm) {
    if (!(depthCm > 0)) return { error: "the bury depth must be positive" };
    if (depthCm <= 5) return { error: "the lid already sits at or above grade" };
    var riser = round1(depthCm - 5);
    var verdict;
    if (riser < 20) verdict = "a stub riser";
    else if (riser <= 60) verdict = "a standard riser";
    else verdict = "a deep dig";
    return { riser: riser, verdict: verdict };
  }

  function renderTank(r, bedrooms) {
    return "A house with " + plural(bedrooms, "bedroom") + " asks a labeled " + r.tank + " gallon tank - " + r.verdict + ".";
  }

  function renderPump(r, people, tankGal) {
    return "A household of " + people + " on a labeled " + tankGal + " gallon tank pumps about every " + plural(r.years, "year") + " - " + r.verdict + ".";
  }

  function renderRiser(r, depthCm) {
    return "A lid buried " + depthCm + " cm takes a labeled " + r.riser + " cm riser to reach grade - " + r.verdict + ".";
  }

  var api = { tankPlan: tankPlan, pumpPlan: pumpPlan, riserPlan: riserPlan, renderTank: renderTank, renderPump: renderPump, renderRiser: renderRiser };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.SeptiMath = api;
})(this);
