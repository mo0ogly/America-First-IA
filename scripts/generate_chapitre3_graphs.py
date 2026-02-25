#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre III : Diagnostic Empirique 2020-2026
 Générateur de graphiques en 3 langues (FR / EN / PT-BR)
=============================================================================
 Usage  : python generate_chapitre3_graphs.py
 Output : PNG files in ./output/figures_ch3/
=============================================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
DPI = 300

# Couleurs
US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
CN_COLOR = "#C0392B"
FR_COLOR = "#2E86C1"
ACCENT1 = "#148F77"
ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"
REST_COLOR = "#95A5A6"
BG_COLOR = "#FAFBFC"
GRID_COLOR = "#E0E0E0"

LANGS = {
    "fr": {
        "suffix": "FR",
        # Fig 3.1 — Conso data centers par région
        "f1_title": "Consommation électrique des data centers par région\n(2020–2030, TWh)",
        "f1_ylabel": "TWh / an",
        "f1_us": "États-Unis", "f1_cn": "Chine", "f1_eu": "UE", "f1_rest": "Reste du monde",
        "f1_source": "Source : IEA Energy and AI (2025), Tableau 4 du chapitre",
        "f1_proj": "← Projection →",

        # Fig 3.2 — Ventes semi-conducteurs
        "f2_title": "Ventes mondiales de semi-conducteurs 2020–2026\n(Md$, SIA/WSTS)",
        "f2_ylabel": "Milliards USD",
        "f2_logic": "Puces logiques (GPU, CPU, ASIC)",
        "f2_memory": "Mémoires (DRAM, NAND)",
        "f2_other": "Autres (analogique, discret, capteurs)",
        "f2_source": "Sources : SIA/WSTS (fév. 2026), Tableau 5 du chapitre",
        "f2_growth": "Croissance annuelle",

        # Fig 3.3 — Répartition compute GPU
        "f3_title": "Répartition géographique de la performance\ndes clusters GPU (2019–2025)",
        "f3_ylabel": "Part de la performance mondiale (%)",
        "f3_us": "États-Unis", "f3_cn": "Chine", "f3_eu": "UE", "f3_rest": "Reste du monde",
        "f3_source": "Sources : Epoch AI / Pilz et al. (2025), GeoCoded/Sanchez (2025)",
        "f3_note": "Ratio US/EU ≈ 15:1 en 2025",

        # Fig 3.4 — Frise chronologique réglementaire
        "f4_title": "Chronologie des mesures US sur les semi-conducteurs et l'IA\n(2022–2026) : de l'export control au protectionnisme tarifaire",
        "f4_events": [
            ("Oct.\n2022", "Export controls BIS\nGPU avancés, SME\nCible : Chine", "Biden"),
            ("Oct.\n2023", "Renforcement seuils\n+40 pays, A800/H800\ncapturés", "Biden"),
            ("Déc.\n2024", "Vague 3 : 24 types SME\nHBM, 140 entités", "Biden"),
            ("Janv.\n2025", "AI Diffusion Rule\nModèles + Cloud\n120 pays, 3 tiers", "Biden"),
            ("Juil.\n2025", "America's AI\nAction Plan\nDérégulation US", "Trump"),
            ("Janv.\n2026", "Section 232\nTarif 25% GPU\nExemption US", "Trump"),
        ],
        "f4_source": "Sources : BIS, White House, Pillsbury Law (2026), Gibson Dunn (2026)",
        "f4_phase_d": "Denial strategy\n(déni d'accès)",
        "f4_phase_c": "Capture strategy\n(protectionnisme offensif)",

        # Fig 3.5 — Calibration CACI
        "f5_title": "Calibration du CACI : décomposition de l'avantage US\n(2024–2025)",
        "f5_components": ["Compute\ninstallé\n(F ratio)", "Coût\nénergétique\n(E ratio)", "CACI\nrésultant\n(fourchette)"],
        "f5_ylabel": "Ratio US / EU",
        "f5_source": "Élaboration auteur — Section 3.3.3, données Epoch AI, IEA, Eurostat",

        # Fig 3.6 — Synthèse indicateurs domination US
        "f6_title": "Synthèse : indicateurs de la domination US\nen compute IA (2024–2025)",
        "f6_indicators": ["Performance\nclusters GPU", "Secteur privé\ncompute IA", "Consommation\ndata centers",
                          "Investissement\nIA 2025", "Puissance\npuces IA"],
        "f6_us_vals": [75, 65, 45, 85, 70],
        "f6_eu_vals": [5, 3, 15, 5, 4],
        "f6_cn_vals": [15, 12, 25, 8, 18],
        "f6_ylabel": "Part mondiale (%)",
        "f6_source": "Sources : Epoch AI, IEA, GeoCoded/Sanchez, estimations auteur",
    },
    "en": {
        "suffix": "EN",
        "f1_title": "Data Center Electricity Consumption by Region\n(2020–2030, TWh)",
        "f1_ylabel": "TWh / year",
        "f1_us": "United States", "f1_cn": "China", "f1_eu": "EU", "f1_rest": "Rest of world",
        "f1_source": "Source: IEA Energy and AI (2025), Chapter Table 4",
        "f1_proj": "← Projection →",

        "f2_title": "Global Semiconductor Sales 2020–2026\n(Bn$, SIA/WSTS)",
        "f2_ylabel": "Billion USD",
        "f2_logic": "Logic chips (GPU, CPU, ASIC)",
        "f2_memory": "Memory (DRAM, NAND)",
        "f2_other": "Other (analog, discrete, sensors)",
        "f2_source": "Sources: SIA/WSTS (Feb. 2026), Chapter Table 5",
        "f2_growth": "Annual growth",

        "f3_title": "Geographic Distribution of GPU Cluster\nPerformance (2019–2025)",
        "f3_ylabel": "Share of global performance (%)",
        "f3_us": "United States", "f3_cn": "China", "f3_eu": "EU", "f3_rest": "Rest of world",
        "f3_source": "Sources: Epoch AI / Pilz et al. (2025), GeoCoded/Sanchez (2025)",
        "f3_note": "US/EU ratio ≈ 15:1 in 2025",

        "f4_title": "Timeline of US Semiconductor & AI Measures\n(2022–2026): From Export Controls to Tariff Protectionism",
        "f4_events": [
            ("Oct.\n2022", "BIS Export Controls\nAdvanced GPUs, SME\nTarget: China", "Biden"),
            ("Oct.\n2023", "Threshold update\n+40 countries, A800/H800\ncaptured", "Biden"),
            ("Dec.\n2024", "Wave 3: 24 SME types\nHBM, 140 entities", "Biden"),
            ("Jan.\n2025", "AI Diffusion Rule\nModels + Cloud\n120 countries, 3 tiers", "Biden"),
            ("Jul.\n2025", "America's AI\nAction Plan\nUS deregulation", "Trump"),
            ("Jan.\n2026", "Section 232\n25% GPU tariff\nUS exemption", "Trump"),
        ],
        "f4_source": "Sources: BIS, White House, Pillsbury Law (2026), Gibson Dunn (2026)",
        "f4_phase_d": "Denial strategy\n(access denial)",
        "f4_phase_c": "Capture strategy\n(offensive protectionism)",

        "f5_title": "CACI Calibration: Decomposition of US Advantage\n(2024–2025)",
        "f5_components": ["Installed\ncompute\n(F ratio)", "Energy\ncost\n(E ratio)", "Resulting\nCACI\n(range)"],
        "f5_ylabel": "US / EU Ratio",
        "f5_source": "Author's elaboration — Section 3.3.3, Epoch AI, IEA, Eurostat data",

        "f6_title": "Summary: US Dominance Indicators\nin AI Compute (2024–2025)",
        "f6_indicators": ["GPU cluster\nperformance", "Private sector\nAI compute", "Data center\nconsumption",
                          "AI investment\n2025", "AI chip\npower"],
        "f6_us_vals": [75, 65, 45, 85, 70],
        "f6_eu_vals": [5, 3, 15, 5, 4],
        "f6_cn_vals": [15, 12, 25, 8, 18],
        "f6_ylabel": "Global share (%)",
        "f6_source": "Sources: Epoch AI, IEA, GeoCoded/Sanchez, author estimates",
    },
    "pt": {
        "suffix": "PT-BR",
        "f1_title": "Consumo de Eletricidade em Data Centers por Região\n(2020–2030, TWh)",
        "f1_ylabel": "TWh / ano",
        "f1_us": "Estados Unidos", "f1_cn": "China", "f1_eu": "UE", "f1_rest": "Resto do mundo",
        "f1_source": "Fonte: IEA Energy and AI (2025), Tabela 4 do capítulo",
        "f1_proj": "← Projeção →",

        "f2_title": "Vendas Globais de Semicondutores 2020–2026\n(Bi$, SIA/WSTS)",
        "f2_ylabel": "Bilhões USD",
        "f2_logic": "Chips lógicos (GPU, CPU, ASIC)",
        "f2_memory": "Memórias (DRAM, NAND)",
        "f2_other": "Outros (analógico, discreto, sensores)",
        "f2_source": "Fontes: SIA/WSTS (fev. 2026), Tabela 5 do capítulo",
        "f2_growth": "Crescimento anual",

        "f3_title": "Distribuição Geográfica do Desempenho\ndos Clusters GPU (2019–2025)",
        "f3_ylabel": "Participação no desempenho global (%)",
        "f3_us": "Estados Unidos", "f3_cn": "China", "f3_eu": "UE", "f3_rest": "Resto do mundo",
        "f3_source": "Fontes: Epoch AI / Pilz et al. (2025), GeoCoded/Sanchez (2025)",
        "f3_note": "Razão EUA/UE ≈ 15:1 em 2025",

        "f4_title": "Cronologia das Medidas dos EUA sobre Semicondutores e IA\n(2022–2026): Do Controle de Exportação ao Protecionismo Tarifário",
        "f4_events": [
            ("Out.\n2022", "Controles BIS\nGPUs avançadas, SME\nAlvo: China", "Biden"),
            ("Out.\n2023", "Atualização limites\n+40 países, A800/H800\ncapturados", "Biden"),
            ("Dez.\n2024", "Onda 3: 24 tipos SME\nHBM, 140 entidades", "Biden"),
            ("Jan.\n2025", "AI Diffusion Rule\nModelos + Cloud\n120 países, 3 níveis", "Biden"),
            ("Jul.\n2025", "America's AI\nAction Plan\nDesregulação EUA", "Trump"),
            ("Jan.\n2026", "Seção 232\nTarifa 25% GPU\nIsenção EUA", "Trump"),
        ],
        "f4_source": "Fontes: BIS, White House, Pillsbury Law (2026), Gibson Dunn (2026)",
        "f4_phase_d": "Denial strategy\n(negação de acesso)",
        "f4_phase_c": "Capture strategy\n(protecionismo ofensivo)",

        "f5_title": "Calibração do CACI: Decomposição da Vantagem EUA\n(2024–2025)",
        "f5_components": ["Compute\ninstalado\n(razão F)", "Custo\nenergético\n(razão E)", "CACI\nresultante\n(faixa)"],
        "f5_ylabel": "Razão EUA / UE",
        "f5_source": "Elaboração do autor — Seção 3.3.3, dados Epoch AI, IEA, Eurostat",

        "f6_title": "Síntese: Indicadores de Dominância dos EUA\nem Compute IA (2024–2025)",
        "f6_indicators": ["Desempenho\nclusters GPU", "Setor privado\ncompute IA", "Consumo\ndata centers",
                          "Investimento\nIA 2025", "Potência\nchips IA"],
        "f6_us_vals": [75, 65, 45, 85, 70],
        "f6_eu_vals": [5, 3, 15, 5, 4],
        "f6_cn_vals": [15, 12, 25, 8, 18],
        "f6_ylabel": "Participação global (%)",
        "f6_source": "Fontes: Epoch AI, IEA, GeoCoded/Sanchez, estimativas do autor",
    }
}


