"""
Chapter III - Empirical Diagnosis - matplotlib figures generator (FR/EN/PT-BR).

Renders the seven figures used to illustrate Chapter III of the doctoral
study "AI for Americans First". Figures are produced in three languages
and saved as 300-DPI PNGs.

Figures
-------
3.1  Data center electricity consumption by region 2020-2030 (stacked
     area, IEA Energy and AI 2025).
3.2  Global semiconductor sales 2020-2026 (segmented stacked bars + YoY
     growth line, SIA/WSTS February 2026).
3.3  Geographical distribution of GPU cluster performance (stacked bar
     2019-2025, Epoch AI). Annotation refreshed to "US/EU ratio ~17.6:1".
3.4  Timeline of US regulatory measures 2022-2026 (Biden denial strategy
     -> Trump capture strategy).
3.5  CACI calibration - now using the live April 2026 dashboard values
     (F ratio 17.6:1, E ratio 1.59x, CACI Power Mode ratio 3.46:1)
     instead of the obsolete 15 / 2.5 / 7-12 figures.
3.6  US dominance indicators dashboard - all values refreshed to the
     April 2026 snapshot (operational compute share 76.9 percent, etc.).
3.7  US vs EU compute trajectory 2020-2026 (NEW) - log-scale H100-eq
     curve that visually surfaces the divergence between the two zones
     since the BIS October 2022 shock.

Output
------
Directory selectable via the CH3_FIG_DIR environment variable
(default: ./figures_ch3). Each figure is saved as
Fig_3.x_NAME_<LANG>.png.

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
log = logging.getLogger("chapter3_graphs")


# ---------------------------------------------------------------------------
# Live dashboard reference values (Sorbonne 2026 dataset)
# ---------------------------------------------------------------------------

CACI_POWER_RATIO_US_EU = 3.46
US_EU_H100_RATIO = 17.6
PPA_RATIO_EU_US = 1.59
US_SHARE_OPERATIONAL = 76.9
CN_SHARE_OPERATIONAL = 12.8
EU_SHARE_OPERATIONAL = 4.4

# Cumulative trajectory by First Operational Date (true reconstruction from
# the dashboard CSV, operational clusters only). Year-end values, in
# H100-equivalents (thousands). Used by Fig 3.7.
US_TRAJ_H100K = [21, 32, 68, 233, 908, 1395]    # 2020-2025 year-end
EU_TRAJ_H100K = [3, 4, 12, 20, 45, 79]           # EU(13)
CN_TRAJ_H100K = [11, 21, 32, 48, 213, 231]
TRAJ_YEARS = [2020, 2021, 2022, 2023, 2024, 2025]

OUTPUT_DIR = Path(os.environ.get("CH3_FIG_DIR", "./figures_ch3")).resolve()
DPI = 300
FIGSIZE_WIDE = (12, 6.5)
FIGSIZE_TALL = (12, 9)


# ---------------------------------------------------------------------------
# Visual identity (shared with Chapters I and II)
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
    """Container for one language version of all Chapter III figure labels."""

    code: str
    suffix: str

    # Fig 3.1
    f1_title: str = ""
    f1_ylabel: str = ""
    f1_us: str = ""
    f1_cn: str = ""
    f1_eu: str = ""
    f1_rest: str = ""
    f1_source: str = ""
    f1_proj: str = ""

    # Fig 3.2
    f2_title: str = ""
    f2_ylabel: str = ""
    f2_logic: str = ""
    f2_memory: str = ""
    f2_other: str = ""
    f2_source: str = ""
    f2_growth: str = ""

    # Fig 3.3
    f3_title: str = ""
    f3_ylabel: str = ""
    f3_us: str = ""
    f3_cn: str = ""
    f3_eu: str = ""
    f3_rest: str = ""
    f3_source: str = ""
    f3_note: str = ""

    # Fig 3.4
    f4_title: str = ""
    f4_events: list[tuple[str, str, str]] = field(default_factory=list)
    f4_source: str = ""
    f4_phase_d: str = ""
    f4_phase_c: str = ""

    # Fig 3.5
    f5_title: str = ""
    f5_components: list[str] = field(default_factory=list)
    f5_values_label: list[str] = field(default_factory=list)
    f5_ylabel: str = ""
    f5_source: str = ""

    # Fig 3.6
    f6_title: str = ""
    f6_indicators: list[str] = field(default_factory=list)
    f6_us_vals: list[float] = field(default_factory=list)
    f6_cn_vals: list[float] = field(default_factory=list)
    f6_eu_vals: list[float] = field(default_factory=list)
    f6_us_label: str = ""
    f6_cn_label: str = ""
    f6_eu_label: str = ""
    f6_ylabel: str = ""
    f6_source: str = ""

    # Fig 3.7 (NEW)
    f7_title: str = ""
    f7_subtitle: str = ""
    f7_ylabel: str = ""
    f7_us: str = ""
    f7_cn: str = ""
    f7_eu: str = ""
    f7_bis_label: str = ""
    f7_section232_label: str = ""
    f7_source: str = ""


# ===========================================================================
# Language pack content
# ===========================================================================

FR = LangPack(
    code="fr", suffix="FR",
    f1_title="Consommation electrique des centres de donnees par region (2020-2030, TWh)",
    f1_ylabel="TWh / an",
    f1_us="Etats-Unis", f1_cn="Chine", f1_eu="UE", f1_rest="Reste du monde",
    f1_source="Source : AIE Energy and AI (2025), Tableau 4 du chapitre",
    f1_proj="Projection",
    f2_title="Ventes mondiales de semi-conducteurs 2020-2026 (milliards USD, SIA/WSTS)",
    f2_ylabel="Milliards USD",
    f2_logic="Puces logiques (GPU, CPU, ASIC)",
    f2_memory="Memoire (DRAM, NAND)",
    f2_other="Autres (analogique, discret, capteurs)",
    f2_source="Sources : SIA/WSTS (fevrier 2026), Tableau 5 du chapitre",
    f2_growth="Croissance annuelle",
    f3_title="Repartition geographique de la performance des clusters GPU (2019-2025)",
    f3_ylabel="Part de la performance mondiale (pct)",
    f3_us="Etats-Unis", f3_cn="Chine", f3_eu="UE", f3_rest="Reste du monde",
    f3_source="Sources : Epoch AI / Pilz et al. (2025), tableau de bord avril 2026",
    f3_note=f"Ratio US/UE ~ {US_EU_H100_RATIO}:1 sur le compute operationnel (avril 2026)",
    f4_title="Chronologie des mesures US sur les semi-conducteurs et l'IA (2022-2026) : du controle export au protectionnisme tarifaire",
    f4_events=[
        ("Oct.\n2022", "Controles export BIS\nGPU avances, SME\nCible : Chine", "Biden"),
        ("Oct.\n2023", "Mise a jour seuils\n+40 pays, A800/H800\ncaptures", "Biden"),
        ("Dec.\n2024", "Vague 3 : 24 types SME\nHBM, 140 entites", "Biden"),
        ("Jan.\n2025", "AI Diffusion Rule\nModeles + cloud\n120 pays, 3 paliers", "Biden"),
        ("Jul.\n2025", "America's AI\nAction Plan\nDereglementation US", "Trump"),
        ("Jan.\n2026", "Section 232\nTarif 25 pct GPU\nExemption domestique US", "Trump"),
    ],
    f4_source="Sources : BIS, Maison-Blanche, Pillsbury Law (2026), Gibson Dunn (2026)",
    f4_phase_d="Strategie de denial\n(deni d'acces)",
    f4_phase_c="Strategie de capture\n(protectionnisme offensif)",
    f5_title="Calibration CACI : decomposition de l'avantage US (avril 2026)",
    f5_components=["Compute installe\n(ratio F)", "Cout energetique\n(ratio E, PPA)", "CACI resultant\n(Power Mode)"],
    f5_values_label=[f"x{US_EU_H100_RATIO}", f"x{PPA_RATIO_EU_US}", f"{CACI_POWER_RATIO_US_EU}:1"],
    f5_ylabel="Ratio US/UE",
    f5_source="Elaboration auteur - Section 3.3.3, donnees Epoch AI / dashboard avril 2026",
    f6_title=f"Synthese : indicateurs de la domination US en compute IA (snapshot avril 2026)",
    f6_indicators=["Performance\nclusters GPU\n(operationnel)", "F_total\n(op + planifie)",
                   "Secteur prive\ncompute IA", "Consommation\ndata centers",
                   "Investissement\nIA 2025", "CACI\nPower Mode"],
    f6_us_vals=[76.9, 49.9, 65, 45, 85, 100],
    f6_eu_vals=[4.4, 3.3, 3, 15, 5, 28.9],
    f6_cn_vals=[12.8, 0.5, 12, 25, 8, 15.7],
    f6_us_label="Etats-Unis", f6_cn_label="Chine", f6_eu_label="UE",
    f6_ylabel="Part mondiale ou score CACI (pct)",
    f6_source="Sources : Epoch AI, AIE, dashboard avril 2026, estimations auteur",
    f7_title="Trajectoire compute US vs UE 2020-2025 (echelle log)",
    f7_subtitle="Capacite cumulee en H100-equivalents (milliers), clusters operationnels",
    f7_ylabel="H100-equivalents cumules (milliers, log10)",
    f7_us="Etats-Unis", f7_cn="Chine", f7_eu="UE(13)",
    f7_bis_label="Choc BIS\noct. 2022",
    f7_section232_label="Section 232\njanv. 2026",
    f7_source="Sources : Epoch AI GPU Clusters dataset (avril 2026), agregation par First Operational Date",
)

EN = LangPack(
    code="en", suffix="EN",
    f1_title="Data center electricity consumption by region (2020-2030, TWh)",
    f1_ylabel="TWh / year",
    f1_us="United States", f1_cn="China", f1_eu="EU", f1_rest="Rest of world",
    f1_source="Source: IEA Energy and AI (2025), Chapter Table 4",
    f1_proj="Projection",
    f2_title="Global semiconductor sales 2020-2026 (billion USD, SIA/WSTS)",
    f2_ylabel="Billion USD",
    f2_logic="Logic chips (GPU, CPU, ASIC)",
    f2_memory="Memory (DRAM, NAND)",
    f2_other="Other (analog, discrete, sensors)",
    f2_source="Sources: SIA/WSTS (February 2026), Chapter Table 5",
    f2_growth="Annual growth",
    f3_title="Geographic distribution of GPU cluster performance (2019-2025)",
    f3_ylabel="Share of global performance (pct)",
    f3_us="United States", f3_cn="China", f3_eu="EU", f3_rest="Rest of world",
    f3_source="Sources: Epoch AI / Pilz et al. (2025), April 2026 dashboard snapshot",
    f3_note=f"US/EU ratio ~ {US_EU_H100_RATIO}:1 on operational compute (April 2026)",
    f4_title="Timeline of US semiconductor and AI measures (2022-2026): from export controls to tariff protectionism",
    f4_events=[
        ("Oct.\n2022", "BIS Export Controls\nAdvanced GPUs, SME\nTarget: China", "Biden"),
        ("Oct.\n2023", "Threshold update\n+40 countries, A800/H800\ncaptured", "Biden"),
        ("Dec.\n2024", "Wave 3: 24 SME types\nHBM, 140 entities", "Biden"),
        ("Jan.\n2025", "AI Diffusion Rule\nModels + cloud\n120 countries, 3 tiers", "Biden"),
        ("Jul.\n2025", "America AI\nAction Plan\nUS deregulation", "Trump"),
        ("Jan.\n2026", "Section 232\n25 pct GPU tariff\nUS domestic exemption", "Trump"),
    ],
    f4_source="Sources: BIS, White House, Pillsbury Law (2026), Gibson Dunn (2026)",
    f4_phase_d="Denial strategy\n(access denial)",
    f4_phase_c="Capture strategy\n(offensive protectionism)",
    f5_title="CACI calibration: decomposition of US advantage (April 2026)",
    f5_components=["Installed compute\n(F ratio)", "Energy cost\n(E ratio, PPA)", "Resulting CACI\n(Power Mode)"],
    f5_values_label=[f"x{US_EU_H100_RATIO}", f"x{PPA_RATIO_EU_US}", f"{CACI_POWER_RATIO_US_EU}:1"],
    f5_ylabel="US/EU ratio",
    f5_source="Author's elaboration - Section 3.3.3, Epoch AI / April 2026 dashboard data",
    f6_title="Summary: US dominance indicators in AI compute (April 2026 snapshot)",
    f6_indicators=["GPU cluster\nperformance\n(operational)", "F_total\n(op + planned)",
                   "Private sector\nAI compute", "Data center\nconsumption",
                   "AI investment\n2025", "CACI\nPower Mode"],
    f6_us_vals=[76.9, 49.9, 65, 45, 85, 100],
    f6_eu_vals=[4.4, 3.3, 3, 15, 5, 28.9],
    f6_cn_vals=[12.8, 0.5, 12, 25, 8, 15.7],
    f6_us_label="United States", f6_cn_label="China", f6_eu_label="EU",
    f6_ylabel="Global share or CACI score (pct)",
    f6_source="Sources: Epoch AI, IEA, April 2026 dashboard, author estimates",
    f7_title="US vs EU compute trajectory 2020-2025 (log scale)",
    f7_subtitle="Cumulative capacity in H100-equivalents (thousands), operational clusters",
    f7_ylabel="Cumulative H100-equivalents (thousands, log10)",
    f7_us="United States", f7_cn="China", f7_eu="EU(13)",
    f7_bis_label="BIS shock\nOct. 2022",
    f7_section232_label="Section 232\nJan. 2026",
    f7_source="Sources: Epoch AI GPU Clusters dataset (April 2026), aggregation by First Operational Date",
)

PT = LangPack(
    code="pt-br", suffix="PT-BR",
    f1_title="Consumo eletrico dos data centers por regiao (2020-2030, TWh)",
    f1_ylabel="TWh / ano",
    f1_us="Estados Unidos", f1_cn="China", f1_eu="UE", f1_rest="Resto do mundo",
    f1_source="Fonte: IEA Energy and AI (2025), Tabela 4 do capitulo",
    f1_proj="Projecao",
    f2_title="Vendas globais de semicondutores 2020-2026 (bilhoes USD, SIA/WSTS)",
    f2_ylabel="Bilhoes USD",
    f2_logic="Chips logicos (GPU, CPU, ASIC)",
    f2_memory="Memoria (DRAM, NAND)",
    f2_other="Outros (analogico, discreto, sensores)",
    f2_source="Fontes: SIA/WSTS (fevereiro de 2026), Tabela 5 do capitulo",
    f2_growth="Crescimento anual",
    f3_title="Distribuicao geografica do desempenho dos clusters GPU (2019-2025)",
    f3_ylabel="Parcela do desempenho global (pct)",
    f3_us="Estados Unidos", f3_cn="China", f3_eu="UE", f3_rest="Resto do mundo",
    f3_source="Fontes: Epoch AI / Pilz et al. (2025), snapshot painel abril de 2026",
    f3_note=f"Razao EUA/UE ~ {US_EU_H100_RATIO}:1 no compute operacional (abril de 2026)",
    f4_title="Cronologia das medidas dos EUA sobre semicondutores e IA (2022-2026): do controle de exportacao ao protecionismo tarifario",
    f4_events=[
        ("Out.\n2022", "Controles export BIS\nGPUs avancados, SME\nAlvo: China", "Biden"),
        ("Out.\n2023", "Atualizacao de limites\n+40 paises, A800/H800\ncapturados", "Biden"),
        ("Dez.\n2024", "Onda 3: 24 tipos SME\nHBM, 140 entidades", "Biden"),
        ("Jan.\n2025", "AI Diffusion Rule\nModelos + nuvem\n120 paises, 3 niveis", "Biden"),
        ("Jul.\n2025", "America AI\nAction Plan\nDesregulacao EUA", "Trump"),
        ("Jan.\n2026", "Secao 232\nTarifa 25 pct GPUs\nIsencao domestica EUA", "Trump"),
    ],
    f4_source="Fontes: BIS, Casa Branca, Pillsbury Law (2026), Gibson Dunn (2026)",
    f4_phase_d="Estrategia de denial\n(negacao de acesso)",
    f4_phase_c="Estrategia de capture\n(protecionismo ofensivo)",
    f5_title="Calibracao CACI: decomposicao da vantagem dos EUA (abril de 2026)",
    f5_components=["Compute instalado\n(razao F)", "Custo de energia\n(razao E, PPA)", "CACI resultante\n(Power Mode)"],
    f5_values_label=[f"x{US_EU_H100_RATIO}", f"x{PPA_RATIO_EU_US}", f"{CACI_POWER_RATIO_US_EU}:1"],
    f5_ylabel="Razao EUA/UE",
    f5_source="Elaboracao do autor - Secao 3.3.3, dados Epoch AI / painel abril de 2026",
    f6_title="Sintese: indicadores de dominancia dos EUA em compute IA (snapshot abril de 2026)",
    f6_indicators=["Desempenho\nclusters GPU\n(operacional)", "F_total\n(op + planejado)",
                   "Setor privado\ncompute IA", "Consumo\ndata centers",
                   "Investimento\nIA 2025", "CACI\nPower Mode"],
    f6_us_vals=[76.9, 49.9, 65, 45, 85, 100],
    f6_eu_vals=[4.4, 3.3, 3, 15, 5, 28.9],
    f6_cn_vals=[12.8, 0.5, 12, 25, 8, 15.7],
    f6_us_label="Estados Unidos", f6_cn_label="China", f6_eu_label="UE",
    f6_ylabel="Parcela global ou score CACI (pct)",
    f6_source="Fontes: Epoch AI, IEA, painel abril de 2026, estimativas do autor",
    f7_title="Trajetoria de compute EUA vs UE 2020-2025 (escala log)",
    f7_subtitle="Capacidade cumulativa em H100-equivalentes (milhares), clusters operacionais",
    f7_ylabel="H100-equivalentes cumulativos (milhares, log10)",
    f7_us="Estados Unidos", f7_cn="China", f7_eu="UE(13)",
    f7_bis_label="Choque BIS\nout. 2022",
    f7_section232_label="Secao 232\njan. 2026",
    f7_source="Fontes: Epoch AI GPU Clusters dataset (abril de 2026), agregacao por First Operational Date",
)

LANGS: list[LangPack] = [FR, EN, PT]


# ===========================================================================
# Figure 3.1 - Data center electricity consumption stacked area
# ===========================================================================

def fig1_energy_by_region(L: LangPack) -> Path:
    """Render the data center electricity consumption stacked area."""
    years = [2020, 2022, 2024, 2026, 2028, 2030]
    us = [120, 150, 180, 260, 340, 420]
    cn = [60, 80, 102, 150, 210, 280]
    eu = [45, 55, 70, 85, 100, 115]
    rest = [45, 55, 63, 80, 100, 130]

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.stackplot(years, us, cn, eu, rest,
                 labels=[L.f1_us, L.f1_cn, L.f1_eu, L.f1_rest],
                 colors=[US_COLOR, CN_COLOR, EU_COLOR, ACCENT1],
                 alpha=0.85)

    ax.axvline(x=2024.5, color=GREY, linestyle="--", linewidth=1.5, alpha=0.7)
    ax.text(2025, 990, L.f1_proj, fontsize=10,
            color=GREY, style="italic", ha="left")

    ax.set_title(L.f1_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_xlabel("")
    ax.set_ylabel(L.f1_ylabel, fontsize=11)
    ax.set_xlim(2020, 2030)
    ax.set_ylim(0, 1100)
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f1_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_3.1_Energy_By_Region", L.suffix)


# ===========================================================================
# Figure 3.2 - Semiconductor sales segmented stacked bars + growth line
# ===========================================================================

def fig2_semi_sales(L: LangPack) -> Path:
    """Render the segmented semiconductor sales bars."""
    years = ["2020", "2022", "2023", "2024", "2025", "2026 proj."]
    logic = [165, 215, 200, 245, 302, 380]
    memory = [120, 165, 100, 175, 223, 280]
    other = [155, 176, 227, 211, 267, 330]
    growth = [6.8, 3.3, -8.2, 19.1, 25.6, 24.0]

    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(years))
    w = 0.6

    p1 = ax.bar(x, logic, w, color=US_COLOR, alpha=0.9,
                label=L.f2_logic, edgecolor="white", linewidth=1)
    p2 = ax.bar(x, memory, w, bottom=logic, color=ACCENT3, alpha=0.9,
                label=L.f2_memory, edgecolor="white", linewidth=1)
    p3 = ax.bar(x, other, w,
                bottom=[a + b for a, b in zip(logic, memory)],
                color=ACCENT1, alpha=0.85,
                label=L.f2_other, edgecolor="white", linewidth=1)

    totals = [a + b + c for a, b, c in zip(logic, memory, other)]
    for i, t in enumerate(totals):
        ax.text(i, t + 12, f"{t}", ha="center", fontsize=10,
                fontweight="bold", color=NAVY)

    ax2 = ax.twinx()
    ax2.plot(x, growth, color=CN_COLOR, marker="o", markersize=8,
             linewidth=2.2, label=L.f2_growth)
    for i, g in enumerate(growth):
        sign = "+" if g >= 0 else ""
        ax2.annotate(f"{sign}{g} pct",
                     xy=(i, g), xytext=(0, 14), textcoords="offset points",
                     ha="center", fontsize=9, color=CN_COLOR, fontweight="bold")
    ax2.set_ylabel(L.f2_growth + " (pct)", color=CN_COLOR, fontsize=11)
    ax2.tick_params(axis="y", labelcolor=CN_COLOR)
    ax2.set_ylim(-15, 50)
    ax2.spines["right"].set_visible(True)
    ax2.spines["top"].set_visible(False)

    ax.set_title(L.f2_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=10)
    ax.set_ylabel(L.f2_ylabel, fontsize=11)
    ax.set_ylim(0, 1100)
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f2_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_3.2_Semiconductor_Sales_Segmented", L.suffix)


# ===========================================================================
# Figure 3.3 - GPU cluster performance distribution stacked bars
# ===========================================================================

def fig3_gpu_distribution(L: LangPack) -> Path:
    """Render the GPU cluster performance distribution by region."""
    years = ["2019", "2021", "2023", "2025", "April 2026"]
    us = [55, 60, 68, 74.5, 76.9]
    cn = [22, 18, 16, 14.1, 12.8]
    eu = [10, 8, 6, 4.8, 4.4]
    rest = [13, 14, 10, 6.6, 5.9]

    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(years))
    w = 0.62

    p1 = ax.bar(x, us, w, color=US_COLOR, alpha=0.9,
                label=L.f3_us, edgecolor="white", linewidth=1)
    p2 = ax.bar(x, cn, w, bottom=us, color=CN_COLOR, alpha=0.9,
                label=L.f3_cn, edgecolor="white", linewidth=1)
    p3 = ax.bar(x, eu, w, bottom=[a + b for a, b in zip(us, cn)],
                color=EU_COLOR, alpha=0.9,
                label=L.f3_eu, edgecolor="white", linewidth=1)
    p4 = ax.bar(x, rest, w,
                bottom=[a + b + c for a, b, c in zip(us, cn, eu)],
                color=ACCENT1, alpha=0.85,
                label=L.f3_rest, edgecolor="white", linewidth=1)

    for i in range(len(years)):
        ax.text(i, us[i] / 2, f"{us[i]:.1f} pct",
                ha="center", va="center", fontsize=10,
                fontweight="bold", color="white")

    ax.set_title(L.f3_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=10)
    ax.set_ylabel(L.f3_ylabel, fontsize=11)
    ax.set_ylim(0, 105)
    ax.legend(loc="upper right", frameon=False, fontsize=10,
              bbox_to_anchor=(1, 0.95))

    ax.text(0.02, 0.97, L.f3_note, transform=ax.transAxes,
            fontsize=10, color=GOLD, fontweight="bold", fontstyle="italic",
            verticalalignment="top",
            bbox=dict(boxstyle="round,pad=0.4",
                      facecolor=GOLD, alpha=0.18, edgecolor=GOLD))

    fig.text(0.5, 0.005, L.f3_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_3.3_GPU_Cluster_Distribution", L.suffix)


# ===========================================================================
# Figure 3.4 - US regulatory measures timeline
# ===========================================================================

def fig4_regulatory_timeline(L: LangPack) -> Path:
    """Render the regulatory timeline with denial vs capture phases."""
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(7, 8.4, L.f4_title, ha="center",
            fontsize=13, fontweight="bold", color=NAVY)

    # Timeline arrow
    ax.annotate("", xy=(13.5, 4.0), xytext=(0.5, 4.0),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=NAVY))

    event_x = [1.5, 3.7, 5.9, 8.1, 10.3, 12.5]
    event_top = [True, False, True, False, True, False]
    admin_color = {"Biden": ACCENT2, "Trump": ACCENT3}

    for ex, top, (date, label, admin) in zip(event_x, event_top, L.f4_events):
        col = admin_color[admin]
        bbox_y = 5.0 if top else 1.6
        # Box
        rect = mpatches.FancyBboxPatch(
            (ex - 1.0, bbox_y), 2.0, 1.6,
            boxstyle="round,pad=0.1",
            facecolor=col, alpha=0.1, edgecolor=col, linewidth=1.8,
        )
        ax.add_patch(rect)
        ax.text(ex, bbox_y + 1.35, date, ha="center", fontsize=10,
                fontweight="bold", color=col)
        ax.text(ex, bbox_y + 0.55, label, ha="center", va="center",
                fontsize=8.5, color="#333", linespacing=1.3)
        # Connector line + dot
        line_y_top = bbox_y if top else bbox_y + 1.6
        line_y_bot = 4.0
        ax.plot([ex, ex], [line_y_top, line_y_bot],
                color=col, linewidth=1.5, linestyle=":")
        ax.plot(ex, 4.0, "o", color=col, markersize=10)

    # Phase bands
    band_d = mpatches.FancyBboxPatch(
        (0.3, 7.3), 9.5, 0.6, boxstyle="round,pad=0.05",
        facecolor=ACCENT2, alpha=0.16, edgecolor=ACCENT2, linewidth=1,
    )
    ax.add_patch(band_d)
    ax.text(5.0, 7.6, L.f4_phase_d, ha="center", va="center",
            fontsize=10, fontweight="bold", color=ACCENT2)

    band_c = mpatches.FancyBboxPatch(
        (10.0, 7.3), 3.5, 0.6, boxstyle="round,pad=0.05",
        facecolor=ACCENT3, alpha=0.16, edgecolor=ACCENT3, linewidth=1,
    )
    ax.add_patch(band_c)
    ax.text(11.7, 7.6, L.f4_phase_c, ha="center", va="center",
            fontsize=10, fontweight="bold", color=ACCENT3)

    ax.text(7, 0.3, L.f4_source, ha="center",
            fontsize=8, color="gray", fontstyle="italic")

    return save_fig(fig, "Fig_3.4_Regulatory_Timeline", L.suffix)


# ===========================================================================
# Figure 3.5 - CACI calibration (refreshed values)
# ===========================================================================

def fig5_caci_calibration(L: LangPack) -> Path:
    """Render the CACI calibration bar chart with the live April 2026 values."""
    fig, ax = plt.subplots(figsize=(11, 7))

    components = L.f5_components
    vals = [US_EU_H100_RATIO, PPA_RATIO_EU_US, CACI_POWER_RATIO_US_EU]
    colors = [US_COLOR, ACCENT3, GOLD]

    bars = ax.bar(components, vals, width=0.5, color=colors, alpha=0.9,
                  edgecolor="white", linewidth=2)

    for bar, val, label in zip(bars, vals, L.f5_values_label):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.6, label,
                ha="center", fontsize=14, fontweight="bold",
                color=bar.get_facecolor())

    # Operator annotation (visual cue: geometric weighting bridges F and CACI)
    ax.text(0.5, 0.92, "geometric weighting", transform=ax.transAxes,
            fontsize=9, color=GREY, ha="center", fontstyle="italic")
    ax.annotate("", xy=(0.84, 0.40), xytext=(0.18, 0.85),
                xycoords="axes fraction",
                arrowprops=dict(arrowstyle="->", lw=1.5,
                                color=GREY, linestyle=":"))

    ax.set_title(L.f5_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_ylabel(L.f5_ylabel, fontsize=11)
    ax.set_ylim(0, 22)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f5_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_3.5_CACI_Calibration", L.suffix)


# ===========================================================================
# Figure 3.6 - US dominance synthesis
# ===========================================================================

def fig6_dominance_synthesis(L: LangPack) -> Path:
    """Render the grouped bar chart of US dominance indicators."""
    fig, ax = plt.subplots(figsize=(14, 7))

    indicators = L.f6_indicators
    x = np.arange(len(indicators))
    w = 0.27

    bars_us = ax.bar(x - w, L.f6_us_vals, w, color=US_COLOR,
                     label=L.f6_us_label, edgecolor="white", linewidth=1.5)
    bars_cn = ax.bar(x, L.f6_cn_vals, w, color=CN_COLOR,
                     label=L.f6_cn_label, edgecolor="white", linewidth=1.5)
    bars_eu = ax.bar(x + w, L.f6_eu_vals, w, color=EU_COLOR,
                     label=L.f6_eu_label, edgecolor="white", linewidth=1.5)

    for bars, col in [(bars_us, US_COLOR), (bars_cn, CN_COLOR), (bars_eu, EU_COLOR)]:
        for bar in bars:
            h = bar.get_height()
            label = f"{h:.1f}" if h < 100 else f"{int(h)}"
            ax.text(bar.get_x() + bar.get_width() / 2, h + 1.5, label,
                    ha="center", fontsize=9, fontweight="bold", color=col)

    ax.axhline(y=50, color="#CCC", linewidth=1, linestyle=":", alpha=0.7)
    ax.text(len(indicators) - 0.4, 51, "50",
            fontsize=8, color="#999")

    ax.set_title(L.f6_title, fontsize=13, fontweight="bold",
                 color=NAVY, pad=14)
    ax.set_ylabel(L.f6_ylabel, fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(indicators, fontsize=9)
    ax.set_ylim(0, 115)
    ax.legend(fontsize=11, framealpha=0.9, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f6_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_3.6_US_Dominance_Synthesis", L.suffix)


# ===========================================================================
# Figure 3.7 - US vs EU compute trajectory 2020-2025 (NEW)
# ===========================================================================

def fig7_compute_trajectory(L: LangPack) -> Path:
    """Render the cumulative US vs EU compute trajectory on log scale."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    ax.plot(TRAJ_YEARS, US_TRAJ_H100K, color=US_COLOR,
            marker="o", markersize=9, linewidth=3, label=L.f7_us)
    ax.plot(TRAJ_YEARS, CN_TRAJ_H100K, color=CN_COLOR,
            marker="s", markersize=8, linewidth=2.5, label=L.f7_cn)
    ax.plot(TRAJ_YEARS, EU_TRAJ_H100K, color=EU_COLOR,
            marker="^", markersize=8, linewidth=2.5, label=L.f7_eu)

    # Endpoint annotations
    for x, y, col in [
        (TRAJ_YEARS[-1], US_TRAJ_H100K[-1], US_COLOR),
        (TRAJ_YEARS[-1], CN_TRAJ_H100K[-1], CN_COLOR),
        (TRAJ_YEARS[-1], EU_TRAJ_H100K[-1], EU_COLOR),
    ]:
        ax.annotate(f"{int(y)}k",
                    xy=(x, y), xytext=(8, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=10,
                    fontweight="bold", color=col)

    # BIS shock vertical line
    ax.axvline(x=2022.75, color=ACCENT3, linestyle="--",
               linewidth=1.5, alpha=0.85)
    ax.text(2022.83, 1100, L.f7_bis_label, fontsize=9,
            color=ACCENT3, fontweight="bold", style="italic", va="top")

    # Section 232 vertical line (early 2026 - placed at the right edge)
    ax.axvline(x=2025.95, color=ACCENT2, linestyle="--",
               linewidth=1.5, alpha=0.85)
    ax.text(2025.93, 1100, L.f7_section232_label, fontsize=9,
            color=ACCENT2, fontweight="bold", style="italic",
            va="top", ha="right")

    ax.set_yscale("log")
    ax.set_title(f"{L.f7_title}\n{L.f7_subtitle}",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.set_ylabel(L.f7_ylabel, fontsize=11)
    ax.set_xticks(TRAJ_YEARS)
    ax.set_ylim(8, 2200)
    ax.legend(loc="upper left", frameon=False, fontsize=11)
    ax.grid(True, which="both", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, L.f7_source, ha="center",
             fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_3.7_Compute_Trajectory", L.suffix)


# ===========================================================================
# Main
# ===========================================================================

FIGURES = [
    fig1_energy_by_region,
    fig2_semi_sales,
    fig3_gpu_distribution,
    fig4_regulatory_timeline,
    fig5_caci_calibration,
    fig6_dominance_synthesis,
    fig7_compute_trajectory,
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
