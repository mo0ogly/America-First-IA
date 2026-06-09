#!/usr/bin/env python3
"""
Extract STEM workforce (researchers in R&D) from the World Bank Open Data API.

Replaces the round-number proxy estimates in workforce_data.csv with sourced,
traceable figures. Factor L of the CACI index.

Method:
  - Pull most-recent-non-empty value per country (mrnev=1) for:
      SP.POP.SCIE.RD.P6 : Researchers in R&D (per million people)
      SP.POP.TOTL       : Total population
  - Absolute researchers per country = per_million * population / 1e6
  - Single countries: direct. Regions: sum of member countries (explicit ISO3
    lists below), which is more rigorous and transparent than World Bank
    macro-region aggregates (whose R&D series are largely null, e.g. SSF/AFW).

Regions are documented as sums of reporting member countries. Countries with no
reported R&D value contribute 0 (undercount, disclosed in the audit output).

Output column order matches the existing CSV so the dashboard keeps working.
"""

import csv
import sys
import urllib.request
import json

WB = "https://api.worldbank.org/v2"
RD = "SP.POP.SCIE.RD.P6"   # researchers per million
POP = "SP.POP.TOTL"        # total population

ROW_ORDER = ["USA", "China", "EU", "UK", "Asia (Ex-China)",
             "India", "France", "Germany", "South America", "Africa"]

# Single-country keys -> ISO3
SINGLE = {
    "USA": "USA", "China": "CHN", "UK": "GBR",
    "India": "IND", "France": "FRA", "Germany": "DEU",
}

EU27 = ["AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA",
        "DEU", "GRC", "HUN", "IRL", "ITA", "LVA", "LTU", "LUX", "MLT", "NLD",
        "POL", "PRT", "ROU", "SVK", "SVN", "ESP", "SWE"]

SOUTH_AMERICA = ["ARG", "BOL", "BRA", "CHL", "COL", "ECU", "GUY", "PRY",
                 "PER", "SUR", "URY", "VEN"]

AFRICA = ["DZA", "AGO", "BEN", "BWA", "BFA", "BDI", "CPV", "CMR", "CAF", "TCD",
          "COM", "COG", "COD", "CIV", "DJI", "EGY", "GNQ", "ERI", "SWZ", "ETH",
          "GAB", "GMB", "GHA", "GIN", "GNB", "KEN", "LSO", "LBR", "LBY", "MDG",
          "MWI", "MLI", "MRT", "MUS", "MAR", "MOZ", "NAM", "NER", "NGA", "RWA",
          "STP", "SEN", "SYC", "SLE", "SOM", "ZAF", "SSD", "SDN", "TZA", "TGO",
          "TUN", "UGA", "ZMB", "ZWE"]

# Asia excluding China (includes India, per the model where India is also broken
# out separately). East + South-East + South + Central Asia. Middle East excluded.
ASIA_EX_CHINA = ["IND", "JPN", "KOR", "PRK", "MNG", "TWN", "HKG",
                 "IDN", "MYS", "PHL", "SGP", "THA", "VNM", "KHM", "LAO", "MMR", "BRN", "TLS",
                 "PAK", "BGD", "LKA", "NPL", "BTN", "MDV", "AFG",
                 "KAZ", "UZB", "TKM", "KGZ", "TJK"]


def fetch_all(indicator):
    """Most-recent-non-empty value per country -> {iso3: (year, value)}."""
    out = {}
    url = f"{WB}/country/all/indicator/{indicator}?format=json&mrnev=1&per_page=400"
    with urllib.request.urlopen(url, timeout=60) as r:
        payload = json.load(r)
    if not isinstance(payload, list) or len(payload) < 2 or payload[1] is None:
        return out
    for row in payload[1]:
        if row.get("value") is None:
            continue
        iso3 = row["countryiso3code"]
        if iso3:
            out[iso3] = (row["date"], float(row["value"]))
    return out


def absolute_millions(iso3, rd, pop):
    """Researchers (millions) for one country, or None if data missing."""
    if iso3 not in rd or iso3 not in pop:
        return None
    per_million = rd[iso3][1]
    population = pop[iso3][1]
    return per_million * population / 1e12  # (per_million * pop/1e6) /1e6 -> millions


def region_sum(members, rd, pop):
    """Sum researchers (millions) over reporting members; report coverage."""
    total = 0.0
    reporting = []
    for iso3 in members:
        m = absolute_millions(iso3, rd, pop)
        if m is not None:
            total += m
            reporting.append(iso3)
    return round(total, 3), reporting


def main():
    rd = fetch_all(RD)
    pop = fetch_all(POP)
    print(f"WB returned R&D for {len(rd)} entities, population for {len(pop)}",
          file=sys.stderr)

    results, audit = {}, {}

    for key, iso3 in SINGLE.items():
        m = absolute_millions(iso3, rd, pop)
        if m is None:
            print(f"WARN: no data for {key} ({iso3})", file=sys.stderr)
            continue
        results[key] = round(m, 3)
        audit[key] = f"{iso3} (yr {rd[iso3][0]})"

    for key, members in [("EU", EU27), ("South America", SOUTH_AMERICA),
                         ("Africa", AFRICA), ("Asia (Ex-China)", ASIA_EX_CHINA)]:
        total, reporting = region_sum(members, rd, pop)
        results[key] = total
        audit[key] = f"sum of {len(reporting)}/{len(members)} reporting countries"

    print("=== Workforce extraction (millions of researchers in R&D) ===")
    for key in ROW_ORDER:
        if key in results:
            print(f"  {key:18s} {results[key]:>7.3f}   [{audit.get(key,'')}]")
        else:
            print(f"  {key:18s}   MISSING")

    targets = [
        "caci-dashboard/public/data/workforce_data.csv",
        "docs/dashboard/data/workforce_data.csv",
    ]
    for path in targets:
        with open(path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Country", "Workforce_Millions"])
            for key in ROW_ORDER:
                if key in results:
                    w.writerow([key, results[key]])
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
