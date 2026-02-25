#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre VI quater : Conséquences pour l'Afrique
 Générateur de graphiques en 3 langues (FR / EN / PT-BR)
=============================================================================
 Auteur : Script généré pour l'étude académique
 Usage  : python generate_chapitre6quat_graphs.py
 Output : PNG files in ./output/figures_ch6quat/
=============================================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os

# ─── Configuration ──────────────────────────────────────────────────────────
OUTPUT_DIR = "./output/figures_ch6quat"
DPI = 300
FIGSIZE_WIDE = (12, 6.5)
FIGSIZE_SQUARE = (10, 7)
FIGSIZE_TALL = (11, 8)

# Couleurs palette professionnelle
DARK_BLUE  = "#1B3A5C"
MEDIUM_BLUE= "#2E75B6"
US_COLOR   = "#1B4F72"
CN_COLOR   = "#C0392B"
AF_COLOR   = "#D4A574"    # Sable / Africa
SA_COLOR   = "#2E86C1"    # South Africa
NG_COLOR   = "#148F77"    # Nigeria
KE_COLOR   = "#E67E22"    # Kenya
MA_COLOR   = "#884EA0"    # Morocco
EG_COLOR   = "#D4AC0D"    # Egypt
RW_COLOR   = "#27AE60"    # Rwanda
BG_COLOR   = "#FAFBFC"
GRID_COLOR = "#E0E0E0"
WARN_RED   = "#CC0000"

