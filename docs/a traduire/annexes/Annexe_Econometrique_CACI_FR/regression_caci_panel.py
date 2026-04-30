"""
Script de reproduction des regressions de l'annexe econometrique CACI.

Reproduce the panel regressions M1 (OLS), M2 (FE), M3 (RE) of the
econometric annex and the Hausman test. The panel is calibrated on the
April 2026 snapshot of the public dashboard
(https://mo0ogly.github.io/America-First-IA/dashboard/).

IMPORTANT - panel disclaimer
----------------------------
The companion CSV `panel_caci_2020_2024.csv` is an ILLUSTRATIVE panel
calibrated on the 2024 endpoint values from the public dashboard, with
back-cast trajectories using documented growth dynamics. It serves as
a reproduction skeleton for the methodology, not the source data of
the official Tableau A.2 estimates.

The official Tableau A.2 values (beta = 0.173 / 0.251 / 0.504) are
derived from the full panel maintained privately by the author with
richer covariate sets (regulation gradient by year, finer L proxies)
and are reported in the annex as the reference estimates.

To reproduce Tableau A.2 exactly, replace the calibrated CSV with the
full panel data (available on request from the author). To explore
the methodology with the illustrative panel, run this script as is.

Variables
---------
    country, year, F_phys, L, R, E, GDP, GDP_per_capita, regulation,
    export_control, prod_ai (gain productivite IA sectorielle, % annuel)

Dependencies
------------
    pip install pandas statsmodels linearmodels

Usage
-----
    python regression_caci_panel.py

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
log = logging.getLogger("regression_caci")


# ---------------------------------------------------------------------------
# CACI Power Mode formula
# ---------------------------------------------------------------------------

# Calibrated weights from chap II
ALPHA_F = 0.40   # Compute (dominant)
ALPHA_L = 0.20   # Workforce
ALPHA_R = 0.15   # Regulatory access
ALPHA_E = 0.25   # Energy cost (denominator)


def compute_caci_power(df: pd.DataFrame) -> pd.Series:
    """Compute the CACI Power Mode index for each (country, year).

    CACI(r,t) = F^0.40 * L^0.20 * R^0.15 / E^0.25

    Parameters
    ----------
    df : DataFrame
        Must contain columns F_phys, L, R, E (all positive).

    Returns
    -------
    Series
        Raw CACI values (not normalized).
    """
    return (
        df["F_phys"] ** ALPHA_F
        * df["L"] ** ALPHA_L
        * df["R"] ** ALPHA_R
        / df["E"] ** ALPHA_E
    )


def normalize_caci(caci: pd.Series, country_col: pd.Series,
                   year_col: pd.Series, base_country: str = "USA",
                   base_year: int = 2024) -> pd.Series:
    """Normalize CACI such that the base country at base year = 100."""
    mask = (country_col == base_country) & (year_col == base_year)
    if not mask.any():
        raise ValueError(f"Base ({base_country}, {base_year}) missing")
    base_value = caci[mask].iloc[0]
    return caci / base_value * 100


# ---------------------------------------------------------------------------
# Panel regressions
# ---------------------------------------------------------------------------

def run_pooled_ols(df: pd.DataFrame):
    """Run M1 : pooled OLS with cluster-robust SE."""
    import statsmodels.api as sm

    log.info("=" * 70)
    log.info("M1 : Pooled OLS (heteroscedasticity-robust SE, HC1)")
    log.info("=" * 70)

    y = np.log(df["prod_ai"])
    X = pd.DataFrame({
        "ln_caci": np.log(df["caci_norm"]),
        "ln_gdp_pc": np.log(df["GDP_per_capita"]),
        "regulation": df["regulation"],
        "export_control": df["export_control"],
    })
    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit(cov_type="cluster",
                             cov_kwds={"groups": df["country"]})
    log.info("\n%s", model.summary())
    return model


def run_fixed_effects(df: pd.DataFrame):
    """Run M2 : Fixed Effects (within estimator) with country and time FE.

    Note : `regulation` is constant within country (data limitation of
    the calibrated panel) and is therefore absorbed by entity effects.
    It is dropped from the FE specification but reported in M1 (pooled
    OLS) for comparison. In a richer panel with year-varying regulation
    indices (e.g. AI Act enforcement gradient), it would be retained.
    """
    from linearmodels.panel import PanelOLS

    log.info("=" * 70)
    log.info("M2 : Fixed Effects (PanelOLS, country + time FE, clustered SE)")
    log.info("=" * 70)

    panel = df.set_index(["country", "year"])
    y = np.log(panel["prod_ai"])
    X = pd.DataFrame({
        "ln_caci": np.log(panel["caci_norm"]),
        "export_control": panel["export_control"],
    }, index=panel.index)

    model = PanelOLS(y, X, entity_effects=True, time_effects=True).fit(
        cov_type="clustered", cluster_entity=True
    )
    log.info("\n%s", model)
    return model


def run_random_effects(df: pd.DataFrame):
    """Run M3 : Random Effects (GLS).

    Same note as M2 : `regulation` is dropped due to time-invariance in
    the calibrated panel.
    """
    from linearmodels.panel import RandomEffects

    log.info("=" * 70)
    log.info("M3 : Random Effects (GLS, robust SE)")
    log.info("=" * 70)

    panel = df.set_index(["country", "year"])
    y = np.log(panel["prod_ai"])
    X = pd.DataFrame({
        "ln_caci": np.log(panel["caci_norm"]),
        "export_control": panel["export_control"],
    }, index=panel.index)
    X = X.assign(constant=1.0)

    model = RandomEffects(y, X).fit(cov_type="robust")
    log.info("\n%s", model)
    return model


def hausman_test(fe_model, re_model):
    """Compute the Hausman test comparing FE and RE estimators."""
    log.info("=" * 70)
    log.info("Hausman test : H0 = RE consistent and efficient")
    log.info("=" * 70)

    common_params = [p for p in fe_model.params.index
                     if p in re_model.params.index]
    b_fe = fe_model.params[common_params]
    b_re = re_model.params[common_params]
    var_fe = fe_model.cov.loc[common_params, common_params]
    var_re = re_model.cov.loc[common_params, common_params]

    diff = b_fe - b_re
    var_diff = var_fe - var_re

    try:
        chi2 = float(diff.T @ np.linalg.inv(var_diff) @ diff)
        dof = len(common_params)
        from scipy.stats import chi2 as chi2_dist
        p_value = 1 - chi2_dist.cdf(chi2, df=dof)
        log.info("Chi-square statistic : %.3f (df = %d)", chi2, dof)
        log.info("p-value : %.4f", p_value)
        if p_value < 0.05:
            log.info("=> Reject H0 : Fixed Effects model is preferred")
        else:
            log.info("=> Fail to reject H0 : Random Effects is efficient")
    except np.linalg.LinAlgError:
        log.warning("var_diff is non-invertible (FE and RE too close)")


# ---------------------------------------------------------------------------
# Robustness checks
# ---------------------------------------------------------------------------

def decompose_components(df: pd.DataFrame):
    """Robustness check section A.4.1 : FE on individual components."""
    from linearmodels.panel import PanelOLS

    log.info("=" * 70)
    log.info("Robustness check : FE on decomposed CACI components")
    log.info("=" * 70)

    panel = df.set_index(["country", "year"])
    y = np.log(panel["prod_ai"])
    X = pd.DataFrame({
        "ln_F": np.log(panel["F_phys"]),
        "ln_E_inv": -np.log(panel["E"]),
        "ln_L": np.log(panel["L"]),
        "ln_R": np.log(panel["R"]),
        "regulation": panel["regulation"],
        "export_control": panel["export_control"],
    }, index=panel.index)

    model = PanelOLS(y, X, entity_effects=True, time_effects=True).fit(
        cov_type="clustered", cluster_entity=True
    )
    log.info("\n%s", model)
    log.info("Note : the coefficient on ln_F (compute) should dominate, "
             "validating the 0.40 weight in the Power Mode formula.")
    return model


def alternative_weights(df: pd.DataFrame):
    """Robustness check section A.4.2 : alternative weight specifications."""
    from linearmodels.panel import PanelOLS

    log.info("=" * 70)
    log.info("Robustness check : alternative CACI weight specifications")
    log.info("=" * 70)

    weight_specs = {
        "Power Mode (retained)": (0.40, 0.20, 0.15, 0.25),
        "Equal weights": (0.25, 0.25, 0.25, 0.25),
        "Energy-First": (0.25, 0.20, 0.15, 0.40),
        "Talent-First": (0.30, 0.35, 0.15, 0.20),
    }

    for name, (a_f, a_l, a_r, a_e) in weight_specs.items():
        caci_alt = (
            df["F_phys"] ** a_f
            * df["L"] ** a_l
            * df["R"] ** a_r
            / df["E"] ** a_e
        )
        df_alt = df.copy()
        df_alt["caci_alt_norm"] = normalize_caci(
            caci_alt, df_alt["country"], df_alt["year"],
        )

        panel = df_alt.set_index(["country", "year"])
        y = np.log(panel["prod_ai"])
        X = pd.DataFrame({
            "ln_caci_alt": np.log(panel["caci_alt_norm"]),
            "regulation": panel["regulation"],
            "export_control": panel["export_control"],
        }, index=panel.index)

        model = PanelOLS(y, X, entity_effects=True, time_effects=True).fit(
            cov_type="clustered", cluster_entity=True
        )
        beta = model.params["ln_caci_alt"]
        se = model.std_errors["ln_caci_alt"]
        r2 = model.rsquared_within
        log.info("%-25s : beta(CACI) = %.3f (SE %.3f), R2 within = %.3f",
                 name, beta, se, r2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(panel_path: Path) -> None:
    """Reproduce the full annex econometric analysis."""
    log.info("Loading panel from %s", panel_path)
    df = pd.read_csv(panel_path)
    log.info("Panel shape : %d obs, %d countries, %d years",
             len(df), df["country"].nunique(), df["year"].nunique())

    # Compute CACI Power Mode and normalize
    df["caci_raw"] = compute_caci_power(df)
    df["caci_norm"] = normalize_caci(df["caci_raw"], df["country"], df["year"])

    # Main regressions
    m1 = run_pooled_ols(df)
    m2 = run_fixed_effects(df)
    m3 = run_random_effects(df)

    # Hausman test
    hausman_test(m2, m3)

    # Robustness checks
    decompose_components(df)
    alternative_weights(df)

    log.info("=" * 70)
    log.info("Analysis complete. Compare with Tableau A.2 of the annex.")
    log.info("=" * 70)


if __name__ == "__main__":
    panel_csv = Path(__file__).parent / "panel_caci_2020_2024.csv"
    if not panel_csv.exists():
        log.error("Panel CSV not found at %s", panel_csv)
        log.error("Run build_panel_caci.py first to generate the panel.")
    else:
        main(panel_csv)
