#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST - Chapter I: Introduction & Theoretical Framework
 Trilingual figure generator (FR / EN / PT-BR)
=============================================================================
 Author        : Fabrice Pizzi (Universite Paris-Sorbonne)
 Build         : python generate_chapitre1_graphs.py
 Output        : PNG files in $CH1_FIG_DIR (default ./figures/ch1)

 Revisions vs. previous version (April 2026 dashboard alignment):
   * Fig 1.3: replaces hard-coded "compute gap x15" with the actual
     CACI Power Mode US/EU ratio (3.46:1) computed from the live
     Sorbonne 2026 dataset, plus the secondary compute density ratio
     (H100-eq per T$ GDP).
   * Fig 1.6: theoretical framework chain updated to cite the CACI
     ratio instead of the obsolete x15 placeholder.
   * Fig 1.7 (NEW): CACI Power Mode decomposition - visualises the
     four exponents (F^0.40, L^0.20, R^0.15, E^0.25, weights 40/20/15/25)
     and how each region scores per dimension.
   * Fig 1.8 (NEW): Physical CACI vs Sovereign CACI - quantifies the
     dependence of each region on foreign hyperscalers (gap = strategic
     vulnerability).
=============================================================================
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("ch1_graphs")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OUTPUT_DIR = Path(os.environ.get(
    "CH1_FIG_DIR",
    Path(__file__).resolve().parent / "figures" / "ch1",
))
DPI = 300
FIGSIZE_WIDE = (12, 6.5)

# Professional palette
US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
FR_COLOR = "#2E86C1"
CN_COLOR = "#C0392B"
ACCENT1 = "#148F77"
ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"
BG_COLOR = "#FAFBFC"
GRID_COLOR = "#E0E0E0"


# ---------------------------------------------------------------------------
# Live dashboard reference values (Sorbonne 2026 dataset, April 2026 snapshot)
# ---------------------------------------------------------------------------

CACI_POWER_RATIO_US_EU = 3.46         # Fig 1.3 main number
COMPUTE_DENSITY_US_EU = 8.2           # H100-eq per T$ GDP, US / EU
US_SHARE_OPERATIONAL_COMPUTE = 76.9   # percent of operational H100-eq worldwide

# CACI Power Mode scores (normalised, leader = 100)
# Computed locally via F^0.40 x L^0.20 x R^0.15 / E^0.25 on the live CSVs
CACI_POWER_SCORES = {
    "USA":     100.0,
    "China":    15.7,
    "EU":       28.9,
    "France":   25.3,
    "Germany":   5.4,
    "UK":        7.0,
    "India":    22.2,
}

# Physical vs Sovereign CACI (April 2026 dashboard snapshot, computed by
# filtering Epoch AI clusters by Owner column).
# F_dom = clusters owned by domestic operators only; F_phys = all clusters
# physically located in the territory regardless of ownership.
# The phys-sov gap therefore measures dependence on foreign-owned compute
# physically hosted on the territory. The UAE case is the textbook example:
# 99.6 percent of UAE F_total is owned by US-side actors (Stargate UAE,
# Microsoft, OpenAI), collapsing the Sovereign CACI from 56 to 6.
# For the EU and France, the gap on F_installed is small because most
# EU-located clusters are owned by EU operators (OVH, Scaleway, Sesterce,
# Fluidstack, EuroHPC consortium, AI Factories). The real EU dependence
# manifests on compute *workloads* (cloud usage running on AWS/Azure/GCP),
# which is a separate dimension treated in Chapter III and beyond.
CACI_PHYS_VS_SOV = {
    "USA":     {"phys": 100.0, "sov": 100.0},
    "China":   {"phys":  15.7, "sov":  15.7},
    "EU":      {"phys":  28.9, "sov":  28.8},   # F installed is mostly EU-owned
    "France":  {"phys":  25.3, "sov":  25.3},   # Fluidstack + Sesterce domestic
    "UAE":     {"phys":  55.7, "sov":   6.0},   # 99.6 pct US-owned compute
}


# ---------------------------------------------------------------------------
# Translations
# ---------------------------------------------------------------------------

