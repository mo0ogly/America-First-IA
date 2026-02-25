#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre VI ter : Conséquences pour l'Asie
 Générateur de graphiques en 3 langues (FR / EN / PT-BR)
=============================================================================
 Auteur : Script généré pour la note académique
 Usage  : python generate_chapitre6ter_graphs.py
 Output : PNG files in ./output/figures_ch6ter/
=============================================================================

 GUIDE D'INSERTION (pages du chapitre VI ter) :
 ──────────────────────────────────────────────────────────────────
 Fig 6ter.1  Investissements Japon US-IA       → p. 2  (après §6ter.1.1)
 Fig 6ter.2  Capacité Data Centers Asie        → p. 3  (après §6ter.1.2)
 Fig 6ter.3  Taiwan/Corée chaîne semi-cond.    → p. 5  (après §6ter.2.2)
 Fig 6ter.4  Inde : ambition vs réalité        → p. 7  (après §6ter.3.2)
 Fig 6ter.5  Chine : autonomisation forcée      → p. 9  (après §6ter.4.2)
 Fig 6ter.6  Synthèse comparative Asie (Tiers) → p. 12 (après §6ter.6)
 ──────────────────────────────────────────────────────────────────
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os

# ─── Configuration ──────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
DPI = 300
FIGSIZE_WIDE = (12, 6.5)
FIGSIZE_SQUARE = (10, 7)
FIGSIZE_TALL = (11, 8)

# Couleurs palette professionnelle (même palette que les autres chapitres)
US_COLOR = "#1B4F72"       # Bleu foncé (US)
EU_COLOR = "#D4AC0D"       # Or/jaune (EU)
FR_COLOR = "#2E86C1"       # Bleu moyen (France)
CN_COLOR = "#C0392B"       # Rouge (Chine)
JP_COLOR = "#E74C3C"       # Rouge vif (Japon)
KR_COLOR = "#3498DB"       # Bleu clair (Corée)
TW_COLOR = "#1ABC9C"       # Turquoise (Taiwan)
IN_COLOR = "#F39C12"       # Orange (Inde)
ASEAN_COLOR = "#27AE60"    # Vert (ASEAN)
GULF_COLOR = "#8E44AD"     # Violet (Golfe)
ACCENT1 = "#148F77"        # Vert teal
ACCENT2 = "#884EA0"        # Violet
ACCENT3 = "#E67E22"        # Orange
BG_COLOR = "#FAFBFC"
GRID_COLOR = "#E0E0E0"

