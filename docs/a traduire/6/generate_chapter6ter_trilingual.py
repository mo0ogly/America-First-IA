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

Chapter VI ter - Consequences for Asia and China - trilingual generator.

Generates the .docx for Chapter VI ter in English, French, and Brazilian Portuguese.
All content is aligned with the April 2026 dashboard snapshot.

Author: Fabrice Pizzi (Université Paris-Sorbonne, M2 Intelligence Économique).
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path

from chap6_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
    render_image,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("chapter6ter_trilingual")

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
    label="CHAPTER VI TER",
    title="Consequences for Asia and China",
    intro=(
        "Asia is the main target and the primary victim of American AI protectionism. "
        "This chapter analyzes the consequences of the containment regime on China, "
        "the pressure on the 'Tier 1' allies (Japan, South Korea, Taiwan), and the "
        "emergence of Southeast Asia as a secondary compute hub. The analysis highlights "
        "the transition from a logic of interdependence to a logic of total decoupling."
    ),
    sections=[
        ("6ter.1 China: resilience under maximum containment", []),
        ("6ter.1.1 The impact of total hardware decoupling", [
            "China faces the most severe restrictions in history. Since the October 2022 and 2023 rules, supplemented by the June 2025 'Superchips' restrictions, Chinese access to advanced AI accelerators (Nvidia H100, B200) is de facto prohibited. In April 2026, the US/China CACI Power Mode ratio is 2.14:1, a significant gap that measures the effectiveness of the containment (Chapter III).",
            "This asymmetry forces China into a strategy of hardware substitution. Huawei (Ascend 910C), Biren, and Moore Threads are developing national accelerators which, although 1 to 2 generations behind Nvidia, allow for the training of Large Language Models (LLMs). ByteDance has notably placed an order for 100,000 Ascend 910B chips in 2024 to compensate for the H100 shortage.[1] However, the yield of SMIC's 7nm and 5nm nodes remains limited by the lack of EUV lithography (ASML export prohibition), creating a structural ceiling for Chinese hardware sovereignty.",
        ]),
        ("6ter.1.2 Reorientation toward 'Global South Compute'", [
            "In response to domestic containment, China is deploying an international compute strategy. The ByteDance-Pecém project in Brazil (38 billion USD, Chapter VI bis) and investments in Malaysia (Johor hub) illustrate this desire to build 'Geographic Redundancy' for Chinese compute. By installing data centers in Tier 2 countries (Malaysia, Brazil, UAE), Chinese actors seek to bypass direct export controls, even if the US 'Affiliates Rule' (November 2025) seeks to close this loophole by extending restrictions to foreign subsidiaries of listed entities.[2]",
        ]),
        ("6ter.2 The Tier 1 Allies: Japan, South Korea, Taiwan", []),
        ("6ter.2.1 Taiwan: the geopolitical fab under pressure", [
            "Taiwan (TSMC) produces 92% of the world's most advanced semiconductors. Under US protectionism, Taiwan is under dual pressure: (i) the 'hollowing out' of its production toward the US (Arizona Fabs) to satisfy American resilience requirements, and (ii) the hardening of export controls toward China, its primary trading partner. The 'Geographic Diversity' required by the US (Chapter IV) creates a risk of industrial dilution for Taiwan, while increasing the cost of chips for its domestic ecosystem.",
        ]),
        ("6ter.2.2 Japan and South Korea: the RISC-V and alternative foundry bet", [
            "Japan (Rapidus) and South Korea (Samsung) are investing massively to break the TSMC/Nvidia duopoly. Japan has launched the 'LSTC' (Leading-edge Semiconductor Technology Center) to develop 2nm chips by 2027. South Korea, through the 'AI Semiconductor Strategy', aims to capture 80% of the AI memory market (HBM3e/4) by 2030.[3] For these allies, US protectionism is a double-edged sword: it offers protected access to the US market (Tier 1) but imposes alignment on export controls that damages their relations with China.",
        ]),
        ("6ter.3 Southeast Asia: the new 'Middle Ground'", [
            "Malaysia (Johor), Vietnam, and Indonesia are emerging as the new preferred destinations for data centers. Malaysia attracted more than 15 billion USD in data center investments in 2024-2025 (Microsoft, Google, ByteDance, Nvidia/YTL).[4] These countries take advantage of their Tier 2 status to host both American and Chinese infrastructure, creating a 'Compute Non-Alignment' similar to Brazil's, but with much greater proximity to the Chinese supply chain.",
        ]),
        ("6ter.4 Synthesis: toward a fragmented Asian compute", [
            "Asia is fracturing into three distinct zones: a 'Sovereign Chinese Zone' (hardware substitution, massive state investment), a 'Tier 1 Pro-US Zone' (high-end foundry, total alignment), and a 'Tier 2 Emerging Zone' (arbitrage hub, US-China duality). This fragmentation increases the complexity of global supply chains and significantly raises the marginal cost of compute for the entire region.",
        ]),
    ],
    tables=[
        ("Table 18. Comparison of AI hardware capacities in Asia (April 2026).",
         "Source: Author's construction, calibration on the public dashboard.",
         [
             ["Country/Region", "US Status", "Primary Hardware", "CACI Power Mode (est.)", "Strategic Constraint"],
             ["China", "Tier 3", "Huawei Ascend, Biren", "0.47 (relative to US)", "SMIC yield (7nm ceiling)"],
             ["Taiwan", "Tier 1", "TSMC (Nvidia/AMD)", "0.85 (relative to US)", "Resilience-driven offshoring"],
             ["Japan", "Tier 1", "Rapidus/Nvidia", "0.62 (relative to US)", "Energy cost + 2nm execution risk"],
             ["Malaysia", "Tier 2", "Nvidia (H100/H200)", "0.15 (relative to US)", "US import caps + energy grid"],
         ]),
    ],
    notes=[
        "Reuters (2024), 'ByteDance orders 100,000 Huawei AI chips'.",
        "BIS (November 10, 2025), 'Implementation of the Affiliates Rule'.",
        "South Korea Ministry of Science and ICT (2025), 'AI Semiconductor Strategy 2030'.",
        "MIDA (2025), 'Malaysia Data Center Investment Report'.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapter VI ter",
    filename="Chapter_VI_ter_Asia_China_EN.docx"
)

