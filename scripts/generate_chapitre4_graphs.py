#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre IV : Mécanismes Avantage Concurrentiel
 Générateur de graphiques en 3 langues (FR / EN / PT-BR)
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

US_COLOR = "#1B4F72"; EU_COLOR = "#D4AC0D"; CN_COLOR = "#C0392B"
FR_COLOR = "#2E86C1"; ACCENT1 = "#148F77"; ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"; ACCENT4 = "#2C3E50"; REST_COLOR = "#95A5A6"
BG_COLOR = "#FAFBFC"; GRID_COLOR = "#E0E0E0"

LANGS = {
  "fr": {
    "suffix": "FR",
    # Fig 4.1 — Coûts training exponentiels
    "f1_title": "Explosion des coûts d'entraînement des modèles IA\n(2017–2030, estimation)",
    "f1_ylabel": "Coût d'entraînement (USD, échelle log)",
    "f1_source": "Sources : Epoch AI, Martens/Bruegel (2024), Cottier et al. (2024)",
    "f1_note": "Infrastructure ≈ 10× coût training",
    # Fig 4.2 — Cloud EU dominé par US
    "f2_title": "Marché cloud européen : domination des hyperscalers US\n(2017–2024)",
    "f2_ylabel": "Milliards € / Part de marché (%)",
    "f2_us3": "AWS + Azure + GCP", "f2_eu": "Fournisseurs EU", "f2_other": "Autres",
    "f2_market": "Taille marché (€ Md)", "f2_source": "Source : Synergy Research Group (juil. 2025)",
    # Fig 4.3 — Gap productivité
    "f3_title": "Productivité IA : potentiel théorique vs réalisable\n(États-Unis vs Union Européenne)",
    "f3_ylabel": "Croissance productivité (%/an)",
    "f3_cats": ["Potentiel\nthéorique\n(scén. accéléré)", "Potentiel\nréalisable\n(sous contrainte\ncompute)"],
    "f3_us": "États-Unis", "f3_eu": "Union Européenne",
    "f3_gap": "Gap\n−1,5 à −2\npts/an",
    "f3_source": "Sources : McKinsey (2024, 2025), FMI (2025), calibration CACI auteur",
    # Fig 4.4 — Chaîne de valeur IA gen (présence EU)
    "f4_title": "Chaîne de valeur de l'IA générative :\nprésence européenne par segment",
    "f4_segments": ["Semi-conducteurs\nIA (GPU/ASIC)", "Plateformes\nCloud IA", "Modèles de\nfondation",
                    "Outils de\ndéveloppement", "Applications\nsectorielles", "Semi-conducteurs\nspécialisés",
                    "Intégration\nindustrielle", "Services\nprofessionnels"],
    "f4_eu_presence": [2, 5, 8, 10, 70, 55, 65, 50],  # % EU presence
    "f4_ylabel": "Présence européenne estimée (%)",
    "f4_source": "Sources : McKinsey (2024), Omdia/Informa, estimations auteur",
    "f4_absent": "EU quasi\nabsente", "f4_compet": "EU\ncompétitive",
    # Fig 4.5 — Cercle vicieux renforçant
    "f5_title": "Le cercle auto-renforçant de l'avantage concurrentiel US",
    "f5_boxes": ["ASYMÉTRIE\nDE COMPUTE\n(×15 US/EU)",
                 "COÛTS TRAINING\nDIFFÉRENCIÉS\n(×2,4–3,6)",
                 "DÉPENDANCE\nCLOUD US\n(70% marché EU)",
                 "PRODUCTIVITÉ\nCONTRAINTE\n(−1,5 pts/an)",
                 "CAPTATION\nDES RENTES\n(first-mover)"],
    "f5_center": "PROTECTIONNISME\nSECTION 232\n(institutionnalise\nl'avantage)",
    "f5_source": "Élaboration auteur — Synthèse §4.5",
    # Fig 4.6 — Déficit investissement EU vs US
    "f6_title": "Écart d'investissement technologique\nÉtats-Unis vs Europe (2021–2025)",
    "f6_cats": ["R&D + Capex\ncorporate\n(annuel)", "Startups &\nScale-ups\n(annuel)", "Infrastructure\nIA 2025\n(Big Tech)",
                "Capex cloud\nen Europe\n(US providers)"],
    "f6_us": [1200, 380, 320, 40],  # Md$
    "f6_eu": [500, 80, 20, 5],
    "f6_ylabel": "Milliards USD / an",
    "f6_source": "Sources : McKinsey (2026), IEA (2025), Synergy Research (2025)",
    "f6_us_label": "États-Unis", "f6_eu_label": "Union Européenne",
  },
  "en": {
    "suffix": "EN",
    "f1_title": "Explosion of AI Model Training Costs\n(2017–2030, estimate)",
    "f1_ylabel": "Training cost (USD, log scale)",
    "f1_source": "Sources: Epoch AI, Martens/Bruegel (2024), Cottier et al. (2024)",
    "f1_note": "Infrastructure ≈ 10× training cost",
    "f2_title": "European Cloud Market: US Hyperscaler Dominance\n(2017–2024)",
    "f2_ylabel": "Billion € / Market share (%)",
    "f2_us3": "AWS + Azure + GCP", "f2_eu": "EU providers", "f2_other": "Others",
    "f2_market": "Market size (€ Bn)", "f2_source": "Source: Synergy Research Group (Jul. 2025)",
    "f3_title": "AI Productivity: Theoretical vs Achievable Potential\n(United States vs European Union)",
    "f3_ylabel": "Productivity growth (%/year)",
    "f3_cats": ["Theoretical\npotential\n(accelerated sc.)", "Achievable\npotential\n(compute-\nconstrained)"],
    "f3_us": "United States", "f3_eu": "European Union",
    "f3_gap": "Gap\n−1.5 to −2\npts/year",
    "f3_source": "Sources: McKinsey (2024, 2025), IMF (2025), author CACI calibration",
    "f4_title": "Generative AI Value Chain:\nEuropean Presence by Segment",
    "f4_segments": ["AI Semiconductors\n(GPU/ASIC)", "Cloud AI\nPlatforms", "Foundation\nModels",
                    "Development\nTools", "Sectoral\nApplications", "Specialized\nSemiconductors",
                    "Industrial\nIntegration", "Professional\nServices"],
    "f4_eu_presence": [2, 5, 8, 10, 70, 55, 65, 50],
    "f4_ylabel": "Estimated European presence (%)",
    "f4_source": "Sources: McKinsey (2024), Omdia/Informa, author estimates",
    "f4_absent": "EU nearly\nabsent", "f4_compet": "EU\ncompetitive",
    "f5_title": "The Self-Reinforcing Cycle of US Competitive Advantage",
    "f5_boxes": ["COMPUTE\nASYMMETRY\n(×15 US/EU)",
                 "DIFFERENTIATED\nTRAINING COSTS\n(×2.4–3.6)",
                 "US CLOUD\nDEPENDENCE\n(70% EU market)",
                 "CONSTRAINED\nPRODUCTIVITY\n(−1.5 pts/yr)",
                 "RENT\nCAPTURE\n(first-mover)"],
    "f5_center": "SECTION 232\nPROTECTIONISM\n(institutionalizes\nadvantage)",
    "f5_source": "Author's elaboration — Synthesis §4.5",
    "f6_title": "Technology Investment Gap\nUnited States vs Europe (2021–2025)",
    "f6_cats": ["R&D + Capex\ncorporate\n(annual)", "Startups &\nScale-ups\n(annual)", "AI Infrastructure\n2025\n(Big Tech)",
                "Cloud capex\nin Europe\n(US providers)"],
    "f6_us": [1200, 380, 320, 40],
    "f6_eu": [500, 80, 20, 5],
    "f6_ylabel": "Billion USD / year",
    "f6_source": "Sources: McKinsey (2026), IEA (2025), Synergy Research (2025)",
    "f6_us_label": "United States", "f6_eu_label": "European Union",
  },
  "pt": {
    "suffix": "PT-BR",
    "f1_title": "Explosão dos Custos de Treinamento de Modelos IA\n(2017–2030, estimativa)",
    "f1_ylabel": "Custo de treinamento (USD, escala log)",
    "f1_source": "Fontes: Epoch AI, Martens/Bruegel (2024), Cottier et al. (2024)",
    "f1_note": "Infraestrutura ≈ 10× custo treinamento",
    "f2_title": "Mercado Cloud Europeu: Dominância dos Hyperscalers EUA\n(2017–2024)",
    "f2_ylabel": "Bilhões € / Participação de mercado (%)",
    "f2_us3": "AWS + Azure + GCP", "f2_eu": "Provedores UE", "f2_other": "Outros",
    "f2_market": "Tamanho mercado (€ Bi)", "f2_source": "Fonte: Synergy Research Group (jul. 2025)",
    "f3_title": "Produtividade IA: Potencial Teórico vs Realizável\n(Estados Unidos vs União Europeia)",
    "f3_ylabel": "Crescimento produtividade (%/ano)",
    "f3_cats": ["Potencial\nteórico\n(cen. acelerado)", "Potencial\nrealizável\n(sob restrição\ncompute)"],
    "f3_us": "Estados Unidos", "f3_eu": "União Europeia",
    "f3_gap": "Gap\n−1,5 a −2\npts/ano",
    "f3_source": "Fontes: McKinsey (2024, 2025), FMI (2025), calibração CACI autor",
    "f4_title": "Cadeia de Valor da IA Generativa:\nPresença Europeia por Segmento",
    "f4_segments": ["Semicondutores\nIA (GPU/ASIC)", "Plataformas\nCloud IA", "Modelos de\nFundação",
                    "Ferramentas de\nDesenvolvimento", "Aplicações\nSetoriais", "Semicondutores\nEspecializados",
                    "Integração\nIndustrial", "Serviços\nProfissionais"],
    "f4_eu_presence": [2, 5, 8, 10, 70, 55, 65, 50],
    "f4_ylabel": "Presença europeia estimada (%)",
    "f4_source": "Fontes: McKinsey (2024), Omdia/Informa, estimativas do autor",
    "f4_absent": "UE quase\nausente", "f4_compet": "UE\ncompetitiva",
    "f5_title": "O Ciclo Auto-Reforçante da Vantagem Competitiva dos EUA",
    "f5_boxes": ["ASSIMETRIA\nDE COMPUTE\n(×15 EUA/UE)",
                 "CUSTOS TRAINING\nDIFERENCIADOS\n(×2,4–3,6)",
                 "DEPENDÊNCIA\nCLOUD EUA\n(70% mercado UE)",
                 "PRODUTIVIDADE\nRESTRINGIDA\n(−1,5 pts/ano)",
                 "CAPTURA\nDE RENDAS\n(first-mover)"],
    "f5_center": "PROTECIONISMO\nSEÇÃO 232\n(institucionaliza\na vantagem)",
    "f5_source": "Elaboração do autor — Síntese §4.5",
    "f6_title": "Déficit de Investimento Tecnológico\nEstados Unidos vs Europa (2021–2025)",
    "f6_cats": ["P&D + Capex\ncorporativo\n(anual)", "Startups &\nScale-ups\n(anual)", "Infraestrutura\nIA 2025\n(Big Tech)",
                "Capex cloud\nna Europa\n(provedores EUA)"],
    "f6_us": [1200, 380, 320, 40],
    "f6_eu": [500, 80, 20, 5],
    "f6_ylabel": "Bilhões USD / ano",
    "f6_source": "Fontes: McKinsey (2026), IEA (2025), Synergy Research (2025)",
    "f6_us_label": "Estados Unidos", "f6_eu_label": "União Europeia",
  }
}

