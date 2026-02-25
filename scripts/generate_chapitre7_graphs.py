#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre VII : Recommandations stratégiques
 Générateur de graphiques en 3 langues (FR / EN / PT-BR)
=============================================================================
 Usage  : python generate_chapitre7_graphs.py
 Output : PNG files in ./output/figures_ch7/

 GUIDE D'INSERTION (pages du chapitre VII) :
 ──────────────────────────────────────────────────────────────────
 Fig 7.1  Écart de capex US vs EU                  → p. 2  (après §7.1.1)
 Fig 7.2  Atout nucléaire français (énergie IA)    → p. 4  (après §7.2.1)
 Fig 7.3  Chaîne alliances technologiques EU       → p. 6  (après §7.3.1)
 Fig 7.4  Matrice temporelle des recommandations   → p. 9  (après §7.6)
 Fig 7.5  Conditions de succès et fenêtre d'action → p. 10 (après §7.7)
 Fig 7.6  Positionnement comparatif mondial        → p. 11 (après §7.8)
 ──────────────────────────────────────────────────────────────────
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

US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
FR_COLOR = "#2E86C1"
CN_COLOR = "#C0392B"
JP_COLOR = "#E74C3C"
IN_COLOR = "#F39C12"
BR_COLOR = "#27AE60"
ACCENT1 = "#148F77"
ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"
NUC_COLOR = "#F1C40F"  # Nuclear yellow
BG_COLOR = "#FAFBFC"
GRID_COLOR = "#E0E0E0"

