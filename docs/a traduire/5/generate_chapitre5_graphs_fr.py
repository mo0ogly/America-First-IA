"""
Chapitre V - Scenarios Prospectifs 2026-2030 - generateur de graphiques FR.

Genere les figures du chapitre V en francais uniquement. Toutes les
valeurs sont alignees sur le snapshot du tableau de bord d'avril 2026.

Figures
-------
5.1 Trajectoires CACI(US)/CACI(UE) 2025-2030 par scenario (4 courbes,
    baseline 3,46:1 en avril 2026 ; A et B divergent vers le haut, C
    converge vers 2,0-2,5:1, D fait la courbe en U).
5.2 Chronologie des points de bascule 2026-2030 et fenetres decisionnelles.
5.3 Heatmap de synthese : 6 metriques x 4 scenarios (2030).
5.4 Les 4 elements predetermines (EP1-EP4) avec valeurs consolidees.
5.5 Ratio compute brut US/UE (M1) par scenario - barres horizontales.
5.6 Matrice 2x2 actualisee avec probabilites et CACI 2030.
5.7 NEW : Impact des Cloud Sovereignty Mandates 2028 sur le CACI par
    juridiction (pre/post-Mandate, basee sur Tableau 12).

Output : ./figures_ch5/Fig_5.x_NAME_FR.png (300 DPI)

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
log = logging.getLogger("chapitre5_graphs")


# ---------------------------------------------------------------------------
# Constants - April 2026 dashboard snapshot
# ---------------------------------------------------------------------------

CACI_BASELINE_2026 = 3.46
US_EU_RAW_OPERATIONAL_2025 = 17.6
PPA_RATIO_EU_US = 1.59
US_SHARE_OPERATIONAL = 76.9

OUTPUT_DIR = Path(os.environ.get("CH5_FIG_DIR", "./figures_ch5")).resolve()
DPI = 300


# ---------------------------------------------------------------------------
# Visual identity
# ---------------------------------------------------------------------------

NAVY = "#1A2744"
GOLD = "#B8922F"
US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
CN_COLOR = "#C0392B"
ACCENT1 = "#148F77"
ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"
ACCENT4 = "#2C3E50"

# Per-scenario colours
SC_A = "#3498DB"
SC_B = "#E74C3C"
SC_C = "#27AE60"
SC_D = "#8E44AD"

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
# Fig 5.1 - CACI trajectories
# ===========================================================================

def fig1_caci_trajectories() -> Path:
    """4 CACI trajectories 2025-2030, baseline 3.46:1.

    Trajectories follow the §5.3-5.6 narratives:
        A: 3.46 -> 4-5:1 (slow drift)
        B: 3.46 -> 6-8:1 (digital fracture)
        C: 3.46 -> 2.0-2.5:1 (catch-up)
        D: U-shape: 3.46 -> 8-12:1 in 2027-2028 (peak shock),
           then improvement to 4-7:1 by 2030.
    """
    fig, ax = plt.subplots(figsize=(13, 7.5))
    years = [2025, 2026, 2027, 2028, 2029, 2030]

    # Anchor: 3.46 in 2026 (April snapshot). 2025 is interpolated slightly lower.
    sc_a = [3.30, 3.46, 3.80, 4.20, 4.50, 4.50]
    sc_b = [3.30, 3.46, 4.50, 6.00, 7.00, 7.00]
    sc_c = [3.30, 3.46, 3.20, 2.80, 2.40, 2.25]
    sc_d = [3.30, 3.46, 6.50, 10.00, 7.50, 5.50]  # U-shape

    series = [
        (sc_a, SC_A, "o", "A - Statu quo renforce"),
        (sc_b, SC_B, "s", "B - Fracture numerique"),
        (sc_c, SC_C, "D", "C - Partenariat asymetrique"),
        (sc_d, SC_D, "^", "D - Souverainete contestee"),
    ]

    for data, col, mk, label in series:
        ax.plot(years, data, color=col, linewidth=3,
                marker=mk, markersize=9, label=label, zorder=5)
        # End-value annotation
        ax.text(years[-1] + 0.08, data[-1], f"{data[-1]:.1f}",
                fontsize=10, fontweight="bold", color=col,
                va="center", ha="left")

    # Baseline horizontal line at 3.46 (April 2026)
    ax.axhline(y=CACI_BASELINE_2026, color=GREY, linewidth=1,
               linestyle=":", alpha=0.6)
    ax.text(2025.05, CACI_BASELINE_2026 - 0.25,
            f"baseline avril 2026\nCACI = {CACI_BASELINE_2026:.2f}:1",
            fontsize=9, color=GREY, fontstyle="italic")

    # 2028 vertical guide
    ax.axvline(x=2028, color=ACCENT4, linewidth=1.5,
               linestyle="--", alpha=0.4)
    ax.text(2028.05, 0.6, "Point de\nconvergence\n2028",
            fontsize=9, fontweight="bold", color=ACCENT4)

    # Danger zone above 8:1
    ax.axhspan(8, 12, alpha=0.06, color=CN_COLOR)
    ax.text(2025.1, 11.0, "Zone de decrochage\nirreversible",
            fontsize=10, fontweight="bold", color=CN_COLOR,
            fontstyle="italic")

    ax.set_title("Trajectoires du ratio CACI(US)/CACI(UE) 2025-2030 par scenario\n"
                 "(Power Mode, baseline 3,46:1 avril 2026)",
                 fontsize=14, fontweight="bold", color=NAVY, pad=15)
    ax.set_ylabel("Ratio CACI(US) / CACI(UE)", fontsize=12)
    ax.set_xlim(2024.8, 2030.4)
    ax.set_ylim(0, 12)
    ax.set_xticks(years)
    ax.legend(fontsize=10, loc="upper left", framealpha=0.95)
    ax.grid(True, linestyle=":", alpha=0.4)

    fig.text(0.5, 0.01,
             "Source : construction de l'auteur - Section 5.7.1, calibration CACI",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_5.1_CACI_Trajectories")


# ===========================================================================
# Fig 5.2 - Tipping points timeline
# ===========================================================================

def fig2_tipping_points() -> Path:
    """5 tipping points on a horizontal timeline 2026-2030."""
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(7.5, 6.7,
            "Chronologie des points de bascule 2026-2030 et fenetres decisionnelles",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)

    y_line = 3.5
    ax.plot([0.8, 14.2], [y_line, y_line], color="#333",
            linewidth=3, zorder=1)

    events = [
        ("Avr.\n2026", "Rapport Phase 1\nNegociations US-UE", "Modere\nvs agressif", ACCENT3),
        ("Juil.\n2026", "Rapport Commerce\nsemi data centers", "Extension\ntarifs ?", CN_COLOR),
        ("2027", "Premieres Gigafactories\noperationnelles ?", "Proactif\nvs reactif", SC_C),
        ("2028", "POINT CRITIQUE\nDemande > Capacite UE", "Moment de\nverite", SC_B),
        ("2029-30", "Premiers SMR nucleaires\nDARE/RISC-V maturite ?", "Autonomie\na long terme", ACCENT2),
    ]
    event_x = [1.8, 4.2, 6.8, 9.5, 12.5]

    for i, (ex, (date, desc, impact, col)) in enumerate(zip(event_x, events)):
        y_off = 1.8 if i % 2 == 0 else -1.7
        y_text = y_line + y_off

        size = 16 if i == 3 else 12  # 2028 emphasised
        ax.plot(ex, y_line, "o", color=col, markersize=size, zorder=5)
        ax.plot(ex, y_line, "o", color="white", markersize=size - 5, zorder=6)

        ax.plot([ex, ex], [y_line, y_text + (0.3 if y_off > 0 else -0.3)],
                color=col, linewidth=1.5, linestyle="--", zorder=2)

        bw, bh = 2.2, 1.5
        rect = mpatches.FancyBboxPatch(
            (ex - bw / 2, y_text - bh / 2), bw, bh,
            boxstyle="round,pad=0.1",
            facecolor=col, alpha=0.15, edgecolor=col, linewidth=1.8,
        )
        ax.add_patch(rect)

        ax.text(ex, y_text + 0.45, date, ha="center", fontsize=10,
                fontweight="bold", color=col)
        ax.text(ex, y_text - 0.05, desc, ha="center", fontsize=8.5,
                color="#333")
        ax.text(ex, y_text - 0.55, impact, ha="center", fontsize=8,
                fontstyle="italic", color=col)

    # Decision window highlight 2026-2027
    ax.axvspan(1.5, 7.0, ymin=0.45, ymax=0.55, alpha=0.1, color=GOLD)
    ax.text(4.0, y_line + 0.05, "Fenetre decisionnelle critique",
            ha="center", fontsize=9, fontweight="bold",
            color=GOLD, fontstyle="italic")

    ax.text(7.5, 0.3,
            "Source : construction de l'auteur - Sections 5.7.2-5.7.3",
            ha="center", fontsize=8, color="gray", fontstyle="italic")

    return save_fig(fig, "Fig_5.2_Tipping_Points")


# ===========================================================================
# Fig 5.3 - Heatmap 6 metrics x 4 scenarios
# ===========================================================================

def fig3_heatmap_synthesis() -> Path:
    """Heatmap of 6 metrics x 4 scenarios with normalised scores."""
    fig, ax = plt.subplots(figsize=(11, 7))

    metrics = ["M1 Compute\nratio", "M2 Cout\nFLOP",
               "M3 Cloud\nUS (pct)", "M4 Product.\nUE (pct/an)",
               "M5 Energie\nUE (TWh)", "M6 CACI\nratio"]
    scenarios = ["A\nStatu quo", "B\nFracture", "C\nPartenariat", "D\nSouverainete"]

    # Score grid: lower is better for EU. Normalised 0 (best) to 1 (worst).
    # Order: rows = metrics, cols = scenarios (A, B, C, D)
    data = np.array([
        [0.50, 1.00, 0.20, 0.40],   # M1
        [0.45, 1.00, 0.10, 0.35],   # M2
        [0.65, 0.95, 0.30, 0.05],   # M3 (cloud share, lower better -> C wins)
        [0.55, 1.00, 0.05, 0.40],   # M4 (productivity gap, inverted: lower=better)
        [0.40, 0.10, 0.65, 0.95],   # M5 (energy demand neutral; high = active)
        [0.45, 1.00, 0.05, 0.55],   # M6 CACI
    ])

    im = ax.imshow(data, cmap="RdYlGn_r", aspect="auto", vmin=0, vmax=1)

    ax.set_xticks(np.arange(len(scenarios)))
    ax.set_xticklabels(scenarios, fontsize=10)
    ax.set_yticks(np.arange(len(metrics)))
    ax.set_yticklabels(metrics, fontsize=10)

    # Display the textual value of each cell from Tableau 11
    annotations = [
        ["18-22:1", "25-35:1", "8-10:1", "12-15:1"],
        ["2,4-3,2x", "4-6x", "1,5-2,0x", "1,8-2,5x"],
        ["72-75 pct", "78-82 pct", "60-65 pct", "50-55 pct"],
        ["+1,0-1,5", "+0,3-0,8", "+1,8-2,5", "+1,2-2,0"],
        ["~115", "~95", "~140", "~155"],
        ["4-5:1", "6-8:1", "2,0-2,5:1", "4-7:1"],
    ]

    for i in range(len(metrics)):
        for j in range(len(scenarios)):
            ax.text(j, i, annotations[i][j], ha="center", va="center",
                    fontsize=9, fontweight="bold",
                    color="white" if data[i, j] > 0.5 else "#222")

    ax.set_title("Synthese : 6 metriques x 4 scenarios (horizon 2030)",
                 fontsize=14, fontweight="bold", color=NAVY, pad=15)

    cbar = fig.colorbar(im, ax=ax, shrink=0.6, pad=0.03)
    cbar.set_label("Severite pour l'UE\n(0 = favorable, 1 = critique)",
                   fontsize=9, rotation=270, labelpad=22)

    fig.text(0.5, 0.01,
             "Source : construction de l'auteur - Tableau 11",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_5.3_Heatmap_Synthesis")


# ===========================================================================
# Fig 5.4 - Predetermined elements
# ===========================================================================

def fig4_predetermined_elements() -> Path:
    """Visual summary of the 4 predetermined elements EP1-EP4."""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(6, 7.4,
            "Les 4 elements predetermines (EP) structurant tous les scenarios",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)

    items = [
        ("EP1", "Croissance exponentielle\ndemande compute IA",
         "Ventes semis x2 en 2 ans\nPuces IA doublent / 7 mois", US_COLOR),
        ("EP2", "Concentration persistante\ncompute aux USA",
         f"Ratio brut {US_EU_RAW_OPERATIONAL_2025:.1f}:1 US/UE\nCACI Power Mode {CACI_BASELINE_2026:.2f}:1", ACCENT3),
        ("EP3", "Tension energetique\ncroissante",
         "415 -> 950 TWh (2024-2030)\nUE 1,4-1,7x cher (PPA)", ACCENT2),
        ("EP4", "Section 232\nen place",
         "Base legale confirmee\nRapport Commerce juil. 2026", CN_COLOR),
    ]

    box_w, box_h = 2.6, 4.5
    x_starts = [0.4, 3.4, 6.4, 9.4]

    for x_start, (code, title, detail, col) in zip(x_starts, items):
        rect = mpatches.FancyBboxPatch(
            (x_start, 1.0), box_w, box_h,
            boxstyle="round,pad=0.15",
            facecolor=col, alpha=0.12, edgecolor=col, linewidth=2.5,
        )
        ax.add_patch(rect)

        cx = x_start + box_w / 2
        ax.text(cx, 5.0, code, ha="center", fontsize=22,
                fontweight="bold", color=col)
        ax.text(cx, 4.0, title, ha="center", fontsize=11,
                fontweight="bold", color="#222", linespacing=1.3)
        ax.text(cx, 2.4, detail, ha="center", fontsize=10,
                color="#444", linespacing=1.4)

    ax.text(6, 0.3, "Source : construction de l'auteur - Section 5.1",
            ha="center", fontsize=8, color="gray", fontstyle="italic")

    return save_fig(fig, "Fig_5.4_Predetermined_Elements")


# ===========================================================================
# Fig 5.5 - M1 compute ratio per scenario (horizontal bars)
# ===========================================================================

def fig5_compute_ratio_per_scenario() -> Path:
    """M1 metric (US/EU compute ratio) for each scenario at 2030."""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    scenarios = ["Baseline\n2025", "A - Statu quo\n(2030)", "B - Fracture\n(2030)",
                 "C - Partenariat\n(2030)", "D - Souverainete\n(2030)"]
    midpoints = [
        US_EU_RAW_OPERATIONAL_2025,
        20,    # 18-22 midpoint
        30,    # 25-35 midpoint
        9,     # 8-10 midpoint
        13.5,  # 12-15 midpoint
    ]
    colors = [GREY, SC_A, SC_B, SC_C, SC_D]

    y = np.arange(len(scenarios))
    bars = ax.barh(y, midpoints, color=colors, alpha=0.85,
                   edgecolor="white", linewidth=1.5)

    for bar, mid, label in zip(bars, midpoints,
                                ["17,6:1", "18-22:1", "25-35:1", "8-10:1", "12-15:1"]):
        ax.text(mid + 0.5, bar.get_y() + bar.get_height() / 2,
                label, va="center", fontsize=11, fontweight="bold",
                color=bar.get_facecolor())

    # Vertical reference at baseline
    ax.axvline(x=US_EU_RAW_OPERATIONAL_2025, color=GREY,
               linestyle=":", linewidth=1.5, alpha=0.6)

    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, fontsize=10)
    ax.invert_yaxis()
    ax.set_xlim(0, 38)
    ax.set_xlabel("Ratio compute brut US/UE (operationnel, equivalents H100)",
                  fontsize=11)
    ax.set_title("Ratio compute installe US/UE (M1) - projection 2030 par scenario",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.grid(axis="x", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005,
             "Source : construction de l'auteur - Sections 5.3-5.6, baseline avril 2026",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_5.5_Compute_Ratio_Per_Scenario")


# ===========================================================================
# Fig 5.6 - 2x2 matrix with probabilities
# ===========================================================================

def fig6_matrix_probabilities() -> Path:
    """2x2 matrix with scenario, probability, CACI 2030."""
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(5, 9.5,
            "Matrice 2x2 actualisee : scenarios, probabilites et CACI 2030",
            ha="center", fontsize=14, fontweight="bold", color=NAVY)

    # Quadrants
    quad_data = [
        # (x, y, w, h, color, name, prob, caci, x_label, y_label)
        (0.8, 4.5, 4.0, 3.6, SC_A, "A - Statu quo\nrenforce", "40-50 pct", "4-5:1"),
        (5.2, 4.5, 4.0, 3.6, SC_C, "C - Partenariat\nasymetrique", "15-20 pct", "2,0-2,5:1"),
        (0.8, 0.7, 4.0, 3.6, SC_B, "B - Fracture\nnumerique", "15-20 pct", "6-8:1"),
        (5.2, 0.7, 4.0, 3.6, SC_D, "D - Souverainete\ncontestee", "15-20 pct", "4-7:1"),
    ]

    for x, y, w, h, col, name, prob, caci in quad_data:
        rect = mpatches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.1",
            facecolor=col, alpha=0.18, edgecolor=col, linewidth=2.5,
        )
        ax.add_patch(rect)

        cx = x + w / 2
        cy = y + h / 2
        ax.text(cx, cy + 0.85, name, ha="center", fontsize=13,
                fontweight="bold", color=col, linespacing=1.3)
        ax.text(cx, cy - 0.2, f"Probabilite : {prob}",
                ha="center", fontsize=11, color="#333")
        ax.text(cx, cy - 0.95, f"CACI 2030 : {caci}",
                ha="center", fontsize=12, fontweight="bold", color=col,
                bbox=dict(boxstyle="round,pad=0.3",
                          facecolor="white", edgecolor=col, alpha=0.9))

    # Axis labels
    ax.text(2.8, 8.3, "US MODERE", ha="center", fontsize=11,
            fontweight="bold", color="#444")
    ax.text(7.2, 8.3, "UE PROACTIVE", ha="center", fontsize=11,
            fontweight="bold", color="#444")
    ax.text(2.8, 4.4, "UE REACTIVE", ha="center", fontsize=11,
            fontweight="bold", color="#444")
    ax.text(0.4, 6.3, "PROTECTIONNISME US", ha="center", fontsize=10,
            fontweight="bold", color="#444", rotation=90)
    ax.text(0.4, 2.5, "PROTECTIONNISME US", ha="center", fontsize=10,
            fontweight="bold", color="#444", rotation=90)
    ax.text(0.6, 8.3, "MODERE", ha="center", fontsize=10, color="#666")
    ax.text(0.6, 0.5, "AGRESSIF", ha="center", fontsize=10, color="#666")

    ax.text(5, 0.1,
            "Source : construction de l'auteur - Section 5.7, baseline avril 2026 (CACI 3,46:1)",
            ha="center", fontsize=8, color="gray", fontstyle="italic")

    return save_fig(fig, "Fig_5.6_Matrix_Probabilities")


# ===========================================================================
# Fig 5.7 - Cloud Sovereignty Mandates impact (NEW)
# ===========================================================================

def fig7_csm_impact() -> Path:
    """CACI impact pre/post Cloud Sovereignty Mandates 2028.

    Shows for each jurisdiction the CACI score before and after mandate
    activation. The collapse measures the share of installed/used compute
    that is operated by US-side hyperscalers.
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    jurisdictions = ["Etats-Unis", "Chine", "UE\n(workloads)", "EAU\n(installe)",
                     "Singapour\n(installe)", "Inde\n(workloads)"]

    # Pre-Mandate values: existing CACI (Power Mode) or hub-level scores
    pre = [100, 15.7, 28.9, 55.7, 50.0, 22.2]
    # Post-Mandate values: use F_sov factor from Tableau 12
    # collapse percentages: US 0, China 0, EU 30-50 pct -> 60 pct retained,
    # UAE 60-80 pct -> 30 pct retained (we already computed 6.0 from F_dom),
    # Singapore 55-75 pct -> 30 pct retained, India 30 pct -> 65 pct retained
    post = [
        100,                    # USA unaffected
        15.7,                   # CN already sovereign
        28.9 * 0.60,            # EU workloads collapse 40 pct
        6.0,                    # UAE: rigorous Sovereign CACI from Chap I
        50.0 * 0.30,            # Singapore 70 pct collapse
        22.2 * 0.65,            # India 35 pct collapse
    ]

    x = np.arange(len(jurisdictions))
    w = 0.36

    bars_pre = ax.bar(x - w / 2, pre, w, color=US_COLOR, alpha=0.6,
                      label="CACI pre-Mandate (avril 2026)",
                      edgecolor=US_COLOR, linewidth=1.5)
    bars_post = ax.bar(x + w / 2, post, w, color=CN_COLOR, alpha=0.85,
                       label="CACI post-Mandate (2028)",
                       edgecolor=CN_COLOR, linewidth=1.5)

    for bar, val in zip(bars_pre, pre):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5,
                f"{val:.1f}" if val < 100 else "100",
                ha="center", fontsize=10,
                fontweight="bold", color=US_COLOR)
    for bar, val in zip(bars_post, post):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5,
                f"{val:.1f}" if val < 100 else "100",
                ha="center", fontsize=10,
                fontweight="bold", color=CN_COLOR)

    # Collapse arrows for jurisdictions with significant impact
    for i, (p, q) in enumerate(zip(pre, post)):
        gap = p - q
        if gap >= 5:
            collapse_pct = 100 * gap / p
            ax.annotate(
                f"-{collapse_pct:.0f} pct",
                xy=(i, q + (p - q) / 2),
                xytext=(i + 0.45, q + (p - q) / 2),
                fontsize=9, color=CN_COLOR, fontweight="bold",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.2",
                          facecolor="#FFF3E0",
                          edgecolor=CN_COLOR, alpha=0.85),
            )

    ax.set_xticks(x)
    ax.set_xticklabels(jurisdictions, fontsize=10)
    ax.set_ylabel("Score CACI Power Mode (US = 100)", fontsize=11)
    ax.set_ylim(0, 115)
    ax.set_title("Impact des Cloud Sovereignty Mandates 2028 sur le CACI par juridiction\n"
                 "(le compute physique reste, mais devient legalement conditionnel)",
                 fontsize=13, fontweight="bold", color=NAVY, pad=15)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005,
             "Source : Tableau 12 et chapitre I Fig 1.8. Le cas EAU illustre l'effondrement maximal (99,6 pct US-side).",
             ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    return save_fig(fig, "Fig_5.7_CSM_Impact")


# ===========================================================================
# Main
# ===========================================================================

FIGURES = [
    fig1_caci_trajectories,
    fig2_tipping_points,
    fig3_heatmap_synthesis,
    fig4_predetermined_elements,
    fig5_compute_ratio_per_scenario,
    fig6_matrix_probabilities,
    fig7_csm_impact,
]


def main() -> None:
    log.info("Output directory: %s", OUTPUT_DIR)
    _common_style()
    for fn in FIGURES:
        fn()
    log.info("Done. %d figures rendered.", len(FIGURES))


if __name__ == "__main__":
    main()
