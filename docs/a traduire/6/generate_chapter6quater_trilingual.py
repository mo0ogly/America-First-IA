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

Chapter VI quater - Consequences for Africa - trilingual generator.

Generates the .docx for Chapter VI quater in English, French, and Brazilian Portuguese.
All content is aligned with the April 2026 dashboard snapshot.

Author: Fabrice Pizzi (Université Paris-Sorbonne, M2 Intelligence Économique).
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
log = logging.getLogger("chapter6quater_trilingual")

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
    label="CHAPTER VI QUATER",
    title="Consequences for Africa",
    intro=(
        "Africa represents the next frontier of the AI economy. While the region currently "
        "has the lowest compute density in the world, its demographic potential and renewable "
        "energy assets make it a strategic terrain for the next decade. This chapter analyzes "
        "the impact of US protectionism on the African 'Compute Leapfrog', the infrastructure "
        "competition between the US and China, and the risk of a new digital divide."
    ),
    sections=[
        ("6quater.1 The African 'Compute Leapfrog' challenge", []),
        ("6quater.1.1 Infrastructure deficit and potential", [
            "Africa represents less than 1% of global colocation data center capacity in 2025.[1] However, the demand for local compute is exploding, driven by the digitization of financial services (M-Pesa, Flutterwave) and the need for model localization (African languages, specific socio-economic contexts). South Africa (Cape Town, Johannesburg), Nigeria (Lagos), and Kenya (Nairobi) are the primary hubs.",
            "American AI protectionism (Tier 2 status for the entire continent) creates an entry barrier: African startups and governments have access to the US cloud, but building local sovereign infrastructure is hampered by GPU import caps and the high cost of capital. This reinforces a 'Cloud Dependency' that captures value toward US hyperscalers.",
        ]),
        ("6quater.1.2 Renewable energy: Africa's comparative advantage", [
            "Like Brazil, Africa possesses massive renewable energy potential (solar in the Sahel, hydroelectric in Central Africa, wind in the Maghreb). Data center projects like the 'Green Africa Compute' initiative seek to use this energy to host sustainable AI infrastructure. However, the lack of transmission grids and the instability of the business climate remain major obstacles to attracting the necessary multi-billion dollar investments.",
        ]),
        ("6quater.2 US-China Rivalry in Africa", []),
        ("6quater.2.1 China's 'Digital Silk Road'", [
            "China is the primary provider of telecommunications infrastructure in Africa (Huawei, ZTE). Through the 'Digital Silk Road', Beijing offers integrated packages including connectivity, data centers, and AI solutions. In April 2026, Huawei is the leader in private cloud infrastructure in more than 20 African countries.[2] For many governments, the Chinese offer is more attractive because it is less restrictive than the American Tier 2 status and often accompanied by preferential financing.",
        ]),
        ("6quater.2.2 The US response: the 'Digital Africa' initiative", [
            "The United States seeks to counter Chinese influence through the 'Digital Africa' initiative (part of the PGI), promoting American standards of data governance and security. Microsoft and Google have announced 'AI Centers of Excellence' in Nairobi and Accra.[3] However, US protectionism, by limiting hardware access, paradoxically pushes African actors to accept Chinese hardware, even if they use American software/models.",
        ]),
        ("6quater.3 Synthesis: toward an 'Agentic' or 'Passive' Africa?", [
            "The strategic challenge for Africa is to avoid a 'Passive AI' scenario, where the continent remains a simple consumer of American or Chinese models and a provider of training data (task labeling). An 'Agentic AI' scenario requires the development of local compute hubs, the training of local talent (L(r) factor), and the creation of a 'Sovereign African Cloud' to protect data and culture. US protectionism makes this trajectory more difficult but could catalyze regional cooperation within the African Union.",
        ]),
    ],
    tables=[
        ("Table 19. Emerging AI hubs in Africa (April 2026).",
         "Source: Author's compilation from African Digital Economy Report.",
         [
             ["Country", "Primary Hub", "Major Actors", "Compute Asset", "Main Risk"],
             ["South Africa", "Cape Town", "AWS, Microsoft, Teraco", "Advanced electrical grid (but unstable)", "Brain drain to Europe/US"],
             ["Nigeria", "Lagos", "MainOne, Medallion, Google", "Massive market + young talent", "Energy cost + currency volatility"],
             ["Kenya", "Nairobi", "Microsoft, Google, Safaricom", "Connectivity + mobile fintech leader", "Tier 2 import caps"],
             ["Egypt", "Cairo", "Orange, Telecom Egypt", "Strategic location (cables) + solar", "Regulatory complexity"],
         ]),
    ],
    notes=[
        "Xalam Analytics (2025), 'The State of African Data Centers'.",
        "International Institute for Strategic Studies (IISS, 2025), 'China's Digital Silk Road in Africa'.",
        "USAID (2025), 'Digital Africa Initiative Progress Report'.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapter VI quater",
    filename="Chapter_VI_quater_Africa_EN.docx"
)

