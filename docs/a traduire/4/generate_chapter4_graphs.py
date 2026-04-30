"""
Chapter IV - Mechanisms of US Competitive Advantage - matplotlib figures
generator (FR/EN/PT-BR).

Renders the seven figures used to illustrate Chapter IV. Figures are
produced in three languages and saved as 300-DPI PNGs.

Figures
-------
4.1  Exponential explosion of training costs 2017-2030 (log scale,
     Bruegel/Martens 2024).
4.2  European cloud market: AWS+Azure+GCP vs EU providers, 2017-2024
     (stacked bars + EU share line).
4.3  Differentiated productivity: theoretical vs achievable AI growth
     under compute constraints (US vs EU).
4.4  Generative AI value chain: EU presence by segment.
4.5  Self-reinforcing cycle of US competitive advantage - all numeric
     references refreshed to the April 2026 dashboard snapshot
     (compute asymmetry x17.6 operational, training cost gap x2.4-3.6,
     cloud dependence 70 percent, achievable productivity gap -1.5 pts,
     CACI Power Mode 3.46:1).
4.6  US vs EU technology investment gap (2021-2025).
4.7  CACI vs other AI competitiveness indices - NEW figure showing
     why the CACI surfaces a 3.46:1 ratio while the IMF AIPI compresses
     it to 1.15:1 (the headline methodological contribution of the
     dissertation).

Output
------
Directory selectable via the CH4_FIG_DIR environment variable
(default: ./figures_ch4). Each figure is saved as
Fig_4.x_NAME_<LANG>.png.

Author: Fabrice Pizzi (Universite Paris-Sorbonne, M2 Economic Intelligence).
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("chapter4_graphs")


# ---------------------------------------------------------------------------
# Live dashboard reference values (Sorbonne 2026 dataset)
# ---------------------------------------------------------------------------

CACI_POWER_RATIO_US_EU = 3.46
US_EU_H100_RATIO_OPERATIONAL = 17.6
PPA_RATIO_EU_US = 1.59
US_SHARE_OPERATIONAL = 76.9
TRAINING_COST_GAP_LOW = 2.4
TRAINING_COST_GAP_HIGH = 3.6
EU_CLOUD_SHARE_US_HYPERSCALERS = 70
PRODUCTIVITY_GAP_PTS = 1.7  # midpoint of -1.5 to -2 pts/year

# CACI score for normalised competitive index figure (Fig 4.7)
INDICES_US_EU_RATIOS = {
    "CACI Power Mode": 3.46,
    "Tortoise Global AI Index": 1.45,
    "IMF AI Preparedness Index": 1.15,
    "Stanford AI Index (compute)": 17.6,
}

OUTPUT_DIR = Path(os.environ.get("CH4_FIG_DIR", "./figures_ch4")).resolve()
DPI = 300
FIGSIZE_WIDE = (12, 6.5)
FIGSIZE_TALL = (12, 9)


# ---------------------------------------------------------------------------
# Visual identity (shared with Chapters I/II/III)
# ---------------------------------------------------------------------------

NAVY = "#1A2744"
GOLD = "#B8922F"
US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
FR_COLOR = "#2E86C1"
CN_COLOR = "#C0392B"
ACCENT1 = "#148F77"
ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"
ACCENT4 = "#2C3E50"
GREY = "#999999"
BG_COLOR = "white"


def _common_style() -> None:
    """Apply the project-wide matplotlib defaults."""
    plt.rcParams.update({
        "figure.facecolor": BG_COLOR,
        "axes.facecolor": BG_COLOR,
        "savefig.facecolor": BG_COLOR,
        "font.family": "DejaVu Sans",
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def save_fig(fig, basename: str, lang_suffix: str) -> Path:
    """Save the figure as a 300-DPI PNG in OUTPUT_DIR."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / f"{basename}_{lang_suffix}.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    log.info("Saved %s", out)
    return out


# ---------------------------------------------------------------------------
# Language packs
# ---------------------------------------------------------------------------

