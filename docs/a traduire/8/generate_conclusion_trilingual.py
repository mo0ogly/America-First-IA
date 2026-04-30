"""
General Conclusion - trilingual generator.

Generates the .docx for the General Conclusion in English, French, and Brazilian Portuguese.
All content is aligned with the April 2026 dashboard snapshot.

Author: Fabrice Pizzi (Université Paris-Sorbonne, M2 Intelligence Économique).
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path

from concl_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
    add_paragraph, GREY, WD_ALIGN_PARAGRAPH,
    render_image,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("conclusion_trilingual")

@dataclass
class LangPack:
    code: str
    label: str
    title: str
    intro: str
    sections: list[tuple[str, list[str]]]
    tables: list[tuple[str, str, list[list[str]]]]
    sources_line: str
    notes: list[str]
    footer: str
    filename: str

# ---------------------------------------------------------------------------
# Content - ENGLISH
# ---------------------------------------------------------------------------

EN = LangPack(
    code="EN",
    label="GENERAL CONCLUSION",
    title="From AI Protectionism to the Recomposition of the Global Technological Order",
    intro=(
        "This conclusion synthesizes the results of the study conducted over the 2022-2026 period, "
        "validates the central hypothesis of an American AI protectionist regime, outlines the "
        "contributions to the literature, identifies limitations and research avenues, and "
        "argues the civilizational challenge represented by AI compute as a fourth factor "
        "of production. It closes with a summary table of the eleven chapters and "
        "an inventory of the primary sources mobilized."
    ),
    sections=[
        ("1. Validation of the central hypothesis", [
            "This study started from a precise hypothesis: that the Trump 2.0 administration would transform the Biden export controls into a broader protectionist regime, using AI compute as an instrument of economic and geopolitical power—an implicit 'AI for Americans First' decree. The empirical analysis conducted over the 2022-2026 period substantially validates this hypothesis.",
            "On January 15, 2026, the Trump administration simultaneously promulgated a 25 percent tariff (Section 232) on advanced AI semiconductors (Nvidia H200, AMD MI325X) for re-exports to China, and published the BIS final rule governing AI chip exports. The combination of tariffs and export controls constitutes precisely the hybrid mechanism we anticipated: a tax on access to frontier compute that generates revenue for the US Treasury while slowing down competitors, combined with unlimited domestic access that strengthens the competitive advantage of US Big Tech.[1]",
            "Furthermore, the July 2025 AI Action Plan formalizes a doctrine that goes beyond simple national security controls: exporting the complete AI stack (hardware, models, software, applications, and standards) to countries willing to join the American AI alliance, subject to compliance with US security requirements.[2] AI is no longer treated as just another technology, but as an instrument of power projection analogous to the dollar in the monetary system or oil in the energy system.",
        ]),
        ("2. Synthesis of results", []),
        ("2.1 A measurable and growing American competitive advantage", [
            "The CACI (Compute-Adjusted Competitive Index) developed in this study allows for the quantification of structural asymmetry. On the April 2026 public dashboard snapshot, the US/EU(13) operational installed compute raw ratio stands at 17.6:1, translated by a weighted geometric formula F^0.40 x L^0.20 x R^0.15 / E^0.25 into a CACI Power Mode ratio of 3.46:1. The concentration of 76.9 percent of global operational AI compute in the United States (49.9 percent including planned capacities), an annual hyperscaler capex of 660-690 billion USD (higher than Sweden's GDP), and a frontier model training cost 5 to 10 times lower than the European cost confirm this dominance. The advantage is self-reinforcing: companies with abundant access to compute capture innovation and data rents that are very difficult to catch up with later (Chapter IV).",
            "An important methodological nuance from Chapter I (Fig 1.8): the Phys/Sov decomposition rigorously calculated from the Epoch AI 'Owner' field reveals that asymmetry is differentiated by jurisdiction. The United States and China are fully sovereign over their installed compute (CACI Phys = CACI Sov). The EU is also very largely sovereign over its installed F (99.2 percent EU-owned). The extreme case is that of the UAE: 99.6 percent of Emirati F_total is held by US-side operators (Stargate UAE, Microsoft, OpenAI), causing the sovereign CACI to drop from 55.7 (Physical) to 6.0. This Phys/Sov dissociation, formalized in Chapter V section 5.9.2 under the hypothesis of the 2028 Cloud Sovereignty Mandates activation, radically transforms the reading of asymmetry: European vulnerability lies not on installed compute but on the operational layer of cloud workloads (mostly hosted on AWS/Azure/GCP).",
        ]),
        ("2.2 A three-tier protectionist architecture", [
            "The analysis reveals that American AI protectionism operates at three distinct but cumulative levels.",
            "Tier 1: Export controls (inherited from Biden, maintained and transformed by Trump). The tier system (Tier 1/2/3) segments the world based on geopolitical alignment: free access for close allies (20 countries), quantitative caps for the rest of the world, prohibition for adversaries (China, Russia). Even after the formal repeal of the AI Diffusion Rule in May 2025, regulatory uncertainty weighs on the investment decisions of Tier 2 countries (Chapter III).",
            "Tier 2: Customs tariffs (Trump innovation). The 25 percent tariff on advanced AI semiconductors (Section 232, January 2026) constitutes a rupture: export controls targeted national security, tariffs explicitly target revenue and competitive advantage. The combination of tariffs and domestic exemptions creates a direct cost differential between American and non-American companies (Chapter V).",
            "Tier 3: Capitalistic gravity. The concentration of capex (660-690 billion USD across five companies in 2026), combined with energy access (the United States accepts increased use of fossil fuels, 53.7 GW of installed DC capacity), creates a gravitational effect: investments from Japan (550 billion), the UAE, and SoftBank/Stargate converge on American soil, strengthening the compute hub without additional regulatory intervention (Chapter VI ter).",
            "A potential fourth tier is emerging on the 2028 horizon: the Cloud Sovereignty Mandates analyzed in Chapter V section 5.9. By extending the requirements of the Framework for AI Diffusion to the cloud layer, they would transform US hyperscalers operating offshore into conditional intermediaries of global compute. The European vulnerability window (operational CADA by 2027-2028 at best, US Mandates activatable in 2028) is maximal between 2028 and 2030.",
        ]),
        ("2.3 Differentiated consequences by region", [
            "Table 24 below summarizes the structural positions and specific risks of each region studied, integrating the extension to Africa developed in Chapter VI quater.",
        ]),
        ("3. Contributions of this study", [
            "This research makes five contributions to the economic and geostrategic literature.",
            "First, the analytical integration of trajectories usually treated separately—energy, semiconductors, compute, regulation, productivity—into a unified framework. Most academic works treat these dimensions separately; our analysis shows that they form a system of interdependencies where each constraint amplifies the others (energy constrains compute, compute constrains productivity, productivity determines competitiveness).",
            "Second, the proposal of the CACI (Compute-Adjusted Competitive Index), which provides a measurement framework for comparing AI competitiveness between regions by integrating available FLOPs, human capital, regulation, and energy cost according to a weighted geometric formula. While this index remains to be empirically refined, it constitutes a first attempt to synthesize the concept of compute-adjusted competitiveness identified as missing in the literature (Chapter II). The Phys/Sov extension introduced in Chapter I and formalized in Chapter V (F = F_phys x F_sov) adds a jurisdictional dimension that distinguishes physically present compute from legally controllable compute—a distinction operational as of the April 2026 snapshot (UAE 99.6 percent US-side case) and systemic under the 2028 Cloud Sovereignty Mandates regime.",
            "Third, the demonstration that American AI protectionism produces systemic paradoxical effects. Restrictions intended to maintain the US advantage accelerate the construction of an alternative Chinese ecosystem (DeepSeek, Huawei Ascend, real capacity 246-300 EFLOP/s versus 0.5 percent apparent in consolidated Epoch AI data), push Tier 2 countries toward China (ByteDance in Brazil, ASEAN, Africa), and incentivize Tier 1 allies to co-finance US supremacy rather than build true autonomy (Japan: 550 billion to the United States). AI protectionism does not produce a unipolar world but a world fragmented into technological blocs.",
            "Fourth, the unprecedented comparative analysis of regional responses to AI protectionism (Europe, South America, Asia, Africa), showing that geopolitical position, energy endowment, and proximity to value chains determine fundamentally different dependency trajectories, irreducible to a single model of catch-up or falling behind.",
            "Fifth, the extension to Africa (Chapter VI quater) documents the most extreme compute asymmetry in the world (deficit x44 to x417 depending on indicators) and shows how American protectionism creates a specific double bind for this continent: restriction of access to US frontier compute on one side, exposure to risks of surveillance and secondary sanctions from using the Chinese alternative on the other.",
        ]),
        ("4. Limitations and research avenues", [
            "This study has several limitations that should be explicitly stated.",
            "Regulatory uncertainty. The export controls environment is evolving rapidly. Biden's AI Diffusion Rule was repealed in May 2025; the Trump final rule of January 2026 could itself be modified (Commerce is to provide an update to the President by July 2026). The scenarios proposed in Chapter V reflect this uncertainty, but the space of possibilities is broader than the four formalized scenarios.",
            "Fragmentary data. AI compute data by region remains incomplete despite the rigorous April 2026 public dashboard snapshot. Epoch AI estimates significantly under-represent real Chinese capacity (China 0.5 percent apparent vs 246-300 EFLOP/s claimed) due to the anonymization of Chinese clusters and the opacity of Huawei/Cambricon/Biren providers. The CACI is an exploratory index, calibrated on the April 2026 snapshot but not yet validated over long time series.",
            "Time horizon. The analysis covers 2026-2030, but technological disruptions (quantum computing, sub-2 nm nodes, neuromorphic architectures) could redistribute the cards after 2030. Nvidia's current GPU advantage could be challenged by specialized ASICs (Google TPU, Amazon Trainium, Huawei Ascend) or radically different architectures (European DARE/RISC-V, 2030-2032 horizon).",
            "Sensitivity to CACI weightings. The weightings of the geometric formula (F^0.40 x L^0.20 x R^0.15 / E^0.25) were chosen in Chapter II based on the literature but do not stem from an econometric calibration. A systematic sensitivity analysis on these weightings could reveal alternative trajectories not explored.",
            "Future research avenues. Four extensions are required. First, the empirical calibration of the CACI on survey data (sectoral productivity by compute access) would allow for the validation or adjustment of current weightings. Second, the sectoral deepening of African coverage (Chapter VI quater)—notably the country-by-country analysis of the 16 identified national AI strategies and the implementation of the AU Continental Strategy Phase II 2028. Third, the dynamic modeling of the energy-compute-productivity interaction via computable general equilibrium (CGE) models integrating compute constraints as a production factor. Fourth, the longitudinal observation of the 2028 Cloud Sovereignty Mandates regime (if it actually activates) and its effects on the F_sov trajectory of different jurisdictions.",
        ]),
        ("5. The civilizational challenge", [
            "Beyond economic metrics and geopolitical scenarios, this study reveals a more fundamental challenge. AI compute is becoming the fourth factor of production (after capital, labor, and land/energy), structuring access to productivity gains, innovation, and ultimately prosperity. Like oil in the 20th century, the control of compute in the 21st century will determine which nations and which companies capture the rents of innovation.",
            "The United States has understood this. The July 2025 AI Action Plan explicitly treats the AI stack as an instrument of geopolitical alliance, comparable to the Marshall Plan or the Bretton Woods system: access to American compute is conditioned on strategic alignment, creating a system of hierarchical dependencies. Carnegie notes that the rule aimed to use AI exports as leverage over geopolitical pivot states, by establishing incentives for other governments to adopt American technological standards and protections in exchange for US chips.[3]",
            "Faced with this new system, France and Europe have a strategic choice that fundamentally boils down to three options. The first is subordinate integration: accepting the status of technological junior partner in the American bloc, as Japan chose by investing 550 billion USD on US soil. This option minimizes the risk of access disruption but maximizes dependency. The second is sovereignist confrontation: building an entirely autonomous AI ecosystem, as China is forced to do. This option is unrealistic by 2030 for Europe, which lacks both a sufficient semiconductor industrial base and interior market capacity.",
            "The third option—the one recommended by this study in Chapter VII—is targeted strategic autonomy. it consists of building sovereignty on the segments where Europe possesses a comparative advantage (French nuclear energy at 1.35x US PPP cost, ASML lithography equipment, Mistral open AI models, AI Act regulatory framework) while maintaining interoperability with the American ecosystem. The goal is not autarky but the capacity of choice: to have credible alternatives (SOV-3 sovereign cloud, local compute under EU jurisdiction, open models) to never be captive to a provider whose geopolitical interests might diverge from ours. The Phys/Sov distinction established in Chapter I is operational here: it is about increasing F_sov on the cloud workload layer, not just F_phys on the installed infrastructure.",
            "Time is of the essence. The tipping point identified in this study is in 2028: convergence of EU compute and energy saturation (Chapter V section 5.7.3), potential activation of Cloud Sovereignty Mandates (Chapter V section 5.9), and the probable end of the vulnerability window before positions crystallize. After this date, positions stiffen around the 17.6:1 raw / 3.46:1 CACI Power Mode baseline and dependencies become structural. The 2026-2028 strategic action window is narrow. The 109 billion EUR in AI investments announced for France, the 200 billion EUR InvestAI program, the rise of Mistral Compute, and dedicated EDF nuclear sites are the elements of a response. But between announcement and execution, there is the distance that separates strategy from reality. India promises 200 billion USD but only has 1.4 GW installed. Europe cannot afford a comparable gap between ambition and realization.",
            "Ultimately, 'AI for Americans First' is not just a trade policy scenario. It is the signal of a recomposition of the global technological order comparable to the major restructurings of the 20th century—Bretton Woods, the oil shock, the end of the Cold War. Each of these ruptures created winners and losers for decades. The question for France and Europe is no longer whether this recomposition will take place—it is underway—but to determine whether we will be its architects or its subjects.",
            "Fabrice Pizzi, Paris, February 2026.",
        ]),
    ],
    tables=[
        ("Table 24. Summary of regional consequences of American AI protectionism.",
         "Source: Author's construction, calibrated on the April 2026 snapshot (US 76.9% operational AI compute, EU raw ratio 17.6:1, CACI Power Mode 3.46:1).",
         [
             ["Region", "Structural Position", "Main Impact", "Specific Risk"],
             ["Europe / France", "Tier 1, dependent on US GPU + cloud (72-80% workloads)",
              "Compute gap 17.6:1 raw / 3.46:1 CACI; training costs x5-10",
              "Geopolitical vendor lock-in; marginalization if US-Asia bloc closes; F_sov vulnerability on cloud workloads"],
             ["South America / Brazil", "Tier 2, US-China competition ground",
              "Technological bifurcation; amplified brain drain",
              "Triple fracture (North-South, East-West, intra-regional)"],
             ["Japan / Korea / Taiwan", "Tier 1, critical value chain links",
              "Co-financing US supremacy (550B USD Japan); production transfer",
              "Asymmetric partnership; Taiwan advantage erosion; Japanese investment in US instead of EU"],
             ["India", "Tier 2, Global South pivot",
              "GPU cap tension vs compute hub ambition",
              "Applicative sovereignty without hardware sovereignty"],
             ["China", "Tier 3, forced autonomization",
              "Parallel AI ecosystem (Huawei/DeepSeek); real capacity 246-300 EFLOP/s; 2-3 gen GPU lag",
              "Permanent technological bifurcation; exporting to Tier 2/3 (Brazil, ASEAN, Africa)"],
             ["Africa", "Tier 2/3, compute deficit x44-x417",
              "Extreme asymmetry; US/China double bind",
              "Huawei/DeepSeek dependency; surveillance; structural confinement; UAE 99.6% US-side case"],
         ]),
        ("Table 25. Summary of chapters, volume, and critical apparatus of the study.",
         "Source: Author's construction. Volume (in indicative pages) includes figures and tables but excludes econometric appendices.",
         [
             ["Chapter", "Title", "Indicative Pages", "Notes"],
             ["I", "Theoretical Framework: Technological Protectionism and AI", "~12", "22"],
             ["II", "Methodology: Scenario Matrix and CACI Index", "~8", "10"],
             ["III", "Empirical Diagnosis 2020-2026: Energy, Semiconductors, Compute", "~11", "20"],
             ["IV", "Mechanisms of the US Competitive Advantage", "~9", "19"],
             ["V", "Prospective Scenarios 2026-2030 and Cloud Sovereignty Mandates", "~14", "29"],
             ["VI", "Consequences for France and Europe", "~10", "14"],
             ["VI bis", "Consequences for South America and Brazil", "~11", "19"],
             ["VI ter", "Consequences for Asia", "~12", "16"],
             ["VI quater", "Consequences for Africa", "~13", "26"],
             ["VII", "Strategic Recommendations for France and Europe", "~11", "18"],
             ["Conclusion", "From AI Protectionism to the Recomposition of the Global Technological Order", "~9", "3"],
             ["TOTAL", "11 chapters", "~120", "196"],
         ]),
    ],
    sources_line=(
        "Primary sources mobilized: IEA, McKinsey, Bruegel, Brookings, Carnegie Endowment, "
        "European Commission, White House/BIS, European Parliament, CSIS, S&P Global, Epoch AI, "
        "Centre for Future Generations (CFG), Euronews, ECLAC/CENIA (ILIA 2025), World Bank, "
        "Futurum, Introl, World Nuclear News, Arizton, Pillsbury Law, ITIF, Foreign Policy, Hudson "
        "Institute, Mordor Intelligence, McKinsey Global Institute, IMF. Additional data: "
        "Bloomberg, DCD, Morgan Lewis, Tom's Hardware, Serrari Group, Data Center Knowledge, "
        "WEF, Africa Defense Forum, Atlantic Council DFRLab, Carnegie Endowment, New Lines Institute, "
        "RTE, EDF, ANSSI, USTDA. Primary data: Epoch AI public dashboard snapshot "
        "April 2026 (https://mo0ogly.github.io/America-First-IA/dashboard/)."
    ),
    notes=[
        "Pillsbury Law (January 2026), 'Trump Admin Targets Advanced AI Semiconductors'. Section 232: 25 percent tariff on Nvidia H200, AMD MI325X for China re-export. US domestic exemptions. Simultaneous BIS final rule. DC market update scheduled July 2026.",
        "White House / CM Trade Law (July 2025), 'America's AI Action Plan'. Pillar III: export the full AI technology stack to allies. Four principles: export to allies, enforcement strengthening, global alignment, measures protection.",
        "Carnegie Endowment for International Peace (May 2025), 'The Trump Administration May Be About to Repeal the AI Diffusion Rule'. Analysis of the control/promotion/leverage trilemma. Recommendation: broaden Tier 1 group, increase India allocations, strengthen localization requirements.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - General Conclusion",
    filename="General_Conclusion_EN.docx"
)

# ---------------------------------------------------------------------------
# Content - FRENCH (Reference)
# ---------------------------------------------------------------------------

FR = LangPack(
    code="FR",
    label="CONCLUSION GENERALE",
    title="Du protectionnisme IA a la recomposition de l'ordre technologique mondial",
    intro=(
        "Cette conclusion synthetise les resultats de l'etude conduite sur la periode 2022-2026, "
        "valide l'hypothese centrale d'un regime protectionniste IA americain, expose les "
        "contributions a la litterature, identifie les limites et pistes de recherche, et "
        "argumente l'enjeu de civilisation que represente le compute IA comme quatrieme facteur "
        "de production. Elle se cloture par le tableau recapitulatif des onze chapitres et "
        "l'inventaire des sources principales mobilisees."
    ),
    sections=[
        ("1. Validation de l'hypothese centrale", [
            "Cette etude partait d'une hypothese precise : l'administration Trump 2.0 transformerait les controles a l'export Biden en un regime protectionniste plus large, utilisant le compute IA comme instrument de puissance economique et geopolitique - un decret implicite AI for Americans First. L'analyse empirique conduite sur la periode 2022-2026 valide cette hypothese de maniere substantielle.",
            "Le 15 janvier 2026, l'administration Trump a simultanement promulgue un tarif de 25 pour cent (Section 232) sur les semi-conducteurs IA avances (Nvidia H200, AMD MI325X) pour les reexportations vers la Chine, et publie la regle finale BIS regissant les exportations de puces IA. La combinaison tarifs plus controles a l'export constitue precisement le mecanisme hybride que nous anticipions : une taxe sur l'acces au compute de pointe qui genere des revenus pour le Tresor americain tout en ralentissant les concurrents, combinee a un acces domestique illimite qui renforce l'avantage competitif des Big Tech US.[1]",
            "Plus encore, l'AI Action Plan de juillet 2025 formalise une doctrine qui depasse les simples controles de securite nationale : exporter le stack IA complet (hardware, modeles, logiciels, applications et standards) aux pays disposes a rejoindre l'alliance IA americaine, sous condition de conformite aux exigences de securite US.[2] L'IA n'est plus traitee comme une technologie parmi d'autres, mais comme un instrument de projection de puissance analogue au dollar dans le systeme monetaire ou au petrole dans le systeme energetique.",
        ]),
        ("2. Synthese des resultats", []),
        ("2.1 Un avantage competitif americain mesurable et croissant", [
            "L'indice CACI (Compute-Adjusted Competitive Index) developpe dans cette etude permet de quantifier l'asymetrie structurelle. Sur le snapshot du tableau de bord public d'avril 2026, le ratio brut compute installe operationnel US/UE(13) s'etablit a 17,6:1, traduit par une formule geometrique ponderee F^0,40 x L^0,20 x R^0,15 / E^0,25 en un ratio CACI Power Mode de 3,46:1. La concentration de 76,9 pour cent du compute IA operationnel mondial aux Etats-Unis (49,9 pour cent en incluant les capacites planifiees), un capex annuel des hyperscalers de 660-690 milliards USD (superieur au PIB de la Suede), et un cout de training des modeles frontier 5 a 10 fois inferieur au cout europeen confirment cette domination. L'avantage est auto-renforcant : les entreprises disposant d'un acces abondant au compute captent des rentes d'innovation et de donnees qui sont tres difficiles a rattraper ensuite (chapitre IV).",
            "Une nuance methodologique importante issue du chapitre I (Fig 1.8) : la decomposition Phys/Sov rigoureusement calculee a partir du champ Owner d'Epoch AI revele que l'asymetrie est differenciee selon les juridictions. Les Etats-Unis et la Chine sont integralement souverains sur leur compute installe (CACI Phys = CACI Sov). L'UE est aussi tres largement souveraine sur son F installe (99,2 pour cent UE-owned). Le cas extreme est celui des Emirats arabes unis : 99,6 pour cent du F_total emirati est detenu par des operateurs US-side (Stargate UAE, Microsoft, OpenAI), faisant chuter le CACI souverain de 55,7 (Physique) a 6,0. Cette dissociation Phys/Sov, formalisee au chapitre V section 5.9.2 sous l'hypothese d'activation des Cloud Sovereignty Mandates 2028, transforme radicalement la lecture de l'asymetrie : la vulnerabilite europeenne se situe non sur le compute installe mais sur la couche operationnelle des charges cloud (majoritairement hebergees sur AWS/Azure/GCP).",
        ]),
        ("2.2 Une architecture protectionniste a trois etages", [
            "L'analyse revele que le protectionnisme IA americain opere a trois niveaux distincts mais cumulatifs.",
            "Premier etage : les controles a l'export (herites de Biden, maintenus et transformes par Trump). Le systeme de tiers (Tier 1/2/3) segmente le monde en fonction de l'alignement geopolitique : acces libre pour les allies proches (20 pays), caps quantitatifs pour le reste du monde, interdiction pour les adversaires (Chine, Russie). Meme apres l'abrogation formelle de l'AI Diffusion Rule en mai 2025, l'incertitude reglementaire pese sur les decisions d'investissement des pays Tier 2 (chapitre III).",
            "Deuxieme etage : les tarifs douaniers (innovation Trump). Le tarif de 25 pour cent sur les semi-conducteurs IA avances (Section 232, janvier 2026) constitue une rupture : les controles a l'export visaient la securite nationale, les tarifs visent explicitement les revenus et l'avantage concurrentiel. La combinaison tarifs plus exemptions domestiques cree un differentiel de cout direct entre entreprises americaines et non-americaines (chapitre V).",
            "Troisieme etage : la gravite capitalistique. La concentration du capex (660-690 milliards USD chez cinq entreprises en 2026), combinee a l'acces energetique (les Etats-Unis acceptent un recours accru aux fossiles, 53,7 GW de capacite DC installee), cree un effet gravitationnel : les investissements japonais (550 milliards), des Emirats, de SoftBank/Stargate convergent vers le sol americain, renforcant le hub compute sans intervention reglementaire supplementaire (chapitre VI ter).",
            "Un quatrieme etage potentiel se profile a l'horizon 2028 : les Cloud Sovereignty Mandates analyses au chapitre V section 5.9. En etendant les obligations du Framework for AI Diffusion a la couche cloud, ils transformeraient les hyperscalers US operant offshore en intermediaires conditionnels du compute mondial. La fenetre de vulnerabilite europeenne (CADA operationnel au mieux 2027-2028, Mandates US activables 2028) est maximale entre 2028 et 2030.",
        ]),
        ("2.3 Consequences differenciees par region", [
            "Le Tableau 24 ci-apres synthetise les positions structurelles et les risques specifiques de chaque region etudiee, en integrant l'extension a l'Afrique developpee au chapitre VI quater.",
        ]),
        ("3. Contributions de cette etude", [
            "Cette recherche apporte cinq contributions a la litterature economique et geostrategique.",
            "Premierement, l'integration analytique de trajectoires habituellement traitees separement - energie, semi-conducteurs, compute, regulation, productivite - dans un cadre unifie. L'essentiel des travaux academiques traite separement ces dimensions ; notre analyse montre qu'elles forment un systeme d'interdependances ou chaque contrainte amplifie les autres (l'energie contraint le compute, le compute contraint la productivite, la productivite determine la competitivite).",
            "Deuxiemement, la proposition de l'indice CACI (Compute-Adjusted Competitive Index), qui offre un cadre de mesure pour comparer la competitivite IA entre regions en integrant FLOPs disponibles, capital humain, regulation et cout energetique selon une formule geometrique ponderee. Si cet indice reste a affiner empiriquement, il constitue une premiere tentative de synthetiser le concept de compute-adjusted competitiveness identifie comme manquant dans la litterature (chapitre II). L'extension Phys/Sov introduite au chapitre I et formalisee au chapitre V (F = F_phys x F_sov) ajoute une dimension juridictionnelle qui distingue le compute physiquement present du compute legalement controlable - distinction operationnelle des le snapshot avril 2026 (cas EAU 99,6 pct US-side) et systemique sous regime Cloud Sovereignty Mandates 2028.",
            "Troisiemement, la demonstration que le protectionnisme IA americain produit des effets paradoxaux systemiques. Les restrictions destinees a maintenir l'avantage US accelerent la construction d'un ecosysteme chinois alternatif (DeepSeek, Huawei Ascend, capacite reelle 246-300 EFLOP/s contre 0,5 pct apparent dans les donnees Epoch AI consolidees), poussent les pays Tier 2 vers la Chine (ByteDance au Bresil, en ASEAN, en Afrique), et incitent les allies Tier 1 a co-financer la suprematie US plutot qu'a construire une autonomie veritable (Japon : 550 milliards vers les Etats-Unis). Le protectionnisme IA ne produit pas un monde unipolaire mais un monde fragmente en blocs technologiques.",
            "Quatriemement, l'analyse comparative inedite des reponses regionales au protectionnisme IA (Europe, Amerique du Sud, Asie, Afrique), montrant que la position geopolitique, la dotation energetique et la proximite avec les chaines de valeur determinent des trajectoires de dependance fondamentalement differentes, irreductibles a un modele unique de rattrapage ou de decrochage.",
            "Cinquiemement, l'extension a l'Afrique (chapitre VI quater) documente l'asymetrie compute la plus extreme au monde (deficit x44 a x417 selon les indicateurs) et montre comment le protectionnisme americain cree pour ce continent un double bind specifique : restriction d'acces au compute frontier US d'un cote, exposition aux risques de surveillance et de sanctions secondaires du recours a l'alternative chinoise de l'autre.",
        ]),
        ("4. Limites et pistes de recherche", [
            "Cette etude comporte plusieurs limites qu'il convient d'expliciter.",
            "Incertitude reglementaire. L'environnement des export controls evolue rapidement. L'AI Diffusion Rule de Biden a ete abrogee en mai 2025 ; la regle finale Trump de janvier 2026 pourrait elle-meme etre modifiee (Commerce doit fournir une mise a jour au President d'ici juillet 2026). Les scenarios proposes au chapitre V refletent cette incertitude, mais l'espace des possibles est plus large que les quatre scenarios formalises.",
            "Donnees fragmentaires. Les donnees de compute IA par region restent incompletes malgre le snapshot rigoureux du tableau de bord public d'avril 2026. Les estimations Epoch AI sous-representent significativement la capacite chinoise reelle (Chine 0,5 pct apparent vs 246-300 EFLOP/s revendiques) en raison de l'anonymisation des clusters chinois et de l'opacite des fournisseurs Huawei/Cambricon/Biren. Le CACI est un indice exploratoire, calibre sur le snapshot avril 2026 mais non encore valide sur series temporelles longues.",
            "Horizon temporel. L'analyse porte sur 2026-2030, mais des ruptures technologiques (quantum computing, noeuds sub-2 nm, architectures neuromorphiques) pourraient redistribuer les cartes apres 2030. L'avantage actuel de Nvidia en GPU pourrait etre conteste par des ASIC specialises (Google TPU, Amazon Trainium, Huawei Ascend) ou des architectures radicalement differentes (DARE/RISC-V europeen, horizon 2030-2032).",
            "Sensibilite aux ponderations CACI. Les ponderations de la formule geometrique (F^0,40 x L^0,20 x R^0,15 / E^0,25) ont ete choisies au chapitre II en fonction de la litterature mais ne sont pas issues d'une calibration econometrique. Une analyse de sensibilite systematique sur ces ponderations pourrait reveler des trajectoires alternatives non explorees.",
            "Pistes de recherche futures. Quatre prolongements s'imposent. Premierement, le calibrage empirique du CACI sur donnees d'enquete (productivite sectorielle par acces au compute) permettrait de valider ou ajuster les ponderations actuelles. Deuxiemement, l'approfondissement sectoriel de la couverture Afrique (chapitre VI quater) - notamment l'analyse pays par pays des 16 strategies IA nationales recensees et de la mise en oeuvre de la Strategie continentale UA Phase II 2028. Troisiemement, la modelisation dynamique de l'interaction energie-compute-productivite via des modeles d'equilibre general calculable (CGE) integrant les contraintes de compute comme facteur de production. Quatriemement, l'observation longitudinale du regime Cloud Sovereignty Mandates 2028 (s'il s'active effectivement) et de ses effets sur la trajectoire F_sov des differentes juridictions.",
        ]),
        ("5. L'enjeu de civilisation", [
            "Au-dela des metriques economiques et des scenarios geopolitiques, cette etude revele un enjeu plus fondamental. Le compute IA est en passe de devenir le quatrieme facteur de production (apres le capital, le travail et la terre/energie), structurant l'acces aux gains de productivite, a l'innovation, et in fine a la prosperite. Comme le petrole au XXe siecle, le controle du compute au XXIe siecle determinera quelles nations et quelles entreprises captent les rentes de l'innovation.",
            "Les Etats-Unis l'ont compris. L'AI Action Plan de juillet 2025 traite explicitement le stack IA comme un instrument d'alliance geopolitique, comparable au Plan Marshall ou au systeme de Bretton Woods : l'acces au compute americain est conditionne a l'alignement strategique, creant un systeme de dependances hierarchisees. Carnegie note que la regle visait a utiliser les exportations d'IA comme levier sur les Etats pivots geopolitiques, en etablissant des incitations pour que d'autres gouvernements adoptent les standards et protections technologiques americains en echange de puces US.[3]",
            "Face a ce nouveau systeme, la France et l'Europe disposent d'un choix strategique qui se resume, au fond, a trois options. La premiere est l'integration subordonnee : accepter le statut de junior partner technologique dans le bloc americain, comme le Japon l'a choisi en investissant 550 milliards USD sur le sol US. Cette option minimise le risque de rupture d'acces mais maximise la dependance. La deuxieme est la confrontation souverainiste : construire un ecosysteme IA entierement autonome, comme la Chine y est contrainte. Cette option est irrealiste a l'horizon 2030 pour l'Europe, qui ne dispose ni de la base industrielle de semi-conducteurs ni de la capacite de marche interieur suffisantes.",
            "La troisieme option - celle que cette etude recommande au chapitre VII - est l'autonomie strategique ciblee. Elle consiste a batir une souverainete sur les segments ou l'Europe possede un avantage comparatif (energie nucleaire francaise au cout PPA 1,35x USA, equipements de lithographie ASML, modeles IA ouverts Mistral, cadre reglementaire AI Act) tout en maintenant l'interoperabilite avec l'ecosysteme americain. L'objectif n'est pas l'autarcie mais la capacite de choix : disposer d'alternatives credibles (cloud souverain SOV-3, compute local sous juridiction UE, modeles ouverts) pour ne jamais etre captif d'un fournisseur dont les interets geopolitiques pourraient diverger des notres. La distinction Phys/Sov etablie au chapitre I est ici operationnelle : il s'agit d'augmenter F_sov sur la couche des charges cloud, pas seulement F_phys sur l'infrastructure installee.",
            "Le temps presse. Le point de basculement identifie dans cette etude se situe en 2028 : convergence de la saturation compute et energie UE (chapitre V section 5.7.3), activation potentielle des Cloud Sovereignty Mandates (chapitre V section 5.9), et fin probable de la fenetre de vulnerabilite avant cristallisation des positions. Apres cette date, les positions se rigidifient autour de la baseline 17,6:1 brut / 3,46:1 CACI Power Mode et les dependances deviennent structurelles. La fenetre d'action strategique 2026-2028 est etroite. Les 109 milliards EUR d'investissements IA annonces pour la France, le programme InvestAI de 200 milliards EUR, la montee en puissance de Mistral Compute, et les sites nucleaires EDF dedies constituent les elements d'une reponse. Mais entre l'annonce et l'execution, il y a la distance qui separe la strategie du reel. L'Inde promet 200 milliards USD mais ne dispose que de 1,4 GW installe. L'Europe ne peut pas se permettre un ecart comparable entre ambition et realisation.",
            "En definitive, AI for Americans First n'est pas seulement un scenario de politique commerciale. C'est le signal d'une recomposition de l'ordre technologique mondial comparable aux grandes restructurations du XXe siecle - Bretton Woods, le choc petrolier, la fin de la guerre froide. Chacune de ces ruptures a cree des gagnants et des perdants pour des decennies. La question pour la France et l'Europe n'est plus de savoir si cette recomposition aura lieu - elle est en cours - mais de determiner si nous en serons les architectes ou les sujets.",
            "Fabrice Pizzi, Paris, fevrier 2026.",
        ]),
    ],
    tables=[
        ("Tableau 24. Synthese des consequences regionales du protectionnisme IA americain.",
         "Source : construction de l'auteur, calibration sur le snapshot avril 2026 (US 76,9 pct compute IA operationnel, ratio brut UE 17,6:1, CACI Power Mode 3,46:1).",
         [
             ["Region", "Position structurelle", "Impact principal", "Risque specifique"],
             ["Europe / France", "Tier 1, dependante GPU + cloud US (72-80 pct workloads)",
              "Compute gap 17,6:1 brut / 3,46:1 CACI ; couts training x5-10",
              "Vendor lock-in geopolitique ; marginalisation si bloc US-Asie se ferme ; vulnerabilite F_sov sur charges cloud"],
             ["Amerique du Sud / Bresil", "Tier 2, terrain de competition US-Chine",
              "Bifurcation technologique ; brain drain amplifie",
              "Triple fracture (Nord-Sud, Est-Ouest, intra-regionale)"],
             ["Japon / Coree / Taiwan", "Tier 1, maillons critiques chaine de valeur",
              "Co-financement suprematie US (550 Md USD Japon) ; transfert production",
              "Partenariat asymetrique ; erosion avantage Taiwan ; investissement japonais aux US plutot qu'en UE"],
             ["Inde", "Tier 2, pivot Sud global",
              "Tension caps GPU vs ambition hub compute",
              "Souverainete applicative sans souverainete hardware"],
             ["Chine", "Tier 3, autonomisation forcee",
              "Ecosysteme IA parallele (Huawei/DeepSeek) ; capacite reelle 246-300 EFLOP/s ; retard 2-3 generations GPU",
              "Bifurcation technologique permanente ; exportation aux Tier 2/3 (Bresil, ASEAN, Afrique)"],
             ["Afrique", "Tier 2/3, compute deficit x44-x417",
              "Asymetrie extreme ; double bind US/Chine",
              "Dependance Huawei/DeepSeek ; surveillance ; enfermement structurel ; cas EAU 99,6 pct US-side"],
         ]),
        ("Tableau 25. Recapitulatif des chapitres, volume et appareil critique de l'etude.",
         "Source : construction de l'auteur. Le volume (en pages indicatives) inclut figures et tableaux mais exclut les annexes econometriques.",
         [
             ["Chapitre", "Titre", "Pages indicatives", "Notes"],
             ["I", "Cadre theorique : protectionnisme technologique et IA", "~12", "22"],
             ["II", "Methodologie : matrice scenarielle et indice CACI", "~8", "10"],
             ["III", "Diagnostic empirique 2020-2026 : energie, semi-conducteurs, compute", "~11", "20"],
             ["IV", "Mecanismes de l'avantage competitif US", "~9", "19"],
             ["V", "Scenarios prospectifs 2026-2030 et Cloud Sovereignty Mandates", "~14", "29"],
             ["VI", "Consequences pour la France et l'Europe", "~10", "14"],
             ["VI bis", "Consequences pour l'Amerique du Sud et le Bresil", "~11", "19"],
             ["VI ter", "Consequences pour l'Asie", "~12", "16"],
             ["VI quater", "Consequences pour l'Afrique", "~13", "26"],
             ["VII", "Recommandations strategiques pour la France et l'Europe", "~11", "18"],
             ["Conclusion", "Du protectionnisme IA a la recomposition de l'ordre technologique mondial", "~9", "3"],
             ["TOTAL", "11 chapitres", "~120", "196"],
         ]),
    ],
    sources_line=(
        "Sources principales mobilisees : AIE, McKinsey, Bruegel, Brookings, Carnegie Endowment, "
        "Commission europeenne, White House/BIS, Parlement europeen, CSIS, S&P Global, Epoch AI, "
        "Centre for Future Generations (CFG), Euronews, CEPALC/CENIA (ILIA 2025), Banque mondiale, "
        "Futurum, Introl, World Nuclear News, Arizton, Pillsbury Law, ITIF, Foreign Policy, Hudson "
        "Institute, Mordor Intelligence, McKinsey Global Institute, FMI. Donnees complementaires : "
        "Bloomberg, DCD, Morgan Lewis, Tom's Hardware, Serrari Group, Data Center Knowledge, "
        "WEF, Africa Defense Forum, Atlantic Council DFRLab, Carnegie Endowment, New Lines Institute, "
        "RTE, EDF, ANSSI, USTDA. Donnees primaires : tableau de bord public Epoch AI snapshot "
        "avril 2026 (https://mo0ogly.github.io/America-First-IA/dashboard/)."
    ),
    notes=[
        "Pillsbury Law (janvier 2026), 'Trump Admin Targets Advanced AI Semiconductors'. Section 232 : tarif 25 pct sur Nvidia H200, AMD MI325X pour reexportation Chine. Exemptions domestiques US. Regle finale BIS simultanee. Mise a jour marche DC prevue juillet 2026.",
        "White House / CM Trade Law (juillet 2025), 'America's AI Action Plan'. Pilier III : exporter le full AI technology stack aux allies. Quatre principes : export aux allies, renforcement enforcement, alignement global, protection mesures.",
        "Carnegie Endowment for International Peace (mai 2025), 'The Trump Administration May Be About to Repeal the AI Diffusion Rule'. Analyse du trilemme controle/promotion/levier. Recommandation : elargir le groupe Tier 1, augmenter les allocations Inde, renforcer les exigences de localisation.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Conclusion generale",
    filename="Conclusion_Generale_FR.docx"
)

# ---------------------------------------------------------------------------
# Content - PORTUGUESE (BRAZIL)
# ---------------------------------------------------------------------------

BR = LangPack(
    code="PT-BR",
    label="CONCLUSAO GERAL",
    title="Do Protecionismo de IA a Recomposicao da Ordem Tecnologica Mundial",
    intro=(
        "Esta conclusao sintetiza os resultados do estudo conduzido no periodo 2022-2026, "
        "valida a hipotese central de um regime protecionista de IA americano, descreve as "
        "contribuicoes para a literatura, identifica limitacoes e caminhos de pesquisa, e "
        "discute o desafio civilizacional representado pela computacao de IA como o quarto "
        "fator de producao. Encerra-se com uma tabela resumida dos onze capitulos e "
        "um inventario das principais fontes mobilizadas."
    ),
    sections=[
        ("1. Validacao da hipotese central", [
            "Este estudo partiu de uma hipotese precisa: que a administracao Trump 2.0 transformaria os controles de exportacao de Biden em um regime protecionista mais amplo, usando a computacao de IA como um instrumento de poder economico e geopolitico - um decreto implicito 'IA para Americanos Primeiro'. A analise empirica conduzida no periodo 2022-2026 valida substancialmente essa hipotese.",
            "Em 15 de janeiro de 2026, a administracao Trump promulgou simultaneamente uma tarifa de 25 por cento (Secao 232) sobre semicondutores de IA avancados (Nvidia H200, AMD MI325X) para reexportacoes para a China, e publicou a regra final do BIS que governa as exportacoes de chips de IA. A combinacao de tarifas e controles de exportacao constitui precisamente o mecanismo hibrido que antecipavamos: um imposto sobre o acesso a computacao de fronteira que gera receita para o Tesouro dos EUA enquanto retarda os concorrentes, combinado com o acesso domestico ilimitado que fortalece a vantagem competitiva das Big Techs dos EUA.[1]",
            "Alem disso, o Plano de Acao de IA de julho de 2025 formaliza uma doutrina que vai alem dos simples controles de seguranca nacional: exportar o stack completo de tecnologia de IA (hardware, modelos, software, aplicacoes e padroes) para paises dispostos a se juntar a alianca de IA americana, sujeitos ao cumprimento dos requisitos de seguranca dos EUA.[2] A IA nao e mais tratada como apenas mais uma tecnologia, mas como um instrumento de projecao de poder analogo ao dolar no sistema monetario ou ao petroleo no sistema energetico.",
        ]),
        ("2. Sintese dos resultados", []),
        ("2.1 Uma vantagem competitiva americana mensuravel e crescente", [
            "O indice CACI (Compute-Adjusted Competitive Index) desenvolvido neste estudo permite a quantificacao da assimetria estrutural. No snapshot do painel publico de abril de 2026, a razao bruta de computacao instalada operacional EUA/UE(13) e de 17,6:1, traduzida por uma formula geometrica ponderada F^0,40 x L^0,20 x R^0,15 / E^0,25 em uma razao CACI Power Mode de 3,46:1. A concentracao de 76,9 por cento da computacao de IA operacional global nos Estados Unidos (49,9 por cento incluindo capacidades planejadas), um capex anual dos hyperscalers de 660-690 bilhoes de USD (superior ao PIB da Suecia) e um custo de treinamento de modelos de fronteira 5 a 10 vezes inferior ao custo europeu confirmam este dominio. A vantagem e autorreforcante: as empresas com acesso abundante a computacao captam rendas de inovacao e de dados que sao muito dificeis de alcancar posteriormente (Capitulo IV).",
            "Uma nuance metodologica importante do Capitulo I (Fig 1.8): a decomposicao Phys/Sov rigorosamente calculada a partir do campo 'Proprietario' da Epoch AI revela que a assimetria e diferenciada por jurisdicao. Os Estados Unidos e a China sao integralmente soberanos sobre sua computacao instalada (CACI Phys = CACI Sov). A UE tambem e amplamente soberana sobre seu F instalado (99,2 por cento de propriedade da UE). O caso extremo e o dos Emirados Arabes Unidos: 99,6 por cento do F_total emirati e detido por operadores do lado dos EUA (Stargate UAE, Microsoft, OpenAI), fazendo com que o CACI soberano caia de 55,7 (Fisico) para 6,0. Esta dissociacao Phys/Sov, formalizada no Capitulo V secao 5.9.2 sob a hipotese de ativacao dos Mandatos de Soberania de Nuvem de 2028, transforma radicalmente a leitura da assimetria: a vulnerabilidade europeia reside nao na computacao instalada, mas na camada operacional de cargas de trabalho na nuvem (principalmente hospedadas na AWS/Azure/GCP).",
        ]),
        ("2.2 Uma arquitetura protecionista de tres niveis", [
            "A analise revela que o protecionismo de IA americano opera em tres niveis distintos, mas cumulativos.",
            "Primeiro nivel: Controles de exportacao (herdados de Biden, mantidos e transformados por Trump). O sistema de niveis (Tier 1/2/3) segmenta o mundo com base no alinhamento geopolitico: acesso livre para aliados proximos (20 paises), limites quantitativos para o resto do mundo, proibicao para adversarios (China, Russia). Mesmo apos a revogacao formal da AI Diffusion Rule em maio de 2025, a incerteza regulatoria pesa sobre as decisoes de investimento dos paises Tier 2 (Capitulo III).",
            "Segundo nivel: Tarifas alfandegarias (inovacao de Trump). A tarifa de 25 por cento sobre semicondutores de IA avancados (Secao 232, janeiro de 2026) constitui uma ruptura: os controles de exportacao visavam a seguranca nacional, as tarifas visam explicitamente a receita e a vantagem competitiva. A combinacao de tarifas e isencoes domesticas cria um diferencial de custo direto entre empresas americanas e nao americanas (Capitulo V).",
            "Terceiro nivel: Gravidade capitalista. A concentracao de capex (660-690 bilhoes de USD em cinco empresas em 2026), combinada com o acesso energetico (os Estados Unidos aceitam um maior uso de combustiveis fosseis, 53,7 GW de capacidade de DC instalada), cria um efeito gravitacional: investimentos do Japao (550 bilhoes), dos Emirados Arabes Unidos e do SoftBank/Stargate convergem para o solo americano, reforcando o hub de computacao sem intervencao regulatoria adicional (Capitulo VI ter).",
            "Um quarto nivel potencial esta surgindo no horizonte de 2028: os Mandatos de Soberania de Nuvem analisados no Capitulo V secao 5.9. Ao estender os requisitos do Framework for AI Diffusion para a camada de nuvem, eles transformariam os hyperscalers dos EUA operando offshore em intermediarios condicionais da computacao global. A janela de vulnerabilidade europeia (CADA operacional ate 2027-2028, na melhor das hipoteses, Mandatos dos EUA ativaveis em 2028) e maxima entre 2028 e 2030.",
        ]),
        ("2.3 Consequencias diferenciadas por regiao", [
            "A Tabela 24 abaixo resume as posicoes estruturais e os riscos especificos de cada regiao estudada, integrando a extensao para a Africa desenvolvida no Capitulo VI quater.",
        ]),
        ("3. Contribuicoes deste estudo", [
            "Esta pesquisa faz cinco contribuicoes para a literatura economica e geoestrategica.",
            "Primeiro, a integracao analitica de trajetorias geralmente tratadas separadamente - energia, semicondutores, computacao, regulamentacao, produtividade - em um quadro unificado. A maioria dos trabalhos academicos trata essas dimensoes separadamente; nossa analise mostra que elas formam um sistema de interdependencias onde cada restricao amplia as outras (a energia restringe a computacao, a computacao restringe a produtividade, a produtividade determina a competitividade).",
            "Segundo, a proposta do indice CACI (Compute-Adjusted Competitive Index), que fornece um quadro de medicao para comparar a competitividade da IA entre regioes, integrando FLOPs disponiveis, capital humano, regulamentacao e custo de energia de acordo com uma formula geometrica ponderada. Embora este indice ainda precise ser refinado empiricamente, ele constitui uma primeira tentativa de sintetizar o conceito de competitividade ajustada pela computacao, identificado como ausente na literatura (Capitulo II). A extensao Phys/Sov introduzida no Capitulo I e formalizada no Capitulo V (F = F_phys x F_sov) adiciona uma dimensao jurisdicional que distingue a computacao fisicamente presente da computacao legalmente controlavel - uma distincao operacional a partir do snapshot de abril de 2026 (caso UAE 99,6 por cento do lado dos EUA) e sistemica sob o regime dos Mandatos de Soberania de Nuvem de 2028.",
            "Terceiro, a demonstracao de que o protecionismo de IA americano produz efeitos paradoxais sitemicos. As restricoes destinadas a manter a vantagem dos EUA aceleram a construcao de um ecossistema chines alternativo (DeepSeek, Huawei Ascend, capacidade real 246-300 EFLOP/s contra 0,5 por cento aparente nos dados consolidados da Epoch AI), empurram os paises Tier 2 em direcao a China (ByteDance no Brasil, na ASEAN, na Africa) e incentivam os aliados Tier 1 a cofinanciar a supremacia dos EUA em vez de construir uma autonomia real (Japao: 550 bilhoes para os Estados Unidos). O protecionismo de IA nao produz um mundo unipolar, mas um mundo fragmentado em blocos tecnologicos.",
            "Quarto, a analise comparativa inedita das respostas regionais ao protecionismo de IA (Europa, America do Sul, Asia, Africa), mostrando que a posicao geopolitica, a dotacao energetica e a proximidade com as cadeias de valor determinam trajetorias de dependencia fundamentalmente diferentes, irredutiveis a um unico modelo de recuperacao ou atraso.",
            "Quinto, a extensao para a Africa (Capitulo VI quater) documenta a assimetria de computacao mais extrema do mundo (deficit de x44 a x417 dependendo dos indicadores) e mostra como o protecionismo americano cria um 'double bind' especifico para este continente: restricao de acesso a computacao de fronteira dos EUA de um lado, exposicao a riscos de vigilancia e sancoes secundarias pelo uso da alternativa chinesa do outro.",
        ]),
        ("4. Limitacoes e caminhos de pesquisa", [
            "Este estudo possui varias limitacoes que devem ser explicitadas.",
            "Incerteza regulatoria. O ambiente de controles de exportacao esta evoluindo rapidamente. A AI Diffusion Rule de Biden foi revogada em maio de 2025; a regra final de Trump de janeiro de 2026 poderia ser modificada (o Comercio deve fornecer uma atualizacao ao Presidente ate julho de 2026). Os cenarios propostos no Capitulo V refletem essa incerteza, mas o espaco de possibilidades e mais amplo do que os quatro cenarios formalizados.",
            "Dados fragmentados. Os dados de computacao de IA por regiao permanecem incompletos, apesar do rigoroso snapshot do painel publico de abril de 2026. As estimativas da Epoch AI representam significativamente menos a capacidade chinesa real (China 0,5 por cento aparente vs 246-300 EFLOP/s reivindicados) devido a anonimizacao dos clusters chineses e a opacidade dos fornecedores Huawei/Cambricon/Biren. O CACI e um indice exploratorio, calibrado no snapshot de abril de 2026, mas ainda nao validado em series temporais longas.",
            "Horizonte temporal. A analise cobre 2026-2030, mas rupturas tecnologicas (computacao quantica, nos sub-2 nm, arquiteturas neuromorficas) poderiam redistribuir as cartas apos 2030. A vantagem atual da Nvidia em GPUs poderia ser contestada por ASICs especializados (Google TPU, Amazon Trainium, Huawei Ascend) ou arquiteturas radicalementes diferentes (DARE/RISC-V europeu, horizonte 2030-2032).",
            "Sensibilidade as ponderacoes do CACI. As ponderacoes da formula geometrica (F^0,40 x L^0,20 x R^0,15 / E^0,25) foram escolhidas no Capitulo II com base na literatura, mas nao provem de uma calibragem econometrica. Uma analise de sensibilidade sistematica nessas ponderacoes poderia revelar trajetorias alternativas nao exploradas.",
            "Futuros caminhos de pesquisa. Quatro extensoes sao necessarias. Primeiro, a calibragem empirica do CACI em dados de pesquisa (produtividade setorial por acesso a computacao) permitiria a validacao ou ajuste das ponderacoes atuais. Segundo, o aprofundamento setorial da cobertura da Africa (Capitulo VI quater) - notadamente a analise pais por pais das 16 estrategias nacionais de IA identificadas e a implementacao da Estrategia Continental da UA Fase II 2028. Terceiro, a modelagem dinamica da interacao energia-computacao-produtividade via modelos de equilibrio geral computavel (CGE) integrando as restricoes de computacao como um fator de producao. Quarto, a observacao longitudinal do regime dos Mandatos de Soberania de Nuvem de 2028 (se ele realmente for ativado) e seus efeitos na trajetoria F_sov de diferentes jurisdicoes.",
        ]),
        ("5. O desafio civilizacional", [
            "Alem das metricas economicas e cenarios geopoliticos, este estudo revela um desafio mais fundamental. A computacao de IA esta se tornando o quarto fator de producao (apos o capital, o trabalho e a terra/energia), estruturando o acesso aos ganhos de produtividade, a inovacao e, finalmente, a prosperidade. Como o petroleo no seculo XX, o controle da computacao no seculo XXI determinara quais nacoes e quais empresas captam as rendas da inovacao.",
            "Os Estados Unidos entenderam isso. O Plano de Acao de IA de julho de 2025 trata explicitamente o stack de IA como um instrumento de alianca geopolitica, comparavel ao Plano Marshall ou ao sistema de Bretton Woods: o acesso a computacao americana e condicionado ao alinhamento estrategico, criando um sistema de dependencias hierarquizadas. A Carnegie observa que a regra visava usar as exportacoes de IA como alavanca sobre os estados pivores geopoliticos, estabelecendo incentivos para que outros governos adotassem os padroes e protecoes tecnologicas americanos em troca de chips dos EUA.[3]",
            "Diante deste novo sistema, a Franca e a Europa tem uma escolha estrategica que se resume, fundamentalmente, a tres opcoes. A primeira e a integracao subordinada: aceitar o status de parceiro tecnologico junior no bloco americano, como o Japao escolheu ao investir 550 bilhoes de USD em solo americano. Esta opcao minimiza o risco de interrupcao do acesso, mas maximiza a dependencia. A segunda e a confrontacao soberanista: construir um ecossistema de IA inteiramente autonomo, como a China e forcada a fazer. Esta opcao e irrealista para 2030 para a Europa, que carece tanto de uma base industrial de semicondutores suficiente quanto de capacidade de mercado interno.",
            "A terceira opcao - aquela que este estudo recomenda no Capitulo VII - e a autonomia estrategica direcionada. Consiste em construir soberania nos segmentos onde a Europa possui uma vantagem comparativa (energia nuclear francesa com custo PPP de 1,35x em relacao aos EUA, equipamentos de litografia ASML, modelos de IA abertos Mistral, quadro regulatorio AI Act), mantendo a interoperabilidade com o ecossistema americano. O objetivo nao e a autarquia, mas a capacidade de escolha: ter alternativas crediveis (nuvem soberana SOV-3, computacao local sob jurisdicao da UE, modelos abertos) para nunca ser cativo de um fornecedor cujos interesses geopoliticos possam divergir dos nossos. A distincao Phys/Sov estabelecida no Capitulo I e operacional aqui: trata-se de aumentar o F_sov na camada de carga de trabalho na nuvem, nao apenas o F_phys na infraestrutura instalada.",
            "O tempo e essencial. O ponto de virada identificado neste estudo e em 2028: convergencia da saturacao de computacao e energia da UE (Capitulo V secao 5.7.3), potencial ativacao dos Mandatos de Soberania de Nuvem (Capitulo V secao 5.9) e o provavel fim da janela de vulnerabilidade antes que as posicoes se cristalizem. Apos esta data, as posicoes se tornam rigidas em torno da linha de base de 17,6:1 bruto / 3,46:1 CACI Power Mode e as dependencias tornam-se estruturais. A janela de acao estrategica 2026-2028 e estreita. Os 109 bilhoes de EUR em investimentos em IA anunciados para a Franca, o programa InvestAI de 200 bilhoes de EUR, a ascensao da Mistral Compute e os locais nucleares dedicados da EDF sao os elementos de uma resposta. Mas entre o anuncio e a execucao, existe a distancia que separa a estrategia da realidade. A India promete 200 bilhoes de USD, mas possui apenas 1,4 GW instalados. A Europa nao pode se dar ao luxo de uma lacuna comparavel entre ambicao e realizacao.",
            "Em ultima analise, 'IA para Americanos Primeiro' nao e apenas um cenario de politica comercial. E o sinal de uma recomposicao da ordem tecnologica mundial comparavel as grandes reestruturacoes do seculo XX - Bretton Woods, o choque do petroleo, o fim da Guerra Fria. Cada uma dessas rupturas criou vencedores e perdedores por decadas. A questao para a Franca e a Europa nao e mais se essa recomposicao ocorrera - ela esta em andamento - mas determinar se seremos seus arquitetos ou seus suditos.",
            "Fabrice Pizzi, Paris, fevereiro de 2026.",
        ]),
    ],
    tables=[
        ("Tabela 24. Sintese das consequencias regionais do protecionismo de IA americano.",
         "Fonte: Construcao do autor, calibrada no snapshot de abril de 2026 (EUA 76,9% da computacao de IA operacional, razao bruta da UE de 17,6:1, CACI Power Mode de 3,46:1).",
         [
             ["Regiao", "Posicao Estrutural", "Impacto Principal", "Risco Especifico"],
             ["Europa / Franca", "Tier 1, dependente de GPUs + nuvem dos EUA (72-80% das cargas de trabalho)",
              "Compute gap 17,6:1 bruto / 3,46:1 CACI; custos de treinamento x5-10",
              "Aprisionamento tecnologico geopolitico; marginalizacao se o bloco EUA-Asia se fechar; vulnerabilidade F_sov em cargas de trabalho na nuvem"],
             ["America do Sul / Brasil", "Tier 2, campo de competicao EUA-China",
              "Bifurcacao tecnologica; fuga de cerebros amplificada",
              "Tripla fratura (Norte-Sul, Leste-Oeste, intrarregional)"],
             ["Japao / Coreia / Taiwan", "Tier 1, elos criticos da cadeia de valor",
              "Cofinanciamento da supremacia dos EUA (550 Bi USD Japao); transferencia de producao",
              "Parceria assimetrica; erosao da vantagem de Taiwan; investimento japones nos EUA em vez da UE"],
             ["India", "Tier 2, pivo do Sul Global",
              "Tensao entre limites de GPU vs ambicao de hub de computacao",
              "Soberania aplicativa sem soberania de hardware"],
             ["China", "Tier 3, autonomizacao forcada",
              "Ecossistema de IA paralelo (Huawei/DeepSeek); capacidade real 246-300 EFLOP/s; atraso de 2-3 geracoes de GPU",
              "Bifurcacao tecnologica permanente; exportacao para Tier 2/3 (Brasil, ASEAN, Africa)"],
             ["Africa", "Tier 2/3, deficit de computacao x44-x417",
              "Assimetria extrema; 'double bind' EUA/China",
              "Dependencia de Huawei/DeepSeek; vigilancia; confinamento estrutural; caso UAE 99,6% do lado dos EUA"],
         ]),
        ("Tabela 25. Resumo dos capitulos, volume e aparato critico do estudo.",
         "Fonte: Construcao do autor. O volume (em paginas indicativas) inclui figuras e tabelas, mas exclui anexos econometricos.",
         [
             ["Capitulo", "Titulo", "Paginas Indicativas", "Notas"],
             ["I", "Quadro Teorico: Protecionismo Tecnologico e IA", "~12", "22"],
             ["II", "Metodologia: Matriz de Cenarios e Indice CACI", "~8", "10"],
             ["III", "Diagnostico Empirico 2020-2026: Energia, Semicondutores, Computacao", "~11", "20"],
             ["IV", "Mecanismos da Vantagem Competitiva dos EUA", "~9", "19"],
             ["V", "Cenarios Prospectivos 2026-2030 e Mandatos de Soberania de Nuvem", "~14", "29"],
             ["VI", "Consequencias para a Franca e a Europa", "~10", "14"],
             ["VI bis", "Consequencias para a America do Sul e o Brasil", "~11", "19"],
             ["VI ter", "Consequencias para a Asia", "~12", "16"],
             ["VI quater", "Consequencias para a Africa", "~13", "26"],
             ["VII", "Recomendacoes Estrategicas para a Franca e a Europa", "~11", "18"],
             ["Conclusao", "Do Protecionismo de IA a Recomposicao da Ordem Tecnologica Mundial", "~9", "3"],
             ["TOTAL", "11 capitulos", "~120", "196"],
         ]),
    ],
    sources_line=(
        "Principais fontes mobilizadas: AIE, McKinsey, Bruegel, Brookings, Carnegie Endowment, "
        "Comissao Europeia, White House/BIS, Parlamento Europeu, CSIS, S&P Global, Epoch AI, "
        "Centre for Future Generations (CFG), Euronews, CEPAL/CENIA (ILIA 2025), Banco Mundial, "
        "Futurum, Introl, World Nuclear News, Arizton, Pillsbury Law, ITIF, Foreign Policy, Hudson "
        "Institute, Mordor Intelligence, McKinsey Global Institute, FMI. Dados adicionais: "
        "Bloomberg, DCD, Morgan Lewis, Tom's Hardware, Serrari Group, Data Center Knowledge, "
        "WEF, Africa Defense Forum, Atlantic Council DFRLab, Carnegie Endowment, New Lines Institute, "
        "RTE, EDF, ANSSI, USTDA. Dados primarios: snapshot do painel publico da Epoch AI "
        "abril de 2026 (https://mo0ogly.github.io/America-First-IA/dashboard/)."
    ),
    notes=[
        "Pillsbury Law (janeiro de 2026), 'Trump Admin Targets Advanced AI Semiconductors'. Secao 232: tarifa de 25 por cento sobre Nvidia H200, AMD MI325X para reexportacao para a China. Isencoes domesticas dos EUA. Regra final simultanea do BIS. Atualizacao do mercado de DC planejada para julho de 2026.",
        "White House / CM Trade Law (julho de 2025), 'America's AI Action Plan'. Pilar III: exportar o stack completo de tecnologia de IA para aliados. Quatro principios: exportacao para aliados, fortalecimento da fiscalizacao, alinhamento global, protecao de medidas.",
        "Carnegie Endowment for International Peace (maio de 2025), 'The Trump Administration May Be About to Repeal the AI Diffusion Rule'. Analise do trilema controle/promocao/alavanca. Recomendacao: ampliar o grupo Tier 1, aumentar as alocacoes para a India, fortalecer os requisitos de localizacao.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Conclusao geral",
    filename="Conclusao_Geral_PT-BR.docx"
)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

LANGS = [EN, FR, BR]

def build_all(out_dir: Path) -> None:
    for lp in LANGS:
        log.info("Building Conclusion [%s] -> %s", lp.code, lp.filename)
        doc = init_document()
        # Figures
        fig_dir = out_dir / "figures_conclusion"
        
        # Build document
        add_cover(doc, lang=lp.code, chapter_label=lp.label, chapter_subtitle=lp.title)
        add_chapter_header(doc, label=lp.label, title=lp.title, intro=lp.intro)
        
        for title, paragraphs in lp.sections:
            render_section(doc, title, paragraphs)
            
            # Insert synthesis image after section 2.3
            if title.startswith("2.3"):
                img_path = fig_dir / f"Fig_Conclusion_Synthese_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
            
        for caption, source, rows in lp.tables:
            render_table(doc, lang=lp.code, caption=caption, source=source, rows=rows)
            
        # Sources line at the end
        add_paragraph(doc, lp.sources_line,
                      align=WD_ALIGN_PARAGRAPH.LEFT,
                      size=9, italic=True, color=GREY, space_after=6)
                      
        render_notes(doc, lang=lp.code, notes=lp.notes)
        render_license(doc, lang=lp.code, page_footer=lp.footer)
        
        out = out_dir / lp.filename
        doc.save(out)
        log.info("Saved %s", out)

if __name__ == "__main__":
    build_all(Path(__file__).parent)
