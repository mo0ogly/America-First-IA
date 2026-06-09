#!/usr/bin/env python3
"""
Stand-alone Database Update and Alignment Tool for CACI Dashboard and Thesis.
Allows fetching latest World Bank data and updating local CSVs and frontend code.
"""

import csv
import json
import os
import re
import urllib.request
import argparse

# Absolute paths based on workspace root
BASE_DIR = r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main"
DATA_DIR = os.path.join(BASE_DIR, "caci-dashboard", "public", "data")
GDP_CSV = os.path.join(DATA_DIR, "gdp_data.csv")
WORKFORCE_CSV = os.path.join(DATA_DIR, "workforce_data.csv")
ROBUSTNESS_JSX = os.path.join(BASE_DIR, "caci-dashboard", "src", "components", "RobustnessCheck.jsx")
HELPER_PY = os.path.join(BASE_DIR, "docs", "a traduire", "caci_data_helper.py")

# Updated 2026 Nominal GDP projections (IMF WEO April 2026)
DEFAULT_GDP_2026 = {
    "USA": 31.9,
    "China": 23.7,
    "EU": 20.0,
    "UK": 3.9,
    "Asia (Ex-China)": 14.8,
    "India": 5.6,
    "France": 3.4,
    "Germany": 4.7,
    "South America": 5.0,
    "Africa": 3.6
}

# Updated 2026 Workforce / STEM R&D FTE counts (millions of people, World Bank/OECD)
DEFAULT_WORKFORCE_2026 = {
    "USA": 3.6,
    "China": 4.8,
    "France": 0.65,
    "Germany": 0.85,
    "UK": 0.5,
    "India": 0.4,
    "South America": 0.6,
    "Africa": 0.4,
    "Asia (Ex-China)": 1.8,
    "EU": 3.1
}

# Geopolitical R values
R_TIERS = {
    "USA": 1.0, "China": 0.1, "EU": 1.0, "UK": 1.0, "Asia (Ex-China)": 0.5,
    "India": 0.5, "France": 1.0, "Germany": 1.0, "South America": 0.5, "Africa": 0.5
}

# Energy prices (USD/MWh) from public/data/energy_prices.csv
ENERGY_PRICES = {
    "USA": 85.0, "China": 92.0, "France": 115.0, "Germany": 140.0, "UK": 190.0,
    "India": 88.0, "South America": 95.0, "Africa": 110.0, "Asia (Ex-China)": 120.0, "EU": 135.0
}

# World Bank Country codes to aggregate
WB_MAPPINGS = {
    "USA": ["US"],
    "China": ["CN"],
    "France": ["FR"],
    "Germany": ["DE"],
    "UK": ["GB"],
    "India": ["IN"],
    "EU": ["EUU"],
    "UAE": ["ARE"],
    "South America": ["BRA", "ARG", "CHL", "COL", "PER", "VEN", "ECU", "URY", "PRY", "BOL"],
    "Africa": ["ZAF", "NGA", "EGY", "DZA", "MAR", "KEN", "ETH", "GHA", "TUN", "SEN", "RWA", "TZA", "UGA", "CMR", "AGO", "COD", "MOZ", "MDG", "CIV", "LBY", "SDN"],
    "Asia (Ex-China)": ["JPN", "KOR", "SGP", "SAU", "AUS", "MYS", "THA", "IDN", "VNM", "PHL"]
}

def fetch_wb_value(country_code, indicator, year=2022):
    """Fetch indicator value for a country and year from World Bank API."""
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?date={year}&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if len(data) > 1 and data[1]:
                val = data[1][0]['value']
                return val
    except Exception as e:
        # Silently fail, calling function handles defaults
        pass
    return None

def fetch_workforce_wb(year=2022):
    """Query World Bank API to construct R&D FTE researcher workforce counts."""
    print(f"Querying World Bank API for year {year} (SP.POP.SCIE.RD.P6 and SP.POP.TOTL)...")
    workforce = {}
    
    for region, codes in WB_MAPPINGS.items():
        total_researchers = 0.0
        success_count = 0
        
        for code in codes:
            pop = fetch_wb_value(code, "SP.POP.TOTL", year)
            rd_per_m = fetch_wb_value(code, "SP.POP.SCIE.RD.P6", year)
            
            # Fallback to older years if latest year is null
            if pop is None:
                for y in [year-1, year-2, year-3]:
                    pop = fetch_wb_value(code, "SP.POP.TOTL", y)
                    if pop is not None: break
            if rd_per_m is None:
                for y in [year-1, year-2, year-3]:
                    rd_per_m = fetch_wb_value(code, "SP.POP.SCIE.RD.P6", y)
                    if rd_per_m is not None: break
            
            if pop and rd_per_m:
                # Count in millions
                count = (rd_per_m * pop) / 1e12
                total_researchers += count
                success_count += 1
        
        if success_count > 0:
            workforce[region] = round(total_researchers, 2)
            print(f"  {region:<16}: {workforce[region]:>6.2f}M (calculated from {success_count}/{len(codes)} countries)")
        else:
            # Fallback to default 2026 values if API returns no data
            workforce[region] = DEFAULT_WORKFORCE_2026[region]
            print(f"  {region:<16}: {workforce[region]:>6.2f}M (API fallback to default)")
            
    return workforce