# ---------------------------------------------------------------------------
# Content - FRENCH (Reference)
# ---------------------------------------------------------------------------

FR = LangPack(
    code="FR",
    label="CHAPITRE VI QUATER",
    title="Consequences pour l'Afrique",
    intro=(
        "L'Afrique represente la prochaine frontiere de l'economie de l'IA. Si la region dispose "
        "actuellement de la densite de compute la plus faible au monde, son potentiel demographique "
        "et ses atouts en energies renouvelables en font un terrain strategique pour la prochaine decennie. "
        "Ce chapitre analyse l'impact du protectionnisme US sur le 'Compute Leapfrog' africain, la "
        "competition infrastructurelle entre les US et la Chine, et le risque d'une nouvelle fracture numerique."
    ),
    sections=[
        ("6quater.1 Le defi du 'Compute Leapfrog' africain", []),
        ("6quater.1.1 Deficit infrastructurel et potentiel", [
            "L'Afrique represente moins de 1% de la capacite mondiale de data centers en colocation en 2025.[1] Cependant, la demande pour le compute local explose, portee par la numerisation des services financiers (M-Pesa, Flutterwave) et le besoin de localisation des modeles (langues africaines, contextes socio-economiques specifiques). L'Afrique du Sud (Le Cap, Johannesburg), le Nigeria (Lagos) et le Kenya (Nairobi) sont les principaux hubs.",
            "Le protectionnisme IA americain (statut Tier 2 pour l'ensemble du continent) cree une barriere a l'entree : les startups et gouvernements africains ont acces au cloud US, mais la construction d'infrastructures souveraines locales est freinee par les caps d'importation de GPU et le cout eleve du capital. Cela renforce une 'Cloud Dependency' qui capture la valeur vers les hyperscalers US.",
        ]),
        ("6quater.1.2 Energies renouvelables : l'avantage comparatif africain", [
            "Comme le Bresil, l'Afrique possede un potentiel massif en energies renouvelables (solaire au Sahel, hydroelectrique en Afrique Centrale, eolien au Maghreb). Des projets de data centers comme l'initiative 'Green Africa Compute' cherchent a utiliser cette energie pour heberger des infrastructures IA durables. Cependant, le manque de reseaux de transport et l'instabilite du climat des affaires restent des obstacles majeurs pour attirer les investissements de plusieurs milliards de dollars necessaires.",
        ]),
        ("6quater.2 Rivalite US-Chine en Afrique", []),
        ("6quater.2.1 La 'Route de la Soie Numerique' chinoise", [
            "La Chine est le premier fournisseur d'infrastructures de telecommunications en Afrique (Huawei, ZTE). Via la 'Digital Silk Road', Pekin propose des packages integres incluant connectivite, data centers et solutions IA. En avril 2026, Huawei est le leader des infrastructures cloud privees dans plus de 20 pays africains.[2] Pour de nombreux gouvernements, l'offre chinoise est plus attractive car moins restrictive que le statut Tier 2 americain et souvent accompagnee de financements preferentiels.",
        ]),
        ("6quater.2.2 La reponse US : l'initiative 'Digital Africa'", [
            "Les Etats-Unis cherchent a contrer l'influence chinoise via l'initiative 'Digital Africa' (partie du PGI), en promouvant les standards americains de gouvernance des donnees et de securite. Microsoft et Google ont annonce des 'AI Centers of Excellence' a Nairobi et Accra.[3] Cependant, le protectionnisme US, en limitant l'acces hardware, pousse paradoxalement les acteurs africains a accepter du hardware chinois, meme s'ils utilisent des softwares/modeles americains.",
        ]),
        ("6quater.3 Synthese : vers une Afrique 'Agentique' ou 'Passive' ?", [
            "L'enjeu strategique pour l'Afrique est d'eviter un scenario d'IA Passive, ou le continent reste un simple consommateur de modeles americains ou chinois et un fournisseur de donnees d'entrainement (task labeling). Un scenario d'IA Agentique necessite le developpement de hubs de compute locaux, la formation de talents locaux (facteur L(r)), et la creation d'un 'Cloud Souverain Africain' pour proteger les donnees et la culture. Le protectionnisme US rend cette trajectoire plus difficile, mais pourrait catalyser une cooperation regionale au sein de l'Union Africaine.",
        ]),
    ],
    tables=[
        ("Tableau 19. Hubs IA emergents en Afrique (avril 2026).",
         "Source : compilation de l'auteur a partir de l'African Digital Economy Report.",
         [
             ["Pays", "Hub principal", "Acteurs majeurs", "Atout compute", "Risque principal"],
             ["Afrique du Sud", "Le Cap", "AWS, Microsoft, Teraco", "Reseau electrique avance (mais instable)", "Brain drain vers Europe/US"],
             ["Nigeria", "Lagos", "MainOne, Medallion, Google", "Marche massif + jeunes talents", "Cout energie + volatilite devise"],
             ["Kenya", "Nairobi", "Microsoft, Google, Safaricom", "Connectivite + leader fintech mobile", "Caps d'importation Tier 2"],
             ["Egypte", "Le Caire", "Orange, Telecom Egypt", "Position strategique (cables) + solaire", "Complexite reglementaire"],
         ]),
    ],
    notes=[
        "Xalam Analytics (2025), 'The State of African Data Centers'.",
        "International Institute for Strategic Studies (IISS, 2025), 'China's Digital Silk Road in Africa'.",
        "USAID (2025), 'Digital Africa Initiative Progress Report'.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapitre VI quater",
    filename="Chapitre_VI_quater_Afrique_FR.docx"
)

# ---------------------------------------------------------------------------
# Content - PORTUGUESE (BRAZIL)
# ---------------------------------------------------------------------------

BR = LangPack(
    code="PT-BR",
    label="CAPITULO VI QUATER",
    title="Consequencias para a Africa",
    intro=(
        "A Africa representa a proxima fronteira da economia da IA. Embora a regiao "
        "atualmente tenha a menor densidade de computacao do mundo, seu potencial demografico "
        "e seus ativos de energia renovavel a tornam um terreno estrategico para a proxima decada. "
        "Este capitulo analisa o impacto do protecionismo dos EUA no 'Compute Leapfrog' africano, "
        "a competicao infraestrutural entre os EUA e a China e o risco de uma nova exclusao digital."
    ),
    sections=[
        ("6quater.1 O desafio do 'Compute Leapfrog' africano", []),
        ("6quater.1.1 Deficit infraestrutural e potencial", [
            "A Africa representa menos de 1% da capacidade mundial de data centers de colocation em 2025.[1] No entanto, a demanda por computacao local esta explodindo, impulsionada pela digitalizacao dos servicos financeiros (M-Pesa, Flutterwave) e pela necessidade de localizacao de modelos (linguas africanas, contextos socioeconomicos especificos). Africa do Sul (Cidade do Cabo, Joanesburgo), Nigeria (Lagos) e Quenia (Nairóbi) sao os principais hubs.",
            "O protecionismo de IA americano (status Tier 2 para todo o continente) cria uma barreira de entrada: startups e governos africanos tem acesso a nuvem dos EUA, mas a construcao de infraestrutura soberana local e prejudicada pelos limites de importacao de GPU e pelo alto custo de capital. Isso reforca uma 'Dependencia da Nuvem' que captura valor em direcao aos hyperscalers dos EUA.",
        ]),
        ("6quater.1.2 Energia renovavel: a vantagem comparativa da Africa", [
            "Como o Brasil, a Africa possui um potencial massivo de energia renovavel (solar no Sahel, hidroeletrica na Africa Central, eolica no Magrebe). Projetos de data centers como a iniciativa 'Green Africa Compute' buscam usar essa energia para hospedar infraestrutura de IA sustentavel. No entanto, a falta de redes de transmissao e a instabilidade do clima de negocios continuam sendo grandes obstaculos para atrair os investimentos necessarios de bilhoes de dolares.",
        ]),
        ("6quater.2 Rivalidade EUA-China na Africa", []),
        ("6quater.2.1 A 'Rota da Seda Digital' da China", [
            "A China e o principal fornecedor de infraestrutura de telecomunicacoes na Africa (Huawei, ZTE). Por meio da 'Rota da Seda Digital', Pequim oferece pacotes integrados, incluindo conectividade, data centers e solucoes de IA. Em abril de 2026, a Huawei e lider em infraestrutura de nuvem privada em mais de 20 paises africanos.[2] Para muitos governos, a oferta chinesa e mais atraente porque e menos restritiva do que o status Tier 2 americano e muitas vezes acompanhada de financiamento preferencial.",
        ]),
        ("6quater.2.2 A resposta dos EUA: a iniciativa 'Digital Africa'", [
            "Os Estados Unidos buscam conter a influencia chinesa por meio da iniciativa 'Digital Africa' (parte do PGI), promovendo padroes americanos de governanca e seguranca de dados. Microsoft e Google anunciaram 'Centros de Excelencia em IA' em Nairóbi e Acra.[3] No entanto, o protecionismo dos EUA, ao limitar o acesso ao hardware, paradoxalmente empurra os atores africanos a aceitar hardware chines, mesmo que usem softwares/modelos americanos.",
        ]),
        ("6quater.3 Sintese: rumo a uma Africa 'Agentica' ou 'Passiva'?", [
            "O desafio estrategico para a Africa e evitar um cenario de IA Passiva, onde o continente continua sendo um simples consumidor de modelos americanos ou chineses e um fornecedor de dados de treinamento (task labeling). Um cenario de IA Agentica requer o desenvolvimento de hubs de computacao locais, o treinamento de talentos locais (fator L(r)) e a criacao de uma 'Nuvem Africana Soberana' para proteger dados e cultura. O protecionismo dos EUA torna essa trajetoria mais dificil, mas pode catalisar a cooperacao regional dentro da Uniao Africana.",
        ]),
    ],
    tables=[
        ("Tabela 19. Hubs de IA emergentes na Africa (abril de 2026).",
         "Fonte: Compilacao do autor a partir do African Digital Economy Report.",
         [
             ["Pais", "Hub principal", "Principais atores", "Ativo de computacao", "Principal risco"],
             ["Africa do Sul", "Cidade do Cabo", "AWS, Microsoft, Teraco", "Rede eletrica avancada (mas instavel)", "Fuga de cerebros para Europa/EUA"],
             ["Nigeria", "Lagos", "MainOne, Medallion, Google", "Mercado massivo + jovens talentos", "Custo de energia + volatilidade da moeda"],
             ["Quenia", "Nairóbi", "Microsoft, Google, Safaricom", "Conectividade + lider em fintech movel", "Limites de importacao Tier 2"],
             ["Egito", "Cairo", "Orange, Telecom Egypt", "Localizacao estrategica (cabos) + solar", "Complexidade regulatoria"],
         ]),
    ],
    notes=[
        "Xalam Analytics (2025), 'The State of African Data Centers'.",
        "International Institute for Strategic Studies (IISS, 2025), 'China's Digital Silk Road in Africa'.",
        "USAID (2025), 'Digital Africa Initiative Progress Report'.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Capitulo VI quater",
    filename="Capitulo_VI_quater_Africa_PT-BR.docx"
)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

LANGS = [EN, FR, BR]

def build_all(out_dir: Path) -> None:
    for lp in LANGS:
        log.info("Building Chapter VI quater [%s] -> %s", lp.code, lp.filename)
        doc = init_document()
        # Figures
        fig_dir = out_dir / "figures_ch6"
        
        # Build document
        add_cover(doc, lang=lp.code, chapter_label=lp.label, chapter_subtitle=lp.title)
        add_chapter_header(doc, label=lp.label, title=lp.title, intro=lp.intro)
        
        for title, paragraphs in lp.sections:
            render_section(doc, title, paragraphs)
            
            # Insert images after specific sections
            if title.startswith("6quater.1"):
                img_path = fig_dir / f"Fig_6quat.1_Africa_Deficit_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
            elif title.startswith("6quater.2"):
                img_path = fig_dir / f"Fig_6quat.2_US_China_Africa_{lp.code}.png"
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
