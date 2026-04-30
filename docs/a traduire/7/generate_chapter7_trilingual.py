"""
Chapter VII - Strategic Recommendations for France and Europe - trilingual generator.

Generates the .docx for Chapter VII in English, French, and Brazilian Portuguese.
All content is aligned with the April 2026 dashboard snapshot.

Author: Fabrice Pizzi (Université Paris-Sorbonne, M2 Intelligence Économique).
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path

from chap7_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
    render_image,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("chapter7_trilingual")

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
    label="CHAPTER VII",
    title="Strategic Recommendations for France and Europe",
    intro=(
        "The previous chapters have established that American AI protectionism creates a measurable "
        "structural competitive advantage (US/EU CACI Power Mode of 3.46:1 on the April 2026 snapshot, "
        "operational installed compute raw ratio of 17.6:1), accelerated by the 2026 Trump tariffs "
        "and the concentration of compute in the United States (76.9% of global operational AI compute, "
        "660-690 billion USD in annual capex from hyperscalers alone). This chapter formulates "
        "strategic recommendations articulated across three time horizons and five structuring axes, "
        "leveraging France's specific comparative advantages (nuclear, Mistral, regulation) and "
        "existing European instruments (AI Continent Action Plan, Chips Act, InvestAI)."
    ),
    sections=[
        ("7.1 Axis 1 - Compute infrastructure: closing the gap", []),
        ("7.1.1 Short term (2026-2027): accelerating AI Factories", [
            "The starting point is the infrastructure gap. The EU has approximately 35 GW of IT data center capacity compared to 53.7 GW in the United States and 19.6 GW in China. In strict AI compute, the April 2026 public dashboard establishes an EU(13) F_total share of 3.3% versus 76.9% for the United States, representing a raw operational ratio of 17.6:1 and a CACI Power Mode ratio (geometric formula F^0.40 x L^0.20 x R^0.15 / E^0.25) of 3.46:1. Three immediate measures are required.",
            "First, accelerate the commissioning of the 13 European AI Factories already created across 17 Member States (AI Continent Action Plan, April 2025), with a target of full operationality by the end of 2027 instead of the 2028-2029 horizon currently envisioned.[1] Second, implement the Special Compute Zones proposed by the Centre for Future Generations, which are derogatory zones (accelerated permits, reduced taxation, priority network connection) for AI data centers of national importance.[2] France has already initiated this process with legislation envisioned to designate data centers as projects of major national interest. Third, secure long-term GPU contracts with Nvidia, AMD, and Intel via multilateral framework agreements (EU-Nvidia, EU-AMD) guaranteeing a minimum annual delivery volume.",
            "A key nuance from the Phys/Sov analysis of Chapter I (Fig 1.8): on physically installed compute, the EU is already largely sovereign (99.2% of EU F_total is held by EU operators). The window of vulnerability is therefore not so much on installed F as on the cloud workload layer (the compute actually used by EU companies, mostly hosted on AWS/Azure/GCP). The following recommendations primarily target this operational layer.",
        ]),
        ("7.1.2 Medium term (2027-2029): AI Gigafactories and sovereign cloud", [
            "The InvestAI program provides for 200 billion EUR (50 billion public, 150 billion private), including 20 billion for five AI Gigafactories that will allow for the creation of sovereign frontier models.[3] This program must be calibrated against the American benchmark: the 660-690 billion USD in 2026 capex from the five US hyperscalers alone represents more than three times the European envelope over five years. The investment gap is structural and will not be closed by public funds alone.[4]",
            "France has a distinctive advantage in this competition. The MGX-Bpifrance-Mistral-Nvidia AI campus, announced at the Choose France Summit 2025, plans for 1.4 GW of compute power powered by nuclear energy, with exascale capabilities operational by 2028.[5] Mistral Compute, launched with 18,000 Nvidia Grace Blackwell superchips in a 40 MW data center in Essonne, constitutes the first credible European offer of frontier compute without exposure to the CLOUD Act. Mistral's capex of 1 billion EUR for 2026, supplemented by the Borlänge data center (Sweden, 1.2 billion EUR, green energy, opening 2027), shows that a European champion can build an alternative infrastructure.[6]",
            "Sovereign cloud constitutes the necessary complement. The ANSSI's SecNumCloud 3.2 certification and the S3NS joint venture (Thales-Google Cloud, SecNumCloud certified December 2025), the Bleu joint venture (Orange-Capgemini-Microsoft, milestone 1 reached November 2025), and the AWS European Sovereign Cloud (launched January 2026, separate German GmbH) create a gradually sovereign ecosystem.[7] The goal should be to reach 30-40% of sensitive AI workloads hosted on certified sovereign cloud by 2029. It is precisely the increase in the F_sov factor (Chap V section 5.9.2) that protects against the hypothetical activation of US Cloud Sovereignty Mandates in 2028.",
        ]),
        ("7.2 Axis 2 - Energy: transforming the nuclear asset into a compute advantage", []),
        ("7.2.1 The French energy advantage", [
            "France has a unique energy advantage in Europe: 70% low-carbon nuclear electricity, a fleet of 56 reactors (plus Flamanville 3 at full power), competitive electricity costs, and a robust transport infrastructure. On the April 2026 snapshot of the public dashboard, the France/USA PPP-adjusted cost stands at 115 versus 85 USD/MWh, a 1.35x ratio much more favorable than the EU average (135 USD/MWh, 1.59x ratio). EDF has identified four industrial sites totaling 2 GW (expandable to six sites by 2026), with direct connection to the grid, reducing connection delays.[8] EDF's Nuclear for AI initiative plans for 250 MW connected to AI chips by the end of 2026, creating a new off-take market for nuclear power.",
            "This advantage is explicitly recognized by international investors. Investments announced at the February 2025 AI Action Summit total 109 billion EUR, including Brookfield/Data4 (20 billion), UAE (30-50 billion), and Fluidstack (10 billion for a 1 GW supercomputer powered by nuclear, operational 2026).[9] France is the only European country capable of simultaneously offering abundant low-carbon electricity, baseload grid stability, and tariff competitiveness for AI data centers—a triptych that neither Germany (nuclear exit), nor the Netherlands (grid constraints), nor Ireland (energy saturation) can reproduce.",
        ]),
        ("7.2.2 Energy recommendations", [
            "First, accelerate the EPR 2 program. The six announced EPR 2 reactors (Penly, Bugey, 9,900 MW, construction from 2027) must be explicitly integrated into data center energy planning. The addition of eight additional optional reactors should be confirmed before 2028, to anticipate 2032-2035 demand.[10]",
            "Second, support SMRs (Small Modular Reactors). The France 2030 program allocates 1 billion EUR to SMRs. NUWARD (EDF subsidiary, 340 MWe) remains the most advanced project. Three startups (Newcleo, Stellaria, Jimmy Energy) filed applications with the ASN in late 2025-early 2026. The goal should be the first commercial SMR dedicated to a data center by 2033-2035, with a pilot connected to an AI campus. However, uncertainty over SMR commercialization timelines dictates that it should not be the sole strategy.[11]",
            "Third, plan AI-grid energy integration. RTE projects an additional 10 GW need for data centers by 2030 in France. Integrating AI demand forecasts into national grid planning (in line with the McKinsey recommendation to align AI growth with sustainable energy expansion) is indispensable to avoid bottlenecks.[12]",
        ]),
        ("7.3 Axis 3 - Technological alliances and supply chain diversification", []),
        ("7.3.1 Consolidating asymmetric industrial partnerships", [
            "The analysis of Chapters VI, VI bis, VI ter, and VI quater reveals that France and Europe do not intend to reproduce the entire AI value chain (which is unrealistic by 2030), but must build targeted strategic alliances that reduce the most critical dependencies.",
            "ASML-Mistral Alliance. ASML's 1.3 billion EUR investment in Mistral AI (September 2025, ASML becoming the primary shareholder at 11%) is the most significant European partnership, linking the global leader in lithography (a critical segment where Europe dominates) to the European AI champion.[13] This type of vertical coupling of European hardware plus European AI should be systematized.",
            "TSMC-Europe Partnership. The TSMC Dresden plant (10 billion EUR, production started 2027) manufactures chips on 28/16/12 nm nodes—insufficient for frontier AI GPUs but critical for automotive and industrial IoT. Negotiating a second TSMC investment in Europe on more advanced nodes (7/5 nm) should be a diplomatic priority.",
            "Japan-EU and Korea-EU Alliances. Japan and Korea control critical segments of the value chain that the United States cannot substitute (SK hynix HBM memory, Tokyo Electron and Shin-Etsu equipment and materials). Bilateral EU-Japan and EU-Korea agreements on the security of AI component supply, structured outside the US-Japan-Korea trilateral framework, would strengthen European autonomy. Chapter VI ter documented that Japanese investment in the United States (550 billion USD) is unilateral—a cross EU-Japan investment would balance this dynamic.",
        ]),
        ("7.3.2 Reducing exposure to protectionist risk", [
            "The Biden-Trump experience shows that export controls and tariffs can be extended rapidly and unpredictably. Three risk reduction measures are required.",
            "Constitution of strategic GPU reserves. On the model of strategic oil reserves (90 days), constitute a national/European stock of AI accelerators covering 6 to 12 months of projected needs. This stock would serve as a buffer against any activation of the Affiliates Rule (suspended until November 2026) or extended Section 232 tariffs.",
            "Hardware provider diversification. Accelerate the evaluation and deployment of alternatives to Nvidia GPUs: AMD MI300X/MI350X, Intel Gaudi 3, Graphcore (UK), and eventually SiPearl (European, Rhea processor for supercomputers). Finance via the European Chips Act a multi-vendor AI accelerator qualification program. The DARE project (European RISC-V, EuroHPC JU) is the 2030-2032 horizon, but intermediate alternatives are available immediately.",
            "Anti-weaponization clauses in trade agreements. Integrate into the future EU-US trade agreement clauses preventing the unilateral use of export controls as a commercial competitiveness instrument, on the model of WTO non-discrimination clauses.",
        ]),
        ("7.4 Axis 4 - Regulation as a competitive advantage", []),
        ("7.4.1 From the AI Act to the Apply AI Strategy", [
            "Mistral CEO Arthur Mensch summarized the European paradox: you cannot regulate your way to compute supremacy.[14] The AI Act, in progressive application since 2024, imposes obligations (transparency, risk assessments, compliance) that constitute both a burden for European companies and a differentiation advantage in global markets. The Apply AI Strategy (2025) complements the AI Act by adopting an AI-first approach for the public sector and promoting buy European, particularly for open-source solutions.[15]",
            "The recommendation is to transform regulation into an offensive rather than defensive lever. Three concrete measures can contribute to this.",
            "(a) Require that AI Factories and AI Gigafactories funded by InvestAI prioritize the use of European models (Mistral, Aleph Alpha, etc.) and certified clouds (SecNumCloud, high-level EUCS).",
            "(b) Exploit the Brussels Effect: global companies complying with the AI Act to access the European market (450 million consumers) de facto adopt European standards, creating a normative advantage. Accelerate mutual recognition agreements with Japan, Brazil, and India.",
            "(c) Create a European CLOUD Act Shield: blocking legislation (on the model of the 1996 EU blocking regulation) preventing European companies from complying with extraterritorial US access requests without authorization from the competent national authority. This measure is the legal instrument that gives substance to the SOV-3 Cloud Sovereignty Framework published by the Commission in October 2025 (Chap V section 5.10.4).",
        ]),
        ("7.4.2 Regulation of compute as a strategic asset", [
            "Comparative analysis (Chapters V and VI ter) shows that frontier compute is now treated by the United States, China, Japan, India, and the Gulf States as a national strategic asset on par with energy or critical raw materials. Europe must formalize this recognition. Gartner predicts that countries pursuing independent AI stacks will need to invest at least 1% of GDP in infrastructure by 2029.[16] For France, this would represent approximately 28 billion EUR annually, an order of magnitude consistent with the 109 billion in investments announced in 2025 (of which a significant portion comes from foreign capital).",
            "The UAE case documented in Chapter I (Fig 1.8) constitutes a warning: 99.6% of Emirati F_total is held by US-side operators, dropping the sovereign CACI from 55.7 to 6.0. An investment attraction policy indifferent to the legal nationality of operators would reproduce this pattern in Europe. European compute regulation must provide for minimum domestic ownership thresholds (for example, 50% minimum of operators under EU jurisdiction for sites over 100 MW), with a mechanism analogous to the Investment Screening Mechanism already applied to strategic investments.",
        ]),
        ("7.5 Axis 5 - Talent and human capital", [
            "Infrastructure without talent produces nothing. Europe is losing AI researchers to American laboratories (salaries, access to frontier compute, scale of projects). Two complementary measures are required.",
            "First, European AI fellowships and talent visas (McKinsey recommendation: launch before end 2026) to attract world-class researchers.[17] France has an advantage with the Mistral/LightOn/Hugging Face ecosystem and the grandes écoles (Polytechnique, ENS, CentraleSupélec), but must match the salaries offered by GAFAM (average x2 to x4 gap for senior AI profiles).",
            "Second, guarantee European researchers access to compute equivalent to that of American laboratories. The deployment of 500,000 GPUs via Fluidstack (operational 2026), the 18,000 Mistral Compute superchips, and the EuroHPC AI Factories constitute the beginning of a response. The goal is that no European researcher leaves the continent for compute access reasons by 2028.",
        ]),
        ("7.6 Synthesis: temporal matrix of recommendations", [
            "Table 23 below summarizes the recommendations by crossing three horizons (2026-2027, 2027-2029, 2029-2032) with the Compute, Energy, and Alliances axes. The Regulation and Talent axes are deployed transversally across the three horizons and are not detailed line by line in the matrix.",
        ]),
        ("7.7 Success conditions and limits", [
            "Several conditions will determine the effectiveness of these recommendations.",
            "Condition 1: Mistral's competitiveness. The entire French AI sovereignty strategy relies in part on Mistral's ability to maintain competitive performance against OpenAI, Anthropic, and Google DeepMind. If the capability gap widens, French infrastructure will serve compliance needs (sovereign hosting of US models) rather than true technological sovereignty.[18] The 1.7 billion EUR fundraising (11.7 billion valuation) and the establishment of Mistral Compute are positive signals, but the scale of competition (OpenAI: 20 billion USD in 2025 recurring revenue) remains disproportionate.",
            "Condition 2: industrial execution. European AI infrastructure programs have historically suffered from delays (EuroHPC, Chips Act). The 13 AI Factories must be operational, not just announced. The experience of Japan (Rapidus 2 nm program) and India (gap between 200+ billion announcements and 1.4 GW installed capacity) illustrate the risks of misalignment between ambition and realization.",
            "Condition 3: European coherence. Intra-European fragmentation (27 energy regimes, divergent positions on nuclear, competing national sovereignty approaches) remains the main obstacle. Scenario C of Chapter V (asymmetric partnership, baseline 3.46:1 toward 2.0-2.5:1) only works for Europe if it speaks with one voice in negotiations with Washington.",
            "Condition 4: the time factor. The tipping point identified in Chapter V (2028, EU compute plus energy saturation, and potential activation of Cloud Sovereignty Mandates) imposes a constrained schedule. If the AI Factories are not operational and the EDF sites not connected by that date, the compute gap will solidify into structural dependence. The window for strategic action is between 2026 and 2028—after which positions crystallize around the 17.6:1 raw / 3.46:1 CACI Power Mode baseline.",
        ]),
    ],
    tables=[
        ("Table 23. Temporal matrix of strategic recommendations by axis (2026-2032).",
         "Source: Author's construction; April 2026 baseline (US/EU operational raw compute 17.6:1, CACI Power Mode 3.46:1).",
         [
             ["Horizon", "Compute Axis", "Energy Axis", "Alliances Axis"],
             ["2026-2027",
              "13 AI Factories operational; FR Special Compute Zones; long-term GPU contracts",
              "250 MW nuclear-AI (EDF); 6 EDF data center sites; Fluidstack 1 GW operational",
              "EU-Nvidia volume agreement; strategic GPU reserves; AI talent visas"],
             ["2027-2029",
              "5 AI Gigafactories (20B EUR); 30-40% sovereign workloads; 1.4 GW MGX-Mistral Campus",
              "6 EPR 2 construction started; AI integration in grid plan; 8 optional EPRs confirmed",
              "TSMC Europe 7/5 nm node; EU-Japan/Korea HBM agreements; European CLOUD Act Shield"],
             ["2029-2032",
              "40% local compute (vs 5%); sovereign frontier models; SiPearl EU AI accelerator",
              "First SMR data center; +20 GW nuclear 2035; integrated AI energy mix",
              "Multi-vendor GPU qualified; AI export norms (Brussels effect); 60% value chain autonomy"],
         ]),
    ],
    notes=[
        "European Commission (April 2025), AI Continent Action Plan. 13 AI Factories in 17 Member States, 200B EUR InvestAI program. Apply AI Strategy (2025): AI-first approach, buy European.",
        "Centre for Future Generations (October 2025), 'Special Compute Zones: Europe's Recipe'. Derogatory zones to reduce data center installation times from 3-5 years to 12-18 months.",
        "Deloitte (November 2025), 'A New Era of Self-Reliance'. InvestAI: 20B EUR for 5 AI Gigafactories, sovereign frontier models.",
        "Euronews (February 2026), 'Will Big Tech's AI Spending Crush Europe's Data Sovereignty?' 2026 capex: Amazon 200B USD, Alphabet 185B USD, Microsoft 145B USD, Meta 135B USD, Oracle 50B USD. Total: 660-690B USD. European sovereign cloud spending: 10.6B EUR 2026.",
        "Global Data Center Hub (May 2025), 'France's 8.5 Bn USD AI Campus'. MGX-Bpifrance-Mistral-Nvidia AI Campus: 1.4 GW, exascale, operational 2028.",
        "Euronews, op. cit. Mistral Compute: 18,000 Grace Blackwell, 40 MW Essonne. Capex 1B EUR (2026). Borlänge data center (Sweden): 1.2B EUR, EcoDataCenter, green energy, opening 2027.",
        "Julien Simon, Medium (January 2026), 'AI Sovereignty in Europe: A Decision Framework'. S3NS: SecNumCloud December 2025. Bleu: milestone 1 November 2025. AWS European Sovereign Cloud: January 2026, Brandenburg GmbH.",
        "World Nuclear News (February 2025), 'France Tempts AI Firms with Nuclear Electricity'. EDF: 4 sites, 2 GW total, call for expression of interest. Data4: 40 MW nuclear supplied by EDF. France PPP-adjusted cost 115 USD/MWh according to public dashboard (April 2026).",
        "Introl Blog (2025), 'France's AI Sovereignty Push'. AI Action Summit: 109B EUR. Bpifrance: 10B EUR. Fluidstack: 10B EUR, 500,000 GPUs, 1 GW, operational 2026.",
        "Enki AI (February 2026), 'Top 10 Nuclear & SMR Projects in France'. EPR 2: 6 reactors (Penly, Bugey), 9,900 MWe, construction 2027. Option for 8 additional reactors. 20 existing reactors: life extension (26 GW).",
        "Enki AI, op. cit. NUWARD: 340 MWe, EDF/Naval Group subsidiary. France 2030: 1B EUR SMR. Newcleo, Stellaria, Jimmy Energy: ASN applications filed. Counter-point: Beyond Nuclear International (January 2026) signals financial difficulties for some SMR startups.",
        "McKinsey (December 2025), 'Accelerating Europe's AI Adoption: The Role of Sovereign AI'. Recommendation: integrate AI demand forecasts into national energy planning. Productivity gains: up to 40% in lighthouse factories.",
        "S&P Global (December 2025), 'Geopolitics of Data Centers'. ASML: 1.3B EUR in Mistral (September 2025), 11% stake. Mistral fundraising: 1.7B EUR, 11.7B EUR valuation.",
        "Euronews, op. cit. Arthur Mensch (2025) quote: 'US companies are building the equivalent of a new Apollo program every year' and 'you cannot regulate your way to computing supremacy'.",
        "European Commission (2025), Apply AI Strategy. AI-first for the public sector, buy European for open-source solutions. AI Observatory for trend monitoring.",
        "Intelligent CIO Europe (February 2026). Gartner: 1/3 of companies will use localized AI platforms by 2027 (vs 5% today). Minimum 1% of GDP investment in AI infrastructure by 2029.",
        "McKinsey, op. cit. AI fellowships and talent visas to be launched before end 2026. 44% of European tech leaders cite data security as a barrier to public cloud; 31% data localization.",
        "Introl Blog, op. cit. 'If the capability gap widens, French infrastructure may serve compliance requirements without enabling competitive AI applications.' OpenAI: 20B USD ARR 2025 (x3 in one year).",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapter VII",
    filename="Chapter_VII_Recommendations_EN.docx"
)

# ---------------------------------------------------------------------------
# Content - FRENCH (Reference)
# ---------------------------------------------------------------------------

FR = LangPack(
    code="FR",
    label="CHAPITRE VII",
    title="Recommandations strategiques pour la France et l'Europe",
    intro=(
        "Les chapitres precedents ont etabli que le protectionnisme IA americain cree un avantage "
        "competitif structurel mesurable (CACI Power Mode US/UE de 3,46:1 sur le snapshot avril 2026, "
        "ratio brut compute installe operationnel de 17,6:1), accelere par les tarifs Trump de 2026 "
        "et la concentration du compute aux Etats-Unis (76,9 pct du compute IA operationnel mondial, "
        "660-690 milliards USD de capex annuel des seuls hyperscalers). Ce chapitre formule des "
        "recommandations strategiques articulees en trois horizons temporels et cinq axes structurants, "
        "en s'appuyant sur les avantages comparatifs specifiques de la France (nucleaire, Mistral, "
        "regulation) et les instruments europeens existants (AI Continent Action Plan, Chips Act, "
        "InvestAI)."
    ),
    sections=[
        ("7.1 Axe 1 - Infrastructure compute : combler le gap", []),
        ("7.1.1 Court terme (2026-2027) : accelerer les AI Factories", [
            "Le point de depart est l'ecart d'infrastructure. L'UE dispose d'environ 35 GW de capacite IT data centers contre 53,7 GW aux Etats-Unis et 19,6 GW en Chine. En compute IA strict, le tableau de bord public d'avril 2026 etablit une part UE(13) F_total de 3,3 pct contre 76,9 pct pour les Etats-Unis, soit un ratio brut operationnel de 17,6:1 et un ratio CACI Power Mode (formule geometrique F^0,40 x L^0,20 x R^0,15 / E^0,25) de 3,46:1. Trois mesures immediates s'imposent.",
            "Premierement, accelerer la mise en service des 13 AI Factories europeennes deja creees dans 17 Etats membres (AI Continent Action Plan, avril 2025), avec un objectif de pleine operationnalite fin 2027 au lieu de l'horizon 2028-2029 actuellement envisage.[1] Deuxiemement, mettre en oeuvre les Special Compute Zones proposees par le Centre for Future Generations, c'est-a-dire des zones derogatoires (permis acceleres, fiscalite allegee, connexion reseau prioritaire) pour les data centers IA d'importance nationale.[2] La France a deja amorce cette demarche avec la legislation envisagee pour designer les data centers comme projets d'interet national majeur. Troisiemement, securiser les contrats long-terme de GPU avec Nvidia, AMD et Intel via des accords cadres multilateraux (UE-Nvidia, UE-AMD) garantissant un volume annuel plancher de livraison.",
            "Une nuance cle issue de l'analyse Phys/Sov du chapitre I (Fig 1.8) : sur le compute physiquement installe, l'UE est deja largement souveraine (99,2 pct du F_total UE est detenu par des operateurs UE). La fenetre de vulnerabilite n'est donc pas tant sur le F installe que sur la couche des charges cloud (le compute reellement utilise par les entreprises UE, majoritairement heberge sur AWS/Azure/GCP). Les recommandations qui suivent ciblent prioritairement cette couche operationnelle.",
        ]),
        ("7.1.2 Moyen terme (2027-2029) : les AI Gigafactories et le cloud souverain", [
            "Le programme InvestAI prevoit 200 milliards EUR (50 milliards publics, 150 milliards prives), dont 20 milliards pour cinq AI Gigafactories qui permettront de creer des modeles frontiers souverains.[3] Ce programme doit etre calibre en fonction du benchmark americain : les 660-690 milliards USD de capex 2026 des seuls cinq hyperscalers US representent plus de trois fois l'enveloppe europeenne sur cinq ans. L'ecart d'investissement est structurel et ne sera pas comble par les seuls fonds publics.[4]",
            "La France dispose d'un avantage distinctif dans cette competition. Le campus IA MGX-Bpifrance-Mistral-Nvidia, annonce au Choose France Summit 2025, prevoit 1,4 GW de puissance compute alimentee par le nucleaire, avec des capacites exascale operationnelles d'ici 2028.[5] Mistral Compute, lance avec 18 000 superchips Nvidia Grace Blackwell dans un data center de 40 MW en Essonne, constitue la premiere offre europeenne credible de compute frontier sans exposition au CLOUD Act. Le capex de Mistral de 1 milliard EUR pour 2026, complete par le data center de Borlange (Suede, 1,2 milliard EUR, energie verte, ouverture 2027), montre qu'un champion europeen peut constituer une infrastructure alternative.[6]",
            "Le cloud souverain constitue le complement necessaire. La certification SecNumCloud 3.2 de l'ANSSI et la joint-venture S3NS (Thales-Google Cloud, certifiee SecNumCloud decembre 2025), la joint-venture Bleu (Orange-Capgemini-Microsoft, milestone 1 atteint novembre 2025), et l'AWS European Sovereign Cloud (lance janvier 2026, GmbH allemande separee) creent un ecosysteme graduellement souverain.[7] L'objectif devrait etre d'atteindre 30-40 pct des workloads IA sensibles heberges sur cloud souverain certifie d'ici 2029. C'est precisement l'augmentation du facteur F_sov (Chap V section 5.9.2) qui protege contre l'activation hypothetique des Cloud Sovereignty Mandates US en 2028.",
        ]),
        ("7.2 Axe 2 - Energie : transformer l'atout nucleaire en avantage compute", []),
        ("7.2.1 L'avantage energetique francais", [
            "La France dispose d'un avantage energetique unique en Europe : 70 pct d'electricite nucleaire decarbonee, un parc de 56 reacteurs (plus Flamanville 3 a pleine puissance), des couts electriques competitifs et une infrastructure de transport robuste. Sur le snapshot avril 2026 du tableau de bord public, le cout PPA-ajuste France/USA s'etablit a 115 contre 85 USD/MWh, soit un ratio de 1,35x bien plus favorable que la moyenne UE (135 USD/MWh, ratio 1,59x). EDF a identifie quatre sites industriels totalisant 2 GW (extensibles a six sites d'ici 2026), avec connexion directe au reseau, reduisant les delais de raccordement.[8] L'initiative Nuclear for AI d'EDF prevoit 250 MW connectes a des chips IA fin 2026, creant un marche off-take nouveau pour le nucleaire.",
            "Cet avantage est explicitement reconnu par les investisseurs internationaux. Les investissements annonces lors de l'AI Action Summit de fevrier 2025 totalisent 109 milliards EUR, dont Brookfield/Data4 (20 milliards), EAU (30-50 milliards), et Fluidstack (10 milliards pour un supercalculateur de 1 GW alimente par le nucleaire, operationnel 2026).[9] La France est le seul pays europeen capable d'offrir simultanement electricite decarbonee abondante, stabilite du reseau baseload, et competitivite tarifaire pour les data centers IA - un triptyque que ni l'Allemagne (sortie du nucleaire), ni les Pays-Bas (contraintes grid), ni l'Irlande (saturation energetique) ne peuvent reproduire.",
        ]),
        ("7.2.2 Recommandations energetiques", [
            "Premierement, accelerer le programme EPR 2. Les six reacteurs EPR 2 annonces (Penly, Bugey, 9 900 MW, construction a partir de 2027) doivent etre explicitement integres dans la planification energetique des data centers. L'ajout de huit reacteurs optionnels supplementaires devrait etre confirme avant 2028, pour anticiper la demande 2032-2035.[10]",
            "Deuxiemement, soutenir les SMR (Small Modular Reactors). Le programme France 2030 alloue 1 milliard EUR aux SMR. NUWARD (filiale EDF, 340 MWe) reste le projet le plus avance. Trois start-ups (Newcleo, Stellaria, Jimmy Energy) ont depose des dossiers aupres de l'ASN fin 2025-debut 2026. L'objectif devrait etre le premier SMR commercial dedie data center d'ici 2033-2035, avec un pilote connecte a un campus IA. Cependant, l'incertitude sur les delais de commercialisation des SMR impose de ne pas en faire la strategie unique.[11]",
            "Troisiemement, planifier l'integration energetique IA-reseau. RTE projette un besoin supplementaire de 10 GW pour les data centers d'ici 2030 en France. L'integration des previsions de demande IA dans la planification du reseau national (conformement a la recommandation McKinsey d'alignement de la croissance IA avec l'expansion energetique durable) est indispensable pour eviter les goulets d'etranglement.[12]",
        ]),
        ("7.3 Axe 3 - Alliances technologiques et diversification des chaines d'approvisionnement", []),
        ("7.3.1 Consolider les partenariats industriels asymetriques", [
            "L'analyse des chapitres VI, VI bis, VI ter et VI quater revele que la France et l'Europe n'ont pas vocation a reproduire l'ensemble de la chaine de valeur IA (ce qui est irrealiste a l'horizon 2030), mais doivent construire des alliances strategiques ciblees qui reduisent les dependances les plus critiques.",
            "Alliance ASML-Mistral. L'investissement d'ASML de 1,3 milliard EUR dans Mistral AI (septembre 2025, ASML devenu premier actionnaire a 11 pct) est le partenariat europeen le plus significatif, reliant le leader mondial de la lithographie (segment critique ou l'Europe domine) au champion europeen de l'IA.[13] Ce type de couplage vertical hardware europeen plus IA europeenne devrait etre systematise.",
            "Partenariat TSMC-Europe. L'usine TSMC de Dresde (10 milliards EUR, production debutee 2027) fabrique des puces sur noeud 28/16/12 nm - insuffisant pour les GPU IA de pointe mais critique pour l'automobile et l'IoT industriel. La negociation d'un second investissement TSMC en Europe sur des noeuds plus avances (7/5 nm) devrait etre une priorite diplomatique.",
            "Alliances Japon-UE et Coree-UE. Le Japon et la Coree controlent des segments critiques de la chaine de valeur que les Etats-Unis ne peuvent pas substituer (memoire HBM de SK hynix, equipements et materiaux de Tokyo Electron et Shin-Etsu). Des accords bilateraux UE-Japon et UE-Coree sur la securite d'approvisionnement en composants IA, structures hors du cadre trilateral US-Japon-Coree, renforceraient l'autonomie europeenne. Le chapitre VI ter a documente que l'engagement japonais aux Etats-Unis (550 milliards USD) est unilateral - un investissement croise UE-Japon equilibrerait cette dynamique.",
        ]),
        ("7.3.2 Reduire l'exposition au risque protectionniste", [
            "L'experience Biden-Trump montre que les controles a l'export et les tarifs peuvent etre etendus rapidement et de maniere imprevisible. Trois mesures de reduction du risque s'imposent.",
            "Constitution de reserves strategiques de GPU. Sur le modele des reserves strategiques de petrole (90 jours), constituer un stock national/europeen d'accelerateurs IA couvrant 6 a 12 mois de besoins projetes. Ce stock servirait d'amortisseur face a une activation eventuelle de l'Affiliates Rule (suspendue jusqu'en novembre 2026) ou des tarifs Section 232 etendus.",
            "Diversification des fournisseurs hardware. Accelerer l'evaluation et le deploiement d'alternatives aux GPU Nvidia : AMD MI300X/MI350X, Intel Gaudi 3, Graphcore (UK), et a terme SiPearl (europeen, processeur Rhea pour supercalculateurs). Financer via le Chips Act europeen un programme de qualification d'accelerateurs IA multi-fournisseurs. Le projet DARE (RISC-V europeen, EuroHPC JU) est l'horizon 2030-2032, mais les alternatives intermediaires sont disponibles immediatement.",
            "Clauses anti-weaponisation dans les accords commerciaux. Integrer dans le futur accord commercial UE-US des clauses empechant l'utilisation unilaterale des controles a l'export comme instrument de competitivite commerciale, sur le modele des clauses de non-discrimination de l'OMC.",
        ]),
        ("7.4 Axe 4 - Regulation comme avantage competitif", []),
        ("7.4.1 De l'AI Act a l'Apply AI Strategy", [
            "Le CEO de Mistral, Arthur Mensch, a resume le paradoxe europeen : on ne peut pas reguler son chemin vers la suprematie du compute.[14] L'AI Act, entre en application progressive depuis 2024, impose des obligations (transparence, evaluations de risques, conformite) qui constituent a la fois une charge pour les entreprises europeennes et un avantage de differenciation sur les marches mondiaux. L'Apply AI Strategy (2025) complete l'AI Act en adoptant une approche AI first pour le secteur public et en promouvant un buy European, particulierement pour les solutions open-source.[15]",
            "La recommandation est de transformer la regulation en levier offensif plutot que defensif. Trois mesures concretes peuvent y contribuer.",
            "(a) Exiger que les AI Factories et AI Gigafactories financees par InvestAI utilisent en priorite des modeles europeens (Mistral, Aleph Alpha, etc.) et des clouds certifies (SecNumCloud, EUCS niveau eleve).",
            "(b) Exploiter l'effet Bruxelles : les entreprises mondiales se conformant a l'AI Act pour acceder au marche europeen (450 millions de consommateurs) adoptent de facto des standards europeens, creant un avantage normatif. Accelerer les accords de reconnaissance mutuelle avec le Japon, le Bresil et l'Inde.",
            "(c) Creer un CLOUD Act Shield europeen : legislation bloquante (sur le modele du reglement de blocage UE de 1996) empechant les entreprises europeennes de se conformer aux demandes d'acces extraterritoriales americaines sans autorisation de l'autorite nationale competente. Cette mesure est l'instrument legal qui donne corps au Cloud Sovereignty Framework SOV-3 publie par la Commission en octobre 2025 (Chap V section 5.10.4).",
        ]),
        ("7.4.2 Regulation du compute comme bien strategique", [
            "L'analyse comparative (chapitres V et VI ter) montre que le compute de pointe est desormais traite par les Etats-Unis, la Chine, le Japon, l'Inde et les Etats du Golfe comme un actif strategique national au meme titre que l'energie ou les matieres premieres critiques. L'Europe doit formaliser cette reconnaissance. Gartner prevoit que les pays poursuivant des stacks IA independants devront investir au minimum 1 pct du PIB dans l'infrastructure d'ici 2029.[16] Pour la France, cela representerait environ 28 milliards EUR annuels, un ordre de grandeur coherent avec les 109 milliards d'investissements annonces en 2025 (dont une part significative provient de capitaux etrangers).",
            "Le cas des EAU documente au chapitre I (Fig 1.8) constitue un avertissement : 99,6 pct du F_total emirati est detenu par des operateurs US-side, faisant chuter le CACI souverain de 55,7 a 6,0. Une politique d'attraction d'investissements indifferente a la nationalite legale des operateurs reproduirait ce schema en Europe. La regulation europeenne du compute doit prevoir des seuils minimaux de propriete domestique (par exemple, 50 pct minimum d'operateurs sous juridiction UE pour les sites de plus de 100 MW), avec un mecanisme analogue a l'Investment Screening Mechanism deja applique aux investissements strategiques.",
        ]),
        ("7.5 Axe 5 - Talent et capital humain", [
            "L'infrastructure sans talent ne produit rien. L'Europe perd des chercheurs IA au profit des laboratoires americains (salaires, acces au compute frontier, echelle des projets). Deux mesures complementaires s'imposent.",
            "Premierement, des bourses IA et des visas talents europeens (recommandation McKinsey : lancement avant fin 2026) pour attirer des chercheurs de rang mondial.[17] La France dispose d'un avantage avec l'ecosysteme Mistral/LightOn/Hugging Face et les grandes ecoles (Polytechnique, ENS, CentraleSupelec), mais doit egaler les salaires offerts par les GAFAM (ecart moyen x2 a x4 pour les profils seniors IA).",
            "Deuxiemement, garantir aux chercheurs europeens un acces au compute equivalent a celui des laboratoires americains. Le deploiement de 500 000 GPU via Fluidstack (operationnel 2026), les 18 000 superchips Mistral Compute, et les AI Factories EuroHPC constituent le debut de reponse. L'objectif est qu'aucun chercheur europeen ne quitte le continent pour des raisons d'acces au compute d'ici 2028.",
        ]),
        ("7.6 Synthese : matrice temporelle des recommandations", [
            "Le Tableau 23 ci-apres recapitule les recommandations en croisant trois horizons (2026-2027, 2027-2029, 2029-2032) with the Compute, Energie, et Alliances axes. Les axes Regulation et Talent se deploient transversalement sur les trois horizons et ne sont pas detailles ligne par ligne dans la matrice.",
        ]),
        ("7.7 Conditions de succes et limites", [
            "Plusieurs conditions determineront l'efficacite de ces recommandations.",
            "Condition 1 : la competitivite de Mistral. L'ensemble de la strategie francaise de souverainete IA repose en partie sur la capacite de Mistral a maintenir des performances competitives face a OpenAI, Anthropic et Google DeepMind. Si l'ecart de capacite se creuse, l'infrastructure francaise servira des besoins de conformite (hebergement souverain de modeles US) plutot que de veritable souverainete technologique.[18] La levee de fonds de 1,7 milliard EUR (evaluation 11,7 milliards) et l'etablissement de Mistral Compute sont des signaux positifs, mais l'echelle de competition (OpenAI : 20 milliards USD de revenus recurrents 2025) reste demesuree.",
            "Condition 2 : l'execution industrielle. Les programmes d'infrastructure IA europeens ont historiquement souffert de retards (EuroHPC, Chips Act). Les 13 AI Factories doivent etre operationnelles, pas simplement annoncees. L'experience du Japon (programme Rapidus 2 nm) et de l'Inde (fosse entre annonces de 200+ milliards et capacite installee de 1,4 GW) illustrent les risques de decalage entre ambition et realisation.",
            "Condition 3 : l'coherence europeenne. La fragmentation intra-europeenne (27 regimes energetiques, positions divergentes sur le nucleaire, approches nationales de souverainete concurrentes) reste le principal obstacle. Le scenario C du chapitre V (partenariat asymetrique, baseline 3,46:1 vers 2,0-2,5:1) ne fonctionne pour l'Europe que si elle parle d'une seule voix dans les negociations avec Washington.",
            "Condition 4 : le facteur temps. Le point de basculement identifie au chapitre V (2028, saturation compute plus energie UE, et activation potentielle des Cloud Sovereignty Mandates) impose un calendrier contraint. Si les AI Factories ne sont pas operationnelles et les sites EDF non raccordes a cette date, le gap de compute se solidifiera en dependance structurelle. La fenetre d'action strategique se situe entre 2026 et 2028 - apres quoi les positions se cristallisent autour de la baseline 17,6:1 brut / 3,46:1 CACI Power Mode.",
        ]),
        ("7.8 Conclusion du chapitre", [
            "La France dispose d'un ensemble d'atouts uniques en Europe pour repondre au protectionnisme IA americain : un parc nucleaire incomparable (70 pct de l'electricite, en cours d'extension), un champion IA competitif (Mistral, 11,7 milliards EUR de valorisation, infrastructure compute propre), un ecosysteme cloud souverain en formation (S3NS, Bleu, OVHcloud, Scaleway, OUTSCALE), et une capacite d'attraction d'investissements etrangers (109 milliards EUR en 2025).",
            "Mais ces atouts ne constituent pas une garantie. L'ecart de capex avec les Etats-Unis (660-690 milliards USD annuels contre 200 milliards EUR sur cinq ans), l'ecart de compute (CACI Power Mode 3,46:1 et brut operationnel 17,6:1), et la dependance structurelle aux GPU americaines (Nvidia : 80 pct du marche des accelerateurs IA) definissent le perimetre realiste de l'autonomie atteignable. L'objectif n'est pas l'autarcie technologique - elle est impossible a horizon 2030 - mais une autonomie strategique suffisante pour que le protectionnisme americain ne se traduise pas en dependance irreversible. La distinction Phys/Sov etablie au chapitre I est ici operationnelle : l'Europe est deja largement souveraine sur le compute installe, le travail consiste a securiser la couche des charges cloud avant que les Cloud Sovereignty Mandates 2028 ne transforment cette dependance en levier geopolitique.",
            "Les lecons comparatives sont claires. Le Japon investit 550 milliards USD aux Etats-Unis pour securiser son acces au compute, au prix d'un co-financement de la suprematie americaine. L'Inde promet 200 milliards USD mais ne dispose que de 1,4 GW installe. La Chine, sous restriction maximale, construit un ecosysteme parallele avec un retard de 2-3 generations en GPU mais une capacite reelle (246-300 EFLOP/s) significativement superieure aux 0,5 pct apparents dans les donnees Epoch AI consolidees. Le Bresil hesite entre les deux blocs et risque la fragmentation. L'Afrique cumule l'asymetrie compute la plus extreme (deficit x44 a x417 selon les indicateurs) et le risque de bifurcation imposee. La France, avec son atout nucleaire et Mistral, dispose d'une trajectoire mediane credible : ni alignement total (Japon), ni confrontation (Chine), ni hesitation (Bresil), mais construction methodique d'une autonomie energetique et compute qui garantit la capacite de choix. Le temps pour agir est mesure : la fenetre 2026-2028 est decisive.",
        ]),
    ],
    tables=[
        ("Tableau 23. Matrice temporelle des recommandations strategiques par axe (2026-2032).",
         "Source : construction de l'auteur ; baseline avril 2026 (compute brut operationnel US/UE 17,6:1, CACI Power Mode 3,46:1).",
         [
             ["Horizon", "Axe Compute", "Axe Energie", "Axe Alliances"],
             ["2026-2027",
              "13 AI Factories operationnelles ; Special Compute Zones FR ; contrats GPU long-terme",
              "250 MW nucleaire-IA (EDF) ; 6 sites EDF data centers ; Fluidstack 1 GW operationnel",
              "Accord UE-Nvidia volumes ; reserves strategiques GPU ; visas talents IA"],
             ["2027-2029",
              "5 AI Gigafactories (20 Md EUR) ; 30-40 pct workloads souverains ; Campus MGX-Mistral 1,4 GW",
              "6 EPR 2 construction lancee ; integration IA dans plan reseau ; 8 EPR optionnels confirmes",
              "TSMC Europe noeud 7/5 nm ; accords UE-Japon/Coree HBM ; CLOUD Act Shield europeen"],
             ["2029-2032",
              "40 pct compute local (vs 5 pct) ; modeles frontier souverains ; SiPearl accelerateur IA UE",
              "Premier SMR data center ; +20 GW nucleaire 2035 ; mix energetique IA integre",
              "Multi-fournisseur GPU qualifie ; normes IA export (effet Bruxelles) ; autonomie 60 pct chaine valeur"],
         ]),
    ],
    notes=[
        "Commission europeenne (avril 2025), AI Continent Action Plan. 13 AI Factories dans 17 Etats membres, programme InvestAI 200 Md EUR. Apply AI Strategy (2025) : approche AI first, buy European.",
        "Centre for Future Generations (octobre 2025), 'Special Compute Zones : Europe's Recipe'. Zones derogatoires pour reduire les delais d'installation de data centers de 3-5 ans a 12-18 mois.",
        "Deloitte (novembre 2025), 'A New Era of Self-Reliance'. InvestAI : 20 Md EUR pour 5 AI Gigafactories, modeles frontier souverains.",
        "Euronews (fevrier 2026), 'Will Big Tech's AI Spending Crush Europe's Data Sovereignty ?' Capex 2026 : Amazon 200 Md USD, Alphabet 185 Md USD, Microsoft 145 Md USD, Meta 135 Md USD, Oracle 50 Md USD. Total : 660-690 Md USD. Depenses cloud souverain europeen : 10,6 Md EUR 2026.",
        "Global Data Center Hub (mai 2025), 'France's 8.5 Bn USD AI Campus'. Campus MGX-Bpifrance-Mistral-Nvidia : 1,4 GW, exascale, operationnel 2028.",
        "Euronews, op. cit. Mistral Compute : 18 000 Grace Blackwell, 40 MW Essonne. Capex 1 Md EUR (2026). Data center Borlange (Suede) : 1,2 Md EUR, EcoDataCenter, energie verte, ouverture 2027.",
        "Julien Simon, Medium (janvier 2026), 'AI Sovereignty in Europe : A Decision Framework'. S3NS : SecNumCloud decembre 2025. Bleu : milestone 1 novembre 2025. AWS European Sovereign Cloud : janvier 2026, GmbH Brandebourg.",
        "World Nuclear News (fevrier 2025), 'France Tempts AI Firms with Nuclear Electricity'. EDF : 4 sites, 2 GW total, appel a manifestation d'interet. Data4 : 40 MW nucleaire fournis par EDF. Cout PPA-ajuste France 115 USD/MWh selon tableau de bord public (avril 2026).",
        "Introl Blog (2025), 'France's AI Sovereignty Push'. AI Action Summit : 109 Md EUR. Bpifrance : 10 Md EUR. Fluidstack : 10 Md EUR, 500 000 GPU, 1 GW, operationnel 2026.",
        "Enki AI (fevrier 2026), 'Top 10 Nuclear & SMR Projects in France'. EPR 2 : 6 reacteurs (Penly, Bugey), 9 900 MWe, construction 2027. Option 8 reacteurs supplementaires. 20 reacteurs existants : extension de vie (26 GW).",
        "Enki AI, op. cit. NUWARD : 340 MWe, filiale EDF/Naval Group. France 2030 : 1 Md EUR SMR. Newcleo, Stellaria, Jimmy Energy : dossiers ASN deposes. Contre-point : Beyond Nuclear International (janvier 2026) signale des difficultes financieres de certaines start-ups SMR.",
        "McKinsey (decembre 2025), 'Accelerating Europe's AI Adoption : The Role of Sovereign AI'. Recommandation : integrer previsions demande IA dans planification energetique nationale. Gains productivite : jusqu'a 40 pct dans les lighthouse factories.",
        "S&P Global (decembre 2025), 'Geopolitics of Data Centers'. ASML : 1,3 Md EUR dans Mistral (septembre 2025), 11 pct du capital. Levee Mistral : 1,7 Md EUR, valorisation 11,7 Md EUR.",
        "Euronews, op. cit. Citation Arthur Mensch (2025) : 'US companies are building the equivalent of a new Apollo program every year' et 'you cannot regulate your way to computing supremacy'.",
        "Commission europeenne (2025), Apply AI Strategy. AI first pour le secteur public, buy European pour les solutions open-source. AI Observatory pour suivi des tendances.",
        "Intelligent CIO Europe (fevrier 2026). Gartner : 1/3 des entreprises utiliseront des plateformes IA localisees d'ici 2027 (vs 5 pct aujourd'hui). Investissement minimum 1 pct du PIB en infrastructure IA d'ici 2029.",
        "McKinsey, op. cit. Bourses IA et visas talents a lancer avant fin 2026. 44 pct des leaders tech europeens citent la securite des donnees comme frein au cloud public ; 31 pct la localisation des donnees.",
        "Introl Blog, op. cit. 'If the capability gap widens, French infrastructure may serve compliance requirements without enabling competitive AI applications.' OpenAI : 20 Md USD ARR 2025 (x3 en un an).",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapitre VII",
    filename="Chapitre_VII_Recommandations_FR.docx"
)

# ---------------------------------------------------------------------------
# Content - PORTUGUESE (BRAZIL)
# ---------------------------------------------------------------------------

BR = LangPack(
    code="PT-BR",
    label="CAPITULO VII",
    title="Recomendacoes Estrategicas para a Franca e a Europa",
    intro=(
        "Os capitulos anteriores estabeleceram que o protecionismo de IA americano cria uma vantagem "
        "competitiva estrutural mensuravel (CACI Power Mode EUA/UE de 3,46:1 no snapshot de abril de 2026, "
        "razao bruta de computacao instalada operacional de 17,6:1), acelerada pelas tarifas Trump de 2026 "
        "e pela concentracao de computacao nos Estados Unidos (76,9% da computacao de IA operacional global, "
        "660-690 bilhoes de USD em capex anual apenas dos hyperscalers). Este capitulo formula "
        "recomendacoes estrategicas articuladas em tres horizontes temporais e cinco eixos estruturantes, "
        "aproveitando as vantagens comparativas especificas da Franca (nuclear, Mistral, regulamentacao) e "
        "os instrumentos europeus existentes (Plano de Acao do Continente de IA, Chips Act, InvestAI)."
    ),
    sections=[
        ("7.1 Eixo 1 - Infraestrutura de computacao: fechando a lacuna", []),
        ("7.1.1 Curto prazo (2026-2027): acelerando as AI Factories", [
            "O ponto de partida e a lacuna de infraestrutura. A UE possui aproximadamente 35 GW de capacidade de data center de TI em comparacao com 53,7 GW nos Estados Unidos e 19,6 GW na China. Em computacao de IA estrita, o painel publico de abril de 2026 estabelece uma participacao da UE(13) F_total de 3,3% contra 76,9% para os Estados Unidos, representando uma razao operacional bruta de 17,6:1 e uma razao CACI Power Mode (formula geometrica F^0,40 x L^0,20 x R^0,15 / E^0,25) de 3,46:1. Tres medidas imediatas sao necessarias.",
            "Primeiro, acelerar o comissionamento das 13 European AI Factories ja criadas em 17 Estados-Membros (Plano de Acao do Continente de IA, abril de 2025), com uma meta de operacionalidade total ate o final de 2027, em vez do horizonte 2028-2029 atualmente previsto.[1] Segundo, implementar as Special Compute Zones propostas pelo Centre for Future Generations, que sao zonas derogatorias (licencas aceleradas, tributacao reduzida, conexao de rede prioritaria) para data centers de IA de importancia nacional.[2] A Franca ja iniciou esse processo com a legislacao prevista para designar os data centers como projetos de grande interesse nacional. Terceiro, garantir contratos de GPU de longo prazo com Nvidia, AMD e Intel por meio de acordos-quadro multilaterais (UE-Nvidia, UE-AMD) que garantam um volume minimo de entrega anual.",
            "Uma nuance fundamental da analise Phys/Sov do Capitulo I (Fig 1.8): na computacao fisicamente instalada, a UE ja e amplamente soberana (99,2% do F_total da UE e detido por operadores da UE). A janela de vulnerabilidade, portanto, nao esta tanto no F instalado, mas na camada de carga de trabalho na nuvem (a computacao realmente usada pelas empresas da UE, hospedada principalmente na AWS/Azure/GCP). As recomendacoes a seguir visam prioritariamente esta camada operacional.",
        ]),
        ("7.1.2 Medio prazo (2027-2029): AI Gigafactories e nuvem soberana", [
            "O programa InvestAI preve 200 bilhoes de EUR (50 bilhoes publicos, 150 bilhoes privados), incluindo 20 bilhoes para cinco AI Gigafactories que permitirao a criacao de modelos de fronteira soberanos.[3] Este programa deve ser calibrado em relacao ao benchmark americano: os 660-690 bilhoes de USD em capex de 2026 apenas dos cinco hyperscalers dos EUA representam mais de tres vezes o envelope europeu ao longo de cinco anos. A lacuna de investimento e estrutural e nao sera fechada apenas por fundos publicos.[4]",
            "A Franca possui uma vantagem distintiva nesta competicao. O campus de IA MGX-Bpifrance-Mistral-Nvidia, anunciado na Cupula Choose France 2025, preve 1,4 GW de potencia computacional alimentada por energia nuclear, com capacidades exascale operacionais ate 2028.[5] A Mistral Compute, lancada com 18.000 superchips Nvidia Grace Blackwell em um data center de 40 MW em Essonne, constitui a primeira oferta europeia credivel de computacao de fronteira sem exposicao a Lei CLOUD. O capex da Mistral de 1 bilhao de EUR para 2026, complementado pelo data center de Borlänge (Suecia, 1,2 bilhao de EUR, energia verde, abertura em 2027), mostra que uma campea europeia pode construir uma infraestrutura alternativa.[6]",
            "A nuvem soberana constitui o complemento necessario. A certificacao SecNumCloud 3.2 da ANSSI e a joint venture S3NS (Thales-Google Cloud, certificada SecNumCloud em dezembro de 2025), a joint venture Bleu (Orange-Capgemini-Microsoft, marco 1 alcancado em novembro de 2025) e a AWS European Sovereign Cloud (lancada em janeiro de 2026, GmbH alema separada) criam um ecossistema gradualmente soberano.[7] A meta deve ser alcancar 30-40% das cargas de trabalho de IA sensiveis hospedadas em nuvem soberana certificada ate 2029. E precisamente o aumento do fator F_sov (Cap V secao 5.9.2) que protege contra a hipotetica ativacao dos Mandatos de Soberania de Nuvem dos EUA em 2028.",
        ]),
        ("7.2 Eixo 2 - Energia: transformando o ativo nuclear em uma vantagem computacional", []),
        ("7.2.1 A vantagem energetica francesa", [
            "A Franca possui uma vantagem energetica unica na Europa: 70% de eletricidade nuclear de baixo carbono, uma frota de 56 reatores (mais Flamanville 3 em potencia total), custos de eletricidade competitivos e uma infraestrutura de transporte robusta. No snapshot de abril de 2026 do painel publico, o custo ajustado por PPP Franca/EUA e de 115 contra 85 USD/MWh, uma razao de 1,35x muito mais favoravel que a media da UE (135 USD/MWh, razao de 1,59x). A EDF identificou quatro locais industriais totalizando 2 GW (expansiveis para seis locais ate 2026), com conexao direta a rede, reduzindo os atrasos na conexao.[8] A iniciativa Nuclear for AI da EDF preve 250 MW conectados a chips de IA ate o final de 2026, criando um novo mercado de off-take para a energia nuclear.",
            "Esta vantagem e explicitamente reconhecida por investidores internacionais. Os investimentos anunciados na Cupula de Acao de IA de fevereiro de 2025 totalizam 109 bilhoes de EUR, incluindo Brookfield/Data4 (20 bilhoes), Emirados Arabes Unidos (30-50 bilhoes) e Fluidstack (10 bilhoes para um supercomputador de 1 GW alimentado por energia nuclear, operacional em 2026).[9] A Franca e o unico pais europeu capaz de oferecer simultaneamente eletricidade de baixo carbono abundante, estabilidade de rede baseload e competitividade tarifaria para data centers de IA - um triptico que nem a Alemanha (saida nuclear), nem a Holanda (restricoes de rede), nem a Irlanda (saturacao energetica) podem reproduzir.",
        ]),
        ("7.2.2 Recomendacoes energeticas", [
            "Primeiro, acelerar o programa EPR 2. Os seis reatores EPR 2 anunciados (Penly, Bugey, 9.900 MW, construcao a partir de 2027) devem ser explicitamente integrados no planejamento energetico dos data centers. A adicao de oito reatores opcionais adicionais deve ser confirmada antes de 2028, para antecipar a demanda de 2032-2035.[10]",
            "Segundo, apoiar os SMRs (Reatores Modulares Pequenos). O programa Franca 2030 aloca 1 bilhao de EUR para SMRs. A NUWARD (subsidiaria da EDF, 340 MWe) continua sendo o projeto mais avancado. Tres startups (Newcleo, Stellaria, Jimmy Energy) entraram com pedidos na ASN no final de 2025 e inicio de 2026. O objetivo deve ser o primeiro SMR comercial dedicado a um data center ate 2033-2035, com um piloto conectado a um campus de IA. No entanto, a incerteza sobre os cronogramas de comercializacao dos SMRs dita que esta nao deve ser a unica estrategia.[11]",
            "Terceiro, planejar a integracao energetica IA-rede. A RTE projeta uma necessidade adicional de 10 GW para data centers ate 2030 na Franca. Integrar as prevecoes de demanda de IA no planejamento da rede nacional (em linha com a recomendacao da McKinsey de alinhar o crescimento da IA com a expansao energetica sustentavel) e indispensavel para evitar gargalos.[12]",
        ]),
        ("7.3 Eixo 3 - Aliancas tecnologicas e diversificacao da cadeia de suprimentos", []),
        ("7.3.1 Consolidando parcerias industriais assimetricas", [
            "A analise dos Capitulos VI, VI bis, VI ter e VI quater revela que a Franca e a Europa nao pretendem reproduzir toda a cadeia de valor da IA (o que e irrealista ate 2030), mas devem construir aliancas estrategicas direcionadas que reduzam as dependencias mais criticas.",
            "Alianca ASML-Mistral. O investimento de 1,3 bilhao de EUR da ASML na Mistral AI (setembro de 2025, com a ASML tornando-se a principal acionista com 11%) e a parceria europeia mais significativa, ligando a lider global em litografia (um segmento critico onde a Europa domina) a campea europeia de IA.[13] Este tipo de acoplamento vertical de hardware europeu mais IA europeia deve ser sistematizado.",
            "Parceria TSMC-Europa. A fabrica da TSMC em Dresden (10 bilhoes de EUR, producao iniciada em 2027) fabrica chips em nos de 28/16/12 nm - insuficientes para GPUs de IA de fronteira, mas criticos para os setores automotivo e IoT industrial. Negociar um segundo investimento da TSMC na Europa em nos mais avancados (7/5 nm) deve ser uma prioridade diplomatica.",
            "Aliancas Japao-UE e Coreia-UE. Japao e Coreia controlam segmentos criticos da cadeia de valor que os Estados Unidos nao podem substituir (memoria HBM da SK hynix, equipamentos e materiais da Tokyo Electron e Shin-Etsu). Acordos bilaterais UE-Japao e UE-Coreia sobre a seguranca do fornecimento de componentes de IA, estruturados fora do quadro trilateral EUA-Japao-Coreia, reforcariam a autonomia europeia. O Capitulo VI ter documentou que o investimento japones nos Estados Unidos (550 bilhoes de USD) e unilateral - um investimento cruzado UE-Japao equilibraria essa dinamica.",
        ]),
        ("7.3.2 Reduzindo a exposicao ao risco protecionista", [
            "A experiencia Biden-Trump mostra que os controles de exportacao e as tarifas podem ser estendidos de forma rapida e imprevisivel. Tres medidas de reducao de risco sao necessarias.",
            "Constituicao de reservas estrategicas de GPU. No modelo das reservas estrategicas de petroleo (90 dias), constituir um estoque nacional/europeu de aceleradores de IA cobrindo de 6 a 12 meses das necessidades projetadas. Este estoque serviria como um amortecedor contra qualquer ativacao da Affiliates Rule (suspensa ate novembro de 2026) ou tarifas estendidas da Secao 232.",
            "Diversificacao de fornecedores de hardware. Acelerar a avaliacao e implantacao de alternativas as GPUs da Nvidia: AMD MI300X/MI350X, Intel Gaudi 3, Graphcore (Reino Unido) e, eventualmente, SiPearl (europeu, processador Rhea para supercomputadores). Financiar via o Chips Act europeu um programa de qualificacao de aceleradores de IA de multiplos fornecedores. O projeto DARE (RISC-V europeu, EuroHPC JU) e o horizonte 2030-2032, mas alternativas intermediarias estao disponiveis imediatamente.",
            "Clausulas anti-armamento em acordos comerciais. Integrar no futuro acordo comercial UE-EUA clausulas que impecam o uso unilateral de controles de exportacao como instrumento de competitividade comercial, no modelo das clausulas de nao discriminacao da OMC.",
        ]),
        ("7.4 Eixo 4 - Regulamentacao como vantagem competitiva", []),
        ("7.4.1 Do AI Act a Apply AI Strategy", [
            "O CEO da Mistral, Arthur Mensch, resumiu o paradoxo europeu: voce nao pode regulamentar seu caminho para a supremacia computacional.[14] O AI Act, em aplicacao progressiva desde 2024, impoe obrigacoes (transparencia, avaliacoes de risco, conformidade) que constituem tanto um fardo para as empresas europeias quanto uma vantagem de diferenciacao nos mercados globais. A Apply AI Strategy (2025) complementa o AI Act ao adotar uma abordagem 'IA primeiro' para o setor publico e promover o 'compre europeu', particularmente para solucoes de codigo aberto.[15]",
            "A recomendacao e transformar a regulamentacao em uma alavanca ofensiva em vez de defensiva. Tres medidas concretas podem contribuir para isso.",
            "(a) Exigir que as AI Factories e AI Gigafactories financiadas pelo InvestAI priorizem o uso de modelos europeus (Mistral, Aleph Alpha, etc.) e nuvens certificadas (SecNumCloud, EUCS de alto nivel).",
            "(b) Explorar o Efeito Bruxelas: empresas globais que cumprem o AI Act para acessar o mercado europeu (450 milhoes de consumidores) adotam padroes europeus de fato, criando uma vantagem normativa. Acelerar acordos de reconhecimento mutuo com Japao, Brasil e India.",
            "(c) Criar um Escudo da Lei CLOUD Europeu: legislacao de bloqueio (no modelo do regulamento de bloqueio da UE de 1996) impedindo que empresas europeias cumpram pedidos de acesso extraterritoriais dos EUA sem autorizacao da autoridade nacional competente. Esta medida e o instrumento legal que da substancia ao Quadro de Soberania de Nuvem SOV-3 publicado pela Comissao em outubro de 2025 (Cap V secao 5.10.4).",
        ]),
        ("7.4.2 Regulamentacao da computacao como um ativo estrategico", [
            "A analise comparativa (Capitulos V e VI ter) mostra que a computacao de fronteira e agora tratada pelos Estados Unidos, China, Japao, India e Estados do Golfo como um ativo estrategico nacional no mesmo nivel da energia ou das materias-primas criticas. A Europa deve formalizar este reconhecimento. A Gartner preve que os paises que buscam stacks de IA independentes precisarao investir pelo menos 1% do PIB em infraestrutura ate 2029.[16] Para a Franca, isso representaria aproximadamente 28 bilhoes de EUR anuais, uma ordem de grandeza consistente com os 109 bilhoes de investimentos anunciados em 2025 (dos quais uma parte significativa vem de capital estrangeiro).",
            "O caso dos Emirados Arabes Unidos documentado no Capitulo I (Fig 1.8) constitui um alerta: 99,6% do F_total emirati e detido por operadores do lado dos EUA, derrubando o CACI soberano de 55,7 para 6,0. Uma politica de atracao de investimentos indiferente a nacionalidade legal dos operadores reproduziria este padrao na Europa. A regulamentacao europeia de computacao deve prever limites minimos de propriedade domestica (por exemplo, minimo de 50% de operadores sob jurisdicao da UE para locais com mais de 100 MW), com um mecanismo analogo ao Mecanismo de Triagem de Investimento ja aplicado a investimentos estrategicos.",
        ]),
        ("7.5 Eixo 5 - Talento e capital humano", [
            "Infraestrutura sem talento nao produz nada. A Europa esta perdendo pesquisadores de IA para laboratorios americanos (salarios, acesso a computacao de fronteira, escala de projetos). Duas medidas complementares sao necessarias.",
            "Primeiro, bolsas de IA europeias e vistos de talento (recomendacao da McKinsey: lancamento antes do final de 2026) para atrair pesquisadores de classe mundial.[17] A Franca possui uma vantagem com o ecossistema Mistral/LightOn/Hugging Face e as grandes écoles (Polytechnique, ENS, CentraleSupélec), mas deve igualar os salarios oferecidos pela GAFAM (lacuna media de x2 a x4 para perfis senior de IA).",
            "Segundo, garantir aos pesquisadores europeus acesso a computacao equivalente a dos laboratorios americanos. A implantacao de 500.000 GPUs via Fluidstack (operacional em 2026), os 18.000 superchips Mistral Compute e as European AI Factories constituem o inicio de uma resposta. O objetivo e que nenhum pesquisador europeu deixe o continente por razoes de acesso a computacao ate 2028.",
        ]),
        ("7.6 Sintese: matriz temporal de recomendacoes", [
            "A Tabela 23 abaixo resume as recomendacoes cruzando tres horizontes (2026-2027, 2027-2029, 2029-2032) com os eixos de Computacao, Energia e Aliancas. Os eixos de Regulamentacao e Talento sao implantados transversalmente nos tres horizontes e nao sao detalhados linha por linha na matriz.",
        ]),
        ("7.7 Condicoes de sucesso e limites", [
            "Varias condicoes determinarao a eficacia destas recomendacoes.",
            "Condicao 1: competitividade da Mistral. Toda a estrategia de soberania de IA francesa depende, em parte, da capacidade da Mistral de manter um desempenho competitivo contra OpenAI, Anthropic e Google DeepMind. Se a lacuna de capacidade aumentar, a infraestrutura francesa atendera as necessidades de conformidade (hospedagem soberana de modelos dos EUA) em vez de uma verdadeira soberania tecnologica.[18] A arrecadacao de fundos de 1,7 bilhao de EUR (avaliacao de 11,7 bilhoes) e o estabelecimento da Mistral Compute sao sinais positivos, mas a escala da competicao (OpenAI: 20 bilhoes de USD em receita recorrente de 2025) continua desproporcional.",
            "Condicao 2: execucao industrial. Os programas de infraestrutura de IA europeus sofreram historicamente com atrasos (EuroHPC, Chips Act). As 13 AI Factories devem estar operacionais, nao apenas anunciadas. A experiencia do Japao (programa Rapidus 2 nm) e da India (lacuna entre anuncios de mais de 200 bilhoes e capacidade instalada de 1,4 GW) ilustram os riscos de desalinhamento entre ambicao e realizacao.",
            "Condicao 3: coerencia europeia. A fragmentacao intra-europeia (27 regimes energeticos, posicoes divergentes sobre energia nuclear, abordagens nacionais de soberania concorrentes) continua sendo o principal obstaculo. O Cenario C do Capitulo V (parceria assimetrica, linha de base de 3,46:1 para 2,0-2,5:1) so funciona para a Europa se ela falar com uma unica voz nas negociacoes com Washington.",
            "Condicao 4: o fator tempo. O ponto de virada identificado no Capitulo V (2028, saturacao de computacao e energia da UE e potencial ativacao dos Mandatos de Soberania de Nuvem) impoe um cronograma restrito. Se as AI Factories nao estiverem operacionais e os locais da EDF nao estiverem conectados ate essa data, a lacuna de computacao se solidificara em dependencia estrutural. A janela para acao estrategica e entre 2026 e 2028 - apos o que as posicoes se cristalizam em torno da linha de base de 17,6:1 bruto / 3,46:1 CACI Power Mode.",
        ]),
        ("7.8 Conclusao do capitulo", [
            "A Franca possui um conjunto de ativos unicos na Europa para responder ao protecionismo de IA americano: um parque nuclear incomparavel (70% da eletricidade, em processo de expansao), uma campea de IA competitiva (Mistral, valorizacao de 11,7 bilhoes de EUR, infraestrutura de computacao propria), um ecossistema de nuvem soberana em formacao (S3NS, Bleu, OVHcloud, Scaleway, OUTSCALE) e uma capacidade de atracao de investimentos estrangeiros (109 bilhoes de EUR em 2025).",
            "Mas esses ativos nao constituem uma garantia. A lacuna de capex com os Estados Unidos (660-690 bilhoes de USD anuais contra 200 bilhoes de EUR ao longo de cinco anos), a lacuna de computacao (CACI Power Mode 3,46:1 e bruto operacional 17,6:1) e a dependencia estrutural das GPUs americanas (Nvidia: 80% do mercado de aceleradores de IA) definem o perimetro realista da autonomia alcancavel. O objetivo nao e a autarquia tecnologica - ela e impossivel no horizonte de 2030 - mas uma autonomia estrategica suficiente para que o protecionismo americano nao se traduza em dependencia irreversivel. A distincao Phys/Sov estabelecida no Capitulo I e operacional aqui: a Europa ja e amplamente soberana na computacao instalada, o trabalho consiste em proteger a camada de cargas de trabalho na nuvem antes que os Mandatos de Soberania de Nuvem de 2028 transformem essa dependencia em alavanca geopolitica.",
            "As licoes comparativas sao claras. O Japao investe 550 bilhoes de USD nos Estados Unidos para garantir seu acesso a computacao, ao custo de um cofinanciamento da supremacia americana. A India promete 200 bilhoes de USD, mas possui apenas 1,4 GW instalado. A China, sob restricao maxima, constroi um ecossistema paralelo com um atraso de 2-3 geracoes em GPUs, mas com uma capacidade real (246-300 EFLOP/s) significativamente superior aos 0,5% aparentes nos dados consolidados da Epoch AI. O Brasil hesita entre os dois blocos e corre o risco de fragmentacao. A Africa acumula a assimetria de computacao mais extrema (deficit de x44 a x417 de acordo com os indicadores) e o risco de bifurcacao imposta. A Franca, com seu ativo nuclear e a Mistral, possui uma trajetoria mediana credivel: nem alinhamento total (Japao), nem confronto (China), nem hesitacao (Brasil), mas construcao metodica de uma autonomia energetica e computacional que garante a capacidade de escolha. O tempo para agir e limitado: a janela 2026-2028 e decisiva.",
        ]),
    ],
    tables=[
        ("Tabela 23. Matriz temporal de recomendacoes estrategicas por eixo (2026-2032).",
         "Fonte: Construcao do autor; linha de base de abril de 2026 (razao bruta operacional de computacao EUA/UE de 17,6:1, CACI Power Mode de 3,46:1).",
         [
             ["Horizonte", "Eixo de Computacao", "Eixo de Energia", "Eixo de Aliancas"],
             ["2026-2027",
              "13 AI Factories operacionais; Special Compute Zones na FR; contratos de GPU de longo prazo",
              "250 MW nuclear-IA (EDF); 6 locais de data center da EDF; Fluidstack 1 GW operacional",
              "Acordo de volume UE-Nvidia; reservas estrategicas de GPU; vistos de talento de IA"],
             ["2027-2029",
              "5 AI Gigafactories (20 Bi EUR); 30-40% de cargas de trabalho soberanas; Campus MGX-Mistral de 1,4 GW",
              "6 EPR 2 construcao iniciada; integracao de IA no plano de rede; 8 EPRs opcionais confirmados",
              "TSMC Europa no de 7/5 nm; acordos UE-Japao/Coreia HBM; Escudo da Lei CLOUD Europeu"],
             ["2029-2032",
              "40% de computacao local (vs 5%); modelos de fronteira soberanos; acelerador de IA SiPearl da UE",
              "Primeiro data center SMR; +20 GW nuclear em 2035; matriz energetica de IA integrada",
              "Multi-fornecedor de GPU qualificado; normas de exportacao de IA (efeito Bruxelas); 60% de autonomia da cadeia de valor"],
         ]),
    ],
    notes=[
        "Comissao Europeia (abril de 2025), Plano de Acao do Continente de IA. 13 AI Factories em 17 Estados-Membros, programa InvestAI de 200 Bi EUR. Apply AI Strategy (2025): abordagem IA-primeiro, compre europeu.",
        "Centre for Future Generations (outubro de 2025), 'Special Compute Zones: Europe's Recipe'. Zonas derogatorias para reduzir os tempos de instalacao de data centers de 3-5 anos para 12-18 meses.",
        "Deloitte (novembro de 2025), 'A New Era of Self-Reliance'. InvestAI: 20 Bi EUR para 5 AI Gigafactories, modelos de fronteira soberanos.",
        "Euronews (fevereiro de 2026), 'Will Big Tech's AI Spending Crush Europe's Data Sovereignty?' Capex de 2026: Amazon 200 Bi USD, Alphabet 185 Bi USD, Microsoft 145 Bi USD, Meta 135 Bi USD, Oracle 50 Bi USD. Total: 660-690 Bi USD. Gastos com nuvem soberana europeia: 10,6 Bi EUR em 2026.",
        "Global Data Center Hub (maio de 2025), 'France's 8.5 Bn USD AI Campus'. Campus de IA MGX-Bpifrance-Mistral-Nvidia: 1,4 GW, exascale, operacional em 2028.",
        "Euronews, op. cit. Mistral Compute: 18.000 Grace Blackwell, 40 MW Essonne. Capex de 1 Bi EUR (2026). Data center de Borlänge (Suecia): 1,2 Bi EUR, EcoDataCenter, energia verde, abertura em 2027.",
        "Julien Simon, Medium (janeiro de 2026), 'AI Sovereignty in Europe: A Decision Framework'. S3NS: SecNumCloud em dezembro de 2025. Bleu: marco 1 em novembro de 2025. AWS European Sovereign Cloud: janeiro de 2026, Brandenburg GmbH.",
        "World Nuclear News (fevereiro de 2025), 'France Tempts AI Firms with Nuclear Electricity'. EDF: 4 locais, 2 GW no total, chamada para manifestacao de interesse. Data4: 40 MW nucleares fornecidos pela EDF. Custo ajustado por PPP da Franca de 115 USD/MWh de acordo com o painel publico (abril de 2026).",
        "Introl Blog (2025), 'France's AI Sovereignty Push'. Cupula de Acao de IA: 109 Bi EUR. Bpifrance: 10 Bi EUR. Fluidstack: 10 Bi EUR, 500.000 GPUs, 1 GW, operacional em 2026.",
        "Enki AI (fevereiro de 2026), 'Top 10 Nuclear & SMR Projects in France'. EPR 2: 6 reatores (Penly, Bugey), 9.900 MWe, construcao em 2027. Opcao para 8 reatores adicionais. 20 reatores existentes: extensao de vida (26 GW).",
        "Enki AI, op. cit. NUWARD: 340 MWe, subsidiaria da EDF/Naval Group. Franca 2030: 1 Bi EUR para SMR. Newcleo, Stellaria, Jimmy Energy: pedidos na ASN registrados. Contraponto: Beyond Nuclear International (janeiro de 2026) sinaliza dificuldades financeiras para algumas startups de SMR.",
        "McKinsey (dezembro de 2025), 'Accelerating Europe's AI Adoption: The Role of Sovereign AI'. Recomendacao: integrar previsoes de demanda de IA no planejamento energetico nacional. Ganhos de produtividade: ate 40% em lighthouse factories.",
        "S&P Global (dezembro de 2025), 'Geopolitics of Data Centers'. ASML: 1,3 Bi EUR na Mistral (setembro de 2025), participacao de 11%. Arrecadacao de fundos da Mistral: 1,7 Bi EUR, avaliacao de 11,7 Bi EUR.",
        "Euronews, op. cit. Citacao de Arthur Mensch (2025): 'As empresas dos EUA estao construindo o equivalente a um novo programa Apollo todos os anos' e 'voce nao pode regulamentar seu caminho para a supremacia computacional'.",
        "Comissao Europeia (2025), Apply AI Strategy. IA-primeiro para o setor publico, compre europeu para solucoes de codigo aberto. Observatorio de IA para monitoramento de tendencias.",
        "Intelligent CIO Europe (fevereiro de 2026). Gartner: 1/3 das empresas usarao plataformas de IA localizadas ate 2027 (vs 5% hoje). Investimento minimo de 1% do PIB em infraestrutura de IA ate 2029.",
        "McKinsey, op. cit. Bolsas de IA e vistos de talento a serem lancados antes do final de 2026. 44% dos lideres tech europeus citam a seguranca de dados como barreira a nuvem publica; 31% a localizacao dos dados.",
        "Introl Blog, op. cit. 'Se a lacuna de capacidade aumentar, a infraestrutura francesa podera atender aos requisitos de conformidade sem permitir aplicacoes competitivas de IA.' OpenAI: 20 Bi USD em ARR em 2025 (x3 em um ano).",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Capitulo VII",
    filename="Capitulo_VII_Recomendacoes_PT-BR.docx"
)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

LANGS = [EN, FR, BR]

def build_all(out_dir: Path) -> None:
    for lp in LANGS:
        log.info("Building Chapter VII [%s] -> %s", lp.code, lp.filename)
        doc = init_document()
        # Figures
        fig_dir = out_dir / "figures_ch7"
        
        # Build document
        add_cover(doc, lang=lp.code, chapter_label=lp.label, chapter_subtitle=lp.title)
        add_chapter_header(doc, label=lp.label, title=lp.title, intro=lp.intro)
        
        for title, paragraphs in lp.sections:
            render_section(doc, title, paragraphs)
            
            # Insert images after specific sections
            if title.startswith("7.1.1"):
                img_path = fig_dir / f"Fig_7.1_Capex_Gap_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
            elif title.startswith("7.1.2"):
                img_path = fig_dir / f"Fig_7.2_Recommendations_Heatmap_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
            elif title.startswith("7.2.1"):
                img_path = fig_dir / f"Fig_7.3_FSov_Trajectory_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
            elif title.startswith("7.3.1"):
                img_path = fig_dir / f"Fig_7.4_Energy_Mix_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
            elif title.startswith("7.4.2"):
                img_path = fig_dir / f"Fig_7.5_Risk_Reduction_{lp.code}.png"
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
