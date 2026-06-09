#!/usr/bin/env python3
"""
Build energy_prices.csv (Factor E: industrial electricity price, USD/MWh).

Hybrid sourcing, honest provenance:
  - EU bloc (France, Germany, EU aggregate): LIVE from Eurostat nrg_pc_205
      band MWH20000-69999 (large industrial consumer), tax X_VAT
      (excludes recoverable VAT, includes network charges and non-recoverable
      levies = the relevant end-use industrial price), latest semester.
      EUR/kWh converted to USD/MWh via ECB EUR/USD reference rate.
  - Everyone else (USA, UK, China, India, regions): PROXY values. No free,
    authoritative API exists for industrial electricity prices in these
    markets (IEA full DB is paywalled; EIA needs a key). Kept as documented
    estimates and clearly flagged [proxy] in the audit output.

Source refs for the proxy values (most recent published, for the record):
  USA            ~85  -- EIA Electric Power Monthly, industrial avg
  UK             190  -- GOV.UK industrial electricity price series
  China           92  -- IEA / national grid published industrial tariffs
  India           88  -- CEA / GlobalPetrolPrices industrial
  South America   95  -- Brazil (ANEEL) representative industrial
  Africa         110  -- regional aggregate, public reports
  Asia (Ex-China) 120 -- Japan/Korea-weighted, IEA published
"""

import csv
import os
import sys
import subprocess
import urllib.request
import urllib.error
import json
import xml.etree.ElementTree as ET

# EIA bulk Electricity file (https://api.eia.gov/bulk/ELEC.zip, ~1.4GB, not in
# repo). Contains series ELEC.PRICE.US-IND.A = US industrial retail price.
# Set EIA_BULK_FILE to override the default download location.
EIA_BULK_FILE = os.environ.get(
    "EIA_BULK_FILE", os.path.expanduser("~/Downloads/ELEC.txt"))

EUROSTAT = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
            "nrg_pc_205?format=JSON&unit=KWH&siec=E7000&tax=X_VAT&currency=EUR"
            "&nrg_cons=MWH20000-69999&geo={geo}")

# Output row order (must match existing energy_prices.csv)
ROW_ORDER = ["USA", "China", "France", "Germany", "UK", "India",
             "South America", "Africa", "Asia (Ex-China)", "EU"]

# CACI key -> Eurostat geo code (live-sourced subset)
EUROSTAT_GEO = {"France": "FR", "Germany": "DE", "EU": "EU27_2020"}

# Proxy values for markets with no free authoritative API (USD/MWh).
# USA is upgraded from the EIA bulk file when available (see eia_us_industrial).
PROXY = {
    "USA": 85, "UK": 190, "China": 92, "India": 88,
    "South America": 95, "Africa": 110, "Asia (Ex-China)": 120,
}


def eia_us_industrial():
    """US industrial retail price (USD/MWh, year) from the EIA bulk file.

    Reads series ELEC.PRICE.US-IND.A (cents/kWh) and converts to USD/MWh.
    Returns (None, None) if the bulk file is absent or the series is missing.
    """
    if not os.path.exists(EIA_BULK_FILE):
        return None, None
    try:
        line = subprocess.check_output(
            ["grep", "-m1", '"ELEC.PRICE.US-IND.A"', EIA_BULK_FILE],
            text=True, timeout=120)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None, None
    d = json.loads(line)
    for year, cents in d["data"]:
        if cents is not None:
            return round(cents * 10, 1), year  # cents/kWh -> USD/MWh
    return None, None


def eur_usd_rate():
    """ECB EUR/USD reference rate; ECB XML primary, frankfurter fallback."""
    try:
        url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
        with urllib.request.urlopen(url, timeout=20) as r:
            root = ET.fromstring(r.read())
        for cube in root.iter():
            if cube.get("currency") == "USD":
                return float(cube.get("rate")), "ECB"
    except Exception as e:
        print(f"ECB FX failed ({e}), trying frankfurter", file=sys.stderr)
    url = "https://api.frankfurter.dev/v1/latest?base=EUR&symbols=USD"
    with urllib.request.urlopen(url, timeout=20) as r:
        return float(json.load(r)["rates"]["USD"]), "Frankfurter"


def eurostat_latest(geo):
    """Latest (semester, EUR/kWh) for a geo, or (None, None)."""
    with urllib.request.urlopen(EUROSTAT.format(geo=geo), timeout=30) as r:
        d = json.load(r)
    if "error" in d or not d.get("value"):
        return None, None
    idx = d["dimension"]["time"]["category"]["index"]
    inv = {v: k for k, v in idx.items()}
    pairs = sorted((inv[int(i)], val) for i, val in d["value"].items())
    return pairs[-1] if pairs else (None, None)


def main():
    rate, fx_src = eur_usd_rate()
    print(f"EUR/USD = {rate} ({fx_src})", file=sys.stderr)

    results, audit = {}, {}

    for key, geo in EUROSTAT_GEO.items():
        sem, eur_kwh = eurostat_latest(geo)
        if eur_kwh is None:
            print(f"WARN: Eurostat no data for {key} ({geo}), using proxy",
                  file=sys.stderr)
            continue
        usd_mwh = round(eur_kwh * 1000 * rate, 1)
        results[key] = usd_mwh
        audit[key] = f"Eurostat {geo} {sem}, {eur_kwh} EUR/kWh"

    for key, val in PROXY.items():
        results[key] = val
        audit[key] = "proxy (no free API)"

    # Upgrade USA from the EIA bulk file if present
    usa_usd, usa_yr = eia_us_industrial()
    if usa_usd is not None:
        results["USA"] = usa_usd
        audit["USA"] = f"EIA bulk ELEC.PRICE.US-IND.A {usa_yr}"
    else:
        print("INFO: EIA bulk file not found, USA stays proxy", file=sys.stderr)

    print("=== Energy extraction (industrial electricity, USD/MWh) ===")
    for key in ROW_ORDER:
        print(f"  {key:18s} {results[key]:>7.1f}   [{audit.get(key,'')}]")

    targets = [
        "caci-dashboard/public/data/energy_prices.csv",
        "docs/dashboard/data/energy_prices.csv",
    ]
    for path in targets:
        with open(path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Country", "Industrial_Electricity_USD_per_MWh"])
            for key in ROW_ORDER:
                w.writerow([key, results[key]])
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
