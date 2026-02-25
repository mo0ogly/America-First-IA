#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre VI : Conséquences France & Europe
 Générateur de graphiques en 3 langues (FR / EN / PT-BR)
=============================================================================
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
DPI = 300
US_COLOR="#1B4F72"; EU_COLOR="#D4AC0D"; CN_COLOR="#C0392B"
FR_COLOR="#2E86C1"; ACCENT1="#148F77"; ACCENT2="#884EA0"
ACCENT3="#E67E22"; ACCENT4="#2C3E50"; REST_COLOR="#95A5A6"
SC_A="#3498DB"; SC_B="#E74C3C"; SC_C="#27AE60"; SC_D="#8E44AD"
BG_COLOR="#FAFBFC"; GRID_COLOR="#E0E0E0"

LANGS = {
 "fr": {
  "suffix":"FR",
  # Fig 6.1 — Exposition sectorielle (Tableau 12)
  "f1_title":"Exposition sectorielle française\nà l'asymétrie de compute IA",
  "f1_sectors":["Finance","Auto / Aéro","Santé / Pharma","Robotique / Indus.","Défense / Spatial"],
  "f1_dims":["Intensité\ncompute","Sensibilité\ndonnées","Dépendance\ncloud US","Risque\nscénario B"],
  "f1_source":"Élaboration auteur — Tableau 12",
  # Fig 6.2 — Atouts vs Vulnérabilités France (Tableau 13)
  "f2_title":"Bilan stratégique France :\natouts vs vulnérabilités dans le contexte IA",
  "f2_atouts":["Énergie nucléaire\n65-70% mix\ncoût compétitif","Mistral AI\n€11,7 Md valoris.\nMistral Compute","Formation\nd'excellence\nENS, X, INRIA","109 Md€\nengagements\nprivés IA","1ère destination\nEU investiss.\nIA (5 ans)","AI Act :\nconformité\npar design"],
  "f2_vulner":["Pas de champion\nhardware IA\n(GPU/ASIC)","Compute : ~5%\nglobal\nratio US/FR ~30:1","Brain drain\npost-doctorat\nvers US","Permitting lent\n24+ mois\nréseau saturé","Dépendance\ncloud US\n70-80%","AI Act :\nsurcoûts\nincertitude"],
  "f2_source":"Élaboration auteur — Tableau 13",
  "f2_col_a":"ATOUTS","f2_col_v":"VULNÉRABILITÉS",
  # Fig 6.3 — Trois configurations France 2030
  "f3_title":"La France face à trois futurs à l'horizon 2030",
  "f3_configs":[
    ("Config. 1","Consommatrice\ndépendante","Scénarios A & B\nAdoption IA via cloud US\nDépendance croissante\nÉcart productivité\n+5 à +15 pts cumulés"),
    ("Config. 2","Hub énergétique\net applicatif","Scénario C\nAvantage nucléaire\nCompute local\nSouveraine en application\nÉcart contenu 1-2 pts"),
    ("Config. 3","Pilier souveraineté\neuropéenne","Scénario D\nMobilisation inédite\n20 GW nucléaire dédié\nRISC-V / DARE\nPériode vulnérable 26-28"),
  ],
  "f3_source":"Élaboration auteur — Section 6.5",
  # Fig 6.4 — Impact par type d'acteur
  "f4_title":"Impact différencié par type d'acteur français\n(scénarios A/B vs C/D)",
  "f4_actors":["Grands\ngroupes\n(CAC 40)","PME / ETI\nindustrielles","Startups IA\n(Mistral...)","Secteur\npublic\n/ Défense"],
  "f4_source":"Élaboration auteur — Section 6.2",
  # Fig 6.5 — Écosystème startup France
  "f5_title":"Écosystème startup IA français :\nacteurs clés et positionnement",
  "f5_source":"Sources : Mistral AI, Dealroom, CrunchBase (2025-2026)",
  # Fig 6.6 — Productivité sectorielle impact scénarios
  "f6_title":"Impact sur la productivité sectorielle française\nselon les scénarios (variation %/an par rapport au potentiel)",
  "f6_sectors":["Finance","Auto/Aéro","Santé","Robotique","Défense"],
  "f6_ylabel":"Productivité réalisée (% du potentiel théorique)",
  "f6_source":"Élaboration auteur — Sections 6.1, 6.2",
 },
 "en": {
  "suffix":"EN",
  "f1_title":"French Sectoral Exposure\nto AI Compute Asymmetry",
  "f1_sectors":["Finance","Auto / Aero","Health / Pharma","Robotics / Manuf.","Defense / Space"],
  "f1_dims":["Compute\nintensity","Data\nsensitivity","US cloud\ndependence","Scenario B\nrisk"],
  "f1_source":"Author's elaboration — Table 12",
  "f2_title":"France Strategic Assessment:\nStrengths vs Vulnerabilities in the AI Context",
  "f2_atouts":["Nuclear energy\n65-70% mix\ncompetitive cost","Mistral AI\n€11.7B valuation\nMistral Compute","Excellence in\neducation\nENS, X, INRIA","€109B private\nAI commitments","#1 EU destination\nfor AI foreign\ninvestment (5 yrs)","AI Act:\ncompliance\nby design"],
  "f2_vulner":["No hardware AI\nchampion\n(GPU/ASIC)","Compute: ~5%\nglobal\nUS/FR ratio ~30:1","Brain drain\npost-PhD\nto US","Slow permitting\n24+ months\ngrid saturated","US cloud\ndependence\n70-80%","AI Act:\ncompliance costs\nuncertainty"],
  "f2_source":"Author's elaboration — Table 13",
  "f2_col_a":"STRENGTHS","f2_col_v":"VULNERABILITIES",
  "f3_title":"France Facing Three Futures by 2030",
  "f3_configs":[
    ("Config. 1","Dependent\nconsumer","Scenarios A & B\nAI adoption via US cloud\nGrowing dependence\nProductivity gap\n+5 to +15 pts cumulative"),
    ("Config. 2","Energy &\napplication hub","Scenario C\nNuclear advantage\nLocal compute\nSovereign in application\nGap contained 1-2 pts"),
    ("Config. 3","European\nsovereignty pillar","Scenario D\nUnprecedented mobilization\n20 GW dedicated nuclear\nRISC-V / DARE\nVulnerable period 26-28"),
  ],
  "f3_source":"Author's elaboration — Section 6.5",
  "f4_title":"Differentiated Impact by French Actor Type\n(Scenarios A/B vs C/D)",
  "f4_actors":["Large\ncorporations\n(CAC 40)","SMEs / Mid-\nsized firms","AI Startups\n(Mistral...)","Public sector\n/ Defense"],
  "f4_source":"Author's elaboration — Section 6.2",
  "f5_title":"French AI Startup Ecosystem:\nKey Players and Positioning",
  "f5_source":"Sources: Mistral AI, Dealroom, CrunchBase (2025-2026)",
  "f6_title":"Impact on French Sectoral Productivity\nby Scenario (% of theoretical potential achieved)",
  "f6_sectors":["Finance","Auto/Aero","Health","Robotics","Defense"],
  "f6_ylabel":"Productivity achieved (% of theoretical potential)",
  "f6_source":"Author's elaboration — Sections 6.1, 6.2",
 },
 "pt": {
  "suffix":"PT-BR",
  "f1_title":"Exposição Setorial Francesa\nà Assimetria de Compute IA",
  "f1_sectors":["Finanças","Auto / Aero","Saúde / Farma","Robótica / Indúst.","Defesa / Espacial"],
  "f1_dims":["Intensidade\ncompute","Sensibilidade\ndados","Dependência\ncloud EUA","Risco\ncenário B"],
  "f1_source":"Elaboração do autor — Tabela 12",
  "f2_title":"Balanço Estratégico França:\nForças vs Vulnerabilidades no Contexto IA",
  "f2_atouts":["Energia nuclear\n65-70% mix\ncusto competitivo","Mistral AI\n€11,7 Bi valoriz.\nMistral Compute","Formação de\nexcelência\nENS, X, INRIA","€109 Bi\ncompromissos\nprivados IA","1º destino UE\ninvestim. IA\nestrangeiro (5 anos)","AI Act:\nconformidade\npor design"],
  "f2_vulner":["Sem campeão\nhardware IA\n(GPU/ASIC)","Compute: ~5%\nglobal\nrazão EUA/FR ~30:1","Brain drain\npós-doutorado\npara EUA","Permitting lento\n24+ meses\nrede saturada","Dependência\ncloud EUA\n70-80%","AI Act:\ncustos extra\nincerteza"],
  "f2_source":"Elaboração do autor — Tabela 13",
  "f2_col_a":"FORÇAS","f2_col_v":"VULNERABILIDADES",
  "f3_title":"A França Diante de Três Futuros até 2030",
  "f3_configs":[
    ("Config. 1","Consumidora\ndependente","Cenários A & B\nAdoção IA via cloud EUA\nDependência crescente\nDéficit produtividade\n+5 a +15 pts acumulados"),
    ("Config. 2","Hub energético\ne aplicativo","Cenário C\nVantagem nuclear\nCompute local\nSoberana em aplicação\nDéficit contido 1-2 pts"),
    ("Config. 3","Pilar soberania\neuropeia","Cenário D\nMobilização inédita\n20 GW nuclear dedicado\nRISC-V / DARE\nPeríodo vulnerável 26-28"),
  ],
  "f3_source":"Elaboração do autor — Seção 6.5",
  "f4_title":"Impacto Diferenciado por Tipo de Ator Francês\n(Cenários A/B vs C/D)",
  "f4_actors":["Grandes\ngrupos\n(CAC 40)","PMEs / ETIs\nindustriais","Startups IA\n(Mistral...)","Setor público\n/ Defesa"],
  "f4_source":"Elaboração do autor — Seção 6.2",
  "f5_title":"Ecossistema Startup IA Francês:\nAtores-Chave e Posicionamento",
  "f5_source":"Fontes: Mistral AI, Dealroom, CrunchBase (2025-2026)",
  "f6_title":"Impacto na Produtividade Setorial Francesa\npor Cenário (% do potencial teórico alcançado)",
  "f6_sectors":["Finanças","Auto/Aero","Saúde","Robótica","Defesa"],
  "f6_ylabel":"Produtividade alcançada (% do potencial teórico)",
  "f6_source":"Elaboração do autor — Seções 6.1, 6.2",
 }
}

