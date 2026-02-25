#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre II : Méthodologie
 Générateur de graphiques en 3 langues (FR / EN / PT-BR)
=============================================================================
 Usage  : python generate_chapitre2_graphs.py
 Output : PNG files in ./output/figures_ch2/
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
FIGSIZE_WIDE = (13, 7)
FIGSIZE_SQUARE = (10, 7)

# Couleurs
US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
FR_COLOR = "#2E86C1"
CN_COLOR = "#C0392B"
ACCENT1 = "#148F77"
ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"
ACCENT4 = "#2C3E50"
BG_COLOR = "#FAFBFC"
GRID_COLOR = "#E0E0E0"

# Couleurs scénarios
SC_A = "#3498DB"  # Dérive lente (bleu)
SC_B = "#27AE60"  # Rattrapage (vert)
SC_C = "#E74C3C"  # Vassalisation (rouge)
SC_D = "#8E44AD"  # Guerre froide (violet)

# ─── Traductions ────────────────────────────────────────────────────────────
LANGS = {
    "fr": {
        "suffix": "FR",
        # Fig 2.1 — Architecture méthodologique
        "fig1_title": "Architecture méthodologique de l'étude",
        "fig1_retro": "VOLET RÉTROSPECTIF\n2020–2026",
        "fig1_retro_sub": "Diagnostic empirique\n(Chapitre III)",
        "fig1_prosp": "VOLET PROSPECTIF\n2026–2030",
        "fig1_prosp_sub": "Scénarios\n(Chapitre V)",
        "fig1_sources": ["Sources primaires\n(IEA, SIA, BIS)", "Sources académiques\n(Bruegel, Carnegie)", "Sources industry\n(McKinsey, Deloitte)"],
        "fig1_metrics": "6 Métriques\nde divergence\n+ CACI",
        "fig1_scenarios": "4 Scénarios\n(Matrice 2×2)",
        "fig1_output": "Recommandations\n(Chapitre VII)",
        "fig1_method": "Méthode mixte : quantitative descriptive + scenario planning (Schwartz, 1991)",
        "fig1_source": "Élaboration auteur — Section 2.1",

        # Fig 2.2 — Matrice 2×2 scénarios
        "fig2_title": "Matrice 2×2 des scénarios 2026–2030",
        "fig2_xaxis": "Capacité de réponse européenne →",
        "fig2_yaxis": "← Intensité du protectionnisme US",
        "fig2_xlabels": ["EU PASSIVE", "EU ACTIVE (riposte)"],
        "fig2_ylabels": ["US statu quo\nrenforcé", "US durcissement\nagressif"],
        "fig2_scenarios": [
            ("A — Dérive lente", "Gap stable\nDépendance croissante\nVassalisation douce"),
            ("B — Rattrapage partiel", "EU investit massivement\nGap réduit\nAutonomie renforcée"),
            ("C — Vassalisation", "Quotas GPU EU\nProductivité −25%\nDélocalisations massives"),
            ("D — Guerre froide techno.", "Fragmentation bloc\nCoûts élevés\nAutonomie forcée"),
        ],
        "fig2_source": "Élaboration auteur — Section 2.3, inspiré de Schwartz (1991)",

        # Fig 2.3 — 6 Métriques de divergence
        "fig3_title": "Tableau de bord : les six métriques de divergence US/EU",
        "fig3_metrics": ["M1\nCompute\nGap", "M2\nCoût relatif\ndu FLOP", "M3\nDépendance\nCloud",
                         "M4\nProductivité\nIA sectorielle", "M5\nContrainte\nÉnergétique", "M6\nDélocalisations\nIA"],
        "fig3_values_label": "Situation actuelle (2025-2026)",
        "fig3_values": ["×15\n(US/EU)", "×2-3\n(EU/US)", "~70%\nsur infra US",
                        "+12% US\nvs +3% EU", "Critique\n(20% projets\nretardés EU)", "~8%\nprojets EU\nvers US"],
        "fig3_source": "Élaboration auteur — Section 2.4.1",

        # Fig 2.4 — CACI décomposé
        "fig4_title": "Décomposition du Compute-Adjusted\nCompetitiveness Index (CACI)",
        "fig4_formula": "CACI(r) = [ F(r) × E(r)⁻¹ ] / [ PIB(r) × L(r) ]",
        "fig4_components": [
            ("F(r)", "FLOPs IA installés\net accessibles", "Epoch AI, CFG,\nTop500, Hawkins\net al. (2025)"),
            ("E(r)⁻¹", "Inverse du coût\nénergétique (€/MWh)", "Eurostat, EIA,\nIEA (2025)"),
            ("PIB(r)", "Produit Intérieur\nBrut (normalisation)", "Banque mondiale,\nEurostat"),
            ("L(r)", "Capital humain IA\n(diplômés STEM)", "OCDE, LinkedIn\nEconomic Graph"),
        ],
        "fig4_interpret": "Ratio CACI(US)/CACI(EU) = avantage concurrentiel relatif",
        "fig4_source": "Élaboration auteur — Section 2.4.2",
        "fig4_numerator": "NUMÉRATEUR\n(capacité effective)",
        "fig4_denominator": "DÉNOMINATEUR\n(normalisation)",

        # Fig 2.5 — Sources et triangulation
        "fig5_title": "Triangulation des sources : classification et biais",
        "fig5_cats": ["Sources primaires\nofficielless", "Sources académiques\n/ think tanks", "Sources industry\n/ consulting"],
        "fig5_fiab": [9, 7.5, 5.5],
        "fig5_couv": [6, 7, 8.5],
        "fig5_biais": [3, 5, 8],
        "fig5_fiab_label": "Fiabilité factuelle",
        "fig5_couv_label": "Couverture données",
        "fig5_biais_label": "Risque de biais",
        "fig5_source": "Élaboration auteur — Section 2.2",

        # Fig 2.6 — Périmètre temporel et géographique
        "fig6_title": "Périmètre de l'étude : axes temporel, géographique\net technologique",
        "fig6_time_label": "AXE TEMPOREL",
        "fig6_retro": "Diagnostic rétrospectif\n2020 → 2026",
        "fig6_prosp": "Projection prospective\n2026 → 2030",
        "fig6_geo_label": "AXE GÉOGRAPHIQUE",
        "fig6_geo_main": ["États-Unis\n(focus principal)", "Union Européenne\n(focus principal)", "France\n(focus spécifique)"],
        "fig6_geo_sec": ["Chine\n(variable\ncontextuelle)", "Japon / Corée\n/ Taïwan\n(chaîne appro.)"],
        "fig6_tech_label": "AXE TECHNOLOGIQUE",
        "fig6_tech": ["IA de frontière\n(modèles fondation)", "GPU / ASIC\n(semi-conducteurs)", "Data centers\n& Énergie", "Robotique IA\n(amplificateur)"],
        "fig6_source": "Élaboration auteur — Section 2.5",
    },
    "en": {
        "suffix": "EN",
        "fig1_title": "Study Methodological Architecture",
        "fig1_retro": "RETROSPECTIVE\n2020–2026",
        "fig1_retro_sub": "Empirical Diagnosis\n(Chapter III)",
        "fig1_prosp": "PROSPECTIVE\n2026–2030",
        "fig1_prosp_sub": "Scenarios\n(Chapter V)",
        "fig1_sources": ["Primary sources\n(IEA, SIA, BIS)", "Academic sources\n(Bruegel, Carnegie)", "Industry sources\n(McKinsey, Deloitte)"],
        "fig1_metrics": "6 Divergence\nMetrics\n+ CACI",
        "fig1_scenarios": "4 Scenarios\n(2×2 Matrix)",
        "fig1_output": "Recommendations\n(Chapter VII)",
        "fig1_method": "Mixed method: descriptive quantitative + scenario planning (Schwartz, 1991)",
        "fig1_source": "Author's elaboration — Section 2.1",

        "fig2_title": "2×2 Scenario Matrix 2026–2030",
        "fig2_xaxis": "European Response Capacity →",
        "fig2_yaxis": "← US Protectionism Intensity",
        "fig2_xlabels": ["EU PASSIVE", "EU ACTIVE (response)"],
        "fig2_ylabels": ["US reinforced\nstatus quo", "US aggressive\nhardening"],
        "fig2_scenarios": [
            ("A — Slow Drift", "Stable gap\nGrowing dependence\nSoft vassalization"),
            ("B — Partial Catch-up", "EU invests massively\nGap reduced\nEnhanced autonomy"),
            ("C — Vassalization", "GPU quotas for EU\nProductivity −25%\nMass relocations"),
            ("D — Tech Cold War", "Western bloc\nfragmentation\nHigh costs, forced autonomy"),
        ],
        "fig2_source": "Author's elaboration — Section 2.3, inspired by Schwartz (1991)",

        "fig3_title": "Dashboard: Six US/EU Divergence Metrics",
        "fig3_metrics": ["M1\nCompute\nGap", "M2\nRelative\nFLOP Cost", "M3\nCloud\nDependence",
                         "M4\nSectoral AI\nProductivity", "M5\nEnergy\nConstraint", "M6\nAI\nRelocations"],
        "fig3_values_label": "Current situation (2025-2026)",
        "fig3_values": ["×15\n(US/EU)", "×2-3\n(EU/US)", "~70%\non US infra",
                        "+12% US\nvs +3% EU", "Critical\n(20% EU projects\ndelayed)", "~8%\nEU projects\nto US"],
        "fig3_source": "Author's elaboration — Section 2.4.1",

        "fig4_title": "Decomposition of the Compute-Adjusted\nCompetitiveness Index (CACI)",
        "fig4_formula": "CACI(r) = [ F(r) × E(r)⁻¹ ] / [ GDP(r) × L(r) ]",
        "fig4_components": [
            ("F(r)", "Installed & accessible\nAI FLOPs", "Epoch AI, CFG,\nTop500, Hawkins\net al. (2025)"),
            ("E(r)⁻¹", "Inverse energy cost\n(€/MWh)", "Eurostat, EIA,\nIEA (2025)"),
            ("GDP(r)", "Gross Domestic\nProduct (normalization)", "World Bank,\nEurostat"),
            ("L(r)", "AI Human Capital\n(STEM graduates)", "OECD, LinkedIn\nEconomic Graph"),
        ],
        "fig4_interpret": "CACI(US)/CACI(EU) ratio = relative competitive advantage",
        "fig4_source": "Author's elaboration — Section 2.4.2",
        "fig4_numerator": "NUMERATOR\n(effective capacity)",
        "fig4_denominator": "DENOMINATOR\n(normalization)",

        "fig5_title": "Source Triangulation: Classification and Bias",
        "fig5_cats": ["Primary official\nsources", "Academic /\nthink tank sources", "Industry /\nconsulting sources"],
        "fig5_fiab": [9, 7.5, 5.5],
        "fig5_couv": [6, 7, 8.5],
        "fig5_biais": [3, 5, 8],
        "fig5_fiab_label": "Factual reliability",
        "fig5_couv_label": "Data coverage",
        "fig5_biais_label": "Bias risk",
        "fig5_source": "Author's elaboration — Section 2.2",

        "fig6_title": "Study Scope: Temporal, Geographic\nand Technological Axes",
        "fig6_time_label": "TEMPORAL AXIS",
        "fig6_retro": "Retrospective diagnosis\n2020 → 2026",
        "fig6_prosp": "Prospective projection\n2026 → 2030",
        "fig6_geo_label": "GEOGRAPHIC AXIS",
        "fig6_geo_main": ["United States\n(primary focus)", "European Union\n(primary focus)", "France\n(specific focus)"],
        "fig6_geo_sec": ["China\n(contextual\nvariable)", "Japan / Korea\n/ Taiwan\n(supply chain)"],
        "fig6_tech_label": "TECHNOLOGICAL AXIS",
        "fig6_tech": ["Frontier AI\n(foundation models)", "GPU / ASIC\n(semiconductors)", "Data centers\n& Energy", "AI Robotics\n(amplifier)"],
        "fig6_source": "Author's elaboration — Section 2.5",
    },
    "pt": {
        "suffix": "PT-BR",
        "fig1_title": "Arquitetura Metodológica do Estudo",
        "fig1_retro": "COMPONENTE\nRETROSPECTIVO\n2020–2026",
        "fig1_retro_sub": "Diagnóstico Empírico\n(Capítulo III)",
        "fig1_prosp": "COMPONENTE\nPROSPECTIVO\n2026–2030",
        "fig1_prosp_sub": "Cenários\n(Capítulo V)",
        "fig1_sources": ["Fontes primárias\n(IEA, SIA, BIS)", "Fontes acadêmicas\n(Bruegel, Carnegie)", "Fontes industry\n(McKinsey, Deloitte)"],
        "fig1_metrics": "6 Métricas\nde divergência\n+ CACI",
        "fig1_scenarios": "4 Cenários\n(Matriz 2×2)",
        "fig1_output": "Recomendações\n(Capítulo VII)",
        "fig1_method": "Método misto: quantitativo descritivo + planejamento por cenários (Schwartz, 1991)",
        "fig1_source": "Elaboração do autor — Seção 2.1",

        "fig2_title": "Matriz 2×2 de Cenários 2026–2030",
        "fig2_xaxis": "Capacidade de resposta europeia →",
        "fig2_yaxis": "← Intensidade do protecionismo EUA",
        "fig2_xlabels": ["UE PASSIVA", "UE ATIVA (resposta)"],
        "fig2_ylabels": ["EUA status quo\nreforçado", "EUA endurecimento\nagressivo"],
        "fig2_scenarios": [
            ("A — Deriva lenta", "Gap estável\nDependência crescente\nVassalização suave"),
            ("B — Recuperação parcial", "UE investe maciçamente\nGap reduzido\nAutonomia reforçada"),
            ("C — Vassalização", "Cotas GPU UE\nProdutividade −25%\nDeslocalizações massivas"),
            ("D — Guerra fria tecno.", "Fragmentação bloco\nCustos elevados\nAutonomia forçada"),
        ],
        "fig2_source": "Elaboração do autor — Seção 2.3, inspirado em Schwartz (1991)",

        "fig3_title": "Painel: Seis Métricas de Divergência EUA/UE",
        "fig3_metrics": ["M1\nCompute\nGap", "M2\nCusto relativo\ndo FLOP", "M3\nDependência\nCloud",
                         "M4\nProdutividade\nIA setorial", "M5\nRestrição\nEnergética", "M6\nDeslocalizações\nIA"],
        "fig3_values_label": "Situação atual (2025-2026)",
        "fig3_values": ["×15\n(EUA/UE)", "×2-3\n(UE/EUA)", "~70%\nem infra EUA",
                        "+12% EUA\nvs +3% UE", "Crítico\n(20% projetos\natrasados UE)", "~8%\nprojetos UE\npara EUA"],
        "fig3_source": "Elaboração do autor — Seção 2.4.1",

        "fig4_title": "Decomposição do Compute-Adjusted\nCompetitiveness Index (CACI)",
        "fig4_formula": "CACI(r) = [ F(r) × E(r)⁻¹ ] / [ PIB(r) × L(r) ]",
        "fig4_components": [
            ("F(r)", "FLOPs IA instalados\ne acessíveis", "Epoch AI, CFG,\nTop500, Hawkins\net al. (2025)"),
            ("E(r)⁻¹", "Inverso do custo\nenergético (€/MWh)", "Eurostat, EIA,\nIEA (2025)"),
            ("PIB(r)", "Produto Interno\nBruto (normalização)", "Banco Mundial,\nEurostat"),
            ("L(r)", "Capital humano IA\n(graduados STEM)", "OCDE, LinkedIn\nEconomic Graph"),
        ],
        "fig4_interpret": "Razão CACI(EUA)/CACI(UE) = vantagem competitiva relativa",
        "fig4_source": "Elaboração do autor — Seção 2.4.2",
        "fig4_numerator": "NUMERADOR\n(capacidade efetiva)",
        "fig4_denominator": "DENOMINADOR\n(normalização)",

        "fig5_title": "Triangulação de Fontes: Classificação e Vieses",
        "fig5_cats": ["Fontes primárias\noficiais", "Fontes acadêmicas\n/ think tanks", "Fontes industry\n/ consultoria"],
        "fig5_fiab": [9, 7.5, 5.5],
        "fig5_couv": [6, 7, 8.5],
        "fig5_biais": [3, 5, 8],
        "fig5_fiab_label": "Confiabilidade factual",
        "fig5_couv_label": "Cobertura de dados",
        "fig5_biais_label": "Risco de viés",
        "fig5_source": "Elaboração do autor — Seção 2.2",

        "fig6_title": "Escopo do Estudo: Eixos Temporal, Geográfico\ne Tecnológico",
        "fig6_time_label": "EIXO TEMPORAL",
        "fig6_retro": "Diagnóstico retrospectivo\n2020 → 2026",
        "fig6_prosp": "Projeção prospectiva\n2026 → 2030",
        "fig6_geo_label": "EIXO GEOGRÁFICO",
        "fig6_geo_main": ["Estados Unidos\n(foco principal)", "União Europeia\n(foco principal)", "França\n(foco específico)"],
        "fig6_geo_sec": ["China\n(variável\ncontextual)", "Japão / Coreia\n/ Taiwan\n(cadeia suprim.)"],
        "fig6_tech_label": "EIXO TECNOLÓGICO",
        "fig6_tech": ["IA de fronteira\n(modelos fundação)", "GPU / ASIC\n(semicondutores)", "Data centers\n& Energia", "Robótica IA\n(amplificador)"],
        "fig6_source": "Elaboração do autor — Seção 2.5",
    }
}