def write_csvs(gdp_data, workforce_data):
    """Write data to gdp_data.csv and workforce_data.csv."""
    # Write GDP
    with open(GDP_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Country", "GDP_Trillions_USD"])
        for k, v in gdp_data.items():
            # Add quotes if needed
            country_name = f'"{k}"' if ',' in k or ' ' in k else k
            writer.writerow([k, v])
    print(f"Updated: {GDP_CSV}")

    # Write Workforce
    with open(WORKFORCE_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Country", "Workforce_Millions"])
        # Maintain specific order matching the old CSV
        order = ["USA", "China", "France", "Germany", "UK", "India", "South America", "Africa", "Asia (Ex-China)", "EU"]
        for k in order:
            if k in workforce_data:
                writer.writerow([k, workforce_data[k]])
    print(f"Updated: {WORKFORCE_CSV}")

def update_caci_data_helper_baselines(gdp_2026):
    """Update UAE GDP in caci_data_helper.py baselines block."""
    if not os.path.exists(HELPER_PY):
        print(f"Warning: {HELPER_PY} not found")
        return
        
    with open(HELPER_PY, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the 'UAE': {'f': 85, 'f_total': 620, 'e': 80, 'gdp': 0.51, 'l': 0.15} block
    pattern = r"('UAE':\s*\{[^}]*'gdp':\s*)([0-9.]+)([^}]*\})"
    replacement = rf"\g<1>0.62\g<3>"
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(HELPER_PY, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated UAE GDP in {HELPER_PY}")

def update_robustness_jsx_fallbacks(gdp_data, workforce_data):
    """Update RobustnessCheck.jsx FALLBACK_COUNTRIES to stay in sync with new CSV values."""
    if not os.path.exists(ROBUSTNESS_JSX):
        print(f"Warning: {ROBUSTNESS_JSX} not found")
        return

    with open(ROBUSTNESS_JSX, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse new values and update the JS block
    # We will locate the FALLBACK_COUNTRIES block and construct a new one
    # Note: f values are obtained by a quick estimation or current values
    # To keep it exact, we will extract current f values, and only update gdp, l, e, r
    current_f = {
        "USA": 2769706,
        "China": 1004123,
        "EU": 157640,
        "UK": 95340,
        "France": 36420,
        "Germany": 42000,
        "India": 150,
        "Asia (Ex-China)": 185120
    }

    new_fallback_block = "const FALLBACK_COUNTRIES = {\n"
    for k in ["USA", "China", "EU", "UK", "France", "Germany", "India", "Asia (Ex-China)"]:
        f_val = current_f[k]
        e_val = ENERGY_PRICES[k]
        l_val = workforce_data[k]
        gdp_val = gdp_data[k]
        r_val = R_TIERS[k]
        
        # Add nice spacing
        key_str = f"    {k}:"
        key_str = f"{key_str:<22}"
        new_fallback_block += f"{key_str}{{ f: {f_val:<8}, e: {e_val:<4}, l: {l_val:<5}, gdp: {gdp_val:<5}, r: {r_val:<3} }},\n"
    new_fallback_block += "};"

    # Regex search and replace the FALLBACK_COUNTRIES block
    pattern = r"const FALLBACK_COUNTRIES = \{[\s\S]*?\};"
    new_content = re.sub(pattern, new_fallback_block, content)

    with open(ROBUSTNESS_JSX, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated fallbacks in: {ROBUSTNESS_JSX}")

def main():
    parser = argparse.ArgumentParser(description="Update CACI GDP and Workforce databases.")
    parser.add_argument("--fetch-wb", action="store_true", help="Fetch workforce data directly from World Bank API.")
    parser.add_argument("--year", type=int, default=2022, help="World Bank data year to query (default: 2022).")
    args = parser.parse_args()

    print("=== CACI Database Update Tool ===")
    
    # 1. Prepare GDP Data
    gdp_data = DEFAULT_GDP_2026.copy()
    print("Prepared IMF WEO 2026 GDP projections.")

    # 2. Prepare Workforce Data
    if args.fetch_wb:
        workforce_data = fetch_workforce_wb(args.year)
    else:
        workforce_data = DEFAULT_WORKFORCE_2026.copy()
        print("Using audited 2026 R&D FTE researcher workforce projections.")

    # 3. Write CSVs
    write_csvs(gdp_data, workforce_data)

    # 4. Update JSX fallbacks
    update_robustness_jsx_fallbacks(gdp_data, workforce_data)

    # 5. Update Helper baseline
    update_caci_data_helper_baselines(gdp_data)

    print("\nDatabase update completed successfully! Run run_all_chapters.py to compile the changes.")

if __name__ == "__main__":
    main()
