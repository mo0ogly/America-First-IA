"""
Panel CACI builder for the econometric annex.

Constructs the calibrated panel `panel_caci_2020_2024.csv` used by
`regression_caci_panel.py` to reproduce the regressions of the annex.

The 2024 endpoint values are calibrated on the April 2026 snapshot of
the public dashboard (https://mo0ogly.github.io/America-First-IA/dashboard/)
and trajectory back to 2020 follows the documented growth dynamics
(Epoch AI, IEA, Hawkins et al. 2025).

Variables generated
-------------------
    F_phys           Operational compute installed (M H100-eq)
    L                Workforce IA (M people)
    R                Regulatory access index (1.0 Tier 1, 0.6 Tier 2,
                                              0.2 Tier 3)
    E                Energy cost PPA-adjusted (USD/MWh)
    GDP              GDP (trillions USD)
    GDP_per_capita   GDP per capita (kUSD)
    regulation       Regulatory burden index 0-1 (higher = heavier)
    export_control   1.0 if Tier 3 since 2022, 0.5 if Tier 2 since 2024,
                     0 otherwise
    prod_ai          AI sectoral productivity gain (% per year)

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
from pathlib import Path

import numpy as np
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("build_panel")


# 2024 endpoint values (snapshot avril 2026, dashboard rebased to 2024)
# Format: country, F_phys (M H100-eq), L (M workforce), R (Tier index),
#         E (USD/MWh PPA), GDP (T USD), GDP_pc (kUSD), regulation,
#         export_control 2024, prod_ai (% gain annuel sectoriel)
ENDPOINTS_2024 = [
    ("USA",       1381.78, 3.6,  1.0,  85, 31.9, 84.0, 0.30, 0.0, 4.2),
    ("Chine",      233.93, 4.8,  0.1,  92, 23.7, 12.5, 0.50, 1.0, 2.0),
    ("Allemagne",   25.78, 0.85, 1.0, 140,  4.7, 53.6, 0.55, 0.0, 1.6),
    ("France",      18.21, 0.65, 1.0, 115,  3.4, 44.4, 0.55, 0.0, 2.0),
    ("UK",           7.89, 0.50, 1.0, 190,  3.9, 50.0, 0.45, 0.0, 1.8),
    ("Japon",       18.74, 0.70, 1.0, 165,  4.5, 33.6, 0.40, 0.0, 2.4),
    ("Coree",        6.54, 0.50, 1.0, 110,  1.8, 33.0, 0.40, 0.0, 2.7),
    ("Inde",         5.38, 0.40, 0.5,  88,  5.6,  2.5, 0.50, 0.5, 1.9),
    ("Canada",       3.08, 0.15, 1.0,  98,  2.3, 53.8, 0.40, 0.0, 2.1),
    ("Pays-Bas",     0.94, 0.15, 1.0, 145,  1.1, 62.7, 0.50, 0.0, 2.0),
    ("Suede",        4.88, 0.10, 1.0,  68,  0.6, 57.7, 0.45, 0.0, 2.6),
    ("Bresil",       1.24, 0.30, 0.5,  78,  2.7,  9.7, 0.45, 0.5, 1.4),
]


# Growth rates for back-casting 2024 to 2020 (CAGR)
# Compute (F): rapid US acceleration, China plateau post-Oct 2022
F_CAGR = {
    "USA": 0.95,        # x14.5 over 4 years
    "Chine": 0.10,      # ~10%/yr until 2022 then near 0
    "Allemagne": 0.45, "France": 0.50, "UK": 0.45, "Japon": 0.40,
    "Coree": 0.40, "Inde": 0.55, "Canada": 0.40, "Pays-Bas": 0.40,
    "Suede": 0.35, "Bresil": 0.30,
}

# Productivity: gradual ramp following AI adoption
PROD_CAGR_INVERSE = 0.30   # multiplicative factor to discount each year backward

# Workforce L grows slowly (~5%/yr)
L_CAGR = 0.05

# Energy E increased sharply post-2022 in EU (gas crisis)
E_2022_SHOCK_EU = 1.4   # 40% spike in EU/UK 2022


def back_cast_value(value_2024: float, cagr: float, year: int) -> float:
    """Compute the value at `year` from the 2024 endpoint and a CAGR."""
    return value_2024 / (1 + cagr) ** (2024 - year)


def build_panel() -> pd.DataFrame:
    """Build the 12-country, 5-year panel as a DataFrame."""
    rows = []
    rng = np.random.default_rng(42)
    EU_LIKE = {"Allemagne", "France", "UK", "Pays-Bas", "Suede"}

    for country, F24, L24, R, E24, GDP24, GDP_pc24, reg, ec24, prod24 in ENDPOINTS_2024:
        F_cagr = F_CAGR[country]

        for year in range(2020, 2025):
            # F : back-cast with growth rate. China plateaus after 2022.
            if country == "Chine" and year >= 2022:
                F = back_cast_value(F24, F_cagr, 2022)
            else:
                F = back_cast_value(F24, F_cagr, year)

            # L : back-cast with stable CAGR
            L = back_cast_value(L24, L_CAGR, year)

            # R : Tier classification only changed in 2022 (BIS) and 2024 (Diffusion)
            if country == "Chine" and year < 2022:
                R_year = 0.6     # Was Tier 2-equivalent before BIS Oct 2022
            elif country in {"Inde", "Bresil"} and year < 2024:
                R_year = 0.8     # Was less restricted before AI Diffusion Rule
            else:
                R_year = R

            # E : EU shock 2022, gradual normalization 2023-2024
            if country in EU_LIKE:
                if year == 2022:
                    E = E24 * E_2022_SHOCK_EU
                elif year == 2023:
                    E = E24 * 1.20
                else:
                    E = E24 * (1 - 0.03 * (2024 - year))   # mild upward drift
            else:
                E = E24 * (1 - 0.04 * (2024 - year))

            # GDP : flat 2% CAGR
            GDP = back_cast_value(GDP24, 0.02, year)
            GDP_pc = back_cast_value(GDP_pc24, 0.02, year)

            # Export control : Tier 3 since 2022 for China, Tier 2 since 2024 for India/Brazil
            if country == "Chine":
                ec = 1.0 if year >= 2022 else 0.0
            elif country in {"Inde", "Bresil"}:
                ec = 0.5 if year >= 2024 else 0.0
            else:
                ec = 0.0

            # prod_ai : back-cast with discount factor + small noise
            prod = prod24 * np.exp(-PROD_CAGR_INVERSE * (2024 - year))
            prod *= 1 + rng.normal(0, 0.03)

            rows.append({
                "country": country,
                "year": year,
                "F_phys": F,
                "L": L,
                "R": R_year,
                "E": E,
                "GDP": GDP,
                "GDP_per_capita": GDP_pc,
                "regulation": reg,
                "export_control": ec,
                "prod_ai": prod,
            })

    df = pd.DataFrame(rows)
    return df


def main(out_path: Path) -> None:
    """Build and save the panel CSV."""
    df = build_panel()
    log.info("Panel built : %d obs", len(df))
    log.info("Countries : %s", sorted(df["country"].unique()))
    log.info("Years : %s", sorted(df["year"].unique()))
    df.to_csv(out_path, index=False, float_format="%.4f")
    log.info("Saved to %s", out_path)

    # Summary statistics
    log.info("\nSummary statistics:")
    log.info("\n%s", df.describe(include=[np.number]).round(2).to_string())


if __name__ == "__main__":
    out = Path(__file__).parent / "panel_caci_2020_2024.csv"
    main(out)