def setup_style():
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 11,
        'axes.facecolor': BG_COLOR,
        'figure.facecolor': 'white',
        'axes.grid': False,
        'axes.spines.top': False,
        'axes.spines.right': False,
    })


def save_fig(fig, name, lang_suffix):
    path = os.path.join(OUTPUT_DIR, f"{name}_{lang_suffix}.png")
    fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  ✓ {path}")
    return path


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 2.1 — Architecture méthodologique (flowchart)
# Page suggestion : p. 1-2 (ouverture du chapitre, après §2.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig1_architecture(L, lang_key):
    fig, ax = plt.subplots(figsize=(14, 8.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Titre
    ax.text(7, 8.1, L["fig1_title"], ha='center', fontsize=15, fontweight='bold')

    # ── Volet rétrospectif (gauche) ──
    rect = mpatches.FancyBboxPatch((0.5, 4.5), 5.5, 3.0, boxstyle="round,pad=0.2",
                                    facecolor=US_COLOR, alpha=0.08, edgecolor=US_COLOR, linewidth=2)
    ax.add_patch(rect)
    ax.text(3.25, 7.1, L["fig1_retro"], ha='center', fontsize=11, fontweight='bold', color=US_COLOR)
    ax.text(3.25, 6.3, L["fig1_retro_sub"], ha='center', fontsize=10, color=US_COLOR)

    # Sources (3 petites boîtes)
    src_colors = [ACCENT1, ACCENT2, ACCENT3]
    for i, (src, col) in enumerate(zip(L["fig1_sources"], src_colors)):
        y = 5.6 - i * 0.55
        r = mpatches.FancyBboxPatch((0.8, y - 0.22), 4.8, 0.44, boxstyle="round,pad=0.08",
                                     facecolor=col, alpha=0.1, edgecolor=col, linewidth=1)
        ax.add_patch(r)
        ax.text(3.2, y, src, ha='center', va='center', fontsize=7.5, color=col)

    # ── Volet prospectif (droite) ──
    rect2 = mpatches.FancyBboxPatch((8.0, 4.5), 5.5, 3.0, boxstyle="round,pad=0.2",
                                     facecolor=ACCENT2, alpha=0.08, edgecolor=ACCENT2, linewidth=2)
    ax.add_patch(rect2)
    ax.text(10.75, 7.1, L["fig1_prosp"], ha='center', fontsize=11, fontweight='bold', color=ACCENT2)
    ax.text(10.75, 6.3, L["fig1_prosp_sub"], ha='center', fontsize=10, color=ACCENT2)

    # Scénarios (boîte)
    r = mpatches.FancyBboxPatch((8.5, 4.8), 4.5, 1.2, boxstyle="round,pad=0.1",
                                 facecolor=ACCENT2, alpha=0.12, edgecolor=ACCENT2, linewidth=1)
    ax.add_patch(r)
    ax.text(10.75, 5.4, L["fig1_scenarios"], ha='center', va='center', fontsize=9, fontweight='bold', color=ACCENT2)

    # ── Métriques centrales ──
    r_met = mpatches.FancyBboxPatch((5.2, 2.0), 3.6, 1.8, boxstyle="round,pad=0.15",
                                     facecolor=CN_COLOR, alpha=0.1, edgecolor=CN_COLOR, linewidth=2.5)
    ax.add_patch(r_met)
    ax.text(7.0, 2.9, L["fig1_metrics"], ha='center', va='center', fontsize=11, fontweight='bold', color=CN_COLOR)

    # ── Output ──
    r_out = mpatches.FancyBboxPatch((5.2, 0.3), 3.6, 1.2, boxstyle="round,pad=0.15",
                                     facecolor=ACCENT1, alpha=0.12, edgecolor=ACCENT1, linewidth=2)
    ax.add_patch(r_out)
    ax.text(7.0, 0.9, L["fig1_output"], ha='center', va='center', fontsize=10, fontweight='bold', color=ACCENT1)

    # Flèches
    arrow_kw = dict(arrowstyle='->', lw=2.5, color='#666')
    # Retro → Métriques
    ax.annotate('', xy=(5.8, 3.4), xytext=(3.25, 4.5), arrowprops=arrow_kw)
    # Prosp → Métriques
    ax.annotate('', xy=(8.2, 3.4), xytext=(10.75, 4.5), arrowprops=arrow_kw)
    # Métriques → Output
    ax.annotate('', xy=(7.0, 1.5), xytext=(7.0, 2.0), arrowprops=arrow_kw)
    # Retro → Prosp
    ax.annotate('', xy=(8.0, 6.0), xytext=(6.0, 6.0),
                arrowprops=dict(arrowstyle='->', lw=2, color=ACCENT4, linestyle='--'))

    # Méthode
    ax.text(7, -0.15, L["fig1_method"], ha='center', fontsize=9, fontstyle='italic', color='#666',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0F0F0', edgecolor='#CCC'))
    ax.text(7, -0.65, L["fig1_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')

    return save_fig(fig, "Fig_2.1_Methodological_Architecture", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 2.2 — Matrice 2×2 des scénarios
# Page suggestion : p. 3-4 (section 2.3, Étape 2)
# ═══════════════════════════════════════════════════════════════════════════
def fig2_scenario_matrix(L, lang_key):
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis('off')

    ax.text(6, 8.6, L["fig2_title"], ha='center', fontsize=15, fontweight='bold')

    # Quadrants
    sc_colors = [SC_A, SC_B, SC_C, SC_D]
    positions = [(1.0, 4.6), (6.2, 4.6), (1.0, 0.8), (6.2, 0.8)]  # A, B, C, D
    qw, qh = 4.8, 3.4

    for i, ((x, y), col) in enumerate(zip(positions, sc_colors)):
        rect = mpatches.FancyBboxPatch((x, y), qw, qh, boxstyle="round,pad=0.15",
                                        facecolor=col, alpha=0.08, edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        title, desc = L["fig2_scenarios"][i]
        ax.text(x + qw/2, y + qh - 0.4, title, ha='center', fontsize=12,
                fontweight='bold', color=col)
        ax.text(x + qw/2, y + qh/2 - 0.2, desc, ha='center', va='center',
                fontsize=9.5, color='#333', linespacing=1.4)

    # Axes labels
    # X axis
    ax.annotate('', xy=(11.5, 4.45), xytext=(0.5, 4.45),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='#999'))
    ax.text(0.8, 4.2, L["fig2_xlabels"][0], fontsize=9, color='#999', fontstyle='italic')
    ax.text(10.2, 4.2, L["fig2_xlabels"][1], fontsize=9, color='#999', fontstyle='italic', ha='right')
    ax.text(6, 4.15, L["fig2_xaxis"], ha='center', fontsize=10, color='#666')

    # Y axis
    ax.annotate('', xy=(0.7, 8.3), xytext=(0.7, 0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='#999'))
    ax.text(0.2, 1.5, L["fig2_ylabels"][1], fontsize=8, color='#999', fontstyle='italic',
            rotation=90, va='center')
    ax.text(0.2, 6.5, L["fig2_ylabels"][0], fontsize=8, color='#999', fontstyle='italic',
            rotation=90, va='center')

    ax.text(6, 0.15, L["fig2_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')

    return save_fig(fig, "Fig_2.2_Scenario_Matrix_2x2", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 2.3 — Six métriques de divergence (dashboard)
# Page suggestion : p. 4-5 (section 2.4.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig3_metrics_dashboard(L, lang_key):
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    fig.suptitle(L["fig3_title"], fontsize=14, fontweight='bold', y=0.98)

    colors = [CN_COLOR, ACCENT3, US_COLOR, ACCENT1, ACCENT2, SC_D]
    severity = [0.9, 0.6, 0.85, 0.7, 0.8, 0.5]  # for visual gauge

    for idx, ax in enumerate(axes.flat):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        col = colors[idx]
        # Card background
        rect = mpatches.FancyBboxPatch((0.3, 0.3), 9.4, 9.4, boxstyle="round,pad=0.3",
                                        facecolor=col, alpha=0.06, edgecolor=col, linewidth=2)
        ax.add_patch(rect)

        # Metric name
        ax.text(5, 8.2, L["fig3_metrics"][idx], ha='center', va='center',
                fontsize=10, fontweight='bold', color=col, linespacing=1.2)

        # Value
        ax.text(5, 4.5, L["fig3_values"][idx], ha='center', va='center',
                fontsize=11, fontweight='bold', color='#333', linespacing=1.3)

        # Severity bar
        bar_w = 7 * severity[idx]
        rect_bar = mpatches.FancyBboxPatch((1.5, 1.2), bar_w, 0.6, boxstyle="round,pad=0.05",
                                            facecolor=col, alpha=0.4, edgecolor='none')
        ax.add_patch(rect_bar)
        rect_bg = mpatches.FancyBboxPatch((1.5, 1.2), 7, 0.6, boxstyle="round,pad=0.05",
                                           facecolor='#EEE', alpha=0.5, edgecolor='#CCC', linewidth=0.5)
        ax.add_patch(rect_bg)
        rect_bar2 = mpatches.FancyBboxPatch((1.5, 1.2), bar_w, 0.6, boxstyle="round,pad=0.05",
                                             facecolor=col, alpha=0.5, edgecolor='none')
        ax.add_patch(rect_bar2)

    fig.text(0.5, 0.02, L["fig3_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')
    plt.tight_layout(rect=[0, 0.04, 1, 0.95])

    return save_fig(fig, "Fig_2.3_Metrics_Dashboard", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 2.4 — Décomposition CACI
# Page suggestion : p. 5-6 (section 2.4.2)
# ═══════════════════════════════════════════════════════════════════════════
def fig4_caci_decomposition(L, lang_key):
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(7, 7.6, L["fig4_title"], ha='center', fontsize=14, fontweight='bold')

    # Formule principale
    ax.text(7, 6.7, L["fig4_formula"], ha='center', fontsize=16, fontweight='bold',
            color=ACCENT4, family='monospace',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#F8F8F8', edgecolor=ACCENT4, linewidth=2))

    # 4 composantes
    comp_colors = [US_COLOR, ACCENT3, ACCENT1, ACCENT2]
    comp_x = [1.0, 4.5, 8.0, 11.0]
    box_w, box_h = 2.5, 3.0

    for i, (cx, col) in enumerate(zip(comp_x, comp_colors)):
        symbol, desc, source = L["fig4_components"][i]

        rect = mpatches.FancyBboxPatch((cx, 1.8), box_w, box_h, boxstyle="round,pad=0.15",
                                        facecolor=col, alpha=0.08, edgecolor=col, linewidth=2)
        ax.add_patch(rect)

        # Symbol
        ax.text(cx + box_w/2, 4.3, symbol, ha='center', fontsize=14, fontweight='bold', color=col)
        # Description
        ax.text(cx + box_w/2, 3.3, desc, ha='center', va='center', fontsize=8.5, color='#333')
        # Source
        ax.text(cx + box_w/2, 2.2, source, ha='center', va='center', fontsize=7,
                color='#888', fontstyle='italic')

        # Flèche vers formule
        ax.annotate('', xy=(cx + box_w/2, 5.8), xytext=(cx + box_w/2, 4.8),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color=col, linestyle='--'))

    # Labels numérateur / dénominateur
    # Numérateur = F(r) et E(r)
    ax.text(3.5, 5.5, L["fig4_numerator"], ha='center', fontsize=9, fontweight='bold',
            color=US_COLOR, bbox=dict(boxstyle='round,pad=0.2', facecolor=US_COLOR, alpha=0.1, edgecolor=US_COLOR))
    # Dénominateur = PIB et L
    ax.text(10.5, 5.5, L["fig4_denominator"], ha='center', fontsize=9, fontweight='bold',
            color=ACCENT1, bbox=dict(boxstyle='round,pad=0.2', facecolor=ACCENT1, alpha=0.1, edgecolor=ACCENT1))

    # Multiplication signs
    ax.text(3.7, 3.3, "×", fontsize=20, fontweight='bold', color='#999', ha='center')
    ax.text(7.2, 3.3, "/", fontsize=24, fontweight='bold', color='#999', ha='center')
    ax.text(10.7, 3.3, "×", fontsize=20, fontweight='bold', color='#999', ha='center')

    # Interprétation
    ax.text(7, 1.2, L["fig4_interpret"], ha='center', fontsize=11, fontweight='bold',
            color=CN_COLOR, bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=CN_COLOR))

    ax.text(7, 0.4, L["fig4_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')

    return save_fig(fig, "Fig_2.4_CACI_Decomposition", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 2.5 — Triangulation des sources
# Page suggestion : p. 2-3 (section 2.2)
# ═══════════════════════════════════════════════════════════════════════════
def fig5_source_triangulation(L, lang_key):
    fig, ax = plt.subplots(figsize=(11, 7))

    cats = L["fig5_cats"]
    x = np.arange(len(cats))
    width = 0.25

    bars1 = ax.bar(x - width, L["fig5_fiab"], width, color=ACCENT1, alpha=0.8,
                   label=L["fig5_fiab_label"], edgecolor='white', linewidth=1.5)
    bars2 = ax.bar(x, L["fig5_couv"], width, color=US_COLOR, alpha=0.8,
                   label=L["fig5_couv_label"], edgecolor='white', linewidth=1.5)
    bars3 = ax.bar(x + width, L["fig5_biais"], width, color=CN_COLOR, alpha=0.8,
                   label=L["fig5_biais_label"], edgecolor='white', linewidth=1.5)

    # Valeurs
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.15, f"{h:.1f}",
                    ha='center', fontsize=9, fontweight='bold', color='#333')

    ax.set_title(L["fig5_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=10)
    ax.set_ylim(0, 11)
    ax.set_ylabel("/10", fontsize=11)
    ax.legend(fontsize=10, loc='upper right', framealpha=0.9)
    ax.grid(axis='y', color=GRID_COLOR, alpha=0.5)

    ax.text(0.5, -0.12, L["fig5_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')

    return save_fig(fig, "Fig_2.5_Source_Triangulation", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# FIGURE 2.6 — Périmètre de l'étude
# Page suggestion : p. 6-7 (section 2.5)
# ═══════════════════════════════════════════════════════════════════════════
def fig6_study_scope(L, lang_key):
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')

    ax.text(7, 8.6, L["fig6_title"], ha='center', fontsize=14, fontweight='bold')

    # ── AXE TEMPOREL (top) ──
    ax.text(1.2, 7.8, L["fig6_time_label"], fontsize=10, fontweight='bold', color=US_COLOR)
    # Rétrospectif
    rect_r = mpatches.FancyBboxPatch((1.5, 6.8), 4.8, 0.85, boxstyle="round,pad=0.1",
                                      facecolor=US_COLOR, alpha=0.1, edgecolor=US_COLOR, linewidth=1.5)
    ax.add_patch(rect_r)
    ax.text(3.9, 7.22, L["fig6_retro"], ha='center', va='center', fontsize=9, color=US_COLOR)
    # Prospectif
    rect_p = mpatches.FancyBboxPatch((7.0, 6.8), 4.8, 0.85, boxstyle="round,pad=0.1",
                                      facecolor=ACCENT2, alpha=0.1, edgecolor=ACCENT2, linewidth=1.5)
    ax.add_patch(rect_p)
    ax.text(9.4, 7.22, L["fig6_prosp"], ha='center', va='center', fontsize=9, color=ACCENT2)
    # Arrow
    ax.annotate('', xy=(12.2, 7.22), xytext=(1.2, 7.22),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='#999'))

    # ── AXE GÉOGRAPHIQUE (middle) ──
    ax.text(1.2, 6.1, L["fig6_geo_label"], fontsize=10, fontweight='bold', color=ACCENT1)
    geo_main_colors = [US_COLOR, EU_COLOR, FR_COLOR]
    for i, (label, col) in enumerate(zip(L["fig6_geo_main"], geo_main_colors)):
        x = 1.5 + i * 3.0
        rect = mpatches.FancyBboxPatch((x, 4.9), 2.6, 1.0, boxstyle="round,pad=0.1",
                                        facecolor=col, alpha=0.12, edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + 1.3, 5.4, label, ha='center', va='center', fontsize=8.5, fontweight='bold', color=col)

    for i, label in enumerate(L["fig6_geo_sec"]):
        x = 10.2 + i * 1.8
        rect = mpatches.FancyBboxPatch((x, 4.9), 1.6, 1.0, boxstyle="round,pad=0.1",
                                        facecolor='#EEE', edgecolor='#999', linewidth=1, linestyle='--')
        ax.add_patch(rect)
        ax.text(x + 0.8, 5.4, label, ha='center', va='center', fontsize=7, color='#666', fontstyle='italic')

    # ── AXE TECHNOLOGIQUE (bottom) ──
    ax.text(1.2, 4.1, L["fig6_tech_label"], fontsize=10, fontweight='bold', color=ACCENT3)
    tech_colors = [CN_COLOR, ACCENT4, ACCENT3, ACCENT2]
    for i, (label, col) in enumerate(zip(L["fig6_tech"], tech_colors)):
        x = 1.5 + i * 3.0
        rect = mpatches.FancyBboxPatch((x, 2.5), 2.6, 1.2, boxstyle="round,pad=0.1",
                                        facecolor=col, alpha=0.1, edgecolor=col, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + 1.3, 3.1, label, ha='center', va='center', fontsize=8.5, color=col)

    # Connecting arrows tech
    for i in range(3):
        x_start = 1.5 + i * 3.0 + 2.6
        x_end = 1.5 + (i+1) * 3.0
        ax.annotate('', xy=(x_end, 3.1), xytext=(x_start, 3.1),
                    arrowprops=dict(arrowstyle='->', lw=1.2, color='#BBB'))

    # Timeline marks
    years = [2020, 2022, 2024, 2026, 2028, 2030]
    for yr in years:
        xpos = 1.5 + (yr - 2020) * (10.5 / 10)
        ax.text(xpos, 1.8, str(yr), ha='center', fontsize=9, color='#888')
        ax.plot([xpos, xpos], [1.95, 2.15], color='#BBB', linewidth=1)
    ax.plot([1.5, 12.0], [2.1, 2.1], color='#CCC', linewidth=1)
    # 2026 highlight
    x2026 = 1.5 + 6 * (10.5/10)
    ax.axvline(x=x2026, ymin=0.19, ymax=0.85, color=CN_COLOR, linewidth=1.5, linestyle='--', alpha=0.4)

    ax.text(7, 0.8, L["fig6_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')

    return save_fig(fig, "Fig_2.6_Study_Scope", L["suffix"])


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()

    print("=" * 70)
    print(" CHAPITRE II — Génération des graphiques en 3 langues")
    print("=" * 70)

    all_files = []

    for lang_key, L in LANGS.items():
        print(f"\n{'─'*50}")
        print(f" Langue : {L['suffix']}")
        print(f"{'─'*50}")

        all_files.append(fig1_architecture(L, lang_key))
        all_files.append(fig2_scenario_matrix(L, lang_key))
        all_files.append(fig3_metrics_dashboard(L, lang_key))
        all_files.append(fig4_caci_decomposition(L, lang_key))
        all_files.append(fig5_source_triangulation(L, lang_key))
        all_files.append(fig6_study_scope(L, lang_key))

    print(f"\n{'='*70}")
    print(f" Total : {len(all_files)} fichiers générés dans {OUTPUT_DIR}/")
    print(f"{'='*70}")

    print("""
╔══════════════════════════════════════════════════════════════════════╗
║  GUIDE D'INSERTION — Chapitre II                                   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Fig 2.1  Architecture méthodologique  → p.1-2 (après §2.1)       ║
║           Flowchart des deux volets + métriques                    ║
║                                                                    ║
║  Fig 2.2  Matrice 2×2 scénarios       → p.3-4 (§2.3 Étape 2)    ║
║           4 quadrants : Dérive / Rattrapage / Vassal. / Gfroide   ║
║                                                                    ║
║  Fig 2.3  Dashboard 6 métriques       → p.4-5 (§2.4.1)          ║
║           M1-M6 avec valeurs actuelles et jauges                   ║
║                                                                    ║
║  Fig 2.4  Décomposition CACI          → p.5-6 (§2.4.2)          ║
║           Formule + 4 composantes + sources                        ║
║                                                                    ║
║  Fig 2.5  Triangulation sources       → p.2-3 (§2.2)            ║
║           Fiabilité / Couverture / Biais par catégorie             ║
║                                                                    ║
║  Fig 2.6  Périmètre de l'étude        → p.6-7 (§2.5)            ║
║           3 axes : temporel / géographique / technologique         ║
║                                                                    ║
╚══════════════════════════════════════════════════════════════════════╝
    """)

    return all_files


if __name__ == "__main__":
    main()
