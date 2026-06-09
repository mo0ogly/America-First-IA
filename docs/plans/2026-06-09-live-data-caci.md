# Live Data for CACI Dashboard Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make the CACI dashboard compute on live data (World Bank workforce + GDP, Eurostat EU energy) fetched on load, with the committed CSV as a per-cell fallback.

**Architecture:** Add a GDP fetcher to `liveSources.js` mirroring the workforce fetcher. Extend the `useDataConsolidation` hook to call the three live fetchers in parallel after loading the CSV baseline, merge their values per cell over the baseline through a pure `mergeLive` function, and expose a `dataStatus` map. F, R and US energy stay on CSV. Any fetch failure leaves that factor on CSV; a total failure renders pure CSV.

**Tech Stack:** React 18, Vite 7, PapaParse, browser `fetch`. Tests run with plain Node (ESM, `node --test`), no new framework.

Design: `docs/plans/2026-06-09-live-data-caci-design.md`

---

## Conventions

- All paths are relative to `caci-dashboard/`.
- Run commands from `caci-dashboard/`.
- Node 18+ provides global `fetch` and `node --test`.
- Commit after each task. Branch: `feature/live-data-caci` (already created).

---

### Task 1: Pure merge function `mergeLive`

Extract the per-cell merge into a pure, browser-free function so it can be unit tested.

**Files:**
- Modify: `src/lib/liveSources.js` (add and export `mergeLive`)
- Test: `src/lib/liveSources.merge.test.mjs`

**Step 1: Write the failing test**

```js
// src/lib/liveSources.merge.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mergeLive } from './liveSources.js';

test('mergeLive overrides l/e/gdp when live present, keeps CSV otherwise', () => {
  const base = {
    USA: { f_total: 100, f: 100, e: 86.2, gdp: 31.9, l: 1.679, r: 1.0 },
    EU:  { f_total: 50,  f: 40,  e: 154.9, gdp: 18.0, l: 2.136, r: 1.0 },
  };
  const live = {
    workforce: { USA: 1.8, EU: 2.2 },        // override l
    energy:    { EU: 150.0 },                // override e (US absent -> keep CSV)
    gdp:       { USA: 30.0 },                // override gdp (EU absent -> keep CSV)
  };
  const { merged, status } = mergeLive(base, live);
  assert.equal(merged.USA.l, 1.8);
  assert.equal(merged.EU.l, 2.2);
  assert.equal(merged.EU.e, 150.0);
  assert.equal(merged.USA.e, 86.2);   // US energy kept from CSV
  assert.equal(merged.USA.gdp, 30.0);
  assert.equal(merged.EU.gdp, 18.0);  // EU gdp kept from CSV
  assert.equal(merged.USA.f_total, 100); // F never touched
  assert.equal(status.l, 'live');
  assert.equal(status.gdp, 'live');
  assert.equal(status.eUs, 'csv');
});

test('mergeLive with empty live keeps everything from CSV', () => {
  const base = { USA: { f_total: 100, f: 100, e: 86.2, gdp: 31.9, l: 1.679, r: 1.0 } };
  const { merged, status } = mergeLive(base, { workforce: {}, energy: {}, gdp: {} });
  assert.deepEqual(merged.USA, base.USA);
  assert.equal(status.l, 'csv');
  assert.equal(status.e, 'csv');
  assert.equal(status.gdp, 'csv');
});
```

**Step 2: Run test to verify it fails**

Run: `node --test src/lib/liveSources.merge.test.mjs`
Expected: FAIL with `mergeLive is not a function` (or import error).

**Step 3: Write minimal implementation**

Add near the end of `src/lib/liveSources.js`:

```js
/**
 * Merge live factor maps over the CSV-built base, per cell.
 * live = { workforce: {key:Number}, energy: {key:Number}, gdp: {key:Number} }
 * Returns { merged, status } where status flags each factor live vs csv.
 * F and R are never touched. US energy is reported separately as eUs.
 */
export function mergeLive(base, live) {
  const merged = {};
  for (const [k, v] of Object.entries(base)) merged[k] = { ...v };

  const apply = (field, map) => {
    let any = false;
    if (map) {
      for (const [k, val] of Object.entries(map)) {
        if (merged[k] && Number.isFinite(val)) { merged[k][field] = val; any = true; }
      }
    }
    return any;
  };

  const lLive = apply('l', live.workforce);
  const eLive = apply('e', live.energy);
  const gLive = apply('gdp', live.gdp);

  const status = {
    l: lLive ? 'live' : 'csv',
    e: eLive ? 'live' : 'csv',
    gdp: gLive ? 'live' : 'csv',
    f: 'csv',
    r: 'csv',
    eUs: (live.energy && Number.isFinite(live.energy.USA)) ? 'live' : 'csv',
  };
  return { merged, status };
}
```

**Step 4: Run test to verify it passes**

Run: `node --test src/lib/liveSources.merge.test.mjs`
Expected: PASS (2 tests).

