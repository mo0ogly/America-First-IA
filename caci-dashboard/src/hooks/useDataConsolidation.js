import { useState, useEffect } from 'react';
import Papa from 'papaparse';
import { fetchWorkforceLive, fetchEnergyLive, fetchGdpLive, mergeLive } from '../lib/liveSources';

// Map CSV Country Names to our standard dashboard keys
const COUNTRY_MAP = {
    // Core entities
    'United States of America': 'USA',
    'United States': 'USA',
    'USA': 'USA',
    'China': 'China',
    'Hong Kong': 'China',
    'EU': 'EU',
    'European Union': 'EU',
    'France': 'France',
    'Germany': 'Germany',
    'United Kingdom of Great Britain and Northern Ireland': 'UK',
    'United Kingdom': 'UK',
    'UK': 'UK',
    'India': 'India',
    'South America': 'South America',
    'Africa': 'Africa',
    'Asia (Ex-China)': 'Asia (Ex-China)',

    // South America
    'Brazil': 'South America',
    'Argentina': 'South America',
    'Chile': 'South America',
    'Mexico': 'South America',

    // Asia (Ex-China)
    'Japan': 'Asia (Ex-China)',
    'Korea (Republic of)': 'Asia (Ex-China)',
    'Singapore': 'Asia (Ex-China)',
    'Taiwan': 'Asia (Ex-China)',
    'United Arab Emirates': 'UAE',
    'UAE': 'UAE',
    'Saudi Arabia': 'Asia (Ex-China)',
    'Israel': 'Asia (Ex-China)',
    'Malaysia': 'Asia (Ex-China)',
    'Thailand': 'Asia (Ex-China)',
    'Indonesia': 'Asia (Ex-China)',
    'Vietnam': 'Asia (Ex-China)',
    'Philippines (the)': 'Asia (Ex-China)',
    'Australia': 'Asia (Ex-China)',

    // Africa — full continental coverage
    'South Africa': 'Africa',
    'Nigeria': 'Africa',
    'Morocco': 'Africa',
    'Egypt': 'Africa',
    'Kenya': 'Africa',
    'Ethiopia': 'Africa',
    'Ghana': 'Africa',
    'Algeria': 'Africa',
    'Tunisia': 'Africa',
    'Senegal': 'Africa',
    'Rwanda': 'Africa',
    'Tanzania': 'Africa',
    'Tanzania, United Republic of': 'Africa',
    'Uganda': 'Africa',
    'Cameroon': 'Africa',
    'Angola': 'Africa',
    'Congo': 'Africa',
    'Congo (the Democratic Republic of the)': 'Africa',
    'Mozambique': 'Africa',
    'Madagascar': 'Africa',
    'Côte d\'Ivoire': 'Africa',
    'Libya': 'Africa',
    'Sudan': 'Africa',

    // Additional EU members (also counted individually if key exists)
    'Canada': 'USA', // FVEY/NAFTA compute alliance — clusters serve US ecosystem
};

// EU-28 member states to aggregate for Factor F (EU-27 + UK pre-Brexit)
// NOTE: France, Germany, and UK are handled via EU_MEMBER_INDIVIDUAL_KEYS (counted in both)
// This list = EU-28 minus France/Germany/UK = 25 remaining members
const EU_COUNTRIES = [
    'Italy', 'Spain', 'Netherlands', 'Sweden', 'Finland', 'Poland', 'Ireland',
    'Denmark', 'Belgium', 'Austria', 'Luxembourg', 'Czechia', 'Slovenia',
    'Portugal', 'Romania', 'Bulgaria', 'Croatia', 'Hungary', 'Greece',
    'Estonia', 'Latvia', 'Lithuania', 'Malta', 'Cyprus', 'Slovakia',
];

