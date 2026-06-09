/**
 * Browser-side live data fetchers for the CACI factors.
 *
 * Mirrors the Python scripts in /scripts (extract_workforce.py,
 * extract_energy_prices.py) so the dashboard can refresh Factor L (STEM
 * workforce, World Bank) and Factor E (industrial electricity price,
 * Eurostat + optional EIA) directly from the source APIs, then offer the
 * regenerated CSV for download (the static site cannot write the repo).
 *
 * All endpoints used here send permissive CORS headers (World Bank,
 * Eurostat, Frankfurter/ECB, EIA), so they work from the browser.
 *
 * Fallback: the committed CSV in public/data/ is the baseline. Each fetcher
 * starts from it, overrides what it can fetch live, and keeps the CSV value
 * for any source that is unavailable or fails.
 */

// ----- CSV baseline loader (fallback source) --------------------------------

const BASE_URL = (import.meta?.env?.BASE_URL) || '/';

// Minimal CSV parser: header row + comma split, supports one level of quoting.
function parseCSV(text) {
  const lines = text.trim().split(/\r?\n/);
  const headers = splitCSVLine(lines[0]);
  return lines.slice(1).filter(Boolean).map((line) => {
    const cells = splitCSVLine(line);
    const obj = {};
    headers.forEach((h, i) => { obj[h] = cells[i]; });
    return obj;
  });
}

function splitCSVLine(line) {
  const out = [];
  let cur = '';
  let inQ = false;
  for (let i = 0; i < line.length; i += 1) {
    const ch = line[i];
    if (ch === '"') { inQ = !inQ; continue; }
    if (ch === ',' && !inQ) { out.push(cur); cur = ''; continue; }
    cur += ch;
  }
  out.push(cur);
  return out;
}

async function loadBaselineCSV(filename) {
  try {
    const res = await fetch(`${BASE_URL}data/${filename}`);
    if (!res.ok) return {};
    const rows = parseCSV(await res.text());
    const map = {};
    for (const r of rows) map[r.Country] = r;
    return map;
  } catch {
    return {};
  }
}

// ----- Factor L: STEM workforce (World Bank) --------------------------------

const WB = 'https://api.worldbank.org/v2';
const RD = 'SP.POP.SCIE.RD.P6'; // researchers in R&D per million people
const POP = 'SP.POP.TOTL'; // total population

const WORKFORCE_ROW_ORDER = [
  'USA', 'China', 'EU', 'UK', 'Asia (Ex-China)',
  'India', 'France', 'Germany', 'South America', 'Africa',
];

const SINGLE = {
  USA: 'USA', China: 'CHN', UK: 'GBR',
  India: 'IND', France: 'FRA', Germany: 'DEU',
};

