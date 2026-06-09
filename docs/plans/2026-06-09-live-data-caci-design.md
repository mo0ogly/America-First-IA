# Live data for the CACI dashboard, with CSV fallback

Date: 2026-06-09
Status: approved design

## Problem

The dashboard computes the CACI from committed CSV files in
`caci-dashboard/public/data/`. A live-import tool exists (`liveSources.js`,
wired into `DataHub.jsx`) but it is decoupled: it fetches live, shows a table,
and lets the user download a CSV to commit by hand. The dashboard never
computes on live data. We want a real live mode that feeds the CACI
computation directly, with the CSV as a per-cell fallback.

## Decisions

- Trigger: auto-fetch on dashboard load, then compute on whatever came back,
  falling back per cell to the CSV when a source fails.
- US energy (EIA): stays on CSV. No API key is exposed on a public GitHub
  Pages site. Live energy covers the EU only (Eurostat).
- Scope: factors L (workforce) and E (EU energy) already have fetchers. We add
  a GDP fetcher (World Bank). F (Epoch compute) and R (geopolitical tier) have
  no free API and stay on CSV.

## Architecture

Extend the existing `useDataConsolidation` hook rather than add a parallel
hook, to keep a single source of truth. The per-cell CSV fallback already
lives inside `liveSources.js`.

### Components

1. `liveSources.js`: add `fetchGdpLive()`.
   - World Bank indicator `NY.GDP.MKTP.CD` (GDP, current USD), same shape as
     the workforce fetcher: per country, regions summed for the EU aggregate.
   - Per-cell fallback to `gdp_data.csv`.
   - Returns `{ rows: [{Country, GDP_Trillions_USD}], audit: {key: string} }`.

2. `useDataConsolidation.js`: wire the live fetch.
   - Load the CSV baseline first (unchanged).
   - `Promise.allSettled([fetchWorkforceLive(), fetchEnergyLive(), fetchGdpLive()])`
     in parallel.
   - Override `base[k].l`, `base[k].e`, `base[k].gdp` with live values when
     present; keep the CSV value otherwise.
   - US energy stays CSV (no EIA key passed).
   - F and R always come from CSV.
   - Wrap in try/catch: a total network failure falls back to pure CSV, the
     current behavior, so there is no regression.
   - Extract the merge step into a pure function `mergeLive(base, liveResults)`
     so it can be unit tested without a browser.

3. Status surface: the hook returns `dataStatus`, e.g.
   `{ l: 'live', e: 'live', gdp: 'live', f: 'csv', r: 'csv', eUs: 'csv' }`,
   plus the per-source `audit` map already produced by the fetchers. A small
   banner shows "Live: L, E-EU, GDP | CSV: F, R, E-US".

### Data flow

CSV baseline -> parallel live fetch -> per-cell merge -> CACI compute -> render
plus status banner.

### Error handling

- `Promise.allSettled` isolates each source: one API down leaves that factor on
  CSV.
- Total network failure: the whole live block is skipped, dashboard renders on
  CSV.
- The dashboard already has a loading state; live adds roughly 1 to 3 seconds.

### Expected effect on values

F carries the 0.40 weight and stays on CSV, so the headline US/EU ratio moves
little in live mode. That is expected: live refreshes L, EU energy, and GDP,
which is where free authoritative APIs exist.

## Testing

- Unit test `mergeLive` (pure function) with node: live overrides present,
  CSV kept when a source is missing, total-failure path.
- Build check (`npm run build`).
- Dev run: confirm the status banner and per-source audit, and that the page
  still renders with the network blocked.

## Out of scope

- EIA US energy live (needs a key or a serverless proxy).
- F (Epoch) and R live sources (no free API).
- Caching the live result across visits (can be added later if load latency
  is a problem).
