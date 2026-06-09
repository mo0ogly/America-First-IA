import csv
import math
import os
import sys

# Paths to the CSV files in caci-dashboard/public/data/
BASE_DIR = r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main"
DATA_DIR = os.path.join(BASE_DIR, "caci-dashboard", "public", "data")
GPU_CLUSTERS = os.path.join(DATA_DIR, "gpu_clusters.csv")
GDP_DATA = os.path.join(DATA_DIR, "gdp_data.csv")
ENERGY_PRICES = os.path.join(DATA_DIR, "energy_prices.csv")
WORKFORCE_DATA = os.path.join(DATA_DIR, "workforce_data.csv")

# Standard country maps from useDataConsolidation.js
COUNTRY_MAP = {
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
    'Brazil': 'South America',
    'Argentina': 'South America',
    'Chile': 'South America',
    'Mexico': 'South America',
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
    "Côte d'Ivoire": 'Africa',
    'Libya': 'Africa',
    'Sudan': 'Africa',
    'Canada': 'USA',
}

EU_COUNTRIES = [
    'Italy', 'Spain', 'Netherlands', 'Sweden', 'Finland', 'Poland', 'Ireland',
    'Denmark', 'Belgium', 'Austria', 'Luxembourg', 'Czechia', 'Slovenia',
    'Portugal', 'Romania', 'Bulgaria', 'Croatia', 'Hungary', 'Greece',
    'Estonia', 'Latvia', 'Lithuania', 'Malta', 'Cyprus', 'Slovakia',
]

OWNER_COUNTRY_MAP = {
    'Microsoft': 'USA', 'Amazon': 'USA', 'Google': 'USA', 'Oracle': 'USA',
    'Meta AI': 'USA', 'xAI': 'USA', 'OpenAI': 'USA', 'CoreWeave': 'USA',
    'Lambda Labs': 'USA', 'Together': 'USA', 'Inflection AI': 'USA',
    'Tesla': 'USA', 'Anthropic': 'USA', 'US Department of Energy': 'USA',
    'US Department of Defense': 'USA', 'Applied Digital': 'USA',
    'Nebius AI': 'USA', 'together.ai': 'USA', 'Crusoe': 'USA',
    'Equinix': 'USA', 'Stargate (OpenAI)': 'USA', 'Andreessen Horowitz': 'USA',
    'Baidu': 'China', 'Alibaba': 'China', 'Tencent': 'China', 'Huawei': 'China',
    'Z.ai (Zhipu AI)': 'China', 'Bytedance': 'China', 'Anonymized Chinese System': 'China',
    'Mistral': 'France', 'Sesterce': 'France', 'Scaleway': 'France',
    'OVHcloud': 'France', 'Fluidstack': 'France', 'EuroHPC JU': 'EU',
    'Julich Supercomputing Center': 'Germany', 'G42': 'UAE',
    'Saudi Aramco': 'Saudi Arabia', 'DataVolt': 'Saudi Arabia',
    'Reliance Industries': 'India', 'Yotta Data Services': 'India',
    'Softbank': 'Japan', 'Sakura Internet': 'Japan',
}

# Geopolitical tiers (R values) from live dashboard
R_TIERS = {
    'USA': 1.0, 'China': 0.1, 'EU': 1.0, 'UK': 1.0, 'Asia (Ex-China)': 0.5,
    'India': 0.5, 'UAE': 0.5, 'France': 1.0, 'Germany': 1.0, 'South America': 0.5, 'Africa': 0.5
}