# ─── Traductions ────────────────────────────────────────────────────────────
LANGS = {
    "fr": {
        "suffix": "FR",
        # Fig 1 — Capacité DC Afrique vs Monde
        "fig1_title": "Capacité data center : l'Afrique face au monde\n(MW IT load, mi-2025)",
        "fig1_ylabel": "MW (IT load)",
        "fig1_cats": ["États-Unis", "Europe", "Chine", "Inde", "Afrique"],
        "fig1_source": "Sources : IEA (2025), McKinsey (2025), Mordor Intelligence (2026), African Energy Chamber (2025)",
        "fig1_annot": "< 2 % du total mondial",
        # Fig 2 — Pôles IA africains
        "fig2_title": "Les six pôles IA africains : data centers et investissements\n(2025)",
        "fig2_ylabel": "",
        "fig2_cats": ["Afrique du Sud", "Nigeria", "Kenya", "Maroc", "Égypte", "Rwanda"],
        "fig2_dc_label": "Data centers (nb)",
        "fig2_inv_label": "Investissement clé (M$)",
        "fig2_source": "Sources : Mordor Intelligence (2026), African Energy Chamber (2025), DCD (2025), Bloomberg (2025)",
        # Fig 3 — Croissance marché IA africain
        "fig3_title": "Marché IA africain : trajectoire de croissance\n(2025-2031, milliards USD)",
        "fig3_ylabel": "Milliards USD",
        "fig3_xlabel": "",
        "fig3_label_ai": "Marché IA africain",
        "fig3_label_dc": "Marché data centers africain",
        "fig3_source": "Sources : Tech In Africa (2025), Mordor Intelligence (2026), McKinsey (2025)",
        "fig3_cagr_ai": "CAGR 27 %",
        "fig3_cagr_dc": "CAGR 14,5 %",
        # Fig 4 — Compétition US vs Chine en Afrique
        "fig4_title": "Compétition IA en Afrique : engagements États-Unis vs Chine\n(principaux investissements, M$)",
        "fig4_ylabel": "Millions USD",
        "fig4_cats": ["Infrastructure\nDC/GPU", "Cloud &\nhyperscalers", "Formation\ntalents IA", "Modèles IA\n& services"],
        "fig4_legend_us": "États-Unis",
        "fig4_legend_cn": "Chine",
        "fig4_source": "Sources : Bloomberg (2025), DCD (2025), Semafor (2025), Rest of World (2025), Africa Defense Forum (2025)",
        # Fig 5 — Matrice scénarielle Afrique
        "fig5_title": "Matrice scénarielle 2×2 : trajectoires IA pour l'Afrique\n(2026-2030)",
        "fig5_x_label": "Intensité du protectionnisme US →",
        "fig5_y_label": "← Réponse africaine active",
        "fig5_s1": "S1\nStagnation\ndépendante",
        "fig5_s2": "S2\nRattrapage\nciblé",
        "fig5_s3": "S3\nBifurcation\nimposée",
        "fig5_s4": "S4\nNon-alignement\nnumérique",
        "fig5_s1_detail": "IA ~1 % PIB 2030\nBrain drain continu",
        "fig5_s2_detail": "AI Factories opérationnelles\nIA ~3 % PIB 2030",
        "fig5_s3_detail": "Dépendance Huawei/DeepSeek\nRisque surveillance",
        "fig5_s4_detail": "Multi-sourcing\nSouveraineté données",
        "fig5_source": "Source : Analyse auteur, adaptation matrice Chapitre V",
        "fig5_mod": "Modéré",
        "fig5_int": "Intense",
        "fig5_pass": "Passive",
        "fig5_act": "Active",
        # Fig 6 — Ratios CACI Afrique vs US
        "fig6_title": "Ratios CACI : l'abîme Afrique / États-Unis\n(2025)",
        "fig6_ylabel": "Ratio US / Afrique (×)",
        "fig6_cats": ["Capacité DC\n(GW IT)", "Investissement\nDC ($)", "GPUs IA\n(Nvidia)", "Talent IA\n(pool)", "Marché IA\n($)"],
        "fig6_source": "Sources : données compilées auteur — IEA, McKinsey, Mordor Intelligence, WEF, Tech In Africa (2025-2026)",
    },
    "en": {
        "suffix": "EN",
        "fig1_title": "Data Center Capacity: Africa vs the World\n(MW IT load, mid-2025)",
        "fig1_ylabel": "MW (IT load)",
        "fig1_cats": ["United States", "Europe", "China", "India", "Africa"],
        "fig1_source": "Sources: IEA (2025), McKinsey (2025), Mordor Intelligence (2026), African Energy Chamber (2025)",
        "fig1_annot": "< 2% of global total",
        "fig2_title": "The Six African AI Hubs: Data Centers and Investments\n(2025)",
        "fig2_ylabel": "",
        "fig2_cats": ["South Africa", "Nigeria", "Kenya", "Morocco", "Egypt", "Rwanda"],
        "fig2_dc_label": "Data centers (#)",
        "fig2_inv_label": "Key investment ($M)",
        "fig2_source": "Sources: Mordor Intelligence (2026), African Energy Chamber (2025), DCD (2025), Bloomberg (2025)",
        "fig3_title": "African AI Market: Growth Trajectory\n(2025-2031, USD billions)",
        "fig3_ylabel": "USD Billions",
        "fig3_xlabel": "",
        "fig3_label_ai": "African AI market",
        "fig3_label_dc": "African data center market",
        "fig3_source": "Sources: Tech In Africa (2025), Mordor Intelligence (2026), McKinsey (2025)",
        "fig3_cagr_ai": "CAGR 27%",
        "fig3_cagr_dc": "CAGR 14.5%",
        "fig4_title": "AI Competition in Africa: US vs China Engagements\n(key investments, $M)",
        "fig4_ylabel": "USD Millions",
        "fig4_cats": ["DC/GPU\nInfrastructure", "Cloud &\nHyperscalers", "AI Talent\nTraining", "AI Models\n& Services"],
        "fig4_legend_us": "United States",
        "fig4_legend_cn": "China",
        "fig4_source": "Sources: Bloomberg (2025), DCD (2025), Semafor (2025), Rest of World (2025), Africa Defense Forum (2025)",
        "fig5_title": "2×2 Scenario Matrix: AI Trajectories for Africa\n(2026-2030)",
        "fig5_x_label": "US Protectionism Intensity →",
        "fig5_y_label": "← Active African Response",
        "fig5_s1": "S1\nDependent\nStagnation",
        "fig5_s2": "S2\nTargeted\nCatch-Up",
        "fig5_s3": "S3\nImposed\nBifurcation",
        "fig5_s4": "S4\nDigital\nNon-Alignment",
        "fig5_s1_detail": "AI ~1% of GDP 2030\nContinuous brain drain",
        "fig5_s2_detail": "Operational AI Factories\nAI ~3% of GDP 2030",
        "fig5_s3_detail": "Huawei/DeepSeek dependency\nSurveillance risk",
        "fig5_s4_detail": "Multi-sourcing\nData sovereignty",
        "fig5_source": "Source: Author analysis, adapted from Chapter V matrix",
        "fig5_mod": "Moderate",
        "fig5_int": "Intense",
        "fig5_pass": "Passive",
        "fig5_act": "Active",
        "fig6_title": "CACI Ratios: The Africa / US Abyss\n(2025)",
        "fig6_ylabel": "US / Africa Ratio (×)",
        "fig6_cats": ["DC Capacity\n(GW IT)", "DC Investment\n($)", "AI GPUs\n(Nvidia)", "AI Talent\n(pool)", "AI Market\n($)"],
        "fig6_source": "Sources: compiled data — IEA, McKinsey, Mordor Intelligence, WEF, Tech In Africa (2025-2026)",
    },
    "pt": {
        "suffix": "PT",
        "fig1_title": "Capacidade de data center: África vs o mundo\n(MW IT load, meados de 2025)",
        "fig1_ylabel": "MW (IT load)",
        "fig1_cats": ["Estados Unidos", "Europa", "China", "Índia", "África"],
        "fig1_source": "Fontes: IEA (2025), McKinsey (2025), Mordor Intelligence (2026), African Energy Chamber (2025)",
        "fig1_annot": "< 2% do total global",
        "fig2_title": "Os seis polos de IA africanos: data centers e investimentos\n(2025)",
        "fig2_ylabel": "",
        "fig2_cats": ["África do Sul", "Nigéria", "Quênia", "Marrocos", "Egito", "Ruanda"],
        "fig2_dc_label": "Data centers (nº)",
        "fig2_inv_label": "Investimento-chave (M$)",
        "fig2_source": "Fontes: Mordor Intelligence (2026), African Energy Chamber (2025), DCD (2025), Bloomberg (2025)",
        "fig3_title": "Mercado de IA africano: trajetória de crescimento\n(2025-2031, bilhões USD)",
        "fig3_ylabel": "Bilhões USD",
        "fig3_xlabel": "",
        "fig3_label_ai": "Mercado de IA africano",
        "fig3_label_dc": "Mercado de data centers africano",
        "fig3_source": "Fontes: Tech In Africa (2025), Mordor Intelligence (2026), McKinsey (2025)",
        "fig3_cagr_ai": "CAGR 27%",
        "fig3_cagr_dc": "CAGR 14,5%",
        "fig4_title": "Competição de IA na África: engajamentos EUA vs China\n(principais investimentos, M$)",
        "fig4_ylabel": "Milhões USD",
        "fig4_cats": ["Infraestrutura\nDC/GPU", "Cloud &\nhyperscalers", "Formação\ntalentos IA", "Modelos de IA\n& serviços"],
        "fig4_legend_us": "Estados Unidos",
        "fig4_legend_cn": "China",
        "fig4_source": "Fontes: Bloomberg (2025), DCD (2025), Semafor (2025), Rest of World (2025), Africa Defense Forum (2025)",
        "fig5_title": "Matriz de cenários 2×2: trajetórias de IA para a África\n(2026-2030)",
        "fig5_x_label": "Intensidade do protecionismo EUA →",
        "fig5_y_label": "← Resposta africana ativa",
        "fig5_s1": "C1\nEstagnação\ndependente",
        "fig5_s2": "C2\nRecuperação\ndirecionada",
        "fig5_s3": "C3\nBifurcação\nimposta",
        "fig5_s4": "C4\nNão-alinhamento\ndigital",
        "fig5_s1_detail": "IA ~1% do PIB 2030\nFuga de cérebros contínua",
        "fig5_s2_detail": "AI Factories operacionais\nIA ~3% do PIB 2030",
        "fig5_s3_detail": "Dependência Huawei/DeepSeek\nRisco de vigilância",
        "fig5_s4_detail": "Multi-sourcing\nSoberania de dados",
        "fig5_source": "Fonte: Análise do autor, adaptação da matriz Capítulo V",
        "fig5_mod": "Moderado",
        "fig5_int": "Intenso",
        "fig5_pass": "Passiva",
        "fig5_act": "Ativa",
        "fig6_title": "Razões CACI: o abismo África / Estados Unidos\n(2025)",
        "fig6_ylabel": "Razão EUA / África (×)",
        "fig6_cats": ["Capacidade DC\n(GW IT)", "Investimento\nDC ($)", "GPUs de IA\n(Nvidia)", "Talento IA\n(pool)", "Mercado IA\n($)"],
        "fig6_source": "Fontes: dados compilados — IEA, McKinsey, Mordor Intelligence, WEF, Tech In Africa (2025-2026)",
    },
}