LANGS: dict[str, dict[str, Any]] = {
    "fr": {
        "suffix": "FR",

        "fig1_title": "Consommation electrique mondiale des data centers\n(Projection IEA 2022-2030)",
        "fig1_ylabel": "TWh / an",
        "fig1_label_total": "Total data centers",
        "fig1_label_ai": "Dont IA (estimation)",
        "fig1_source": "Source : IEA Energy and AI (2025), IEA-4E (2025)",
        "fig1_annot_2024": "415 TWh\n(2024)",
        "fig1_annot_2030": "945 TWh\n(2030, scen. base)",

        "fig2_title": "Marche mondial des semi-conducteurs\n(Projection 2020-2030)",
        "fig2_ylabel": "Milliards USD",
        "fig2_label_total": "Total semi-conducteurs",
        "fig2_label_ai": "Dont puces IA (estimation)",
        "fig2_source": "Sources : SIA/WSTS, McKinsey (2026), Deloitte (2026), AMD",
        "fig2_cagr": "CAGR ~13%",

        "fig3_title": "CACI Power Mode US vs UE et densite compute\n(snapshot dataset Sorbonne avril 2026)",
        "fig3_ylabel_left": "Indice CACI Power Mode (UE = 1)",
        "fig3_ylabel_right": "H100-eq par T$ de PIB (UE = 1)",
        "fig3_labels": ["Etats-Unis", "Union Europeenne"],
        "fig3_source": "Source : tableau de bord public America-First-IA, formule F^0.40 x L^0.20 x R^0.15 / E^0.25",
        "fig3_annot_caci": "x3,46\nCACI Power",
        "fig3_annot_dens": "x8,2\nH100-eq / T$",

        "fig4_title": "Taux d'adoption de l'IA par les entreprises\n(Etats-Unis vs Union Europeenne, 2025)",
        "fig4_ylabel": "% d'entreprises utilisant l'IA",
        "fig4_cats": ["Petites entreprises", "Grandes entreprises"],
        "fig4_legend": ["Etats-Unis", "Union Europeenne"],
        "fig4_source": "Sources : Parlement europeen (2025), US Chamber of Commerce (2025)",
        "fig4_gap_label": "Ecart",

        "fig5_title": "Domination americaine sur les points d'etranglement\nde la chaine de valeur IA (2025)",
        "fig5_cats": ["GPU data centers\n(Nvidia)", "Infrastructure\ncloud", "Capital-risque\nIA generative"],
        "fig5_ylabel": "Part de marche controlee par des acteurs US (%)",
        "fig5_source": "Sources : OCDE (2025), Fed Board (2025), Bruegel (2024)",
        "fig5_threshold": "Seuil 50%",

        "fig6_title": "Cadre theorique integre : du protectionnisme technologique\na la divergence de competitivite",
        "fig6_boxes": [
            "PROTECTIONNISME\nTECHNOLOGIQUE US\n(Export controls,\ntarifs, quotas)",
            "RESTRICTION\nDU COMPUTE\nEUROPEEN\n(CACI Power\nUS/UE = 3,46:1)",
            "DIVERGENCE DE\nPRODUCTIVITE\n(J-curve retardee,\ncouts accrus)",
            "DEPENDANCE\nSTRATEGIQUE\n(Vendor lock-in\ngeopolitique)",
        ],
        "fig6_amplifiers": ["Energie\n(couts x1,6 vs US)", "Robotique IA\n(demande x2 compute)"],
        "fig6_theories": [
            "Weaponized\nInterdependence\n(Farrell & Newman)",
            "GPT & J-Curve\n(Brynjolfsson et al.)",
            "Concentration\n& Rentes\n(Martens, OCDE)",
            "Souverainete\nnumerique\n(Mugge, Hawkins)",
        ],
        "fig6_source": "Elaboration auteur - Cadre theorique, section 1.3",
        "fig6_amp_label": "AMPLIFICATEURS",

        "fig7_title": "Decomposition du CACI Power Mode\nF^0,40 x L^0,20 x R^0,15 / E^0,25 (poids 40/20/15/25)",
        "fig7_axes": ["Compute (F)", "Travail (L)", "Acces (R)", "Energie (E)"],
        "fig7_legend": ["Etats-Unis", "Union Europeenne", "France"],
        "fig7_source": "Source : tableau de bord public America-First-IA. Valeurs normalisees (US = 100 sur chaque axe).",
        "fig7_caption": "Poids exposants : F=0,40 - L=0,20 - R=0,15 - E=0,25. La somme = 1.",
        "fig7_pie_title": "Poids des exposants",
        "fig7_index_label": "Indice (US = 100)",

        "fig8_title": "CACI physique vs CACI souverain\n(F installe vs F detenu domestiquement)",
        "fig8_ylabel": "Score CACI Power Mode (US = 100)",
        "fig8_legend_phys": "CACI physique (F_total)",
        "fig8_legend_sov": "CACI souverain (F domestique)",
        "fig8_source": "Source : tableau de bord public America-First-IA, classification par Owner. Le cas EAU illustre l'offshoring US (gap 56 -> 6).",
        "fig8_gap_label": "Gap",
    },

    "en": {
        "suffix": "EN",

        "fig1_title": "Global Data Center Electricity Consumption\n(IEA Projection 2022-2030)",
        "fig1_ylabel": "TWh / year",
        "fig1_label_total": "Total data centers",
        "fig1_label_ai": "Of which AI (estimate)",
        "fig1_source": "Source: IEA Energy and AI (2025), IEA-4E (2025)",
        "fig1_annot_2024": "415 TWh\n(2024)",
        "fig1_annot_2030": "945 TWh\n(2030, base sc.)",

        "fig2_title": "Global Semiconductor Market\n(Projection 2020-2030)",
        "fig2_ylabel": "Billion USD",
        "fig2_label_total": "Total semiconductors",
        "fig2_label_ai": "Of which AI chips (estimate)",
        "fig2_source": "Sources: SIA/WSTS, McKinsey (2026), Deloitte (2026), AMD",
        "fig2_cagr": "CAGR ~13%",

        "fig3_title": "CACI Power Mode US vs EU and compute density\n(Sorbonne dataset snapshot, April 2026)",
        "fig3_ylabel_left": "CACI Power Mode index (EU = 1)",
        "fig3_ylabel_right": "H100-eq per T$ GDP (EU = 1)",
        "fig3_labels": ["United States", "European Union"],
        "fig3_source": "Source: America-First-IA public dashboard, formula F^0.40 x L^0.20 x R^0.15 / E^0.25",
        "fig3_annot_caci": "x3.46\nCACI Power",
        "fig3_annot_dens": "x8.2\nH100-eq / T$",

        "fig4_title": "AI Adoption Rate by Enterprises\n(United States vs European Union, 2025)",
        "fig4_ylabel": "% of enterprises using AI",
        "fig4_cats": ["Small enterprises", "Large enterprises"],
        "fig4_legend": ["United States", "European Union"],
        "fig4_source": "Sources: European Parliament (2025), US Chamber of Commerce (2025)",
        "fig4_gap_label": "Gap",

        "fig5_title": "US Dominance Over AI Value Chain Chokepoints\n(2025)",
        "fig5_cats": ["Data center GPUs\n(Nvidia)", "Cloud\ninfrastructure", "Generative AI\nventure capital"],
        "fig5_ylabel": "Market share controlled by US players (%)",
        "fig5_source": "Sources: OECD (2025), Fed Board (2025), Bruegel (2024)",
        "fig5_threshold": "50% threshold",

        "fig6_title": "Integrated Theoretical Framework: From Technological Protectionism\nto Competitiveness Divergence",
        "fig6_boxes": [
            "US TECHNOLOGICAL\nPROTECTIONISM\n(Export controls,\ntariffs, quotas)",
            "RESTRICTION OF\nEUROPEAN\nCOMPUTE\n(CACI Power\nUS/EU = 3.46:1)",
            "PRODUCTIVITY\nDIVERGENCE\n(Delayed J-curve,\nhigher costs)",
            "STRATEGIC\nDEPENDENCE\n(Geopolitical\nvendor lock-in)",
        ],
        "fig6_amplifiers": ["Energy\n(costs x1.6 vs US)", "AI Robotics\n(x2 compute demand)"],
        "fig6_theories": [
            "Weaponized\nInterdependence\n(Farrell & Newman)",
            "GPT & J-Curve\n(Brynjolfsson et al.)",
            "Concentration\n& Rents\n(Martens, OECD)",
            "Digital\nSovereignty\n(Mugge, Hawkins)",
        ],
        "fig6_source": "Author's elaboration - Theoretical framework, section 1.3",
        "fig6_amp_label": "AMPLIFIERS",

        "fig7_title": "CACI Power Mode decomposition\nF^0.40 x L^0.20 x R^0.15 / E^0.25 (weights 40/20/15/25)",
        "fig7_axes": ["Compute (F)", "Labor (L)", "Access (R)", "Energy (E)"],
        "fig7_legend": ["United States", "European Union", "France"],
        "fig7_source": "Source: America-First-IA public dashboard. Values normalised (US = 100 on each axis).",
        "fig7_caption": "Exponent weights: F=0.40 - L=0.20 - R=0.15 - E=0.25. Sum = 1.",
        "fig7_pie_title": "Exponent weights",
        "fig7_index_label": "Index (US = 100)",

        "fig8_title": "Physical CACI vs Sovereign CACI\n(F installed vs F domestically owned)",
        "fig8_ylabel": "CACI Power Mode score (US = 100)",
        "fig8_legend_phys": "Physical CACI (F_total)",
        "fig8_legend_sov": "Sovereign CACI (F domestic)",
        "fig8_source": "Source: America-First-IA public dashboard, classification by Owner. UAE case illustrates US offshoring (gap 56 -> 6).",
        "fig8_gap_label": "Gap",
    },

    "pt": {
        "suffix": "PT-BR",

        "fig1_title": "Consumo Global de Eletricidade em Data Centers\n(Projecao IEA 2022-2030)",
        "fig1_ylabel": "TWh / ano",
        "fig1_label_total": "Total data centers",
        "fig1_label_ai": "Dos quais IA (estimativa)",
        "fig1_source": "Fonte: IEA Energy and AI (2025), IEA-4E (2025)",
        "fig1_annot_2024": "415 TWh\n(2024)",
        "fig1_annot_2030": "945 TWh\n(2030, cen. base)",

        "fig2_title": "Mercado Global de Semicondutores\n(Projecao 2020-2030)",
        "fig2_ylabel": "Bilhoes USD",
        "fig2_label_total": "Total semicondutores",
        "fig2_label_ai": "Dos quais chips IA (estimativa)",
        "fig2_source": "Fontes: SIA/WSTS, McKinsey (2026), Deloitte (2026), AMD",
        "fig2_cagr": "CAGR ~13%",

        "fig3_title": "CACI Power Mode EUA vs UE e densidade de compute\n(snapshot dataset Sorbonne abril 2026)",
        "fig3_ylabel_left": "Indice CACI Power Mode (UE = 1)",
        "fig3_ylabel_right": "H100-eq por T$ de PIB (UE = 1)",
        "fig3_labels": ["Estados Unidos", "Uniao Europeia"],
        "fig3_source": "Fonte: painel publico America-First-IA, formula F^0,40 x L^0,20 x R^0,15 / E^0,25",
        "fig3_annot_caci": "x3,46\nCACI Power",
        "fig3_annot_dens": "x8,2\nH100-eq / T$",

        "fig4_title": "Taxa de Adocao de IA pelas Empresas\n(Estados Unidos vs Uniao Europeia, 2025)",
        "fig4_ylabel": "% de empresas usando IA",
        "fig4_cats": ["Pequenas empresas", "Grandes empresas"],
        "fig4_legend": ["Estados Unidos", "Uniao Europeia"],
        "fig4_source": "Fontes: Parlamento Europeu (2025), US Chamber of Commerce (2025)",
        "fig4_gap_label": "Gap",

        "fig5_title": "Dominancia Americana nos Pontos de Estrangulamento\nda Cadeia de Valor da IA (2025)",
        "fig5_cats": ["GPUs data center\n(Nvidia)", "Infraestrutura\ncloud", "Capital de risco\nIA generativa"],
        "fig5_ylabel": "Participacao de mercado controlada por atores dos EUA (%)",
        "fig5_source": "Fontes: OCDE (2025), Fed Board (2025), Bruegel (2024)",
        "fig5_threshold": "Limite 50%",

        "fig6_title": "Quadro Teorico Integrado: Do Protecionismo Tecnologico\na Divergencia de Competitividade",
        "fig6_boxes": [
            "PROTECIONISMO\nTECNOLOGICO EUA\n(Controles exportacao,\ntarifas, cotas)",
            "RESTRICAO DO\nCOMPUTE\nEUROPEU\n(CACI Power\nEUA/UE = 3,46:1)",
            "DIVERGENCIA DE\nPRODUTIVIDADE\n(J-curve atrasada,\ncustos elevados)",
            "DEPENDENCIA\nESTRATEGICA\n(Vendor lock-in\ngeopolitico)",
        ],
        "fig6_amplifiers": ["Energia\n(custos x1,6 vs EUA)", "Robotica IA\n(demanda x2 compute)"],
        "fig6_theories": [
            "Weaponized\nInterdependence\n(Farrell & Newman)",
            "GPT & J-Curve\n(Brynjolfsson et al.)",
            "Concentracao\n& Rendas\n(Martens, OCDE)",
            "Soberania\nDigital\n(Mugge, Hawkins)",
        ],
        "fig6_source": "Elaboracao do autor - Quadro teorico, secao 1.3",
        "fig6_amp_label": "AMPLIFICADORES",

        "fig7_title": "Decomposicao do CACI Power Mode\nF^0,40 x L^0,20 x R^0,15 / E^0,25 (pesos 40/20/15/25)",
        "fig7_axes": ["Compute (F)", "Trabalho (L)", "Acesso (R)", "Energia (E)"],
        "fig7_legend": ["Estados Unidos", "Uniao Europeia", "Franca"],
        "fig7_source": "Fonte: painel publico America-First-IA. Valores normalizados (EUA = 100 em cada eixo).",
        "fig7_caption": "Pesos dos expoentes: F=0,40 - L=0,20 - R=0,15 - E=0,25. Soma = 1.",
        "fig7_pie_title": "Pesos dos expoentes",
        "fig7_index_label": "Indice (EUA = 100)",

        "fig8_title": "CACI fisico vs CACI soberano\n(F instalado vs F detido domesticamente)",
        "fig8_ylabel": "Score CACI Power Mode (EUA = 100)",
        "fig8_legend_phys": "CACI fisico (F_total)",
        "fig8_legend_sov": "CACI soberano (F domestico)",
        "fig8_source": "Fonte: painel publico America-First-IA, classificacao por Owner. Caso EAU ilustra o offshoring dos EUA (gap 56 -> 6).",
        "fig8_gap_label": "Gap",
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def setup_style() -> None:
    """Apply a consistent matplotlib style for all figures."""
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.facecolor": BG_COLOR,
        "figure.facecolor": "white",
        "axes.grid": True,
        "grid.color": GRID_COLOR,
        "grid.alpha": 0.7,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def save_fig(fig, name: str, lang_suffix: str) -> Path:
    """Persist the figure to disk under OUTPUT_DIR with a localised suffix."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"{name}_{lang_suffix}.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white", edgecolor="none")
    plt.close(fig)
    log.info("  saved %s", path.name)
    return path


# ---------------------------------------------------------------------------
# Figure 1.1 - Data center electricity consumption
# ---------------------------------------------------------------------------

def fig1_energy_datacenter(L: dict[str, Any]) -> Path:
    """Render IEA data center consumption projection 2022-2030."""
    years = np.array([2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])
    total_twh = np.array([310, 360, 415, 500, 580, 670, 760, 850, 945])
    ai_share = np.array([0.10, 0.13, 0.17, 0.22, 0.27, 0.32, 0.36, 0.39, 0.42])
    ai_twh = total_twh * ai_share

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    ax.fill_between(years, total_twh, color=US_COLOR, alpha=0.15, label=L["fig1_label_total"])
    ax.plot(years, total_twh, color=US_COLOR, linewidth=2.5, marker="o", markersize=6)
    ax.fill_between(years, ai_twh, color=CN_COLOR, alpha=0.25, label=L["fig1_label_ai"])
    ax.plot(years, ai_twh, color=CN_COLOR, linewidth=2, marker="s", markersize=5, linestyle="--")

    ax.annotate(L["fig1_annot_2024"], xy=(2024, 415), xytext=(2023.2, 520),
                fontsize=10, fontweight="bold", color=US_COLOR,
                arrowprops=dict(arrowstyle="->", color=US_COLOR, lw=1.5))
    ax.annotate(L["fig1_annot_2030"], xy=(2030, 945), xytext=(2028.5, 1020),
                fontsize=10, fontweight="bold", color=US_COLOR,
                arrowprops=dict(arrowstyle="->", color=US_COLOR, lw=1.5))

    ax.axvspan(2025.5, 2030.5, alpha=0.05, color="gray")

    ax.set_title(L["fig1_title"], fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel(L["fig1_ylabel"], fontsize=12)
    ax.set_xlim(2021.5, 2030.5)
    ax.set_ylim(0, 1100)
    ax.set_xticks(years)
    ax.legend(loc="upper left", fontsize=10, framealpha=0.9)
    ax.text(0.5, -0.1, L["fig1_source"], transform=ax.transAxes, fontsize=8,
            color="gray", ha="center", fontstyle="italic")

    return save_fig(fig, "Fig_1.1_Energy_DataCenters", L["suffix"])


# ---------------------------------------------------------------------------
# Figure 1.2 - Semiconductor market 2020-2030
# ---------------------------------------------------------------------------

def fig2_semiconductor_market(L: dict[str, Any]) -> Path:
    """Render the SIA/McKinsey/Deloitte semiconductor market projection."""
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])
    total_mkt = np.array([440, 556, 574, 527, 628, 720, 850, 1000, 1150, 1350, 1600])
    ai_share = np.array([0.05, 0.06, 0.08, 0.12, 0.18, 0.25, 0.32, 0.36, 0.40, 0.43, 0.45])
    ai_mkt = total_mkt * ai_share

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    ax.bar(years, total_mkt, width=0.7, color=US_COLOR, alpha=0.3,
           label=L["fig2_label_total"], edgecolor=US_COLOR, linewidth=0.5)
    ax.bar(years, ai_mkt, width=0.7, color=ACCENT3, alpha=0.8,
           label=L["fig2_label_ai"], edgecolor=ACCENT3, linewidth=0.5)

    for yr, val in zip(years, total_mkt):
        if yr in (2020, 2024, 2030):
            ax.text(yr, val + 25, f"${val}B", ha="center", fontsize=9,
                    fontweight="bold", color=US_COLOR)

    ax.annotate(L["fig2_cagr"], xy=(2027, 1050), fontsize=12, fontweight="bold",
                color=ACCENT1, ha="center",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                          edgecolor=ACCENT1, alpha=0.9))

    ax.axvspan(2024.5, 2030.5, alpha=0.05, color="gray")

    ax.set_title(L["fig2_title"], fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel(L["fig2_ylabel"], fontsize=12)
    ax.set_xlim(2019.2, 2031)
    ax.set_ylim(0, 1800)
    ax.set_xticks(years)
    ax.legend(loc="upper left", fontsize=10, framealpha=0.9)
    ax.text(0.5, -0.1, L["fig2_source"], transform=ax.transAxes, fontsize=8,
            color="gray", ha="center", fontstyle="italic")

    return save_fig(fig, "Fig_1.2_Semiconductor_Market", L["suffix"])


# ---------------------------------------------------------------------------
# Figure 1.3 - CACI Power ratio + compute density (DASHBOARD-ALIGNED)
# ---------------------------------------------------------------------------

def fig3_compute_gap(L: dict[str, Any]) -> Path:
    """Replace the obsolete x15 placeholder with two grounded ratios.

    Left panel : CACI Power Mode index (US vs EU = 3.46:1).
    Right panel: H100-eq density per T$ GDP (US vs EU = 8.2:1).
    Both numbers are computed from the live dashboard dataset.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6.2))

    # ---- Left: CACI Power Mode (normalised, EU = 1) ----
    caci_vals = [CACI_POWER_RATIO_US_EU, 1.0]
    bars = ax1.bar(L["fig3_labels"], caci_vals, width=0.5,
                   color=[US_COLOR, EU_COLOR], edgecolor="white", linewidth=2)
    for bar, val, color in zip(bars, caci_vals, [US_COLOR, EU_COLOR]):
        ax1.text(bar.get_x() + bar.get_width() / 2, val + 0.08,
                 f"{val:.2f}".replace(".", ","),
                 ha="center", fontsize=22, fontweight="bold", color=color)

    ax1.annotate("", xy=(0, CACI_POWER_RATIO_US_EU - 0.3), xytext=(1, 1.3),
                 arrowprops=dict(arrowstyle="<->", color=CN_COLOR, lw=2.5))
    ax1.text(0.5, (CACI_POWER_RATIO_US_EU + 1) / 2 + 0.2, L["fig3_annot_caci"],
             ha="center", fontsize=18, fontweight="bold", color=CN_COLOR,
             path_effects=[pe.withStroke(linewidth=4, foreground="white")])

    ax1.set_ylabel(L["fig3_ylabel_left"], fontsize=11)
    ax1.set_ylim(0, CACI_POWER_RATIO_US_EU * 1.25)

    # ---- Right: compute density (H100-eq / T$ GDP) ----
    dens_vals = [COMPUTE_DENSITY_US_EU, 1.0]
    bars2 = ax2.bar(L["fig3_labels"], dens_vals, width=0.5,
                    color=[US_COLOR, EU_COLOR], edgecolor="white", linewidth=2)
    for bar, val, color in zip(bars2, dens_vals, [US_COLOR, EU_COLOR]):
        ax2.text(bar.get_x() + bar.get_width() / 2, val + 0.2,
                 f"{val:.1f}".replace(".", ","),
                 ha="center", fontsize=22, fontweight="bold", color=color)

    ax2.annotate("", xy=(0, COMPUTE_DENSITY_US_EU - 0.6), xytext=(1, 1.6),
                 arrowprops=dict(arrowstyle="<->", color=CN_COLOR, lw=2.5))
    ax2.text(0.5, (COMPUTE_DENSITY_US_EU + 1) / 2 + 0.4, L["fig3_annot_dens"],
             ha="center", fontsize=18, fontweight="bold", color=CN_COLOR,
             path_effects=[pe.withStroke(linewidth=4, foreground="white")])

    ax2.set_ylabel(L["fig3_ylabel_right"], fontsize=11)
    ax2.set_ylim(0, COMPUTE_DENSITY_US_EU * 1.25)

    fig.suptitle(L["fig3_title"], fontsize=13, fontweight="bold", y=1.02)
    fig.text(0.5, -0.04, L["fig3_source"], fontsize=8, color="gray",
             ha="center", fontstyle="italic")

    fig.tight_layout()
    return save_fig(fig, "Fig_1.3_CACI_Compute_Gap", L["suffix"])