// Map major AI entities to their home countries for Sovereign Mode filtering
const OWNER_COUNTRY_MAP = {
    // USA
    'Microsoft': 'USA',
    'Amazon': 'USA',
    'Google': 'USA',
    'Oracle': 'USA',
    'Meta AI': 'USA',
    'xAI': 'USA',
    'OpenAI': 'USA',
    'CoreWeave': 'USA',
    'Lambda Labs': 'USA',
    'Together': 'USA',
    'Inflection AI': 'USA',
    'Tesla': 'USA',
    'Anthropic': 'USA',
    'US Department of Energy': 'USA',
    'US Department of Defense': 'USA',
    'Applied Digital': 'USA',
    'Nebius AI': 'USA', // Hybrid but primarily US-Western operation
    'together.ai': 'USA',
    'Crusoe': 'USA',
    'Equinix': 'USA',
    'Stargate (OpenAI)': 'USA',
    'Andreessen Horowitz': 'USA',

    // China
    'Baidu': 'China',
    'Alibaba': 'China',
    'Tencent': 'China',
    'Huawei': 'China',
    'Z.ai (Zhipu AI)': 'China',
    'Bytedance': 'China',
    'Anonymized Chinese System': 'China',

    // France / EU
    'Mistral': 'France',
    'Sesterce': 'France',
    'Scaleway': 'France',
    'OVHcloud': 'France',
    'Fluidstack': 'France',
    'EuroHPC JU': 'EU',
    'Julich Supercomputing Center': 'Germany',

    // UAE
    'G42': 'UAE',
    'Saudi Aramco': 'Saudi Arabia',
    'DataVolt': 'Saudi Arabia',

    // India
    'Reliance Industries': 'India',
    'Yotta Data Services': 'India',

    // Japan
    'Softbank': 'Japan',
    'Sakura Internet': 'Japan',
};