LANGS = {
    "fr": {
        "suffix": "FR",
        "fig1_title": "Écart de capex IA : hyperscalers US vs Europe\n(2026, milliards USD/EUR)",
        "fig1_ylabel": "Milliards (USD pour US, EUR pour EU)",
        "fig1_cats": ["Amazon", "Alphabet", "Microsoft", "Meta", "Oracle", "Total US\n(5 hypers.)", "InvestAI EU\n(sur 5 ans)"],
        "fig1_source": "Sources : Euronews (2026), Commission européenne (2025)",
        "fig1_annot": "×3,3 sur\nune seule\nannée",

        "fig2_title": "L'avantage nucléaire français pour l'IA :\ninfrastructure énergétique dédiée",
        "fig2_ylabel": "Capacité (GW / MW)",
        "fig2_cats": ["Parc nucléaire\nactuel (56 réact.)", "Sites EDF\ndata centers", "Campus MGX-\nMistral-Nvidia", "Fluidstack\n(nuc. IA)", "EPR 2\n(6 réacteurs)", "SMR\n(horizon 2033)"],
        "fig2_source": "Sources : EDF, World Nuclear News, Global DC Hub (2025)",
        "fig2_legend": ["Opérationnel / en cours", "Planifié 2027-2032"],
        "fig2_fr_advantage": "France : seul pays EU avec\ntriptyque nucléaire + baseload + compétitivité",

        "fig3_title": "Alliances technologiques stratégiques\npour réduire la dépendance",
        "fig3_source": "Source : élaboration auteur, §7.3",

        "fig4_title": "Matrice temporelle des recommandations\nstratégiques (2026-2032)",
        "fig4_horizons": ["Court terme\n2026-2027", "Moyen terme\n2027-2029", "Long terme\n2029-2032"],
        "fig4_axes": ["Compute", "Énergie", "Alliances", "Régulation", "Talent"],
        "fig4_source": "Source : Tableau 17 du chapitre",

        "fig5_title": "Fenêtre d'action stratégique 2026-2028 :\nconditions de succès",
        "fig5_conditions": ["Compétitivité\nMistral", "Exécution\nindustrielle", "Cohérence\neuropéenne", "Facteur\ntemps"],
        "fig5_source": "Source : §7.7, élaboration auteur",
        "fig5_window": "FENÊTRE DÉCISIVE : 2026-2028",

        "fig6_title": "Positionnement comparatif mondial :\nstratégies face au protectionnisme IA US",
        "fig6_countries": ["Japon", "France/UE", "Inde", "Brésil", "Chine"],
        "fig6_source": "Source : synthèse auteur, §7.8",
        "fig6_strategies": ["Co-financement\nUS ($550B)", "Autonomie\nénergétique\n+ Mistral", "Compute\nas export\n+ Tier 2", "Hub neutre\ndual\nUS-Chine", "Écosystème\nparallèle\nautonomisé"],
    },
    "en": {
        "suffix": "EN",
        "fig1_title": "AI Capex Gap: US Hyperscalers vs Europe\n(2026, billion USD/EUR)",
        "fig1_ylabel": "Billions (USD for US, EUR for EU)",
        "fig1_cats": ["Amazon", "Alphabet", "Microsoft", "Meta", "Oracle", "Total US\n(5 hypers.)", "InvestAI EU\n(over 5 yrs)"],
        "fig1_source": "Sources: Euronews (2026), European Commission (2025)",
        "fig1_annot": "×3.3 in a\nsingle\nyear",

        "fig2_title": "France's Nuclear Advantage for AI:\nDedicated Energy Infrastructure",
        "fig2_ylabel": "Capacity (GW / MW)",
        "fig2_cats": ["Current nuclear\nfleet (56 react.)", "EDF DC\nsites", "MGX-Mistral-\nNvidia campus", "Fluidstack\n(nuclear AI)", "EPR 2\n(6 reactors)", "SMR\n(horizon 2033)"],
        "fig2_source": "Sources: EDF, World Nuclear News, Global DC Hub (2025)",
        "fig2_legend": ["Operational / underway", "Planned 2027-2032"],
        "fig2_fr_advantage": "France: only EU country with\nnuclear + baseload + cost competitiveness",

        "fig3_title": "Strategic Technological Alliances\nto Reduce Dependency",
        "fig3_source": "Source: author's elaboration, §7.3",

        "fig4_title": "Strategic Recommendations\nTime Matrix (2026-2032)",
        "fig4_horizons": ["Short term\n2026-2027", "Medium term\n2027-2029", "Long term\n2029-2032"],
        "fig4_axes": ["Compute", "Energy", "Alliances", "Regulation", "Talent"],
        "fig4_source": "Source: Table 17 of the chapter",

        "fig5_title": "Strategic Action Window 2026-2028:\nConditions for Success",
        "fig5_conditions": ["Mistral\ncompetitiveness", "Industrial\nexecution", "European\ncoherence", "Time\nfactor"],
        "fig5_source": "Source: §7.7, author's elaboration",
        "fig5_window": "DECISIVE WINDOW: 2026-2028",

        "fig6_title": "Comparative Global Positioning:\nStrategies Facing US AI Protectionism",
        "fig6_countries": ["Japan", "France/EU", "India", "Brazil", "China"],
        "fig6_source": "Source: author's synthesis, §7.8",
        "fig6_strategies": ["US co-financing\n($550B)", "Energy\nautonomy\n+ Mistral", "Compute\nas export\n+ Tier 2", "Neutral dual\nhub\nUS-China", "Parallel\nautonomized\necosystem"],
    },
    "pt": {
        "suffix": "PT-BR",
        "fig1_title": "Gap de Capex em IA: Hyperscalers EUA vs Europa\n(2026, bilhões USD/EUR)",
        "fig1_ylabel": "Bilhões (USD para EUA, EUR para UE)",
        "fig1_cats": ["Amazon", "Alphabet", "Microsoft", "Meta", "Oracle", "Total EUA\n(5 hypers.)", "InvestAI UE\n(em 5 anos)"],
        "fig1_source": "Fontes: Euronews (2026), Comissão Europeia (2025)",
        "fig1_annot": "×3,3 em\num único\nano",

        "fig2_title": "Vantagem Nuclear Francesa para a IA:\nInfraestrutura Energética Dedicada",
        "fig2_ylabel": "Capacidade (GW / MW)",
        "fig2_cats": ["Parque nuclear\natual (56 reat.)", "Sites EDF\ndata centers", "Campus MGX-\nMistral-Nvidia", "Fluidstack\n(nuclear IA)", "EPR 2\n(6 reatores)", "SMR\n(horizonte 2033)"],
        "fig2_source": "Fontes: EDF, World Nuclear News, Global DC Hub (2025)",
        "fig2_legend": ["Operacional / em andamento", "Planejado 2027-2032"],
        "fig2_fr_advantage": "França: único país UE com\nnuclear + base + competitividade de custo",

        "fig3_title": "Alianças Tecnológicas Estratégicas\npara Reduzir a Dependência",
        "fig3_source": "Fonte: elaboração do autor, §7.3",

        "fig4_title": "Matriz Temporal das Recomendações\nEstratégicas (2026-2032)",
        "fig4_horizons": ["Curto prazo\n2026-2027", "Médio prazo\n2027-2029", "Longo prazo\n2029-2032"],
        "fig4_axes": ["Compute", "Energia", "Alianças", "Regulação", "Talento"],
        "fig4_source": "Fonte: Tabela 17 do capítulo",

        "fig5_title": "Janela de Ação Estratégica 2026-2028:\nCondições de Sucesso",
        "fig5_conditions": ["Competitividade\nMistral", "Execução\nindustrial", "Coerência\neuropeia", "Fator\ntempo"],
        "fig5_source": "Fonte: §7.7, elaboração do autor",
        "fig5_window": "JANELA DECISIVA: 2026-2028",

        "fig6_title": "Posicionamento Comparativo Mundial:\nEstratégias Face ao Protecionismo de IA dos EUA",
        "fig6_countries": ["Japão", "França/UE", "Índia", "Brasil", "China"],
        "fig6_source": "Fonte: síntese do autor, §7.8",
        "fig6_strategies": ["Co-financiamento\nEUA (US$ 550 bi)", "Autonomia\nenergética\n+ Mistral", "Compute\ncomo export\n+ Tier 2", "Hub neutro\ndual\nEUA-China", "Ecossistema\nparalelo\nautonomizado"],
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
# FIG 7.1 — Écart de capex US hyperscalers vs InvestAI EU
# Page : p. 2 (après §7.1.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig1_capex_gap(L, lang_key):
    fig, ax = plt.subplots(figsize=(13, 7))
    cats = L["fig1_cats"]
    # 2026 capex: Amazon 200, Alphabet 185, MS 145, Meta 135, Oracle 50 = 660-690
    # InvestAI: 200 Md€ over 5 years = 40/yr equivalent
    values = [200, 185, 145, 135, 50, 675, 200]
    colors = [US_COLOR]*5 + ["#154360", EU_COLOR]
    alphas = [0.75]*5 + [1.0, 0.85]

    bars = ax.bar(cats, values, width=0.6, color=colors, edgecolor='white',
                  linewidth=2)
    for bar, alpha in zip(bars, alphas):
        bar.set_alpha(alpha)

    for bar, val in zip(bars, values):
        suffix = "B$" if bar != bars[-1] else "B€"
        ax.text(bar.get_x() + bar.get_width()/2, val + 8,
                f"${val}B" if suffix == "B$" else f"€{val}B",
                ha='center', fontsize=11, fontweight='bold',
                color=US_COLOR if suffix == "B$" else EU_COLOR)

    # Divider line
    ax.axvline(x=4.5, color='gray', linewidth=1, linestyle=':', alpha=0.5)
    ax.text(4.5, 710, "─── vs ───", ha='center', fontsize=9, color='gray')

    # Annotation ×3.3
    ax.annotate(L["fig1_annot"], xy=(5.5, 675), xytext=(6.2, 500),
                fontsize=14, fontweight='bold', color=CN_COLOR,
                ha='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFEBEE',
                          edgecolor=CN_COLOR, alpha=0.9),
                arrowprops=dict(arrowstyle='->', color=CN_COLOR, lw=2))

    # Labels
    ax.text(2, 730, "2026 (1 an)", ha='center', fontsize=11,
            fontweight='bold', color=US_COLOR,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF5FB', edgecolor=US_COLOR))
    ax.text(6, 730, "5 ans", ha='center', fontsize=11,
            fontweight='bold', color=EU_COLOR,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF9E7', edgecolor=EU_COLOR))

    ax.set_title(L["fig1_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig1_ylabel"], fontsize=11)
    ax.set_ylim(0, 780)
    ax.text(0.5, -0.12, L["fig1_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_7.1_Capex_Gap", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 7.2 — Avantage nucléaire français
# Page : p. 4 (après §7.2.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig2_nuclear_advantage(L, lang_key):
    fig, ax = plt.subplots(figsize=(13, 7.5))
    cats = L["fig2_cats"]
    # Values in GW: nuclear fleet 61.4, EDF sites 2, MGX campus 1.4, Fluidstack 1, EPR2 9.9, SMR 0.34
    vals_operational = [61.4, 2.0, 1.4, 1.0, 0, 0]
    vals_planned = [0, 0, 0, 0, 9.9, 0.34]

    x = np.arange(len(cats))
    w = 0.35
    bars1 = ax.bar(x - w/2, vals_operational, w, color=FR_COLOR,
                   label=L["fig2_legend"][0], edgecolor='white', linewidth=1.5)
    bars2 = ax.bar(x + w/2, vals_planned, w, color=NUC_COLOR,
                   label=L["fig2_legend"][1], edgecolor='white', linewidth=1.5, alpha=0.8)

    for bar, val in zip(bars1, vals_operational):
        if val > 0:
            ax.text(bar.get_x() + bar.get_width()/2, val + 1.2,
                    f"{val} GW", ha='center', fontsize=10, fontweight='bold', color=FR_COLOR)
    for bar, val in zip(bars2, vals_planned):
        if val > 0:
            ax.text(bar.get_x() + bar.get_width()/2, val + 1.2,
                    f"{val} GW", ha='center', fontsize=10, fontweight='bold', color='#B7950B')

    # France advantage box
    ax.text(0.98, 0.95, L["fig2_fr_advantage"], transform=ax.transAxes,
            fontsize=10, color=FR_COLOR, ha='right', va='top', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#EBF5FB',
                      edgecolor=FR_COLOR, linewidth=2))

    # 70% nuclear annotation
    ax.text(0, 55, "70%\nnucléaire", ha='center', fontsize=9, color='white',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=FR_COLOR, alpha=0.8))

    ax.set_title(L["fig2_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig2_ylabel"], fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=9)
    ax.set_ylim(0, 75)
    ax.legend(fontsize=10, framealpha=0.9, loc='upper right')
    ax.text(0.5, -0.12, L["fig2_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_7.2_Nuclear_Advantage", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 7.3 — Alliances technologiques (schéma conceptuel)
# Page : p. 6 (après §7.3.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig3_alliances(L, lang_key):
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    ax.text(7, 8.6, L["fig3_title"], ha='center', fontsize=14, fontweight='bold')

    # Central: France/EU
    rect = mpatches.FancyBboxPatch((5.2, 3.8), 3.6, 2.0,
                                    boxstyle="round,pad=0.2",
                                    facecolor=FR_COLOR, alpha=0.15,
                                    edgecolor=FR_COLOR, linewidth=3)
    ax.add_patch(rect)
    ax.text(7, 4.8, "FRANCE / UE\nMistral + ASML\nSecNumCloud\nAI Factories", ha='center',
            fontsize=10, fontweight='bold', color=FR_COLOR, linespacing=1.3)

    # Alliances around
    alliances = [
        (0.5, 6.0, 3.0, 1.8, "ASML → Mistral\n1,3 Md€ (11%)\nLithographie EU", ACCENT1),
        (10.5, 6.0, 3.0, 1.8, "TSMC Dresde\n10 Md€\n28/16/12nm → 7/5nm?", "#E74C3C"),
        (0.5, 1.5, 3.0, 1.8, "Japon-UE\nTokyo Electron\nShin-Etsu\nMatériaux", JP_COLOR),
        (10.5, 1.5, 3.0, 1.8, "Corée-UE\nSK hynix HBM\nSamsung\nMémoire IA", "#3498DB"),
        (5.2, 0.3, 3.6, 1.5, "Diversification GPU\nAMD MI350X | Intel Gaudi 3\nSiPearl (EU)", ACCENT2),
        (5.2, 6.5, 3.6, 1.5, "Cloud souverain\nS3NS | Bleu | OVH\nSecNumCloud 3.2", EU_COLOR),
    ]

    for x, y, w, h, text, color in alliances:
        rect = mpatches.FancyBboxPatch((x, y), w, h,
                                        boxstyle="round,pad=0.12",
                                        facecolor=color, alpha=0.1,
                                        edgecolor=color, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=8, fontweight='bold', color=color, linespacing=1.2)

    # Arrows from center to alliances
    arrow_targets = [(2.0, 6.9, 5.2, 5.5), (12.0, 6.9, 8.8, 5.5),
                     (2.0, 2.4, 5.2, 4.0), (12.0, 2.4, 8.8, 4.0),
                     (7.0, 1.8, 7.0, 3.8), (7.0, 6.5, 7.0, 5.8)]
    for x1, y1, x2, y2 in arrow_targets:
        ax.annotate('', xy=(x1, y1), xytext=(x2, y2),
                    arrowprops=dict(arrowstyle='->', color='#888', lw=1.8, linestyle='--'))

    ax.text(7, -0.15, L["fig3_source"], ha='center', fontsize=8,
            color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_7.3_Alliances", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 7.4 — Matrice temporelle des recommandations
# Page : p. 9 (après §7.6)
# ═══════════════════════════════════════════════════════════════════════════
def fig4_timeline_matrix(L, lang_key):
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    ax.text(7, 8.6, L["fig4_title"], ha='center', fontsize=14, fontweight='bold')

    horizons = L["fig4_horizons"]
    axes_labels = L["fig4_axes"]
    h_colors = ["#2ECC71", ACCENT3, CN_COLOR]

    # Horizon columns headers
    for i, (h, col) in enumerate(zip(horizons, h_colors)):
        x = 3.5 + i * 3.5
        ax.text(x, 7.8, h, ha='center', fontsize=11, fontweight='bold', color=col,
                bbox=dict(boxstyle='round,pad=0.3', facecolor=col, alpha=0.1, edgecolor=col))

    # Axe row labels
    axe_colors = [FR_COLOR, NUC_COLOR, ACCENT1, ACCENT2, "#5D6D7E"]
    for j, (axe, acol) in enumerate(zip(axes_labels, axe_colors)):
        y = 6.5 - j * 1.3
        ax.text(1.2, y, axe, ha='center', va='center', fontsize=10,
                fontweight='bold', color=acol,
                bbox=dict(boxstyle='round,pad=0.2', facecolor=acol, alpha=0.1, edgecolor=acol))

    # Content cells (simplified key actions)
    content = [
        # Compute
        ["13 AI Factories\nSpecial Compute\nZones FR", "5 AI Gigafact.\n20 Md€\nCampus MGX 1.4GW", "40% compute\nlocal\nSiPearl EU"],
        # Energy
        ["250 MW nuc-IA\n6 sites EDF\nFluidstack 1 GW", "6 EPR 2 lancés\nIntégration réseau\n8 EPR optionnels", "Premier SMR DC\n+20 GW nuc. 2035\nMix IA intégré"],
        # Alliances
        ["Accord UE-Nvidia\nRéserves GPU\nVisas talents", "TSMC EU 7/5nm\nUE-Japon/Corée\nCLOUD Act Shield", "Multi-fournis.\nGPU qualifié\nNormes export"],
        # Regulation
        ["AI Act\napplication\nApply AI Strat.", "SecNumCloud\n30-40% souverain\nEffet Bruxelles", "Compute bien\nstratégique\n1% PIB infra"],
        # Talent
        ["Bourses IA EU\nVisas talents\nMistral compute", "500K GPU accès\nchercheurs\nÉquivalence US", "Zéro départ\ncompute\nd'ici 2028"],
    ]

    for j, row in enumerate(content):
        for i, cell in enumerate(row):
            x = 2.8 + i * 3.5
            y = 6.0 - j * 1.3
            rect = mpatches.FancyBboxPatch((x, y), 2.6, 1.1,
                                            boxstyle="round,pad=0.08",
                                            facecolor=h_colors[i], alpha=0.06,
                                            edgecolor=h_colors[i], linewidth=1)
            ax.add_patch(rect)
            ax.text(x + 1.3, y + 0.55, cell, ha='center', va='center',
                    fontsize=7, color='#333', linespacing=1.2)

    ax.text(7, -0.1, L["fig4_source"], ha='center', fontsize=8,
            color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_7.4_Timeline_Matrix", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 7.5 — Conditions de succès et fenêtre d'action
# Page : p. 10 (après §7.7)
# ═══════════════════════════════════════════════════════════════════════════
def fig5_conditions_success(L, lang_key):
    fig, ax = plt.subplots(figsize=(12, 7))

    conditions = L["fig5_conditions"]
    # Criticality score /10
    scores = [8, 9, 7, 10]
    colors = [ACCENT2, FR_COLOR, EU_COLOR, CN_COLOR]

    bars = ax.barh(conditions, scores, height=0.5, color=colors,
                   edgecolor='white', linewidth=2, alpha=0.8)

    for i, (bar, val) in enumerate(zip(bars, scores)):
        ax.text(val + 0.2, bar.get_y() + bar.get_height()/2,
                f"{val}/10", va='center', fontsize=14, fontweight='bold',
                color=colors[i])

    # Window annotation
    ax.text(0.5, 0.95, L["fig5_window"], transform=ax.transAxes,
            fontsize=14, fontweight='bold', color=CN_COLOR, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFEBEE',
                      edgecolor=CN_COLOR, linewidth=2.5))

    # Timeline bar at bottom
    ax.axhline(y=-0.8, color='gray', linewidth=0.5)
    years = [2026, 2027, 2028, 2029, 2030]
    for yr in years:
        xpos = (yr - 2026) / 4 * 10
        ax.plot(xpos, -0.6, 'v', color='gray', markersize=8)
        ax.text(xpos, -1.0, str(yr), ha='center', fontsize=9, color='gray')

    # Critical window highlight
    ax.axhspan(-1.2, -0.4, xmin=0, xmax=0.5, alpha=0.1, color=CN_COLOR)
    ax.text(2.5, -0.8, "← ZONE CRITIQUE →", ha='center', fontsize=9,
            fontweight='bold', color=CN_COLOR)

    ax.set_title(L["fig5_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_xlim(0, 11)
    ax.set_ylim(-1.3, len(conditions) - 0.3)
    ax.invert_yaxis()
    ax.set_xlabel("", fontsize=1)
    ax.text(0.5, -0.15, L["fig5_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_7.5_Conditions_Success", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIG 7.6 — Positionnement comparatif mondial (synthèse)
# Page : p. 11 (après §7.8)
# ═══════════════════════════════════════════════════════════════════════════
def fig6_global_positioning(L, lang_key):
    fig, ax = plt.subplots(figsize=(14, 8.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.5)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    ax.text(7, 8.1, L["fig6_title"], ha='center', fontsize=14, fontweight='bold')

    countries = L["fig6_countries"]
    strategies = L["fig6_strategies"]
    colors = [JP_COLOR, FR_COLOR, IN_COLOR, BR_COLOR, CN_COLOR]

    # Spectrum: alignment US (left) → confrontation (right)
    ax.annotate('', xy=(1, 1.0), xytext=(13, 1.0),
                arrowprops=dict(arrowstyle='<->', color='#888', lw=2))
    ax.text(1, 0.5, "Alignement US", fontsize=10, color=US_COLOR, fontweight='bold')
    ax.text(13, 0.5, "Confrontation", fontsize=10, color=CN_COLOR,
            fontweight='bold', ha='right')
    ax.text(7, 0.5, "Autonomie", fontsize=10, color=ACCENT1,
            fontweight='bold', ha='center')

    # Country cards positioned on spectrum
    x_positions = [1.5, 4.5, 7.0, 9.5, 12.0]  # Japan most aligned, China least
    for i, (x, country, strategy, col) in enumerate(zip(x_positions, countries, strategies, colors)):
        rect = mpatches.FancyBboxPatch((x, 2.0), 2.2, 4.5,
                                        boxstyle="round,pad=0.15",
                                        facecolor=col, alpha=0.1,
                                        edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + 1.1, 6.0, country, ha='center', fontsize=12,
                fontweight='bold', color=col)
        ax.text(x + 1.1, 4.0, strategy, ha='center', fontsize=8.5,
                color='#333', linespacing=1.3)

        # Vertical line to spectrum
        ax.plot([x + 1.1, x + 1.1], [1.0, 2.0], color=col, linewidth=2,
                linestyle=':', alpha=0.5)
        ax.plot(x + 1.1, 1.0, 'o', color=col, markersize=10)

    # Highlight France
    highlight = mpatches.FancyBboxPatch((4.3, 1.85), 2.6, 4.85,
                                         boxstyle="round,pad=0.1",
                                         facecolor='none',
                                         edgecolor=FR_COLOR, linewidth=3,
                                         linestyle='--')
    ax.add_patch(highlight)
    ax.text(5.6, 7.0, "★", ha='center', fontsize=16, color=FR_COLOR)

    ax.text(7, -0.1, L["fig6_source"], ha='center', fontsize=8,
            color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_7.6_Global_Positioning", L["suffix"])


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()
    print("=" * 70)
    print(" CHAPITRE VII — Génération des graphiques en 3 langues")
    print("=" * 70)
    all_files = []
    for lang_key, L in LANGS.items():
        print(f"\n{'─'*50}\n Langue : {L['suffix']}\n{'─'*50}")
        all_files.append(fig1_capex_gap(L, lang_key))
        all_files.append(fig2_nuclear_advantage(L, lang_key))
        all_files.append(fig3_alliances(L, lang_key))
        all_files.append(fig4_timeline_matrix(L, lang_key))
        all_files.append(fig5_conditions_success(L, lang_key))
        all_files.append(fig6_global_positioning(L, lang_key))
    print(f"\n{'='*70}\n Total : {len(all_files)} fichiers dans {OUTPUT_DIR}/\n{'='*70}")
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║  GUIDE D'INSERTION — Chapitre VII (Recommandations stratégiques)       ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Fig 7.1  Écart capex US vs EU              → p. 2  (après §7.1.1)    ║
║  Fig 7.2  Avantage nucléaire français       → p. 4  (après §7.2.1)    ║
║  Fig 7.3  Alliances technologiques EU       → p. 6  (après §7.3.1)    ║
║  Fig 7.4  Matrice temporelle recommandations→ p. 9  (après §7.6)      ║
║  Fig 7.5  Conditions de succès              → p. 10 (après §7.7)      ║
║  Fig 7.6  Positionnement comparatif mondial → p. 11 (après §7.8)      ║
╚══════════════════════════════════════════════════════════════════════════╝
    """)
    return all_files

if __name__ == "__main__":
    main()