def setup_style():
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
        'font.size': 11,
        'axes.facecolor': BG_COLOR,
        'figure.facecolor': 'white',
        'axes.grid': True,
        'grid.alpha': 0.3,
        'grid.color': GRID_COLOR,
        'axes.spines.top': False,
        'axes.spines.right': False,
    })


def save_fig(fig, name, lang_suffix):
    path = os.path.join(OUTPUT_DIR, f"{name}_{lang_suffix}.png")
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  ✓ {path}")


# =============================================================================
# FIGURE 1 — Capacité DC Afrique vs Monde
# =============================================================================
def fig1_dc_capacity(L, lang):
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    # Data: US 53,700 MW, Europe ~35,000 MW, China ~25,000 MW, India ~1,400 MW, Africa ~980 MW
    values = [53700, 35000, 25000, 1400, 980]
    colors = [US_COLOR, "#D4AC0D", CN_COLOR, "#E67E22", AF_COLOR]

    bars = ax.bar(L["fig1_cats"], values, color=colors, edgecolor='white', linewidth=0.5, width=0.6)

    # Annotate values
    for bar, val in zip(bars, values):
        label = f"{val:,.0f}" if val >= 1000 else str(val)
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 800,
                label, ha='center', va='bottom', fontsize=10, fontweight='bold',
                color=DARK_BLUE)

    # Africa annotation with arrow
    ax.annotate(L["fig1_annot"], xy=(4, 980), xytext=(3.3, 15000),
                fontsize=12, fontweight='bold', color=WARN_RED,
                arrowprops=dict(arrowstyle='->', color=WARN_RED, lw=2),
                ha='center')

    ax.set_ylabel(L["fig1_ylabel"], fontsize=12, fontweight='bold')
    ax.set_title(L["fig1_title"], fontsize=14, fontweight='bold', color=DARK_BLUE, pad=15)

    ax.set_ylim(0, 62000)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1000:.0f}k'))

    fig.text(0.5, -0.02, L["fig1_source"], ha='center', fontsize=8, color='gray', style='italic')
    fig.tight_layout()
    save_fig(fig, "fig1_dc_capacity", L["suffix"])