def setup_style():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
        'axes.facecolor':BG_COLOR,'figure.facecolor':'white',
        'axes.grid':True,'grid.color':GRID_COLOR,'grid.alpha':0.5,
        'axes.spines.top':False,'axes.spines.right':False})

def save_fig(fig, name, sfx):
    p=os.path.join(OUTPUT_DIR,f"{name}_{sfx}.png")
    fig.savefig(p,dpi=DPI,bbox_inches='tight',facecolor='white',edgecolor='none')
    plt.close(fig); print(f"  ✓ {p}"); return p

# ═══════════════════════════════════════════════════════════════════════════
# FIG 6.1 — Exposition sectorielle (heatmap) — Tableau 12
# Page : p. 3-4 (après §6.1.4)
# ═══════════════════════════════════════════════════════════════════════════
def fig1_sectoral_exposure(L, lk):
    fig, ax = plt.subplots(figsize=(11, 7))
    # Scores 1-10 (10=highest exposure/risk)
    data = np.array([
        [7, 9, 8, 8],   # Finance
        [9, 7, 7, 9],   # Auto/Aero
        [7, 10, 5, 7],  # Santé
        [8, 5, 6, 7],   # Robotique
        [9, 10, 4, 10],  # Défense
    ])

    cmap = plt.cm.YlOrRd
    im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=1, vmax=10)

    ax.set_xticks(range(4))
    ax.set_xticklabels(L["f1_dims"], fontsize=10, fontweight='bold')
    ax.set_yticks(range(5))
    ax.set_yticklabels(L["f1_sectors"], fontsize=11, fontweight='bold')

    labels_map = {
        (1,10):["Élevée","Très élevée","Haute","Élevée","Très élevée"],
    }
    txt_labels = [
        ["Élevée","Très élevée","70-80%","Critique"],
        ["Très élevée","Élevée","60-70%","Critique"],
        ["Haute","Maximale","40-60%","Élevé"],
        ["Élevée","Modérée","50-65%","Élevé"],
        ["Très élevée","Critique","Variable","Maximal"],
    ]
    if lk == "en":
        txt_labels = [
            ["High","Very high","70-80%","Critical"],
            ["Very high","High","60-70%","Critical"],
            ["High","Maximum","40-60%","High"],
            ["High","Moderate","50-65%","High"],
            ["Very high","Critical","Variable","Maximum"],
        ]
    elif lk == "pt":
        txt_labels = [
            ["Elevada","Muito elevada","70-80%","Crítico"],
            ["Muito elevada","Elevada","60-70%","Crítico"],
            ["Alta","Máxima","40-60%","Elevado"],
            ["Elevada","Moderada","50-65%","Elevado"],
            ["Muito elevada","Crítica","Variável","Máximo"],
        ]

    for i in range(5):
        for j in range(4):
            color = 'white' if data[i,j] > 7 else 'black'
            ax.text(j, i, txt_labels[i][j], ha='center', va='center',
                    fontsize=9, fontweight='bold', color=color)

    ax.set_title(L["f1_title"], fontsize=13, fontweight='bold', pad=15)
    cbar = plt.colorbar(im, ax=ax, fraction=0.03, pad=0.04)
    cbar.set_label("Exposition →" if lk!="en" else "Exposure →", fontsize=9)
    ax.text(0.5, -0.08, L["f1_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_6.1_Sectoral_Exposure", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 6.2 — Atouts vs Vulnérabilités France (Tableau 13)
# Page : p. 7-8 (§6.4)
# ═══════════════════════════════════════════════════════════════════════════
def fig2_strengths_weaknesses(L, lk):
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14); ax.set_ylim(0, 9); ax.axis('off')
    ax.text(7, 8.6, L["f2_title"], ha='center', fontsize=14, fontweight='bold')

    # Headers
    ax.text(3.5, 7.9, L["f2_col_a"], ha='center', fontsize=13, fontweight='bold', color=ACCENT1)
    ax.text(10.5, 7.9, L["f2_col_v"], ha='center', fontsize=13, fontweight='bold', color=CN_COLOR)
    ax.plot([7, 7], [0.5, 7.7], color='#CCC', linewidth=2, linestyle='-')

    for i, (a, v) in enumerate(zip(L["f2_atouts"], L["f2_vulner"])):
        y = 6.8 - i * 1.15
        # Atout box
        rect_a = mpatches.FancyBboxPatch((0.5, y-0.4), 6, 0.95, boxstyle="round,pad=0.1",
                                          facecolor=ACCENT1, alpha=0.07, edgecolor=ACCENT1, linewidth=1.5)
        ax.add_patch(rect_a)
        ax.text(0.7, y+0.1, "✓", fontsize=14, color=ACCENT1, fontweight='bold')
        ax.text(1.3, y+0.08, a, fontsize=8, color='#333', va='center', linespacing=1.2)

        # Vulnérabilité box
        rect_v = mpatches.FancyBboxPatch((7.5, y-0.4), 6, 0.95, boxstyle="round,pad=0.1",
                                          facecolor=CN_COLOR, alpha=0.07, edgecolor=CN_COLOR, linewidth=1.5)
        ax.add_patch(rect_v)
        ax.text(7.7, y+0.1, "✗", fontsize=14, color=CN_COLOR, fontweight='bold')
        ax.text(8.3, y+0.08, v, fontsize=8, color='#333', va='center', linespacing=1.2)

    ax.text(7, 0.15, L["f2_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_6.2_Strengths_Weaknesses_FR", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 6.3 — Trois configurations France 2030
# Page : p. 8-9 (§6.5)
# ═══════════════════════════════════════════════════════════════════════════
def fig3_three_futures(L, lk):
    fig, ax = plt.subplots(figsize=(14, 7.5))
    ax.set_xlim(0, 14); ax.set_ylim(0, 7.5); ax.axis('off')
    ax.text(7, 7.2, L["f3_title"], ha='center', fontsize=14, fontweight='bold')

    colors = [SC_A, SC_C, SC_D]
    severity = [CN_COLOR, ACCENT3, ACCENT2]  # border accents
    x_positions = [0.3, 4.8, 9.3]

    for i, ((code, title, desc), col, x) in enumerate(zip(L["f3_configs"], colors, x_positions)):
        w, h = 4.2, 6.0
        rect = mpatches.FancyBboxPatch((x, 0.6), w, h, boxstyle="round,pad=0.15",
                                        facecolor=col, alpha=0.08, edgecolor=col, linewidth=3)
        ax.add_patch(rect)

        # Header
        ax.text(x+w/2, h+0.15, code, ha='center', fontsize=12, fontweight='bold', color=col,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=col, alpha=0.9))
        ax.text(x+w/2, h-0.5, title, ha='center', fontsize=11, fontweight='bold', color=col)

        # Description
        ax.text(x+w/2, 3.2, desc, ha='center', va='center', fontsize=9, color='#333', linespacing=1.4)

    # Arrow showing progression
    ax.annotate('', xy=(13.2, 0.3), xytext=(0.5, 0.3),
                arrowprops=dict(arrowstyle='->', lw=2, color='#999'))
    lbl = "Dépendance → Autonomie" if lk=="fr" else ("Dependence → Autonomy" if lk=="en" else "Dependência → Autonomia")
    ax.text(7, 0.05, lbl, ha='center', fontsize=10, fontweight='bold', color='#999', fontstyle='italic')

    return save_fig(fig, "Fig_6.3_Three_Futures_France", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 6.4 — Impact par type d'acteur
# Page : p. 4-5 (§6.2)
# ═══════════════════════════════════════════════════════════════════════════
def fig4_actor_impact(L, lk):
    fig, ax = plt.subplots(figsize=(12, 7))
    actors = L["f4_actors"]
    x = np.arange(len(actors))
    w = 0.35

    # Impact under scenarios A/B (negative = worse)
    ab_impact = [-3, -6, -4, -5]  # productivity loss pts/yr
    cd_impact = [-1, -2, -1.5, -0.5]

    lb_ab = "Scénarios A/B" if lk=="fr" else ("Scenarios A/B" if lk=="en" else "Cenários A/B")
    lb_cd = "Scénarios C/D" if lk=="fr" else ("Scenarios C/D" if lk=="en" else "Cenários C/D")

    bars_ab = ax.bar(x - w/2, ab_impact, w, color=CN_COLOR, label=lb_ab,
                     edgecolor='white', linewidth=1.5, alpha=0.8)
    bars_cd = ax.bar(x + w/2, cd_impact, w, color=ACCENT1, label=lb_cd,
                     edgecolor='white', linewidth=1.5, alpha=0.8)

    for bar, val in zip(bars_ab, ab_impact):
        ax.text(bar.get_x()+bar.get_width()/2, val-0.3, f"{val} pts",
                ha='center', fontsize=10, fontweight='bold', color=CN_COLOR)
    for bar, val in zip(bars_cd, cd_impact):
        ax.text(bar.get_x()+bar.get_width()/2, val-0.3, f"{val} pts",
                ha='center', fontsize=10, fontweight='bold', color=ACCENT1)

    ax.axhline(y=0, color='#333', linewidth=1)
    ylabel = "Écart productivité vs potentiel (pts/an)" if lk=="fr" else ("Productivity gap vs potential (pts/yr)" if lk=="en" else "Déficit produtividade vs potencial (pts/ano)")
    ax.set_title(L["f4_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(actors, fontsize=10)
    ax.set_ylim(-8, 1)
    ax.legend(fontsize=11, framealpha=0.9, loc='lower right')
    ax.text(0.5, -0.12, L["f4_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_6.4_Actor_Impact", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 6.5 — Écosystème startup IA France
# Page : p. 5-6 (§6.2.3)
# ═══════════════════════════════════════════════════════════════════════════
def fig5_startup_ecosystem(L, lk):
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13); ax.set_ylim(0, 8); ax.axis('off')
    ax.text(6.5, 7.6, L["f5_title"], ha='center', fontsize=13, fontweight='bold')

    # Mistral center
    rect_m = mpatches.FancyBboxPatch((4, 4), 5, 2.5, boxstyle="round,pad=0.15",
                                      facecolor=FR_COLOR, alpha=0.1, edgecolor=FR_COLOR, linewidth=3)
    ax.add_patch(rect_m)
    ax.text(6.5, 5.9, "MISTRAL AI", ha='center', fontsize=14, fontweight='bold', color=FR_COLOR)
    ax.text(6.5, 5.3, "€11,7 Md | 700+ emp. | LLM frontier", ha='center', fontsize=9, color='#444')
    ax.text(6.5, 4.7, "Mistral Compute: 18K GPU GB | 40 MW Essonne", ha='center', fontsize=8, color='#666')
    ax.text(6.5, 4.25, "Data center Borlänge (Suède) 1,2 Md€", ha='center', fontsize=8, color='#666')

    # Satellites
    satellites = [
        (1.2, 6.5, "Hugging Face\n$4,5 Md\nPlateforme modèles", ACCENT2),
        (10, 6.5, "Scaleway\nCloud souverain\n1er GPU Blackwell EU", ACCENT1),
        (0.8, 2.5, "Owkin\nIA Santé\nDrug discovery", ACCENT3),
        (11, 2.5, "Exotec\n€2+ Md\nRobotique logistique", US_COLOR),
        (3.5, 0.8, "LightOn\nModèles entreprise\nSouveraineté", SC_D),
        (8.5, 0.8, "H Company\nAI agents\nFoundation models", SC_C),
    ]

    for sx, sy, text, col in satellites:
        rect = mpatches.FancyBboxPatch((sx-0.8, sy-0.3), 2.2, 1.2, boxstyle="round,pad=0.1",
                                        facecolor=col, alpha=0.08, edgecolor=col, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(sx+0.3, sy+0.3, text, ha='center', va='center', fontsize=7.5,
                color=col, fontweight='bold', linespacing=1.2)
        # Line to Mistral
        ax.plot([sx+0.3, 6.5], [sy+0.3, 5.0 if sy > 4 else 4.3],
                color=col, linewidth=1, linestyle='--', alpha=0.3)

    # Key metrics
    metrics_y = 3.2
    metrics = [("€2,8 Md", "levés Mistral\n(total)"), ("109 Md€", "engagements\nprivés IA FR"),
               ("12", "licornes IA EU\nS1 2025"), ("+55%", "financement IA\nEU T1 2025")]
    for i, (val, desc) in enumerate(metrics):
        mx = 1.5 + i * 3.2
        ax.text(mx, metrics_y, val, ha='center', fontsize=12, fontweight='bold', color=FR_COLOR)
        ax.text(mx, metrics_y - 0.5, desc, ha='center', fontsize=7.5, color='#666', linespacing=1.1)

    ax.text(6.5, 0.1, L["f5_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_6.5_Startup_Ecosystem_FR", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 6.6 — Productivité sectorielle par scénario
# Page : p. 3 (après §6.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig6_sectoral_productivity(L, lk):
    fig, ax = plt.subplots(figsize=(13, 7))
    sectors = L["f6_sectors"]
    x = np.arange(len(sectors))
    w = 0.2

    # % of theoretical potential achieved per scenario
    sc_a = [65, 55, 60, 50, 40]
    sc_b = [35, 25, 30, 25, 20]
    sc_c = [80, 75, 75, 70, 70]
    sc_d = [60, 55, 55, 60, 75]

    sc_names = ["A" if lk!="pt" else "A", "B", "C", "D"]
    sc_colors = [SC_A, SC_B, SC_C, SC_D]

    for i, (data, col, name) in enumerate(zip([sc_a, sc_b, sc_c, sc_d], sc_colors, sc_names)):
        offset = (i - 1.5) * w
        bars = ax.bar(x + offset, data, w, color=col, label=f"Scén. {name}" if lk=="fr" else f"Sc. {name}",
                      edgecolor='white', linewidth=1, alpha=0.85)
        for bar, val in zip(bars, data):
            ax.text(bar.get_x()+bar.get_width()/2, val+1.5, f"{val}%",
                    ha='center', fontsize=7.5, fontweight='bold', color=col)

    ax.axhline(y=100, color='#CCC', linewidth=1, linestyle=':', alpha=0.7)
    pot_lbl = "100% = potentiel théorique" if lk=="fr" else ("100% = theoretical potential" if lk=="en" else "100% = potencial teórico")
    ax.text(4.5, 102, pot_lbl, fontsize=8, color='#999')

    ax.set_title(L["f6_title"], fontsize=12, fontweight='bold', pad=15)
    ax.set_ylabel(L["f6_ylabel"], fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(sectors, fontsize=10, fontweight='bold')
    ax.set_ylim(0, 115)
    ax.legend(fontsize=10, framealpha=0.9, ncol=4, loc='upper center')
    ax.text(0.5, -0.1, L["f6_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_6.6_Sectoral_Productivity", L["suffix"])


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()
    print("="*70+"\n CHAPITRE VI — Génération des graphiques en 3 langues\n"+"="*70)
    all_files = []
    for lk, L in LANGS.items():
        print(f"\n{'─'*50}\n Langue : {L['suffix']}\n{'─'*50}")
        all_files.append(fig1_sectoral_exposure(L, lk))
        all_files.append(fig2_strengths_weaknesses(L, lk))
        all_files.append(fig3_three_futures(L, lk))
        all_files.append(fig4_actor_impact(L, lk))
        all_files.append(fig5_startup_ecosystem(L, lk))
        all_files.append(fig6_sectoral_productivity(L, lk))
    print(f"\n{'='*70}\n Total : {len(all_files)} fichiers\n{'='*70}")
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║  GUIDE D'INSERTION — Chapitre VI                                   ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Fig 6.1  Exposition sectorielle       → p.3-4 (après §6.1.4)    ║
║           Heatmap 5 secteurs × 4 dimensions  [= Tableau 12]       ║
║                                                                    ║
║  Fig 6.6  Productivité sectorielle     → p.3 (après §6.1)        ║
║           % potentiel atteint par scénario, 5 secteurs             ║
║                                                                    ║
║  Fig 6.4  Impact par type d'acteur     → p.4-5 (§6.2)            ║
║           Barres négatives : écart productivité A/B vs C/D         ║
║                                                                    ║
║  Fig 6.5  Écosystème startup France    → p.5-6 (§6.2.3)          ║
║           Mistral AI + satellites + métriques clés                  ║
║                                                                    ║
║  Fig 6.2  Atouts vs Vulnérabilités     → p.7-8 (§6.4 Tab.13)    ║
║           6 paires : forces / faiblesses France                    ║
║                                                                    ║
║  Fig 6.3  Trois futures France 2030    → p.8-9 (§6.5)            ║
║           3 configurations : dépendante → hub → pilier souv.      ║
║                                                                    ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    return all_files

if __name__ == "__main__":
    main()