const EU27 = ['AUT', 'BEL', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 'FIN', 'FRA',
  'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LTU', 'LUX', 'MLT', 'NLD',
  'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'SWE'];

const SOUTH_AMERICA = ['ARG', 'BOL', 'BRA', 'CHL', 'COL', 'ECU', 'GUY', 'PRY',
  'PER', 'SUR', 'URY', 'VEN'];

const AFRICA = ['DZA', 'AGO', 'BEN', 'BWA', 'BFA', 'BDI', 'CPV', 'CMR', 'CAF', 'TCD',
  'COM', 'COG', 'COD', 'CIV', 'DJI', 'EGY', 'GNQ', 'ERI', 'SWZ', 'ETH',
  'GAB', 'GMB', 'GHA', 'GIN', 'GNB', 'KEN', 'LSO', 'LBR', 'LBY', 'MDG',
  'MWI', 'MLI', 'MRT', 'MUS', 'MAR', 'MOZ', 'NAM', 'NER', 'NGA', 'RWA',
  'STP', 'SEN', 'SYC', 'SLE', 'SOM', 'ZAF', 'SSD', 'SDN', 'TZA', 'TGO',
  'TUN', 'UGA', 'ZMB', 'ZWE'];

// Asia excluding China (includes India; Middle East excluded).
const ASIA_EX_CHINA = ['IND', 'JPN', 'KOR', 'PRK', 'MNG', 'TWN', 'HKG',
  'IDN', 'MYS', 'PHL', 'SGP', 'THA', 'VNM', 'KHM', 'LAO', 'MMR', 'BRN', 'TLS',
  'PAK', 'BGD', 'LKA', 'NPL', 'BTN', 'MDV', 'AFG',
  'KAZ', 'UZB', 'TKM', 'KGZ', 'TJK'];

async function wbFetchAll(indicator) {
  // Most-recent-non-empty value per country -> { iso3: { year, value } }
  const url = `${WB}/country/all/indicator/${indicator}?format=json&mrnev=1&per_page=400`;
  const res = await fetch(url);
  if (!res.ok) throw new Error(`World Bank ${indicator} HTTP ${res.status}`);
  const payload = await res.json();
  const out = {};
  if (!Array.isArray(payload) || payload.length < 2 || !payload[1]) return out;
  for (const row of payload[1]) {
    if (row.value == null) continue;
    const iso3 = row.countryiso3code;
    if (iso3) out[iso3] = { year: row.date, value: Number(row.value) };
  }
  return out;
}

function absMillions(iso3, rd, pop) {
  if (!rd[iso3] || !pop[iso3]) return null;
  // (per_million * pop / 1e6) researchers, then / 1e6 -> millions
  return (rd[iso3].value * pop[iso3].value) / 1e12;
}

function regionSum(members, rd, pop) {
  let total = 0;
  let reporting = 0;
  for (const iso3 of members) {
    const m = absMillions(iso3, rd, pop);
    if (m != null) { total += m; reporting += 1; }
  }
  return { value: Number(total.toFixed(3)), reporting, count: members.length };
}

/**
 * Fetch Factor L live from the World Bank, with the committed CSV as fallback.
 * Returns { rows: [{Country, Workforce_Millions}], audit: {key: string} }.
 */
export async function fetchWorkforceLive() {
  // Baseline from the committed CSV (fallback if the live API is unavailable).
  const baseline = await loadBaselineCSV('workforce_data.csv');
  const results = {};
  const audit = {};
  for (const key of WORKFORCE_ROW_ORDER) {
    if (baseline[key]) {
      results[key] = Number(baseline[key].Workforce_Millions);
      audit[key] = 'CSV fallback';
    }
  }

  let rd;
  let pop;
  try {
    [rd, pop] = await Promise.all([wbFetchAll(RD), wbFetchAll(POP)]);
  } catch (e) {
    // Keep the CSV baseline entirely.
    const rows = WORKFORCE_ROW_ORDER
      .filter((k) => k in results)
      .map((k) => ({ Country: k, Workforce_Millions: results[k] }));
    return { rows, audit, error: `World Bank unavailable, using CSV (${e.message})` };
  }

  for (const [key, iso3] of Object.entries(SINGLE)) {
    const m = absMillions(iso3, rd, pop);
    if (m == null) continue; // keep CSV fallback
    results[key] = Number(m.toFixed(3));
    audit[key] = `${iso3} (yr ${rd[iso3].year})`;
  }

  const regions = [
    ['EU', EU27], ['South America', SOUTH_AMERICA],
    ['Africa', AFRICA], ['Asia (Ex-China)', ASIA_EX_CHINA],
  ];
  for (const [key, members] of regions) {
    const r = regionSum(members, rd, pop);
    if (r.reporting === 0) continue; // keep CSV fallback
    results[key] = r.value;
    audit[key] = `sum of ${r.reporting}/${r.count} reporting countries`;
  }

  const rows = WORKFORCE_ROW_ORDER
    .filter((k) => k in results)
    .map((k) => ({ Country: k, Workforce_Millions: results[k] }));
  return { rows, audit };
}

// ----- Factor E: industrial electricity price (Eurostat + EIA) --------------

const ENERGY_ROW_ORDER = ['USA', 'China', 'France', 'Germany', 'UK', 'India',
  'South America', 'Africa', 'Asia (Ex-China)', 'EU'];

const EUROSTAT_GEO = { France: 'FR', Germany: 'DE', EU: 'EU27_2020' };

// Proxy values for markets with no free authoritative API (USD/MWh).
const ENERGY_PROXY = {
  USA: 85, UK: 190, China: 92, India: 88,
  'South America': 95, Africa: 110, 'Asia (Ex-China)': 120,
};

function eurostatUrl(geo) {
  return 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'
    + `nrg_pc_205?format=JSON&unit=KWH&siec=E7000&tax=X_VAT&currency=EUR`
    + `&nrg_cons=MWH20000-69999&geo=${geo}`;
}

async function eurUsdRate() {
  // Frankfurter mirrors ECB reference rates and sends CORS headers.
  const res = await fetch('https://api.frankfurter.dev/v1/latest?base=EUR&symbols=USD');
  if (!res.ok) throw new Error(`FX HTTP ${res.status}`);
  const d = await res.json();
  return Number(d.rates.USD);
}

async function eurostatLatest(geo) {
  const res = await fetch(eurostatUrl(geo));
  if (!res.ok) throw new Error(`Eurostat ${geo} HTTP ${res.status}`);
  const d = await res.json();
  if (d.error || !d.value) return null;
  const idx = d.dimension.time.category.index; // { "2025-S2": 5, ... }
  const inv = {};
  for (const [k, v] of Object.entries(idx)) inv[v] = k;
  const pairs = Object.entries(d.value)
    .map(([i, val]) => [inv[i], val])
    .sort((a, b) => (a[0] < b[0] ? -1 : 1));
  return pairs.length ? pairs[pairs.length - 1] : null; // [semester, EUR/kWh]
}

async function eiaUsIndustrial(apiKey) {
  // US industrial retail price (cents/kWh) -> USD/MWh. Requires a free key.
  const url = 'https://api.eia.gov/v2/electricity/retail-sales/data/'
    + `?api_key=${encodeURIComponent(apiKey)}&frequency=annual&data[0]=price`
    + '&facets[sectorid][]=IND&facets[stateid][]=US'
    + '&sort[0][column]=period&sort[0][direction]=desc&length=1';
  const res = await fetch(url);
  if (!res.ok) throw new Error(`EIA HTTP ${res.status}`);
  const d = await res.json();
  const rec = d?.response?.data?.[0];
  if (!rec || rec.price == null) return null;
  return { usdMwh: Number((rec.price * 10).toFixed(1)), year: rec.period };
}

/**
 * Fetch Factor E live, with the committed CSV as fallback. eiaKey is optional;
 * when absent (or on error) USA keeps its CSV value. Eurostat overrides
 * France/Germany/EU; every other market keeps the committed CSV value (the
 * non-API markets), falling back to a built-in constant only if the CSV lacks
 * the row.
 * Returns { rows: [{Country, Industrial_Electricity_USD_per_MWh}], audit }.
 */
export async function fetchEnergyLive(eiaKey) {
  const baseline = await loadBaselineCSV('energy_prices.csv');
  const results = {};
  const audit = {};

  // Start from the committed CSV (or the built-in proxy if a row is missing).
  for (const key of ENERGY_ROW_ORDER) {
    if (baseline[key]) {
      results[key] = Number(baseline[key].Industrial_Electricity_USD_per_MWh);
      audit[key] = 'CSV fallback';
    } else if (key in ENERGY_PROXY) {
      results[key] = ENERGY_PROXY[key];
      audit[key] = 'proxy (no free API)';
    }
  }

  // Live override: EU bloc via Eurostat (per-geo, keep CSV on failure).
  let rate = null;
  try {
    rate = await eurUsdRate();
  } catch (e) {
    audit._fx = `FX unavailable, EU bloc kept from CSV (${e.message})`;
  }
  if (rate) {
    await Promise.all(Object.entries(EUROSTAT_GEO).map(async ([key, geo]) => {
      try {
        const latest = await eurostatLatest(geo);
        if (!latest) return; // keep CSV fallback
        const [sem, eurKwh] = latest;
        results[key] = Number((eurKwh * 1000 * rate).toFixed(1));
        audit[key] = `Eurostat ${geo} ${sem}, ${eurKwh} EUR/kWh`;
      } catch {
        // keep CSV fallback for this geo
      }
    }));
  }

  // Live override: USA via EIA when a key is supplied.
  if (eiaKey) {
    try {
      const usa = await eiaUsIndustrial(eiaKey);
      if (usa) {
        results.USA = usa.usdMwh;
        audit.USA = `EIA ELEC retail-sales US-IND ${usa.year}`;
      }
    } catch (e) {
      audit.USA = `${audit.USA || 'CSV fallback'} (EIA error: ${e.message})`;
    }
  }

  const rows = ENERGY_ROW_ORDER
    .filter((k) => k in results)
    .map((k) => ({ Country: k, Industrial_Electricity_USD_per_MWh: results[k] }));
  return { rows, audit, rate };
}

// ----- CSV download helper --------------------------------------------------

/**
 * Build a CSV string from rows (array of objects) using the given column order,
 * then trigger a browser download. Quotes any field containing a comma.
 */
export function downloadCSV(filename, rows, columns) {
  const esc = (v) => {
    const s = String(v);
    return s.includes(',') ? `"${s}"` : s;
  };
  const lines = [columns.join(',')];
  for (const row of rows) lines.push(columns.map((c) => esc(row[c])).join(','));
  const blob = new Blob([lines.join('\n') + '\n'], { type: 'text/csv;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