# =============================================================================
# FIGURE 2 — Pôles IA africains
# =============================================================================
def fig2_african_hubs(L, lang):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIGSIZE_WIDE)

    hubs = L["fig2_cats"]
    dc_counts = [56, 18, 19, 15, 12, 4]
    investments = [2300, 388, 1000, 1000, 720, 50]  # M$ aggregated key investments
    hub_colors = [SA_COLOR, NG_COLOR, KE_COLOR, MA_COLOR, EG_COLOR, RW_COLOR]

    y_pos = np.arange(len(hubs))

    # Left: Data centers count
    bars1 = ax1.barh(y_pos, dc_counts, color=hub_colors, edgecolor='white', height=0.6)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(hubs, fontsize=10)
    ax1.set_xlabel(L["fig2_dc_label"], fontsize=11, fontweight='bold')
    ax1.invert_yaxis()
    for bar, val in zip(bars1, dc_counts):
        ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                str(val), va='center', fontsize=10, fontweight='bold', color=DARK_BLUE)

    # Right: Investments
    bars2 = ax2.barh(y_pos, investments, color=hub_colors, edgecolor='white', height=0.6)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([""] * len(hubs))
    ax2.set_xlabel(L["fig2_inv_label"], fontsize=11, fontweight='bold')
    ax2.invert_yaxis()
    for bar, val in zip(bars2, investments):
        ax2.text(bar.get_width() + 15, bar.get_y() + bar.get_height()/2,
                f"${val:,.0f}M", va='center', fontsize=9, fontweight='bold', color=DARK_BLUE)

    fig.suptitle(L["fig2_title"], fontsize=14, fontweight='bold', color=DARK_BLUE, y=1.02)
    fig.text(0.5, -0.04, L["fig2_source"], ha='center', fontsize=8, color='gray', style='italic')
    fig.tight_layout()
    save_fig(fig, "fig2_african_hubs", L["suffix"])