export const useDataConsolidation = (sovereignMode = false) => {
    const [consolidatedData, setConsolidatedData] = useState(null);
    const [dataStatus, setDataStatus] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAndConsolidate = async () => {
            try {
                // Initialize base structure with static IMF/Tortoise AIPI indices which are not in our 4 core datasets
                const base = {
                    USA: { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 1.0, imf: 85, tortoise: 100 },
                    China: { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 0.1, imf: 60, tortoise: 62 },
                    EU: { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 1.0, imf: 74, tortoise: 36 },
                    UK: { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 1.0, imf: 75, tortoise: 41 },
                    "Asia (Ex-China)": { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 0.5, imf: 82, tortoise: 68 },
                    India: { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 0.5, imf: 62, tortoise: 45 },
                    UAE: { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 0.5, imf: 78, tortoise: 55 },
                    France: { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 1.0, imf: 72, tortoise: 35 },
                    Germany: { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 1.0, imf: 74, tortoise: 36 },
                    "South America": { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 0.5, imf: 45, tortoise: 25 },
                    Africa: { f: 0, f_total: 0, e: 0, gdp: 0, l: 0, r: 0.5, imf: 38, tortoise: 18 },
                };

                const parseCSV = (url) => {
                    return new Promise((resolve, reject) => {
                        Papa.parse(url, {
                            download: true,
                            header: true,
                            skipEmptyLines: true,
                            complete: (results) => resolve(results.data),
                            error: (err) => reject(err)
                        });
                    });
                };

                const [epochData, gdpData, energyData, workforceData] = await Promise.all([
                    parseCSV(`${import.meta.env.BASE_URL}data/gpu_clusters.csv`),
                    parseCSV(`${import.meta.env.BASE_URL}data/gdp_data.csv`),
                    parseCSV(`${import.meta.env.BASE_URL}data/energy_prices.csv`),
                    parseCSV(`${import.meta.env.BASE_URL}data/workforce_data.csv`)
                ]);

                // 1. Process GDP
                gdpData.forEach(row => {
                    const countryName = row.Country;
                    const mappedKey = COUNTRY_MAP[countryName];
                    const gdp = parseFloat(row.GDP_Trillions_USD);
                    if (mappedKey && base[mappedKey] && !isNaN(gdp)) {
                        base[mappedKey].gdp = gdp;
                    } else if (base[countryName] && !isNaN(gdp)) {
                        base[countryName].gdp = gdp;
                    }
                });

                // 2. Process Energy (USD/MWh)
                energyData.forEach(row => {
                    const countryName = row.Country;
                    const mappedKey = COUNTRY_MAP[countryName];
                    const energy = parseFloat(row.Industrial_Electricity_USD_per_MWh);
                    if (mappedKey && base[mappedKey] && !isNaN(energy)) {
                        base[mappedKey].e = energy;
                    } else if (base[countryName] && !isNaN(energy)) {
                        base[countryName].e = energy;
                    }
                });

                // 3. Process Workforce (Millions)
                workforceData.forEach(row => {
                    const countryName = row.Country;
                    const mappedKey = COUNTRY_MAP[countryName];
                    const workforce = parseFloat(row.Workforce_Millions);
                    if (mappedKey && base[mappedKey] && !isNaN(workforce)) {
                        base[mappedKey].l = workforce;
                    } else if (base[countryName] && !isNaN(workforce)) {
                        base[countryName].l = workforce;
                    }
                });

                // 4. Process Epoch AI (Factor F - Compute in PetaFLOP/s)
                // CRITICAL: France and Germany must count toward BOTH their individual keys AND the EU aggregate.
                // UK is NOT included (Brexit — UK is its own separate entity)
                const EU_MEMBER_INDIVIDUAL_KEYS = ['France', 'Germany'];

                epochData.forEach(row => {
                    let country = row.Country ? row.Country.trim() : '';
                    let status = row.Status ? row.Status.trim().toLowerCase() : '';
                    let owner = row.Owner ? row.Owner.trim() : '';

                    if (!country) return;

                    // Only count operational compute to avoid massive skew from 'planned' datacenters
                    if (status.includes('planned') || status.includes('cancelled')) return;

                    const maxOpLog = parseFloat(row['Max OP/s (log)']);
                    if (isNaN(maxOpLog)) return;
                    const pflops = Math.pow(10, maxOpLog) / 1e15;

                    let mappedKey = COUNTRY_MAP[country] || null;
                    const isEuCountry = EU_COUNTRIES.includes(country);
                    if (isEuCountry) mappedKey = 'EU';

                    if (!mappedKey || !base[mappedKey]) return;

                    // Track TOTAL physical compute regardless of sovereignty
                    base[mappedKey].f_total += pflops;
                    if (EU_MEMBER_INDIVIDUAL_KEYS.includes(mappedKey) && base['EU']) {
                        base['EU'].f_total += pflops;
                    }

                    // --- SOVEREIGN MODE FILTER ---
                    const ownerNation = OWNER_COUNTRY_MAP[owner];
                    const locationNation = COUNTRY_MAP[country] || country;

                    // Special case: US hyperscalers (even if not explicitly in map) are considered foreign to Europe/Asia
                    const isUsOwner = ownerNation === 'USA' || 
                                        owner.toLowerCase().includes('microsoft') || 
                                        owner.toLowerCase().includes('amazon') || 
                                        owner.toLowerCase().includes('google') ||
                                        owner.toLowerCase().includes('azure') ||
                                        owner.toLowerCase().includes('oracle');
                    
                    const isForeign = ownerNation && ownerNation !== locationNation;
                    const isSovereign = !(isForeign || (isUsOwner && locationNation !== 'USA'));

                    if (isSovereign) {
                        base[mappedKey].f += pflops;
                        if (EU_MEMBER_INDIVIDUAL_KEYS.includes(mappedKey) && base['EU']) {
                            base['EU'].f += pflops;
                        }
                    }
                });

                // Apply documented baselines for entities not fully covered by CSV sources
                // Sources: IMF WEO 2025, IEA 2025, World Bank 2025
                const DOCUMENTED_BASELINES = {
                    'UAE': { f: 85, f_total: 620, e: 80, gdp: 0.51, l: 0.15 },
                    'India': { f: 80, f_total: 150 },
                    'South America': { e: 95, gdp: 5.4, l: 1.8 },
                    'Africa': { e: 110, gdp: 3.1, l: 0.6 },
                };

                Object.keys(base).forEach(k => {
                    base[k].f_total = Math.round(base[k].f_total);
                    base[k].f = Math.round(base[k].f);

                    const bl = DOCUMENTED_BASELINES[k];

                    // Apply compute baselines if data is sparse
                    if ((base[k].f_total < 5 || k === 'UAE') && bl) {
                        if (bl.f_total) base[k].f_total = bl.f_total;
                        if (bl.f) base[k].f = bl.f;
                    } else if (base[k].f_total < 5) {
                        base[k].f_total = 10;
                        base[k].f = 10;
                    }

                    // Apply non-compute baselines for entities missing from CSV sources
                    if (bl) {
                        if (base[k].e === 0 && bl.e) base[k].e = bl.e;
                        if (base[k].gdp === 0 && bl.gdp) base[k].gdp = bl.gdp;
                        if (base[k].l === 0 && bl.l) base[k].l = bl.l;
                    }
                });

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
            } catch (err) {
                console.error(err);
                setError(err.message);
                setLoading(false);
            }
        };

        fetchAndConsolidate();
    }, [sovereignMode]);

    return { consolidatedData, loading, error, dataStatus };
};
