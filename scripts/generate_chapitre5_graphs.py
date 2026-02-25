#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Chapitre V : Scénarios Prospectifs 2026-2030
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
ACCENT1="#148F77"; ACCENT2="#884EA0"; ACCENT3="#E67E22"; ACCENT4="#2C3E50"
SC_A="#3498DB"; SC_B="#E74C3C"; SC_C="#27AE60"; SC_D="#8E44AD"
BG_COLOR="#FAFBFC"; GRID_COLOR="#E0E0E0"

LANGS = {
 "fr": {
  "suffix":"FR",
  # Fig 5.1 — Trajectoire CACI 4 scénarios (G5)
  "f1_title":"Trajectoires du ratio CACI(US)/CACI(EU)\n2025–2030 par scénario",
  "f1_ylabel":"Ratio CACI(US) / CACI(EU)",
  "f1_sc":["A — Statu quo renforcé","B — Fracture numérique","C — Partenariat asymétrique","D — Souveraineté contestée"],
  "f1_source":"Élaboration auteur — Section 5.7.1, calibration CACI",
  "f1_danger":"Zone de décrochage\nirréversible",
  # Fig 5.2 — Points de bascule chronologie (G6)
  "f2_title":"Chronologie des points de bascule 2026–2030\net fenêtres décisionnelles",
  "f2_events":[
    ("Avr.\n2026","Rapport Phase 1\nNégociations US-UE","Modéré\nvs Agressif"),
    ("Juil.\n2026","Rapport Commerce\nSur semi data centers","Extension\ntarifs ?"),
    ("2027","Premières Gigafactories\nopérationnelles ?","Proactif\nvs Réactif"),
    ("2028","POINT CRITIQUE\nDemande > Capacité EU","Moment de\nvérité"),
    ("2029-30","Premiers SMR nucléaires\nRISC-V maturité ?","Autonomie\nà long terme"),
  ],
  "f2_source":"Élaboration auteur — Section 5.7.2-5.7.3",
  "f2_window":"Fenêtre décisionnelle critique",
  # Fig 5.3 — Heatmap 6 métriques × 4 scénarios
  "f3_title":"Synthèse : 6 métriques × 4 scénarios (2030)",
  "f3_metrics":["M1 Compute\nratio","M2 Coût\nFLOP","M3 Cloud\nUS (%)","M4 Product.\nEU (%/an)","M5 Énergie\nEU (TWh)","M6 CACI\nratio"],
  "f3_scenarios":["A\nStatu quo","B\nFracture","C\nPartenariat","D\nSouveraineté"],
  "f3_source":"Élaboration auteur — Tableau 11",
  # Fig 5.4 — Éléments prédéterminés
  "f4_title":"Les 4 éléments prédéterminés (EP)\nstructurant tous les scénarios",
  "f4_items":[("EP1","Croissance exponentielle\ndemande compute IA","Ventes semis ×2 en 2 ans\nPuces IA doublent / 7 mois"),
              ("EP2","Concentration persistante\ncompute aux USA","Ratio 15:1 US/EU\nDélais data centers 18-36 mois"),
              ("EP3","Tension énergétique\ncroissante","415→945 TWh (2024→2030)\nCoûts EU 2-3× plus élevés"),
              ("EP4","Section 232\nen place","Base légale confirmée\nRapport Commerce juil. 2026")],
  "f4_source":"Élaboration auteur — Section 5.1",
  # Fig 5.5 — M1 Compute ratio par scénario (barres)
  "f5_title":"Ratio compute installé US/EU (M1)\nProjection 2030 par scénario",
  "f5_ylabel":"Ratio US / EU",
  "f5_baseline":"2025\n(actuel)",
  "f5_source":"Élaboration auteur — Sections 5.3-5.6",
  # Fig 5.6 — Matrice 2×2 actualisée avec probabilités
  "f6_title":"Matrice 2×2 actualisée : scénarios, probabilités\net CACI 2030",
  "f6_prob":["40-50%","15-20%","15-20%","15-20%"],
  "f6_caci":["10-15:1","20-35:1","4-7:1","8-12:1"],
  "f6_xlabels":["EU RÉACTIVE","EU PROACTIVE"],
  "f6_ylabels":["US MODÉRÉ","US AGRESSIF"],
  "f6_scenarios":["A — Statu quo\nrenforcé","B — Fracture\nnumérique","C — Partenariat\nasymétrique","D — Souveraineté\ncontestée"],
  "f6_source":"Élaboration auteur — Section 5.7",
 },
 "en": {
  "suffix":"EN",
  "f1_title":"CACI(US)/CACI(EU) Ratio Trajectories\n2025–2030 by Scenario",
  "f1_ylabel":"CACI(US) / CACI(EU) Ratio",
  "f1_sc":["A — Reinforced Status Quo","B — Digital Fracture","C — Asymmetric Partnership","D — Contested Sovereignty"],
  "f1_source":"Author's elaboration — Section 5.7.1, CACI calibration",
  "f1_danger":"Irreversible\ndecoupling zone",
  "f2_title":"Tipping Points Timeline 2026–2030\nand Decision Windows",
  "f2_events":[
    ("Apr.\n2026","Phase 1 Report\nUS-EU Negotiations","Moderate\nvs Aggressive"),
    ("Jul.\n2026","Commerce Report\nOn DC semiconductors","Tariff\nextension?"),
    ("2027","First Gigafactories\noperational?","Proactive\nvs Reactive"),
    ("2028","CRITICAL POINT\nDemand > EU Capacity","Moment of\ntruth"),
    ("2029-30","First nuclear SMRs\nRISC-V maturity?","Long-term\nautonomy"),
  ],
  "f2_source":"Author's elaboration — Section 5.7.2-5.7.3",
  "f2_window":"Critical decision window",
  "f3_title":"Summary: 6 Metrics × 4 Scenarios (2030)",
  "f3_metrics":["M1 Compute\nratio","M2 FLOP\ncost","M3 US Cloud\n(%)","M4 EU Prod.\n(%/yr)","M5 EU Energy\n(TWh)","M6 CACI\nratio"],
  "f3_scenarios":["A\nStatus Quo","B\nFracture","C\nPartnership","D\nSovereignty"],
  "f3_source":"Author's elaboration — Table 11",
  "f4_title":"The 4 Predetermined Elements (PE)\nStructuring All Scenarios",
  "f4_items":[("PE1","Exponential growth\nAI compute demand","Semi sales ×2 in 2 yrs\nAI chips double / 7 months"),
              ("PE2","Persistent US\ncompute concentration","15:1 US/EU ratio\nDC build delays 18-36 months"),
              ("PE3","Growing energy\ntension","415→945 TWh (2024→2030)\nEU costs 2-3× higher"),
              ("PE4","Section 232\nin place","Legal basis confirmed\nCommerce report Jul. 2026")],
  "f4_source":"Author's elaboration — Section 5.1",
  "f5_title":"Installed Compute Ratio US/EU (M1)\n2030 Projection by Scenario",
  "f5_ylabel":"US / EU Ratio",
  "f5_baseline":"2025\n(current)",
  "f5_source":"Author's elaboration — Sections 5.3-5.6",
  "f6_title":"Updated 2×2 Matrix: Scenarios, Probabilities\nand CACI 2030",
  "f6_prob":["40-50%","15-20%","15-20%","15-20%"],
  "f6_caci":["10-15:1","20-35:1","4-7:1","8-12:1"],
  "f6_xlabels":["EU REACTIVE","EU PROACTIVE"],
  "f6_ylabels":["US MODERATE","US AGGRESSIVE"],
  "f6_scenarios":["A — Reinforced\nStatus Quo","B — Digital\nFracture","C — Asymmetric\nPartnership","D — Contested\nSovereignty"],
  "f6_source":"Author's elaboration — Section 5.7",
 },
 "pt": {
  "suffix":"PT-BR",
  "f1_title":"Trajetórias do Ratio CACI(EUA)/CACI(UE)\n2025–2030 por Cenário",
  "f1_ylabel":"Razão CACI(EUA) / CACI(UE)",
  "f1_sc":["A — Status Quo Reforçado","B — Fratura Digital","C — Parceria Assimétrica","D — Soberania Contestada"],
  "f1_source":"Elaboração do autor — Seção 5.7.1, calibração CACI",
  "f1_danger":"Zona de desacoplamento\nirreversível",
  "f2_title":"Cronologia dos Pontos de Inflexão 2026–2030\ne Janelas Decisórias",
  "f2_events":[
    ("Abr.\n2026","Relatório Fase 1\nNegociações EUA-UE","Moderado\nvs Agressivo"),
    ("Jul.\n2026","Relatório Comércio\nSobre semi DCs","Extensão\ntarifas?"),
    ("2027","Primeiras Gigafábricas\noperacionais?","Proativo\nvs Reativo"),
    ("2028","PONTO CRÍTICO\nDemanda > Capacidade UE","Momento da\nverdade"),
    ("2029-30","Primeiros SMRs nucleares\nRISC-V maturidade?","Autonomia\nlongo prazo"),
  ],
  "f2_source":"Elaboração do autor — Seção 5.7.2-5.7.3",
  "f2_window":"Janela decisória crítica",
  "f3_title":"Síntese: 6 Métricas × 4 Cenários (2030)",
  "f3_metrics":["M1 Razão\ncompute","M2 Custo\nFLOP","M3 Cloud\nEUA (%)","M4 Prod.\nUE (%/ano)","M5 Energia\nUE (TWh)","M6 Razão\nCACI"],
  "f3_scenarios":["A\nStatus Quo","B\nFratura","C\nParceria","D\nSoberania"],
  "f3_source":"Elaboração do autor — Tabela 11",
  "f4_title":"Os 4 Elementos Predeterminados (EP)\nEstruturando Todos os Cenários",
  "f4_items":[("EP1","Crescimento exponencial\ndemanda compute IA","Vendas semi ×2 em 2 anos\nChips IA dobram / 7 meses"),
              ("EP2","Concentração persistente\ncompute nos EUA","Razão 15:1 EUA/UE\nPrazos DCs 18-36 meses"),
              ("EP3","Tensão energética\ncrescente","415→945 TWh (2024→2030)\nCustos UE 2-3× mais altos"),
              ("EP4","Seção 232\nem vigor","Base legal confirmada\nRelatório Comércio jul. 2026")],
  "f4_source":"Elaboração do autor — Seção 5.1",
  "f5_title":"Razão Compute Instalado EUA/UE (M1)\nProjeção 2030 por Cenário",
  "f5_ylabel":"Razão EUA / UE",
  "f5_baseline":"2025\n(atual)",
  "f5_source":"Elaboração do autor — Seções 5.3-5.6",
  "f6_title":"Matriz 2×2 Atualizada: Cenários, Probabilidades\ne CACI 2030",
  "f6_prob":["40-50%","15-20%","15-20%","15-20%"],
  "f6_caci":["10-15:1","20-35:1","4-7:1","8-12:1"],
  "f6_xlabels":["UE REATIVA","UE PROATIVA"],
  "f6_ylabels":["EUA MODERADO","EUA AGRESSIVO"],
  "f6_scenarios":["A — Status Quo\nReforçado","B — Fratura\nDigital","C — Parceria\nAssimétrica","D — Soberania\nContestada"],
  "f6_source":"Elaboração do autor — Seção 5.7",
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
# FIG 5.1 — Trajectoires CACI (G5 du texte)
# Page : p. 8-9 (§5.7.1 après Tableau 11)
# ═══════════════════════════════════════════════════════════════════════════
def fig1_caci_trajectories(L, lk):
    fig, ax = plt.subplots(figsize=(13, 7.5))
    years = [2025, 2026, 2027, 2028, 2029, 2030]
    # Midpoints from text
    sc_a = [9.5, 10.5, 11.5, 12, 12.5, 12.5]
    sc_b = [9.5, 12, 18, 25, 28, 27.5]
    sc_c = [9.5, 9, 8, 7, 6, 5.5]
    sc_d = [9.5, 11, 15, 17.5, 12, 10]

    colors = [SC_A, SC_B, SC_C, SC_D]
    datas = [sc_a, sc_b, sc_c, sc_d]
    markers = ['o','s','D','^']

    for data, col, mk, label in zip(datas, colors, markers, L["f1_sc"]):
        ax.plot(years, data, color=col, linewidth=3, marker=mk, markersize=8, label=label, zorder=5)

    # Danger zone
    ax.axhspan(20, 40, alpha=0.06, color=CN_COLOR)
    ax.text(2025.3, 32, L["f1_danger"], fontsize=10, fontweight='bold', color=CN_COLOR, fontstyle='italic')

    # Reference line
    ax.axhline(y=9.5, color='gray', linewidth=1, linestyle=':', alpha=0.5)
    ax.text(2025.1, 8, "2025", fontsize=9, color='gray')

    # 2028 vertical
    ax.axvline(x=2028, color=ACCENT4, linewidth=1.5, linestyle='--', alpha=0.4)
    ax.text(2028.1, 2, "2028", fontsize=9, fontweight='bold', color=ACCENT4, rotation=90)

    ax.set_title(L["f1_title"], fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel(L["f1_ylabel"], fontsize=12)
    ax.set_xlim(2024.8, 2030.2)
    ax.set_ylim(0, 36)
    ax.set_xticks(years)
    ax.legend(fontsize=10, loc='upper left', framealpha=0.95)
    ax.text(0.5, -0.1, L["f1_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_5.1_CACI_Trajectories", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 5.2 — Points de bascule (G6 du texte)
# Page : p. 10-11 (§5.7.2-5.7.3)
# ═══════════════════════════════════════════════════════════════════════════
def fig2_tipping_points(L, lk):
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_xlim(0, 15); ax.set_ylim(0, 7); ax.axis('off')
    ax.text(7.5, 6.7, L["f2_title"], ha='center', fontsize=13, fontweight='bold')

    y_line = 3.5
    ax.plot([0.8, 14.2], [y_line, y_line], color='#333', linewidth=3, zorder=1)

    event_x = [1.8, 4.2, 6.8, 9.5, 12.5]
    event_colors = [ACCENT3, CN_COLOR, SC_C, SC_B, ACCENT2]

    for i, (ex, (date, desc, impact), col) in enumerate(zip(event_x, L["f2_events"], event_colors)):
        y_off = 1.8 if i % 2 == 0 else -1.7
        y_text = y_line + y_off

        # Dot
        size = 16 if i == 3 else 12  # 2028 bigger
        ax.plot(ex, y_line, 'o', color=col, markersize=size, zorder=5)
        ax.plot(ex, y_line, 'o', color='white', markersize=size-5, zorder=6)

        # Connector
        ax.plot([ex, ex], [y_line, y_text + (0.3 if y_off > 0 else -0.3)],
                color=col, linewidth=1.5, linestyle='--', zorder=2)

        # Box
        bw, bh = 2.2, 1.5
        by = y_text - 0.3 if y_off > 0 else y_text - 0.5
        rect = mpatches.FancyBboxPatch((ex-bw/2, by), bw, bh, boxstyle="round,pad=0.1",
                                        facecolor=col, alpha=0.08, edgecolor=col, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(ex, by+bh-0.25, date, ha='center', fontsize=8, fontweight='bold', color=col)
        ax.text(ex, by+bh/2-0.15, desc, ha='center', va='center', fontsize=7, color='#333', linespacing=1.2)

        # Impact label (below/above)
        imp_y = by - 0.35 if y_off > 0 else by + bh + 0.25
        ax.text(ex, imp_y, impact, ha='center', fontsize=7, color=col, fontstyle='italic',
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor=col, alpha=0.7))

    # Critical window
    ax.annotate('', xy=(10.8, 1.0), xytext=(1.2, 1.0),
                arrowprops=dict(arrowstyle='<->', color=CN_COLOR, lw=2.5))
    ax.text(6, 0.5, L["f2_window"], ha='center', fontsize=10, fontweight='bold', color=CN_COLOR)

    ax.text(7.5, 0.05, L["f2_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_5.2_Tipping_Points", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 5.3 — Heatmap 6 métriques × 4 scénarios
# Page : p. 8 (§5.7.1, accompagne Tableau 11)
# ═══════════════════════════════════════════════════════════════════════════
def fig3_metrics_heatmap(L, lk):
    fig, ax = plt.subplots(figsize=(11, 8))
    # Severity score (0=good for EU, 10=bad for EU)
    data = np.array([
        [6, 9, 4, 5],    # M1 compute ratio
        [5, 8, 3, 5],    # M2 cost FLOP
        [6, 9, 4, 3],    # M3 cloud US
        [5, 9, 2, 4],    # M4 productivity
        [5, 3, 6, 8],    # M5 energy (high=more demand=more compute=good)
        [6, 10, 2, 5],   # M6 CACI
    ])
    # Values to display
    vals = [
        ["18-20:1","25-30:1","8-10:1","8-12:1"],
        ["2.4-3.2×","4-6×","1.5-2.0×","1.8-2.5×"],
        ["72-75%","78-82%","60-65%","50-55%"],
        ["+1.0-1.5%","+0.3-0.8%","+1.8-2.5%","+1.2-2.0%"],
        ["~115","~95","~140","~155"],
        ["10-15:1","20-35:1","4-7:1","8-12:1"],
    ]

    cmap = plt.cm.RdYlGn_r
    im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0, vmax=10)

    ax.set_xticks(range(4))
    ax.set_xticklabels(L["f3_scenarios"], fontsize=10, fontweight='bold')
    ax.set_yticks(range(6))
    ax.set_yticklabels(L["f3_metrics"], fontsize=10)

    for i in range(6):
        for j in range(4):
            color = 'white' if data[i,j] > 6 else 'black'
            ax.text(j, i, vals[i][j], ha='center', va='center', fontsize=10,
                    fontweight='bold', color=color)

    ax.set_title(L["f3_title"], fontsize=14, fontweight='bold', pad=15)
    cbar = plt.colorbar(im, ax=ax, fraction=0.03, pad=0.04)
    cbar.set_label("← EU favorable    EU défavorable →" if lk=="fr" else
                   ("← EU favorable    EU unfavorable →" if lk=="en" else
                    "← UE favorável    UE desfavorável →"), fontsize=9)

    ax.text(0.5, -0.08, L["f3_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_5.3_Metrics_Heatmap", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 5.4 — Éléments prédéterminés
# Page : p. 1-2 (§5.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig4_predetermined(L, lk):
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13); ax.set_ylim(0, 7); ax.axis('off')
    ax.text(6.5, 6.6, L["f4_title"], ha='center', fontsize=14, fontweight='bold')

    ep_colors = [US_COLOR, ACCENT3, CN_COLOR, ACCENT2]
    for i, ((code, title, detail), col) in enumerate(zip(L["f4_items"], ep_colors)):
        x = 0.5 + (i % 2) * 6.3
        y = 4.2 if i < 2 else 0.8
        w, h = 5.8, 2.8

        rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                                        facecolor=col, alpha=0.07, edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x+0.4, y+h-0.4, code, fontsize=14, fontweight='bold', color=col)
        ax.text(x+w/2, y+h-0.9, title, ha='center', fontsize=10, fontweight='bold', color=col)
        ax.text(x+w/2, y+0.8, detail, ha='center', va='center', fontsize=9, color='#444', linespacing=1.3)

    ax.text(6.5, 0.15, L["f4_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_5.4_Predetermined_Elements", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 5.5 — M1 Compute ratio par scénario (barres)
# Page : p. 7-8 (§5.7.1)
# ═══════════════════════════════════════════════════════════════════════════
def fig5_compute_ratio_bars(L, lk):
    fig, ax = plt.subplots(figsize=(11, 7))
    cats = [L["f5_baseline"]] + [s.split("—")[0].strip() + "\n2030" for s in L["f1_sc"]]
    vals = [15, 19, 27.5, 9, 11]
    err_lo = [0, 1, 2.5, 1, 2]
    err_hi = [0, 1, 2.5, 1, 3]
    colors = ['#888', SC_A, SC_B, SC_C, SC_D]

    bars = ax.bar(cats, vals, width=0.55, color=colors, alpha=0.85,
                  edgecolor='white', linewidth=2,
                  yerr=[err_lo, err_hi], capsize=6,
                  error_kw={'elinewidth':2, 'capthick':2, 'color':'#666'})

    for bar, val in zip(bars, vals):
        ax.text(bar.get_x()+bar.get_width()/2, val+1.5, f"×{val:.0f}",
                ha='center', fontsize=13, fontweight='bold', color=bar.get_facecolor())

    ax.axhline(y=15, color='gray', linewidth=1, linestyle=':', alpha=0.5)
    ax.text(4.6, 15.5, "2025 baseline", fontsize=8, color='gray')

    ax.set_title(L["f5_title"], fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel(L["f5_ylabel"], fontsize=12)
    ax.set_ylim(0, 35)
    ax.text(0.5, -0.1, L["f5_source"], transform=ax.transAxes, fontsize=8,
            color='gray', ha='center', fontstyle='italic')
    return save_fig(fig, "Fig_5.5_Compute_Ratio_Scenarios", L["suffix"])

# ═══════════════════════════════════════════════════════════════════════════
# FIG 5.6 — Matrice 2×2 actualisée
# Page : p. 2-3 (§5.2.3)
# ═══════════════════════════════════════════════════════════════════════════
def fig6_updated_matrix(L, lk):
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_xlim(0, 12); ax.set_ylim(0, 9); ax.axis('off')
    ax.text(6, 8.6, L["f6_title"], ha='center', fontsize=14, fontweight='bold')

    sc_colors = [SC_A, SC_C, SC_B, SC_D]
    positions = [(1.0, 4.6), (6.2, 4.6), (1.0, 0.8), (6.2, 0.8)]
    qw, qh = 4.8, 3.4

    for i, ((x, y), col) in enumerate(zip(positions, sc_colors)):
        rect = mpatches.FancyBboxPatch((x, y), qw, qh, boxstyle="round,pad=0.15",
                                        facecolor=col, alpha=0.08, edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x+qw/2, y+qh-0.5, L["f6_scenarios"][i], ha='center', fontsize=11,
                fontweight='bold', color=col)
        # Probability
        ax.text(x+qw/2, y+qh/2, f"P = {L['f6_prob'][i]}", ha='center', fontsize=14,
                fontweight='bold', color=col,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=col, alpha=0.8))
        # CACI
        ax.text(x+qw/2, y+0.6, f"CACI: {L['f6_caci'][i]}", ha='center', fontsize=11,
                fontweight='bold', color='#555')

    # Axes
    ax.annotate('', xy=(11.5, 4.45), xytext=(0.5, 4.45),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='#999'))
    ax.text(1.2, 4.15, L["f6_xlabels"][0], fontsize=9, color='#999', fontstyle='italic')
    ax.text(10, 4.15, L["f6_xlabels"][1], fontsize=9, color='#999', fontstyle='italic', ha='right')

    ax.annotate('', xy=(0.7, 8.3), xytext=(0.7, 0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='#999'))
    ax.text(0.15, 6.3, L["f6_ylabels"][0], fontsize=8, color='#999', rotation=90, va='center')
    ax.text(0.15, 2.3, L["f6_ylabels"][1], fontsize=8, color='#999', rotation=90, va='center')

    ax.text(6, 0.15, L["f6_source"], ha='center', fontsize=8, color='gray', fontstyle='italic')
    return save_fig(fig, "Fig_5.6_Updated_Matrix", L["suffix"])


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_style()
    print("="*70+"\n CHAPITRE V — Génération des graphiques en 3 langues\n"+"="*70)
    all_files = []
    for lk, L in LANGS.items():
        print(f"\n{'─'*50}\n Langue : {L['suffix']}\n{'─'*50}")
        all_files.append(fig1_caci_trajectories(L, lk))
        all_files.append(fig2_tipping_points(L, lk))
        all_files.append(fig3_metrics_heatmap(L, lk))
        all_files.append(fig4_predetermined(L, lk))
        all_files.append(fig5_compute_ratio_bars(L, lk))
        all_files.append(fig6_updated_matrix(L, lk))
    print(f"\n{'='*70}\n Total : {len(all_files)} fichiers\n{'='*70}")
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║  GUIDE D'INSERTION — Chapitre V                                    ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  Fig 5.4  Éléments prédéterminés       → p.1-2 (§5.1)            ║
║           4 EP structurant tous les scénarios                      ║
║                                                                    ║
║  Fig 5.6  Matrice 2×2 actualisée       → p.2-3 (§5.2.3)          ║
║           4 scénarios + probabilités + CACI 2030                   ║
║                                                                    ║
║  Fig 5.5  Ratio compute M1 par scén.   → p.7-8 (§5.7.1)          ║
║           Barres 2025 baseline vs 4 scénarios 2030                 ║
║                                                                    ║
║  Fig 5.3  Heatmap 6 métriques × 4 sc.  → p.8 (§5.7.1 Tab.11)    ║
║           Couleurs sévérité + valeurs par cellule                  ║
║                                                                    ║
║  Fig 5.1  Trajectoires CACI            → p.8-9 (§5.7.1) [=G5]   ║
║           4 courbes 2025→2030, zone danger                         ║
║                                                                    ║
║  Fig 5.2  Points de bascule            → p.10-11 (§5.7.2) [=G6] ║
║           Frise chronologique 5 events + fenêtre critique          ║
║                                                                    ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    return all_files

if __name__ == "__main__":
    main()