# =============================================================================
# FIGURE 3 — Croissance marché IA africain
# =============================================================================
def fig3_market_growth(L, lang):
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    years = [2025, 2026, 2027, 2028, 2029, 2030, 2031]
    # AI market: $4.51B (2025) → $16.53B (2030), extrapolate to 2031
    ai_market = [4.51, 5.73, 7.28, 9.25, 11.76, 16.53, 21.0]
    # DC market: $1.94B (2025) → $4.36B (2031)
    dc_market = [1.94, 2.22, 2.54, 2.91, 3.34, 3.83, 4.36]

    ax.fill_between(years, ai_market, alpha=0.15, color=MEDIUM_BLUE)
    ax.plot(years, ai_market, 'o-', color=MEDIUM_BLUE, linewidth=2.5, markersize=8,
            label=L["fig3_label_ai"], zorder=5)

    ax.fill_between(years, dc_market, alpha=0.15, color=AF_COLOR)
    ax.plot(years, dc_market, 's-', color=AF_COLOR, linewidth=2.5, markersize=8,
            label=L["fig3_label_dc"], zorder=5)

    # CAGR annotations
    ax.annotate(L["fig3_cagr_ai"], xy=(2029, 13), fontsize=12, fontweight='bold',
                color=MEDIUM_BLUE, rotation=25)
    ax.annotate(L["fig3_cagr_dc"], xy=(2029, 3.0), fontsize=11, fontweight='bold',
                color=AF_COLOR, rotation=10)

    # Value labels
    for y, v in [(2025, 4.51), (2030, 16.53)]:
        ax.annotate(f"${v}B", xy=(y, v), xytext=(0, 12), textcoords='offset points',
                    ha='center', fontsize=10, fontweight='bold', color=DARK_BLUE)
    for y, v in [(2025, 1.94), (2031, 4.36)]:
        ax.annotate(f"${v}B", xy=(y, v), xytext=(0, -18), textcoords='offset points',
                    ha='center', fontsize=10, fontweight='bold', color=DARK_BLUE)

    ax.set_ylabel(L["fig3_ylabel"], fontsize=12, fontweight='bold')
    ax.set_title(L["fig3_title"], fontsize=14, fontweight='bold', color=DARK_BLUE, pad=15)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax.set_xlim(2024.5, 2031.5)
    ax.set_ylim(0, 24)

    fig.text(0.5, -0.02, L["fig3_source"], ha='center', fontsize=8, color='gray', style='italic')
    fig.tight_layout()
    save_fig(fig, "fig3_market_growth", L["suffix"])