# ─── Traductions ────────────────────────────────────────────────────────────
LANGS = {
    "fr": {
        "suffix": "FR",

        # ── Fig 6ter.1 — Investissements Japon ──
        "fig1_title": "Accord d'investissement US-Japon en infrastructure IA\n(550 milliards USD, 2025-2026)",
        "fig1_cats": ["Infrastr.\nénergétique", "Semi-\nconducteurs", "Data\ncenters", "Câbles &\ncomposants"],
        "fig1_ylabel": "Milliards USD",
        "fig1_source": "Sources : Construction Today (2025), Taipei Times (2025), compilation auteur",
        "fig1_annot": "Total : 550 Md$",
        "fig1_detail_labels": ["Centrales &\nréseaux (332 Md$)", "Rapidus 2nm\n+ METI (65 Md$)", "SoftBank Stargate\n(40+ Md$)", "Mitsubishi 30 Md$\nTDK 25 Md$\nFujikura"],
        "fig1_domestic": "Invest. domestique Japon :",
        "fig1_dom_val": "330 Md$ (public-privé, décennie)",

        # ── Fig 6ter.2 — Capacité DC Asie ──
        "fig2_title": "Capacité installée de data centers en Asie\nvs États-Unis (GW, 2025)",
        "fig2_cats": ["États-Unis", "Chine", "Japon", "Taiwan +\nCorée Sud", "Inde", "ASEAN", "Golfe"],
        "fig2_ylabel": "Gigawatts (GW)",
        "fig2_source": "Sources : Mind2Markets (2026), Futurum (2026), compilation auteur",
        "fig2_legend_tier": ["Tier 1", "Tier 2", "Tier 3"],

        # ── Fig 6ter.3 — Taiwan/Corée chaîne semi-conducteurs ──
        "fig3_title": "Taiwan et Corée du Sud : position dans la chaîne\nde valeur des semi-conducteurs IA (2025)",
        "fig3_ylabel": "Part de marché mondiale (%)",
        "fig3_cats": ["Puces pointe\n(<7nm)", "Mémoire HBM\n(GPU IA)", "Fonderie\navancée", "Packaging\navancé"],
        "fig3_legend": ["TSMC (Taiwan)", "Samsung + SK hynix (Corée)"],
        "fig3_source": "Sources : données industrielles, TrendForce, IC Insights, compilation auteur",
        "fig3_risk_label": "Risque : transfert\nproduction vers US",

        # ── Fig 6ter.4 — Inde ambition vs réalité ──
        "fig4_title": "Inde : le fossé entre ambitions IA\net capacité installée (2025-2026)",
        "fig4_ylabel_left": "Milliards USD (investissements)",
        "fig4_ylabel_right": "GW (capacité DC installée)",
        "fig4_cats": ["Investissements\nannoncés (2 ans)", "Budget public\nIndiaAI Mission", "GPU déployées\n(en Md$ equiv.)"],
        "fig4_source": "Sources : IBTimes India (2026), Medium/D. Kumar (2026), Mind2Markets",
        "fig4_compare_label": "Capacité DC (GW)",
        "fig4_countries": ["États-Unis\n53,7 GW", "Chine\n19,6 GW", "Inde\n1,4 GW"],
        "fig4_tier_label": "Tier 2 : caps quantitatifs GPU",

        # ── Fig 6ter.5 — Chine autonomisation ──
        "fig5_title": "Chine : trajectoire d'autonomisation IA\nsous restrictions (2022-2030)",
        "fig5_ylabel_left": "Milliards USD",
        "fig5_ylabel_right": "EFLOP/s (capacité calcul IA)",
        "fig5_source": "Sources : IBTimes, Tom's Hardware, ITIF (2025), EastPost (2026)",
        "fig5_legend_invest": "Investissement IA (Md$)",
        "fig5_legend_eflops": "Capacité calcul (EFLOP/s)",
        "fig5_legend_foundry": "Part fonderies mondiales (%)",
        "fig5_annot_deepseek": "DeepSeek-V3\n(performances\ncompétitives)",
        "fig5_annot_huawei": "Huawei Ascend 910c\n(~H100, 60-70% coût)",

        # ── Fig 6ter.6 — Synthèse comparative Tiers ──
        "fig6_title": "Synthèse comparative : position asiatique\nface au protectionnisme IA américain",
        "fig6_countries": ["Japon", "Taiwan", "Corée\ndu Sud", "Inde", "Chine", "ASEAN", "Golfe"],
        "fig6_dimensions": ["Accès GPU\n(Tier)", "Capacité DC\n(GW)", "Investissement\nIA (Md$)", "Autonomie\ntechnologique", "Risque\nprincipal"],
        "fig6_source": "Source : compilation auteur, Tableau 16 du chapitre",
        "fig6_tier_labels": ["Tier 1\n(accès libre)", "Tier 2\n(caps)", "Tier 3\n(interdit)"],
    },

    "en": {
        "suffix": "EN",

        "fig1_title": "US-Japan AI Infrastructure Investment Agreement\n(USD 550 Billion, 2025-2026)",
        "fig1_cats": ["Energy\nInfrastructure", "Semi-\nconductors", "Data\nCenters", "Cables &\nComponents"],
        "fig1_ylabel": "Billion USD",
        "fig1_source": "Sources: Construction Today (2025), Taipei Times (2025), author compilation",
        "fig1_annot": "Total: $550B",
        "fig1_detail_labels": ["Power plants &\ngrids ($332B)", "Rapidus 2nm\n+ METI ($65B)", "SoftBank Stargate\n($40B+)", "Mitsubishi $30B\nTDK $25B\nFujikura"],
        "fig1_domestic": "Japan domestic invest.:",
        "fig1_dom_val": "$330B (public-private, decade)",

        "fig2_title": "Installed Data Center Capacity in Asia\nvs United States (GW, 2025)",
        "fig2_cats": ["United States", "China", "Japan", "Taiwan +\nSouth Korea", "India", "ASEAN", "Gulf"],
        "fig2_ylabel": "Gigawatts (GW)",
        "fig2_source": "Sources: Mind2Markets (2026), Futurum (2026), author compilation",
        "fig2_legend_tier": ["Tier 1", "Tier 2", "Tier 3"],

        "fig3_title": "Taiwan and South Korea: Position in the\nAI Semiconductor Value Chain (2025)",
        "fig3_ylabel": "Global Market Share (%)",
        "fig3_cats": ["Leading-edge\nchips (<7nm)", "HBM Memory\n(AI GPUs)", "Advanced\nfoundry", "Advanced\npackaging"],
        "fig3_legend": ["TSMC (Taiwan)", "Samsung + SK hynix (South Korea)"],
        "fig3_source": "Sources: industry data, TrendForce, IC Insights, author compilation",
        "fig3_risk_label": "Risk: production\ntransfer to US",

        "fig4_title": "India: The Gap Between AI Ambitions\nand Installed Capacity (2025-2026)",
        "fig4_ylabel_left": "Billion USD (investments)",
        "fig4_ylabel_right": "GW (installed DC capacity)",
        "fig4_cats": ["Announced\ninvestments (2 yrs)", "Public budget\nIndiaAI Mission", "GPUs deployed\n(B$ equiv.)"],
        "fig4_source": "Sources: IBTimes India (2026), Medium/D. Kumar (2026), Mind2Markets",
        "fig4_compare_label": "DC capacity (GW)",
        "fig4_countries": ["United States\n53.7 GW", "China\n19.6 GW", "India\n1.4 GW"],
        "fig4_tier_label": "Tier 2: quantitative GPU caps",

        "fig5_title": "China: AI Autonomization Trajectory\nUnder Restrictions (2022-2030)",
        "fig5_ylabel_left": "Billion USD",
        "fig5_ylabel_right": "EFLOP/s (AI compute capacity)",
        "fig5_source": "Sources: IBTimes, Tom's Hardware, ITIF (2025), EastPost (2026)",
        "fig5_legend_invest": "AI Investment ($B)",
        "fig5_legend_eflops": "Compute capacity (EFLOP/s)",
        "fig5_legend_foundry": "Global foundry share (%)",
        "fig5_annot_deepseek": "DeepSeek-V3\n(competitive\nperformance)",
        "fig5_annot_huawei": "Huawei Ascend 910c\n(~H100, 60-70% cost)",

        "fig6_title": "Comparative Synthesis: Asian Position\nFacing US AI Protectionism",
        "fig6_countries": ["Japan", "Taiwan", "South\nKorea", "India", "China", "ASEAN", "Gulf"],
        "fig6_dimensions": ["GPU Access\n(Tier)", "DC Capacity\n(GW)", "AI Investment\n($B)", "Technological\nAutonomy", "Primary\nRisk"],
        "fig6_source": "Source: author compilation, Table 16 of the chapter",
        "fig6_tier_labels": ["Tier 1\n(open access)", "Tier 2\n(caps)", "Tier 3\n(banned)"],
    },

    "pt": {
        "suffix": "PT-BR",

        "fig1_title": "Acordo de Investimento EUA-Japão em Infraestrutura IA\n(550 Bilhões USD, 2025-2026)",
        "fig1_cats": ["Infraestr.\nenergética", "Semi-\ncondutores", "Data\nCenters", "Cabos &\nComponentes"],
        "fig1_ylabel": "Bilhões USD",
        "fig1_source": "Fontes: Construction Today (2025), Taipei Times (2025), compilação do autor",
        "fig1_annot": "Total: US$ 550 bi",
        "fig1_detail_labels": ["Usinas &\nredes (US$ 332 bi)", "Rapidus 2nm\n+ METI (US$ 65 bi)", "SoftBank Stargate\n(US$ 40+ bi)", "Mitsubishi US$ 30 bi\nTDK US$ 25 bi\nFujikura"],
        "fig1_domestic": "Invest. doméstico Japão:",
        "fig1_dom_val": "US$ 330 bi (público-privado, década)",

        "fig2_title": "Capacidade Instalada de Data Centers na Ásia\nvs Estados Unidos (GW, 2025)",
        "fig2_cats": ["Estados Unidos", "China", "Japão", "Taiwan +\nCoreia Sul", "Índia", "ASEAN", "Golfo"],
        "fig2_ylabel": "Gigawatts (GW)",
        "fig2_source": "Fontes: Mind2Markets (2026), Futurum (2026), compilação do autor",
        "fig2_legend_tier": ["Tier 1", "Tier 2", "Tier 3"],

        "fig3_title": "Taiwan e Coreia do Sul: Posição na Cadeia\nde Valor dos Semicondutores IA (2025)",
        "fig3_ylabel": "Participação no Mercado Mundial (%)",
        "fig3_cats": ["Chips ponta\n(<7nm)", "Memória HBM\n(GPUs IA)", "Fundição\navançada", "Empacotamento\navançado"],
        "fig3_legend": ["TSMC (Taiwan)", "Samsung + SK hynix (Coreia)"],
        "fig3_source": "Fontes: dados industriais, TrendForce, IC Insights, compilação do autor",
        "fig3_risk_label": "Risco: transferência\nprodução para EUA",

        "fig4_title": "Índia: O Fosso entre Ambições de IA\ne Capacidade Instalada (2025-2026)",
        "fig4_ylabel_left": "Bilhões USD (investimentos)",
        "fig4_ylabel_right": "GW (capacidade DC instalada)",
        "fig4_cats": ["Investimentos\nanunciados (2 anos)", "Orçamento público\nIndiaAI Mission", "GPUs implantadas\n(bi$ equiv.)"],
        "fig4_source": "Fontes: IBTimes India (2026), Medium/D. Kumar (2026), Mind2Markets",
        "fig4_compare_label": "Capacidade DC (GW)",
        "fig4_countries": ["Estados Unidos\n53,7 GW", "China\n19,6 GW", "Índia\n1,4 GW"],
        "fig4_tier_label": "Tier 2: caps quantitativos de GPU",

        "fig5_title": "China: Trajetória de Autonomização da IA\nsob Restrições (2022-2030)",
        "fig5_ylabel_left": "Bilhões USD",
        "fig5_ylabel_right": "EFLOP/s (capacidade cálculo IA)",
        "fig5_source": "Fontes: IBTimes, Tom's Hardware, ITIF (2025), EastPost (2026)",
        "fig5_legend_invest": "Investimento IA (bi$)",
        "fig5_legend_eflops": "Capacidade cálculo (EFLOP/s)",
        "fig5_legend_foundry": "Participação fundições mundiais (%)",
        "fig5_annot_deepseek": "DeepSeek-V3\n(desempenho\ncompetitivo)",
        "fig5_annot_huawei": "Huawei Ascend 910c\n(~H100, 60-70% custo)",

        "fig6_title": "Síntese Comparativa: Posição Asiática\nFace ao Protecionismo de IA dos EUA",
        "fig6_countries": ["Japão", "Taiwan", "Coreia\ndo Sul", "Índia", "China", "ASEAN", "Golfo"],
        "fig6_dimensions": ["Acesso GPU\n(Tier)", "Capacidade DC\n(GW)", "Investimento\nIA (bi$)", "Autonomia\ntecnológica", "Risco\nprincipal"],
        "fig6_source": "Fonte: compilação do autor, Tabela 16 do capítulo",
        "fig6_tier_labels": ["Tier 1\n(acesso livre)", "Tier 2\n(caps)", "Tier 3\n(proibido)"],
    }
}