@dataclass
class LangPack:
    """Container for one language version of all Chapter IV figure labels."""

    code: str
    suffix: str

    # Fig 4.1
    f1_title: str = ""
    f1_ylabel: str = ""
    f1_source: str = ""
    f1_annot: str = ""

    # Fig 4.2
    f2_title: str = ""
    f2_ylabel: str = ""
    f2_us: str = ""
    f2_eu: str = ""
    f2_eu_share_label: str = ""
    f2_source: str = ""

    # Fig 4.3
    f3_title: str = ""
    f3_ylabel: str = ""
    f3_cats: list[str] = field(default_factory=list)
    f3_us: str = ""
    f3_eu: str = ""
    f3_gap: str = ""
    f3_source: str = ""

    # Fig 4.4
    f4_title: str = ""
    f4_segments: list[str] = field(default_factory=list)
    f4_eu_presence: list[float] = field(default_factory=list)
    f4_ylabel: str = ""
    f4_absent: str = ""
    f4_compet: str = ""
    f4_source: str = ""

    # Fig 4.5
    f5_title: str = ""
    f5_boxes: list[str] = field(default_factory=list)
    f5_center: str = ""
    f5_source: str = ""

    # Fig 4.6
    f6_title: str = ""
    f6_cats: list[str] = field(default_factory=list)
    f6_us: list[float] = field(default_factory=list)
    f6_eu: list[float] = field(default_factory=list)
    f6_us_label: str = ""
    f6_eu_label: str = ""
    f6_ylabel: str = ""
    f6_source: str = ""

    # Fig 4.7
    f7_title: str = ""
    f7_subtitle: str = ""
    f7_xlabel: str = ""
    f7_source: str = ""
    f7_indices: list[str] = field(default_factory=list)


# ===========================================================================
# Language pack content
# ===========================================================================

FR = LangPack(
    code="fr", suffix="FR",
    f1_title="Explosion exponentielle des couts d'entrainement IA (2017-2030, estimation)",
    f1_ylabel="Cout d'entrainement (USD, echelle log)",
    f1_source="Source : Bruegel/Martens (2024) calibre sur Epoch AI",
    f1_annot="GPT-3 -> GPT-4 -> frontier 2030",
    f2_title="Marche cloud europeen : domination des hyperscalers US (2017-2024)",
    f2_ylabel="Part de marche europeen (pct)",
    f2_us="AWS + Azure + GCP", f2_eu="Fournisseurs UE",
    f2_eu_share_label="Part UE",
    f2_source="Source : Synergy Research Group (juillet 2025)",
    f3_title="Productivite IA US vs UE : potentiel theorique vs realisable",
    f3_ylabel="Croissance annuelle de la productivite (pct/an)",
    f3_cats=["Potentiel theorique\n(scen. accelere)", "Potentiel realisable\n(sous contrainte\ncompute)"],
    f3_us="Etats-Unis", f3_eu="Union europeenne",
    f3_gap=f"Gap\n-{PRODUCTIVITY_GAP_PTS:.1f}\npts/an",
    f3_source="Sources : McKinsey (2024, 2025), FMI (2025), calibration CACI auteur",
    f4_title="Chaine de valeur de l'IA generative : presence europeenne par segment",
    f4_segments=["Semi-conducteurs\nIA (GPU/ASIC)", "Plateformes\ncloud IA", "Modeles de\nfondation",
                 "Outils de\ndeveloppement", "Applications\nsectorielles", "Semi-conducteurs\nspecialises",
                 "Integration\nindustrielle", "Services\nprofessionnels"],
    f4_eu_presence=[2, 5, 8, 10, 70, 55, 65, 50],
    f4_ylabel="Presence europeenne estimee (pct)",
    f4_absent="UE quasi\nabsente", f4_compet="UE\ncompetitive",
    f4_source="Sources : McKinsey (2024), Omdia/Informa, estimations auteur",
    f5_title="Le cercle auto-renforcant de l'avantage concurrentiel US",
    f5_boxes=[
        f"ASYMETRIE\nDE COMPUTE\n(x{US_EU_H100_RATIO_OPERATIONAL:.1f} US/UE op.)",
        f"COUTS TRAINING\nDIFFERENCIES\n(x{TRAINING_COST_GAP_LOW}-{TRAINING_COST_GAP_HIGH})",
        f"DEPENDANCE\nCLOUD US\n({EU_CLOUD_SHARE_US_HYPERSCALERS} pct marche UE)",
        f"PRODUCTIVITE\nCONTRAINTE\n(-{PRODUCTIVITY_GAP_PTS:.1f} pts/an)",
        "CAPTATION\nDES RENTES\n(first-mover)",
    ],
    f5_center=f"PROTECTIONNISME\nSECTION 232\n(institutionnalise\nl'avantage)\nCACI {CACI_POWER_RATIO_US_EU:.2f}:1",
    f5_source="Elaboration auteur - Synthese §4.5 sur snapshot avril 2026",
    f6_title="Ecart d'investissement technologique Etats-Unis vs Europe (2021-2025)",
    f6_cats=["R&D + Capex\ncorporate\n(annuel)", "Startups &\nscale-ups\n(annuel)",
             "Infrastructure\nIA 2025\n(Big Tech)", "Capex cloud\nen Europe\n(US providers)"],
    f6_us=[1200, 380, 320, 40],
    f6_eu=[500, 80, 20, 5],
    f6_us_label="Etats-Unis", f6_eu_label="Union europeenne",
    f6_ylabel="Milliards USD / an",
    f6_source="Sources : McKinsey (2026), AIE (2025), Synergy Research (2025)",
    f7_title="CACI vs autres indices de competitivite IA : ratio US/UE",
    f7_subtitle="Le CACI revele un ecart materiel que les indices multidimensionnels compressent",
    f7_xlabel="Ratio US/UE (echelle log)",
    f7_source="Sources : tableau de bord public (CACI), FMI AIPI (2024), Tortoise Media (2024), Stanford AI Index (2025)",
    f7_indices=["CACI Power Mode\n(cette etude)",
                "Tortoise Global\nAI Index 2024",
                "FMI AI\nPreparedness Index",
                "Stanford AI Index\n(compute brut)"],
)