# ---------------------------------------------------------------------------
# Content - FRENCH (Reference)
# ---------------------------------------------------------------------------

FR = LangPack(
    code="FR",
    label="CHAPITRE VI TER",
    title="Consequences pour l'Asie et la Chine",
    intro=(
        "L'Asie est la cible principale et la premiere victime du protectionnisme IA americain. "
        "Ce chapitre analyse les consequences du regime de containment sur la Chine, la pression "
        "sur les allies 'Tier 1' (Japon, Coree du Sud, Taiwan), et l'emergence de l'Asie du Sud-Est "
        "comme hub de compute secondaire. L'analyse met en lumiere le passage d'une logique "
        "d'interdependance a une logique de decouplage total."
    ),
    sections=[
        ("6ter.1 La Chine : resilience sous containment maximum", []),
        ("6ter.1.1 L'impact du decouplage hardware total", [
            "La Chine fait face aux restrictions les plus severes de l'histoire. Depuis les regles d'octobre 2022 et 2023, completees par les restrictions 'Superchips' de juin 2025, l'acces chinois aux accelerateurs IA avances (Nvidia H100, B200) est de facto interdit. En avril 2026, le ratio CACI Power Mode US/Chine est de 2,14:1, un ecart significatif qui mesure l'efficacite du containment (chapitre III).",
            "Cette asymetrie force la Chine vers une strategie de substitution hardware. Huawei (Ascend 910C), Biren et Moore Threads developpent des accelerateurs nationaux qui, bien qu'ayant 1 a 2 generations de retard sur Nvidia, permettent l'entrainement de Large Language Models (LLM). ByteDance a notamment passe commande de 100 000 puces Ascend 910B en 2024 pour compenser la penurie de H100.[1] Cependant, le rendement des noeuds 7nm et 5nm de SMIC reste limite par l'absence de lithographie EUV (interdiction d'export ASML), creant un plafond de verre structurel pour la souverainete hardware chinoise.",
        ]),
        ("6ter.1.2 Reorientation vers le 'Global South Compute'", [
            "En reponse au containment domestique, la Chine deploie une strategie d'internationalisation du compute. Le projet ByteDance-Pecem au Bresil (38 Md USD, chapitre VI bis) et les investissements en Malaisie (hub de Johor) illustrent cette volonte de construire une 'Geographic Redundancy' pour le compute chinois. En installant des data centers dans des pays Tier 2 (Malaisie, Bresil, EAU), les acteurs chinois cherchent a contourner les controles a l'exportation directs, meme si l'Affiliates Rule US (novembre 2025) cherche a fermer cette breche en etendant les restrictions aux filiales etrangeres d'entites listees.[2]",
        ]),
        ("6ter.2 Les allies Tier 1 : Japon, Coree du Sud, Taiwan", []),
        ("6ter.2.1 Taiwan : la fab geopolitique sous pression", [
            "Taiwan (TSMC) produit 92% des semi-conducteurs les plus avances au monde. Sous le protectionnisme US, Taiwan subit une double pression : (i) le 'hollowing out' de sa production vers les US (Arizona Fabs) pour satisfaire les exigences de resilience americaines, et (ii) le durcissement des controles a l'exportation vers la Chine, son premier partenaire commercial. La 'Geographic Diversity' requise par les US (chapitre IV) cree un risque de dilution industrielle pour Taiwan, tout en augmentant le cout des puces pour son ecosysteme domestique.",
        ]),
        ("6ter.2.2 Japon et Coree du Sud : le pari du RISC-V et de la fonderie alternative", [
            "Le Japon (Rapidus) et la Coree du Sud (Samsung) investissent massivement pour briser le duopole TSMC/Nvidia. Le Japon a lance le 'LSTC' (Leading-edge Semiconductor Technology Center) pour developper des puces 2nm d'ici 2027. La Coree du Sud, via la 'AI Semiconductor Strategy', vise a capturer 80% du marche de la memoire IA (HBM3e/4) d'ici 2030.[3] Pour ces allies, le protectionnisme US est une arme a double tranchant : il offre un acces protege au marche US (Tier 1) mais impose un alignement sur les controles a l'exportation qui degrade leurs relations avec la Chine.",
        ]),
        ("6ter.3 L'Asie du Sud-Est : le nouveau 'Middle Ground'", [
            "La Malaisie (Johor), le Vietnam et l'Indonesie emergent comme les nouvelles destinations privilegiees pour les data centers. La Malaisie a attire plus de 15 milliards USD d'investissements en data centers en 2024-2025 (Microsoft, Google, ByteDance, Nvidia/YTL).[4] Ces pays profitent de leur statut Tier 2 pour accueillir a la fois des infrastructures americaines et chinoises, creant un 'Non-alignement du compute' similaire au Bresil, mais avec une proximite beaucoup plus grande avec la supply chain chinoise.",
        ]),
        ("6ter.4 Synthese : vers un compute asiatique fragmente", [
            "L'Asie se fracture en trois zones distinctes : une 'Zone Chinoise Souveraine' (substitution hardware, investissement d'Etat massif), une 'Zone Pro-US Tier 1' (fonderie de pointe, alignement total), et une 'Zone Emergente Tier 2' (hub d'arbitrage, dualite US-Chine). Cette fragmentation augmente la complexite des supply chains mondiales et rencherit significativement le cout marginal du compute pour l'ensemble de la region.",
        ]),
    ],
    tables=[
        ("Tableau 18. Comparaison des capacites hardware IA en Asie (avril 2026).",
         "Source : construction de l'auteur, calibration sur le tableau de bord public.",
         [
             ["Pays/Region", "Statut US", "Hardware principal", "CACI Power Mode (est.)", "Contrainte strategique"],
             ["Chine", "Tier 3", "Huawei Ascend, Biren", "0,47 (relatif US)", "Rendement SMIC (plafond 7nm)"],
             ["Taiwan", "Tier 1", "TSMC (Nvidia/AMD)", "0,85 (relatif US)", "Offshoring force par la resilience"],
             ["Japon", "Tier 1", "Rapidus/Nvidia", "0,62 (relatif US)", "Cout energie + risque execution 2nm"],
             ["Malaisie", "Tier 2", "Nvidia (H100/H200)", "0,15 (relatif US)", "Caps d'importation US + reseau electrique"],
         ]),
    ],
    notes=[
        "Reuters (2024), 'ByteDance orders 100,000 Huawei AI chips'.",
        "BIS (10 novembre 2025), 'Implementation of the Affiliates Rule'.",
        "Ministere de la Science et des TIC de Coree du Sud (2025), 'AI Semiconductor Strategy 2030'.",
        "MIDA (2025), 'Malaysia Data Center Investment Report'.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapitre VI ter",
    filename="Chapitre_VI_ter_Asie_Chine_FR.docx"
)

# ---------------------------------------------------------------------------
# Content - PORTUGUESE (BRAZIL)
# ---------------------------------------------------------------------------

BR = LangPack(
    code="PT-BR",
    label="CAPITULO VI TER",
    title="Consequencias para a Asia e a China",
    intro=(
        "A Asia e o principal alvo e a primeira vitima do protecionismo de IA americano. "
        "Este capitulo analisa as consequencias do regime de contencao sobre a China, a "
        "pressao sobre os aliados 'Tier 1' (Japao, Coreia do Sul, Taiwan) e a emergencia "
        "do Sudeste Asiatico como um hub de computacao secundario. A analise destaca a "
        "transicao de uma logica de interdependencia para uma logica de desacoplamento total."
    ),
    sections=[
        ("6ter.1 China: resiliencia sob contencao maxima", []),
        ("6ter.1.1 O impacto do desacoplamento total de hardware", [
            "A China enfrenta as restricoes mais severas da historia. Desde as regras de outubro de 2022 e 2023, complementadas pelas restricoes 'Superchips' de junho de 2025, o acesso chines a aceleradores de IA avancados (Nvidia H100, B200) e de fato proibido. Em abril de 2026, a razao CACI Power Mode EUA/China e de 2,14:1, uma lacuna significativa que mede a eficacia da contencao (Capitulo III).",
            "Esta assimetria forca a China a uma estrategia de substituicao de hardware. Huawei (Ascend 910C), Biren e Moore Threads estao desenvolvendo aceleradores nacionais que, embora estejam de 1 a 2 geracoes atras da Nvidia, permitem o treinamento de Grandes Modelos de Linguagem (LLMs). A ByteDance encomendou notavelmente 100.000 chips Ascend 910B em 2024 para compensar a escassez de H100.[1] No entanto, o rendimento dos nos de 7nm e 5nm da SMIC continua limitado pela falta de litografia EUV (proibicao de exportacao da ASML), criando um teto estrutural para a soberania de hardware chinesa.",
        ]),
        ("6ter.1.2 Reorientacao para o 'Global South Compute'", [
            "Em resposta a contencao domestica, a China esta implantando uma estrategia internacional de computacao. O projeto ByteDance-Pecem no Brasil (38 bilhoes de USD, Capitulo VI bis) e os investimentos na Malasia (hub de Johor) ilustram esse desejo de construir 'Redundancia Geografica' para a computacao chinesa. Ao instalar data centers em paises Tier 2 (Malasia, Brasil, Emirados Arabes Unidos), os atores chineses buscam contornar os controles de exportacao diretos, mesmo que a 'Affiliates Rule' dos EUA (novembro de 2025) busque fechar essa brecha ao estender as restricoes a subsidiarias estrangeiras de entidades listadas.[2]",
        ]),
        ("6ter.2 Os Aliados Tier 1: Japao, Coreia do Sul, Taiwan", []),
        ("6ter.2.1 Taiwan: a fab geopolitica sob pressao", [
            "Taiwan (TSMC) produz 92% dos semicondutores mais avancados do mundo. Sob o protecionismo dos EUA, Taiwan esta sob dupla pressao: (i) o 'esvaziamento' de sua producao em direcao aos EUA (Arizona Fabs) para satisfazer os requisitos de resiliencia americanos, e (ii) o endurecimento dos controles de exportacao em direcao a China, seu principal parceiro comercial. A 'Diversidade Geografica' exigida pelos EUA (Capitulo IV) cria um risco de diluicao industrial para Taiwan, ao mesmo tempo em que aumenta o custo dos chips para seu ecossistema domestico.",
        ]),
        ("6ter.2.2 Japao e Coreia do Sul: a aposta no RISC-V e na fundicao alternativa", [
            "O Japao (Rapidus) e a Coreia do Sul (Samsung) estao investindo massivamente para quebrar o duopolio TSMC/Nvidia. O Japao lancou o 'LSTC' (Leading-edge Semiconductor Technology Center) para desenvolver chips de 2nm ate 2027. A Coreia do Sul, por meio da 'AI Semiconductor Strategy', visa capturar 80% do mercado de memoria de IA (HBM3e/4) ate 2030.[3] Para esses aliados, o protecionismo dos EUA e uma faca de dois gumes: oferece acesso protegido ao mercado dos EUA (Tier 1), mas impoe um alinhamento nos controles de exportacao que prejudica suas relacoes com a China.",
        ]),
        ("6ter.3 Sudeste Asiatico: o novo 'Middle Ground'", [
            "A Malasia (Johor), o Vietna e a Indonesia estao emergindo como os novos destinos preferidos para data centers. A Malasia atraiu mais de 15 bilhoes de USD em investimentos em data centers em 2024-2025 (Microsoft, Google, ByteDance, Nvidia/YTL).[4] Esses paises aproveitam seu status Tier 2 para hospedar infraestrutura americana e chinesa, criando um 'Nao-Alinhamento de Computacao' semelhante ao do Brasil, mas com uma proximidade muito maior com a cadeia de suprimentos chinesa.",
        ]),
        ("6ter.4 Sintese: rumo a uma computacao asiatica fragmentada", [
            "A Asia esta se fraturando em tres zonas distintas: uma 'Zona Chinesa Soberana' (substituicao de hardware, investimento estatal massivo), uma 'Zona Pro-EUA Tier 1' (fundicao de ponta, alinhamento total) e uma 'Zona Emergente Tier 2' (hub de arbitragem, dualidade EUA-China). Essa fragmentacao aumenta a complexidade das cadeias de suprimentos globais e eleva significativamente o custo marginal da computacao para toda a regiao.",
        ]),
    ],
    tables=[
        ("Tabela 18. Comparacao de capacidades de hardware de IA na Asia (abril de 2026).",
         "Fonte: Construcao do autor, calibracao no painel publico.",
         [
             ["Pais/Regiao", "Status EUA", "Hardware Principal", "CACI Power Mode (est.)", "Restricao Estrategica"],
             ["China", "Tier 3", "Huawei Ascend, Biren", "0,47 (relativo aos EUA)", "Rendimento da SMIC (teto de 7nm)"],
             ["Taiwan", "Tier 1", "TSMC (Nvidia/AMD)", "0,85 (relativo aos EUA)", "Offshoring forcado pela resiliencia"],
             ["Japao", "Tier 1", "Rapidus/Nvidia", "0,62 (relatifo aos EUA)", "Custo de energia + risco de execucao 2nm"],
             ["Malasia", "Tier 2", "Nvidia (H100/H200)", "0,15 (relativo aos EUA)", "Limites de importacao EUA + rede eletrica"],
         ]),
    ],
    notes=[
        "Reuters (2024), 'ByteDance encomenda 100.000 chips de IA da Huawei'.",
        "BIS (10 de novembro de 2025), 'Implementacao da Affiliates Rule'.",
        "Ministerio da Ciencia e TIC da Coreia do Sul (2025), 'Estrategia de Semicondutores de IA 2030'.",
        "MIDA (2025), 'Relatorio de Investimento em Data Centers na Malasia'.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Capitulo VI ter",
    filename="Capitulo_VI_ter_Asia_China_PT-BR.docx"
)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

LANGS = [EN, FR, BR]

def build_all(out_dir: Path) -> None:
    for lp in LANGS:
        log.info("Building Chapter VI ter [%s] -> %s", lp.code, lp.filename)
        doc = init_document()
        # Figures
        fig_dir = out_dir / "figures_ch6"
        
        # Build document
        add_cover(doc, lang=lp.code, chapter_label=lp.label, chapter_subtitle=lp.title)
        add_chapter_header(doc, label=lp.label, title=lp.title, intro=lp.intro)
        
        for title, paragraphs in lp.sections:
            render_section(doc, title, paragraphs)
            
            # Insert images after specific sections
            if title.startswith("6ter.1 "):
                img_path = fig_dir / f"Fig_6ter.1_Asia_Tiers_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
            elif title.startswith("6ter.2"):
                img_path = fig_dir / f"Fig_6ter.2_China_Paradox_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
        for caption, source, rows in lp.tables:
            render_table(doc, lang=lp.code, caption=caption, source=source, rows=rows)
        render_notes(doc, lang=lp.code, notes=lp.notes)
        render_license(doc, lang=lp.code, page_footer=lp.footer)
        
        out = out_dir / lp.filename
        doc.save(out)
        log.info("Saved %s", out)

if __name__ == "__main__":
    build_all(Path(__file__).parent)
