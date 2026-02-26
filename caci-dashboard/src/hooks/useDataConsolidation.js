import { useState, useEffect } from 'react';
import Papa from 'papaparse';

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
    'United Arab Emirates': 'Asia (Ex-China)',
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

// European countries to aggregate into the "EU" entity for Factor F
// This covers the FULL European continent (as per the user's geographic scope)
// NOTE: France, Germany, and UK are handled separately via EU_MEMBER_INDIVIDUAL_KEYS
const EU_COUNTRIES = [
    // EU-27 members (excluding France/Germany which have own dashboard keys)
    'Italy', 'Spain', 'Netherlands', 'Sweden', 'Finland', 'Poland', 'Ireland',
    'Denmark', 'Belgium', 'Austria', 'Luxembourg', 'Czechia', 'Slovenia',
    'Portugal', 'Romania', 'Bulgaria', 'Croatia', 'Hungary', 'Greece',
    'Estonia', 'Latvia', 'Lithuania', 'Malta', 'Cyprus', 'Slovakia',
    // EEA / EFTA / European non-EU
    'Norway', 'Switzerland', 'Iceland', 'Liechtenstein',
    // Wider European continent
    'Russia', 'Ukraine', 'Belarus', 'Serbia', 'Turkey', 'Türkiye',
    'Bosnia and Herzegovina', 'Montenegro', 'North Macedonia', 'Albania',
    'Moldova', 'Moldova (Republic of)', 'Andorra', 'San Marino',
];

export const useDataConsolidation = () => {
    const [consolidatedData, setConsolidatedData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAndConsolidate = async () => {
            try {
                // Initialize base structure with static IMF/Tortoise AIPI indices which are not in our 4 core datasets
                const base = {
                    USA: { f: 0, e: 0, gdp: 0, l: 0, imf: 85, tortoise: 100 },
                    China: { f: 0, e: 0, gdp: 0, l: 0, imf: 60, tortoise: 62 },
                    EU: { f: 0, e: 0, gdp: 0, l: 0, imf: 74, tortoise: 36 },
                    UK: { f: 0, e: 0, gdp: 0, l: 0, imf: 75, tortoise: 41 },
                    "Asia (Ex-China)": { f: 0, e: 0, gdp: 0, l: 0, imf: 82, tortoise: 68 },
                    India: { f: 0, e: 0, gdp: 0, l: 0, imf: 62, tortoise: 45 },
                    France: { f: 0, e: 0, gdp: 0, l: 0, imf: 72, tortoise: 35 },
                    Germany: { f: 0, e: 0, gdp: 0, l: 0, imf: 74, tortoise: 36 },
                    "South America": { f: 0, e: 0, gdp: 0, l: 0, imf: 52, tortoise: 28 },
                    Africa: { f: 0, e: 0, gdp: 0, l: 0, imf: 40, tortoise: 20 },
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
                    const country = row.Country;
                    const gdp = parseFloat(row.GDP_Trillions_USD);
                    if (base[country] && !isNaN(gdp)) {
                        base[country].gdp = gdp;
                    }
                });

                // 2. Process Energy (USD/MWh)
                energyData.forEach(row => {
                    const country = row.Country;
                    const energy = parseFloat(row.Industrial_Electricity_USD_per_MWh);
                    if (base[country] && !isNaN(energy)) {
                        base[country].e = energy;
                    }
                });

                // 3. Process Workforce (Millions)
                workforceData.forEach(row => {
                    const country = row.Country;
                    const workforce = parseFloat(row.Workforce_Millions);
                    if (base[country] && !isNaN(workforce)) {
                        base[country].l = workforce;
                    }
                });

                // 4. Process Epoch AI (Factor F - Compute in PetaFLOP/s)
                // CRITICAL: France, Germany, and UK must count toward BOTH their individual keys AND the EU/Europe aggregate.
                const EU_MEMBER_INDIVIDUAL_KEYS = ['France', 'Germany', 'UK']; // Countries with their own dashboard key that also belong to Europe

                epochData.forEach(row => {
                    let country = row.Country ? row.Country.trim() : '';
                    let status = row.Status ? row.Status.trim().toLowerCase() : '';

                    if (!country) return;

                    // Only count operational compute to avoid massive skew from 'planned' datacenters
                    if (status.includes('planned') || status.includes('cancelled')) return;

                    const maxOpLog = parseFloat(row['Max OP/s (log)']);
                    if (isNaN(maxOpLog)) return;

                    const pflops = Math.pow(10, maxOpLog) / 1e15;

                    let mappedKey = COUNTRY_MAP[country] || null;
                    const isEuCountry = EU_COUNTRIES.includes(country);
                    if (isEuCountry) mappedKey = 'EU';

                    // Add compute to the primary mapped entity
                    if (mappedKey && base[mappedKey]) {
                        base[mappedKey].f += pflops;
                    }

                    // ALSO add to EU aggregate if this country is an EU member with its own individual key
                    if (EU_MEMBER_INDIVIDUAL_KEYS.includes(mappedKey) && base['EU']) {
                        base['EU'].f += pflops;
                    }
                });

                // Round Factor F to nearest integer for clean display and assign baseline minimums
                Object.keys(base).forEach(k => {
                    base[k].f = Math.round(base[k].f);
                    if (base[k].f <= 5) {
                        // Fallback heuristic: If the country wasn't explicitly in the Epoch DB as having an operational supercomputer,
                        // assign a nominal baseline score indicative of general civilian cloud compute to avoid divide-by-zero
                        base[k].f = k === 'Africa' ? 8 : k === 'South America' ? 12 : k === 'France' ? 15 : k === 'Germany' ? 18 : 10;
                    }
                });

                setConsolidatedData(base);
                setLoading(false);
            } catch (err) {
                console.error(err);
                setError(err.message);
                setLoading(false);
            }
        };

        fetchAndConsolidate();
    }, []);

    return { consolidatedData, loading, error };
};