# =============================================================================
# FIGURE 4 — Compétition US vs Chine en Afrique
# =============================================================================
def fig4_us_vs_china(L, lang):
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    cats = L["fig4_cats"]
    # US: Infrastructure (Cassava 720 + MS 300 + AWS 1700 + others), Cloud (MS+Google ~2300),
    #     Talent (MS 3M+Google+Intel = ~200M$), Models (~100M$)
    us_vals  = [2720, 2300, 200, 100]
    # China: Infrastructure (Huawei DCs + 5G ~500M est.), Cloud (~300M est.),
    #        Talent (120K trained ~50M est.), Models (DeepSeek free, Pangu ~80M est.)
    cn_vals  = [500, 300, 50, 80]

    x = np.arange(len(cats))
    width = 0.35

    bars_us = ax.bar(x - width/2, us_vals, width, label=L["fig4_legend_us"],
                     color=US_COLOR, edgecolor='white', linewidth=0.5)
    bars_cn = ax.bar(x + width/2, cn_vals, width, label=L["fig4_legend_cn"],
                     color=CN_COLOR, edgecolor='white', linewidth=0.5)

    for bar, val in zip(bars_us, us_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 30,
                f"${val:,.0f}", ha='center', va='bottom', fontsize=9,
                fontweight='bold', color=US_COLOR)
    for bar, val in zip(bars_cn, cn_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 30,
                f"${val:,.0f}", ha='center', va='bottom', fontsize=9,
                fontweight='bold', color=CN_COLOR)

    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=10)
    ax.set_ylabel(L["fig4_ylabel"], fontsize=12, fontweight='bold')
    ax.set_title(L["fig4_title"], fontsize=14, fontweight='bold', color=DARK_BLUE, pad=15)
    ax.legend(fontsize=11, loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 3200)

    fig.text(0.5, -0.02, L["fig4_source"], ha='center', fontsize=8, color='gray', style='italic')
    fig.tight_layout()
    save_fig(fig, "fig4_us_vs_china", L["suffix"])


# =============================================================================
# FIGURE 5 — Matrice scénarielle 2×2 Afrique
# =============================================================================
def fig5_scenario_matrix(L, lang):
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    # Quadrants
    colors = ['#E8F0FE', '#FFF3CD', '#FDEDEC', '#D5F5E3']
    rects = [(0.5, 5.2, 4.3, 4.3), (5.2, 5.2, 4.3, 4.3),
             (0.5, 0.5, 4.3, 4.3), (5.2, 0.5, 4.3, 4.3)]
    scenarios = [L["fig5_s1"], L["fig5_s2"], L["fig5_s3"], L["fig5_s4"]]
    details = [L["fig5_s1_detail"], L["fig5_s2_detail"], L["fig5_s3_detail"], L["fig5_s4_detail"]]
    borders = [MEDIUM_BLUE, '#D4AC0D', CN_COLOR, '#27AE60']

    for (x, y, w, h), color, sc, det, bc in zip(rects, colors, scenarios, details, borders):
        rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                                        facecolor=color, edgecolor=bc, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h*0.62, sc, ha='center', va='center',
                fontsize=13, fontweight='bold', color=DARK_BLUE)
        ax.text(x + w/2, y + h*0.28, det, ha='center', va='center',
                fontsize=9, color='#555555', style='italic')

    # Axes labels
    ax.annotate('', xy=(9.8, 5.0), xytext=(0.2, 5.0),
                arrowprops=dict(arrowstyle='->', color=DARK_BLUE, lw=1.5))
    ax.annotate('', xy=(5.0, 9.8), xytext=(5.0, 0.2),
                arrowprops=dict(arrowstyle='->', color=DARK_BLUE, lw=1.5))

    ax.text(5.0, 0.0, L["fig5_x_label"], ha='center', fontsize=11,
            fontweight='bold', color=DARK_BLUE)
    ax.text(-0.1, 5.0, L["fig5_y_label"], ha='center', fontsize=11,
            fontweight='bold', color=DARK_BLUE, rotation=90)

    # Corner labels
    ax.text(2.7, 9.7, L["fig5_mod"], ha='center', fontsize=10, color='gray')
    ax.text(7.3, 9.7, L["fig5_int"], ha='center', fontsize=10, color='gray')
    ax.text(0.1, 7.4, L["fig5_act"], ha='center', fontsize=10, color='gray', rotation=90)
    ax.text(0.1, 2.7, L["fig5_pass"], ha='center', fontsize=10, color='gray', rotation=90)

    # Star on S4 (recommended)
    ax.text(7.35, 1.5, "★", ha='center', fontsize=20, color='#27AE60')

    fig.suptitle(L["fig5_title"], fontsize=14, fontweight='bold', color=DARK_BLUE, y=0.98)
    fig.text(0.5, 0.01, L["fig5_source"], ha='center', fontsize=8, color='gray', style='italic')
    save_fig(fig, "fig5_scenario_matrix", L["suffix"])


