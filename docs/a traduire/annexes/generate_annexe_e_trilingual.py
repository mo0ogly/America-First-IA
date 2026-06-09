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

Annexe E - AI as Method Amplifier - Trilingual Generator (EN, FR, PT-BR).

Generates the .docx for Annex E in three languages.
Research note on model behavioral engineering and cognitive density at individual/org levels.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from annexes_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("annexe_e_trilingual")

@dataclass
class LangPack:
    code: str
    label: str
    title: str
    intro: str
    sections: list[tuple[str, list[str]]]
    notes: list[str]
    footer: str
    filename: str

# ---------------------------------------------------------------------------
# Content - ENGLISH
# ---------------------------------------------------------------------------

EN = LangPack(
    code="EN",
    label="ANNEX E - RESEARCH NOTE",
    title="AI as a Method Amplifier: Why the Rare Skill in the AI Economy Will Be Framing, Not Production",
    intro=(
        "This annex presents the March 2026 research note on AI as a method amplifier. The democratization of "
        "generative AI tools since 2023 has produced a paradox: more powerful tools have, initially, industrialized "
        "a new category of professional mediocrity. This note analyzes why the rare skill in the AI economy will not "
        "be the ability to produce, but the ability to frame, verify, orchestrate, and arbitrate model outputs. "
        "The concept of cognitive density economy is introduced for this new work regime, complementing the "
        "geostrategic analysis in Annex D."
    ),
    sections=[
        ("E.1 The Paradox of the First Phase: Tool Power, Method Poverty", [
            "Since 2023, the rapid democratization of LLMs has put considerable production capacity in the hands of professionals who had no structured method to pilot them. The result is often superficial analysis and fragile code—deliverables that pass initial reviews but fail in production.",
            "This was often blamed on model hallucinations, but a more rigorous analysis shows the problem is human: lack of problem framing, lack of output verification, and lack of critical questioning. The machine amplified a poor work method; it did not create it.",
        ]),
        ("E.3 Redistribution of Skills: Method Over Seniority", [
            "AI redistributes competitive advantages counter-intuitively. Seniority without an explicit reasoning structure loses value. A senior professional piloting AI loosely will be overtaken by a junior with a rigorous reflection structure: capable of decomposing problems, orchestrating tools, and validating before delivery.",
        ]),
        ("E.4 Behavioral Engineering of the Model: The LIA-Scan Case", [
            "LIA-Scan is a cybersecurity configuration audit platform (200+ technologies). To automate CVE detection rules, an agentic n8n pipeline was designed. The agent does not produce a direct YAML rule; it goes through a mandatory structured loop: decomposition, planning, action, observation, and explicit scoring evaluation.",
            "This is not just 'using AI'; it is behavioral engineering of the model: designing structural constraints that force the model to produce in a controlled, evaluable, and traceable manner. This is the skill the AI economy will value most.",
        ]),
        ("E.6 Conclusion", [
            f"We are not entering an economy of assisted laziness. We are entering an economy of cognitive density, and the level of demand will rise as fast as the models progress. For European professionals, the imperative is to compensate for infrastructure asymmetry (CACI ratio US/EU {fmt_en(us_eu_caci, 2)}:1) with methodological superiority. Method becomes the strategic weapon of the compute-deprived jurisdiction.",
        ]),
    ],
    notes=[
        "Jensen Huang, GTC 2026 Keynote: Five-layer model (Energy, Chips, Infrastructure, Models, Apps).",
        "CACI Power Mode: F^0.40 x L^0.20 x R^0.15 / E^0.25 (Pizzi, 2026).",
        "LIA-Scan: Cybersecurity audit platform with agentic pipeline.",
        "Annex D: Complementary geostrategic reading of the Huang doctrine.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Annex E Method Amplifier",
    filename="Annex_E_AI_Method_Amplifier_EN.docx"
)

# ---------------------------------------------------------------------------
# Content - FRENCH
# ---------------------------------------------------------------------------

FR = LangPack(
    code="FR",
    label="ANNEXE E - NOTE DE RECHERCHE",
    title="L'IA comme amplificateur de methode : pourquoi la competence rare de l'economie IA sera le cadrage, pas la production",
    intro=(
        "Cette annexe presente la note de recherche de mars 2026 sur l'IA comme amplificateur de methode."
    ),
    sections=[
        ("E.1 Le paradoxe de la premiere phase", [
            "La machine a amplifie une mauvaise methode de travail. Elle ne l'a pas creee."
        ]),
        ("E.4 Ingenierie comportementale : LIA-Scan", [
            "LIA-Scan est une plateforme d'audit de configuration cybersecurite."
        ]),
    ],
    notes=[
        "Jensen Huang, GTC 2026 : modele a 5 couches.",
        f"Snapshot avril 2026 : ratio CACI US/UE {fmt_fr(us_eu_caci, 2)}:1.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Annexe E IA amplificateur de methode",
    filename="Annexe_E_IA_Amplificateur_Methode_FR.docx"
)

# ---------------------------------------------------------------------------
# Content - PORTUGUESE (BRAZIL)
# ---------------------------------------------------------------------------

BR = LangPack(
    code="PT-BR",
    label="ANEXO E - NOTA DE PESQUISA",
    title="A IA como Amplificador de Metodo: Por que a Competencia Rara na Economia da IA sera o Enquadramento, nao a Produçao",
    intro=(
        "Este anexo apresenta a nota de pesquisa de março de 2026 sobre a IA como amplificador de metodo. "
        "A democratizaçao das ferramentas de IA generativa desde 2023 produziu um paradoxo: ferramentas mais potentes "
        "inicialmente industrializaram uma nova categoria de mediocridade profissional. Esta nota analisa por que a "
        "competencia rara na economia da IA nao sera a capacidade de produzir, mas a capacidade de enquadrar, verificar, "
        "orquestrar e arbitrar as saídas dos modelos."
    ),
    sections=[
        ("E.1 O Paradoxo da Primeira Fase: Poder da Ferramenta, Pobreza de Método", [
            "Desde 2023, a democratizaçao dos LLMs colocou uma capacidade de produçao consideravel nas maos de profissionais sem metodo estruturado. O resultado e frequentemente analises superficiais e codigo fragil.",
            "A maquina amplificou um mau metodo de trabalho; ela nao o criou.",
        ]),
        ("E.3 Redistribuição de Competências: Método sobre Senioridade", [
            "A IA redistribui vantagens competitivas de forma contra-intuitiva. Senioridade sem estrutura de raciocinio perde valor. Um profissional senior pilotando a IA de forma vaga sera superado por um junior com uma estrutura de reflexao rigorosa.",
        ]),
        ("E.6 Conclusão", [
            f"Nao estamos entrando em uma economia de preguiça assistida. Estamos entrando em uma economia de densidade cognitiva. Para profissionais europeus e brasileiros, o imperativo e compensar a assimetria de infraestrutura (ratio CACI EUA/UE {fmt_fr(us_eu_caci, 2)}:1) com superioridade metodologica. O metodo torna-se a arma estrategica da jurisdiçao com pouco compute.",
        ]),
    ],
    notes=[
        "Jensen Huang, GTC 2026: Modelo de 5 camadas.",
        "CACI Power Mode: F^0,40 x L^0,20 x R^0,15 / E^0,25 (Pizzi, 2026).",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Anexo E Amplificador de Metodo",
    filename="Anexo_E_AI_Amplificador_Metodo_PT-BR.docx"
)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

LANGS = [EN, FR, BR]

def build_all(out_dir: Path) -> None:
    for lp in LANGS:
        log.info("Building Annexe E [%s] -> %s", lp.code, lp.filename)
        doc = init_document()
        add_cover(doc, lang=lp.code, chapter_label=lp.label, chapter_subtitle="Note de recherche - Methode et IA" if lp.code == "FR" else ("Research Note - AI and Method" if lp.code == "EN" else "Nota de Pesquisa - IA e Metodo"))
        add_chapter_header(doc, label=lp.label, title=lp.title, intro=lp.intro)
        
        for title, paragraphs in lp.sections:
            render_section(doc, title, paragraphs)
            
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