EN = LangPack(
    code="en", suffix="EN",
    f1_title="Exponential explosion of AI training costs (2017-2030, estimate)",
    f1_ylabel="Training cost (USD, log scale)",
    f1_source="Source: Bruegel/Martens (2024) calibrated on Epoch AI",
    f1_annot="GPT-3 -> GPT-4 -> frontier 2030",
    f2_title="European cloud market: US hyperscaler domination (2017-2024)",
    f2_ylabel="European market share (pct)",
    f2_us="AWS + Azure + GCP", f2_eu="EU providers",
    f2_eu_share_label="EU share",
    f2_source="Source: Synergy Research Group (July 2025)",
    f3_title="US vs EU AI productivity: theoretical vs achievable potential",
    f3_ylabel="Annual productivity growth (pct/yr)",
    f3_cats=["Theoretical potential\n(accel. scen.)", "Achievable potential\n(under compute\nconstraints)"],
    f3_us="United States", f3_eu="European Union",
    f3_gap=f"Gap\n-{PRODUCTIVITY_GAP_PTS:.1f}\npts/yr",
    f3_source="Sources: McKinsey (2024, 2025), IMF (2025), CACI calibration by author",
    f4_title="Generative AI value chain: European presence by segment",
    f4_segments=["AI semiconductors\n(GPU/ASIC)", "AI cloud\nplatforms", "Foundation\nmodels",
                 "Development\ntools", "Sectoral\napplications", "Specialised\nsemiconductors",
                 "Industrial\nintegration", "Professional\nservices"],
    f4_eu_presence=[2, 5, 8, 10, 70, 55, 65, 50],
    f4_ylabel="Estimated European presence (pct)",
    f4_absent="EU\nquasi-absent", f4_compet="EU\ncompetitive",
    f4_source="Sources: McKinsey (2024), Omdia/Informa, author estimates",
    f5_title="The self-reinforcing cycle of US competitive advantage",
    f5_boxes=[
        f"COMPUTE\nASYMMETRY\n(x{US_EU_H100_RATIO_OPERATIONAL:.1f} US/EU op.)",
        f"DIFFERENTIATED\nTRAINING COSTS\n(x{TRAINING_COST_GAP_LOW}-{TRAINING_COST_GAP_HIGH})",
        f"US CLOUD\nDEPENDENCE\n({EU_CLOUD_SHARE_US_HYPERSCALERS} pct EU market)",
        f"CONSTRAINED\nPRODUCTIVITY\n(-{PRODUCTIVITY_GAP_PTS:.1f} pts/yr)",
        "RENT\nCAPTURE\n(first-mover)",
    ],
    f5_center=f"SECTION 232\nPROTECTIONISM\n(institutionalises\nthe advantage)\nCACI {CACI_POWER_RATIO_US_EU:.2f}:1",
    f5_source="Author's elaboration - Synthesis 4.5 on April 2026 snapshot",
    f6_title="US vs Europe technology investment gap (2021-2025)",
    f6_cats=["R&D + Capex\ncorporate\n(annual)", "Startups &\nscale-ups\n(annual)",
             "AI Infrastructure\n2025\n(Big Tech)", "Cloud capex\nin Europe\n(US providers)"],
    f6_us=[1200, 380, 320, 40],
    f6_eu=[500, 80, 20, 5],
    f6_us_label="United States", f6_eu_label="European Union",
    f6_ylabel="Billion USD / year",
    f6_source="Sources: McKinsey (2026), IEA (2025), Synergy Research (2025)",
    f7_title="CACI vs other AI competitiveness indices: US/EU ratio",
    f7_subtitle="The CACI surfaces a material gap that multidimensional indices compress",
    f7_xlabel="US/EU ratio (log scale)",
    f7_source="Sources: public dashboard (CACI), IMF AIPI (2024), Tortoise Media (2024), Stanford AI Index (2025)",
    f7_indices=["CACI Power Mode\n(this study)",
                "Tortoise Global\nAI Index 2024",
                "IMF AI\nPreparedness Index",
                "Stanford AI Index\n(raw compute)"],
)

