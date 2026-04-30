"""
Chapter V - Prospective Scenarios 2026-2030 - trilingual graph generator.

Generates the figures for Chapter V in English, French, and Brazilian Portuguese.
All values are aligned with the April 2026 dashboard snapshot.

Figures
-------
5.1 CACI(US)/CACI(EU) trajectories 2025-2030 by scenario.
5.2 Tipping points timeline 2026-2030 and decision windows.
5.3 Synthesis Heatmap: 6 metrics x 4 scenarios (2030).
5.4 The 4 predetermined elements (EP1-EP4).
5.5 Raw compute ratio US/EU (M1) per scenario - horizontal bars.
5.6 Updated 2x2 matrix with probabilities and CACI 2030.
5.7 Cloud Sovereignty Mandates 2028 impact on CACI by jurisdiction.

Output: ./figures_ch5/Fig_5.x_NAME_LANG.png (300 DPI)

Author: Fabrice Pizzi (Universite Paris-Sorbonne, M2 Economic Intelligence).
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
log = logging.getLogger("chapter5_graphs")

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

SC_A = "#3498DB"
SC_B = "#E74C3C"
SC_C = "#27AE60"
SC_D = "#8E44AD"

GREY = "#999999"
BG_COLOR = "white"

# ---------------------------------------------------------------------------
# Localization
# ---------------------------------------------------------------------------

LANGS = {
    "EN": {
        "suffix": "EN",
        "baseline_label": f"April 2026 baseline\nCACI = {CACI_BASELINE_2026:.2f}:1",
        "convergence_2028": "2028\nConvergence\nPoint",
        "danger_zone": "Irreversible Decoupling\nZone",
        "title_51": "CACI(US)/CACI(EU) Ratio Trajectories 2025-2030 by Scenario\n(Power Mode, baseline 3.46:1 April 2026)",
        "ylabel_51": "CACI(US) / CACI(EU) Ratio",
        "sc_names": ["A - Reinforced Status Quo", "B - Digital Fracture", "C - Asymmetric Partnership", "D - Contested Sovereignty"],
        "source_51": "Source: Author's construction - Section 5.7.1, CACI calibration",
        "title_52": "Tipping Points Timeline 2026-2030 and Decision Windows",
        "decision_window": "Critical Decision Window",
        "source_52": "Source: Author's construction - Sections 5.7.2-5.7.3",
        "events": [
            ("Apr.\n2026", "Phase 1 Report\nUS-EU Negotiations", "Moderate\nvs Aggressive"),
            ("July\n2026", "Commerce Report\nSemi Data Centers", "Tariff\nExtension?"),
            ("2027", "First Gigafactories\nOperational?", "Proactive\nvs Reactive"),
            ("2028", "CRITICAL POINT\nDemand > EU Capacity", "Moment of\nTruth"),
            ("2029-30", "First Nuclear SMRs\nDARE/RISC-V Maturity?", "Long-term\nAutonomy"),
        ],
        "metrics_53": ["M1 Compute\nratio", "M2 FLOP\ncost", "M3 Cloud\nUS (pct)", "M4 Product.\nEU (pct/yr)", "M5 Energy\nEU (TWh)", "M6 CACI\nratio"],
        "scenarios_53": ["A\nStatus Quo", "B\nFracture", "C\nPartnership", "D\nSovereignty"],
        "title_53": "Synthesis: 6 Metrics x 4 Scenarios (2030 Horizon)",
        "cbar_label_53": "EU Severity\n(0 = favorable, 1 = critical)",
        "source_53": "Source: Author's construction - Table 11",
        "title_54": "The 4 Predetermined Elements (EP) Structuring All Scenarios",
        "ep_data": [
            ("EP1", "Exponential AI\nCompute Demand", "Semi sales x2 in 2 years\nAI chips double / 7 months"),
            ("EP2", "Persistent US\nCompute Concentration", f"Raw ratio {US_EU_RAW_OPERATIONAL_2025:.1f}:1 US/EU\nCACI Power Mode {CACI_BASELINE_2026:.2f}:1"),
            ("EP3", "Increasing\nEnergy Tension", "415 -> 950 TWh (2024-2030)\nEU 1.4-1.7x more expensive"),
            ("EP4", "Section 232\nFramework in Place", "Confirmed legal basis\nCommerce Report July 2026"),
        ],
        "source_54": "Source: Author's construction - Section 5.1",
        "scenarios_55": ["Baseline\n2025", "A - Status Quo\n(2030)", "B - Fracture\n(2030)", "C - Partnership\n(2030)", "D - Sovereignty\n(2030)"],
        "xlabel_55": "Raw compute ratio US/EU (operational, H100 equivalents)",
        "title_55": "Installed Compute Ratio US/EU (M1) - 2030 Projection per Scenario",
        "source_55": "Source: Author's construction - Sections 5.3-5.6, baseline April 2026",
        "title_56": "Updated 2x2 Matrix: Scenarios, Probabilities and CACI 2030",
        "axis_labels_56": ["MODERATE US", "PROACTIVE EU", "REACTIVE EU", "US PROTECTIONISM", "MODERATE", "AGGRESSIVE"],
        "quad_names_56": ["A - Reinforced\nStatus Quo", "C - Asymmetric\nPartnership", "B - Digital\nFracture", "D - Contested\nSovereignty"],
        "prob_label_56": "Probability",
        "source_56": "Source: Author's construction - Section 5.7, baseline April 2026 (CACI 3.46:1)",
        "jurisdictions_57": ["United States", "China", "EU\n(workloads)", "UAE\n(installed)", "Singapore\n(installed)", "India\n(workloads)"],
        "label_pre_57": "CACI pre-Mandate (April 2026)",
        "label_post_57": "CACI post-Mandate (2028)",
        "ylabel_57": "CACI Power Mode Score (US = 100)",
        "title_57": "2028 Cloud Sovereignty Mandates Impact on CACI by Jurisdiction\n(Physical compute remains, but becomes legally conditional)",
        "source_57": "Source: Table 12 and Chap I Fig 1.8. UAE case illustrates max collapse (99.6% US-side).",
    },
    "FR": {
        "suffix": "FR",
        "baseline_label": f"baseline avril 2026\nCACI = {CACI_BASELINE_2026:.2f}:1",
        "convergence_2028": "Point de\nconvergence\n2028",
        "danger_zone": "Zone de decrochage\nirreversible",
        "title_51": "Trajectoires du ratio CACI(US)/CACI(UE) 2025-2030 par scenario\n(Power Mode, baseline 3,46:1 avril 2026)",
        "ylabel_51": "Ratio CACI(US) / CACI(UE)",
        "sc_names": ["A - Statu quo renforce", "B - Fracture numerique", "C - Partenariat asymetrique", "D - Souverainete contestee"],
        "source_51": "Source : construction de l'auteur - Section 5.7.1, calibration CACI",
        "title_52": "Chronologie des points de bascule 2026-2030 et fenetres decisionnelles",
        "decision_window": "Fenetre decisionnelle critique",
        "source_52": "Source : construction de l'auteur - Sections 5.7.2-5.7.3",
        "events": [
            ("Avr.\n2026", "Rapport Phase 1\nNegociations US-UE", "Modere\nvs agressif"),
            ("Juil.\n2026", "Rapport Commerce\nsemi data centers", "Extension\ntarifs ?"),
            ("2027", "Premieres Gigafactories\noperationnelles ?", "Proactif\nvs reactif"),
            ("2028", "POINT CRITIQUE\nDemande > Capacite UE", "Moment de\nverite"),
            ("2029-30", "Premiers SMR nucleaires\nDARE/RISC-V maturite ?", "Autonomie\na long terme"),
        ],
        "metrics_53": ["M1 Compute\nratio", "M2 Cout\nFLOP", "M3 Cloud\nUS (pct)", "M4 Product.\nUE (pct/an)", "M5 Energie\nUE (TWh)", "M6 CACI\nratio"],
        "scenarios_53": ["A\nStatu quo", "B\nFracture", "C\nPartenariat", "D\nSouverainete"],
        "title_53": "Synthese : 6 metriques x 4 scenarios (horizon 2030)",
        "cbar_label_53": "Severite pour l'UE\n(0 = favorable, 1 = critique)",
        "source_53": "Source : construction de l'auteur - Tableau 11",
        "title_54": "Les 4 elements predetermines (EP) structurant tous les scenarios",
        "ep_data": [
            ("EP1", "Croissance exponentielle\ndemande compute IA", "Ventes semis x2 en 2 ans\nPuces IA doublent / 7 mois"),
            ("EP2", "Concentration persistante\ncompute aux USA", f"Ratio brut {US_EU_RAW_OPERATIONAL_2025:.1f}:1 US/UE\nCACI Power Mode {CACI_BASELINE_2026:.2f}:1"),
            ("EP3", "Tension energetique\ncroissante", "415 -> 950 TWh (2024-2030)\nUE 1,4-1,7x cher (PPA)"),
            ("EP4", "Section 232\nen place", "Base legale confirmee\nRapport Commerce juil. 2026"),
        ],
        "source_54": "Source : construction de l'auteur - Section 5.1",
        "scenarios_55": ["Baseline\n2025", "A - Statu quo\n(2030)", "B - Fracture\n(2030)", "C - Partenariat\n(2030)", "D - Souverainete\n(2030)"],
        "xlabel_55": "Ratio compute brut US/UE (operationnel, equivalents H100)",
        "title_55": "Ratio compute installe US/UE (M1) - projection 2030 par scenario",
        "source_55": "Source : construction de l'auteur - Sections 5.3-5.6, baseline avril 2026",
        "title_56": "Matrice 2x2 actualisee : scenarios, probabilites et CACI 2030",
        "axis_labels_56": ["US MODERE", "UE PROACTIVE", "UE REACTIVE", "PROTECTIONNISME US", "MODERE", "AGRESSIF"],
        "quad_names_56": ["A - Statu quo\nrenforce", "C - Partenariat\nasymetrique", "B - Fracture\nnumerique", "D - Souverainete\ncontestee"],
        "prob_label_56": "Probabilite",
        "source_56": "Source : construction de l'auteur - Section 5.7, baseline avril 2026 (CACI 3,46:1)",
        "jurisdictions_57": ["Etats-Unis", "Chine", "UE\n(workloads)", "EAU\n(installe)", "Singapour\n(installe)", "Inde\n(workloads)"],
        "label_pre_57": "CACI pre-Mandate (avril 2026)",
        "label_post_57": "CACI post-Mandate (2028)",
        "ylabel_57": "Score CACI Power Mode (US = 100)",
        "title_57": "Impact des Cloud Sovereignty Mandates 2028 sur le CACI par juridiction\n(le compute physique reste, mais devient legalement conditionnel)",
        "source_57": "Source : Tableau 12 et chapitre I Fig 1.8. Le cas EAU illustre l'effondrement maximal (99,6 pct US-side).",
    },
    "PT-BR": {
        "suffix": "PT-BR",
        "baseline_label": f"base abril 2026\nCACI = {CACI_BASELINE_2026:.2f}:1",
        "convergence_2028": "Ponto de\nConvergencia\n2028",
        "danger_zone": "Zona de Desacoplamento\nIrreversivel",
        "title_51": "Trajetorias da Razao CACI(EUA)/CACI(UE) 2025-2030 por Cenario\n(Power Mode, base 3,46:1 abril 2026)",
        "ylabel_51": "Razao CACI(EUA) / CACI(UE)",
        "sc_names": ["A - Status Quo Reforcado", "B - Fratura Digital", "C - Parceria Assimetrica", "D - Soberania Contestada"],
        "source_51": "Fonte: Construcao do autor - Secao 5.7.1, calibracao CACI",
        "title_52": "Cronologia dos Pontos de Inflexao 2026-2030 e Janelas de Decisao",
        "decision_window": "Janela de Decisao Critica",
        "source_52": "Fonte: Construcao do autor - Secoes 5.7.2-5.7.3",
        "events": [
            ("Abr.\n2026", "Relatorio Fase 1\nNegociacoes EUA-UE", "Moderado\nvs Agressivo"),
            ("Jul.\n2026", "Relatorio Comercio\nSemi Data Centers", "Extensao\nTarifas?"),
            ("2027", "Primeiras Gigafactories\nOperacionais?", "Proativo\nvs Reativo"),
            ("2028", "PONTO CRITICO\nDemanda > Capacidade UE", "Momento da\nVerdade"),
            ("2029-30", "Primeiros SMR Nucleares\nDARE/RISC-V Maturidade?", "Autonomia\na Longo Prazo"),
        ],
        "metrics_53": ["M1 Razao\ncompute", "M2 Custo\nFLOP", "M3 Nuvem\nEUA (pct)", "M4 Produt.\nUE (pct/ano)", "M5 Energ.\nUE (TWh)", "M6 Razao\nCACI"],
        "scenarios_53": ["A\nStatus Quo", "B\nFratura", "C\nParceria", "D\nSoberania"],
        "title_53": "Sintese: 6 Metricas x 4 Cenarios (Horizonte 2030)",
        "cbar_label_53": "Severidade para a UE\n(0 = favoravel, 1 = critica)",
        "source_53": "Fonte: Construcao do autor - Tabela 11",
        "title_54": "Os 4 Elementos Predeterminados (EP) que Estruturam Todos os Cenarios",
        "ep_data": [
            ("EP1", "Crescimento Exponencial\nDemanda Compute IA", "Vendas semi x2 em 2 anos\nChips IA dobram / 7 meses"),
            ("EP2", "Concentracao Persistente\nCompute nos EUA", f"Razao bruta {US_EU_RAW_OPERATIONAL_2025:.1f}:1 EUA/UE\nCACI Power Mode {CACI_BASELINE_2026:.2f}:1"),
            ("EP3", "Tensao Energetica\nCrescente", "415 -> 950 TWh (2024-2030)\nUE 1,4-1,7x mais caro"),
            ("EP4", "Estrutura Secao 232\nem Vigor", "Base legal confirmada\nRelatorio Comercio Jul 2026"),
        ],
        "source_54": "Fonte: Construcao do autor - Secao 5.1",
        "scenarios_55": ["Baseline\n2025", "A - Status Quo\n(2030)", "B - Fratura\n(2030)", "C - Parceria\n(2030)", "D - Soberania\n(2030)"],
        "xlabel_55": "Razao de compute bruto EUA/UE (operacional, equivalentes H100)",
        "title_55": "Razao de Compute Instalado EUA/UE (M1) - Projecao 2030 por Cenario",
        "source_55": "Fonte: Construcao do autor - Secoes 5.3-5.6, base abril 2026",
        "title_56": "Matriz 2x2 Atualizada: Cenarios, Probabilidades e CACI 2030",
        "axis_labels_56": ["EUA MODERADO", "UE PROATIVA", "UE REATIVA", "PROTECIONISMO EUA", "MODERADO", "AGRESSIVO"],
        "quad_names_56": ["A - Status Quo\nReforcado", "C - Parceria\nAssimetrica", "B - Fratura\nDigital", "D - Soberania\nContestada"],
        "prob_label_56": "Probabilidade",
        "source_56": "Fonte: Construcao do autor - Secao 5.7, base abril 2026 (CACI 3,46:1)",
        "jurisdictions_57": ["Estados Unidos", "China", "UE\n(workloads)", "EAU\n(instalado)", "Cingapura\n(instalado)", "India\n(workloads)"],
        "label_pre_57": "CACI pre-Mandato (abril 2026)",
        "label_post_57": "CACI post-Mandato (2028)",
        "ylabel_57": "Score CACI Power Mode (EUA = 100)",
        "title_57": "Impacto dos Cloud Sovereignty Mandates 2028 no CACI por Jurisdicao\n(O compute fisico permanece, mas torna-se legalmente condicional)",
        "source_57": "Fonte: Tabela 12 e Cap I Fig 1.8. O caso EAU ilustra o colapso max (99,6% US-side).",
    }
}

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

def save_fig(fig, basename: str, lang_code: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    suffix = LANGS[lang_code]["suffix"]
    out = OUTPUT_DIR / f"{basename}_{suffix}.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    log.info("Saved %s", out)
    return out

# ===========================================================================
# Generators
# ===========================================================================

def fig1_caci_trajectories(lang: str) -> Path:
    D = LANGS[lang]
    fig, ax = plt.subplots(figsize=(13, 7.5))
    years = [2025, 2026, 2027, 2028, 2029, 2030]

    sc_a = [3.30, 3.46, 3.80, 4.20, 4.50, 4.50]
    sc_b = [3.30, 3.46, 4.50, 6.00, 7.00, 7.00]
    sc_c = [3.30, 3.46, 3.20, 2.80, 2.40, 2.25]
    sc_d = [3.30, 3.46, 6.50, 10.00, 7.50, 5.50]

    series = [
        (sc_a, SC_A, "o", D["sc_names"][0]),
        (sc_b, SC_B, "s", D["sc_names"][1]),
        (sc_c, SC_C, "D", D["sc_names"][2]),
        (sc_d, SC_D, "^", D["sc_names"][3]),
    ]

    for data, col, mk, label in series:
        ax.plot(years, data, color=col, linewidth=3, marker=mk, markersize=9, label=label, zorder=5)
        ax.text(years[-1] + 0.08, data[-1], f"{data[-1]:.1f}", fontsize=10, fontweight="bold", color=col, va="center", ha="left")

    ax.axhline(y=CACI_BASELINE_2026, color=GREY, linewidth=1, linestyle=":", alpha=0.6)
    ax.text(2025.05, CACI_BASELINE_2026 - 0.25, D["baseline_label"], fontsize=9, color=GREY, fontstyle="italic")

    ax.axvline(x=2028, color=ACCENT4, linewidth=1.5, linestyle="--", alpha=0.4)
    ax.text(2028.05, 0.6, D["convergence_2028"], fontsize=9, fontweight="bold", color=ACCENT4)

    ax.axhspan(8, 12, alpha=0.06, color=CN_COLOR)
    ax.text(2025.1, 11.0, D["danger_zone"], fontsize=10, fontweight="bold", color=CN_COLOR, fontstyle="italic")

    ax.set_title(D["title_51"], fontsize=14, fontweight="bold", color=NAVY, pad=15)
    ax.set_ylabel(D["ylabel_51"], fontsize=12)
    ax.set_xlim(2024.8, 2030.4)
    ax.set_ylim(0, 12)
    ax.set_xticks(years)
    ax.legend(fontsize=10, loc="upper left", framealpha=0.95)
    ax.grid(True, linestyle=":", alpha=0.4)

    fig.text(0.5, 0.01, D["source_51"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_5.1_CACI_Trajectories", lang)

def fig2_tipping_points(lang: str) -> Path:
    D = LANGS[lang]
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(7.5, 6.7, D["title_52"], ha="center", fontsize=14, fontweight="bold", color=NAVY)

    y_line = 3.5
    ax.plot([0.8, 14.2], [y_line, y_line], color="#333", linewidth=3, zorder=1)

    event_x = [1.8, 4.2, 6.8, 9.5, 12.5]
    colors = [ACCENT3, CN_COLOR, SC_C, SC_B, ACCENT2]

    for i, (ex, (date, desc, impact), col) in enumerate(zip(event_x, D["events"], colors)):
        y_off = 1.8 if i % 2 == 0 else -1.7
        y_text = y_line + y_off
        size = 16 if i == 3 else 12
        ax.plot(ex, y_line, "o", color=col, markersize=size, zorder=5)
        ax.plot(ex, y_line, "o", color="white", markersize=size - 5, zorder=6)
        ax.plot([ex, ex], [y_line, y_text + (0.3 if y_off > 0 else -0.3)], color=col, linewidth=1.5, linestyle="--", zorder=2)

        bw, bh = 2.4, 1.5
        rect = mpatches.FancyBboxPatch((ex - bw / 2, y_text - bh / 2), bw, bh, boxstyle="round,pad=0.1", facecolor=col, alpha=0.15, edgecolor=col, linewidth=1.8)
        ax.add_patch(rect)

        ax.text(ex, y_text + 0.45, date, ha="center", fontsize=10, fontweight="bold", color=col)
        ax.text(ex, y_text - 0.05, desc, ha="center", fontsize=8.5, color="#333")
        ax.text(ex, y_text - 0.55, impact, ha="center", fontsize=8, fontstyle="italic", color=col)

    ax.axvspan(1.5, 7.0, ymin=0.45, ymax=0.55, alpha=0.1, color=GOLD)
    ax.text(4.0, y_line + 0.05, D["decision_window"], ha="center", fontsize=9, fontweight="bold", color=GOLD, fontstyle="italic")

    ax.text(7.5, 0.3, D["source_52"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    return save_fig(fig, "Fig_5.2_Tipping_Points", lang)

def fig3_heatmap_synthesis(lang: str) -> Path:
    D = LANGS[lang]
    fig, ax = plt.subplots(figsize=(11, 7))

    metrics = D["metrics_53"]
    scenarios = D["scenarios_53"]

    data = np.array([
        [0.50, 1.00, 0.20, 0.40],
        [0.45, 1.00, 0.10, 0.35],
        [0.65, 0.95, 0.30, 0.05],
        [0.55, 1.00, 0.05, 0.40],
        [0.40, 0.10, 0.65, 0.95],
        [0.45, 1.00, 0.05, 0.55],
    ])

    im = ax.imshow(data, cmap="RdYlGn_r", aspect="auto", vmin=0, vmax=1)
    ax.set_xticks(np.arange(len(scenarios)))
    ax.set_xticklabels(scenarios, fontsize=10)
    ax.set_yticks(np.arange(len(metrics)))
    ax.set_yticklabels(metrics, fontsize=10)

    annotations = [
        ["18-22:1", "25-35:1", "8-10:1", "12-15:1"],
        ["2.4-3.2x", "4-6x", "1.5-2.0x", "1.8-2.5x"],
        ["72-75 pct", "78-82 pct", "60-65 pct", "50-55 pct"],
        ["+1.0-1.5", "+0.3-0.8", "+1.8-2.5", "+1.2-2.0"],
        ["~115", "~95", "~140", "~155"],
        ["4-5:1", "6-8:1", "2.0-2.5:1", "4-7:1"],
    ]

    for i in range(len(metrics)):
        for j in range(len(scenarios)):
            ax.text(j, i, annotations[i][j], ha="center", va="center", fontsize=9, fontweight="bold", color="white" if data[i, j] > 0.5 else "#222")

    ax.set_title(D["title_53"], fontsize=14, fontweight="bold", color=NAVY, pad=15)
    cbar = fig.colorbar(im, ax=ax, shrink=0.6, pad=0.03)
    cbar.set_label(D["cbar_label_53"], fontsize=9, rotation=270, labelpad=22)

    fig.text(0.5, 0.01, D["source_53"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_5.3_Heatmap_Synthesis", lang)

def fig4_predetermined_elements(lang: str) -> Path:
    D = LANGS[lang]
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(6, 7.4, D["title_54"], ha="center", fontsize=14, fontweight="bold", color=NAVY)

    colors = [US_COLOR, ACCENT3, ACCENT2, CN_COLOR]
    box_w, box_h = 2.6, 4.5
    x_starts = [0.4, 3.4, 6.4, 9.4]

    for x_start, (code, title, detail), col in zip(x_starts, D["ep_data"], colors):
        rect = mpatches.FancyBboxPatch((x_start, 1.0), box_w, box_h, boxstyle="round,pad=0.15", facecolor=col, alpha=0.12, edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        cx = x_start + box_w / 2
        ax.text(cx, 5.0, code, ha="center", fontsize=22, fontweight="bold", color=col)
        ax.text(cx, 4.0, title, ha="center", fontsize=11, fontweight="bold", color="#222", linespacing=1.3)
        ax.text(cx, 2.4, detail, ha="center", fontsize=10, color="#444", linespacing=1.4)

    ax.text(6, 0.3, D["source_54"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    return save_fig(fig, "Fig_5.4_Predetermined_Elements", lang)

def fig5_compute_ratio_per_scenario(lang: str) -> Path:
    D = LANGS[lang]
    fig, ax = plt.subplots(figsize=(11, 6.5))

    midpoints = [US_EU_RAW_OPERATIONAL_2025, 20, 30, 9, 13.5]
    colors = [GREY, SC_A, SC_B, SC_C, SC_D]
    labels = ["17.6:1", "18-22:1", "25-35:1", "8-10:1", "12-15:1"]

    y = np.arange(len(D["scenarios_55"]))
    bars = ax.barh(y, midpoints, color=colors, alpha=0.85, edgecolor="white", linewidth=1.5)

    for bar, mid, label in zip(bars, midpoints, labels):
        ax.text(mid + 0.5, bar.get_y() + bar.get_height() / 2, label, va="center", fontsize=11, fontweight="bold", color=bar.get_facecolor())

    ax.axvline(x=US_EU_RAW_OPERATIONAL_2025, color=GREY, linestyle=":", linewidth=1.5, alpha=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(D["scenarios_55"], fontsize=10)
    ax.invert_yaxis()
    ax.set_xlim(0, 38)
    ax.set_xlabel(D["xlabel_55"], fontsize=11)
    ax.set_title(D["title_55"], fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.grid(axis="x", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, D["source_55"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_5.5_Compute_Ratio_Per_Scenario", lang)

def fig6_matrix_probabilities(lang: str) -> Path:
    D = LANGS[lang]
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(5, 9.5, D["title_56"], ha="center", fontsize=14, fontweight="bold", color=NAVY)

    quad_data = [
        (0.8, 4.5, 4.0, 3.6, SC_A, D["quad_names_56"][0], "40-50 pct", "4-5:1"),
        (5.2, 4.5, 4.0, 3.6, SC_C, D["quad_names_56"][1], "15-20 pct", "2.0-2.5:1"),
        (0.8, 0.7, 4.0, 3.6, SC_B, D["quad_names_56"][2], "15-20 pct", "6-8:1"),
        (5.2, 0.7, 4.0, 3.6, SC_D, D["quad_names_56"][3], "15-20 pct", "4-7:1"),
    ]

    for x, y, w, h, col, name, prob, caci in quad_data:
        rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", facecolor=col, alpha=0.18, edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        cx, cy = x + w / 2, y + h / 2
        ax.text(cx, cy + 0.85, name, ha="center", fontsize=13, fontweight="bold", color=col, linespacing=1.3)
        ax.text(cx, cy - 0.2, f"{D['prob_label_56']} : {prob}", ha="center", fontsize=11, color="#333")
        ax.text(cx, cy - 0.95, f"CACI 2030 : {caci}", ha="center", fontsize=12, fontweight="bold", color=col, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=col, alpha=0.9))

    L = D["axis_labels_56"]
    ax.text(2.8, 8.3, L[0], ha="center", fontsize=11, fontweight="bold", color="#444")
    ax.text(7.2, 8.3, L[1], ha="center", fontsize=11, fontweight="bold", color="#444")
    ax.text(2.8, 4.4, L[2], ha="center", fontsize=11, fontweight="bold", color="#444")
    ax.text(0.4, 6.3, L[3], ha="center", fontsize=10, fontweight="bold", color="#444", rotation=90)
    ax.text(0.4, 2.5, L[3], ha="center", fontsize=10, fontweight="bold", color="#444", rotation=90)
    ax.text(0.6, 8.3, L[4], ha="center", fontsize=10, color="#666")
    ax.text(0.6, 0.5, L[5], ha="center", fontsize=10, color="#666")

    ax.text(5, 0.1, D["source_56"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    return save_fig(fig, "Fig_5.6_Matrix_Probabilities", lang)

def fig7_csm_impact(lang: str) -> Path:
    D = LANGS[lang]
    fig, ax = plt.subplots(figsize=(12, 7))

    pre = [100, 15.7, 28.9, 55.7, 50.0, 22.2]
    post = [100, 15.7, 28.9 * 0.60, 6.0, 50.0 * 0.30, 22.2 * 0.65]

    x = np.arange(len(D["jurisdictions_57"]))
    w = 0.36

    bars_pre = ax.bar(x - w / 2, pre, w, color=US_COLOR, alpha=0.6, label=D["label_pre_57"], edgecolor=US_COLOR, linewidth=1.5)
    bars_post = ax.bar(x + w / 2, post, w, color=CN_COLOR, alpha=0.85, label=D["label_post_57"], edgecolor=CN_COLOR, linewidth=1.5)

    for bar, val in zip(bars_pre, pre):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5, f"{val:.1f}" if val < 100 else "100", ha="center", fontsize=10, fontweight="bold", color=US_COLOR)
    for bar, val in zip(bars_post, post):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5, f"{val:.1f}" if val < 100 else "100", ha="center", fontsize=10, fontweight="bold", color=CN_COLOR)

    for i, (p, q) in enumerate(zip(pre, post)):
        gap = p - q
        if gap >= 5:
            ax.annotate(f"-{100*gap/p:.0f} pct", xy=(i, q + (p - q) / 2), xytext=(i + 0.45, q + (p - q) / 2), fontsize=9, color=CN_COLOR, fontweight="bold", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.2", facecolor="#FFF3E0", edgecolor=CN_COLOR, alpha=0.85))

    ax.set_xticks(x)
    ax.set_xticklabels(D["jurisdictions_57"], fontsize=10)
    ax.set_ylabel(D["ylabel_57"], fontsize=11)
    ax.set_ylim(0, 115)
    ax.set_title(D["title_57"], fontsize=13, fontweight="bold", color=NAVY, pad=15)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.text(0.5, 0.005, D["source_57"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return save_fig(fig, "Fig_5.7_CSM_Impact", lang)

# ===========================================================================
# Main
# ===========================================================================

FUNCS = [fig1_caci_trajectories, fig2_tipping_points, fig3_heatmap_synthesis, fig4_predetermined_elements, fig5_compute_ratio_per_scenario, fig6_matrix_probabilities, fig7_csm_impact]

def main() -> None:
    log.info("Output directory: %s", OUTPUT_DIR)
    _common_style()
    for lang in LANGS:
        log.info("Generating figures for language: %s", lang)
        for fn in FUNCS:
            fn(lang)
    log.info("Done. Total %d figures rendered.", len(LANGS) * len(FUNCS))

if __name__ == "__main__":
    main()
