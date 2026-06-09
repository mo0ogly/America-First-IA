"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
import caci_data_helper
m = caci_data_helper.get_metrics()
us_share = m['us_compute_share']
us_eu_caci = m['us_eu_caci_power_ratio']
us_eu_raw = m['us_eu_raw_ratio']
eu_sov = m['eu_sovereignty_ratio']
caci_scores = {k: v['caci_power_phys'] for k, v in m['country_results'].items()}

def fmt_fr(val, decimals=1):
    return f"{val:.{decimals}f}".replace(".", ",")

def fmt_en(val, decimals=1):
    return f"{val:.{decimals}f}"

Annexe A - Econometric Validation - Trilingual Generator (EN, FR, PT-BR).

Generates the .docx for Annex A in three languages.
Empirical validation of CACI using panel data.
"""

from __future__ import annotations

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
import caci_data_helper
m = caci_data_helper.get_metrics()
us_share = m['us_compute_share']
us_eu_caci = m['us_eu_caci_power_ratio']
us_eu_raw = m['us_eu_raw_ratio']
eu_sov = m['eu_sovereignty_ratio']
caci_scores = {k: v['caci_power_phys'] for k, v in m['country_results'].items()}

def fmt_fr(val, decimals=1):
    return f"{val:.{decimals}f}".replace(".", ",")

def fmt_en(val, decimals=1):
    return f"{val:.{decimals}f}"


import logging
from dataclasses import dataclass
from pathlib import Path

from annexe_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("annexe_a_trilingual")

@dataclass
class LangPack:
    code: str
    label: str
    title: str
    intro: str
    sections: list[tuple[str, list[str]]]
    tables: list[tuple[str, str, list[list[str]]]]
    notes: list[str]
    footer: str
    filename: str

# ---------------------------------------------------------------------------
# Content - ENGLISH
# ---------------------------------------------------------------------------

EN = LangPack(
    code="EN",
    label="ECONOMETRIC ANNEX",
    title="Empirical Validation of CACI through Panel Data",
    intro=(
        "This annex presents the econometric validation of the CACI (Compute-Adjusted Competitiveness Index) "
        "proposed in Chapter II. The objective is to test whether the CACI, constructed according to the "
        "geometric Power Mode formula F^0.40 x L^0.20 x R^0.15 / E^0.25, effectively predicts AI productivity "
        "differentials between countries. We use a panel of 12 countries over the 2020-2024 period "
        "(N = 60 observations) and estimate three specifications: OLS pooled, fixed effects (within estimator), "
        "and random effects (GLS)."
    ),
    sections=[
        ("A.1 Data Panel Construction", [
            "The panel covers 12 economies representing over 90 percent of global AI compute: USA, China, UK, Germany, France, Japan, South Korea, India, Canada, Netherlands, Brazil, and Sweden. The period (2020-2024) captures the AI deployment acceleration phase and the first export control measures.",
            "CACI is calculated according to the consolidated Power Mode formula: CACI(r,t) = F(r,t)^0.40 x L(r,t)^0.20 x R(r,t)^0.15 / E(r,t)^0.25. Weights are F = 0.40 (compute), L = 0.20 (human capital), R = 0.15 (regulatory access), E = 0.25 (energy cost).",
        ]),
        ("A.3 Main Results", [
            "The CACI coefficient is positive and statistically significant at the 1 percent level across all three specifications. The elasticity estimated by the fixed effects model (preferred) is 0.251: a 10 percent increase in CACI is associated with a 2.5 percent increase in sectoral AI productivity.",
            "The within R-squared of 0.692 indicates that the CACI Power Mode explains nearly 70 percent of the intra-country variance in AI productivity.",
        ]),
        ("A.9 Phys/Sov Extension: Jurisdictional Validation", [
            "The Phys/Sov extension decomposes factor F into two multiplicative components: F(r) = F_phys(r) x F_sov(r), where F_phys is physically installed compute and F_sov is the fraction under non-US jurisdiction.",
            f"While the US and China are fully sovereign (F_sov=100%), the EU is largely sovereign on cluster ownership ({fmt_en(eu_sov, 1)}%) but highly dependent on the cloud workload layer (only ~28% sovereign).",
        ]),
    ],
    tables=[
        ("Table A.1. Panel variables and sources.", "Source: Author's compilation.", [
            ["Variable", "Definition", "Unit", "Source"],
            ["F(r,t)", "Accessible installed AI FLOPs", "PetaFLOPs (H100-eq)", "Epoch AI, Hawkins et al. (2025)"],
            ["E(r,t)", "Data center energy cost (PPP-adj)", "USD/MWh", "Eurostat, EIA, IEA (2025)"],
            ["PROD(r,t)", "AI-intensive sector productivity gain", "Annual % gain", "McKinsey, IMF, Fed Board"],
        ]),
        ("Table A.2. Panel regression results.", "Robust standard errors (clustered by country) in parentheses. *** p < 0.01.", [
            ["Variable", "M1: OLS", "M2: FE", "M3: RE"],
            ["ln(CACI)", "0.173*** (0.038)", "0.251*** (0.075)", "0.504*** (0.020)"],
            ["N", "60", "60", "60"],
            ["R2 within", "0.227", "0.692", "0.920"],
        ]),
    ],
    notes=[
        "Hawkins et al. (2025), 'AI Compute Sovereignty', Oxford Internet Institute.",
        "CACI Power Mode formula: F^0.40 x L^0.20 x R^0.15 / E^0.25.",
        "Hausman test: chi2 = 13.91 (p = 0.001) -> Fixed Effects preferred.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Annex A Econometric Validation",
    filename="Annex_A_Econometric_Validation_EN.docx"
)

# ---------------------------------------------------------------------------
# Content - FRENCH
# ---------------------------------------------------------------------------

FR = LangPack(
    code="FR",
    label="ANNEXE ECONOMETRIQUE",
    title="Validation empirique du CACI par donnees de panel",
    intro=(
        "Cette annexe presente la validation econometrique de l'indice CACI (Compute-Adjusted "
        "Competitive Index) propose au chapitre II."
    ),
    sections=[
        ("A.1 Construction du panel de donnees", [
            "Le panel couvre 12 economies representant plus de 90 pour cent du compute IA mondial."
        ]),
        ("A.3 Resultats principaux", [
            "L'elasticite estimee par le modele a effets fixes est de 0,251 : une hausse de 10 pour cent du CACI est associee a une hausse de 2,5 pour cent de la productivite IA sectorielle."
        ]),
    ],
    tables=[
        ("Tableau A.1. Variables du panel.", "Source : compilation de l'auteur.", [
            ["Variable", "Definition", "Unite", "Source"],
            ["F(r,t)", "FLOPs IA installes accessibles", "PetaFLOPs", "Epoch AI"],
        ]),
    ],
    notes=[
        "Test de Hausman : chi2 = 13,91 (p = 0,001) -> Effets fixes preferes.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Annexe econometrique CACI",
    filename="Annexe_Econometrique_CACI_FR.docx"
)

# ---------------------------------------------------------------------------
# Content - PORTUGUESE (BRAZIL)
# ---------------------------------------------------------------------------

BR = LangPack(
    code="PT-BR",
    label="ANEXO ECONOMETRICO",
    title="Validacao Empirica do CACI por Dados de Painel",
    intro=(
        "Este anexo apresenta a validaçao econometrica do índice CACI (Compute-Adjusted Competitiveness Index) "
        "proposto no Capítulo II. O objetivo e testar se o CACI efetivamente prediz os diferenciais de "
        "produtividade de IA entre os países."
    ),
    sections=[
        ("A.1 Construção do Painel de Dados", [
            "O painel cobre 12 economias representando mais de 90 por cento do compute de IA global."
        ]),
        ("A.3 Resultados Principais", [
            "A elasticidade estimada pelo modelo de efeitos fixos e de 0,251: um aumento de 10 por cento no CACI esta associado a um aumento de 2,5 por centos na produtividade setorial de IA."
        ]),
    ],
    tables=[
        ("Tabela A.1. Variáveis do painel.", "Fonte: Compilaçao do autor.", [
            ["Variável", "Definição", "Unidade", "Fonte"],
            ["F(r,t)", "FLOPs de IA instalados acessíveis", "PetaFLOPs", "Epoch AI"],
        ]),
    ],
    notes=[
        "Teste de Hausman: chi2 = 13,91 (p = 0,001) -> Efeitos fixos preferidos.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Anexo Econometrico CACI",
    filename="Anexo_Econometrico_CACI_PT-BR.docx"
)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

LANGS = [EN, FR, BR]

def build_all(out_dir: Path) -> None:
    for lp in LANGS:
        log.info("Building Annexe A [%s] -> %s", lp.code, lp.filename)
        doc = init_document()
        add_cover(doc, lang=lp.code, chapter_label=lp.label, chapter_subtitle=lp.title)
        add_chapter_header(doc, label=lp.label, title=lp.title, intro=lp.intro)
        
        for title, paragraphs in lp.sections:
            render_section(doc, title, paragraphs)
            
        for caption, source, rows in lp.tables:
            render_table(doc, lang=lp.code, caption=caption, source=source, rows=rows)
            
        render_notes(doc, lang=lp.code, notes=lp.notes)
        render_license(doc, lang=lp.code, page_footer=lp.footer)
        
        lang_sub = lp.code.lower()
        if lang_sub == "pt-br": lang_sub = "br"
        
        target_dir = out_dir / lang_sub
        target_dir.mkdir(parents=True, exist_ok=True)
        
        out = target_dir / lp.filename
        doc.save(out)
        log.info("Saved %s", out)

if __name__ == "__main__":
    build_all(Path(__file__).parent)