# ---------------------------------------------------------------------------
# Figure 1.4 - AI adoption: US vs EU
# ---------------------------------------------------------------------------

def fig4_ai_adoption(L: dict[str, Any]) -> Path:
    """Render small/large enterprise AI adoption gap between US and EU."""
    fig, ax = plt.subplots(figsize=(10, 6.5))

    cats = L["fig4_cats"]
    us_vals = [58, 72]
    eu_vals = [11, 41]

    x = np.arange(len(cats))
    width = 0.32

    bars_us = ax.bar(x - width / 2, us_vals, width, color=US_COLOR,
                     label=L["fig4_legend"][0], edgecolor="white", linewidth=1.5)
    bars_eu = ax.bar(x + width / 2, eu_vals, width, color=EU_COLOR,
                     label=L["fig4_legend"][1], edgecolor="white", linewidth=1.5)

    for bar, val in zip(bars_us, us_vals):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5, f"{val}%",
                ha="center", fontsize=14, fontweight="bold", color=US_COLOR)
    for bar, val in zip(bars_eu, eu_vals):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5, f"{val}%",
                ha="center", fontsize=14, fontweight="bold", color=EU_COLOR)

    for i, (us, eu) in enumerate(zip(us_vals, eu_vals)):
        gap = us - eu
        mid = (us + eu) / 2
        ax.annotate(f"{L['fig4_gap_label']}: {gap}pp", xy=(i + 0.42, mid),
                    fontsize=10, color=CN_COLOR, fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="#FFF3E0",
                              edgecolor=CN_COLOR, alpha=0.8))

    ax.set_title(L["fig4_title"], fontsize=13, fontweight="bold", pad=15)
    ax.set_ylabel(L["fig4_ylabel"], fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=12)
    ax.set_ylim(0, 90)
    ax.legend(fontsize=11, framealpha=0.9)
    ax.text(0.5, -0.1, L["fig4_source"], transform=ax.transAxes, fontsize=8,
            color="gray", ha="center", fontstyle="italic")

    return save_fig(fig, "Fig_1.4_AI_Adoption_Gap", L["suffix"])