def setup_style():
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 11,
        'axes.facecolor': BG_COLOR, 'figure.facecolor': 'white',
        'axes.grid': True, 'grid.color': GRID_COLOR, 'grid.alpha': 0.5,
        'axes.spines.top': False, 'axes.spines.right': False,
    })

def save_fig(fig, name, sfx):
    p = os.path.join(OUTPUT_DIR, f"{name}_{sfx}.png")
    fig.savefig(p, dpi=DPI, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  ✓ {p}")
    return p


# ═══════════════════════════════════════════════════════════════════════════
# FIG 3.1 — Conso data centers par région (stacked area) — G1 du texte
# Page : p. 2-3 (après §3.1.2, après Tableau 4)
# ═══════════════════════════════════════════════════════════════════════════
def fig1_energy_by_region(L, lk):
    years = [2020, 2022, 2024, 2026, 2028, 2030]
    us  = [120, 150, 180, 260, 340, 420]
    cn  = [60,  78,  102, 155, 215, 280]
    eu  = [45,  55,  70,  85,  100, 115]
    rest= [45,  47,  63,  80,  95,  130]

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.stackplot(years, us, cn, eu, rest,
                 labels=[L["f1_us"], L["f1_cn"], L["f1_eu"], L["f1_rest"]],
                 colors=[US_COLOR, CN_COLOR, EU_COLOR, REST_COLOR],
                 alpha=0.75)

    # Total line
    totals = [u+c+e+r for u,c,e,r in zip(us,cn,eu,rest)]
    ax.plot(years, totals, color='black', linewidth=2, marker='o', markersize=5)
    for yr, t in zip(years, totals):
        if yr in [2024, 2030]:
            ax.text(yr, t+25, f"{t} TWh", ha='center', fontsize=10, fontweight='bold')

    ax.axvspan(2024.5, 2030.5, alpha=0.04, color='gray')
    ax.text(2027.5, 80, L["f1_proj"], fontsize=9, color='gray', fontstyle='italic', ha='center')

    ax.set_title(L["f1_title"], fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel(L["f1_ylabel"], fontsize=12)
    ax.set_xlim(2019.5, 2030.5)
    ax.set_ylim(0, 1100)
    ax.set_xticks(years)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax.text(0.5, -0.1, L["f1_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_3.1_Energy_By_Region", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 3.2 — Ventes semi-conducteurs segmentées — G2 du texte
# Page : p. 4-5 (après §3.2.1, après Tableau 5)
# ═══════════════════════════════════════════════════════════════════════════
def fig2_semi_sales(L, lk):
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025, 2026])
    total = np.array([440, 556, 556, 527, 631, 792, 988])
    # Segmentation estimates
    logic_share  = np.array([0.32, 0.33, 0.34, 0.36, 0.38, 0.38, 0.40])
    memory_share = np.array([0.25, 0.27, 0.27, 0.23, 0.27, 0.28, 0.30])
    logic  = total * logic_share
    memory = total * memory_share
    other  = total - logic - memory

    fig, ax = plt.subplots(figsize=(12, 7))
    w = 0.65
    ax.bar(years, other, w, bottom=logic+memory, color=REST_COLOR, label=L["f2_other"],
           edgecolor='white', linewidth=0.5)
    ax.bar(years, memory, w, bottom=logic, color=ACCENT3, label=L["f2_memory"],
           edgecolor='white', linewidth=0.5)
    ax.bar(years, logic, w, color=US_COLOR, label=L["f2_logic"],
           edgecolor='white', linewidth=0.5)

    # Total labels
    for yr, t in zip(years, total):
        ax.text(yr, t + 15, f"${t}", ha='center', fontsize=9, fontweight='bold', color='#333')

    # Growth rates
    growths = ["+6.8%", "+26.4%", "0%", "−8.2%", "+19.1%", "+25.6%", "+24.7%"]
    for yr, g in zip(years, growths):
        col = ACCENT1 if not g.startswith("−") else CN_COLOR
        ax.text(yr, -35, g, ha='center', fontsize=8, fontweight='bold', color=col)
    ax.text(years[0]-0.8, -35, L["f2_growth"], fontsize=8, color='gray', ha='right')

    ax.axvspan(2025.5, 2026.5, alpha=0.05, color='gray')

    ax.set_title(L["f2_title"], fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel(L["f2_ylabel"], fontsize=12)
    ax.set_xlim(2019.2, 2027)
    ax.set_ylim(-50, 1100)
    ax.set_xticks(years)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax.text(0.5, -0.12, L["f2_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_3.2_Semiconductor_Sales_Segmented", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 3.3 — Répartition GPU clusters par région (stacked bar) — G3
# Page : p. 6-7 (après §3.3.1, après Tableau 6)
# ═══════════════════════════════════════════════════════════════════════════
def fig3_gpu_distribution(L, lk):
    years = ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]
    # Estimated shares (Epoch AI trends)
    us   = [55, 58, 62, 67, 70, 73, 75]
    cn   = [25, 23, 20, 18, 17, 15, 15]
    eu   = [12, 11, 10,  8,  7,  6,  5]
    rest = [8,   8,  8,  7,  6,  6,  5]

    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(years))
    w = 0.6

    ax.bar(x, us, w, color=US_COLOR, label=L["f3_us"], edgecolor='white', linewidth=1)
    ax.bar(x, cn, w, bottom=us, color=CN_COLOR, label=L["f3_cn"], edgecolor='white', linewidth=1)
    ax.bar(x, eu, w, bottom=[u+c for u,c in zip(us,cn)], color=EU_COLOR, label=L["f3_eu"],
           edgecolor='white', linewidth=1)
    ax.bar(x, rest, w, bottom=[u+c+e for u,c,e in zip(us,cn,eu)], color=REST_COLOR,
           label=L["f3_rest"], edgecolor='white', linewidth=1)

    # US % labels
    for i, val in enumerate(us):
        ax.text(i, val/2, f"{val}%", ha='center', va='center', fontsize=11,
                fontweight='bold', color='white')
    # EU % labels
    for i, (val, b) in enumerate(zip(eu, [u+c for u,c in zip(us,cn)])):
        ax.text(i, b + val/2, f"{val}%", ha='center', va='center', fontsize=9,
                fontweight='bold', color='#333')

    # Note
    ax.text(6.35, 45, L["f3_note"], fontsize=11, fontweight='bold', color=CN_COLOR,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=CN_COLOR, alpha=0.9))

    ax.set_title(L["f3_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["f3_ylabel"], fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylim(0, 108)
    ax.legend(loc='lower right', fontsize=10, framealpha=0.9)
    ax.text(0.5, -0.1, L["f3_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_3.3_GPU_Cluster_Distribution", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 3.4 — Frise chronologique réglementaire — G4
# Page : p. 9-10 (après §3.4, après Tableau 7)
# ═══════════════════════════════════════════════════════════════════════════
def fig4_regulatory_timeline(L, lk):
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(7.5, 6.7, L["f4_title"], ha='center', fontsize=12, fontweight='bold')

    # Timeline line
    y_line = 3.5
    ax.plot([0.5, 14.5], [y_line, y_line], color='#333', linewidth=3, zorder=1)

    # Events
    event_x = [1.5, 3.7, 5.9, 8.1, 10.3, 12.8]
    biden_color = "#2471A3"
    trump_color = CN_COLOR

    for i, (ex, (date, desc, admin)) in enumerate(zip(event_x, L["f4_events"])):
        col = biden_color if admin == "Biden" else trump_color
        y_offset = 1.8 if i % 2 == 0 else -1.8
        y_text = y_line + y_offset

        # Dot on line
        ax.plot(ex, y_line, 'o', color=col, markersize=12, zorder=5)
        ax.plot(ex, y_line, 'o', color='white', markersize=6, zorder=6)

        # Vertical connector
        ax.plot([ex, ex], [y_line, y_text + (0.4 if y_offset > 0 else -0.4)],
                color=col, linewidth=1.5, linestyle='--', zorder=2)

        # Text box
        bbox_y = y_text - 0.6 if y_offset > 0 else y_text - 0.4
        rect = mpatches.FancyBboxPatch((ex - 1.0, bbox_y), 2.0, 1.6,
                                        boxstyle="round,pad=0.12",
                                        facecolor=col, alpha=0.08,
                                        edgecolor=col, linewidth=1.5)
        ax.add_patch(rect)

        # Date
        ax.text(ex, y_text + 0.5 if y_offset > 0 else y_text + 0.5, date,
                ha='center', fontsize=8, fontweight='bold', color=col)
        # Description
        ax.text(ex, y_text - 0.1 if y_offset > 0 else y_text - 0.1, desc,
                ha='center', va='center', fontsize=7, color='#333', linespacing=1.3)

    # Phase labels
    ax.annotate('', xy=(7.5, 1.2), xytext=(0.8, 1.2),
                arrowprops=dict(arrowstyle='<->', color=biden_color, lw=2))
    ax.text(4.1, 0.7, L["f4_phase_d"], ha='center', fontsize=9,
            fontweight='bold', color=biden_color, fontstyle='italic')

    ax.annotate('', xy=(14.2, 1.2), xytext=(9.5, 1.2),
                arrowprops=dict(arrowstyle='<->', color=trump_color, lw=2))
    ax.text(11.8, 0.7, L["f4_phase_c"], ha='center', fontsize=9,
            fontweight='bold', color=trump_color, fontstyle='italic')

    # Admin labels
    ax.text(4.0, y_line + 0.3, "Biden", fontsize=9, color=biden_color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=biden_color, alpha=0.8))
    ax.text(11.5, y_line + 0.3, "Trump", fontsize=9, color=trump_color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=trump_color, alpha=0.8))

    ax.text(7.5, 0.15, L["f4_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_3.4_Regulatory_Timeline", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 3.5 — Calibration CACI
# Page : p. 7-8 (après §3.3.3)
# ═══════════════════════════════════════════════════════════════════════════
def fig5_caci_calibration(L, lk):
    fig, ax = plt.subplots(figsize=(10, 7))

    components = L["f5_components"]
    # F ratio ~15, E ratio ~2.5 (inverted: US advantage), CACI range 7-12
    vals = [15, 2.5, 9.5]
    errors = [[0, 0, 2.5], [0, 0, 2.5]]  # error bars for CACI range
    colors = [US_COLOR, ACCENT3, CN_COLOR]

    bars = ax.bar(components, vals, width=0.5, color=colors, alpha=0.8,
                  edgecolor='white', linewidth=2, yerr=errors, capsize=8,
                  error_kw={'elinewidth': 2, 'capthick': 2, 'color': '#666'})

    # Value labels
    labels = ["×15", "×2.5", "×7 – ×12"]
    for bar, val, label in zip(bars, vals, labels):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.8, label,
                ha='center', fontsize=14, fontweight='bold', color=bar.get_facecolor())

    # Arrow showing multiplication
    ax.annotate('×', xy=(0.72, 8), fontsize=20, fontweight='bold', color='#999', ha='center')
    ax.annotate('=', xy=(1.68, 8), fontsize=20, fontweight='bold', color='#999', ha='center')

    ax.set_title(L["f5_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["f5_ylabel"], fontsize=12)
    ax.set_ylim(0, 20)
    ax.text(0.5, -0.1, L["f5_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_3.5_CACI_Calibration", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 3.6 — Synthèse indicateurs domination US (radar-like grouped bar)
# Page : p. 10-11 (section 3.5 Synthèse)
# ═══════════════════════════════════════════════════════════════════════════
def fig6_dominance_synthesis(L, lk):
    fig, ax = plt.subplots(figsize=(13, 7))

    indicators = L["f6_indicators"]
    x = np.arange(len(indicators))
    w = 0.25

    bars_us = ax.bar(x - w, L["f6_us_vals"], w, color=US_COLOR, label=L["f1_us"],
                     edgecolor='white', linewidth=1.5)
    bars_cn = ax.bar(x, L["f6_cn_vals"], w, color=CN_COLOR, label=L["f1_cn"],
                     edgecolor='white', linewidth=1.5)
    bars_eu = ax.bar(x + w, L["f6_eu_vals"], w, color=EU_COLOR, label=L["f1_eu"],
                     edgecolor='white', linewidth=1.5)

    # Value labels
    for bars, col in [(bars_us, US_COLOR), (bars_cn, CN_COLOR), (bars_eu, EU_COLOR)]:
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h + 1, f"{int(h)}%",
                    ha='center', fontsize=9, fontweight='bold', color=col)

    # Dominance line
    ax.axhline(y=50, color='#CCC', linewidth=1, linestyle=':', alpha=0.7)
    ax.text(4.6, 51, "50%", fontsize=8, color='#999')

    ax.set_title(L["f6_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["f6_ylabel"], fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(indicators, fontsize=9)
    ax.set_ylim(0, 100)
    ax.legend(fontsize=11, framealpha=0.9, loc='upper right')
    ax.text(0.5, -0.12, L["f6_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_3.6_US_Dominance_Synthesis", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()

    print("=" * 70)
    print(" CHAPITRE III — Génération des graphiques en 3 langues")
    print("=" * 70)

    all_files = []
    for lk, L in LANGS.items():
        print(f"\n{'─'*50}\n Langue : {L['suffix']}\n{'─'*50}")
        all_files.append(fig1_energy_by_region(L, lk))
        all_files.append(fig2_semi_sales(L, lk))
        all_files.append(fig3_gpu_distribution(L, lk))
        all_files.append(fig4_regulatory_timeline(L, lk))
        all_files.append(fig5_caci_calibration(L, lk))
        all_files.append(fig6_dominance_synthesis(L, lk))

    print(f"\n{'='*70}\n Total : {len(all_files)} fichiers\n{'='*70}")
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║  GUIDE D'INSERTION — Chapitre III                                  ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Fig 3.1  Énergie data centers/région   → p.2-3 (après §3.1.2)   ║
║           Stacked area US/CN/EU/Reste 2020-2030  [= G1 texte]     ║
║                                                                    ║
║  Fig 3.2  Ventes semi-conducteurs       → p.4-5 (après §3.2.1)   ║
║           Barres segmentées logique/mémoire/autre [= G2 texte]    ║
║                                                                    ║
║  Fig 3.3  Répartition clusters GPU      → p.6-7 (après §3.3.1)   ║
║           Stacked bars US/CN/EU/Reste 2019-2025  [= G3 texte]     ║
║                                                                    ║
║  Fig 3.4  Frise chronologique réglement.→ p.9-10 (après §3.4)    ║
║           6 événements Biden→Trump, phases [= G4 texte]           ║
║                                                                    ║
║  Fig 3.5  Calibration CACI              → p.7-8 (après §3.3.3)   ║
║           Décomposition ratio F × E → CACI 7-12                    ║
║                                                                    ║
║  Fig 3.6  Synthèse domination US        → p.10-11 (§3.5)         ║
║           5 indicateurs : US vs CN vs EU (grouped bars)            ║
║                                                                    ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    return all_files

if __name__ == "__main__":
    main()
