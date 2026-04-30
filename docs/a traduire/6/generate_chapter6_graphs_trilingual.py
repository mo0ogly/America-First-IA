"""
Chapter VI - Trilingual Graph Generator (EN, FR, PT-BR).

Generates the figures for the 4 sub-chapters:
    6.X    France/Europe
    6bis.X South America / Brazil
    6ter.X Asia
    6quat.X Africa

All values are aligned with the April 2026 dashboard snapshot.
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
log = logging.getLogger("chapter6_graphs_trilingual")

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

# Labels Dictionary
LABELS = {
    "EN": {
        "source": "Source: Author's construction",
        "score_y": "Exposition Score (0-100)",
        "sectors": ["Finance", "Auto/Aero", "Health/Pharma", "Robotics/Indus.", "Defense/Space"],
        "sector_tags": ["Compute Intensity", "Data Sensitivity", "US Cloud Dep. (%)"],
        "fig61_title": "French Sectoral Exposure to AI Compute Asymmetry\n(Scenario B = Worst Case)",
        "fig62_title": "France Facing Three Futures (2030)",
        "fig62_c1": "Configuration 1\nDependent Consumer",
        "fig62_c1_b": "Scenarios A & B\n\nCACI ratio: 4-8:1\nUS Cloud: 75-82%\nEU Productivity: +0.3 to +1.5%/yr\nBrain drain: accelerated\nGDP Gap: -5 to -15 pts over 5 yrs",
        "fig62_c2": "Configuration 2\nEnergy & App Hub",
        "fig62_c2_b": "Scenario C\n\nCACI ratio: 2.0-2.5:1\nUS Cloud: 60-65%\nEU Productivity: +1.8 to +2.5%/yr\nMistral Compute + Gigafactories\nFrance as EU nuclear hub",
        "fig62_c3": "Configuration 3\nEU Sovereignty Pillar",
        "fig62_c3_b": "Scenario D\n\nCACI ratio: 4-7:1 (post-dip)\nUS Cloud: 50-55%\nEU Productivity: +1.2 to +2.0%/yr\n20 GW dedicated nuclear\nDARE/RISC-V + JP/KR/TW alliances",
        "fig6bis1_title": "Probabilities of Specific Scenarios for Brazil\nfacing US AI Protectionism",
        "fig6bis1_center": "BRAZIL\n2026-2030",
        "fig6bis1_labels": ["A' Neutral Dual Hub", "B' Secondary Sanctions", "C' Pro-US Alignment", "D' LATAM Sovereignty", "Hybrid Trajectories"],
        "fig6bis2_title": "AI Investment Deficit in Latin America\n(GDP/AI Invest Ratio = 5.9)",
        "fig6bis2_x": ["Global\nPop (%)", "Global\nGDP (%)", "Global\nAI Invest (%)", "Global\nAI DC Cap (%)"],
        "fig6bis2_legend": ["Latin America", "United States"],
        "fig6ter1_title": "Asian Position facing US AI Protectionism\n(Tier 1 = Green, Tier 2 = Orange, Tier 3 = Red)",
        "fig6ter1_x": ["Japan", "Taiwan", "Korea", "India", "China", "ASEAN", "Gulf (UAE)"],
        "fig6ter1_y": "Installed DC Capacity (GW)",
        "fig6ter1_legend": ["Tier 1 - Unlimited access", "Tier 2 - Quantitative caps", "Tier 3 - Prohibited access"],
        "fig6ter2_title": "Strategic Paradox: US Restrictions Accelerate Chinese Autonomy",
        "fig6ter2_y1": "AI Investment (B USD)",
        "fig6ter2_y2": "AI Capacity (EFLOP/s)",
        "fig6ter2_legend": ["China AI Investment (B USD)", "China AI Capacity (EFLOP/s)"],
        "fig6ter2_event": "October 2022\nBIS H100/A100\nBanned Tier 3",
        "fig6quat1_title": "African Compute Deficit: x44-x417 Asymmetry by Indicator",
        "fig6quat1_x": ["DC Capacity\n(GW)", "DC Invest.\n(B USD)", "AI GPUs\n(Thousands)", "AI Talent\n(% Global)", "AI Market\n(B USD)"],
        "fig6quat2_title": "US-China Rivalry in Africa: Strengths and Attack Vectors",
        "fig6quat2_x": ["Infrastructure\n(B USD)", "Trained Talent\n(M People)", "Coverage\n(% Continent)", "AI Models\n(Deployment)"],
    },
    "FR": {
        "source": "Source : construction de l'auteur",
        "score_y": "Score d'exposition (0-100)",
        "sectors": ["Finance", "Auto/Aero", "Sante/Pharma", "Robotique/Indus.", "Defense/Spatial"],
        "sector_tags": ["Intensite compute", "Sensibilite donnees", "Dep. Cloud US (%)"],
        "fig61_title": "Exposition sectorielle francaise a l'asymetrie de compute IA\n(scenario B = pire cas)",
        "fig62_title": "La France face a trois futurs (2030)",
        "fig62_c1": "Configuration 1\nConsommatrice dependante",
        "fig62_c1_b": "Scenarios A & B\n\nCACI ratio : 4-8:1\nCloud US : 75-82 pct\nProductivite UE : +0,3 a +1,5 pct/an\nBrain drain : accelere\nEcart PIB : -5 a -15 pts sur 5 ans",
        "fig62_c2": "Configuration 2\nHub energetique et applicatif",
        "fig62_c2_b": "Scenario C\n\nCACI ratio : 2,0-2,5:1\nCloud US : 60-65 pct\nProductivite UE : +1,8 a +2,5 pct/an\nMistral Compute + Gigafactories\nFrance hub nucleaire EU",
        "fig62_c3": "Configuration 3\nPilier souverainete UE",
        "fig62_c3_b": "Scenario D\n\nCACI ratio : 4-7:1 (post-creux)\nCloud US : 50-55 pct\nProductivite UE : +1,2 a +2,0 pct/an\n20 GW nucleaire dedie\nDARE/RISC-V + alliances JP/KR/TW",
        "fig6bis1_title": "Probabilites des scenarios specifiques pour le Bresil\nface au protectionnisme IA US",
        "fig6bis1_center": "BRESIL\n2026-2030",
        "fig6bis1_labels": ["A' Hub neutre dual", "B' Sanctions sec.", "C' Alignement pro-US", "D' Souverainete LATAM", "Trajectoires hybrides"],
        "fig6bis2_title": "Le deficit d'investissement IA en Amerique latine\n(le ratio PIB/Invest. IA = 5,9)",
        "fig6bis2_x": ["Population\nmondiale (%)", "PIB\nmondial (%)", "Invest. IA\nmondial (%)", "Cap. DC IA\nmondiale (%)"],
        "fig6bis2_legend": ["Amerique latine", "Etats-Unis"],
        "fig6ter1_title": "Position asiatique face au protectionnisme IA US\n(Tier 1 = vert, Tier 2 = orange, Tier 3 = rouge)",
        "fig6ter1_x": ["Japon", "Taiwan", "Coree", "Inde", "Chine", "ASEAN", "Golfe (EAU)"],
        "fig6ter1_y": "Capacite DC installee (GW)",
        "fig6ter1_legend": ["Tier 1 - acces illimite", "Tier 2 - caps quantitatifs", "Tier 3 - acces interdit"],
        "fig6ter2_title": "Le paradoxe strategique : les restrictions US accelerent l'autonomisation chinoise",
        "fig6ter2_y1": "Investissement IA (Md USD)",
        "fig6ter2_y2": "Capacite IA (EFLOP/s)",
        "fig6ter2_legend": ["Investissement IA Chine (Md USD)", "Capacite IA Chine (EFLOP/s)"],
        "fig6ter2_event": "Octobre 2022\nBIS H100/A100\ninterdites Tier 3",
        "fig6quat1_title": "Le deficit compute africain : asymetrie x44-x417 selon les indicateurs",
        "fig6quat1_x": ["Capacite DC\n(GW)", "Invest. DC\n(Md USD)", "GPU IA\n(milliers)", "Talent IA\n(% mondial)", "Marche IA\n(Md USD)"],
        "fig6quat2_title": "La rivalite US-Chine en Afrique : forces et angles d'attaque",
        "fig6quat2_x": ["Infrastructure\n(Md USD)", "Talents formes\n(M personnes)", "Couverture\n(% continent)", "Modeles IA\n(deploiement)"],
    },
    "PT-BR": {
        "source": "Fonte: Construcao do autor",
        "score_y": "Pontuacao de Exposicao (0-100)",
        "sectors": ["Financas", "Auto/Aero", "Saude/Pharma", "Robotica/Indus.", "Defesa/Espaco"],
        "sector_tags": ["Intensidade Compute", "Sensibilidade Dados", "Dep. Nuvem EUA (%)"],
        "fig61_title": "Exposicao Setorial Francesa a Assimetria de Computacao de IA\n(Cenario B = Pior Caso)",
        "fig62_title": "Franca Diante de Tres Futuros (2030)",
        "fig62_c1": "Configuracao 1\nConsumidora Dependente",
        "fig62_c1_b": "Cenarios A & B\n\nRazao CACI: 4-8:1\nNuvem EUA: 75-82%\nProdutividade UE: +0,3 a +1,5%/ano\nFuga de cerebros: acelerada\nLacuna PIB: -5 a -15 pts em 5 anos",
        "fig62_c2": "Configuracao 2\nHub de Energia e Aplicacoes",
        "fig62_c2_b": "Cenario C\n\nRazao CACI: 2,0-2,5:1\nNuvem EUA: 60-65%\nProdutividade UE: +1,8 a +2,5%/ano\nMistral Compute + Gigafactories\nFranca como hub nuclear da UE",
        "fig62_c3": "Configuracao 3\nPilar de Soberania da UE",
        "fig62_c3_b": "Cenario D\n\nRazao CACI: 4-7:1 (pos-queda)\nNuvem EUA: 50-55%\nProdutividade UE: +1,2 a +2,0%/ano\n20 GW nuclear dedicado\nDARE/RISC-V + aliancas JP/KR/TW",
        "fig6bis1_title": "Probabilidades de Cenarios Especificos para o Brasil\ndiante do Protecionismo de IA dos EUA",
        "fig6bis1_center": "BRASIL\n2026-2030",
        "fig6bis1_labels": ["A' Hub Neutro Dual", "B' Sancoes Sec.", "C' Alinhamento Pro-EUA", "D' Soberania LATAM", "Trajetorias Hibridas"],
        "fig6bis2_title": "Deficit de Investimento em IA na America Latina\n(Razao PIB/Invest. IA = 5,9)",
        "fig6bis2_x": ["Populacao\nMundial (%)", "PIB\nMundial (%)", "Invest. IA\nMundial (%)", "Cap. DC IA\nMundial (%)"],
        "fig6bis2_legend": ["America Latina", "Estados Unidos"],
        "fig6ter1_title": "Posicao Asiatica diante do Protecionismo de IA dos EUA\n(Tier 1 = Verde, Tier 2 = Laranja, Tier 3 = Vermelho)",
        "fig6ter1_x": ["Japao", "Taiwan", "Coreia", "India", "China", "ASEAN", "Golfo (EAU)"],
        "fig6ter1_y": "Capacidade DC Instalada (GW)",
        "fig6ter1_legend": ["Tier 1 - Acesso ilimitado", "Tier 2 - Limites quantitativos", "Tier 3 - Acesso proibido"],
        "fig6ter2_title": "O Paradoxo Estrategico: Restricoes dos EUA Aceleram Autonomia Chinesa",
        "fig6ter2_y1": "Investimento em IA (Bi USD)",
        "fig6ter2_y2": "Capacidade de IA (EFLOP/s)",
        "fig6ter2_legend": ["Investimento em IA China (Bi USD)", "Capacidade de IA China (EFLOP/s)"],
        "fig6ter2_event": "Outubro 2022\nBIS H100/A100\nProibidas Tier 3",
        "fig6quat1_title": "Deficit de Computacao Africano: Assimetria x44-x417 por Indicador",
        "fig6quat1_x": ["Capacidade DC\n(GW)", "Invest. DC\n(Bi USD)", "GPUs de IA\n(Milhares)", "Talento IA\n(% Global)", "Mercado de IA\n(Bi USD)"],
        "fig6quat2_title": "Rivalidade EUA-China na Africa: Forcas e Vetores de Ataque",
        "fig6quat2_x": ["Infraestrutura\n(Bi USD)", "Talento Treinado\n(M Pessoas)", "Cobertura\n(% Continente)", "Modelos de IA\n(Implantacao)"],
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

def save_fig(fig, basename: str, lang: str, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{basename}_{lang}.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    log.info("Saved %s", out)
    return out

# --- Figure Generators ---

def gen_fig_6_1(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(11, 6.5))
    intensity = [85, 95, 70, 80, 95]
    data_sens = [95, 80, 100, 60, 100]
    cloud_dep = [75, 65, 50, 58, 50]
    x = np.arange(len(L["sectors"]))
    w = 0.27
    bars1 = ax.bar(x - w, intensity, w, label=L["sector_tags"][0], color=US_COLOR, alpha=0.85)
    bars2 = ax.bar(x, data_sens, w, label=L["sector_tags"][1], color=GOLD, alpha=0.85)
    bars3 = ax.bar(x + w, cloud_dep, w, label=L["sector_tags"][2], color=CN_COLOR, alpha=0.85)
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{int(bar.get_height())}", ha="center", fontsize=9, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(L["sectors"], fontsize=10)
    ax.set_ylabel(L["score_y"], fontsize=11)
    ax.set_ylim(0, 115)
    ax.set_title(L["fig61_title"], fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    fig.text(0.5, 0.005, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_6.1_Sectoral_Exposure_France", lang, out_dir)

def gen_fig_6_2(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(13, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.text(6, 7.5, L["fig62_title"], ha="center", fontsize=15, fontweight="bold", color=NAVY)
    configs = [
        (0.4, L["fig62_c1"], L["fig62_c1_b"], CN_COLOR),
        (4.4, L["fig62_c2"], L["fig62_c2_b"], ACCENT1),
        (8.4, L["fig62_c3"], L["fig62_c3_b"], ACCENT2),
    ]
    box_w, box_h = 3.4, 5.5
    for x, title, body, col in configs:
        rect = mpatches.FancyBboxPatch((x, 0.8), box_w, box_h, boxstyle="round,pad=0.15", facecolor=col, alpha=0.12, edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + box_w / 2, 5.6, title, ha="center", fontsize=12, fontweight="bold", color=col, linespacing=1.3)
        ax.text(x + box_w / 2, 3.2, body, ha="center", fontsize=9.5, color="#333", linespacing=1.5)
    ax.text(6, 0.2, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_6.2_Three_Configurations_France", lang, out_dir)

def gen_fig_6bis_1(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(10, 8))
    sizes = [40, 17, 22, 12, 9]
    colors = ["#3498DB", "#E74C3C", "#27AE60", "#8E44AD", GREY]
    explode = [0.04, 0.04, 0.04, 0.04, 0]
    ax.pie(sizes, labels=L["fig6bis1_labels"], colors=colors, autopct="%1.0f %%", explode=explode, startangle=90, wedgeprops=dict(width=0.5, edgecolor="white", linewidth=2), textprops={"fontsize": 10})
    ax.text(0, 0, L["fig6bis1_center"], ha="center", va="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.set_title(L["fig6bis1_title"], fontsize=13, fontweight="bold", color=NAVY, pad=20)
    fig.text(0.5, 0.02, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_6bis.1_Brazil_Scenarios", lang, out_dir)

def gen_fig_6bis_2(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(10, 6))
    latam = [8.4, 6.6, 1.12, 1.5]
    us = [4.2, 25.5, 65, 76.9]
    x = np.arange(len(L["fig6bis2_x"]))
    w = 0.35
    b1 = ax.bar(x - w / 2, latam, w, color=ACCENT3, label=L["fig6bis2_legend"][0])
    b2 = ax.bar(x + w / 2, us, w, color=US_COLOR, label=L["fig6bis2_legend"][1])
    for bars, col in [(b1, ACCENT3), (b2, US_COLOR)]:
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{bar.get_height():.1f}%", ha="center", fontsize=10, fontweight="bold", color=col)
    ax.set_xticks(x)
    ax.set_xticklabels(L["fig6bis2_x"], fontsize=10)
    ax.set_ylabel("Global Share (%)", fontsize=11)
    ax.set_ylim(0, 92)
    ax.set_title(L["fig6bis2_title"], fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, framealpha=0.9, loc="upper left")
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    fig.text(0.5, 0.005, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_6bis.2_LATAM_Deficit", lang, out_dir)

def gen_fig_6ter_1(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(13, 7))
    tiers = [1, 1, 1, 2, 3, 2, 2]
    dc_capacity = [12.8, 3.0, 5.0, 1.4, 19.6, 3.0, 2.0]
    investment = [135, 40, 6.7, 200, 125, 15, 20]
    tier_colors = {1: ACCENT1, 2: ACCENT3, 3: CN_COLOR}
    colors = [tier_colors[t] for t in tiers]
    x = np.arange(len(L["fig6ter1_x"]))
    bars = ax.bar(x, dc_capacity, color=colors, alpha=0.85)
    for i, (bar, tier, inv, cap) in enumerate(zip(bars, tiers, investment, dc_capacity)):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.4, f"Tier {tier}\n{inv} B USD", ha="center", fontsize=9, fontweight="bold", color=bar.get_facecolor())
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f"{cap} GW", ha="center", va="center", fontsize=11, fontweight="bold", color="white")
    ax.set_xticks(x)
    ax.set_xticklabels(L["fig6ter1_x"], fontsize=10)
    ax.set_ylabel(L["fig6ter1_y"], fontsize=11)
    ax.set_ylim(0, 25)
    ax.set_title(L["fig6ter1_title"], fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    legend_elements = [mpatches.Patch(color=c, label=l) for c, l in zip([ACCENT1, ACCENT3, CN_COLOR], L["fig6ter1_legend"])]
    ax.legend(handles=legend_elements, fontsize=10, loc="upper left", framealpha=0.9)
    fig.text(0.5, 0.005, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_6ter.1_Asia_Tiers", lang, out_dir)

def gen_fig_6ter_2(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(11, 6))
    years = [2022, 2023, 2024, 2025, 2026]
    cn_invest = [40, 60, 90, 125, 195]
    cn_efflops = [120, 160, 220, 280, 340]
    ax_right = ax.twinx()
    l1 = ax.plot(years, cn_invest, color=CN_COLOR, linewidth=3, marker="o", label=L["fig6ter2_legend"][0])
    l2 = ax_right.plot(years, cn_efflops, color=US_COLOR, linewidth=3, marker="s", linestyle="--", label=L["fig6ter2_legend"][1])
    ax.axvline(x=2022.8, color=GREY, linestyle=":", alpha=0.6)
    ax.text(2022.85, 175, L["fig6ter2_event"], fontsize=8.5, color=GREY, fontstyle="italic")
    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel(L["fig6ter2_y1"], fontsize=11, color=CN_COLOR)
    ax_right.set_ylabel(L["fig6ter2_y2"], fontsize=11, color=US_COLOR)
    ax.set_ylim(0, 220)
    ax_right.set_ylim(0, 380)
    ax.set_xticks(years)
    ax.set_title(L["fig6ter2_title"], fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(l1+l2, [l.get_label() for l in l1+l2], fontsize=10, loc="upper left")
    fig.text(0.5, 0.005, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_6ter.2_China_Paradox", lang, out_dir)

def gen_fig_6quat_1(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(11, 6))
    africa = [1.0, 2.0, 12.0, 3.0, 4.5]
    us = [53.7, 675.0, 5000.0, 40.0, 200.0]
    ratios = [54, 338, 417, 13, 44]
    x = np.arange(len(L["fig6quat1_x"]))
    w = 0.35
    ax.bar(x - w / 2, africa, w, color=ACCENT3, label=lang=="FR" and "Afrique" or (lang=="PT-BR" and "Africa" or "Africa"))
    ax.bar(x + w / 2, us, w, color=US_COLOR, label=lang=="FR" and "Etats-Unis" or (lang=="PT-BR" and "Estados Unidos" or "United States"))
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(L["fig6quat1_x"], fontsize=10)
    ax.set_title(L["fig6quat1_title"], fontsize=13, fontweight="bold", color=NAVY, pad=14)
    for i, r in enumerate(ratios):
        ax.text(i, us[i] * 1.5, f"x{r}", ha="center", fontsize=11, fontweight="bold", color=CN_COLOR)
    ax.legend(fontsize=10, loc="upper left")
    fig.text(0.5, 0.005, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_6quat.1_Africa_Deficit", lang, out_dir)

def gen_fig_6quat_2(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(11, 6))
    us_score = [3.7, 7.0, 25, 30]
    cn_score = [0.3, 0.12, 70, 60]
    x = np.arange(len(L["fig6quat2_x"]))
    w = 0.35
    ax.bar(x - w / 2, us_score, w, color=US_COLOR, label=lang=="FR" and "Etats-Unis" or (lang=="PT-BR" and "Estados Unidos" or "United States"))
    ax.bar(x + w / 2, cn_score, w, color=CN_COLOR, label=lang=="FR" and "Chine" or (lang=="PT-BR" and "China" or "China"))
    ax.set_xticks(x)
    ax.set_xticklabels(L["fig6quat2_x"], fontsize=10)
    ax.set_title(L["fig6quat2_title"], fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, loc="upper right")
    fig.text(0.5, 0.005, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_6quat.2_US_China_Africa", lang, out_dir)

def main() -> None:
    _common_style()
    out_dir = Path("./figures_ch6").resolve()
    for lang in ["EN", "FR", "PT-BR"]:
        log.info("Generating Chapter VI graphs for: %s", lang)
        gen_fig_6_1(lang, out_dir)
        gen_fig_6_2(lang, out_dir)
        gen_fig_6bis_1(lang, out_dir)
        gen_fig_6bis_2(lang, out_dir)
        gen_fig_6ter_1(lang, out_dir)
        gen_fig_6ter_2(lang, out_dir)
        gen_fig_6quat_1(lang, out_dir)
        gen_fig_6quat_2(lang, out_dir)

if __name__ == "__main__":
    main()
