"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
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

Annexe D - Huang Doctrine - Trilingual Generator (EN, FR, PT-BR).

Generates the .docx for Annex D in three languages.
Research note on the 'Huang Doctrine' and cognitive density economy.
"""

from __future__ import annotations

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
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

from annexes_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("annexe_d_trilingual")

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
    label="ANNEX D - RESEARCH NOTE",
    title="Cognitive Density Economy and Market Structuring: An Economic Intelligence Analysis of the Huang Doctrine on AI Token Consumption",
    intro=(
        "This annex presents the March 2026 research note on the cognitive density economy, written following the "
        "statement by Jensen Huang (CEO of NVIDIA) on March 20: 'If an engineer paid $500,000 does not consume at "
        "least $250,000 of AI tokens per year, I would be deeply alarmed.' The note proposes an economic intelligence "
        "analysis of this statement, placing it in the context of NVIDIA's dominant market position (80% share) and "
        f"the American protectionist architecture documented in the CACI Power Mode index ({fmt_en(us_eu_caci, 2)}:1 US/EU ratio). "
        "The analysis demonstrates that the prescription of massive token consumption is more about market structuring "
        "than managerial advice."
    ),
    sections=[
        ("D.1 Context: A High-Impact Statement", [
            "On March 20, 2026, at the San Jose GTC, Jensen Huang stated that an engineer earning $500,000 who doesn't spend at least $250,000 on AI tokens would be a cause for alarm. He confirmed NVIDIA is attempting to spend $2 billion on tokens for its own engineering team.",
            "Professional reception focused almost exclusively on the managerial dimension: productivity through intensive AI use. This note proposes a different reading based on economic intelligence.",
        ]),
        ("D.2 Analytical Framework: Who is Speaking?", [
            "The first reflex in economic intelligence is to identify the speaker's structural position. Jensen Huang is the CEO of NVIDIA, the world's leading supplier of AI accelerators (80% market share). NVIDIA is the primary beneficiary of increased token consumption worldwide.",
            "Therefore, the 'consume half your salary in tokens' directive is not a neutral managerial tip; it is a market-structuring act. Every dollar spent on tokens generates demand for compute executed on NVIDIA hardware.",
        ]),
        ("D.5 Cognitive Density Economy: From Managerial to Geostrategic Meaning", [
            "Cognitive density refers not just to individual productivity, but to a new global power regime. A nation's wealth is increasingly measured by its capacity to transform compute into reliable, verifiable, and sovereign results.",
            f"This is formalized by the CACI Power Mode (F^0.40 x L^0.20 x R^0.15 / E^0.25). On the April 2026 snapshot, the US/EU CACI ratio stands at {fmt_en(us_eu_caci, 2)}:1, driven by a {fmt_en(us_eu_raw, 1)}:1 raw operational compute gap and a 1.59x energy cost advantage for the US.",
        ]),
        ("D.7 Conclusion", [
            "The Huang doctrine on cognitive density should be read not as a universal productivity mandate, but as a signal of market structuring whose structural beneficiaries (NVIDIA, US hyperscalers) are identified. For France and Europe, the goal is not technological autarky, but the capacity to choose: mastering the ratio between produced value and accepted dependence.",
        ]),
    ],
    tables=[
        ("Table D.1. Empirical data on GenAI ROI in enterprises (2025-2026).", "Source: Author's compilation from independent surveys.", [
            ["Source", "Year", "Main Finding"],
            ["MIT NANDA 'The GenAI Divide'", "2025", "95% of GenAI projects in enterprises produced no measurable P&L impact"],
            ["PwC CEO Survey (Davos)", "2026", "56% of CEOs state AI has not produced significant benefits"],
            ["Gartner", "2025", "60% of AI projects abandoned by end of 2026 due to non-AI-ready data"],
        ]),
    ],
    notes=[
        "Jensen Huang, All-In Podcast, March 20, 2026.",
        "NVIDIA Market Share: 80% (SIA, McKinsey).",
        f"CACI Power Mode ratio US/EU: {fmt_en(us_eu_caci, 2)}:1 (Snapshot April 2026).",
        "MIT NANDA 'The GenAI Divide' (2025).",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Annex D Huang Doctrine",
    filename="Annex_D_Huang_Doctrine_EN.docx"
)

# ---------------------------------------------------------------------------
# Content - FRENCH
# ---------------------------------------------------------------------------

FR = LangPack(
    code="FR",
    label="ANNEXE D - NOTE DE RECHERCHE",
    title="Economie de densite cognitive et structuration de marche : lecture d'intelligence economique de la doctrine Huang sur la consommation de tokens IA",
    intro=(
        "Cette annexe presente la note de recherche de mars 2026 sur l'economie de densite cognitive, redigee suite a la "
        "declaration de Jensen Huang (CEO de NVIDIA) du 20 mars 2026."
    ),
    sections=[
        ("D.1 Contexte : une declaration a forte resonance mediatique", [
            "Le 20 mars 2026, Jensen Huang a declare qu'un ingenieur remunere 500 000 USD devrait consommer au minimum 250 000 USD de tokens IA par an.",
        ]),
        ("D.2 Grille de lecture : qui parle ?", [
            "Jensen Huang est le CEO de NVIDIA, premier fournisseur mondial d'accelerateurs IA (80% parts de marche).",
        ]),
    ],
    tables=[
        ("Tableau D.1. Donnees empiriques sur le ROI GenAI.", "Source : compilation de l'auteur.", [
            ["Source", "Annee", "Constat principal"],
            ["MIT NANDA", "2025", "95% des projets GenAI sans impact P&L mesurable"],
        ]),
    ],
    notes=[
        "Jensen Huang, All-In Podcast, 20 mars 2026.",
        f"Snapshot avril 2026 : ratio CACI US/UE {fmt_fr(us_eu_caci, 2)}:1.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Annexe D Doctrine Huang",
    filename="Annexe_D_Densite_Cognitive_Huang_FR.docx"
)

# ---------------------------------------------------------------------------
# Content - PORTUGUESE (BRAZIL)
# ---------------------------------------------------------------------------

BR = LangPack(
    code="PT-BR",
    label="ANEXO D - NOTA DE PESQUISA",
    title="Economia de Densidade Cognitiva e Estruturaçao de Mercado: Uma Analise de Inteligencia Economica da Doutrina Huang sobre o Consumo de Tokens de IA",
    intro=(
        "Este anexo apresenta a nota de pesquisa de março de 2026 sobre a economia de densidade cognitiva, escrita apos a "
        "declaraçao de Jensen Huang (CEO da NVIDIA) em 20 de março de 2026: 'Se um engenheiro que ganha $500.000 nao "
        "consome pelo menos $250.000 de tokens de IA por ano, eu ficaria profundamente alarmado.' A nota propoe uma "
        "leitura de inteligencia economica desta declaraçao."
    ),
    sections=[
        ("D.1 Contexto: Uma Declaração de Alto Impacto", [
            "Em 20 de março de 2026, Jensen Huang afirmou que um engenheiro ganhando $500.000 que nao gasta pelo menos $250.000 em tokens de IA seria motivo de alarme.",
        ]),
        ("D.2 Estrutura Analítica: Quem está falando?", [
            "Jensen Huang e o CEO da NVIDIA, lider mundial em aceleradores de IA (80% de mercado). A NVIDIA e a principal beneficiaria do aumento do consumo de tokens.",
        ]),
        ("D.7 Conclusão", [
            "A doutrina Huang sobre densidade cognitiva deve ser lida nao como um mandato universal de produtividade, mas como um sinal de estruturaçao de mercado. Para a França e a Europa, o objetivo e a capacidade de escolha: dominar a razao entre valor produzido e dependencia aceita.",
        ]),
    ],
    tables=[
        ("Tabela D.1. Dados empíricos sobre ROI de GenAI.", "Fonte: Compilaçao do autor.", [
            ["Fonte", "Ano", "Principal Descoberta"],
            ["MIT NANDA", "2025", "95% dos projetos GenAI sem impacto mensuravel no P&L"],
        ]),
    ],
    notes=[
        "Jensen Huang, All-In Podcast, 20 de março de 2026.",
        f"Snapshot abril 2026: ratio CACI EUA/UE {fmt_fr(us_eu_caci, 2)}:1.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Anexo D Doutrina Huang",
    filename="Anexo_D_Densidade_Cognitiva_Huang_PT-BR.docx"
)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

LANGS = [EN, FR, BR]

def build_all(out_dir: Path) -> None:
    for lp in LANGS:
        log.info("Building Annexe D [%s] -> %s", lp.code, lp.filename)
        doc = init_document()
        add_cover(doc, lang=lp.code, chapter_label=lp.label, chapter_subtitle="Note de recherche - Densite cognitive" if lp.code == "FR" else ("Research Note - Cognitive Density" if lp.code == "EN" else "Nota de Pesquisa - Densidade Cognitiva"))
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