# ---------------------------------------------------------------------------
# Figure 1.5 - US chokepoints
# ---------------------------------------------------------------------------

def fig5_chokepoints(L: dict[str, Any]) -> Path:
    """Render US dominance share over the three AI value-chain chokepoints."""
    fig, ax = plt.subplots(figsize=(10, 6.5))

    cats = L["fig5_cats"]
    vals = [80, 70, 75]
    colors_grad = [US_COLOR, "#2471A3", "#2E86C1"]

    bars = ax.barh(cats, vals, height=0.55, color=colors_grad,
                   edgecolor="white", linewidth=2)
    for bar, val in zip(bars, vals):
        ax.text(val + 1.5, bar.get_y() + bar.get_height() / 2, f"{val}%",
                va="center", fontsize=16, fontweight="bold", color=US_COLOR)

    ax.axvline(x=50, color=CN_COLOR, linewidth=1.5, linestyle="--", alpha=0.6)
    ax.text(51, 2.7, L["fig5_threshold"], fontsize=9, color=CN_COLOR,
            fontstyle="italic")

    ax.set_title(L["fig5_title"], fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel(L["fig5_ylabel"], fontsize=11)
    ax.set_xlim(0, 100)
    ax.invert_yaxis()
    ax.text(0.5, -0.1, L["fig5_source"], transform=ax.transAxes, fontsize=8,
            color="gray", ha="center", fontstyle="italic")

    return save_fig(fig, "Fig_1.5_US_Chokepoints", L["suffix"])


# ---------------------------------------------------------------------------
# Figure 1.6 - Integrated theoretical framework
# ---------------------------------------------------------------------------

def fig6_theoretical_framework(L: dict[str, Any]) -> Path:
    """Render the conceptual chain from US protectionism to strategic dependence."""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    ax.text(7, 8.6, L["fig6_title"], ha="center", fontsize=14, fontweight="bold")

    # Main chain
    box_positions = [(1.2, 5.5), (4.4, 5.5), (7.6, 5.5), (10.8, 5.5)]
    box_colors = [CN_COLOR, ACCENT3, ACCENT2, US_COLOR]
    box_w, box_h = 2.6, 2.2

    for i, (x, y) in enumerate(box_positions):
        rect = mpatches.FancyBboxPatch((x, y), box_w, box_h,
                                       boxstyle="round,pad=0.15",
                                       facecolor=box_colors[i], alpha=0.12,
                                       edgecolor=box_colors[i], linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + box_w / 2, y + box_h / 2, L["fig6_boxes"][i],
                ha="center", va="center", fontsize=8.5, fontweight="bold",
                color=box_colors[i])

    arrow_style = dict(arrowstyle="->", color="#555", lw=2.5,
                       connectionstyle="arc3,rad=0")
    for i in range(3):
        x_start = box_positions[i][0] + box_w
        x_end = box_positions[i + 1][0]
        ax.annotate("", xy=(x_end, 6.6), xytext=(x_start, 6.6),
                    arrowprops=arrow_style)

    # Amplifiers
    amp_positions = [(3.5, 2.8), (8.0, 2.8)]
    for i, (x, y) in enumerate(amp_positions):
        rect = mpatches.FancyBboxPatch((x, y), 2.8, 1.4,
                                       boxstyle="round,pad=0.12",
                                       facecolor=ACCENT1, alpha=0.12,
                                       edgecolor=ACCENT1, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + 1.4, y + 0.7, L["fig6_amplifiers"][i],
                ha="center", va="center", fontsize=8.5,
                fontweight="bold", color=ACCENT1)

    ax.text(7, 4.5, L["fig6_amp_label"], ha="center", fontsize=10,
            fontweight="bold", color=ACCENT1,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor=ACCENT1))

    for x_amp in (4.9, 9.4):
        ax.annotate("", xy=(x_amp, 5.5), xytext=(x_amp, 4.2),
                    arrowprops=dict(arrowstyle="->", color=ACCENT1, lw=1.8,
                                    linestyle="--"))

    # Theories
    theory_positions = [(0.5, 0.8), (3.7, 0.8), (6.9, 0.8), (10.1, 0.8)]
    for i, (x, y) in enumerate(theory_positions):
        rect = mpatches.FancyBboxPatch((x, y), 2.8, 1.4,
                                       boxstyle="round,pad=0.1",
                                       facecolor="#F5F5F5",
                                       edgecolor="#999", linewidth=1,
                                       linestyle="--")
        ax.add_patch(rect)
        ax.text(x + 1.4, y + 0.7, L["fig6_theories"][i],
                ha="center", va="center", fontsize=7.5,
                color="#555", fontstyle="italic")

    ax.text(7, 0.15, L["fig6_source"], ha="center", fontsize=8,
            color="gray", fontstyle="italic")

    return save_fig(fig, "Fig_1.6_Theoretical_Framework", L["suffix"])


