"""
Chapter VII - Trilingual Graph Generator (EN, FR, PT-BR).

Generates the figures for Chapter VII (Recommendations) in three languages.
All values are aligned with the April 2026 dashboard snapshot.

Author: Fabrice Pizzi (Université Paris-Sorbonne, M2 Intelligence Économique).
"""

from __future__ import annotations

import logging
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("chapter7_graphs_trilingual")

# Visual identity
NAVY = "#1A2744"
GOLD = "#B8922F"
US_COLOR = "#1B4F72"
EU_COLOR = "#D4AC0D"
CN_COLOR = "#C0392B"
ACCENT1 = "#148F77"
ACCENT2 = "#884EA0"
ACCENT3 = "#E67E22"
ACCENT4 = "#2C3E50"
GREY = "#999999"
BG_COLOR = "white"

DPI = 300

LABELS = {
    "EN": {
        "source": "Source: Author's construction",
        "fig71_title": "AI Capex Asymmetry: 2026 Orders of Magnitude",
        "fig71_y": "AI Capex (B USD or EUR)",
        "fig71_labels": ["US Hyperscalers\n(annual 2026)", "Big 5 Total\n(annual 2026)",
                         "InvestAI EU\n(5 yr, 2026-2030)", "France 1% GDP\n(annual target)",
                         "Mistral Private\nCapex 2026"],
        "fig71_legend": ["USA (hyperscalers)", "EU (InvestAI public+private)", "France (1% GDP target)", "European private (Mistral)"],
        "fig71_ratio": "Annual capex ratio\n675 / 200 / 5 = 6.75x\n(annual/annual)",
        "fig72_title": "Temporal Matrix of Recommendations: 5 Axes x 3 Horizons",
        "fig72_axes": ["A1 Compute\ninfrastructure", "A2 Nuclear\nEnergy", "A3 Tech\nAlliances", "A4 Offensive\nRegulation", "A5 Talent\n& Human Capital"],
        "fig72_horizons": ["2026-2027\nShort term", "2027-2029\nMedium term", "2029-2032\nLong term"],
        "fig72_cbar": "Execution Urgency\n(0 = preparatory, 1 = critical)",
        "fig72_notes": [
            ["13 AI Factories\nSpecial Compute Zones", "5 AI Gigafactories\n30-40% sovereign", "40% local\nsovereign frontier"],
            ["Nuclear for AI 250 MW\n6 EDF sites", "EPR 2 launched\n+8 optional", "1st SMR DC\n+20 GW"],
            ["EU-Nvidia\nGPU Reserves", "TSMC 7/5 nm\nEU-Japan HBM", "DARE/RISC-V\nMulti-vendor"],
            ["Apply AI Strategy\nbuy European", "CLOUD Act Shield\nSOV-3 mandatory", "Brussels Effect\nAI export norms"],
            ["Talent visas\nMcKinsey 2026", "GAFAM-level\nsalaries", "Reverse\nbrain drain"],
        ],
        "fig73_title": "EU Operational Sovereignty Trajectory\n(Rise of F_sov on cloud workloads, 2026-2030)",
        "fig73_y": "Share of EU workloads under European jurisdiction (%)",
        "fig73_legend": ["AI Factories EuroHPC", "Sovereign Cloud (SecNumCloud + EUCS)", "Mistral Compute + similar", "AI Gigafactories"],
        "fig73_target": "Target 30-40% sovereign workloads 2029 (Section 7.1.2)",
        "fig74_title": "French Energy Advantage for AI Data Centers\n(Power mix and PPP-adjusted cost, April 2026 baseline)",
        "fig74_y": "Electricity Mix (%)",
        "fig74_countries": ["France", "Germany", "Netherlands", "Ireland", "USA"],
        "fig74_legend": ["Nuclear", "Renewables", "Fossil"],
        "fig74_decarb": "decarbonized",
        "fig74_ppa": ["115 USD/MWh\nratio 1.35x US", "140 USD/MWh\nratio 1.65x US", "130 USD/MWh\nratio 1.53x US", "150 USD/MWh\nratio 1.76x US", "85 USD/MWh\nbaseline"],
        "fig75_title": "Three Levers for Reducing Protectionist Risk",
        "fig75_levers": [
            ("Lever 1\nStrategic GPU Reserves", "Model: Oil reserves (90 days)\n\nTarget: 6-12 months of EU needs\n\nTarget Volume: 200k-400k\nH100-eq GPUs in stock\n\nEst. Cost: 8-15 B EUR\n(amortized over 3-4 years)\n\nProtects against:\n- Affiliates Rule\n- Extended Sec 232 Tariffs"),
            ("Lever 2\nSupplier Diversification", "Short term:\n- AMD MI300X/MI350X\n- Intel Gaudi 3\n- Graphcore (UK)\n\nMedium term:\n- SiPearl Rhea (FR)\n- Non-sensitive Huawei Ascend\n\nLong term:\n- DARE/RISC-V (EuroHPC)\n- 2030-2032 horizon\n\nTarget: 40% non-Nvidia 2030"),
            ("Lever 3\nAnti-weaponization Clauses", "Model: WTO non-discrimination\n\nIntegration into:\n- EU-US Trade Agreement\n- WTO ITA Renewal\n\nMechanisms:\n- Prior notification\n- Export control reciprocity\n- Independent arbitration\n\nLegal protection in case of\nprotectionist rupture"),
        ]
    },
    "FR": {
        "source": "Source : construction de l'auteur",
        "fig71_title": "L'asymetrie de capex IA : ordres de grandeur 2026",
        "fig71_y": "Capex IA (Md USD ou EUR)",
        "fig71_labels": ["Hyperscalers US\n(annuel 2026)", "Big 5 cumule\n(annuel 2026)",
                          "InvestAI EU\n(5 ans, 2026-2030)", "France 1 pct PIB\n(annuel cible)",
                          "Capex prive\nMistral 2026"],
        "fig71_legend": ["USA (hyperscalers)", "UE (InvestAI public+prive)", "France (cible 1 pct PIB)", "Acteur prive europeen (Mistral)"],
        "fig71_ratio": "Ratio capex annuel\n675 / 200 / 5 = 6,75x\n(annuel/annuel)",
        "fig72_title": "Matrice temporelle des recommandations 5 axes x 3 horizons",
        "fig72_axes": ["A1 Compute\ninfrastructure", "A2 Energie\nnucleaire", "A3 Alliances\ntech", "A4 Regulation\noffensive", "A5 Talent\net capital humain"],
        "fig72_horizons": ["2026-2027\nCourt terme", "2027-2029\nMoyen terme", "2029-2032\nLong terme"],
        "fig72_cbar": "Urgence d'execution\n(0 = preparatoire, 1 = critique)",
        "fig72_notes": [
            ["13 AI Factories\nSpecial Compute Zones", "5 AI Gigafactories\n30-40 pct souverain", "40 pct local\nfrontier souverains"],
            ["Nuclear for AI 250 MW\n6 sites EDF", "EPR 2 lances\n+8 optionnels", "1er SMR DC\n+20 GW"],
            ["UE-Nvidia\nReserves GPU", "TSMC 7/5 nm\nUE-Japon HBM", "DARE/RISC-V\nMulti-fournisseur"],
            ["Apply AI Strategy\nbuy European", "CLOUD Act Shield\nSOV-3 obligatoire", "Effet Bruxelles\nNormes IA export"],
            ["Visas talents\nMcKinsey 2026", "Salaires GAFAM\negales", "Captation\nbrain drain inverse"],
        ],
        "fig73_title": "Trajectoire de la souverainete operationnelle UE\n(montee de F_sov sur les charges cloud, 2026-2030)",
        "fig73_y": "Part workloads UE sous juridiction europeenne (pct)",
        "fig73_legend": ["AI Factories EuroHPC", "Cloud souverain (SecNumCloud + EUCS)", "Mistral Compute + similaires", "AI Gigafactories"],
        "fig73_target": "Cible 30-40 pct workloads souverains 2029 (Section 7.1.2)",
        "fig74_title": "Avantage energetique francais pour les data centers IA\n(mix electrique et cout PPA-ajuste, baseline avril 2026)",
        "fig74_y": "Mix electrique (pct)",
        "fig74_countries": ["France", "Allemagne", "Pays-Bas", "Irlande", "USA"],
        "fig74_legend": ["Nucleaire", "Renouvelables", "Fossiles"],
        "fig74_decarb": "decarbone",
        "fig74_ppa": ["115 USD/MWh\nratio 1,35x US", "140 USD/MWh\nratio 1,65x US", "130 USD/MWh\nratio 1,53x US", "150 USD/MWh\nratio 1,76x US", "85 USD/MWh\nbaseline"],
        "fig75_title": "Trois leviers de reduction du risque protectionniste",
        "fig75_levers": [
            ("Levier 1\nReserves strategiques GPU", "Modele : reserves petrole (90 j)\n\nObjectif : 6-12 mois de besoins UE\n\nVolume cible : 200 000-400 000\nGPU H100-eq en stock\n\nCout estime : 8-15 Md EUR\n(amortissable sur 3-4 ans)\n\nProtege contre :\n- Affiliates Rule\n- Tarifs Section 232 etendus"),
            ("Levier 2\nDiversification fournisseurs", "Court terme :\n- AMD MI300X/MI350X\n- Intel Gaudi 3\n- Graphcore (UK)\n\nMoyen terme :\n- SiPearl Rhea (FR)\n- Huawei Ascend non-sensitif\n\nLong terme :\n- DARE/RISC-V (EuroHPC)\n- Horizon 2030-2032\n\nObjectif : 40 pct non-Nvidia 2030"),
            ("Levier 3\nClauses anti-weaponisation", "Modele : non-discrimination OMC\n\nIntegration dans :\n- Accord commercial UE-US\n- Renouvellement WTO ITA\n\nMecanismes :\n- Notification prealable\n- Reciprocite controles export\n- Arbitrage independant\n\nProtection legale en cas de\nrupture protectionniste"),
        ]
    },
    "PT-BR": {
        "source": "Fonte: Construcao do autor",
        "fig71_title": "Assimetria de Capex em IA: Ordens de Grandeza para 2026",
        "fig71_y": "Capex em IA (Bi USD ou EUR)",
        "fig71_labels": ["Hyperscalers EUA\n(anual 2026)", "Total Big 5\n(anual 2026)",
                         "InvestAI UE\n(5 anos, 2026-2030)", "Franca 1% PIB\n(meta anual)",
                         "Capex Privado\nMistral 2026"],
        "fig71_legend": ["EUA (hyperscalers)", "UE (InvestAI publico+privado)", "Franca (meta 1% PIB)", "Privado europeu (Mistral)"],
        "fig71_ratio": "Razao de capex anual\n675 / 200 / 5 = 6,75x\n(anual/anual)",
        "fig72_title": "Matriz Temporal de Recomendacoes: 5 Eixos x 3 Horizontes",
        "fig72_axes": ["A1 Infraestrutura\nde Computacao", "A2 Energia\nNuclear", "A3 Aliancas\nTecnologicas", "A4 Regulamentacao\nOfensiva", "A5 Talento\ne Capital Humano"],
        "fig72_horizons": ["2026-2027\nCurto prazo", "2027-2029\nMedio prazo", "2029-2032\nLongo prazo"],
        "fig72_cbar": "Urgencia de Execucao\n(0 = preparatorio, 1 = critico)",
        "fig72_notes": [
            ["13 AI Factories\nZonas Esp. Compute", "5 AI Gigafactories\n30-40% soberanas", "40% local\nsoberano fronteira"],
            ["Nuclear para IA 250 MW\n6 sites EDF", "EPR 2 lancados\n+8 opcionais", "1o SMR DC\n+20 GW"],
            ["UE-Nvidia\nReservas GPU", "TSMC 7/5 nm\nUE-Japao HBM", "DARE/RISC-V\nMulti-fornecedor"],
            ["Apply AI Strategy\nCompre Europeu", "CLOUD Act Shield\nSOV-3 obrigatorio", "Efeito Bruxelas\nNormas exp. IA"],
            ["Vistos talentos\nMcKinsey 2026", "Salarios nivel\nGAFAM", "Inversao da\nfuga de cerebros"],
        ],
        "fig73_title": "Trajetoria da Soberania Operacional da UE\n(Aumento de F_sov em cargas de nuvem, 2026-2030)",
        "fig73_y": "Parcela de cargas UE sob jurisdicao europeia (%)",
        "fig73_legend": ["AI Factories EuroHPC", "Nuvem Soberana (SecNumCloud + EUCS)", "Mistral Compute + similares", "AI Gigafactories"],
        "fig73_target": "Meta 30-40% cargas soberanas 2029 (Secao 7.1.2)",
        "fig74_title": "Vantagem Energetica Francesa para Data Centers de IA\n(Mix eletrico e custo ajustado-PPP, abril de 2026)",
        "fig74_y": "Mix Eletrico (%)",
        "fig74_countries": ["Franca", "Alemanha", "Paises Baixos", "Irlanda", "EUA"],
        "fig74_legend": ["Nuclear", "Renovaveis", "Fosseis"],
        "fig74_decarb": "descarbonizado",
        "fig74_ppa": ["115 USD/MWh\nrazao 1,35x EUA", "140 USD/MWh\nrazao 1,65x EUA", "130 USD/MWh\nrazao 1,53x EUA", "150 USD/MWh\nrazao 1,76x EUA", "85 USD/MWh\nlinha de base"],
        "fig75_title": "Tres Alavancas para Reducao do Risco Protecionista",
        "fig75_levers": [
            ("Alavanca 1\nReservas Estrategicas de GPU", "Modelo: Reservas de petroleo (90 d)\n\nMeta: 6-12 meses de nec. da UE\n\nVolume Meta: 200k-400k\nGPUs H100-eq em estoque\n\nCusto Est.: 8-15 Bi EUR\n(amortizado em 3-4 anos)\n\nProtege contra:\n- Affiliates Rule\n- Tarifas Sec 232 estendidas"),
            ("Alavanca 2\nDiversificacao de Fornecedores", "Curto prazo:\n- AMD MI300X/MI350X\n- Intel Gaudi 3\n- Graphcore (UK)\n\nMedio prazo:\n- SiPearl Rhea (FR)\n- Huawei Ascend nao sensivel\n\nLongo prazo:\n- DARE/RISC-V (EuroHPC)\n- Horizonte 2030-2032\n\nMeta: 40% nao-Nvidia 2030"),
            ("Alavanca 3\nClausulas Anti-armamentizacao", "Modelo: Nao discriminacao OMC\n\nIntegracao em:\n- Acordo Comercial UE-EUA\n- Renovacao WTO ITA\n\nMecanismos:\n- Notificacao previa\n- Reciprocidade export control\n- Arbitragem independente\n\nProtecao legal em caso de\nruptura protecionista"),
        ]
    }
}