# =============================================================================
# FIGURE 6 — Ratios CACI Afrique vs US
# =============================================================================
def fig6_caci_ratios(L, lang):
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    cats = L["fig6_cats"]
    # Ratios: DC capacity ×57, DC investment ×337, GPUs ×100+, Talent ×13, Market ×44
    ratios = [57, 337, 100, 13, 44]
    colors_grad = [MEDIUM_BLUE, US_COLOR, WARN_RED, AF_COLOR, "#884EA0"]

    bars = ax.bar(cats, ratios, color=colors_grad, edgecolor='white', linewidth=0.5, width=0.55)

    for bar, val in zip(bars, ratios):
        label = f"×{val}" if val < 200 else f"×{val}"
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                label, ha='center', va='bottom', fontsize=14, fontweight='bold',
                color=DARK_BLUE,
                path_effects=[pe.withStroke(linewidth=3, foreground='white')])

    # Reference line
    ax.axhline(y=1, color='green', linestyle='--', linewidth=1.5, alpha=0.5)
    ax.text(4.7, 5, "Parité = 1", fontsize=9, color='green', alpha=0.7)

    ax.set_ylabel(L["fig6_ylabel"], fontsize=12, fontweight='bold')
    ax.set_title(L["fig6_title"], fontsize=14, fontweight='bold', color=DARK_BLUE, pad=15)
    ax.set_ylim(0, 400)

    fig.text(0.5, -0.02, L["fig6_source"], ha='center', fontsize=8, color='gray', style='italic')
    fig.tight_layout()
    save_fig(fig, "fig6_caci_ratios", L["suffix"])


# =============================================================================
# MAIN
# =============================================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()

    print("=" * 70)
    print(" AI FOR AMERICANS FIRST — Chapitre VI quater : Afrique")
    print(" Génération des 6 figures × 3 langues = 18 PNG")
    print("=" * 70)

    for lang_key, L in LANGS.items():
        print(f"\n─── Langue : {lang_key.upper()} ───")
        fig1_dc_capacity(L, lang_key)
        fig2_african_hubs(L, lang_key)
        fig3_market_growth(L, lang_key)
        fig4_us_vs_china(L, lang_key)
        fig5_scenario_matrix(L, lang_key)
        fig6_caci_ratios(L, lang_key)

    print(f"\n{'=' * 70}")
    print(f" ✅ 18 fichiers PNG générés dans {OUTPUT_DIR}/")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
