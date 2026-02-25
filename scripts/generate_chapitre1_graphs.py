#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre I : Introduction et Cadrage Théorique
 Générateur de graphiques en 3 langues (FR / EN / PT-BR)
=============================================================================
 Auteur : Script généré pour la note académique
 Usage  : python generate_chapitre1_graphs.py
 Output : PNG files in ./output/figures_ch1/
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
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
DPI = 300
FIGSIZE_WIDE = (12, 6.5)
FIGSIZE_SQUARE = (10, 7)
FIGSIZE_TALL = (11, 8)

# Couleurs palette professionnelle
US_COLOR = "#1B4F72"       # Bleu foncé (US)
EU_COLOR = "#D4AC0D"       # Or/jaune (EU)
FR_COLOR = "#2E86C1"       # Bleu moyen (France)
CN_COLOR = "#C0392B"       # Rouge (Chine)
ACCENT1 = "#148F77"        # Vert teal
ACCENT2 = "#884EA0"        # Violet
ACCENT3 = "#E67E22"        # Orange
BG_COLOR = "#FAFBFC"
GRID_COLOR = "#E0E0E0"

# ─── Traductions ────────────────────────────────────────────────────────────
LANGS = {
    "fr": {
        "suffix": "FR",
        "fig1_title": "Consommation électrique mondiale des data centers\n(Projection IEA 2022-2030)",
        "fig1_ylabel": "TWh / an",
        "fig1_label_total": "Total data centers",
        "fig1_label_ai": "Dont IA (estimation)",
        "fig1_source": "Source : IEA Energy and AI (2025), IEA-4E (2025)",
        "fig1_annot_2024": "415 TWh\n(2024)",
        "fig1_annot_2030": "945 TWh\n(2030, scén. base)",

        "fig2_title": "Marché mondial des semi-conducteurs\n(Projection 2020-2030)",
        "fig2_ylabel": "Milliards USD",
        "fig2_label_total": "Total semi-conducteurs",
        "fig2_label_ai": "Dont puces IA (estimation)",
        "fig2_source": "Sources : SIA/WSTS, McKinsey (2026), Deloitte (2026), AMD",
        "fig2_cagr": "CAGR ~13%",

        "fig3_title": "Compute Gap : capacité de calcul IA par unité de PIB\n(États-Unis vs Union Européenne, 2024)",
        "fig3_ylabel": "Indice relatif (UE = 1)",
        "fig3_labels": ["États-Unis", "Union Européenne"],
        "fig3_source": "Sources : Hawkins et al. (2025), Fed Board (2025), estimations auteur",
        "fig3_annot": "×15",

        "fig4_title": "Taux d'adoption de l'IA par les entreprises\n(États-Unis vs Union Européenne, 2025)",
        "fig4_ylabel": "% d'entreprises utilisant l'IA",
        "fig4_cats": ["Petites entreprises", "Grandes entreprises"],
        "fig4_legend": ["États-Unis", "Union Européenne"],
        "fig4_source": "Sources : Parlement européen (2025), US Chamber of Commerce (2025)",

        "fig5_title": "Domination américaine sur les points d'étranglement\nde la chaîne de valeur IA (2025)",
        "fig5_cats": ["GPU data centers\n(Nvidia)", "Infrastructure\ncloud", "Capital-risque\nIA générative"],
        "fig5_ylabel": "Part de marché contrôlée par des acteurs US (%)",
        "fig5_source": "Sources : OCDE (2025), Fed Board (2025), Bruegel (2024)",
        "fig5_label": "Part US",

        "fig6_title": "Cadre théorique intégré : du protectionnisme technologique\nà la divergence de compétitivité",
        "fig6_boxes": [
            "PROTECTIONNISME\nTECHNOLOGIQUE US\n(Export controls,\ntarifs, quotas)",
            "RESTRICTION\nDU COMPUTE\nEUROPÉEN\n(Compute gap ×15)",
            "DIVERGENCE DE\nPRODUCTIVITÉ\n(J-curve retardée,\ncoûts accrus)",
            "DÉPENDANCE\nSTRATÉGIQUE\n(Vendor lock-in\ngéopolitique)"
        ],
        "fig6_amplifiers": ["Énergie\n(coûts ×2-3 vs US)", "Robotique IA\n(demande ×2 compute)"],
        "fig6_theories": [
            "Weaponized\nInterdependence\n(Farrell & Newman)",
            "GPT & J-Curve\n(Brynjolfsson et al.)",
            "Concentration\n& Rentes\n(Martens, OCDE)",
            "Souveraineté\nnumérique\n(Mügge, Hawkins)"
        ],
        "fig6_source": "Élaboration auteur — Cadre théorique, section 1.3",
        "fig6_amp_label": "AMPLIFICATEURS",
    },
    "en": {
        "suffix": "EN",
        "fig1_title": "Global Data Center Electricity Consumption\n(IEA Projection 2022-2030)",
        "fig1_ylabel": "TWh / year",
        "fig1_label_total": "Total data centers",
        "fig1_label_ai": "Of which AI (estimate)",
        "fig1_source": "Source: IEA Energy and AI (2025), IEA-4E (2025)",
        "fig1_annot_2024": "415 TWh\n(2024)",
        "fig1_annot_2030": "945 TWh\n(2030, base sc.)",

        "fig2_title": "Global Semiconductor Market\n(Projection 2020-2030)",
        "fig2_ylabel": "Billion USD",
        "fig2_label_total": "Total semiconductors",
        "fig2_label_ai": "Of which AI chips (estimate)",
        "fig2_source": "Sources: SIA/WSTS, McKinsey (2026), Deloitte (2026), AMD",
        "fig2_cagr": "CAGR ~13%",

        "fig3_title": "Compute Gap: AI Computing Capacity per GDP Unit\n(United States vs European Union, 2024)",
        "fig3_ylabel": "Relative Index (EU = 1)",
        "fig3_labels": ["United States", "European Union"],
        "fig3_source": "Sources: Hawkins et al. (2025), Fed Board (2025), author estimates",
        "fig3_annot": "×15",

        "fig4_title": "AI Adoption Rate by Enterprises\n(United States vs European Union, 2025)",
        "fig4_ylabel": "% of enterprises using AI",
        "fig4_cats": ["Small enterprises", "Large enterprises"],
        "fig4_legend": ["United States", "European Union"],
        "fig4_source": "Sources: European Parliament (2025), US Chamber of Commerce (2025)",

        "fig5_title": "US Dominance Over AI Value Chain Chokepoints\n(2025)",
        "fig5_cats": ["Data center GPUs\n(Nvidia)", "Cloud\ninfrastructure", "Generative AI\nventure capital"],
        "fig5_ylabel": "Market share controlled by US players (%)",
        "fig5_source": "Sources: OECD (2025), Fed Board (2025), Bruegel (2024)",
        "fig5_label": "US share",

        "fig6_title": "Integrated Theoretical Framework: From Technological Protectionism\nto Competitiveness Divergence",
        "fig6_boxes": [
            "US TECHNOLOGICAL\nPROTECTIONISM\n(Export controls,\ntariffs, quotas)",
            "RESTRICTION OF\nEUROPEAN\nCOMPUTE\n(Compute gap ×15)",
            "PRODUCTIVITY\nDIVERGENCE\n(Delayed J-curve,\nhigher costs)",
            "STRATEGIC\nDEPENDENCE\n(Geopolitical\nvendor lock-in)"
        ],
        "fig6_amplifiers": ["Energy\n(costs ×2-3 vs US)", "AI Robotics\n(×2 compute demand)"],
        "fig6_theories": [
            "Weaponized\nInterdependence\n(Farrell & Newman)",
            "GPT & J-Curve\n(Brynjolfsson et al.)",
            "Concentration\n& Rents\n(Martens, OECD)",
            "Digital\nSovereignty\n(Mügge, Hawkins)"
        ],
        "fig6_source": "Author's elaboration — Theoretical framework, section 1.3",
        "fig6_amp_label": "AMPLIFIERS",
    },
    "pt": {
        "suffix": "PT-BR",
        "fig1_title": "Consumo Global de Eletricidade em Data Centers\n(Projeção IEA 2022-2030)",
        "fig1_ylabel": "TWh / ano",
        "fig1_label_total": "Total data centers",
        "fig1_label_ai": "Dos quais IA (estimativa)",
        "fig1_source": "Fonte: IEA Energy and AI (2025), IEA-4E (2025)",
        "fig1_annot_2024": "415 TWh\n(2024)",
        "fig1_annot_2030": "945 TWh\n(2030, cen. base)",

        "fig2_title": "Mercado Global de Semicondutores\n(Projeção 2020-2030)",
        "fig2_ylabel": "Bilhões USD",
        "fig2_label_total": "Total semicondutores",
        "fig2_label_ai": "Dos quais chips IA (estimativa)",
        "fig2_source": "Fontes: SIA/WSTS, McKinsey (2026), Deloitte (2026), AMD",
        "fig2_cagr": "CAGR ~13%",

        "fig3_title": "Compute Gap: Capacidade de Cálculo IA por Unidade de PIB\n(Estados Unidos vs União Europeia, 2024)",
        "fig3_ylabel": "Índice Relativo (UE = 1)",
        "fig3_labels": ["Estados Unidos", "União Europeia"],
        "fig3_source": "Fontes: Hawkins et al. (2025), Fed Board (2025), estimativas do autor",
        "fig3_annot": "×15",

        "fig4_title": "Taxa de Adoção de IA pelas Empresas\n(Estados Unidos vs União Europeia, 2025)",
        "fig4_ylabel": "% de empresas usando IA",
        "fig4_cats": ["Pequenas empresas", "Grandes empresas"],
        "fig4_legend": ["Estados Unidos", "União Europeia"],
        "fig4_source": "Fontes: Parlamento Europeu (2025), US Chamber of Commerce (2025)",

        "fig5_title": "Dominância Americana nos Pontos de Estrangulamento\nda Cadeia de Valor da IA (2025)",
        "fig5_cats": ["GPUs data center\n(Nvidia)", "Infraestrutura\ncloud", "Capital de risco\nIA generativa"],
        "fig5_ylabel": "Participação de mercado controlada por atores dos EUA (%)",
        "fig5_source": "Fontes: OCDE (2025), Fed Board (2025), Bruegel (2024)",
        "fig5_label": "Participação EUA",

        "fig6_title": "Quadro Teórico Integrado: Do Protecionismo Tecnológico\nà Divergência de Competitividade",
        "fig6_boxes": [
            "PROTECIONISMO\nTECNOLÓGICO EUA\n(Controles exportação,\ntarifas, cotas)",
            "RESTRIÇÃO DO\nCOMPUTE\nEUROPEU\n(Compute gap ×15)",
            "DIVERGÊNCIA DE\nPRODUTIVIDADE\n(J-curve atrasada,\ncustos elevados)",
            "DEPENDÊNCIA\nESTRATÉGICA\n(Vendor lock-in\ngeopolítico)"
        ],
        "fig6_amplifiers": ["Energia\n(custos ×2-3 vs EUA)", "Robótica IA\n(demanda ×2 compute)"],
        "fig6_theories": [
            "Weaponized\nInterdependence\n(Farrell & Newman)",
            "GPT & J-Curve\n(Brynjolfsson et al.)",
            "Concentração\n& Rendas\n(Martens, OCDE)",
            "Soberania\nDigital\n(Mügge, Hawkins)"
        ],
        "fig6_source": "Elaboração do autor — Quadro teórico, seção 1.3",
        "fig6_amp_label": "AMPLIFICADORES",
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
# FIGURE 1.1 — Consommation électrique data centers (IEA)
# Page suggestion : p. 4-5 (après section 1.1, illustration de la problématique)
# ═══════════════════════════════════════════════════════════════════════════
def fig1_energy_datacenter(L, lang_key):
    years = np.array([2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])
    # Total data center consumption (IEA base scenario + interpolation)
    total_twh = np.array([310, 360, 415, 500, 580, 670, 760, 850, 945])
    # AI share estimate (growing from ~15% to ~40%)
    ai_share = np.array([0.10, 0.13, 0.17, 0.22, 0.27, 0.32, 0.36, 0.39, 0.42])
    ai_twh = total_twh * ai_share

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    ax.fill_between(years, total_twh, color=US_COLOR, alpha=0.15, label=L["fig1_label_total"])
    ax.plot(years, total_twh, color=US_COLOR, linewidth=2.5, marker='o', markersize=6)
    ax.fill_between(years, ai_twh, color=CN_COLOR, alpha=0.25, label=L["fig1_label_ai"])
    ax.plot(years, ai_twh, color=CN_COLOR, linewidth=2, marker='s', markersize=5, linestyle='--')

    # Annotations
    ax.annotate(L["fig1_annot_2024"], xy=(2024, 415), xytext=(2023.2, 520),
                fontsize=10, fontweight='bold', color=US_COLOR,
                arrowprops=dict(arrowstyle='->', color=US_COLOR, lw=1.5))
    ax.annotate(L["fig1_annot_2030"], xy=(2030, 945), xytext=(2028.5, 1020),
                fontsize=10, fontweight='bold', color=US_COLOR,
                arrowprops=dict(arrowstyle='->', color=US_COLOR, lw=1.5))

    # Zone projection
    ax.axvspan(2025.5, 2030.5, alpha=0.05, color='gray')
    ax.text(2028, 150, "Projection →", fontsize=9, color='gray', fontstyle='italic', ha='center')

    ax.set_title(L["fig1_title"], fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig1_ylabel"], fontsize=12)
    ax.set_xlim(2021.5, 2030.5)
    ax.set_ylim(0, 1100)
    ax.set_xticks(years)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax.text(0.5, -0.1, L["fig1_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')

    return save_fig(fig, "Fig_1.1_Energy_DataCenters", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 1.2 — Marché des semi-conducteurs 2020-2030
# Page suggestion : p. 6-7 (après Corpus 3 de la revue de littérature)
# ═══════════════════════════════════════════════════════════════════════════
def fig2_semiconductor_market(L, lang_key):
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])
    # Market data (SIA, McKinsey, Deloitte)
    total_mkt = np.array([440, 556, 574, 527, 628, 720, 850, 1000, 1150, 1350, 1600])
    # AI chip share (growing from ~8% to ~45%)
    ai_share = np.array([0.05, 0.06, 0.08, 0.12, 0.18, 0.25, 0.32, 0.36, 0.40, 0.43, 0.45])
    ai_mkt = total_mkt * ai_share

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Barres total
    bars1 = ax.bar(years, total_mkt, width=0.7, color=US_COLOR, alpha=0.3,
                   label=L["fig2_label_total"], edgecolor=US_COLOR, linewidth=0.5)
    # Barres IA
    bars2 = ax.bar(years, ai_mkt, width=0.7, color=ACCENT3, alpha=0.8,
                   label=L["fig2_label_ai"], edgecolor=ACCENT3, linewidth=0.5)

    # Valeurs sur barres total
    for yr, val in zip(years, total_mkt):
        if yr in [2020, 2024, 2030]:
            ax.text(yr, val + 25, f"${val}B", ha='center', fontsize=9, fontweight='bold', color=US_COLOR)

    # CAGR arrow
    ax.annotate(L["fig2_cagr"], xy=(2027, 1050), fontsize=12, fontweight='bold',
                color=ACCENT1, ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=ACCENT1, alpha=0.9))

    # Zone projection
    ax.axvspan(2024.5, 2030.5, alpha=0.05, color='gray')

    ax.set_title(L["fig2_title"], fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig2_ylabel"], fontsize=12)
    ax.set_xlim(2019.2, 2031)
    ax.set_ylim(0, 1800)
    ax.set_xticks(years)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax.text(0.5, -0.1, L["fig2_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')

    return save_fig(fig, "Fig_1.2_Semiconductor_Market", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 1.3 — Compute Gap US vs EU
# Page suggestion : p. 3-4 (illustration directe du concept de compute gap, section 1.2)
# ═══════════════════════════════════════════════════════════════════════════
def fig3_compute_gap(L, lang_key):
    fig, ax = plt.subplots(figsize=(9, 6.5))

    values = [15, 1]
    colors = [US_COLOR, EU_COLOR]
    labels = L["fig3_labels"]

    bars = ax.bar(labels, values, width=0.5, color=colors, edgecolor='white', linewidth=2)

    # Valeurs sur barres
    ax.text(0, 15.5, "15", ha='center', fontsize=28, fontweight='bold', color=US_COLOR)
    ax.text(1, 1.8, "1", ha='center', fontsize=28, fontweight='bold', color=EU_COLOR)

    # Flèche compute gap
    ax.annotate('', xy=(0, 14), xytext=(1, 2),
                arrowprops=dict(arrowstyle='<->', color=CN_COLOR, lw=3))
    ax.text(0.5, 8.5, L["fig3_annot"], ha='center', fontsize=32, fontweight='bold',
            color=CN_COLOR,
            path_effects=[pe.withStroke(linewidth=4, foreground='white')])

    ax.set_title(L["fig3_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig3_ylabel"], fontsize=12)
    ax.set_ylim(0, 19)
    ax.set_yticks(range(0, 20, 3))

    ax.text(0.5, -0.12, L["fig3_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')

    return save_fig(fig, "Fig_1.3_Compute_Gap", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 1.4 — Adoption de l'IA : US vs EU
# Page suggestion : p. 7-8 (après Corpus 4 de la revue de littérature)
# ═══════════════════════════════════════════════════════════════════════════
def fig4_ai_adoption(L, lang_key):
    fig, ax = plt.subplots(figsize=(10, 6.5))

    cats = L["fig4_cats"]
    us_vals = [58, 72]   # US: 58% small (Chamber), ~72% large (estimate)
    eu_vals = [11, 41]   # EU: 11% small, 41% large (EP 2025)

    x = np.arange(len(cats))
    width = 0.32

    bars_us = ax.bar(x - width/2, us_vals, width, color=US_COLOR, label=L["fig4_legend"][0],
                     edgecolor='white', linewidth=1.5)
    bars_eu = ax.bar(x + width/2, eu_vals, width, color=EU_COLOR, label=L["fig4_legend"][1],
                     edgecolor='white', linewidth=1.5)

    # Valeurs
    for bar, val in zip(bars_us, us_vals):
        ax.text(bar.get_x() + bar.get_width()/2, val + 1.5, f"{val}%",
                ha='center', fontsize=14, fontweight='bold', color=US_COLOR)
    for bar, val in zip(bars_eu, eu_vals):
        ax.text(bar.get_x() + bar.get_width()/2, val + 1.5, f"{val}%",
                ha='center', fontsize=14, fontweight='bold', color=EU_COLOR)

    # Gap annotations
    for i, (us, eu) in enumerate(zip(us_vals, eu_vals)):
        gap = us - eu
        mid = (us + eu) / 2
        ax.annotate(f"Gap: {gap}pp", xy=(i + 0.42, mid), fontsize=10,
                    color=CN_COLOR, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF3E0', edgecolor=CN_COLOR, alpha=0.8))

    ax.set_title(L["fig4_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["fig4_ylabel"], fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=12)
    ax.set_ylim(0, 90)
    ax.legend(fontsize=11, framealpha=0.9)
    ax.text(0.5, -0.1, L["fig4_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')

    return save_fig(fig, "Fig_1.4_AI_Adoption_Gap", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 1.5 — Points d'étranglement US
# Page suggestion : p. 5-6 (section 1.3.2 Weaponized Interdependence)
# ═══════════════════════════════════════════════════════════════════════════
def fig5_chokepoints(L, lang_key):
    fig, ax = plt.subplots(figsize=(10, 6.5))

    cats = L["fig5_cats"]
    vals = [80, 70, 75]  # Nvidia GPU 80%, Cloud 70%, VC 75%
    colors_grad = [US_COLOR, "#2471A3", "#2E86C1"]

    bars = ax.barh(cats, vals, height=0.55, color=colors_grad, edgecolor='white', linewidth=2)

    for bar, val in zip(bars, vals):
        ax.text(val + 1.5, bar.get_y() + bar.get_height()/2, f"{val}%",
                va='center', fontsize=16, fontweight='bold', color=US_COLOR)

    # Ligne seuil 50%
    ax.axvline(x=50, color=CN_COLOR, linewidth=1.5, linestyle='--', alpha=0.6)
    ax.text(51, 2.7, "50%", fontsize=9, color=CN_COLOR, fontstyle='italic')

    ax.set_title(L["fig5_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel(L["fig5_ylabel"], fontsize=11)
    ax.set_xlim(0, 100)
    ax.invert_yaxis()
    ax.text(0.5, -0.1, L["fig5_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')

    return save_fig(fig, "Fig_1.5_US_Chokepoints", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 1.6 — Cadre théorique intégré (schéma conceptuel)
# Page suggestion : p. 8-9 (fin section 1.4, synthèse avant section 1.5)
# ═══════════════════════════════════════════════════════════════════════════
def fig6_theoretical_framework(L, lang_key):
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Titre
    ax.text(7, 8.6, L["fig6_title"], ha='center', fontsize=14, fontweight='bold')

    # ── Boîtes principales (chaîne causale) ──
    box_positions = [(1.2, 5.5), (4.4, 5.5), (7.6, 5.5), (10.8, 5.5)]
    box_colors = [CN_COLOR, ACCENT3, ACCENT2, US_COLOR]
    box_w, box_h = 2.6, 2.2

    for i, (x, y) in enumerate(box_positions):
        rect = mpatches.FancyBboxPatch((x, y), box_w, box_h,
                                        boxstyle="round,pad=0.15",
                                        facecolor=box_colors[i], alpha=0.12,
                                        edgecolor=box_colors[i], linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + box_w/2, y + box_h/2, L["fig6_boxes"][i],
                ha='center', va='center', fontsize=8.5, fontweight='bold',
                color=box_colors[i])

    # Flèches entre boîtes
    arrow_style = dict(arrowstyle='->', color='#555', lw=2.5, connectionstyle='arc3,rad=0')
    for i in range(3):
        x_start = box_positions[i][0] + box_w
        x_end = box_positions[i+1][0]
        y_mid = 6.6
        ax.annotate('', xy=(x_end, y_mid), xytext=(x_start, y_mid),
                    arrowprops=arrow_style)

    # ── Amplificateurs (en bas) ──
    amp_y = 2.8
    amp_positions = [(3.5, amp_y), (8.0, amp_y)]
    for i, (x, y) in enumerate(amp_positions):
        rect = mpatches.FancyBboxPatch((x, y), 2.8, 1.4,
                                        boxstyle="round,pad=0.12",
                                        facecolor=ACCENT1, alpha=0.12,
                                        edgecolor=ACCENT1, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + 1.4, y + 0.7, L["fig6_amplifiers"][i],
                ha='center', va='center', fontsize=8.5, fontweight='bold', color=ACCENT1)

    # Label amplificateurs
    ax.text(7, 4.5, L["fig6_amp_label"], ha='center', fontsize=10,
            fontweight='bold', color=ACCENT1,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=ACCENT1))

    # Flèches amplificateurs vers chaîne
    for x_amp in [4.9, 9.4]:
        ax.annotate('', xy=(x_amp, 5.5), xytext=(x_amp, 4.2),
                    arrowprops=dict(arrowstyle='->', color=ACCENT1, lw=1.8, linestyle='--'))

    # ── Théories (en haut, petites boîtes) ──
    theory_y = 0.8
    theory_positions = [(0.5, theory_y), (3.7, theory_y), (6.9, theory_y), (10.1, theory_y)]
    for i, (x, y) in enumerate(theory_positions):
        rect = mpatches.FancyBboxPatch((x, y), 2.8, 1.4,
                                        boxstyle="round,pad=0.1",
                                        facecolor='#F5F5F5',
                                        edgecolor='#999', linewidth=1, linestyle='--')
        ax.add_patch(rect)
        ax.text(x + 1.4, y + 0.7, L["fig6_theories"][i],
                ha='center', va='center', fontsize=7.5, color='#555', fontstyle='italic')

    # Source
    ax.text(7, 0.15, L["fig6_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')

    return save_fig(fig, "Fig_1.6_Theoretical_Framework", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# MAIN — Génération pour les 3 langues
# ═══════════════════════════════════════════════════════════════════════════
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()

    print("=" * 70)
    print(" CHAPITRE I — Génération des graphiques en 3 langues")
    print("=" * 70)

    all_files = []

    for lang_key, L in LANGS.items():
        print(f"\n{'─'*50}")
        print(f" Langue : {L['suffix']}")
        print(f"{'─'*50}")

        all_files.append(fig1_energy_datacenter(L, lang_key))
        all_files.append(fig2_semiconductor_market(L, lang_key))
        all_files.append(fig3_compute_gap(L, lang_key))
        all_files.append(fig4_ai_adoption(L, lang_key))
        all_files.append(fig5_chokepoints(L, lang_key))
        all_files.append(fig6_theoretical_framework(L, lang_key))

    print(f"\n{'='*70}")
    print(f" Total : {len(all_files)} fichiers générés dans {OUTPUT_DIR}/")
    print(f"{'='*70}")

    # Résumé des insertions
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║  GUIDE D'INSERTION — Chapitre I                                    ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Fig 1.1  Énergie data centers    → p.4-5  (après §1.1)           ║
║           Illustre la problématique énergétique globale            ║
║                                                                    ║
║  Fig 1.2  Marché semi-conducteurs → p.6-7  (Corpus 3, §1.4)      ║
║           Croissance explosive du marché puces IA                  ║
║                                                                    ║
║  Fig 1.3  Compute Gap US vs EU    → p.3-4  (définition §1.2)     ║
║           Visualisation du ratio ×15                               ║
║                                                                    ║
║  Fig 1.4  Adoption IA US vs EU    → p.7-8  (Corpus 4, §1.4)     ║
║           Écart d'adoption petites/grandes entreprises             ║
║                                                                    ║
║  Fig 1.5  Chokepoints US          → p.5-6  (§1.3.2 Weaponized)   ║
║           Domination sur GPU, Cloud, VC                            ║
║                                                                    ║
║  Fig 1.6  Cadre théorique         → p.8-9  (fin §1.4 / avant 1.5)║
║           Schéma intégré de la trajectoire causale                 ║
║                                                                    ║
╚══════════════════════════════════════════════════════════════════════╝
    """)

    return all_files


if __name__ == "__main__":
    main()