def _common_style() -> None:
    plt.rcParams.update({
        "figure.facecolor": BG_COLOR,
        "axes.facecolor": BG_COLOR,
        "savefig.facecolor": BG_COLOR,
        "font.family": "DejaVu Sans",
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })

def save_fig(fig, basename: str, lang: str, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{basename}_{lang}.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    log.info("Saved %s", out)
    return out

def gen_fig_7_1(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(12, 6.5))
    values = [200, 675, 200, 28, 1.0]
    colors = [US_COLOR, US_COLOR, EU_COLOR, ACCENT1, ACCENT3]
    x = np.arange(len(L["fig71_labels"]))
    bars = ax.bar(x, values, color=colors, alpha=0.85)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 8, f"{val:.0f}" if val >= 10 else f"{val:.1f}", ha="center", fontsize=11, fontweight="bold", color=bar.get_facecolor())
    ax.annotate("", xy=(2.4, 200), xytext=(0.4, 200), arrowprops=dict(arrowstyle="<->", color=GREY, lw=1.5))
    ax.text(1.4, 380, L["fig71_ratio"], ha="center", fontsize=9, fontweight="bold", color=GREY, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=GREY, alpha=0.85))
    ax.set_xticks(x)
    ax.set_xticklabels(L["fig71_labels"], fontsize=9)
    ax.set_ylabel(L["fig71_y"], fontsize=11)
    ax.set_ylim(0, 760)
    ax.set_title(L["fig71_title"], fontsize=14, fontweight="bold", color=NAVY, pad=14)
    legend_elements = [mpatches.Patch(color=c, label=l) for c, l in zip([US_COLOR, EU_COLOR, ACCENT1, ACCENT3], L["fig71_legend"])]
    ax.legend(handles=legend_elements, fontsize=10, loc="upper right", framealpha=0.9)
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    fig.text(0.5, 0.005, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_7.1_Capex_Gap", lang, out_dir)

def gen_fig_7_2(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(11, 7))
    urgency = np.array([[1.00, 0.80, 0.50], [0.85, 1.00, 0.60], [0.70, 0.90, 0.55], [0.65, 1.00, 0.70], [1.00, 0.80, 0.50]])
    im = ax.imshow(urgency, cmap="RdYlGn_r", aspect="auto", vmin=0, vmax=1)
    ax.set_xticks(np.arange(len(L["fig72_horizons"])))
    ax.set_xticklabels(L["fig72_horizons"], fontsize=10)
    ax.set_yticks(np.arange(len(L["fig72_axes"])))
    ax.set_yticklabels(L["fig72_axes"], fontsize=10)
    for i in range(len(L["fig72_axes"])):
        for j in range(len(L["fig72_horizons"])):
            ax.text(j, i, L["fig72_notes"][i][j], ha="center", va="center", fontsize=8.5, fontweight="bold", color="white" if urgency[i, j] > 0.55 else "#222")
    ax.set_title(L["fig72_title"], fontsize=14, fontweight="bold", color=NAVY, pad=15)
    cbar = fig.colorbar(im, ax=ax, shrink=0.7, pad=0.02)
    cbar.set_label(L["fig72_cbar"], fontsize=9, rotation=270, labelpad=22)
    fig.text(0.5, 0.01, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_7.2_Recommendations_Heatmap", lang, out_dir)

def gen_fig_7_3(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(12, 6.5))
    years = [2026, 2027, 2028, 2029, 2030]
    cloud_souv = [10, 13, 18, 23, 28]
    mistral = [3, 5, 8, 11, 14]
    gigafact = [0, 1, 5, 10, 14]
    aifact = [9, 12, 13, 14, 14]
    components = [aifact, cloud_souv, mistral, gigafact]
    colors = [ACCENT1, EU_COLOR, ACCENT3, ACCENT2]
    bottom = np.zeros(len(years))
    for comp, label, col in zip(components, L["fig73_legend"], colors):
        ax.fill_between(years, bottom, bottom + np.array(comp), alpha=0.85, label=label, color=col)
        bottom = bottom + np.array(comp)
    totals = [sum(c[i] for c in components) for i in range(len(years))]
    for x, y in zip(years, totals):
        ax.text(x, y + 1.5, f"{y}%", ha="center", fontsize=10, fontweight="bold", color=NAVY)
    ax.axhline(y=40, color=CN_COLOR, linestyle="--", linewidth=2, alpha=0.7)
    ax.text(2026.1, 41, L["fig73_target"], fontsize=9, fontweight="bold", color=CN_COLOR, fontstyle="italic")
    ax.set_xticks(years)
    ax.set_ylabel(L["fig73_y"], fontsize=11)
    ax.set_ylim(0, 80)
    ax.set_title(L["fig73_title"], fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, loc="upper left")
    fig.text(0.5, 0.005, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_7.3_FSov_Trajectory", lang, out_dir)

def gen_fig_7_4(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(11, 6.5))
    nuclear = [70, 0, 3, 0, 19]
    renewables = [25, 60, 50, 40, 22]
    fossil = [5, 40, 47, 60, 59]
    x = np.arange(len(L["fig74_countries"]))
    w = 0.6
    ax.bar(x, nuclear, w, color=ACCENT1, alpha=0.9, label=L["fig74_legend"][0])
    ax.bar(x, renewables, w, bottom=nuclear, color=EU_COLOR, alpha=0.9, label=L["fig74_legend"][1])
    ax.bar(x, fossil, w, bottom=np.array(nuclear) + np.array(renewables), color=GREY, alpha=0.9, label=L["fig74_legend"][2])
    for i, (cx, cost) in enumerate(zip(x, L["fig74_ppa"])):
        ax.text(cx, 105, cost, ha="center", fontsize=9, fontweight="bold", color=NAVY, bbox=dict(boxstyle="round,pad=0.25", facecolor="#F0F4F8", edgecolor=NAVY, alpha=0.85))
    for i, (cx, n, r) in enumerate(zip(x, nuclear, renewables)):
        decarb = n + r
        ax.text(cx, n + r / 2 if r > 5 else n / 2, f"{decarb}%\n{L['fig74_decarb']}", ha="center", va="center", fontsize=10, fontweight="bold", color="white")
    ax.set_xticks(x)
    ax.set_xticklabels(L["fig74_countries"], fontsize=11)
    ax.set_ylabel(L["fig74_y"], fontsize=11)
    ax.set_ylim(0, 130)
    ax.set_title(L["fig74_title"], fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.legend(fontsize=10, loc="upper right")
    fig.text(0.5, 0.005, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_7.4_Energy_Mix", lang, out_dir)

def gen_fig_7_5(lang: str, out_dir: Path):
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.text(6, 6.6, L["fig75_title"], ha="center", fontsize=15, fontweight="bold", color=NAVY)
    box_w, box_h = 3.4, 5.0
    colors = [CN_COLOR, ACCENT3, ACCENT1]
    for i, (title, body) in enumerate(L["fig75_levers"]):
        x = 0.4 + i * 3.9
        rect = mpatches.FancyBboxPatch((x, 0.6), box_w, box_h, boxstyle="round,pad=0.15", facecolor=colors[i], alpha=0.12, edgecolor=colors[i], linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + box_w / 2, 5.0, title, ha="center", fontsize=12, fontweight="bold", color=colors[i], linespacing=1.3)
        ax.text(x + box_w / 2, 2.7, body, ha="center", fontsize=9.5, color="#333", linespacing=1.5)
    ax.text(6, 0.2, L["source"], ha="center", fontsize=8, color="gray", fontstyle="italic")
    save_fig(fig, "Fig_7.5_Risk_Reduction", lang, out_dir)

def main() -> None:
    _common_style()
    out_dir = Path("./figures_ch7").resolve()
    for lang in ["EN", "FR", "PT-BR"]:
        log.info("Generating Chapter VII graphs for: %s", lang)
        gen_fig_7_1(lang, out_dir)
        gen_fig_7_2(lang, out_dir)
        gen_fig_7_3(lang, out_dir)
        gen_fig_7_4(lang, out_dir)
        gen_fig_7_5(lang, out_dir)

if __name__ == "__main__":
    main()