def load_caci_data():
    """Parse CSV files and calculate CACI metrics, mirroring useDataConsolidation.js."""
    base = {
        'USA': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['USA']},
        'China': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['China']},
        'EU': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['EU']},
        'UK': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['UK']},
        'Asia (Ex-China)': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['Asia (Ex-China)']},
        'India': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['India']},
        'UAE': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0.62, 'l': 0, 'r': R_TIERS['UAE']},
        'France': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['France']},
        'Germany': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['Germany']},
        'South America': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['South America']},
        'Africa': {'f': 0, 'f_total': 0, 'e': 0, 'gdp': 0, 'l': 0, 'r': R_TIERS['Africa']},
    }

    # 1. Process GDP
    with open(GDP_DATA, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country = row['Country'].strip()
            gdp = float(row['GDP_Trillions_USD'])
            mapped = COUNTRY_MAP.get(country, country)
            if mapped in base:
                base[mapped]['gdp'] = gdp

    # 2. Process Energy Prices
    with open(ENERGY_PRICES, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country = row['Country'].strip()
            energy = float(row['Industrial_Electricity_USD_per_MWh'])
            mapped = COUNTRY_MAP.get(country, country)
            if mapped in base:
                base[mapped]['e'] = energy

    # 3. Process Workforce
    with open(WORKFORCE_DATA, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country = row['Country'].strip()
            workforce = float(row['Workforce_Millions'])
            mapped = COUNTRY_MAP.get(country, country)
            if mapped in base:
                base[mapped]['l'] = workforce

    # 4. Process GPU Clusters
    EU_MEMBER_INDIVIDUAL_KEYS = ['France', 'Germany']
    with open(GPU_CLUSTERS, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country = row.get('Country', '').strip()
            status = row.get('Status', '').strip().lower()
            owner = row.get('Owner', '').strip()

            if not country:
                continue
            if 'planned' in status or 'cancelled' in status:
                continue

            max_op_log = row.get('Max OP/s (log)', '')
            if not max_op_log:
                continue
            try:
                pflops = (10 ** float(max_op_log)) / 1e15
            except ValueError:
                continue

            mapped_key = COUNTRY_MAP.get(country)
            if country in EU_COUNTRIES:
                mapped_key = 'EU'

            if not mapped_key or mapped_key not in base:
                continue

            base[mapped_key]['f_total'] += pflops
            if mapped_key in EU_MEMBER_INDIVIDUAL_KEYS:
                base['EU']['f_total'] += pflops

            owner_nation = OWNER_COUNTRY_MAP.get(owner)
            location_nation = COUNTRY_MAP.get(country, country)

            is_us_owner = (
                owner_nation == 'USA' or 
                'microsoft' in owner.lower() or 
                'amazon' in owner.lower() or 
                'google' in owner.lower() or
                'azure' in owner.lower() or 
                'oracle' in owner.lower()
            )
            is_foreign = owner_nation and owner_nation != location_nation
            is_sovereign = not (is_foreign or (is_us_owner and location_nation != 'USA'))

            if is_sovereign:
                base[mapped_key]['f'] += pflops
                if mapped_key in EU_MEMBER_INDIVIDUAL_KEYS:
                    base['EU']['f'] += pflops

    # Apply documented baselines
    DOCUMENTED_BASELINES = {
        'UAE': {'f': 85, 'f_total': 620, 'e': 80, 'gdp': 0.62, 'l': 0.15},
        'India': {'f': 80, 'f_total': 150},
        'South America': {'e': 95, 'gdp': 5.4, 'l': 1.8},
        'Africa': {'e': 110, 'gdp': 3.1, 'l': 0.6},
    }

    for k in base:
        base[k]['f_total'] = round(base[k]['f_total'])
        base[k]['f'] = round(base[k]['f'])

        bl = DOCUMENTED_BASELINES.get(k)
        if (base[k]['f_total'] < 5 or k == 'UAE') and bl:
            if 'f_total' in bl: base[k]['f_total'] = bl['f_total']
            if 'f' in bl: base[k]['f'] = bl['f']
        elif base[k]['f_total'] < 5:
            base[k]['f_total'] = 10
            base[k]['f'] = 10

        if bl:
            if base[k]['e'] == 0 and 'e' in bl: base[k]['e'] = bl['e']
            if base[k]['gdp'] == 0 and 'gdp' in bl: base[k]['gdp'] = bl['gdp']
            if base[k]['l'] == 0 and 'l' in bl: base[k]['l'] = bl['l']

    # 5. CACI Calculations
    wf, we, wl, wr = 0.40, 0.25, 0.20, 0.15

    raw_power_phys = {}
    raw_power_sov = {}
    raw_intensity_phys = {}
    raw_intensity_sov = {}

    for k, d in base.items():
        f_p = d['f_total']
        f_s = d['f']
        l = d['l']
        r = d['r']
        e = d['e']
        gdp = d['gdp']

        if f_p >= 15:
            raw_power_phys[k] = (f_p ** wf * l ** wl * r ** wr) / (e ** we)
            raw_intensity_phys[k] = (f_p ** wf * l ** wl * r ** wr) / ((e ** we) * gdp)
        else:
            raw_power_phys[k] = 0.0
            raw_intensity_phys[k] = 0.0

        if f_s >= 15:
            raw_power_sov[k] = (f_s ** wf * l ** wl * r ** wr) / (e ** we)
            raw_intensity_sov[k] = (f_s ** wf * l ** wl * r ** wr) / ((e ** we) * gdp)
        else:
            raw_power_sov[k] = 0.0
            raw_intensity_sov[k] = 0.0

    # Normalization (USA Physical = 100)
    usa_power_phys = raw_power_phys['USA']
    usa_intensity_phys = raw_intensity_phys['USA']

    results = {}
    for k in base:
        results[k] = {
            'f_total': base[k]['f_total'],
            'f_sov': base[k]['f'],
            'e': base[k]['e'],
            'l': base[k]['l'],
            'gdp': base[k]['gdp'],
            'r': base[k]['r'],
            'caci_power_phys': (raw_power_phys[k] / usa_power_phys) * 100 if usa_power_phys > 0 else 0.0,
            'caci_power_sov': (raw_power_sov[k] / usa_power_phys) * 100 if usa_power_phys > 0 else 0.0,
            'caci_intensity_phys': (raw_intensity_phys[k] / usa_intensity_phys) * 100 if usa_intensity_phys > 0 else 0.0,
            'caci_intensity_sov': (raw_intensity_sov[k] / usa_intensity_phys) * 100 if usa_intensity_phys > 0 else 0.0,
        }

    # Calculate global totals and shares
    total_operational_compute = sum(base[k]['f_total'] for k in base if k != 'EU') # Avoid double counting EU with France/Germany
    # Note: EU is France + Germany + EU_COUNTRIES. If we sum base.keys() except EU, we get:
    # USA, China, UK, Asia (Ex-China), India, UAE, France, Germany, South America, Africa
    # Let's verify if that matches the global operational compute.
    # Total of the individual regions = USA + China + UK + Asia (Ex-China) + India + UAE + EU + South America + Africa
    # Since EU = France + Germany + EU_COUNTRIES, the sum is USA + China + UK + Asia + India + UAE + EU + South America + Africa
    # Let's sum exactly:
    individual_keys = ['USA', 'China', 'UK', 'Asia (Ex-China)', 'India', 'UAE', 'EU', 'South America', 'Africa']
    global_compute = sum(base[k]['f_total'] for k in individual_keys)
    us_compute_share = (base['USA']['f_total'] / global_compute) * 100 if global_compute > 0 else 0.0

    # Ratios
    us_eu_raw_ratio = base['USA']['f_total'] / base['EU']['f_total'] if base['EU']['f_total'] > 0 else 0.0
    us_eu_caci_power_ratio = raw_power_phys['USA'] / raw_power_phys['EU'] if raw_power_phys['EU'] > 0 else 0.0
    us_france_caci_power_ratio = raw_power_phys['USA'] / raw_power_phys['France'] if raw_power_phys['France'] > 0 else 0.0
    us_germany_caci_power_ratio = raw_power_phys['USA'] / raw_power_phys['Germany'] if raw_power_phys['Germany'] > 0 else 0.0
    us_china_caci_power_ratio = raw_power_phys['USA'] / raw_power_phys['China'] if raw_power_phys['China'] > 0 else 0.0

    eu_sovereignty_ratio = (base['EU']['f'] / base['EU']['f_total']) * 100 if base['EU']['f_total'] > 0 else 0.0

    metrics = {
        'global_compute': global_compute,
        'us_compute_share': us_compute_share,
        'us_eu_raw_ratio': us_eu_raw_ratio,
        'us_eu_caci_power_ratio': us_eu_caci_power_ratio,
        'us_france_caci_power_ratio': us_france_caci_power_ratio,
        'us_germany_caci_power_ratio': us_germany_caci_power_ratio,
        'us_china_caci_power_ratio': us_china_caci_power_ratio,
        'eu_sovereignty_ratio': eu_sovereignty_ratio,
        'country_results': results,
    }

    return metrics

# Cached metrics for fast access
_metrics = None

def get_metrics():
    global _metrics
    if _metrics is None:
        _metrics = load_caci_data()
    return _metrics

# Specific helper formats
def get_formatted_kpis(lang="EN"):
    m = get_metrics()
    
    # Render with proper locale decimals (comma for FR/PT-BR, point for EN)
    def fmt_pct(val):
        if lang == "EN":
            return f"{val:.1f}%"
        else:
            return f"{str(round(val, 1)).replace('.', ',')}%" if lang == "PT-BR" else f"{str(round(val, 1)).replace('.', ',')} pct"

    def fmt_mult(val):
        if lang == "EN":
            return f"{val:.2f}x"
        else:
            return f"{str(round(val, 2)).replace('.', ',')}x"

    def fmt_ratio(val):
        if lang == "EN":
            return f"{val:.2f}:1"
        else:
            return f"{str(round(val, 2)).replace('.', ',')}:1"

    if lang == "FR":
        return [
            f"{fmt_pct(m['us_compute_share'])} du compute IA operationnel mondial = USA",
            "1,59x cout energie EU/US (ajuste-PPA)",  # keep energy baseline cost ratio stable as defined
            f"{fmt_ratio(m['us_eu_caci_power_ratio'])} ratio CACI US/EU (Power Mode)"
        ]
    elif lang == "PT-BR":
        return [
            f"{fmt_pct(m['us_compute_share'])} da computacao de IA operacional global = EUA",
            "1,59x custo de energia UE/EUA (ajustado-PPP)",
            f"{fmt_ratio(m['us_eu_caci_power_ratio'])} ratio CACI EUA/UE (Power Mode)"
        ]
    else:  # EN
        return [
            f"{fmt_pct(m['us_compute_share'])} of global operational AI compute = USA",
            "1.59x energy cost EU/US (PPP-adjusted)",
            f"{fmt_ratio(m['us_eu_caci_power_ratio'])} US/EU CACI ratio (Power Mode)"
        ]

if __name__ == "__main__":
    # Test script output
    m = load_caci_data()
    print("US Compute Share:", m['us_compute_share'])
    print("US/EU CACI Power Ratio:", m['us_eu_caci_power_ratio'])
    print("EU Sovereignty Ratio:", m['eu_sovereignty_ratio'])
    print("Formatted KPIs (FR):", get_formatted_kpis("FR"))