# ---------------------------------------------------------------------------
# Figure 1.7 - CACI Power Mode decomposition (NEW)
# ---------------------------------------------------------------------------

def fig7_caci_decomposition(L: dict[str, Any]) -> Path:
    """Visualise the four CACI dimensions and the exponent weights.

    Left:  per-region scores on each axis (F, L, R, E) normalised at US = 100.
           Note that for E (energy price), values >100 mean MORE expensive,
           which penalises the region in the formula.
    Right: pie chart of the exponent weights (40/20/15/25).
    """
    fig = plt.figure(figsize=(13, 7))
    gs = fig.add_gridspec(1, 2, width_ratios=[2, 1], wspace=0.3)
    ax_bar = fig.add_subplot(gs[0])
    ax_pie = fig.add_subplot(gs[1])

    region_scores = {
        L["fig7_legend"][0]: [100.0, 100.0, 100.0, 100.0],   # USA reference
        L["fig7_legend"][1]: [ 18.0,  88.5,  90.0, 220.0],   # EU
        L["fig7_legend"][2]: [ 35.0,  43.0,  90.0, 190.0],   # France
    }
    axes_labels = L["fig7_axes"]
    n_axes = len(axes_labels)
    x = np.arange(n_axes)
    width = 0.27
    colors = [US_COLOR, EU_COLOR, FR_COLOR]

    for i, (region, scores) in enumerate(region_scores.items()):
        offset = (i - 1) * width
        bars = ax_bar.bar(x + offset, scores, width, color=colors[i],
                          label=region, edgecolor="white", linewidth=1.2)
        for bar, val in zip(bars, scores):
            ax_bar.text(bar.get_x() + bar.get_width() / 2, val + 4,
                        f"{val:.0f}", ha="center", fontsize=8.5,
                        fontweight="bold", color=colors[i])

    ax_bar.axhline(y=100, color="gray", linewidth=0.8, linestyle=":")
    ax_bar.set_xticks(x)
    ax_bar.set_xticklabels(axes_labels, fontsize=10)
    ax_bar.set_ylabel(L["fig7_index_label"], fontsize=10)
    ax_bar.set_ylim(0, 260)
    ax_bar.legend(loc="upper center", fontsize=9, framealpha=0.9, ncol=3,
                  bbox_to_anchor=(0.5, -0.08))
    ax_bar.set_title(L["fig7_title"], fontsize=12, fontweight="bold", pad=12)
    ax_bar.text(0.5, -0.22, L["fig7_caption"], transform=ax_bar.transAxes,
                fontsize=8, color="#555", ha="center", fontstyle="italic")

    weights = [40, 20, 15, 25]
    pie_labels = [f"{lbl}\n{w}%" for lbl, w in zip(axes_labels, weights)]
    pie_colors = [US_COLOR, ACCENT1, ACCENT2, ACCENT3]
    ax_pie.pie(weights, labels=pie_labels, colors=pie_colors,
               startangle=90, counterclock=False,
               wedgeprops=dict(edgecolor="white", linewidth=2),
               textprops=dict(fontsize=9, fontweight="bold"))
    ax_pie.set_title(L["fig7_pie_title"], fontsize=10, fontweight="bold", pad=10)

    fig.text(0.5, -0.02, L["fig7_source"], fontsize=8, color="gray",
             ha="center", fontstyle="italic")

    return save_fig(fig, "Fig_1.7_CACI_Decomposition", L["suffix"])