def setup_style():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
        'axes.facecolor':BG_COLOR,'figure.facecolor':'white',
        'axes.grid':True,'grid.color':GRID_COLOR,'grid.alpha':0.5,
        'axes.spines.top':False,'axes.spines.right':False})

def save_fig(fig, name, sfx):
    p = os.path.join(OUTPUT_DIR, f"{name}_{sfx}.png")
    fig.savefig(p, dpi=DPI, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig); print(f"  ✓ {p}"); return p

# ═══════════════════════════════════════════════════════════════════════════
# FIG 4.1 — Coûts training exponentiels (log scale)
# Page : p. 1-2 (après §4.1.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig1_training_costs(L, lk):
    fig, ax = plt.subplots(figsize=(12, 7))
    years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2026, 2028, 2030]
    costs = [1e3, 5e3, 5e4, 5e5, 5e6, 3e7, 6e7, 2e8, 8e8, 3e9, 1e10]
    infra = [c * 10 for c in costs]

    ax.semilogy(years, costs, color=US_COLOR, linewidth=3, marker='o', markersize=7,
                label="Training cost", zorder=5)
    ax.fill_between(years, costs, infra, color=ACCENT3, alpha=0.15, label=L["f1_note"])
    ax.semilogy(years, infra, color=ACCENT3, linewidth=1.5, linestyle='--', alpha=0.6)

    # Key annotations
    annotations = [(2017, 1e3, "$1K\n(2017)"), (2024, 2e8, "$200M\n(2024)"),
                   (2030, 1e10, "$10B+\n(2030 est.)")]
    for yr, val, txt in annotations:
        ax.annotate(txt, xy=(yr, val), xytext=(yr-0.8, val*4),
                    fontsize=10, fontweight='bold', color=US_COLOR,
                    arrowprops=dict(arrowstyle='->', color=US_COLOR, lw=1.2))

    ax.axvspan(2024.5, 2030.5, alpha=0.04, color='gray')
    ax.set_title(L["f1_title"], fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel(L["f1_ylabel"], fontsize=12)
    ax.set_xlim(2016.5, 2030.5)
    ax.set_xticks(years)
    ax.legend(fontsize=10, loc='upper left', framealpha=0.9)
    ax.text(0.5, -0.1, L["f1_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_4.1_Training_Costs_Exponential", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 4.2 — Cloud EU dominé par US (dual axis)
# Page : p. 3-4 (après §4.2.1, Tableau 8)
# ═══════════════════════════════════════════════════════════════════════════
def fig2_cloud_market(L, lk):
    fig, ax1 = plt.subplots(figsize=(12, 7))
    years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    market_size = [10, 14, 19, 24, 28, 35, 49, 61]
    us_share = [50, 55, 60, 63, 65, 67, 69, 70]
    eu_share = [29, 25, 22, 19, 17, 15, 15, 15]

    # Bars for market size
    ax1.bar(years, market_size, 0.6, color=REST_COLOR, alpha=0.3, label=L["f2_market"])
    for yr, ms in zip(years, market_size):
        if yr in [2017, 2020, 2024]:
            ax1.text(yr, ms+1.5, f"€{ms}B", ha='center', fontsize=9, fontweight='bold', color='#555')

    ax1.set_ylabel(L["f2_ylabel"].split("/")[0], fontsize=11, color='#555')
    ax1.set_ylim(0, 80)

    # Line for shares
    ax2 = ax1.twinx()
    ax2.plot(years, us_share, color=US_COLOR, linewidth=3, marker='s', markersize=7, label=L["f2_us3"])
    ax2.plot(years, eu_share, color=EU_COLOR, linewidth=3, marker='D', markersize=7, label=L["f2_eu"])
    ax2.set_ylabel("Part de marché (%)" if lk=="fr" else ("Market share (%)" if lk=="en" else "Participação (%)"),
                    fontsize=11, color=US_COLOR)
    ax2.set_ylim(0, 100)

    # Annotations
    ax2.text(2024.2, 70, f"70%", fontsize=12, fontweight='bold', color=US_COLOR)
    ax2.text(2024.2, 15, f"15%", fontsize=12, fontweight='bold', color=EU_COLOR)

    # Legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1+lines2, labels1+labels2, loc='upper left', fontsize=10, framealpha=0.9)

    ax1.set_title(L["f2_title"], fontsize=13, fontweight='bold', pad=15)
    ax1.set_xticks(years)
    ax1.text(0.5, -0.1, L["f2_source"], transform=ax1.transAxes, fontsize=8,
             color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_4.2_Cloud_Market_EU", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 4.3 — Gap productivité théorique vs réalisable
# Page : p. 5-6 (après §4.3.2, Tableau 9)
# ═══════════════════════════════════════════════════════════════════════════
def fig3_productivity_gap(L, lk):
    fig, ax = plt.subplots(figsize=(11, 7))
    cats = L["f3_cats"]
    x = np.arange(len(cats))
    w = 0.32

    us_vals = [3.0, 2.75]
    eu_vals = [2.75, 1.15]

    bars_us = ax.bar(x - w/2, us_vals, w, color=US_COLOR, label=L["f3_us"],
                     edgecolor='white', linewidth=2)
    bars_eu = ax.bar(x + w/2, eu_vals, w, color=EU_COLOR, label=L["f3_eu"],
                     edgecolor='white', linewidth=2)

    for bar, val in zip(bars_us, us_vals):
        ax.text(bar.get_x()+bar.get_width()/2, val+0.08, f"+{val}%",
                ha='center', fontsize=13, fontweight='bold', color=US_COLOR)
    for bar, val in zip(bars_eu, eu_vals):
        ax.text(bar.get_x()+bar.get_width()/2, val+0.08, f"+{val}%",
                ha='center', fontsize=13, fontweight='bold', color=EU_COLOR)

    # Gap annotation on constrained
    mid = (us_vals[1] + eu_vals[1]) / 2
    ax.annotate('', xy=(1+w/2+0.05, eu_vals[1]), xytext=(1+w/2+0.05, us_vals[1]),
                arrowprops=dict(arrowstyle='<->', color=CN_COLOR, lw=2.5))
    ax.text(1+w/2+0.15, mid, L["f3_gap"], fontsize=11, fontweight='bold', color=CN_COLOR,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=CN_COLOR, alpha=0.9))

    # ≈ sign on theoretical
    ax.text(0, 3.2, "≈", fontsize=24, fontweight='bold', color=ACCENT1, ha='center')

    ax.set_title(L["f3_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["f3_ylabel"], fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=10)
    ax.set_ylim(0, 4.0)
    ax.legend(fontsize=11, framealpha=0.9)
    ax.text(0.5, -0.12, L["f3_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_4.3_Productivity_Gap", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 4.4 — Chaîne de valeur IA gen (présence EU)
# Page : p. 7-8 (après §4.4.2)
# ═══════════════════════════════════════════════════════════════════════════
def fig4_value_chain(L, lk):
    fig, ax = plt.subplots(figsize=(13, 7.5))

    segments = L["f4_segments"]
    eu_pres = L["f4_eu_presence"]
    colors = [CN_COLOR if v < 15 else (ACCENT3 if v < 40 else ACCENT1) for v in eu_pres]

    y = np.arange(len(segments))
    bars = ax.barh(y, eu_pres, height=0.6, color=colors, edgecolor='white', linewidth=1.5)

    for bar, val in zip(bars, eu_pres):
        ax.text(val + 1.5, bar.get_y() + bar.get_height()/2, f"{val}%",
                va='center', fontsize=12, fontweight='bold',
                color=CN_COLOR if val < 15 else (ACCENT3 if val < 40 else ACCENT1))

    # Zones
    ax.axvline(x=15, color=CN_COLOR, linewidth=1.5, linestyle='--', alpha=0.5)
    ax.axvline(x=50, color=ACCENT1, linewidth=1.5, linestyle='--', alpha=0.5)
    ax.text(7, 7.8, L["f4_absent"], fontsize=9, fontweight='bold', color=CN_COLOR,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FDEDEC', edgecolor=CN_COLOR, alpha=0.8))
    ax.text(60, 7.8, L["f4_compet"], fontsize=9, fontweight='bold', color=ACCENT1,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#E8F8F5', edgecolor=ACCENT1, alpha=0.8))

    ax.set_yticks(y)
    ax.set_yticklabels(segments, fontsize=10)
    ax.set_xlabel(L["f4_ylabel"], fontsize=11)
    ax.set_xlim(0, 95)
    ax.invert_yaxis()
    ax.set_title(L["f4_title"], fontsize=13, fontweight='bold', pad=15)
    ax.text(0.5, -0.08, L["f4_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_4.4_Value_Chain_EU_Presence", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 4.5 — Cercle vicieux renforçant (schéma)
# Page : p. 8-9 (§4.5 Synthèse)
# ═══════════════════════════════════════════════════════════════════════════
def fig5_reinforcing_cycle(L, lk):
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 12); ax.set_ylim(0, 10); ax.axis('off')

    ax.text(6, 9.6, L["f5_title"], ha='center', fontsize=14, fontweight='bold')

    # 5 boxes in circle
    angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, 6)[:-1]  # 5 positions
    radius = 3.2
    cx, cy = 6, 5
    box_w, box_h = 2.4, 1.6
    box_colors = [US_COLOR, ACCENT3, FR_COLOR, ACCENT2, ACCENT1]

    positions = []
    for i, angle in enumerate(angles):
        bx = cx + radius * np.cos(angle) - box_w/2
        by = cy + radius * np.sin(angle) - box_h/2
        positions.append((bx, by))

        rect = mpatches.FancyBboxPatch((bx, by), box_w, box_h, boxstyle="round,pad=0.12",
                                        facecolor=box_colors[i], alpha=0.1,
                                        edgecolor=box_colors[i], linewidth=2.5)
        ax.add_patch(rect)
        ax.text(bx+box_w/2, by+box_h/2, L["f5_boxes"][i], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=box_colors[i], linespacing=1.2)

    # Arrows between boxes (circular)
    for i in range(5):
        j = (i+1) % 5
        x1 = positions[i][0] + box_w/2
        y1 = positions[i][1] + box_h/2
        x2 = positions[j][0] + box_w/2
        y2 = positions[j][1] + box_h/2
        # Midpoint
        mx, my = (x1+x2)/2, (y1+y2)/2
        # Offset toward center
        dx, dy = cx - mx, cy - my
        d = np.sqrt(dx**2 + dy**2)
        mx += dx/d * 0.3
        my += dy/d * 0.3
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', lw=2, color='#666',
                                    connectionstyle=f'arc3,rad=0.3'))

    # Center box
    rect_c = mpatches.FancyBboxPatch((cx-1.5, cy-0.9), 3.0, 1.8, boxstyle="round,pad=0.15",
                                      facecolor=CN_COLOR, alpha=0.1, edgecolor=CN_COLOR, linewidth=3)
    ax.add_patch(rect_c)
    ax.text(cx, cy, L["f5_center"], ha='center', va='center', fontsize=9,
            fontweight='bold', color=CN_COLOR, linespacing=1.2)

    ax.text(6, 0.3, L["f5_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_4.5_Reinforcing_Cycle", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 4.6 — Déficit investissement EU vs US
# Page : p. 6-7 (après §4.3.2)
# ═══════════════════════════════════════════════════════════════════════════
def fig6_investment_gap(L, lk):
    fig, ax = plt.subplots(figsize=(12, 7))
    cats = L["f6_cats"]
    x = np.arange(len(cats))
    w = 0.35

    bars_us = ax.bar(x - w/2, L["f6_us"], w, color=US_COLOR, label=L["f6_us_label"],
                     edgecolor='white', linewidth=1.5)
    bars_eu = ax.bar(x + w/2, L["f6_eu"], w, color=EU_COLOR, label=L["f6_eu_label"],
                     edgecolor='white', linewidth=1.5)

    for bar, val in zip(bars_us, L["f6_us"]):
        ax.text(bar.get_x()+bar.get_width()/2, val+15, f"${val}B",
                ha='center', fontsize=10, fontweight='bold', color=US_COLOR)
    for bar, val in zip(bars_eu, L["f6_eu"]):
        ax.text(bar.get_x()+bar.get_width()/2, val+15, f"${val}B",
                ha='center', fontsize=10, fontweight='bold', color=EU_COLOR)

    # Ratio labels
    for i, (us, eu) in enumerate(zip(L["f6_us"], L["f6_eu"])):
        ratio = us / eu if eu > 0 else 99
        ax.text(i, max(us, eu) + 55, f"×{ratio:.0f}", ha='center', fontsize=11,
                fontweight='bold', color=CN_COLOR)

    ax.set_title(L["f6_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["f6_ylabel"], fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=9)
    ax.set_ylim(0, 1450)
    ax.legend(fontsize=11, framealpha=0.9)
    ax.text(0.5, -0.12, L["f6_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_4.6_Investment_Gap", L["suffix"])


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()
    print("="*70+"\n CHAPITRE IV — Génération des graphiques en 3 langues\n"+"="*70)
    all_files = []
    for lk, L in LANGS.items():
        print(f"\n{'─'*50}\n Langue : {L['suffix']}\n{'─'*50}")
        all_files.append(fig1_training_costs(L, lk))
        all_files.append(fig2_cloud_market(L, lk))
        all_files.append(fig3_productivity_gap(L, lk))
        all_files.append(fig4_value_chain(L, lk))
        all_files.append(fig5_reinforcing_cycle(L, lk))
        all_files.append(fig6_investment_gap(L, lk))
    print(f"\n{'='*70}\n Total : {len(all_files)} fichiers\n{'='*70}")
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║  GUIDE D'INSERTION — Chapitre IV                                   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Fig 4.1  Coûts training exponentiels  → p.1-2 (après §4.1.1)    ║
║           Courbe log $1K→$10B+ (2017-2030) + infra ×10            ║
║                                                                    ║
║  Fig 4.2  Cloud EU : domination US     → p.3-4 (après §4.2.1)    ║
║           Dual axis : taille marché + parts US 70% / EU 15%       ║
║                                                                    ║
║  Fig 4.3  Gap productivité IA          → p.5-6 (après §4.3.2)    ║
║           Théorique (≈ égal) vs réalisable (gap -1,5 pts)         ║
║                                                                    ║
║  Fig 4.4  Chaîne de valeur IA gen.     → p.7-8 (après §4.4.2)    ║
║           8 segments : EU absente (amont) / compétitive (aval)     ║
║                                                                    ║
║  Fig 4.5  Cercle auto-renforçant       → p.8-9 (§4.5 Synthèse)   ║
║           5 mécanismes circulaires + Section 232 au centre         ║
║                                                                    ║
║  Fig 4.6  Déficit investissement       → p.6-7 (après §4.3.2)    ║
║           4 catégories : ratios ×2,4 à ×16                        ║
║                                                                    ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    return all_files

if __name__ == "__main__":
    main()