def setup_style():
    """Style commun pour tous les graphiques."""
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 11,
        'axes.facecolor': BG_COLOR,
        'figure.facecolor': 'white',
        'axes.grid': True,
        'grid.color': GRID_COLOR,
        'grid.alpha': 0.7,
        'axes.spines.top': False,
        'axes.spines.right': False,
    })


def save_fig(fig, name, lang_suffix):
    """Sauvegarde avec nom normalisé."""
    path = os.path.join(OUTPUT_DIR, f"{name}_{lang_suffix}.png")
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  ✓ {path}")
    return path


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 6ter.1 — Accord d'investissement US-Japon en infrastructure IA
# Page suggestion : p. 2 (après §6ter.1.1, illustration de l'accord 550 Md$)
# Données : Construction Today (2025), Taipei Times (2025)
# ═══════════════════════════════════════════════════════════════════════════
def fig1_japan_investment(L, lang_key):
    fig, ax = plt.subplots(figsize=(13, 7))

    cats = L["fig1_cats"]
    # Ventilation des 550 Md$ : énergie 332, semi-cond ~65+, DC ~98, câbles ~55
    values = [332, 65, 98, 55]
    colors = ["#E74C3C", "#3498DB", "#2ECC71", "#F39C12"]
    explode = (0.05, 0, 0, 0)

    # Graphique en barres horizontales empilées stylisées
    bars = ax.barh(cats, values, height=0.55, color=colors, edgecolor='white', linewidth=2)

    # Valeurs sur les barres
    for bar, val, detail in zip(bars, values, L["fig1_detail_labels"]):
        # Valeur à droite de la barre
        ax.text(val + 5, bar.get_y() + bar.get_height()/2,
                f"{val} Md$", va='center', fontsize=14, fontweight='bold',
                color='#333')
        # Détail à l'intérieur si la barre est assez grande
        if val > 80:
            ax.text(val/2, bar.get_y() + bar.get_height()/2,
                    detail, va='center', ha='center', fontsize=8,
                    color='white', fontweight='bold',
                    path_effects=[pe.withStroke(linewidth=2, foreground=colors[0])])

    # Annotation total
    ax.text(0.98, 0.95, L["fig1_annot"], transform=ax.transAxes,
            fontsize=16, fontweight='bold', color=JP_COLOR,
            ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor=JP_COLOR, linewidth=2))

    # Investissement domestique Japon
    ax.text(0.98, 0.82, f"{L['fig1_domestic']}\n{L['fig1_dom_val']}",
            transform=ax.transAxes, fontsize=10, color=US_COLOR,
            ha='right', va='top', fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF5FB',
                      edgecolor=US_COLOR, alpha=0.8))

    ax.set_title(L["fig1_title"], fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel(L["fig1_ylabel"], fontsize=12)
    ax.set_xlim(0, 400)
    ax.invert_yaxis()
    ax.text(0.5, -0.1, L["fig1_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')

    return save_fig(fig, "Fig_6ter.1_Japan_Investment", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 6ter.2 — Capacité installée de Data Centers (GW) en Asie vs US
# Page suggestion : p. 3 (après §6ter.1.2, comparaison de la puissance DC)
# Données : Mind2Markets (2026), Futurum (2026)
# ═══════════════════════════════════════════════════════════════════════════
def fig2_datacenter_capacity(L, lang_key):
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    cats = L["fig2_cats"]
    # US 53.7, China 19.6, Japan 12.8, Taiwan+Korea ~5, India 1.4, ASEAN ~3, Gulf ~2
    values = [53.7, 19.6, 12.8, 5.0, 1.4, 3.0, 2.0]
    # Couleurs par Tier
    tier_colors = [US_COLOR, CN_COLOR, JP_COLOR, TW_COLOR, IN_COLOR, ASEAN_COLOR, GULF_COLOR]
    # Tier classification
    tiers = ["-", "3", "1", "1", "2", "2", "2"]
    tier_edge_colors = ["#555", CN_COLOR, "#2ECC71", "#2ECC71", ACCENT3, ACCENT3, ACCENT3]

    bars = ax.bar(cats, values, width=0.6, color=tier_colors, edgecolor='white',
                  linewidth=2, alpha=0.85)

    # Valeurs sur les barres
    for bar, val, tier in zip(bars, values, tiers):
        # Valeur
        ax.text(bar.get_x() + bar.get_width()/2, val + 1.2,
                f"{val} GW", ha='center', fontsize=11, fontweight='bold', color='#333')
        # Tier badge
        if tier != "-":
            badge_color = {"1": "#2ECC71", "2": ACCENT3, "3": CN_COLOR}[tier]
            ax.text(bar.get_x() + bar.get_width()/2, val + 4,
                    f"Tier {tier}", ha='center', fontsize=8, fontweight='bold',
                    color='white',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor=badge_color, alpha=0.9))

    # Ligne repère US
    ax.axhline(y=53.7, color=US_COLOR, linewidth=1, linestyle=':', alpha=0.4)

    # Facteur multiplicatif US vs Inde
    ax.annotate('', xy=(0, 52), xytext=(4, 5),
                arrowprops=dict(arrowstyle='<->', color=CN_COLOR, lw=2.5))
    ax.text(2, 28, "×38", ha='center', fontsize=24, fontweight='bold',
            color=CN_COLOR,
            path_effects=[pe.withStroke(linewidth=3, foreground='white')])

    ax.set_title(L["fig2_title"], fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig2_ylabel"], fontsize=12)
    ax.set_ylim(0, 65)
    ax.text(0.5, -0.12, L["fig2_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')

    # Légende Tiers
    tier_patches = [mpatches.Patch(color="#2ECC71", label=L["fig2_legend_tier"][0]),
                    mpatches.Patch(color=ACCENT3, label=L["fig2_legend_tier"][1]),
                    mpatches.Patch(color=CN_COLOR, label=L["fig2_legend_tier"][2])]
    ax.legend(handles=tier_patches, loc='upper right', fontsize=9, framealpha=0.9)

    return save_fig(fig, "Fig_6ter.2_DC_Capacity_Asia", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 6ter.3 — Taiwan et Corée : chaîne de valeur semi-conducteurs IA
# Page suggestion : p. 5 (après §6ter.2.2, illustration de la domination)
# Données : TrendForce, IC Insights, données industrielles
# ═══════════════════════════════════════════════════════════════════════════
def fig3_taiwan_korea_semiconductors(L, lang_key):
    fig, ax = plt.subplots(figsize=(11, 7))

    cats = L["fig3_cats"]
    # TSMC : ~90% puces pointe, ~15% HBM, ~55% fonderie avancée, ~35% packaging
    tsmc_vals = [90, 15, 55, 35]
    # Samsung+SK hynix : ~8% pointe, ~75% HBM, ~18% fonderie, ~40% packaging
    korea_vals = [8, 75, 18, 40]

    x = np.arange(len(cats))
    width = 0.32

    bars_tw = ax.bar(x - width/2, tsmc_vals, width, color=TW_COLOR,
                     label=L["fig3_legend"][0], edgecolor='white', linewidth=1.5)
    bars_kr = ax.bar(x + width/2, korea_vals, width, color=KR_COLOR,
                     label=L["fig3_legend"][1], edgecolor='white', linewidth=1.5)

    # Valeurs sur barres
    for bar, val in zip(bars_tw, tsmc_vals):
        ax.text(bar.get_x() + bar.get_width()/2, val + 1.5, f"{val}%",
                ha='center', fontsize=13, fontweight='bold', color=TW_COLOR)
    for bar, val in zip(bars_kr, korea_vals):
        ax.text(bar.get_x() + bar.get_width()/2, val + 1.5, f"{val}%",
                ha='center', fontsize=13, fontweight='bold', color=KR_COLOR)

    # Zone dominance combinée
    combined = [t + k for t, k in zip(tsmc_vals, korea_vals)]
    for i, comb in enumerate(combined):
        if comb > 70:
            ax.annotate(f"Combiné: {comb}%", xy=(i, max(tsmc_vals[i], korea_vals[i]) + 8),
                        fontsize=9, fontweight='bold', color='#555', ha='center',
                        bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF9C4',
                                  edgecolor='#F9A825', alpha=0.8))

    # Annotation risque
    ax.text(0.98, 0.95, L["fig3_risk_label"], transform=ax.transAxes,
            fontsize=10, color=CN_COLOR, ha='right', va='top', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFEBEE',
                      edgecolor=CN_COLOR, alpha=0.9))

    # Ligne 50% seuil dominance
    ax.axhline(y=50, color='gray', linewidth=1, linestyle='--', alpha=0.5)
    ax.text(len(cats) - 0.5, 52, "50%", fontsize=9, color='gray', fontstyle='italic')

    ax.set_title(L["fig3_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig3_ylabel"], fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=11)
    ax.set_ylim(0, 110)
    ax.legend(fontsize=11, framealpha=0.9, loc='upper left')
    ax.text(0.5, -0.12, L["fig3_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')

    return save_fig(fig, "Fig_6ter.3_Taiwan_Korea_Semicon", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 6ter.4 — Inde : ambitions vs réalité du compute
# Page suggestion : p. 7 (après §6ter.3.2, illustration du fossé structurel)
# Données : IBTimes India (2026), Medium/D. Kumar (2026), Mind2Markets
# ═══════════════════════════════════════════════════════════════════════════
def fig4_india_gap(L, lang_key):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7),
                                    gridspec_kw={'width_ratios': [1.3, 1]})

    # ── Panneau gauche : investissements annoncés ──
    cats = L["fig4_cats"]
    values = [200, 1.2, 0.8]  # 200 Md$ annoncés, 1.2 Md$ public, ~0.8 Md$ GPU
    colors = [IN_COLOR, "#F5B041", "#EB984E"]

    bars = ax1.bar(cats, values, width=0.55, color=colors, edgecolor='white', linewidth=2)

    for bar, val in zip(bars, values):
        if val >= 10:
            ax1.text(bar.get_x() + bar.get_width()/2, val + 5,
                     f"${val:.0f}B", ha='center', fontsize=14, fontweight='bold', color='#333')
        else:
            ax1.text(bar.get_x() + bar.get_width()/2, val + 5,
                     f"${val:.1f}B", ha='center', fontsize=14, fontweight='bold', color='#333')

    ax1.set_title(L["fig4_title"], fontsize=12, fontweight='bold', pad=15)
    ax1.set_ylabel(L["fig4_ylabel_left"], fontsize=11)
    ax1.set_ylim(0, 240)

    # Tier 2 badge
    ax1.text(0.5, 0.92, L["fig4_tier_label"], transform=ax1.transAxes,
             fontsize=10, fontweight='bold', color='white', ha='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=ACCENT3, alpha=0.9))

    # ── Panneau droit : comparaison capacité DC (GW) ──
    dc_countries = L["fig4_countries"]
    dc_values = [53.7, 19.6, 1.4]
    dc_colors = [US_COLOR, CN_COLOR, IN_COLOR]

    bars2 = ax2.bar(dc_countries, dc_values, width=0.55, color=dc_colors,
                    edgecolor='white', linewidth=2, alpha=0.85)

    for bar, val in zip(bars2, dc_values):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 1.5,
                 f"{val} GW", ha='center', fontsize=13, fontweight='bold', color='#333')

    # Flèche ×38
    ax2.annotate('', xy=(0, 50), xytext=(2, 5),
                 arrowprops=dict(arrowstyle='<->', color=CN_COLOR, lw=2.5))
    ax2.text(1, 28, "×38", ha='center', fontsize=22, fontweight='bold',
             color=CN_COLOR,
             path_effects=[pe.withStroke(linewidth=3, foreground='white')])

    ax2.set_title(L["fig4_compare_label"], fontsize=12, fontweight='bold', pad=15)
    ax2.set_ylabel(L["fig4_ylabel_right"], fontsize=11)
    ax2.set_ylim(0, 65)

    fig.text(0.5, -0.02, L["fig4_source"], fontsize=8,
             color='gray', ha='center', fontstyle='italic')

    plt.tight_layout()
    return save_fig(fig, "Fig_6ter.4_India_Gap", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 6ter.5 — Chine : trajectoire d'autonomisation IA sous restrictions
# Page suggestion : p. 9 (après §6ter.4.2, illustration du paradoxe)
# Données : IBTimes, Tom's Hardware, ITIF (2025), EastPost (2026)
# ═══════════════════════════════════════════════════════════════════════════
def fig5_china_autonomization(L, lang_key):
    fig, ax1 = plt.subplots(figsize=(13, 7.5))

    years = [2022, 2023, 2024, 2025, 2026, 2028, 2030]
    # Investissement IA Chine (Md$) — estimation croissante
    invest = [35, 55, 80, 125, 195, 280, 400]
    # Capacité compute (EFLOP/s)
    eflops = [80, 130, 246, 300, 400, 550, 750]
    # Part fonderies mondiales (%)
    foundry_share = [18, 19, 21, 23, 25, 27, 30]

    # Axe 1 : Investissement (barres)
    bar_colors = [CN_COLOR if y <= 2025 else '#E57373' for y in years]
    bars = ax1.bar(years, invest, width=0.6, color=bar_colors, alpha=0.7,
                   edgecolor='white', linewidth=1.5, label=L["fig5_legend_invest"])

    for bar, val, yr in zip(bars, invest, years):
        if yr in [2022, 2025, 2030]:
            ax1.text(bar.get_x() + bar.get_width()/2, val + 8,
                     f"${val}B", ha='center', fontsize=10, fontweight='bold', color=CN_COLOR)

    ax1.set_xlabel("")
    ax1.set_ylabel(L["fig5_ylabel_left"], fontsize=11, color=CN_COLOR)
    ax1.tick_params(axis='y', labelcolor=CN_COLOR)
    ax1.set_ylim(0, 480)

    # Axe 2 : EFLOP/s (ligne)
    ax2 = ax1.twinx()
    ax2.plot(years, eflops, color=ACCENT1, linewidth=3, marker='D', markersize=8,
             label=L["fig5_legend_eflops"], zorder=5)
    ax2.set_ylabel(L["fig5_ylabel_right"], fontsize=11, color=ACCENT1)
    ax2.tick_params(axis='y', labelcolor=ACCENT1)
    ax2.set_ylim(0, 900)

    # Part fonderies (annotations sur la courbe)
    for i, (yr, fs) in enumerate(zip(years, foundry_share)):
        if yr in [2022, 2025, 2030]:
            ax2.annotate(f"{fs}%", xy=(yr, eflops[i]),
                        xytext=(yr + 0.3, eflops[i] + 60),
                        fontsize=9, color=ACCENT2, fontweight='bold',
                        bbox=dict(boxstyle='round,pad=0.2', facecolor='#F3E5F5',
                                  edgecolor=ACCENT2, alpha=0.8),
                        arrowprops=dict(arrowstyle='->', color=ACCENT2, lw=1))

    # Zone restrictions (2022-2024)
    ax1.axvspan(2021.5, 2024.5, alpha=0.06, color=US_COLOR)
    ax1.text(2023, 450, "Export controls\n2022-2024", fontsize=9, color=US_COLOR,
             ha='center', fontstyle='italic', fontweight='bold')

    # Annotations DeepSeek et Huawei
    ax1.annotate(L["fig5_annot_deepseek"], xy=(2024.5, 80),
                xytext=(2025.5, 350), fontsize=9, color='#1565C0',
                fontweight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD',
                          edgecolor='#1565C0', alpha=0.9),
                arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.5))

    ax1.annotate(L["fig5_annot_huawei"], xy=(2025, 125),
                xytext=(2027, 380), fontsize=9, color='#B71C1C',
                fontweight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE',
                          edgecolor='#B71C1C', alpha=0.9),
                arrowprops=dict(arrowstyle='->', color='#B71C1C', lw=1.5))

    # Titre et source
    ax1.set_title(L["fig5_title"], fontsize=14, fontweight='bold', pad=15)

    # Légende combinée
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    foundry_patch = mpatches.Patch(color=ACCENT2, label=L["fig5_legend_foundry"])
    ax1.legend(lines1 + lines2 + [foundry_patch],
               labels1 + labels2 + [L["fig5_legend_foundry"]],
               loc='upper left', fontsize=9, framealpha=0.9)

    fig.text(0.5, -0.02, L["fig5_source"], fontsize=8,
             color='gray', ha='center', fontstyle='italic')

    return save_fig(fig, "Fig_6ter.5_China_Autonomization", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 6ter.6 — Synthèse comparative : position asiatique par Tier
# Page suggestion : p. 12 (après §6ter.6, Tableau 16, synthèse visuelle)
# Données : compilation auteur (Tableau 16)
# ═══════════════════════════════════════════════════════════════════════════
def fig6_synthesis_comparative(L, lang_key):
    fig, ax = plt.subplots(figsize=(14, 8.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Titre
    ax.text(7, 8.6, L["fig6_title"], ha='center', fontsize=14, fontweight='bold')

    # ── Colonnes Tier ──
    # Tier 1 (gauche) : Japon, Taiwan, Corée
    # Tier 2 (centre) : Inde, ASEAN, Golfe
    # Tier 3 (droite) : Chine

    tier_zones = [
        (0.3, 2.5, 4.2, 5.8, "#2ECC71", L["fig6_tier_labels"][0]),   # Tier 1
        (5.0, 2.5, 4.2, 5.8, ACCENT3, L["fig6_tier_labels"][1]),      # Tier 2
        (9.8, 2.5, 4.0, 5.8, CN_COLOR, L["fig6_tier_labels"][2]),     # Tier 3
    ]

    for x, y, w, h, color, label in tier_zones:
        rect = mpatches.FancyBboxPatch((x, y), w, h,
                                        boxstyle="round,pad=0.2",
                                        facecolor=color, alpha=0.08,
                                        edgecolor=color, linewidth=2.5)
        ax.add_patch(rect)
        # Label Tier en haut
        ax.text(x + w/2, y + h - 0.3, label, ha='center', va='top',
                fontsize=11, fontweight='bold', color=color)

    # ── Pays dans chaque Tier ──
    # Tier 1
    tier1_countries = [
        ("Japon", "🇯🇵", "12,8 GW\n135 Md$\nAlliance US", JP_COLOR),
        ("Taiwan", "🇹🇼", "~3 GW\nTSMC 90%\nSilicon Shield", TW_COLOR),
        ("Corée", "🇰🇷", "~5 GW\n6,7 Md$\nHBM dominant", KR_COLOR),
    ]
    for i, (name, flag, info, color) in enumerate(tier1_countries):
        bx = 0.6 + i * 1.35
        by = 3.0
        rect = mpatches.FancyBboxPatch((bx, by), 1.2, 3.5,
                                        boxstyle="round,pad=0.1",
                                        facecolor=color, alpha=0.12,
                                        edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(bx + 0.6, by + 3.1, name, ha='center', fontsize=9,
                fontweight='bold', color=color)
        ax.text(bx + 0.6, by + 1.5, info, ha='center', fontsize=7.5,
                color='#333', linespacing=1.4)

    # Tier 2
    tier2_countries = [
        ("Inde", "🇮🇳", "1,4 GW\n200+ Md$\nCompute export", IN_COLOR),
        ("ASEAN", "🌏", "~3 GW\n15+ Md$\nUS-CN compét.", ASEAN_COLOR),
        ("Golfe", "🏜️", "~2 GW\n15+ Md$\nCapital massif", GULF_COLOR),
    ]
    for i, (name, flag, info, color) in enumerate(tier2_countries):
        bx = 5.3 + i * 1.35
        by = 3.0
        rect = mpatches.FancyBboxPatch((bx, by), 1.2, 3.5,
                                        boxstyle="round,pad=0.1",
                                        facecolor=color, alpha=0.12,
                                        edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(bx + 0.6, by + 3.1, name, ha='center', fontsize=9,
                fontweight='bold', color=color)
        ax.text(bx + 0.6, by + 1.5, info, ha='center', fontsize=7.5,
                color='#333', linespacing=1.4)

    # Tier 3 : Chine
    bx, by = 10.1, 3.0
    rect = mpatches.FancyBboxPatch((bx, by), 3.4, 3.5,
                                    boxstyle="round,pad=0.1",
                                    facecolor=CN_COLOR, alpha=0.12,
                                    edgecolor=CN_COLOR, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(bx + 1.7, by + 3.1, "Chine", ha='center', fontsize=11,
            fontweight='bold', color=CN_COLOR)
    ax.text(bx + 1.7, by + 1.5,
            "19,6 GW\n125+ Md$ (2025)\n246 EFLOP/s\nHuawei Ascend\nDeepSeek-V3\nÉcosystème parallèle",
            ha='center', fontsize=8, color='#333', linespacing=1.3)

    # ── Flèches dynamiques en bas ──
    # Dynamique 1 : Alliance US ← Tier 1
    ax.annotate("Alliance tech.\nUS-Asie", xy=(2.5, 2.3), fontsize=8,
                fontweight='bold', color="#2ECC71", ha='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor="#2ECC71", alpha=0.9))

    # Dynamique 2 : Bifurcation
    ax.annotate("Compétition\nUS-Chine", xy=(7.5, 2.3), fontsize=8,
                fontweight='bold', color=ACCENT3, ha='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor=ACCENT3, alpha=0.9))

    # Dynamique 3 : Autonomisation
    ax.annotate("Autonomisation\nforcée", xy=(11.8, 2.3), fontsize=8,
                fontweight='bold', color=CN_COLOR, ha='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor=CN_COLOR, alpha=0.9))

    # Source
    ax.text(7, 0.3, L["fig6_source"], ha='center', fontsize=8,
            color='gray', fontstyle='italic')

    return save_fig(fig, "Fig_6ter.6_Synthesis_Asia", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# MAIN — Génération pour les 3 langues
# ═══════════════════════════════════════════════════════════════════════════
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()

    print("=" * 70)
    print(" CHAPITRE VI TER — Génération des graphiques en 3 langues")
    print("=" * 70)

    all_files = []

    for lang_key, L in LANGS.items():
        print(f"\n{'─'*50}")
        print(f" Langue : {L['suffix']}")
        print(f"{'─'*50}")

        all_files.append(fig1_japan_investment(L, lang_key))
        all_files.append(fig2_datacenter_capacity(L, lang_key))
        all_files.append(fig3_taiwan_korea_semiconductors(L, lang_key))
        all_files.append(fig4_india_gap(L, lang_key))
        all_files.append(fig5_china_autonomization(L, lang_key))
        all_files.append(fig6_synthesis_comparative(L, lang_key))

    print(f"\n{'='*70}")
    print(f" Total : {len(all_files)} fichiers générés dans {OUTPUT_DIR}/")
    print(f"{'='*70}")

    # Résumé des insertions
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║  GUIDE D'INSERTION — Chapitre VI ter (Conséquences pour l'Asie)        ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  Fig 6ter.1  Investissements US-Japon      → p. 2  (après §6ter.1.1)  ║
║              Ventilation des 550 Md$ : énergie, semi-cond., DC         ║
║                                                                        ║
║  Fig 6ter.2  Capacité DC Asie vs US        → p. 3  (après §6ter.1.2)  ║
║              Comparaison GW : US 53,7 vs Inde 1,4 (×38)               ║
║                                                                        ║
║  Fig 6ter.3  Taiwan/Corée semi-conducteurs → p. 5  (après §6ter.2.2)  ║
║              TSMC 90% puces pointe + SK hynix 75% HBM                  ║
║                                                                        ║
║  Fig 6ter.4  Inde : ambition vs réalité    → p. 7  (après §6ter.3.2)  ║
║              200 Md$ annoncés vs 1,4 GW installés                      ║
║                                                                        ║
║  Fig 6ter.5  Chine : autonomisation        → p. 9  (après §6ter.4.2)  ║
║              125 Md$ invest. + 246 EFLOP/s + Huawei/DeepSeek           ║
║                                                                        ║
║  Fig 6ter.6  Synthèse comparative Tiers    → p. 12 (après §6ter.6)    ║
║              Vue d'ensemble : Tier 1/2/3 + dynamiques                  ║
║                                                                        ║
╚══════════════════════════════════════════════════════════════════════════╝
    """)

    return all_files


if __name__ == "__main__":
    main()