PT = LangPack(
    code="pt-br", suffix="PT-BR",
    f1_title="Explosao exponencial dos custos de treinamento IA (2017-2030, estimativa)",
    f1_ylabel="Custo de treinamento (USD, escala log)",
    f1_source="Fonte: Bruegel/Martens (2024) calibrado em Epoch AI",
    f1_annot="GPT-3 -> GPT-4 -> fronteira 2030",
    f2_title="Mercado de nuvem europeu: dominancia dos hyperscalers EUA (2017-2024)",
    f2_ylabel="Parcela do mercado europeu (pct)",
    f2_us="AWS + Azure + GCP", f2_eu="Provedores UE",
    f2_eu_share_label="Parcela UE",
    f2_source="Fonte: Synergy Research Group (julho de 2025)",
    f3_title="Produtividade IA EUA vs UE: potencial teorico vs realizavel",
    f3_ylabel="Crescimento anual da produtividade (pct/ano)",
    f3_cats=["Potencial teorico\n(cen. acelerado)", "Potencial realizavel\n(sob restricao\nde compute)"],
    f3_us="Estados Unidos", f3_eu="Uniao Europeia",
    f3_gap=f"Gap\n-{PRODUCTIVITY_GAP_PTS:.1f}\npts/ano",
    f3_source="Fontes: McKinsey (2024, 2025), FMI (2025), calibracao CACI do autor",
    f4_title="Cadeia de valor da IA generativa: presenca europeia por segmento",
    f4_segments=["Semicondutores\nIA (GPU/ASIC)", "Plataformas\nde nuvem IA", "Modelos de\nfundacao",
                 "Ferramentas de\ndesenvolvimento", "Aplicacoes\nsetoriais", "Semicondutores\nespecializados",
                 "Integracao\nindustrial", "Servicos\nprofissionais"],
    f4_eu_presence=[2, 5, 8, 10, 70, 55, 65, 50],
    f4_ylabel="Presenca europeia estimada (pct)",
    f4_absent="UE quase\nausente", f4_compet="UE\ncompetitiva",
    f4_source="Fontes: McKinsey (2024), Omdia/Informa, estimativas do autor",
    f5_title="O ciclo auto-reforcador da vantagem competitiva dos EUA",
    f5_boxes=[
        f"ASSIMETRIA\nDE COMPUTE\n(x{US_EU_H100_RATIO_OPERATIONAL:.1f} EUA/UE op.)",
        f"CUSTOS TREINAM.\nDIFERENCIADOS\n(x{TRAINING_COST_GAP_LOW}-{TRAINING_COST_GAP_HIGH})",
        f"DEPENDENCIA\nNUVEM EUA\n({EU_CLOUD_SHARE_US_HYPERSCALERS} pct mercado UE)",
        f"PRODUTIVIDADE\nRESTRINGIDA\n(-{PRODUCTIVITY_GAP_PTS:.1f} pts/ano)",
        "CAPTURA\nDE RENDAS\n(first-mover)",
    ],
    f5_center=f"PROTECIONISMO\nSECAO 232\n(institucionaliza\na vantagem)\nCACI {CACI_POWER_RATIO_US_EU:.2f}:1",
    f5_source="Elaboracao do autor - Sintese 4.5 sobre snapshot abril de 2026",
    f6_title="Gap de investimento tecnologico Estados Unidos vs Europa (2021-2025)",
    f6_cats=["P&D + Capex\ncorporativo\n(anual)", "Startups e\nscale-ups\n(anual)",
             "Infraestrutura\nIA 2025\n(Big Tech)", "Capex de nuvem\nna Europa\n(provedores EUA)"],
    f6_us=[1200, 380, 320, 40],
    f6_eu=[500, 80, 20, 5],
    f6_us_label="Estados Unidos", f6_eu_label="Uniao Europeia",
    f6_ylabel="Bilhoes USD / ano",
    f6_source="Fontes: McKinsey (2026), AIE (2025), Synergy Research (2025)",
    f7_title="CACI vs outros indices de competitividade IA: razao EUA/UE",
    f7_subtitle="O CACI revela um gap material que os indices multidimensionais comprimem",
    f7_xlabel="Razao EUA/UE (escala log)",
    f7_source="Fontes: painel publico (CACI), FMI AIPI (2024), Tortoise Media (2024), Stanford AI Index (2025)",
    f7_indices=["CACI Power Mode\n(este estudo)",
                "Tortoise Global\nAI Index 2024",
                "FMI AI\nPreparedness Index",
                "Stanford AI Index\n(compute bruto)"],
)

