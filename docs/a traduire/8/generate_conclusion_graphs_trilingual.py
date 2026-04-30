"""
Conclusion - Trilingual Synthesis Graph Generator (EN, FR, PT-BR).

Generates a single visual synthesis figure of the study:
the chapter timeline with their main contributions and the narrative arc
of the thesis (from empirical diagnosis to the 2030 trajectory).

Author: Fabrice Pizzi (Université Paris-Sorbonne, M2 Intelligence Économique).
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
log = logging.getLogger("conclusion_graphs_trilingual")

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

DPI = 300

LABELS = {
    "EN": {
        "title": "AI for Americans First: Thesis Synthesis",
        "subtitle": "From April 2026 Empirical Diagnosis to 2030 Trajectory",
        "stages": [
            ("DIAGNOSTIC", "Chap I: Theoretical Framework\nChap II: CACI Power Mode\nChap III: April 2026 Snapshot\n\nF(USA) = 76.9%\nF(EU) = 3.3%\nRaw Ratio 17.6:1\nCACI 3.46:1\nEU/US PPP 1.59x", US_COLOR),
            ("MECHANISMS", "Chap IV: US Advantage\n\nInstalled Compute 76.9%\nCapex 660-690 B USD/yr\nEnergy PPP 1.59x\n\n+ Phys/Sov (Chap I)\nEU 99.2% sovereign\nUAE 99.6% US-side\n(CACI 56 to 6)", CN_COLOR),
            ("SCENARIOS 2030", "Chap V: 4 Scenarios\n+ Cloud Sovereignty\nMandates 2028\n\nA Status quo: 4-5:1\nB Fracture: 6-8:1\nC Partnership: 2.0-2.5:1\nD Sovereignty: 4-7:1 (U)", ACCENT2),
            ("RESPONSE FR/EU", "Chap VI/bis/ter/quater\nChap VII Recommendations\n\n5 Axes: compute, energy,\nalliances, regulation,\ntalent\n\nEU F_sov 22% (2026)\nto 70% (2030)\nWindow 2026-2028", ACCENT1),
        ],
        "contrib_title": "5 Contributions to the literature",
        "contributions": [
            ("1. Analytical Integration", "Energy + Semiconductors\n+ Compute + Regulation\n+ Productivity unified", GOLD),
            ("2. CACI Index", "Geometric Power Mode\nF^0.40 L^0.20 R^0.15 / E^0.25\n+ Phys/Sov extension", GOLD),
            ("3. Paradoxical Effects", "US restrictions accelerate\nChinese autonomy\n+ Tier 1 co-finances US", GOLD),
            ("4. Regional Comparison", "Europe / S. America /\nAsia / Africa: 4 distinct\ndependency trajectories", GOLD),
            ("5. Africa Extension", "Deficit x44 to x417\nUS/China Double bind\nUA Phase II 2028 Window", GOLD),
        ],
        "footer": "Source: Doctoral thesis Fabrice Pizzi (Université Paris-Sorbonne, M2 IE). Dashboard: https://mo0ogly.github.io/America-First-IA/dashboard/"
    },
    "FR": {
        "title": "AI for Americans First : synthese de la these",
        "subtitle": "Du diagnostic empirique avril 2026 a la trajectoire 2030",
        "stages": [
            ("DIAGNOSTIC", "Chap I : Cadre theorique\nChap II : CACI Power Mode\nChap III : Snapshot avril 2026\n\nF(USA) = 76,9 pct\nF(UE) = 3,3 pct\nRatio brut 17,6:1\nCACI 3,46:1\nPPA UE/US 1,59x", US_COLOR),
            ("MECANISMES", "Chap IV : Avantage US\n\nCompute installe 76,9 pct\nCapex 660-690 Md USD/an\nEnergie PPA 1,59x\n\n+ Phys/Sov (Chap I)\nUE 99,2 pct souverain\nEAU 99,6 pct US-side\n(CACI 56 vers 6)", CN_COLOR),
            ("SCENARIOS 2030", "Chap V : 4 scenarios\n+ Cloud Sovereignty\nMandates 2028\n\nA Statu quo : 4-5:1\nB Fracture : 6-8:1\nC Partenariat : 2,0-2,5:1\nD Souverainete : 4-7:1 (U)", ACCENT2),
            ("REPONSE FR/EU", "Chap VI/bis/ter/quater\nChap VII Recommandations\n\n5 axes : compute, energie,\nalliances, regulation,\ntalent\n\nF_sov UE 22 pct (2026)\nvers 70 pct (2030)\nFenetre 2026-2028", ACCENT1),
        ],
        "contrib_title": "5 contributions a la litterature",
        "contributions": [
            ("1. Integration analytique", "Energie + semi-conducteurs\n+ compute + regulation\n+ productivite unifies", GOLD),
            ("2. Indice CACI", "Power Mode geometrique\nF^0,40 L^0,20 R^0,15 / E^0,25\n+ extension Phys/Sov", GOLD),
            ("3. Effets paradoxaux", "Restrictions US accelerent\nautonomisation chinoise\n+ Tier 1 cofinance US", GOLD),
            ("4. Comparatif regional", "Europe / Am. du Sud /\nAsie / Afrique : 4 trajectoires\nde dependance distinctes", GOLD),
            ("5. Extension Afrique", "Deficit x44 a x417\nDouble bind US/Chine\nFenetre UA Phase II 2028", GOLD),
        ],
        "footer": "Source : these doctorale Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique). Tableau de bord public : https://mo0ogly.github.io/America-First-IA/dashboard/"
    },
    "PT-BR": {
        "title": "AI for Americans First: Sintese da Tese",
        "subtitle": "Do Diagnostico Empirico de Abril de 2026 a Trajetoria de 2030",
        "stages": [
            ("DIAGNOSTICO", "Cap I: Quadro Teorico\nCap II: CACI Power Mode\nCap III: Snapshot Abril 2026\n\nF(EUA) = 76,9%\nF(UE) = 3,3%\nRazao Bruta 17,6:1\nCACI 3,46:1\nPPP UE/EUA 1,59x", US_COLOR),
            ("MECANISMOS", "Cap IV: Vantagem dos EUA\n\nCompute Instalado 76,9%\nCapex 660-690 Bi USD/ano\nEnergia PPP 1,59x\n\n+ Phys/Sov (Cap I)\nUE 99,2% soberana\nEAU 99,6% lado EUA\n(CACI 56 para 6)", CN_COLOR),
            ("CENARIOS 2030", "Cap V: 4 Cenarios\n+ Mandatos de\nSoberania de Nuvem 2028\n\nA Status quo: 4-5:1\nB Fratura: 6-8:1\nC Parceria: 2,0-2,5:1\nD Soberania: 4-7:1 (U)", ACCENT2),
            ("RESPOSTA FR/UE", "Cap VI/bis/ter/quater\nCap VII Recomendacoes\n\n5 Eixos: compute, energia,\naliancas, regulamentacao,\ntalento\n\nEU F_sov 22% (2026)\npara 70% (2030)\nJanela 2026-2028", ACCENT1),
        ],
        "contrib_title": "5 contribuicoes para a literatura",
        "contributions": [
            ("1. Integracao Analitica", "Energia + Semicondutores\n+ Compute + Regulamentacao\n+ Produtividade unificada", GOLD),
            ("2. Indice CACI", "Power Mode Geometrico\nF^0,40 L^0,20 R^0,15 / E^0,25\n+ extensao Phys/Sov", GOLD),
            ("3. Efeitos Paradoxais", "Restricoes dos EUA aceleram\nautonomia chinesa\n+ Tier 1 cofinancia EUA", GOLD),
            ("4. Comparacao Regional", "Europa / Am. do Sul /\nAsia / Africa: 4 trajetorias\nde dependencia distintas", GOLD),
            ("5. Extensao Africa", "Deficit x44 a x417\nDouble bind EUA/China\nJanela UA Fase II 2028", GOLD),
        ],
        "footer": "Fonte: Tese de doutorado Fabrice Pizzi (Universite Paris-Sorbonne, M2 IE). Painel: https://mo0ogly.github.io/America-First-IA/dashboard/"
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
        "axes.spines.top": False,
        "axes.spines.right": False,
    })

def save_fig(fig, basename: str, lang: str, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{basename}_{lang}.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    log.info("Saved %s", out)
    return out

def gen_fig_synthese(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis("off")

    ax.text(8, 10.4, L["title"], ha="center", fontsize=17, fontweight="bold", color=NAVY)
    ax.text(8, 9.85, L["subtitle"], ha="center", fontsize=12, fontstyle="italic", color=GREY)

    box_w, box_h = 3.2, 4.4
    for i, (title, body, col) in enumerate(L["stages"]):
        x = 0.5 + i * 3.5
        y = 7.0
        rect = mpatches.FancyBboxPatch((x, y - box_h / 2 - 0.2), box_w, box_h, boxstyle="round,pad=0.15", facecolor=col, alpha=0.13, edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + box_w / 2, y + 1.7, title, ha="center", fontsize=12, fontweight="bold", color=col)
        ax.text(x + box_w / 2, y - 0.6, body, ha="center", fontsize=8.5, color="#222", linespacing=1.45)

    # Arrows
    for i in range(3):
        x_start = 0.5 + i * 3.5 + 3.2
        x_end = 0.5 + (i+1) * 3.5
        ax.annotate("", xy=(x_end, 7.0), xytext=(x_start, 7.0), arrowprops=dict(arrowstyle="->", color=GREY, lw=2))

    ax.text(8, 4.0, L["contrib_title"], ha="center", fontsize=12, fontweight="bold", color=NAVY, fontstyle="italic")

    box_w2, box_h2 = 2.7, 2.4
    for i, (title, body, col) in enumerate(L["contributions"]):
        x = 0.4 + i * 3.0
        rect = mpatches.FancyBboxPatch((x, 1.2), box_w2, box_h2, boxstyle="round,pad=0.12", facecolor=col, alpha=0.13, edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + box_w2 / 2, 3.05, title, ha="center", fontsize=10, fontweight="bold", color=col)
        ax.text(x + box_w2 / 2, 1.95, body, ha="center", fontsize=8.0, color="#222", linespacing=1.4)

    ax.text(8, 0.4, L["footer"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_Conclusion_Synthese", lang, out_dir)

def main() -> None:
    _common_style()
    out_dir = Path("./figures_conclusion").resolve()
    for lang in ["EN", "FR", "PT-BR"]:
        log.info("Generating Conclusion synthesis graph for: %s", lang)
        gen_fig_synthese(lang, out_dir)

if __name__ == "__main__":
    main()