# ---------------------------------------------------------------------------
# Figure 1.8 - Physical CACI vs Sovereign CACI (NEW)
# ---------------------------------------------------------------------------

def fig8_phys_vs_sov(L: dict[str, Any]) -> Path:
    """Render the gap between Physical and Sovereign CACI per region.

    The gap quantifies dependence on foreign hyperscalers: a region with
    high Physical but low Sovereign CACI hosts foreign-owned compute and
    is therefore strategically vulnerable to extraterritorial decisions.
    """
    regions = list(CACI_PHYS_VS_SOV.keys())
    phys = [CACI_PHYS_VS_SOV[r]["phys"] for r in regions]
    sov = [CACI_PHYS_VS_SOV[r]["sov"] for r in regions]

    fig, ax = plt.subplots(figsize=(11, 6.5))

    x = np.arange(len(regions))
    width = 0.36

    bars_phys = ax.bar(x - width / 2, phys, width, color=US_COLOR,
                       alpha=0.45, label=L["fig8_legend_phys"],
                       edgecolor=US_COLOR, linewidth=1.5)
    bars_sov = ax.bar(x + width / 2, sov, width, color=ACCENT1,
                      label=L["fig8_legend_sov"],
                      edgecolor=ACCENT1, linewidth=1.5)

    for bar, val in zip(bars_phys, phys):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 3,
                f"{val:.0f}", ha="center", fontsize=10,
                fontweight="bold", color=US_COLOR)
    for bar, val in zip(bars_sov, sov):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 3,
                f"{val:.0f}", ha="center", fontsize=10,
                fontweight="bold", color=ACCENT1)

    for i in range(len(regions)):
        gap = phys[i] - sov[i]
        if gap >= 5:
            # Anchor inside the bar pair (between phys and sov bars), at mid-height
            mid_y = (phys[i] + sov[i]) / 2
            ax.annotate(
                f"{L['fig8_gap_label']}: {gap:.0f}",
                xy=(i, mid_y),
                xytext=(i, mid_y),
                ha="center", va="center",
                fontsize=9, color=CN_COLOR, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#FFF3E0",
                          edgecolor=CN_COLOR, alpha=0.9),
            )

    ax.set_xticks(x)
    ax.set_xticklabels(regions, fontsize=11)
    ax.set_ylabel(L["fig8_ylabel"], fontsize=11)
    ax.set_ylim(0, max(phys) * 1.18)
    ax.set_title(L["fig8_title"], fontsize=13, fontweight="bold", pad=15)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper right")
    ax.text(0.5, -0.12, L["fig8_source"], transform=ax.transAxes,
            fontsize=8, color="gray", ha="center", fontstyle="italic")

    return save_fig(fig, "Fig_1.8_Physical_vs_Sovereign_CACI", L["suffix"])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

GENERATORS = (
    fig1_energy_datacenter,
    fig2_semiconductor_market,
    fig3_compute_gap,
    fig4_ai_adoption,
    fig5_chokepoints,
    fig6_theoretical_framework,
    fig7_caci_decomposition,
    fig8_phys_vs_sov,
)


def main() -> list[Path]:
    """Generate all Chapter I figures in three languages."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    setup_style()

    log.info("Chapter I figure generation started, output dir = %s", OUTPUT_DIR)
    all_files: list[Path] = []
    for lang_key, L in LANGS.items():
        log.info("Language: %s", L["suffix"])
        for gen in GENERATORS:
            all_files.append(gen(L))

    log.info("Done. %d figures generated.", len(all_files))
    return all_files


if __name__ == "__main__":
    main()