LANGS: list[LangPack] = [FR, EN, PT]


# ===========================================================================
# Figure 4.1 - Training cost explosion
# ===========================================================================

def fig1_training_costs(L: LangPack) -> Path:
    """Render the exponential explosion of training costs on log scale."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2026, 2028, 2030]
    costs = [1e3, 1e4, 1.5e5, 1e6, 5e6, 5e7, 1.5e8, 2e8, 5e8, 1.5e9, 5e9]

    ax.semilogy(years, costs, color=US_COLOR, marker="o",
                markersize=9, linewidth=3)
    for x, y in zip(years, costs):
        ax.annotate(f"{y:,.0f}",
                    xy=(x, y), xytext=(0, 12), textcoords="offset points",
                    ha="center", fontsize=8, color=US_COLOR)

    ax.axvline(x=2024.5, color=GREY, linestyle="--", alpha=0.5)
    ax.text(2024.7, 1e3, "snapshot 2024 -> projection",
            fontsize=9, color=GREY, fontstyle="italic")

    ax.set_title(L.f1_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_ylabel(L.f1_ylabel, fontsize=11)
    ax.set_xlim(2016.5, 2030.5)
    ax.set_ylim(5e2, 1e10)
    ax.grid(True, which="both", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f1_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_4.1_Training_Costs_Exponential", L.suffix)


# ===========================================================================
# Figure 4.2 - European cloud market
# ===========================================================================

def fig2_cloud_market(L: LangPack) -> Path:
    """Render the EU cloud market with US hyperscaler domination."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    years = [2017, 2019, 2021, 2022, 2024]
    us_share = [50, 58, 65, 67, 70]
    eu_share = [29, 22, 17, 15, 15]
    other = [100 - u - e for u, e in zip(us_share, eu_share)]

    x = np.arange(len(years))
    w = 0.6

    ax.bar(x, us_share, w, color=US_COLOR, alpha=0.9,
           label=L.f2_us, edgecolor="white", linewidth=1)
    ax.bar(x, eu_share, w, bottom=us_share, color=EU_COLOR, alpha=0.9,
           label=L.f2_eu, edgecolor="white", linewidth=1)
    ax.bar(x, other, w,
           bottom=[u + e for u, e in zip(us_share, eu_share)],
           color=ACCENT1, alpha=0.7,
           edgecolor="white", linewidth=1)

    for i in range(len(years)):
        ax.text(i, us_share[i] / 2, f"{us_share[i]} pct",
                ha="center", va="center", fontsize=10,
                fontweight="bold", color="white")
        ax.text(i, us_share[i] + eu_share[i] / 2, f"{eu_share[i]} pct",
                ha="center", va="center", fontsize=9,
                fontweight="bold", color=NAVY)

    ax.set_title(L.f2_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_xticks(x)
    ax.set_xticklabels([str(y) for y in years], fontsize=10)
    ax.set_ylabel(L.f2_ylabel, fontsize=11)
    ax.set_ylim(0, 110)
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f2_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_4.2_Cloud_Market_EU", L.suffix)


# ===========================================================================
# Figure 4.3 - Productivity gap
# ===========================================================================

def fig3_productivity_gap(L: LangPack) -> Path:
    """Render the productivity gap (theoretical vs achievable) US vs EU."""
    fig, ax = plt.subplots(figsize=(11, 7))

    cats = L.f3_cats
    us_vals = [3.0, 2.75]
    eu_vals = [2.75, 1.15]
    x = np.arange(len(cats))
    w = 0.32

    bars_us = ax.bar(x - w / 2, us_vals, w, color=US_COLOR,
                     label=L.f3_us, edgecolor="white", linewidth=1.5)
    bars_eu = ax.bar(x + w / 2, eu_vals, w, color=EU_COLOR,
                     label=L.f3_eu, edgecolor="white", linewidth=1.5)

    for bar, val in zip(bars_us, us_vals):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.08,
                f"+{val:.2f} pct", ha="center", fontsize=10,
                fontweight="bold", color=US_COLOR)
    for bar, val in zip(bars_eu, eu_vals):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.08,
                f"+{val:.2f} pct", ha="center", fontsize=10,
                fontweight="bold", color=EU_COLOR)

    # Highlight gap on second category
    gap_y = (us_vals[1] + eu_vals[1]) / 2
    ax.annotate(L.f3_gap,
                xy=(1, gap_y), xytext=(1.45, gap_y),
                fontsize=10, color=CN_COLOR, fontweight="bold",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.3",
                          facecolor="#FFF3E0",
                          edgecolor=CN_COLOR, alpha=0.9))

    ax.set_title(L.f3_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_ylabel(L.f3_ylabel, fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=10)
    ax.set_ylim(0, 4.0)
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f3_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_4.3_Productivity_Gap", L.suffix)


# ===========================================================================
# Figure 4.4 - Generative AI value chain
# ===========================================================================

def fig4_value_chain(L: LangPack) -> Path:
    """Render the generative AI value chain showing EU presence by segment."""
    fig, ax = plt.subplots(figsize=(13, 7.5))

    segments = L.f4_segments
    presence = L.f4_eu_presence
    x = np.arange(len(segments))
    colors = [CN_COLOR if p < 25 else (ACCENT3 if p < 50 else ACCENT1)
              for p in presence]

    bars = ax.bar(x, presence, color=colors, alpha=0.85,
                  edgecolor="white", linewidth=1.5)

    for bar, p in zip(bars, presence):
        ax.text(bar.get_x() + bar.get_width() / 2, p + 1.5,
                f"{p} pct", ha="center", fontsize=10,
                fontweight="bold", color=bar.get_facecolor())

    # Annotated zones
    ax.axhspan(0, 25, alpha=0.06, color=CN_COLOR)
    ax.axhspan(50, 100, alpha=0.06, color=ACCENT1)
    ax.text(3.5, 12, L.f4_absent, ha="center", va="center",
            fontsize=10, color=CN_COLOR, fontweight="bold", fontstyle="italic")
    ax.text(6.5, 80, L.f4_compet, ha="center", va="center",
            fontsize=10, color=ACCENT1, fontweight="bold", fontstyle="italic")

    ax.set_title(L.f4_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_ylabel(L.f4_ylabel, fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(segments, fontsize=8.5)
    ax.set_ylim(0, 100)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f4_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_4.4_Value_Chain_EU_Presence", L.suffix)


# ===========================================================================
# Figure 4.5 - Self-reinforcing cycle
# ===========================================================================

def fig5_reinforcing_cycle(L: LangPack) -> Path:
    """Render the self-reinforcing cycle of US competitive advantage."""
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(6, 9.55, L.f5_title, ha="center",
            fontsize=14, fontweight="bold", color=NAVY)

    # 5 boxes arranged in a circle around the center
    box_colors = [US_COLOR, ACCENT3, ACCENT2, ACCENT1, CN_COLOR]
    n = 5
    radius_x, radius_y = 4.0, 3.0
    cx, cy = 6, 5
    box_w, box_h = 2.4, 1.6

    box_centers: list[tuple[float, float]] = []
    for i in range(n):
        angle = np.pi / 2 - i * 2 * np.pi / n
        x = cx + radius_x * np.cos(angle)
        y = cy + radius_y * np.sin(angle)
        box_centers.append((x, y))
        rect = mpatches.FancyBboxPatch(
            (x - box_w / 2, y - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.15",
            facecolor=box_colors[i], alpha=0.12,
            edgecolor=box_colors[i], linewidth=2.5,
        )
        ax.add_patch(rect)
        ax.text(x, y, L.f5_boxes[i], ha="center", va="center",
                fontsize=9.5, fontweight="bold",
                color=box_colors[i], linespacing=1.3)

    # Cyclic arrows i -> i+1
    for i in range(n):
        x1, y1 = box_centers[i]
        x2, y2 = box_centers[(i + 1) % n]
        # Pull endpoints inward so arrows do not overlap boxes
        dx, dy = x2 - x1, y2 - y1
        d = (dx ** 2 + dy ** 2) ** 0.5
        shrink = 1.0
        x1s = x1 + dx / d * shrink
        y1s = y1 + dy / d * shrink
        x2s = x2 - dx / d * shrink
        y2s = y2 - dy / d * shrink
        ax.annotate("", xy=(x2s, y2s), xytext=(x1s, y1s),
                    arrowprops=dict(arrowstyle="->", lw=2.2,
                                    color=GOLD, alpha=0.7))

    # Center box
    rect_c = mpatches.FancyBboxPatch(
        (cx - 1.5, cy - 1.0), 3.0, 2.0, boxstyle="round,pad=0.2",
        facecolor=GOLD, alpha=0.18, edgecolor=GOLD, linewidth=3,
    )
    ax.add_patch(rect_c)
    ax.text(cx, cy, L.f5_center, ha="center", va="center",
            fontsize=10, fontweight="bold", color=NAVY, linespacing=1.3)

    ax.text(6, 0.3, L.f5_source, ha="center",
            fontsize=8, color="gray", fontstyle="italic")

    return save_fig(fig, "Fig_4.5_Reinforcing_Cycle", L.suffix)


# ===========================================================================
# Figure 4.6 - Investment gap
# ===========================================================================

def fig6_investment_gap(L: LangPack) -> Path:
    """Render the US vs EU technology investment gap."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    cats = L.f6_cats
    x = np.arange(len(cats))
    w = 0.36

    bars_us = ax.bar(x - w / 2, L.f6_us, w, color=US_COLOR,
                     label=L.f6_us_label, edgecolor="white", linewidth=1.5)
    bars_eu = ax.bar(x + w / 2, L.f6_eu, w, color=EU_COLOR,
                     label=L.f6_eu_label, edgecolor="white", linewidth=1.5)

    for bars, col in [(bars_us, US_COLOR), (bars_eu, EU_COLOR)]:
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 25,
                    f"{int(h)}", ha="center", fontsize=10,
                    fontweight="bold", color=col)

    # Ratio labels
    for i, (us_v, eu_v) in enumerate(zip(L.f6_us, L.f6_eu)):
        if eu_v > 0:
            ratio = us_v / eu_v
            ax.text(i, max(us_v, eu_v) + 90,
                    f"x{ratio:.1f}", ha="center", fontsize=11,
                    fontweight="bold", color=CN_COLOR,
                    bbox=dict(boxstyle="round,pad=0.2",
                              facecolor="#FFF3E0",
                              edgecolor=CN_COLOR, alpha=0.85))

    ax.set_title(L.f6_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_ylabel(L.f6_ylabel, fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=9)
    ax.set_ylim(0, 1500)
    ax.legend(fontsize=11, framealpha=0.9, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f6_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_4.6_Investment_Gap", L.suffix)


# ===========================================================================
# Figure 4.7 - CACI vs other AI competitiveness indices (NEW)
# ===========================================================================

def fig7_caci_vs_other_indices(L: LangPack) -> Path:
    """Render the headline contrast between the CACI ratio and other indices.

    The CACI Power Mode produces a 3.46:1 US/EU ratio. The IMF AIPI
    compresses the same gap to 1.15:1 (because it averages compute with
    regulation, ethics and digital infra). The Stanford AI Index, by
    reporting raw compute, reaches 17.6:1. The CACI sits between these
    two extremes and is the methodologically motivated middle ground.
    """
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    indices = L.f7_indices
    ratios = list(INDICES_US_EU_RATIOS.values())
    # Highlight the CACI bar
    colors = [GOLD, ACCENT3, ACCENT1, US_COLOR]

    y = np.arange(len(indices))
    bars = ax.barh(y, ratios, color=colors, alpha=0.9,
                   edgecolor="white", linewidth=1.5)

    for bar, val in zip(bars, ratios):
        ax.text(val + 0.3, bar.get_y() + bar.get_height() / 2,
                f"{val:.2f}:1", va="center", fontsize=11,
                fontweight="bold", color=bar.get_facecolor())

    # Vertical line at CACI value
    ax.axvline(x=CACI_POWER_RATIO_US_EU, color=GOLD,
               linestyle="--", linewidth=1.5, alpha=0.7)

    ax.set_xscale("log")
    ax.set_yticks(y)
    ax.set_yticklabels(indices, fontsize=10)
    ax.set_xlim(1, 25)
    ax.set_xticks([1, 2, 3, 5, 10, 20])
    ax.set_xticklabels(["1:1", "2:1", "3:1", "5:1", "10:1", "20:1"])
    ax.set_xlabel(L.f7_xlabel, fontsize=10, color="#444")
    ax.set_title(f"{L.f7_title}\n{L.f7_subtitle}",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.grid(axis="x", linestyle=":", alpha=0.4)
    # Invert so CACI (highlight) appears at top
    ax.invert_yaxis()

    fig.text(0.5, 0.005, L.f7_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_4.7_CACI_vs_Other_Indices", L.suffix)


# ===========================================================================
# Main
# ===========================================================================

FIGURES = [
    fig1_training_costs,
    fig2_cloud_market,
    fig3_productivity_gap,
    fig4_value_chain,
    fig5_reinforcing_cycle,
    fig6_investment_gap,
    fig7_caci_vs_other_indices,
]


def main() -> None:
    """Render all 7 figures in 3 languages -> 21 PNGs in OUTPUT_DIR."""
    log.info("Output directory: %s", OUTPUT_DIR)
    _common_style()
    for lp in LANGS:
        log.info("--- Rendering language %s ---", lp.suffix)
        for fn in FIGURES:
            fn(lp)
    log.info("Done. %d figures rendered.", len(LANGS) * len(FIGURES))


if __name__ == "__main__":
    main()
