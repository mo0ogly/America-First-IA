"""
Chapitre VI - Generateur de graphiques FR.

Genere les figures pour les 4 sous-chapitres :

    6.X    France/Europe
    6bis.X Amerique du Sud / Bresil
    6ter.X Asie
    6quat.X Afrique

Toutes les valeurs sont alignees sur le snapshot du tableau de bord
d'avril 2026 (US 76,9 pct operationnel, ratio brut US/UE 17,6:1, CACI
Power Mode 3,46:1, energie 1,59x apres PPA).

Output : ./figures_ch6/Fig_X.Y_NAME_FR.png (300 DPI)

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
import os
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
log = logging.getLogger("chapitre6_graphs")


OUTPUT_DIR = Path(os.environ.get("CH6_FIG_DIR", "./figures_ch6")).resolve()
DPI = 300


# Visual identity
NAVY = "#1A2744"
GOLD = "#B8922F"
US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
CN_COLOR = "#C0392B"
ACCENT1 = "#148F77"
ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"
ACCENT4 = "#2C3E50"
GREY = "#999999"
BG_COLOR = "white"


def _common_style() -> None:
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


def save_fig(fig, basename: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / f"{basename}_FR.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    log.info("Saved %s", out)
    return out


# ===========================================================================
# Fig 6.1 - France/Europe sectoral exposure
# ===========================================================================

def fig_6_1_sectoral_exposure() -> Path:
    """Sectoral exposure radar / bar chart for the 5 French sectors."""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    sectors = ["Finance", "Auto/Aero", "Sante/Pharma", "Robotique/Indus.", "Defense/Spatial"]
    # Synthetic exposure score 0-100 = (intensite_compute*0.4 + sensibilite_data*0.3 + dep_cloud_US*0.3)
    intensity = [85, 95, 70, 80, 95]
    data_sens = [95, 80, 100, 60, 100]
    cloud_dep = [75, 65, 50, 58, 50]

    x = np.arange(len(sectors))
    w = 0.27

    bars1 = ax.bar(x - w, intensity, w, label="Intensite compute",
                    color=US_COLOR, alpha=0.85, edgecolor=US_COLOR, linewidth=1.3)
    bars2 = ax.bar(x, data_sens, w, label="Sensibilite donnees",
                    color=GOLD, alpha=0.85, edgecolor=GOLD, linewidth=1.3)
    bars3 = ax.bar(x + w, cloud_dep, w, label="Dependance cloud US (pct)",
                    color=CN_COLOR, alpha=0.85, edgecolor=CN_COLOR, linewidth=1.3)

    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                    f"{int(bar.get_height())}", ha="center", fontsize=9,
                    fontweight="bold", color=bar.get_facecolor())

    ax.set_xticks(x)
    ax.set_xticklabels(sectors, fontsize=10)
    ax.set_ylabel("Score d'exposition (0-100)", fontsize=11)
    ax.set_ylim(0, 115)
    ax.set_title("Exposition sectorielle francaise a l'asymetrie de compute IA\n(scenario B = pire cas)",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005,
             "Source : construction de l'auteur - Section 6.1, Tableau 14",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_6.1_Sectoral_Exposure_France")


# ===========================================================================
# Fig 6.2 - France 3 configurations 2030
# ===========================================================================

def fig_6_2_three_configurations() -> Path:
    """3 configurations possibles France 2030 : dependante / hub / pilier."""
    fig, ax = plt.subplots(figsize=(13, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(6, 7.5, "La France face a trois futurs (2030)",
            ha="center", fontsize=15, fontweight="bold", color=NAVY)

    configs = [
        (0.4, "Configuration 1\nConsommatrice dependante",
         "Scenarios A et B\n\nCACI ratio : 4-8:1\nCloud US : 75-82 pct\nProductivite UE : +0,3 a +1,5 pct/an\nBrain drain : accelere\nEcart PIB : -5 a -15 pts sur 5 ans",
         CN_COLOR),
        (4.4, "Configuration 2\nHub energetique et applicatif",
         "Scenario C\n\nCACI ratio : 2,0-2,5:1\nCloud US : 60-65 pct\nProductivite UE : +1,8 a +2,5 pct/an\nMistral Compute + Gigafactories\nFrance hub nucleaire EU",
         ACCENT1),
        (8.4, "Configuration 3\nPilier souverainete UE",
         "Scenario D\n\nCACI ratio : 4-7:1 (post-creux)\nCloud US : 50-55 pct\nProductivite UE : +1,2 a +2,0 pct/an\n20 GW nucleaire dedie\nDARE/RISC-V + alliances JP/KR/TW",
         ACCENT2),
    ]
    box_w, box_h = 3.4, 5.5
    for x, title, body, col in configs:
        rect = mpatches.FancyBboxPatch(
            (x, 0.8), box_w, box_h,
            boxstyle="round,pad=0.15",
            facecolor=col, alpha=0.12, edgecolor=col, linewidth=2.5,
        )
        ax.add_patch(rect)
        cx = x + box_w / 2
        ax.text(cx, 5.6, title, ha="center", fontsize=12,
                fontweight="bold", color=col, linespacing=1.3)
        ax.text(cx, 3.2, body, ha="center", fontsize=9.5,
                color="#333", linespacing=1.5)

    ax.text(6, 0.2, "Source : construction de l'auteur - Section 6.5, calibration sur Chap V",
            ha="center", fontsize=8, color="gray", fontstyle="italic")
    return save_fig(fig, "Fig_6.2_Three_Configurations_France")


# ===========================================================================
# Fig 6bis.1 - Brazil scenarios A'/B'/C'/D'
# ===========================================================================

def fig_6bis_1_brazil_scenarios() -> Path:
    """4 Brazil scenarios with probabilities (donut)."""
    fig, ax = plt.subplots(figsize=(10, 8))

    sizes = [40, 17, 22, 12]  # midpoints of the probability ranges
    other = 100 - sum(sizes)
    sizes.append(other)
    labels = ["A' Hub neutre dual\n35-45 pct",
              "B' Sanctions sec.\n15-20 pct",
              "C' Alignement pro-US\n20-25 pct",
              "D' Souverainete LATAM\n10-15 pct",
              "Trajectoires hybrides\n~9 pct"]
    colors = ["#3498DB", "#E74C3C", "#27AE60", "#8E44AD", GREY]
    explode = [0.04, 0.04, 0.04, 0.04, 0]

    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, colors=colors, autopct="%1.0f pct",
        explode=explode, startangle=90,
        wedgeprops=dict(width=0.5, edgecolor="white", linewidth=2),
        textprops={"fontsize": 10},
    )
    for txt in autotexts:
        txt.set_color("white")
        txt.set_fontweight("bold")
        txt.set_fontsize(11)

    ax.text(0, 0, "BRESIL\n2026-2030",
            ha="center", va="center", fontsize=14,
            fontweight="bold", color=NAVY)

    ax.set_title("Probabilites des scenarios specifiques pour le Bresil\nface au protectionnisme IA US",
                 fontsize=13, fontweight="bold", color=NAVY, pad=20)
    fig.text(0.5, 0.02,
             "Source : construction de l'auteur - Section 6bis.4, Tableau 17",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout()
    return save_fig(fig, "Fig_6bis.1_Brazil_Scenarios")


# ===========================================================================
# Fig 6bis.2 - LATAM compute deficit vs US
# ===========================================================================

def fig_6bis_2_latam_deficit() -> Path:
    """Bar chart: PIB share vs AI investment share, LATAM vs US."""
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ["Population\nmondiale (pct)", "PIB\nmondial (pct)",
                  "Invest. IA\nmondial (pct)", "Cap. DC IA\nmondiale (pct)"]
    latam = [8.4, 6.6, 1.12, 1.5]
    us = [4.2, 25.5, 65, 76.9]  # 76.9 = US share AI compute operational

    x = np.arange(len(categories))
    w = 0.35

    b1 = ax.bar(x - w / 2, latam, w, color=ACCENT3, alpha=0.85,
                 label="Amerique latine", edgecolor=ACCENT3, linewidth=1.3)
    b2 = ax.bar(x + w / 2, us, w, color=US_COLOR, alpha=0.85,
                 label="Etats-Unis", edgecolor=US_COLOR, linewidth=1.3)

    for bar in b1:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                f"{bar.get_height():.1f} pct", ha="center",
                fontsize=10, fontweight="bold", color=ACCENT3)
    for bar in b2:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                f"{bar.get_height():.1f} pct", ha="center",
                fontsize=10, fontweight="bold", color=US_COLOR)

    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_ylabel("Part mondiale (pct)", fontsize=11)
    ax.set_ylim(0, 92)
    ax.set_title("Le deficit d'investissement IA en Amerique latine\n(le ratio PIB/Invest. IA = 5,9)",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper left")
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005,
             "Source : ILIA 2025 (CEPALC/CENIA) ; Banque mondiale (novembre 2025) ; tableau de bord public (avril 2026)",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_6bis.2_LATAM_Deficit")


# ===========================================================================
# Fig 6ter.1 - Asia Tier classification map
# ===========================================================================

def fig_6ter_1_asia_tiers() -> Path:
    """Asia Tier classification with capacity and investment data."""
    fig, ax = plt.subplots(figsize=(13, 7))

    countries = ["Japon", "Taiwan", "Coree", "Inde", "Chine", "ASEAN", "Golfe (EAU)"]
    tiers = [1, 1, 1, 2, 3, 2, 2]
    dc_capacity = [12.8, 3.0, 5.0, 1.4, 19.6, 3.0, 2.0]  # GW
    investment = [135, 40, 6.7, 200, 125, 15, 20]  # Md USD

    # Color by tier
    tier_colors = {1: ACCENT1, 2: ACCENT3, 3: CN_COLOR}
    colors = [tier_colors[t] for t in tiers]

    x = np.arange(len(countries))
    bars = ax.bar(x, dc_capacity, color=colors, alpha=0.85,
                   edgecolor="white", linewidth=1.5)

    # Annotate each bar with Tier + investment
    for i, (bar, tier, inv, cap) in enumerate(zip(bars, tiers, investment, dc_capacity)):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.4,
                f"Tier {tier}\n{inv} Md USD",
                ha="center", fontsize=9, fontweight="bold",
                color=bar.get_facecolor())
        # Capacity inside bar
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2,
                f"{cap} GW",
                ha="center", va="center", fontsize=11,
                fontweight="bold", color="white")

    ax.set_xticks(x)
    ax.set_xticklabels(countries, fontsize=10)
    ax.set_ylabel("Capacite DC installee (GW)", fontsize=11)
    ax.set_ylim(0, 25)
    ax.set_title("Position asiatique face au protectionnisme IA US\n(Tier 1 = vert, Tier 2 = orange, Tier 3 = rouge)",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    legend_elements = [
        mpatches.Patch(color=ACCENT1, label="Tier 1 - acces illimite"),
        mpatches.Patch(color=ACCENT3, label="Tier 2 - caps quantitatifs"),
        mpatches.Patch(color=CN_COLOR, label="Tier 3 - acces interdit"),
    ]
    ax.legend(handles=legend_elements, fontsize=10, loc="upper left", framealpha=0.9)

    fig.text(0.5, 0.005,
             "Source : Tableau 18 ; calibration sur baseline avril 2026 et BIS Framework for AI Diffusion (janvier 2025)",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_6ter.1_Asia_Tiers")


# ===========================================================================
# Fig 6ter.2 - China autonomization paradox
# ===========================================================================

def fig_6ter_2_china_paradox() -> Path:
    """China investment trajectory under US restrictions."""
    fig, ax = plt.subplots(figsize=(11, 6))

    years = [2022, 2023, 2024, 2025, 2026]
    cn_invest = [40, 60, 90, 125, 195]  # Md USD AI infrastructure
    cn_efflops = [120, 160, 220, 280, 340]  # EFLOP/s capacity

    ax_left = ax
    ax_right = ax_left.twinx()

    line1 = ax_left.plot(years, cn_invest, color=CN_COLOR, linewidth=3,
                         marker="o", markersize=10,
                         label="Investissement IA Chine (Md USD)")
    line2 = ax_right.plot(years, cn_efflops, color=US_COLOR, linewidth=3,
                          marker="s", markersize=10, linestyle="--",
                          label="Capacite IA Chine (EFLOP/s)")

    # Restriction events
    ax_left.axvline(x=2022.8, color=GREY, linestyle=":", alpha=0.6)
    ax_left.text(2022.85, 175, "Octobre 2022\nBIS H100/A100\ninterdites Tier 3",
                 fontsize=8.5, color=GREY, fontstyle="italic")

    for x, y, label in zip(years, cn_invest, cn_invest):
        ax_left.text(x, y + 8, f"{label}", ha="center",
                     fontsize=9, fontweight="bold", color=CN_COLOR)

    ax_left.set_xlabel("Annee", fontsize=11)
    ax_left.set_ylabel("Investissement IA (Md USD)", fontsize=11, color=CN_COLOR)
    ax_right.set_ylabel("Capacite IA (EFLOP/s)", fontsize=11, color=US_COLOR)
    ax_left.set_ylim(0, 220)
    ax_right.set_ylim(0, 380)
    ax_left.set_xticks(years)
    ax_left.tick_params(axis="y", labelcolor=CN_COLOR)
    ax_right.tick_params(axis="y", labelcolor=US_COLOR)

    ax_left.set_title("Le paradoxe strategique : les restrictions US accelerent l'autonomisation chinoise",
                      fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax_left.grid(True, linestyle=":", alpha=0.4)

    lines = line1 + line2
    labels_l = [l.get_label() for l in lines]
    ax_left.legend(lines, labels_l, fontsize=10, loc="upper left",
                   framealpha=0.9)

    fig.text(0.5, 0.005,
             "Source : IBTimes India (fevrier 2026) ; ITIF (mai 2025) ; EastPost (fevrier 2026). Capacite 2026 projetee selon objectif officiel.",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_6ter.2_China_Paradox")


# ===========================================================================
# Fig 6quat.1 - Africa compute deficit
# ===========================================================================

def fig_6quat_1_africa_deficit() -> Path:
    """Africa vs US compute deficit (log scale)."""
    fig, ax = plt.subplots(figsize=(11, 6))

    metrics = ["Capacite DC\n(GW)", "Invest. DC\n(Md USD)", "GPU IA\n(milliers)",
               "Talent IA\n(pct mondial)", "Marche IA\n(Md USD)"]
    africa = [1.0, 2.0, 12.0, 3.0, 4.5]
    us = [53.7, 675.0, 5000.0, 40.0, 200.0]
    ratios = [54, 338, 417, 13, 44]

    x = np.arange(len(metrics))
    w = 0.35

    ax.bar(x - w / 2, africa, w, color=ACCENT3, alpha=0.85,
            label="Afrique", edgecolor=ACCENT3, linewidth=1.3)
    ax.bar(x + w / 2, us, w, color=US_COLOR, alpha=0.85,
            label="Etats-Unis", edgecolor=US_COLOR, linewidth=1.3)

    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=10)
    ax.set_ylabel("Echelle log (unite variable)", fontsize=11)
    ax.set_title("Le deficit compute africain : asymetrie x44-x417 selon les indicateurs",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)

    # Ratio labels
    for i, ratio in enumerate(ratios):
        ax.text(i, us[i] * 1.5, f"x{ratio}", ha="center",
                fontsize=11, fontweight="bold", color=CN_COLOR,
                bbox=dict(boxstyle="round,pad=0.25",
                          facecolor="#FFF3E0",
                          edgecolor=CN_COLOR, alpha=0.85))

    ax.legend(fontsize=10, framealpha=0.9, loc="upper left")
    ax.grid(axis="y", linestyle=":", alpha=0.4, which="both")

    fig.text(0.5, 0.005,
             "Source : Tableau 22 (Synthese CACI Afrique) ; baseline US sur snapshot avril 2026",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_6quat.1_Africa_Deficit")


# ===========================================================================
# Fig 6quat.2 - Africa US-China competition map
# ===========================================================================

def fig_6quat_2_us_china_africa() -> Path:
    """US vs China engagement in Africa - 4 dimensions stacked."""
    fig, ax = plt.subplots(figsize=(11, 6))

    dimensions = ["Infrastructure\n(Md USD)", "Talents formes\n(M personnes)",
                  "Couverture\n(pct continent)", "Modeles IA\n(deploiement)"]
    us_score = [3.7, 7.0, 25, 30]    # MS+AWS+Google+Cassava ; ms training (1+1+1+4=7M) ; etc.
    cn_score = [0.3, 0.12, 70, 60]    # Huawei DC pilot ; 120K formes ; 70 pct backbone 4G ; etc.

    x = np.arange(len(dimensions))
    w = 0.35

    bars_us = ax.bar(x - w / 2, us_score, w, color=US_COLOR, alpha=0.85,
                      label="Etats-Unis", edgecolor=US_COLOR, linewidth=1.3)
    bars_cn = ax.bar(x + w / 2, cn_score, w, color=CN_COLOR, alpha=0.85,
                      label="Chine", edgecolor=CN_COLOR, linewidth=1.3)

    for bar in bars_us:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                f"{bar.get_height():.1f}", ha="center",
                fontsize=10, fontweight="bold", color=US_COLOR)
    for bar in bars_cn:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                f"{bar.get_height():.1f}", ha="center",
                fontsize=10, fontweight="bold", color=CN_COLOR)

    ax.set_xticks(x)
    ax.set_xticklabels(dimensions, fontsize=10)
    ax.set_ylabel("Score (echelle variable selon dimension)", fontsize=11)
    ax.set_ylim(0, 80)
    ax.set_title("La rivalite US-Chine en Afrique : forces et angles d'attaque",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005,
             "Source : Tableau 20. Couverture = part backbone 4G ; Modeles IA = part deploiement (ChatGPT vs DeepSeek/Qwen).",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_6quat.2_US_China_Africa")


# ===========================================================================
# Main
# ===========================================================================

FIGURES = [
    fig_6_1_sectoral_exposure,
    fig_6_2_three_configurations,
    fig_6bis_1_brazil_scenarios,
    fig_6bis_2_latam_deficit,
    fig_6ter_1_asia_tiers,
    fig_6ter_2_china_paradox,
    fig_6quat_1_africa_deficit,
    fig_6quat_2_us_china_africa,
]


def main() -> None:
    log.info("Output directory: %s", OUTPUT_DIR)
    _common_style()
    for fn in FIGURES:
        fn()
    log.info("Done. %d figures rendered.", len(FIGURES))


if __name__ == "__main__":
    main()
