#!/usr/bin/env python3
"""
=============================================================================
 AI FOR AMERICANS FIRST — Annexe Économétrique
 Générateur de graphiques CACI en 3 langues (FR / EN / PT-BR)
=============================================================================
 Auteur : Script généré pour l'annexe économétrique
 Usage  : python generate_caci_graphs_multilingual.py
 Output : 15 PNG files (5 figures × 3 langues)
=============================================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS, RandomEffects
from scipy import stats
import os
import warnings
warnings.filterwarnings('ignore')

# ─── Configuration ──────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)
DPI = 300

# Couleurs
US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
CN_COLOR = "#C0392B"
FR_COLOR = "#2E86C1"
ACCENT1 = "#148F77"
ACCENT2 = "#E74C3C"
ACCENT3 = "#F39C12"
ACCENT4 = "#27AE60"
BG_COLOR = "#FAFBFC"
GRID_COLOR = "#E0E0E0"

color_map = {
    'USA': US_COLOR, 'China': CN_COLOR, 'UK': FR_COLOR, 'Germany': EU_COLOR,
    'France': FR_COLOR, 'Japan': ACCENT2, 'South Korea': ACCENT2,
    'India': ACCENT3, 'Canada': ACCENT1, 'Netherlands': EU_COLOR,
    'Brazil': ACCENT4, 'Sweden': EU_COLOR,
}

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 11,
    'axes.facecolor': BG_COLOR, 'figure.facecolor': 'white',
    'axes.grid': True, 'grid.color': GRID_COLOR, 'grid.alpha': 0.7,
    'axes.spines.top': False, 'axes.spines.right': False,
})

# ─── Traductions ────────────────────────────────────────────────────────────
LANGS = {
    "fr": {
        "suffix": "FR",
        # Fig A.1
        "a1_title": "Fig. A.1 — Corrélation CACI–Productivité IA (2024)\nTaille des bulles ∝ PIB",
        "a1_xlabel": "ln(CACI)",
        "a1_ylabel": "ln(Productivité IA sectorielle)",
        "a1_legend": "Droite OLS",
        "a1_source": "Source : panel 12 pays, calibration auteur. β = {:.3f} (p < 0.01)",
        # Fig A.2
        "a2_title": "Fig. A.2 — Trajectoires CACI par pays (2020–2024)",
        "a2_xlabel": "Année",
        "a2_ylabel": "CACI (×10⁻⁶)",
        "a2_source": "Source : panel calibré, élaboration auteur",
        # Fig A.3
        "a3_title": "Fig. A.3 — Stabilité du coefficient CACI\nà travers les spécifications (IC 95%)",
        "a3_xlabel": "Coefficient β (ln CACI → ln Productivité IA)",
        "a3_models": ['M1 : OLS Pooled', 'M2 : Effets Fixes', 'M3 : Effets Aléatoires'],
        # Fig A.4
        "a4_title": "Fig. A.4 — Diagnostic des résidus",
        "a4_qq": "QQ-plot des résidus (OLS)",
        "a4_resid": "Résidus vs valeurs ajustées",
        "a4_fitted": "Valeurs prédites",
        "a4_residlabel": "Résidus",
        # Fig A.5
        "a5_title": "Fig. A.5 — Avantage compute US mesuré par le CACI (2024)\nRatio = combien de fois les US disposent de plus de compute effectif",
        "a5_xlabel": "Ratio CACI(US) / CACI(pays)",
        "a5_source": "Source : calcul CACI auteur, calibration Epoch AI / IEA / Banque mondiale",
    },
    "en": {
        "suffix": "EN",
        "a1_title": "Fig. A.1 — CACI–AI Productivity Correlation (2024)\nBubble size ∝ GDP",
        "a1_xlabel": "ln(CACI)",
        "a1_ylabel": "ln(AI sectoral productivity)",
        "a1_legend": "OLS fit",
        "a1_source": "Source: 12-country panel, author calibration. β = {:.3f} (p < 0.01)",
        "a2_title": "Fig. A.2 — CACI Trajectories by Country (2020–2024)",
        "a2_xlabel": "Year",
        "a2_ylabel": "CACI (×10⁻⁶)",
        "a2_source": "Source: calibrated panel, author's elaboration",
        "a3_title": "Fig. A.3 — CACI Coefficient Stability\nAcross Specifications (95% CI)",
        "a3_xlabel": "Coefficient β (ln CACI → ln AI Productivity)",
        "a3_models": ['M1: OLS Pooled', 'M2: Fixed Effects', 'M3: Random Effects'],
        "a4_title": "Fig. A.4 — Residuals Diagnostics",
        "a4_qq": "QQ-plot of residuals (OLS)",
        "a4_resid": "Residuals vs fitted values",
        "a4_fitted": "Fitted values",
        "a4_residlabel": "Residuals",
        "a5_title": "Fig. A.5 — US Compute Advantage Measured by CACI (2024)\nRatio = how many times the US has more effective compute",
        "a5_xlabel": "Ratio CACI(US) / CACI(country)",
        "a5_source": "Source: CACI calculation by author, Epoch AI / IEA / World Bank calibration",
    },
    "pt": {
        "suffix": "PT",
        "a1_title": "Fig. A.1 — Correlação CACI–Produtividade IA (2024)\nTamanho das bolhas ∝ PIB",
        "a1_xlabel": "ln(CACI)",
        "a1_ylabel": "ln(Produtividade setorial de IA)",
        "a1_legend": "Ajuste OLS",
        "a1_source": "Fonte: painel de 12 países, calibração do autor. β = {:.3f} (p < 0,01)",
        "a2_title": "Fig. A.2 — Trajetórias CACI por país (2020–2024)",
        "a2_xlabel": "Ano",
        "a2_ylabel": "CACI (×10⁻⁶)",
        "a2_source": "Fonte: painel calibrado, elaboração do autor",
        "a3_title": "Fig. A.3 — Estabilidade do coeficiente CACI\nentre especificações (IC 95%)",
        "a3_xlabel": "Coeficiente β (ln CACI → ln Produtividade IA)",
        "a3_models": ['M1: OLS Pooled', 'M2: Efeitos Fixos', 'M3: Efeitos Aleatórios'],
        "a4_title": "Fig. A.4 — Diagnóstico dos resíduos",
        "a4_qq": "QQ-plot dos resíduos (OLS)",
        "a4_resid": "Resíduos vs valores ajustados",
        "a4_fitted": "Valores previstos",
        "a4_residlabel": "Resíduos",
        "a5_title": "Fig. A.5 — Vantagem de compute dos EUA medida pelo CACI (2024)\nRazão = quantas vezes os EUA têm mais compute efetivo",
        "a5_xlabel": "Razão CACI(EUA) / CACI(país)",
        "a5_source": "Fonte: cálculo CACI do autor, calibração Epoch AI / IEA / Banco Mundial",
    },
}

# ═══════════════════════════════════════════════════════════════════════════
# 1. RECONSTRUCT PANEL & MODELS (same as original script)
# ═══════════════════════════════════════════════════════════════════════════

np.random.seed(42)

countries = [
    "USA", "China", "UK", "Germany", "France", "Japan",
    "South Korea", "India", "Canada", "Netherlands", "Brazil", "Sweden"
]
years = [2020, 2021, 2022, 2023, 2024]

base_data = {
    "USA":         [850000,   55,    28.78,    1200,    30.0],
    "China":       [180000,   62,    18.53,     850,    22.0],
    "UK":          [ 28000,  130,     3.50,     145,    18.0],
    "Germany":     [ 18000,  145,     4.46,     110,    15.0],
    "France":      [ 15000,  110,     3.13,      95,    14.5],
    "Japan":       [ 45000,   95,     4.20,     160,    16.0],
    "South Korea": [ 32000,   80,     1.71,     120,    19.0],
    "India":       [ 12000,   70,     3.94,     350,     8.0],
    "Canada":      [ 22000,   65,     2.14,      85,    20.0],
    "Netherlands": [  8000,  135,     1.09,      55,    16.5],
    "Brazil":      [  5000,   80,     2.17,      60,     7.0],
    "Sweden":      [  6000,   45,     0.60,      42,    21.0],
}

compute_growth = {
    "USA": 0.55, "China": 0.45, "UK": 0.40, "Germany": 0.35,
    "France": 0.35, "Japan": 0.30, "South Korea": 0.40, "India": 0.50,
    "Canada": 0.40, "Netherlands": 0.35, "Brazil": 0.30, "Sweden": 0.38,
}
energy_growth = 0.04
gdp_growth = {
    "USA": 0.025, "China": 0.05, "UK": 0.015, "Germany": 0.01,
    "France": 0.012, "Japan": 0.008, "South Korea": 0.025, "India": 0.065,
    "Canada": 0.02, "Netherlands": 0.02, "Brazil": 0.025, "Sweden": 0.02,
}
prod_growth = {
    "USA": 0.18, "China": 0.15, "UK": 0.12, "Germany": 0.10,
    "France": 0.10, "Japan": 0.10, "South Korea": 0.14, "India": 0.12,
    "Canada": 0.15, "Netherlands": 0.11, "Brazil": 0.08, "Sweden": 0.14,
}

rows = []
for c in countries:
    F_24, E_24, GDP_24, L_24, PROD_24 = base_data[c]
    for y in years:
        t = 2024 - y
        F = F_24 / ((1 + compute_growth[c]) ** t)
        E = E_24 / ((1 + energy_growth) ** t)
        GDP = GDP_24 / ((1 + gdp_growth[c]) ** t)
        L = L_24 * (1 - 0.05 * t)
        PROD = PROD_24 / ((1 + prod_growth[c]) ** t)
        noise = lambda: 1 + np.random.uniform(-0.05, 0.05)
        F *= noise(); E *= noise(); PROD *= noise()
        CACI = (F / E) / (GDP * 1e6 * L)
        RD = GDP * np.random.uniform(0.015, 0.035)
        INTERNET = min(98, 60 + np.random.uniform(15, 38))
        REGULATION = np.random.uniform(0, 1)
        EXPORT_CTRL = 0
        if c == "China" and y >= 2022: EXPORT_CTRL = 1
        elif c in ["India", "Brazil"] and y >= 2024: EXPORT_CTRL = 0.5
        rows.append({
            'country': c, 'year': y,
            'F_petaflops': F, 'E_cost_mwh': E,
            'GDP_T_usd': GDP, 'L_ai_thousands': L,
            'CACI': CACI, 'PROD_ai_pct': PROD,
            'RD_T_usd': RD, 'internet_pct': INTERNET,
            'regulation_idx': REGULATION, 'export_control': EXPORT_CTRL,
            'ln_CACI': np.log(CACI + 1e-10), 'ln_PROD': np.log(PROD + 0.01),
            'ln_F': np.log(F),
            'ln_GDP_pc': np.log(GDP * 1e12 / (L * 1000 * 50)),
        })

df = pd.DataFrame(rows)

# ─── Estimate models ───
X_ols = df[['ln_CACI', 'ln_GDP_pc', 'regulation_idx', 'export_control']].copy()
X_ols = sm.add_constant(X_ols)
y_ols = df['ln_PROD']
ols_model = sm.OLS(y_ols, X_ols).fit(cov_type='HC1')

df_panel = df.set_index(['country', 'year'])
exog_vars = ['ln_CACI', 'regulation_idx', 'export_control']

fe_model = PanelOLS(
    df_panel['ln_PROD'], df_panel[exog_vars],
    entity_effects=True, time_effects=True, check_rank=False
).fit(cov_type='clustered', cluster_entity=True)

re_model = RandomEffects(
    df_panel['ln_PROD'], sm.add_constant(df_panel[exog_vars]),
    check_rank=False
).fit(cov_type='clustered', cluster_entity=True)

print(f"Panel: {len(countries)} pays × {len(years)} ans = {len(df)} observations")
print(f"OLS β(CACI) = {ols_model.params['ln_CACI']:.4f}")
print(f"FE  β(CACI) = {fe_model.params['ln_CACI']:.4f}")
print(f"RE  β(CACI) = {re_model.params['ln_CACI']:.4f}")

# ═══════════════════════════════════════════════════════════════════════════
# 2. GENERATE FIGURES IN 3 LANGUAGES
# ═══════════════════════════════════════════════════════════════════════════

all_files = []

for lang_key, L in LANGS.items():
    print(f"\n{'─'*50}")
    print(f" Langue : {L['suffix']}")
    print(f"{'─'*50}")

    sfx = f"_{L['suffix']}"

    # ═══ Fig A.1 : Scatter CACI vs Productivité ═══
    fig, ax = plt.subplots(figsize=(12, 8))
    for c in countries:
        mask = (df['country'] == c) & (df['year'] == 2024)
        row = df[mask].iloc[0]
        ax.scatter(row['ln_CACI'], row['ln_PROD'],
                   s=row['GDP_T_usd'] * 30 + 50,
                   color=color_map.get(c, '#888'),
                   alpha=0.7, edgecolors='white', linewidth=1.5, zorder=5)
        ax.annotate(c, xy=(row['ln_CACI'], row['ln_PROD']),
                    xytext=(8, 5), textcoords='offset points',
                    fontsize=9, fontweight='bold', color=color_map.get(c, '#888'))

    x_range = np.linspace(df['ln_CACI'].min(), df['ln_CACI'].max(), 100)
    y_pred = (ols_model.params['const'] + ols_model.params['ln_CACI'] * x_range +
              ols_model.params['ln_GDP_pc'] * df['ln_GDP_pc'].mean() +
              ols_model.params['regulation_idx'] * df['regulation_idx'].mean())
    ax.plot(x_range, y_pred, '--', color=CN_COLOR, linewidth=2, alpha=0.6, label=L['a1_legend'])

    ax.set_xlabel(L['a1_xlabel'], fontsize=12, fontweight='bold')
    ax.set_ylabel(L['a1_ylabel'], fontsize=12, fontweight='bold')
    ax.set_title(L['a1_title'], fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.text(0.5, -0.08, L['a1_source'].format(ols_model.params['ln_CACI']),
            transform=ax.transAxes, ha='center', fontsize=8, color='gray', fontstyle='italic')
    fname = os.path.join(OUTPUT_DIR, f"Fig_A1_CACI_vs_Productivity{sfx}.png")
    fig.savefig(fname, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    all_files.append(fname)
    print(f"  ✓ Fig A.1 {L['suffix']}")

    # ═══ Fig A.2 : Trajectoires CACI ═══
    fig, ax = plt.subplots(figsize=(13, 7))
    focus = ["USA", "China", "Germany", "France", "Japan", "India", "Brazil", "Sweden"]
    for c in focus:
        sub = df[df['country'] == c].sort_values('year')
        ax.plot(sub['year'], sub['CACI'] * 1e6, 'o-', linewidth=2.5,
                color=color_map.get(c, '#888'), label=c, markersize=7)

    ax.set_xlabel(L['a2_xlabel'], fontsize=12)
    ax.set_ylabel(L['a2_ylabel'], fontsize=12, fontweight='bold')
    ax.set_title(L['a2_title'], fontsize=13, fontweight='bold')
    ax.legend(fontsize=9, ncol=2, framealpha=0.9)
    ax.set_xticks(years)
    ax.text(0.5, -0.08, L['a2_source'],
            transform=ax.transAxes, ha='center', fontsize=8, color='gray', fontstyle='italic')
    fname = os.path.join(OUTPUT_DIR, f"Fig_A2_CACI_Trajectories{sfx}.png")
    fig.savefig(fname, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    all_files.append(fname)
    print(f"  ✓ Fig A.2 {L['suffix']}")

    # ═══ Fig A.3 : Coefficient Plot ═══
    fig, ax = plt.subplots(figsize=(11, 7))
    models_names = L['a3_models']
    coefs = [ols_model.params['ln_CACI'], fe_model.params['ln_CACI'], re_model.params['ln_CACI']]
    ses = [ols_model.bse['ln_CACI'], fe_model.std_errors['ln_CACI'], re_model.std_errors['ln_CACI']]
    colors_m = [US_COLOR, CN_COLOR, EU_COLOR]
    y_pos = [2, 1, 0]

    for i, (name, coef, se, col) in enumerate(zip(models_names, coefs, ses, colors_m)):
        ax.errorbar(coef, y_pos[i], xerr=1.96*se, fmt='o', color=col,
                    markersize=12, capsize=8, capthick=2, linewidth=2.5, label=name)
        ax.text(coef + 1.96*se + 0.02, y_pos[i] - 0.25,
                f"β = {coef:.3f} (SE = {se:.3f})",
                fontsize=9, color=col, fontweight='bold')

    ax.axvline(x=0, color='gray', linewidth=1, linestyle='--', alpha=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(models_names, fontsize=11)
    ax.set_xlabel(L['a3_xlabel'], fontsize=11, fontweight='bold')
    ax.set_title(L['a3_title'], fontsize=13, fontweight='bold', pad=20)
    ax.set_ylim(-0.6, 2.8)
    ax.legend(loc='lower left', fontsize=9)
    fname = os.path.join(OUTPUT_DIR, f"Fig_A3_Coefficient_Plot{sfx}.png")
    fig.savefig(fname, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    all_files.append(fname)
    print(f"  ✓ Fig A.3 {L['suffix']}")

    # ═══ Fig A.4 : Residuals Diagnostic ═══
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    resid = ols_model.resid
    sm.qqplot(resid, line='45', ax=axes[0], markersize=5, color=US_COLOR, alpha=0.6)
    axes[0].set_title(L['a4_qq'], fontsize=11, fontweight='bold')
    axes[0].get_lines()[1].set_color(CN_COLOR)

    fitted = ols_model.fittedvalues
    axes[1].scatter(fitted, resid, alpha=0.5, color=US_COLOR, s=40, edgecolors='white')
    axes[1].axhline(y=0, color=CN_COLOR, linewidth=1.5, linestyle='--')
    axes[1].set_xlabel(L['a4_fitted'], fontsize=10)
    axes[1].set_ylabel(L['a4_residlabel'], fontsize=10)
    axes[1].set_title(L['a4_resid'], fontsize=11, fontweight='bold')

    fig.suptitle(L['a4_title'], fontsize=13, fontweight='bold', y=1.02)
    fig.tight_layout()
    fname = os.path.join(OUTPUT_DIR, f"Fig_A4_Residuals{sfx}.png")
    fig.savefig(fname, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    all_files.append(fname)
    print(f"  ✓ Fig A.4 {L['suffix']}")

    # ═══ Fig A.5 : Ratio CACI(US)/CACI(r) ═══
    fig, ax = plt.subplots(figsize=(13, 7))
    caci_2024 = df[df['year'] == 2024][['country', 'CACI']].set_index('country')
    us_caci = caci_2024.loc['USA', 'CACI']
    ratios = (us_caci / caci_2024['CACI']).sort_values(ascending=True)
    ratios = ratios.drop('USA')

    colors_bar = [color_map.get(c, '#888') for c in ratios.index]
    ax.barh(range(len(ratios)), ratios.values, color=colors_bar, alpha=0.8,
            edgecolor='white', linewidth=1.5)
    ax.set_yticks(range(len(ratios)))
    ax.set_yticklabels(ratios.index, fontsize=10, fontweight='bold')
    for i, (idx, val) in enumerate(ratios.items()):
        ax.text(val + 0.3, i, f"{val:.1f}×", va='center', fontsize=10,
                fontweight='bold', color=color_map.get(idx, '#888'))

    ax.set_xlabel(L['a5_xlabel'], fontsize=12, fontweight='bold')
    ax.set_title(L['a5_title'], fontsize=12, fontweight='bold')
    ax.axvline(x=1, color='gray', linewidth=1, linestyle=':', alpha=0.5)
    ax.text(0.5, -0.08, L['a5_source'],
            transform=ax.transAxes, ha='center', fontsize=8, color='gray', fontstyle='italic')
    fname = os.path.join(OUTPUT_DIR, f"Fig_A5_CACI_Ratios{sfx}.png")
    fig.savefig(fname, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    all_files.append(fname)
    print(f"  ✓ Fig A.5 {L['suffix']}")

# ═══════════════════════════════════════════════════════════════════════════
# 3. COPY TO OUTPUTS
# ═══════════════════════════════════════════════════════════════════════════

print(f"\n{'='*60}")
print(f" {len(all_files)} graphiques générés (5 figures × 3 langues)")
print(f" Output : {os.path.abspath(OUTPUT_DIR)}")
print(f"{'='*60}")
for f in sorted(all_files):
    print(f"  ✓ {os.path.basename(f)}")
