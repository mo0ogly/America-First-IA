"""
Chapitre VII - Generateur de graphiques FR.

Genere les figures du chapitre VII (Recommandations) en francais.
Toutes les valeurs sont alignees sur le snapshot du tableau de bord
d'avril 2026.

Figures
-------
7.1 Capex 2026 : hyperscalers US vs InvestAI EU vs France 1 pct PIB.
7.2 Matrice temporelle 5 axes x 3 horizons (heatmap d'urgence).
7.3 Trajectoire France : composantes du F_sov + cible 2029.
7.4 Mix energetique pour data centers : France vs concurrents EU.
7.5 Reduction du risque protectionniste : 3 leviers (reserves GPU,
    diversification, clauses).

Output : ./figures_ch7/Fig_7.X_NAME_FR.png (300 DPI)

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
log = logging.getLogger("chapitre7_graphs")


OUTPUT_DIR = Path(os.environ.get("CH7_FIG_DIR", "./figures_ch7")).resolve()
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
# Fig 7.1 - Capex gap (hyperscalers US vs InvestAI vs France 1 pct PIB)
# ===========================================================================

def fig_7_1_capex_gap() -> Path:
    """Capex 2026 hyperscalers US vs InvestAI EU 5 ans vs France 1 pct PIB."""
    fig, ax = plt.subplots(figsize=(12, 6.5))

    labels = ["Hyperscalers US\n(annuel 2026)", "Big 5 cumule\n(annuel 2026)",
              "InvestAI EU\n(5 ans, 2026-2030)", "France 1 pct PIB\n(annuel cible)",
              "Capex prive\nMistral 2026"]
    values = [200, 675, 200, 28, 1.0]  # Md USD or EUR
    colors = [US_COLOR, US_COLOR, EU_COLOR, ACCENT1, ACCENT3]

    x = np.arange(len(labels))
    bars = ax.bar(x, values, color=colors, alpha=0.85,
                  edgecolor="white", linewidth=1.5)

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 8,
                f"{val:.0f}" if val >= 10 else f"{val:.1f}",
                ha="center", fontsize=11,
                fontweight="bold", color=bar.get_facecolor())

    # Annotation: ratio US/EU capex
    ax.annotate("", xy=(2.4, 200), xytext=(0.4, 200),
                arrowprops=dict(arrowstyle="<->", color=GREY, lw=1.5))
    ax.text(1.4, 380, "Ratio capex annuel\n675 / 200 / 5 = 6,75x\n(annuel/annuel)",
            ha="center", fontsize=9, fontweight="bold", color=GREY,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor=GREY, alpha=0.85))

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Capex IA (Md USD ou EUR)", fontsize=11)
    ax.set_ylim(0, 760)
    ax.set_title("L'asymetrie de capex IA : ordres de grandeur 2026",
                 fontsize=14, fontweight="bold", color=NAVY, pad=14)

    legend_elements = [
        mpatches.Patch(color=US_COLOR, label="USA (hyperscalers)"),
        mpatches.Patch(color=EU_COLOR, label="UE (InvestAI public+prive)"),
        mpatches.Patch(color=ACCENT1, label="France (cible 1 pct PIB Gartner)"),
        mpatches.Patch(color=ACCENT3, label="Acteur prive europeen (Mistral)"),
    ]
    ax.legend(handles=legend_elements, fontsize=10, loc="upper right",
              framealpha=0.9)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005,
             "Source : Euronews (fevrier 2026), Gartner (2025), Deloitte (novembre 2025), Mistral AI (septembre 2025)",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_7.1_Capex_Gap")


# ===========================================================================
# Fig 7.2 - Recommandations heatmap (5 axes x 3 horizons)
# ===========================================================================

def fig_7_2_recommendations_heatmap() -> Path:
    """5 axes x 3 horizons heatmap of urgency."""
    fig, ax = plt.subplots(figsize=(11, 7))

    axes_labels = ["A1 Compute\ninfrastructure", "A2 Energie\nnucleaire",
                   "A3 Alliances\ntech", "A4 Regulation\noffensive",
                   "A5 Talent\net capital humain"]
    horizons = ["2026-2027\nCourt terme", "2027-2029\nMoyen terme",
                "2029-2032\nLong terme"]

    # Urgency score: 1.0 = critical now, 0.6 = important, 0.3 = preparatory
    urgency = np.array([
        [1.00, 0.80, 0.50],   # Compute: AI Factories now, Gigafactories medium, frontier long
        [0.85, 1.00, 0.60],   # Energie: peak EPR 2 in 2027-2029
        [0.70, 0.90, 0.55],   # Alliances: structural negotiation peak medium
        [0.65, 1.00, 0.70],   # Regulation: CADA peak medium
        [1.00, 0.80, 0.50],   # Talent: visas + bourses NOW
    ])

    im = ax.imshow(urgency, cmap="RdYlGn_r", aspect="auto", vmin=0, vmax=1)

    annotations = [
        ["13 AI Factories\nSpecial Compute Zones", "5 AI Gigafactories\n30-40 pct souverain", "40 pct local\nfrontier souverains"],
        ["Nuclear for AI 250 MW\n6 sites EDF", "EPR 2 lances\n+8 optionnels", "1er SMR DC\n+20 GW"],
        ["UE-Nvidia\nReserves GPU", "TSMC 7/5 nm\nUE-Japon HBM", "DARE/RISC-V\nMulti-fournisseur"],
        ["Apply AI Strategy\nbuy European", "CLOUD Act Shield\nSOV-3 obligatoire", "Effet Bruxelles\nNormes IA export"],
        ["Visas talents\nMcKinsey 2026", "Salaires GAFAM\negales", "Captation\nbrain drain inverse"],
    ]

    ax.set_xticks(np.arange(len(horizons)))
    ax.set_xticklabels(horizons, fontsize=10)
    ax.set_yticks(np.arange(len(axes_labels)))
    ax.set_yticklabels(axes_labels, fontsize=10)

    for i in range(len(axes_labels)):
        for j in range(len(horizons)):
            ax.text(j, i, annotations[i][j], ha="center", va="center",
                    fontsize=8.5, fontweight="bold",
                    color="white" if urgency[i, j] > 0.55 else "#222")

    ax.set_title("Matrice temporelle des recommandations 5 axes x 3 horizons",
                 fontsize=14, fontweight="bold", color=NAVY, pad=15)

    cbar = fig.colorbar(im, ax=ax, shrink=0.7, pad=0.02)
    cbar.set_label("Urgence d'execution\n(0 = preparatoire, 1 = critique)",
                   fontsize=9, rotation=270, labelpad=22)

    fig.text(0.5, 0.01,
             "Source : construction de l'auteur - Section 7.6, Tableau 23. La fenetre 2026-2028 concentre l'urgence maximale.",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_7.2_Recommendations_Heatmap")


# ===========================================================================
# Fig 7.3 - F_sov France trajectory
# ===========================================================================

def fig_7_3_fsov_trajectory() -> Path:
    """F_sov France trajectory 2026-2030 with 4 components."""
    fig, ax = plt.subplots(figsize=(12, 6.5))

    years = [2026, 2027, 2028, 2029, 2030]

    # Stacked components - share of EU AI workloads under EU jurisdiction
    # Baseline 2026: ~22 pct (78 pct on AWS/Azure/GCP per Synergy)
    cloud_souv = [10, 13, 18, 23, 28]   # SecNumCloud / S3NS / Bleu / OVHcloud / Scaleway
    mistral = [3, 5, 8, 11, 14]          # Mistral Compute (40 MW + Borlange + scaling)
    gigafact = [0, 1, 5, 10, 14]         # 5 AI Gigafactories ramping
    aifact = [9, 12, 13, 14, 14]         # 13 AI Factories EuroHPC

    components = [aifact, cloud_souv, mistral, gigafact]
    labels = ["AI Factories EuroHPC", "Cloud souverain (SecNumCloud + EUCS)",
              "Mistral Compute + similaires", "AI Gigafactories"]
    colors = [ACCENT1, EU_COLOR, ACCENT3, ACCENT2]

    bottom = np.zeros(len(years))
    for comp, label, col in zip(components, labels, colors):
        ax.fill_between(years, bottom, bottom + np.array(comp),
                        alpha=0.85, label=label, color=col,
                        edgecolor="white", linewidth=1)
        bottom = bottom + np.array(comp)

    # Total annotation
    totals = [sum(c[i] for c in components) for i in range(len(years))]
    for x, y in zip(years, totals):
        ax.text(x, y + 1.5, f"{y} pct", ha="center",
                fontsize=10, fontweight="bold", color=NAVY)

    # Target line
    ax.axhline(y=40, color=CN_COLOR, linestyle="--", linewidth=2, alpha=0.7)
    ax.text(2026.1, 41,
            "Cible 30-40 pct workloads souverains 2029 (Section 7.1.2)",
            fontsize=9, fontweight="bold", color=CN_COLOR, fontstyle="italic")

    ax.set_xticks(years)
    ax.set_xlabel("Annee", fontsize=11)
    ax.set_ylabel("Part workloads UE sous juridiction europeenne (pct)", fontsize=11)
    ax.set_ylim(0, 80)
    ax.set_title("Trajectoire de la souverainete operationnelle UE\n(montee de F_sov sur les charges cloud, 2026-2030)",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper left")
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005,
             "Source : construction de l'auteur. Estimations de calibration : Synergy Research Group (2025), Apply AI Strategy (UE 2025).",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_7.3_FSov_Trajectory")


# ===========================================================================
# Fig 7.4 - Energy mix for data centers (France vs EU competitors)
# ===========================================================================

def fig_7_4_energy_mix() -> Path:
    """Energy mix for data centers - France vs Germany vs Netherlands vs Ireland vs USA."""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    countries = ["France", "Allemagne", "Pays-Bas", "Irlande", "USA"]
    nuclear = [70, 0, 3, 0, 19]
    renewables = [25, 60, 50, 40, 22]
    fossil = [5, 40, 47, 60, 59]

    x = np.arange(len(countries))
    w = 0.6

    p1 = ax.bar(x, nuclear, w, color=ACCENT1, alpha=0.9,
                label="Nucleaire", edgecolor="white", linewidth=1)
    p2 = ax.bar(x, renewables, w, bottom=nuclear, color=EU_COLOR, alpha=0.9,
                label="Renouvelables", edgecolor="white", linewidth=1)
    p3 = ax.bar(x, fossil, w, bottom=np.array(nuclear) + np.array(renewables),
                color=GREY, alpha=0.9, label="Fossiles",
                edgecolor="white", linewidth=1)

    # PPA cost annotations on top of bars
    ppa_costs = ["115 USD/MWh\nratio 1,35x US",
                 "140 USD/MWh\nratio 1,65x US",
                 "130 USD/MWh\nratio 1,53x US",
                 "150 USD/MWh\nratio 1,76x US",
                 "85 USD/MWh\nbaseline"]
    for i, (cx, cost) in enumerate(zip(x, ppa_costs)):
        ax.text(cx, 105, cost, ha="center", fontsize=9,
                fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#F0F4F8",
                          edgecolor=NAVY, alpha=0.85))

    # Decarb percentage at the boundary nuclear+renouvelables
    for i, (cx, n, r) in enumerate(zip(x, nuclear, renewables)):
        decarb = n + r
        ax.text(cx, n + r / 2 if r > 5 else n / 2, f"{decarb} pct\ndecarbone",
                ha="center", va="center", fontsize=10,
                fontweight="bold", color="white")

    ax.set_xticks(x)
    ax.set_xticklabels(countries, fontsize=11)
    ax.set_ylabel("Mix electrique (pct)", fontsize=11)
    ax.set_ylim(0, 130)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_title("Avantage energetique francais pour les data centers IA\n(mix electrique et cout PPA-ajuste, baseline avril 2026)",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005,
             "Source : RTE (2024), AIE (avril 2025), tableau de bord public (avril 2026). Couts PPA-ajuste US baseline 85 USD/MWh.",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_7.4_Energy_Mix")


# ===========================================================================
# Fig 7.5 - Risk reduction levers
# ===========================================================================

def fig_7_5_risk_reduction() -> Path:
    """3 risk reduction levers - quadrant view."""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(6, 6.6, "Trois leviers de reduction du risque protectionniste",
            ha="center", fontsize=15, fontweight="bold", color=NAVY)

    levers = [
        (0.4, "Levier 1\nReserves strategiques GPU",
         "Modele : reserves petrole (90 j)\n\nObjectif : 6-12 mois de besoins UE\n\nVolume cible : 200 000-400 000\nGPU H100-eq en stock\n\nCout estime : 8-15 Md EUR\n(amortissable sur 3-4 ans)\n\nProtege contre :\n- Affiliates Rule\n- Tarifs Section 232 etendus",
         CN_COLOR),
        (4.3, "Levier 2\nDiversification fournisseurs",
         "Court terme :\n- AMD MI300X/MI350X\n- Intel Gaudi 3\n- Graphcore (UK)\n\nMoyen terme :\n- SiPearl Rhea (FR)\n- Huawei Ascend non-sensitif\n\nLong terme :\n- DARE/RISC-V (EuroHPC)\n- Horizon 2030-2032\n\nObjectif : 40 pct non-Nvidia 2030",
         ACCENT3),
        (8.2, "Levier 3\nClauses anti-weaponisation",
         "Modele : non-discrimination OMC\n\nIntegration dans :\n- Accord commercial UE-US\n- Renouvellement WTO ITA\n\nMecanismes :\n- Notification prealable\n- Reciprocite controles export\n- Arbitrage independant\n\nProtection legale en cas de\nrupture protectionniste",
         ACCENT1),
    ]
    box_w, box_h = 3.4, 5.0
    for x, title, body, col in levers:
        rect = mpatches.FancyBboxPatch(
            (x, 0.6), box_w, box_h,
            boxstyle="round,pad=0.15",
            facecolor=col, alpha=0.12, edgecolor=col, linewidth=2.5,
        )
        ax.add_patch(rect)
        cx = x + box_w / 2
        ax.text(cx, 5.0, title, ha="center", fontsize=12,
                fontweight="bold", color=col, linespacing=1.3)
        ax.text(cx, 2.7, body, ha="center", fontsize=9.5,
                color="#333", linespacing=1.5)

    ax.text(6, 0.2,
            "Source : construction de l'auteur - Section 7.3.2",
            ha="center", fontsize=8, color="gray", fontstyle="italic")
    return save_fig(fig, "Fig_7.5_Risk_Reduction")


# ===========================================================================
# Main
# ===========================================================================

FIGURES = [
    fig_7_1_capex_gap,
    fig_7_2_recommendations_heatmap,
    fig_7_3_fsov_trajectory,
    fig_7_4_energy_mix,
    fig_7_5_risk_reduction,
]


def main() -> None:
    log.info("Output directory: %s", OUTPUT_DIR)
    _common_style()
    for fn in FIGURES:
        fn()
    log.info("Done. %d figures rendered.", len(FIGURES))


if __name__ == "__main__":
    main()
