# Septic math

Septic math plans around the tank nobody thinks about: the bedroom
count becomes the labeled tank size, the household and the tank become
the years between pump-outs, and the buried lid becomes the riser that
ends the digging.

Live site: https://ilanis-agent.github.io/septimath/

## The three tools

- **Tank plan** - a labeled 1000 gallon tank to 3 bedrooms plus 250
  gallons a bedroom beyond, with a standard / upsized / big-house
  verdict.
- **Pump plan** - `tank / 3 / (people x labeled 40 gal a year)` years
  between pump-outs, with a tight / normal / relaxed schedule verdict.
- **Riser plan** - `bury depth - labeled 5 cm above grade` of riser,
  with a stub / standard / deep dig verdict.

## Limits

Every default is labeled and illustrative. Real systems follow the
county code, the perc test and the pumper's own records, and sizing
rules vary by jurisdiction. This is planning arithmetic, not a system
design or a health rating: let the county and the licensed pumper
govern.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 132 checks)

Run the tests: `python3 oracle.py && node test.js`
