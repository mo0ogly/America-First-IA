"""
Conclusion generale - generateur de figure de synthese FR.

Genere une figure unique de synthese visuelle de l'etude :
la frise des chapitres avec leur contribution principale et l'arc
narratif de la these (du diagnostic empirique a la trajectoire 2030).

Toutes les valeurs sont alignees sur le snapshot du tableau de bord
d'avril 2026.

Output : ./figures_conclusion/Fig_Conclusion_Synthese_FR.png (300 DPI)

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
log = logging.getLogger("conclusion_graphs")


OUTPUT_DIR = Path(os.environ.get("CONCL_FIG_DIR", "./figures_conclusion")).resolve()
DPI = 300

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


def fig_synthese() -> Path:
    """Synthese visuelle de la these en 11 chapitres + arc narratif."""
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis("off")

    ax.text(8, 10.4,
            "AI for Americans First : synthese de la these",
            ha="center", fontsize=17, fontweight="bold", color=NAVY)
    ax.text(8, 9.85,
            "Du diagnostic empirique avril 2026 a la trajectoire 2030",
            ha="center", fontsize=12, fontstyle="italic", color=GREY)

    # 4 stages of the narrative, vertically: Diagnostic / Mecanismes / Scenarios / Reponse
    stages = [
        (0.5, 7.0, "DIAGNOSTIC",
         "Chap I : Cadre theorique\nChap II : CACI Power Mode\nChap III : Snapshot avril 2026\n\n"
         "F(USA) = 76,9 pct\nF(UE) = 3,3 pct\nRatio brut 17,6:1\nCACI 3,46:1\nPPA UE/US 1,59x",
         US_COLOR),
        (4.0, 7.0, "MECANISMES",
         "Chap IV : Avantage US\n\n"
         "Compute installe 76,9 pct\nCapex 660-690 Md USD/an\nEnergie PPA 1,59x\n\n"
         "+ Phys/Sov (Chap I)\nUE 99,2 pct souverain\nEAU 99,6 pct US-side\n(CACI 56 vers 6)",
         CN_COLOR),
        (7.5, 7.0, "SCENARIOS 2030",
         "Chap V : 4 scenarios\n+ Cloud Sovereignty\nMandates 2028\n\n"
         "A Statu quo : 4-5:1\nB Fracture : 6-8:1\nC Partenariat : 2,0-2,5:1\nD Souverainete : 4-7:1 (U)",
         ACCENT2),
        (11.0, 7.0, "REPONSE FR/UE",
         "Chap VI/bis/ter/quater\nChap VII Recommandations\n\n"
         "5 axes : compute, energie,\nalliances, regulation,\ntalent\n\n"
         "F_sov UE 22 pct (2026)\nvers 70 pct (2030)\nFenetre 2026-2028",
         ACCENT1),
    ]
    box_w, box_h = 3.2, 4.4
    for x, y, title, body, col in stages:
        rect = mpatches.FancyBboxPatch(
            (x, y - box_h / 2 - 0.2), box_w, box_h,
            boxstyle="round,pad=0.15",
            facecolor=col, alpha=0.13, edgecolor=col, linewidth=2.5,
        )
        ax.add_patch(rect)
        cx = x + box_w / 2
        # Title at the top of the box
        ax.text(cx, y + 1.7, title, ha="center", fontsize=12,
                fontweight="bold", color=col)
        # Body below the title
        ax.text(cx, y - 0.6, body, ha="center", fontsize=8.5,
                color="#222", linespacing=1.45)

    # Arrows between stages
    for x_start, x_end in [(3.7, 4.0), (7.2, 7.5), (10.7, 11.0)]:
        ax.annotate("", xy=(x_end, 7.0), xytext=(x_start, 7.0),
                    arrowprops=dict(arrowstyle="->", color=GREY, lw=2))

    # Lower band: 5 contributions
    contributions = [
        (0.4, "1. Integration analytique",
         "Energie + semi-conducteurs\n+ compute + regulation\n+ productivite unifies",
         GOLD),
        (3.4, "2. Indice CACI",
         "Power Mode geometrique\nF^0,40 L^0,20 R^0,15 / E^0,25\n+ extension Phys/Sov",
         GOLD),
        (6.4, "3. Effets paradoxaux",
         "Restrictions US accelerent\nautonomisation chinoise\n+ Tier 1 cofinance US",
         GOLD),
        (9.4, "4. Comparatif regional",
         "Europe / Am. du Sud /\nAsie / Afrique : 4 trajectoires\nde dependance distinctes",
         GOLD),
        (12.4, "5. Extension Afrique",
         "Deficit x44 a x417\nDouble bind US/Chine\nFenetre UA Phase II 2028",
         GOLD),
    ]
    box_w2, box_h2 = 2.7, 2.4
    for x, title, body, col in contributions:
        rect = mpatches.FancyBboxPatch(
            (x, 1.2), box_w2, box_h2,
            boxstyle="round,pad=0.12",
            facecolor=col, alpha=0.13, edgecolor=col, linewidth=2,
        )
        ax.add_patch(rect)
        cx = x + box_w2 / 2
        ax.text(cx, 3.05, title, ha="center", fontsize=10,
                fontweight="bold", color=col)
        ax.text(cx, 1.95, body, ha="center", fontsize=8.0,
                color="#222", linespacing=1.4)

    ax.text(8, 4.0, "5 contributions a la litterature",
            ha="center", fontsize=12, fontweight="bold",
            color=NAVY, fontstyle="italic")

    # Bottom signature
    ax.text(8, 0.4,
            "Source : these doctorale Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique). "
            "Tableau de bord public : https://mo0ogly.github.io/America-First-IA/dashboard/",
            ha="center", fontsize=8, color="gray", fontstyle="italic")

    return save_fig(fig, "Fig_Conclusion_Synthese")


def main() -> None:
    log.info("Output directory: %s", OUTPUT_DIR)
    _common_style()
    fig_synthese()
    log.info("Done.")


if __name__ == "__main__":
    main()
