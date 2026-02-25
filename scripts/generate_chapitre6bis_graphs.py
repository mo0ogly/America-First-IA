#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre VI bis : Amérique du Sud et Brésil
 Générateur de graphiques en 3 langues (FR / EN / PT-BR)
=============================================================================
 Usage  : python generate_chapitre6bis_graphs.py
 Output : PNG files in ./output/figures_ch6bis/

 GUIDE D'INSERTION (pages du chapitre VI bis) :
 ──────────────────────────────────────────────────────────────────
 Fig 6bis.1  Déficit invest. IA LATAM vs monde     → p. 2  (après §6bis.1.1)
 Fig 6bis.2  Mégaprojets DC Brésil (US vs Chine)   → p. 4  (après §6bis.2.2)
 Fig 6bis.3  5 canaux d'impact protectionnisme      → p. 6  (après §6bis.3.2)
 Fig 6bis.4  Scénarios Brésil 2026-2030             → p. 8  (après §6bis.4)
 Fig 6bis.5  Triple fracture Amérique du Sud        → p. 10 (après §6bis.6)
 Fig 6bis.6  Comparaison France vs Brésil           → p. 11 (après §6bis.6)
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
FIGSIZE_TALL = (11, 8)

US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
FR_COLOR = "#2E86C1"
CN_COLOR = "#C0392B"
BR_COLOR = "#27AE60"
LATAM_COLOR = "#1ABC9C"
ACCENT1 = "#148F77"
ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"
BG_COLOR = "#FAFBFC"
GRID_COLOR = "#E0E0E0"