**Step 5: Commit**

```bash
git add src/lib/liveSources.js src/lib/liveSources.merge.test.mjs
git commit -m "feat(live): add pure mergeLive function with CSV fallback"
```

---

### Task 2: GDP live fetcher `fetchGdpLive`

Mirror `fetchWorkforceLive`: World Bank `NY.GDP.MKTP.CD` (GDP, current USD) per country, EU and other regions summed, converted to trillions, CSV fallback per cell.

**Files:**
- Modify: `src/lib/liveSources.js` (add `fetchGdpLive`)
- Test: `src/lib/liveSources.gdp.smoke.mjs` (live network smoke check, run manually)

**Step 1: Write the implementation**

Reuse the existing `WB`, `wbFetchAll`, `SINGLE`, `EU27`, `SOUTH_AMERICA`, `AFRICA`, `ASIA_EX_CHINA`, `loadBaselineCSV`. Add:

```js
// ----- GDP (World Bank, current USD) ---------------------------------------

const GDP_IND = 'NY.GDP.MKTP.CD'; // GDP, current US$
const GDP_ROW_ORDER = [
  'USA', 'China', 'EU', 'UK', 'Asia (Ex-China)',
  'India', 'France', 'Germany', 'South America', 'Africa',
];

function gdpTrillions(iso3, gdp) {
  if (!gdp[iso3]) return null;
  return gdp[iso3].value / 1e12;
}

function gdpRegionSum(members, gdp) {
  let total = 0; let reporting = 0;
  for (const iso3 of members) {
    const t = gdpTrillions(iso3, gdp);
    if (t != null) { total += t; reporting += 1; }
  }
  return { value: Number(total.toFixed(3)), reporting, count: members.length };
}

/**
 * Fetch GDP live from the World Bank, with the committed CSV as fallback.
 * Returns { rows: [{Country, GDP_Trillions_USD}], audit: {key:string} }.
 */
export async function fetchGdpLive() {
  const baseline = await loadBaselineCSV('gdp_data.csv');
  const results = {};
  const audit = {};
  for (const key of GDP_ROW_ORDER) {
    if (baseline[key]) {
      results[key] = Number(baseline[key].GDP_Trillions_USD);
      audit[key] = 'CSV fallback';
    }
  }

  let gdp;
  try {
    gdp = await wbFetchAll(GDP_IND);
  } catch (e) {
    const rows = GDP_ROW_ORDER.filter((k) => k in results)
      .map((k) => ({ Country: k, GDP_Trillions_USD: results[k] }));
    return { rows, audit, error: `World Bank GDP unavailable, using CSV (${e.message})` };
  }

  for (const [key, iso3] of Object.entries(SINGLE)) {
    const t = gdpTrillions(iso3, gdp);
    if (t == null) continue;
    results[key] = Number(t.toFixed(3));
    audit[key] = `${iso3} (yr ${gdp[iso3].year})`;
  }

  const regions = [
    ['EU', EU27], ['South America', SOUTH_AMERICA],
    ['Africa', AFRICA], ['Asia (Ex-China)', ASIA_EX_CHINA],
  ];
  for (const [key, members] of regions) {
    const r = gdpRegionSum(members, gdp);
    if (r.reporting === 0) continue;
    results[key] = r.value;
    audit[key] = `sum of ${r.reporting}/${r.count} reporting countries`;
  }

  const rows = GDP_ROW_ORDER.filter((k) => k in results)
    .map((k) => ({ Country: k, GDP_Trillions_USD: results[k] }));
  return { rows, audit };
}
```

**Step 2: Smoke-test against the live API**

```js
// src/lib/liveSources.gdp.smoke.mjs
// Manual smoke check (needs network). Not part of CI.
const WB = 'https://api.worldbank.org/v2';
const res = await fetch(`${WB}/country/USA/indicator/NY.GDP.MKTP.CD?format=json&mrnev=1&per_page=2`);
const d = await res.json();
const v = d[1][0].value / 1e12;
console.log('USA GDP (trillions):', v.toFixed(2), 'year', d[1][0].date);
if (!(v > 20 && v < 40)) throw new Error('USA GDP out of expected range');
console.log('OK');
```

Run: `node src/lib/liveSources.gdp.smoke.mjs`
Expected: prints a USA GDP near 28-32 trillion and `OK`.

**Step 3: Commit**

```bash
git add src/lib/liveSources.js src/lib/liveSources.gdp.smoke.mjs
git commit -m "feat(live): add World Bank GDP fetcher with CSV fallback"
```

---

### Task 3: Wire live into `useDataConsolidation`

After the CSV `base` is built (and the documented baselines applied), fetch the three live sources in parallel, build per-key maps, merge with `mergeLive`, and expose `dataStatus`.

**Files:**
- Modify: `src/hooks/useDataConsolidation.js`

**Step 1: Add the import**

At the top, after the PapaParse import:

```js
import { fetchWorkforceLive, fetchEnergyLive, fetchGdpLive, mergeLive } from '../lib/liveSources';
```

**Step 2: Add state for status**

Alongside the existing `useState` calls:

```js
const [dataStatus, setDataStatus] = useState(null);
```

**Step 3: Insert the live merge before `setConsolidatedData(base)`**

Replace the line `setConsolidatedData(base);` (around `src/hooks/useDataConsolidation.js:307`) with:

```js
                // ---- LIVE OVERRIDE (per-cell), CSV stays the fallback ----
                let finalData = base;
                let status = { l: 'csv', e: 'csv', gdp: 'csv', f: 'csv', r: 'csv', eUs: 'csv' };
                try {
                    const toMap = (settled, field) => {
                        const m = {};
                        if (settled.status === 'fulfilled' && settled.value?.rows) {
                            for (const row of settled.value.rows) {
                                const v = Number(row[field]);
                                if (Number.isFinite(v)) m[row.Country] = v;
                            }
                        }
                        return m;
                    };
                    const [wf, en, gd] = await Promise.allSettled([
                        fetchWorkforceLive(),
                        fetchEnergyLive(),       // no EIA key -> US energy stays CSV
                        fetchGdpLive(),
                    ]);
                    const live = {
                        workforce: toMap(wf, 'Workforce_Millions'),
                        energy: toMap(en, 'Industrial_Electricity_USD_per_MWh'),
                        gdp: toMap(gd, 'GDP_Trillions_USD'),
                    };
                    const res = mergeLive(base, live);
                    finalData = res.merged;
                    status = res.status;
                } catch (liveErr) {
                    // Total failure -> keep pure CSV. No regression.
                    console.warn('Live fetch failed, using CSV baseline:', liveErr);
                }

                setConsolidatedData(finalData);
                setDataStatus(status);
                setLoading(false);
```

(Remove the old `setConsolidatedData(base); setLoading(false);` lines that this replaces.)

**Step 4: Return `dataStatus`**

Change the hook return (`src/hooks/useDataConsolidation.js:319`) to:

```js
    return { consolidatedData, loading, error, dataStatus };
```

**Step 5: Verify the build**

Run: `npm run build`
Expected: build succeeds, no new errors.

**Step 6: Commit**

```bash
git add src/hooks/useDataConsolidation.js
git commit -m "feat(live): compute CACI on live data with CSV fallback"
```

---

### Task 4: Status banner in the UI

Show which factors are live vs CSV. The `CountryComparison` component already calls `useDataConsolidation`; surface the new `dataStatus` there.

**Files:**
- Modify: `src/components/CountryComparison.jsx` (read `dataStatus`, render a one-line banner)

**Step 1: Read `dataStatus` from the hook**

Find the `useDataConsolidation(...)` call in `CountryComparison.jsx` and add `dataStatus` to the destructure.

**Step 2: Render the banner**

Near the top of the returned JSX (above the chart), add:

```jsx
{dataStatus && (
  <div style={{ fontSize: '0.8rem', color: 'var(--muted, #888)', marginBottom: 8 }}>
    Data: L {dataStatus.l}, E-EU {dataStatus.e}, GDP {dataStatus.gdp}
    {' '}| CSV: F, R, E-US
  </div>
)}
```

**Step 3: Verify the build and run dev**

Run: `npm run build` then `npm run dev`
Expected: build OK. In the browser the banner reads "Data: L live, E-EU live, GDP live | CSV: F, R, E-US" when online, and "L csv, E-EU csv, GDP csv" when offline (DevTools offline).

**Step 4: Commit**

```bash
git add src/components/CountryComparison.jsx
git commit -m "feat(live): show live/CSV data status banner"
```

---

### Task 5: Offline regression check and deploy bundle

**Step 1: Verify offline fallback**

In `npm run dev`, open DevTools, set network to Offline, reload. The dashboard must still render with CACI computed from CSV, banner showing csv for all live factors. This proves no regression.

**Step 2: Build the deploy bundle**

The CI rebuilds on push to `caci-dashboard/**`, so the committed source is enough. Do NOT hand-edit `docs/dashboard/`. Confirm `npm run build` is clean.

**Step 3: Final commit (if anything pending) and open PR**

```bash
git push -u origin feature/live-data-caci
gh pr create --title "Live data for CACI dashboard (CSV fallback)" \
  --body "Auto-fetch World Bank workforce/GDP and Eurostat EU energy on load, merge per cell over the CSV baseline. F, R, US energy stay CSV. Offline falls back to pure CSV."
```

---

## Notes for the implementer

- `mergeLive` is the only pure unit. Everything else is verified by build + manual dev check, because the fetchers depend on `import.meta.env` and browser `fetch`.
- Do not commit any EIA API key. US energy stays CSV by design.
- Keep `liveSources.js`'s existing per-cell fallback logic; the hook trusts the `rows` it returns.
- The headline US/EU ratio will barely move in live mode because F (weight 0.40) stays CSV. That is expected.