LANGS = {
    "fr": {
        "suffix": "FR",
        "fig1_title": "Déficit d'investissement IA de l'Amérique latine\n(part PIB vs part investissement mondial IA)",
        "fig1_ylabel": "Part mondiale (%)",
        "fig1_cats": ["PIB mondial", "Investissement\nmondial IA", "Capacité DC\n(colocation)", "Modèles IA\nnotables", "Startups IA", "Capital-risque\nIA"],
        "fig1_source": "Sources : CEPALC/CENIA ILIA 2025, Banque mondiale (2025)",
        "fig1_legend": ["Amérique latine", "Pays à haut revenu"],
        "fig1_ratio": "Ratio déficit : ×5,9",

        "fig2_title": "Mégaprojets de data centers IA au Brésil\n(investissements US vs Chine, 2025-2033)",
        "fig2_ylabel": "Capacité planifiée (GW)",
        "fig2_source": "Sources : Bloomberg (2025), IndustrialInfo (2026), Introl (2025)",
        "fig2_legend": ["Projets à capitaux chinois", "Projets à capitaux US/brésiliens"],
        "fig2_projects": ["TikTok\nPecém", "Scala\nAI City", "Elea Rio\nAI City", "Microsoft\nAzure", "AWS\nSão Paulo"],
        "fig2_annot": "Mix 83% renouvelable\nCoût: ~0,08 $/kWh",

        "fig3_title": "Cinq canaux d'impact du protectionnisme IA\nsur l'Amérique du Sud",
        "fig3_channels": ["1. Contrainte\nhardware GPU\n(caps Tier 2)", "2. Dépendance\ncloud US\nrenforcée", "3. Bifurcation\ntechnologique\nUS-Chine", "4. Brain drain\namplifié", "5. Fossé de\nproductivité\nélargi"],
        "fig3_source": "Source : élaboration auteur, §6bis.3.2",
        "fig3_severity": "Sévérité de l'impact",

        "fig4_title": "Scénarios du Brésil face au protectionnisme IA\n(2026-2030)",
        "fig4_scenarios": ["A' : Hub neutre\ndual US-Chine", "B' : Sanctions\nsecondaires", "C' : Alignement\npro-US", "D' : Souveraineté\nrégionale LATAM"],
        "fig4_ylabel": "Probabilité estimée (%)",
        "fig4_source": "Source : construction auteur, Tableau 15",

        "fig5_title": "Triple fracture de l'Amérique du Sud\nface au protectionnisme IA",
        "fig5_fractures": ["Fracture\nNord-Sud", "Fracture\nEst-Ouest", "Fracture\nintra-régionale"],
        "fig5_source": "Source : élaboration auteur, §6bis.6",

        "fig6_title": "Comparaison France vs Brésil :\natouts et vulnérabilités face au protectionnisme IA",
        "fig6_dims": ["Atout\nénergétique", "Champion\nnational IA", "Classification\nTier", "Coût du\ncapital", "Capacité DC\ninstallée", "Autonomie\nhardware"],
        "fig6_legend": ["France", "Brésil"],
        "fig6_source": "Source : compilation auteur, §6bis.6",
    },
    "en": {
        "suffix": "EN",
        "fig1_title": "Latin America's AI Investment Deficit\n(GDP share vs global AI investment share)",
        "fig1_ylabel": "Global share (%)",
        "fig1_cats": ["Global GDP", "Global AI\ninvestment", "DC capacity\n(colocation)", "Notable AI\nmodels", "AI startups", "AI venture\ncapital"],
        "fig1_source": "Sources: CEPALC/CENIA ILIA 2025, World Bank (2025)",
        "fig1_legend": ["Latin America", "High-income countries"],
        "fig1_ratio": "Deficit ratio: ×5.9",

        "fig2_title": "Major AI Data Center Projects in Brazil\n(US vs Chinese investments, 2025-2033)",
        "fig2_ylabel": "Planned capacity (GW)",
        "fig2_source": "Sources: Bloomberg (2025), IndustrialInfo (2026), Introl (2025)",
        "fig2_legend": ["Chinese-backed projects", "US/Brazilian-backed projects"],
        "fig2_projects": ["TikTok\nPecém", "Scala\nAI City", "Elea Rio\nAI City", "Microsoft\nAzure", "AWS\nSão Paulo"],
        "fig2_annot": "83% renewable mix\nCost: ~$0.08/kWh",

        "fig3_title": "Five Channels of AI Protectionism Impact\non South America",
        "fig3_channels": ["1. GPU hardware\nconstraint\n(Tier 2 caps)", "2. Reinforced\nUS cloud\ndependency", "3. US-China\ntechnological\nbifurcation", "4. Amplified\nbrain drain", "5. Widened\nproductivity\ngap"],
        "fig3_source": "Source: author's elaboration, §6bis.3.2",
        "fig3_severity": "Impact severity",

        "fig4_title": "Brazil's Scenarios Facing AI Protectionism\n(2026-2030)",
        "fig4_scenarios": ["A': Neutral dual\nhub US-China", "B': Secondary\nsanctions", "C': Pro-US\nalignment", "D': Regional\nLATAM sovereignty"],
        "fig4_ylabel": "Estimated probability (%)",
        "fig4_source": "Source: author construction, Table 15",

        "fig5_title": "South America's Triple Fracture\nFacing AI Protectionism",
        "fig5_fractures": ["North-South\nfracture", "East-West\nfracture", "Intra-regional\nfracture"],
        "fig5_source": "Source: author's elaboration, §6bis.6",

        "fig6_title": "France vs Brazil Comparison:\nAssets and Vulnerabilities Facing AI Protectionism",
        "fig6_dims": ["Energy\nasset", "National AI\nchampion", "Tier\nclassification", "Cost of\ncapital", "Installed DC\ncapacity", "Hardware\nautonomy"],
        "fig6_legend": ["France", "Brazil"],
        "fig6_source": "Source: author compilation, §6bis.6",
    },
    "pt": {
        "suffix": "PT-BR",
        "fig1_title": "Déficit de Investimento em IA da América Latina\n(participação no PIB vs investimento mundial em IA)",
        "fig1_ylabel": "Participação mundial (%)",
        "fig1_cats": ["PIB mundial", "Investimento\nmundial IA", "Capacidade DC\n(colocation)", "Modelos IA\nnotáveis", "Startups IA", "Capital de\nrisco IA"],
        "fig1_source": "Fontes: CEPAL/CENIA ILIA 2025, Banco Mundial (2025)",
        "fig1_legend": ["América Latina", "Países de alta renda"],
        "fig1_ratio": "Razão do déficit: ×5,9",

        "fig2_title": "Megaprojetos de Data Centers IA no Brasil\n(investimentos EUA vs China, 2025-2033)",
        "fig2_ylabel": "Capacidade planejada (GW)",
        "fig2_source": "Fontes: Bloomberg (2025), IndustrialInfo (2026), Introl (2025)",
        "fig2_legend": ["Projetos com capital chinês", "Projetos com capital EUA/brasileiro"],
        "fig2_projects": ["TikTok\nPecém", "Scala\nAI City", "Elea Rio\nAI City", "Microsoft\nAzure", "AWS\nSão Paulo"],
        "fig2_annot": "Mix 83% renovável\nCusto: ~US$ 0,08/kWh",

        "fig3_title": "Cinco Canais de Impacto do Protecionismo de IA\nna América do Sul",
        "fig3_channels": ["1. Restrição\nhardware GPU\n(caps Tier 2)", "2. Dependência\nde cloud EUA\nreforçada", "3. Bifurcação\ntecnológica\nEUA-China", "4. Fuga de\ncérebros\namplificada", "5. Fosso de\nprodutividade\nampliado"],
        "fig3_source": "Fonte: elaboração do autor, §6bis.3.2",
        "fig3_severity": "Severidade do impacto",

        "fig4_title": "Cenários do Brasil Face ao Protecionismo de IA\n(2026-2030)",
        "fig4_scenarios": ["A': Hub neutro\ndual EUA-China", "B': Sanções\nsecundárias", "C': Alinhamento\npró-EUA", "D': Soberania\nregional LATAM"],
        "fig4_ylabel": "Probabilidade estimada (%)",
        "fig4_source": "Fonte: construção do autor, Tabela 15",

        "fig5_title": "Tripla Fratura da América do Sul\nFace ao Protecionismo de IA",
        "fig5_fractures": ["Fratura\nNorte-Sul", "Fratura\nLeste-Oeste", "Fratura\nintra-regional"],
        "fig5_source": "Fonte: elaboração do autor, §6bis.6",

        "fig6_title": "Comparação França vs Brasil:\nAtivos e Vulnerabilidades Face ao Protecionismo de IA",
        "fig6_dims": ["Ativo\nenergético", "Campeão\nnacional IA", "Classificação\nTier", "Custo do\ncapital", "Capacidade DC\ninstalada", "Autonomia\nhardware"],
        "fig6_legend": ["França", "Brasil"],
        "fig6_source": "Fonte: compilação do autor, §6bis.6",
    }
}


def setup_style():
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 11,
        'axes.facecolor': BG_COLOR, 'figure.facecolor': 'white',
        'axes.grid': True, 'grid.color': GRID_COLOR, 'grid.alpha': 0.7,
        'axes.spines.top': False, 'axes.spines.right': False,
    })

def save_fig(fig, name, lang_suffix):
    path = os.path.join(OUTPUT_DIR, f"{name}_{lang_suffix}.png")
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  ✓ {path}")
    return path


# ═══════════════════════════════════════════════════════════════════════════
# FIG 6bis.1 — Déficit d'investissement IA LATAM vs pays riches
# Page : p. 2 (après §6bis.1.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig1_latam_deficit(L, lang_key):
    fig, ax = plt.subplots(figsize=(13, 7))
    cats = L["fig1_cats"]
    latam = [6.6, 1.12, 5, 2, 3, 2]
    high_income = [60, 80, 77, 87, 86, 91]

    x = np.arange(len(cats))
    w = 0.32
    bars1 = ax.bar(x - w/2, latam, w, color=BR_COLOR, label=L["fig1_legend"][0],
                   edgecolor='white', linewidth=1.5)
    bars2 = ax.bar(x + w/2, high_income, w, color=US_COLOR, label=L["fig1_legend"][1],
                   edgecolor='white', linewidth=1.5, alpha=0.75)

    for bar, val in zip(bars1, latam):
        ax.text(bar.get_x() + bar.get_width()/2, val + 1.5, f"{val}%",
                ha='center', fontsize=11, fontweight='bold', color=BR_COLOR)
    for bar, val in zip(bars2, high_income):
        ax.text(bar.get_x() + bar.get_width()/2, val + 1.5, f"{val}%",
                ha='center', fontsize=11, fontweight='bold', color=US_COLOR)

    # Gap annotation on first two bars
    ax.annotate(L["fig1_ratio"], xy=(0.5, 50), fontsize=14, fontweight='bold',
                color=CN_COLOR, ha='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFEBEE',
                          edgecolor=CN_COLOR, alpha=0.9))

    ax.set_title(L["fig1_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig1_ylabel"], fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=10)
    ax.set_ylim(0, 105)
    ax.legend(fontsize=11, framealpha=0.9, loc='upper left')
    ax.text(0.5, -0.12, L["fig1_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_6bis.1_LATAM_AI_Deficit", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 6bis.2 — Mégaprojets DC Brésil (US vs Chine)
# Page : p. 4 (après §6bis.2.2)
# ═══════════════════════════════════════════════════════════════════════════
def fig2_brazil_megaprojects(L, lang_key):
    fig, ax = plt.subplots(figsize=(12, 7))
    projects = L["fig2_projects"]
    # Capacité max planifiée (GW) : Pecém 1, Scala 5, Elea 3.2, MS ~0.3, AWS ~0.2
    capacities = [1.0, 5.0, 3.2, 0.3, 0.2]
    # investissement (Md$) pour la taille des marqueurs
    invest = [38, 8, 6, 2.7, 1.5]
    # Origine : CN, BR/US, BR/US, US, US
    colors = [CN_COLOR, BR_COLOR, BR_COLOR, US_COLOR, US_COLOR]
    is_chinese = [True, False, False, False, False]

    bars = ax.bar(projects, capacities, width=0.55, color=colors, edgecolor='white',
                  linewidth=2, alpha=0.85)

    for bar, val, inv, cn in zip(bars, capacities, invest, is_chinese):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.15,
                f"{val} GW\n(~${inv}B)", ha='center', fontsize=10,
                fontweight='bold', color='#333')

    # Annotation énergie renouvelable
    ax.text(0.98, 0.95, L["fig2_annot"], transform=ax.transAxes,
            fontsize=11, color=BR_COLOR, ha='right', va='top', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#E8F8F5',
                      edgecolor=BR_COLOR, linewidth=2))

    # Légende
    cn_patch = mpatches.Patch(color=CN_COLOR, label=L["fig2_legend"][0])
    us_patch = mpatches.Patch(color=BR_COLOR, label=L["fig2_legend"][1])
    ax.legend(handles=[cn_patch, us_patch], fontsize=10, framealpha=0.9, loc='upper left')

    ax.set_title(L["fig2_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig2_ylabel"], fontsize=12)
    ax.set_ylim(0, 6.5)
    ax.text(0.5, -0.12, L["fig2_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_6bis.2_Brazil_Megaprojects", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 6bis.3 — 5 canaux d'impact (schéma conceptuel)
# Page : p. 6 (après §6bis.3.2)
# ═══════════════════════════════════════════════════════════════════════════
def fig3_five_channels(L, lang_key):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    ax.text(7, 6.6, L["fig3_title"], ha='center', fontsize=14, fontweight='bold')

    channels = L["fig3_channels"]
    severities = [0.85, 0.70, 0.95, 0.65, 0.80]  # normalized severity
    colors_ch = [CN_COLOR, US_COLOR, ACCENT2, ACCENT3, "#5D6D7E"]
    x_positions = [1.2, 3.8, 6.4, 9.0, 11.6]

    for i, (x, ch, sev, col) in enumerate(zip(x_positions, channels, severities, colors_ch)):
        # Bar height proportional to severity
        h = sev * 4.5
        rect = mpatches.FancyBboxPatch((x, 1.2), 2.2, h,
                                        boxstyle="round,pad=0.15",
                                        facecolor=col, alpha=0.15,
                                        edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + 1.1, 1.2 + h/2, ch, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=col, linespacing=1.3)
        # Severity bar
        ax.barh(0.6, sev * 2.2, left=x, height=0.35, color=col, alpha=0.6)
        ax.text(x + sev * 2.2 + 0.1, 0.6, f"{int(sev*100)}%", va='center',
                fontsize=8, fontweight='bold', color=col)

    ax.text(7, 0.15, L["fig3_severity"], ha='center', fontsize=10,
            fontweight='bold', color='#555')

    # Arrow showing cascading effect
    for i in range(4):
        ax.annotate('', xy=(x_positions[i+1], 3.5),
                    xytext=(x_positions[i] + 2.2, 3.5),
                    arrowprops=dict(arrowstyle='->', color='#AAA', lw=1.5))

    ax.text(7, -0.1, L["fig3_source"], ha='center', fontsize=8,
            color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_6bis.3_Five_Channels", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 6bis.4 — Scénarios Brésil 2026-2030
# Page : p. 8 (après §6bis.4)
# ═══════════════════════════════════════════════════════════════════════════
def fig4_brazil_scenarios(L, lang_key):
    fig, ax = plt.subplots(figsize=(12, 7))

    scenarios = L["fig4_scenarios"]
    probs_mid = [40, 17.5, 22.5, 12.5]  # midpoints
    probs_low = [35, 15, 20, 10]
    probs_high = [45, 20, 25, 15]
    colors = [BR_COLOR, CN_COLOR, US_COLOR, ACCENT2]

    bars = ax.barh(scenarios, probs_mid, height=0.5, color=colors,
                   edgecolor='white', linewidth=2, alpha=0.8)

    # Error bars (range)
    for i, (bar, lo, hi, mid) in enumerate(zip(bars, probs_low, probs_high, probs_mid)):
        ax.plot([lo, hi], [bar.get_y() + bar.get_height()/2]*2,
                color=colors[i], linewidth=3, alpha=0.4)
        ax.plot([lo, lo], [bar.get_y() + bar.get_height()/2 - 0.1,
                           bar.get_y() + bar.get_height()/2 + 0.1],
                color=colors[i], linewidth=2)
        ax.plot([hi, hi], [bar.get_y() + bar.get_height()/2 - 0.1,
                           bar.get_y() + bar.get_height()/2 + 0.1],
                color=colors[i], linewidth=2)
        ax.text(hi + 1.5, bar.get_y() + bar.get_height()/2,
                f"{lo}–{hi}%", va='center', fontsize=12, fontweight='bold', color=colors[i])

    ax.set_title(L["fig4_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel(L["fig4_ylabel"], fontsize=12)
    ax.set_xlim(0, 55)
    ax.invert_yaxis()
    ax.text(0.5, -0.1, L["fig4_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_6bis.4_Brazil_Scenarios", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 6bis.5 — Triple fracture Amérique du Sud (schéma conceptuel)
# Page : p. 10 (après §6bis.6)
# ═══════════════════════════════════════════════════════════════════════════
def fig5_triple_fracture(L, lang_key):
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    ax.text(6.5, 7.6, L["fig5_title"], ha='center', fontsize=14, fontweight='bold')

    fracture_data = [
        (1.0, 4.0, CN_COLOR, L["fig5_fractures"][0],
         "CACI US/BR\n≈ 50-100:1\n(vs US/EU 7-12:1)"),
        (5.0, 4.0, ACCENT2, L["fig5_fractures"][1],
         "Cloud US (55%)\nvs Infra. chinoise\n(ByteDance Pecém)\n→ 2 écosystèmes"),
        (9.0, 4.0, ACCENT3, L["fig5_fractures"][2],
         "Brésil: 41% LATAM\nChili: pionnier\nAutres: exclus\n→ fossé interne"),
    ]

    for x, y, color, title, desc in fracture_data:
        rect = mpatches.FancyBboxPatch((x, y), 3.2, 3.0,
                                        boxstyle="round,pad=0.2",
                                        facecolor=color, alpha=0.1,
                                        edgecolor=color, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + 1.6, y + 2.6, title, ha='center', fontsize=11,
                fontweight='bold', color=color)
        ax.text(x + 1.6, y + 1.2, desc, ha='center', fontsize=9,
                color='#333', linespacing=1.3)

    # Connecting arrows between fractures
    for i in range(2):
        x1 = 1.0 + i * 4.0 + 3.2
        x2 = 1.0 + (i+1) * 4.0
        ax.annotate('', xy=(x2, 5.5), xytext=(x1, 5.5),
                    arrowprops=dict(arrowstyle='<->', color='#888', lw=2, linestyle='--'))

    # Bottom: convergence arrow
    ax.annotate("→ Dépendance structurelle amplifiée",
                xy=(6.5, 3.5), fontsize=12, fontweight='bold', color='#555',
                ha='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF9C4',
                          edgecolor='#F9A825', alpha=0.9))

    ax.text(6.5, 0.3, L["fig5_source"], ha='center', fontsize=8,
            color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_6bis.5_Triple_Fracture", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 6bis.6 — Radar : France vs Brésil
# Page : p. 11 (après §6bis.6)
# ═══════════════════════════════════════════════════════════════════════════
def fig6_france_brazil_radar(L, lang_key):
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

    dims = L["fig6_dims"]
    N = len(dims)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    # Scores /10 : France vs Brazil
    france = [9, 8, 9, 7, 6, 3]  # nucléaire, Mistral, Tier1, coût capital ok, DC moyen, pas d'autonomie HW
    brazil = [8, 4, 5, 3, 4, 1]  # renouvelable, pas de champion, Tier2, Selic 14%, DC faible, zéro HW
    france += france[:1]
    brazil += brazil[:1]

    ax.plot(angles, france, 'o-', linewidth=2.5, color=FR_COLOR, label=L["fig6_legend"][0])
    ax.fill(angles, france, alpha=0.15, color=FR_COLOR)
    ax.plot(angles, brazil, 's-', linewidth=2.5, color=BR_COLOR, label=L["fig6_legend"][1])
    ax.fill(angles, brazil, alpha=0.15, color=BR_COLOR)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dims, fontsize=10, fontweight='bold')
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=8, color='gray')
    ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), fontsize=11, framealpha=0.9)

    ax.set_title(L["fig6_title"], fontsize=13, fontweight='bold', pad=25, y=1.08)
    fig.text(0.5, 0.02, L["fig6_source"], fontsize=8,
             color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_6bis.6_France_Brazil_Radar", L["suffix"])


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()
    print("=" * 70)
    print(" CHAPITRE VI BIS — Génération des graphiques en 3 langues")
    print("=" * 70)
    all_files = []
    for lang_key, L in LANGS.items():
        print(f"\n{'─'*50}\n Langue : {L['suffix']}\n{'─'*50}")
        all_files.append(fig1_latam_deficit(L, lang_key))
        all_files.append(fig2_brazil_megaprojects(L, lang_key))
        all_files.append(fig3_five_channels(L, lang_key))
        all_files.append(fig4_brazil_scenarios(L, lang_key))
        all_files.append(fig5_triple_fracture(L, lang_key))
        all_files.append(fig6_france_brazil_radar(L, lang_key))
    print(f"\n{'='*70}\n Total : {len(all_files)} fichiers dans {OUTPUT_DIR}/\n{'='*70}")
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║  GUIDE D'INSERTION — Chapitre VI bis (Amérique du Sud / Brésil)        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Fig 6bis.1  Déficit invest. IA LATAM       → p. 2  (après §6bis.1.1) ║
║  Fig 6bis.2  Mégaprojets DC Brésil US/CN    → p. 4  (après §6bis.2.2) ║
║  Fig 6bis.3  5 canaux d'impact              → p. 6  (après §6bis.3.2) ║
║  Fig 6bis.4  Scénarios Brésil 2026-2030     → p. 8  (après §6bis.4)   ║
║  Fig 6bis.5  Triple fracture Am. du Sud     → p. 10 (après §6bis.6)   ║
║  Fig 6bis.6  Radar France vs Brésil         → p. 11 (après §6bis.6)   ║
╚══════════════════════════════════════════════════════════════════════════╝
    """)
    return all_files

if __name__ == "__main__":
    main()
