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

Chapter VI - Consequences for France and Europe - trilingual generator.

Generates the .docx for Chapter VI in English, French, and Brazilian Portuguese.
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
log = logging.getLogger("chapter6_trilingual")

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
    label="CHAPTER VI",
    title="Consequences for France and Europe",
    intro=(
        "The previous chapters have established the diagnostic (III), the mechanisms (IV) and the "
        "possible trajectories (V). This chapter outlines the concrete consequences for French and "
        "European actors, distinguishing three levels of analysis: sectoral breakdown (which sectors "
        "are most exposed?), differentiation by actor type (large groups, SMEs, startups, public sector), "
        "and second-order effects (brain drain, R&D offshoring, normative fragmentation). The analysis "
        "relies mainly on scenario A (the most probable) and scenario B (the most severe), while signaling "
        "bifurcations specific to scenarios C and D."
    ),
    sections=[
        ("6.1 Sectoral analysis: differentiated exposure to compute asymmetry", []),
        ("6.1.1 Financial services: advanced dependence", [
            "The French financial sector is the most advanced in AI adoption and, paradoxically, the most exposed to the risk of geopolitical vendor lock-in. BNP Paribas, Société Générale, Crédit Agricole, and AXA are massively deploying AI solutions for fraud detection, credit scoring, algorithmic trading, and risk optimization. AXA and BNP Paribas are among the first enterprise customers of Mistral AI in France.[1] These deployments rely largely on US cloud infrastructure (AWS for BNP Paribas, Azure for Société Générale). Productivity gains observed in the global financial sector are among the highest (the IMF cites microeconomic gains of 20 to 40 percent on compliance and analysis tasks), as it is a cognitively intensive and high-wage sector—two factors that maximize the return on investment of automation.[2]",
            "The risk specific to the financial sector is twofold. On one hand, European regulations (DORA, AI Act, GDPR) impose localization and auditability requirements that create tension with the dependence on US cloud: French banks must guarantee that their customers' data is not accessible to US authorities (CLOUD Act), while depending on AWS and Azure for computing power. On the other hand, under scenario B, an increase in the cost of accessing cutting-edge AI cloud would directly hit the most compute-intensive applications (risk models, Monte Carlo simulations, training of specialized LLMs). The productivity gap with US banks (JPMorgan, Goldman Sachs, which each invest several billion a year in AI) would widen by an additional 3 to 5 points per year.",
        ]),
        ("6.1.2 Automotive and aerospace industry: compute-intensive and vulnerable", [
            "The European automotive industry has already experienced a revealing precedent: the 2022 semiconductor shortage cost the EU auto sector alone approximately 100 billion euros (Chapter IV). AI transforms this sector on three axes: autonomous driving (training perception models, requiring tens of thousands of GPUs), production optimization (digital twins, predictive maintenance), and assisted design (aerodynamic simulation, virtual crash tests). Stellantis (formerly PSA) signed a 100 million euro partnership with Mistral AI to integrate AI across all its businesses, from transport to logistics.[3]",
            "Aerospace (Airbus, Safran, Thales, Dassault Aviation) presents a similar profile but aggravated by the defense dimension. Complex aerodynamic simulations, fleet predictive maintenance, and the design of autonomous weapons systems are extremely compute-intensive applications. Airbus relies on AWS and Azure for its cloud workloads. Under scenario B, restrictions on advanced GPUs would directly affect simulation capabilities; under scenario D, pressure to repatriate workloads to sovereign infrastructure would create considerable transition costs but would reduce strategic vulnerability.",
        ]),
        ("6.1.3 Healthcare and life sciences: data sovereignty issue", [
            "The healthcare sector presents a different vulnerability: compute intensity is lower (except for AI-driven drug discovery, which requires massive GPU clusters), but data sensitivity is maximal. The European Health Data Space (EHDS) strictly regulates the processing of medical data. Sanofi, one of the world's leading pharmaceutical groups, has invested 1 billion dollars in AI partnerships (including OpenAI and Owkin, a French startup specialized in AI for clinical research).[4] Novo Nordisk, although Danish, illustrates the European challenge: more than 8.2 billion dollars in R&D in 2024, with increasing use of AI for human body digital twins and accelerating drug discovery.[5]",
            "The impact of protectionism scenarios here is indirect but structural. If access to cutting-edge GPUs is restricted, AI drug discovery projects (which require model training for several weeks on thousands of GPUs) will be slowed down or offshored to the United States. Owkin, founded in Paris, has already opened offices in New York and could transfer its most compute-intensive workloads there if European costs became prohibitive.",
        ]),
        ("6.1.4 Robotics and manufacturing industry: the energy factor", [
            "AI robotics and industrial automation add an additional energy dimension. Training perception and control models for industrial robots is compute-intensive, but it is especially the large-scale deployment of AI-equipped robots (edge computing, embedded inference) that multiplies industrial energy demand. The convergence of data centers + edge compute + robots could add 20 to 30 percent to industrial energy demand by 2030 (Chapter III), an estimate that is still poorly quantified but recognized as a critical sensitivity variable.",
            "France possesses significant players: Exotec (logistics robotics, valued at more than 2 billion euros), Wandercraft (exoskeletons), Aldebaran/SoftBank Robotics (humanoid robots, founded in France). These companies depend on AI hardware (Nvidia GPUs, specialized chips) to train and deploy their systems. Under scenario B, GPU quotas would directly affect the pace of innovation; under scenarios C and D, investment in European Gigafactories would provide the necessary compute, but with a 2 to 3-year delay relative to US competitors.",
        ]),
        ("6.2 Differentiation by actor type", []),
        ("6.2.1 Large groups: constrained beneficiaries", [
            "Large French companies (CAC 40 and SBF 120) are the primary short-term beneficiaries of AI and the most exposed to medium-term dependence. They have the budgets to access the US cloud and the teams to deploy AI, but this adoption reinforces vendor lock-in with each iteration. The cost of migration (switching cost) from a complete cloud ecosystem (AWS to OVHcloud, for example) is estimated at 12-18 months of development and millions of euros in re-architecture, making it economically irrational except under strong regulatory constraint. Under scenario A, they continue to adopt AI via the US cloud, accumulating increasing dependence but benefiting from real productivity gains. Under scenario B, the sudden increase in compute costs puts them in a dilemma: absorb the extra costs (margin compression) or slow down AI projects (loss of competitiveness).",
        ]),
        ("6.2.2 Industrial SMEs and mid-caps: progressive exclusion", [
            "SMEs and mid-sized companies represent the French industrial fabric (4,000 mid-caps, 140,000 SMEs). Their access to cutting-edge AI is already constrained by costs: training a specialized model costs several hundred thousand euros, out of reach for most SMEs without subsidies. McKinsey (December 2025) observes that AI productivity gains are concentrated in large companies, creating an intra-European productivity gap between adopting and non-adopting companies.[6] Under scenario B, rising compute costs widen this gap: SMEs give up on cutting-edge AI and opt for degraded solutions (lightweight open-source models, local inference on limited hardware), progressively losing competitiveness against US SMEs that benefit from domestic compute exempt from tariffs.",
            "EuroHPC AI Factories, designed to give priority access to startups and SMEs, could mitigate this effect (scenarios C and D). But their total capacity (approximately 475,000 GPUs, the order of magnitude of a single US hyperscaler) is insufficient to serve the entire European economic fabric. The gap between the public supply of compute and market demand is structurally deficient.[7]",
        ]),
        ("6.2.3 French AI startups: between championship and dependence", [
            "The French AI startup ecosystem is the most dynamic in Europe. Mistral AI, valued at 11.7 billion euros (September 2025 Series C, led by ASML), is the European champion of generative AI.[8] The company has raised a total of 2.8 billion euros, employs about 700 people, and is developing Mistral Compute, a sovereign cloud platform with 18,000 Nvidia Grace Blackwell GPUs deployed in a 40 MW data center in Essonne, powered by French nuclear energy.[9] In February 2026, Mistral announced a 1.2 billion euro investment for a data center in Sweden (Borlänge), and the acquisition of the startup Koyeb to strengthen Mistral Compute.[10]",
            "The Mistral case illustrates both the potential and the limits of European AI sovereignty. Potential side: the company proves that a European startup can reach global scale, attract massive investments (ASML, Nvidia, Bpifrance, a16z), and build its own compute infrastructure. Limits side: Mistral remains dependent on Nvidia GPUs (no European alternative for AI accelerators), initially used Microsoft Azure and Google Cloud for training, and its investor Microsoft holds a strategic position (conversion of a 15 million EUR investment). The company illustrates application-level sovereignty (models, platforms, services) without hardware-level sovereignty—precisely the junior partner position described in scenario C.",
            "Beyond Mistral, the French ecosystem includes Hugging Face (valued at 4.5 billion dollars, model hosting platform, headquartered in Paris but infrastructure in the US), LightOn (specialized models for enterprise), H Company (formerly Holistic AI), Owkin (AI for healthcare), and Scaleway (French sovereign cloud, first European access to Nvidia Blackwell GPUs). AI funding in Europe grew by 55 percent in the first quarter of 2025, with 12 new unicorns in the first half. France is for the fifth consecutive year the primary European destination for foreign AI investment.[11]",
        ]),
        ("6.2.4 Public sector and defense: the sovereignty imperative", [
            "The French public sector represents a special case. The Ministry of the Armed Forces launched GenIAl.intradef in February 2025, a secure conversational agent based on Mistral AI.[12] The Directorate General of Armaments (DGA) and ANSSI are working on classification frameworks for sovereign AI. For defense and intelligence, dependence on the US cloud is unacceptable regardless of the scenario: classified workloads must be executed on national infrastructure. This captive market provides a guaranteed demand base for sovereign cloud providers (OVHcloud S3ns, Thales S3ns, Scaleway), but its size remains limited compared to the commercial market.",
        ]),
        ("6.3 Second-order effects", []),
        ("6.3.1 Brain drain and capture of AI talent", [
            "Compute asymmetry produces a talent attraction effect toward the United States. European AI researchers and engineers are attracted by: (i) US compensation packages (salary + equity), which are structurally superior to European standards; (ii) access to cutting-edge compute, a necessary condition for frontier research; (iii) the ecosystem (proximity to Big Tech, VCs, research community). Martens (Bruegel) notes that personnel cost (salaries + equity) is often the most important component of the cost of developing an AI model, and that US companies compete fiercely to recruit the world's best talent.[13]",
            "This brain drain directly weakens the L(r) factor of European CACI. It is partially compensated by the excellence of French training (ENS, Polytechnique, INRIA, Parisian universities) which form a continuous flow of talent—but a significant proportion leaves for the United States after their PhD. Mistral AI, founded by alumni of DeepMind and Meta, illustrates the possibility of retaining (or repatriating) talent, but it is the exception rather than the rule. Under scenarios C and D, the deployment of Gigafactories and Mistral Compute could create an ecosystem attractive enough to retain more talent.",
        ]),
        ("6.3.2 R&D Offshoring", [
            "Compute asymmetry produces pressure to offshore the most calculation-intensive R&D activities. This phenomenon is already observable: the largest AI R&D centers of European companies are often located in the US (Bosch AI in Sunnyvale, SAP AI in Palo Alto, DeepMind in London but owned by Google). Under scenario B, this pressure intensifies: 15 to 20 percent of critical AI projects could be offshored to the United States (notably to areas near Nvidia/TSMC fabs in Arizona, or Virginia data centers). Under scenarios C and D, offshoring is mitigated by the availability of local compute, but does not disappear completely because the FLOP cost gap remains positive in favor of the United States in all scenarios.",
        ]),
        ("6.3.3 Normative fragmentation: the AI Act as a double-edged sword", [
            "The European AI Act, in progressive application since 2024, produces ambivalent effects in the context of US protectionism. On one hand, it creates additional compliance costs for European companies (model transparency, copyright management in training data, security audits). Draghi (2024) observed that European data restrictions create high costs and slow down model training. Martens (Bruegel, 2025) notes that the AI Omnibus risks prolonging regulatory uncertainty for at least two more years.[14]",
            "On the other hand, the AI Act creates an entry barrier for US competitors—an unintended protectionist effect that could favor European actors compliant by design (Mistral, whose transparent and auditable models are naturally aligned with the AI Act). The Code of Practice on copyright and training data, published in July 2025, imposes constraints that closed models (OpenAI, Anthropic) have more difficulty satisfying. Under scenarios B and D, where geopolitical mistrust is maximal, the AI Act could become a de facto tool for European preference, analogous to the GDPR which favored the emergence of European solutions in personal data processing.",
        ]),
        ("6.4 The France AI ecosystem: unique assets and structural vulnerabilities", [
            "The differentiated analysis of the preceding sections allows for a balance sheet of France's specific assets and vulnerabilities in the context of AI protectionism, presented in Table 15.",
            "On the assets side, France has unique comparative advantages in Europe: a nuclear fleet (65-70 percent of the electricity mix) that produces competitive and low-carbon electricity, a generative AI champion (Mistral AI valued at 11.7 billion EUR) with ASML as an industrial partner, centers of excellence in training (ENS, Polytechnique, INRIA, CNRS/IDRIS, more than 150 startups passed through Jean Zay), 109 billion EUR in private AI commitments announced at the February 2025 Summit, and the top European destination for foreign AI investments (five consecutive years).",
            f"On the vulnerabilities side, France remains structurally dependent: absence of an AI hardware champion (no GPU/ASIC design), limited installed compute (about 5 percent of the global total for France alone, US/France ratio of the order of 30:1—consistent with the US/EU(13) raw ratio of {fmt_en(us_eu_raw, 1)}:1 since France represents the majority of installed EU compute), post-doctoral brain drain to the US, slow permitting (24+ months), electricity grid under tension (+10 GW needed according to RTE), US cloud dependence on 70-80 percent of AI workloads, and AI Act compliance surcharges in a context of regulatory uncertainty (omnibus 2+ years).",
        ]),
        ("6.5 Synthesis: France facing three futures", [
            "The analysis in this chapter converges toward three possible configurations for France by 2030, corresponding to the trajectories of the scenarios in Chapter V.",
            "Configuration 1: Dependent Consumer (scenarios A and B). France adopts AI via the US cloud, gains productivity in the short term, but accumulates structural dependence that places it in a position of vulnerability to any US hardening. Large groups prosper but are captive; SMEs are progressively excluded from cutting-edge AI; the most promising startups offshore their infrastructure to the United States. Brain drain accelerates. The productivity gap with the United States widens by 5 to 15 cumulative points over five years.",
            f"Configuration 2: Energy and Application Hub (scenario C). France exploits its nuclear advantage to become the energy center of gravity for AI in Europe. Mistral Compute and Gigafactories provide competitive local compute for inference and fine-tuning. French companies are sovereign in application but dependent on US hardware. On raw compute, the US/EU ratio drops from {fmt_en(us_eu_raw, 1)}:1 in 2025 toward 8-10:1 in 2030; on CACI Power Mode, the gap closes from {fmt_en(us_eu_caci, 2)}:1 toward 2.0-2.5:1. Brain drain is slowed by the existence of an attractive local ecosystem.",
            "Configuration 3: Pillar of European Sovereignty (scenario D). US protectionism catalyzes an unprecedented mobilization. France, thanks to its nuclear power, its excellent training, and Mistral, becomes the pillar of a European technological sovereignty effort. Massive investment (20 GW dedicated nuclear, RISC-V/DARE, Japan-Korea alliances) creates the conditions for a long-term catch-up, but the transition period (2026-2028) is painful. Execution risk is maximal: each year of delay in infrastructure prolongs vulnerability.",
            "Chapter VII will elaborate on the strategic recommendations corresponding to each of these configurations, distinguishing short-term measures (suitable regardless of the scenario) from structural investments (dependent on the chosen trajectory).",
        ]),
    ],
    tables=[
        ("Table 14. French sectoral exposure to AI compute asymmetry.",
         "Source: Author's construction, calibration on the public dashboard (April 2026).",
         [
             ["Sector", "Compute Intensity", "Data Sensitivity", "US Cloud Dependence", "Scenario B Risk"],
             ["Finance", "High", "Very high", "70-80%", "Lock-in + surcharges: -3 to -5 pts productivity/yr"],
             ["Auto/Aero", "Very high", "High", "60-70%", "Slowed simulations, R&D offshoring"],
             ["Health/Pharma", "High (drug disc.)", "Maximal", "40-60%", "Offshored drug discovery to US"],
             ["Robotics/Indus.", "High", "Moderate", "50-65%", "Slowed innovation + energy surcharge"],
             ["Defense/Space", "Very high", "Critical", "Variable", "Maximal strategic vulnerability"],
         ]),
        ("Table 15. Balance of France's assets/vulnerabilities in the context of AI protectionism.",
         "Source: Author's synthesis, calibration on the public dashboard (April 2026).",
         [
             ["France's Assets", "France's Vulnerabilities"],
             ["Nuclear energy (65-70% of mix): competitive cost, low carbon, data center deployment",
              "Absence of AI hardware champion (no GPU/ASIC design): Nvidia/AMD dependence"],
             ["Generative AI champion: Mistral AI (11.7B EUR val., Mistral Compute, ASML partner)",
              "Installed compute: France about 5% of global; raw US/France ratio around 30:1"],
             ["Excellence in training: ENS, X, INRIA, CNRS/IDRIS (Jean Zay, 150+ startups)",
              "Post-doctoral brain drain to US (salaries + equity + compute)"],
             ["109B EUR in private AI commitments (February 2025 Summit)",
              "Slow permitting (24+ months), saturated electricity grid (+10 GW RTE need)"],
             ["1st EU destination for foreign AI investments (5 consecutive years)",
              "US cloud dependence: 70-80% AI workloads on AWS/Azure/GCP"],
             ["AI Act: Mistral's compliance by design (open-source, auditability)",
              "AI Act: compliance surcharges, regulatory uncertainty (omnibus 2+ years)"],
         ]),
    ],
    notes=[
        "Mistral AI (2025), partnership press releases. AXA and BNP Paribas are among the first enterprise adopters of Mistral in France. See NVIDIA Blog (June 2025), 'France Bolsters National AI Strategy With NVIDIA Infrastructure'.",
        "IMF (March 2025), op. cit. Financial services are among the sectors with the highest AI exposure (Felten and Eloundou indices), with documented microeconomic gains of 20-40 percent on compliance and risk analysis tasks.",
        "Mistral AI / Wikipedia FR (2026). Stellantis (formerly PSA and Fiat-Chrysler) signed a 100 million EUR partnership with Mistral AI in April 2025. CMA CGM also concluded a 100 million EUR partnership.",
        "Sanofi (2024-2025), press releases. Owkin, founded in Paris in 2016, specializes in AI for clinical research and drug discovery.",
        "McKinsey (January 2026), 'Transforming Europe: Bold Moves to Lift a Continent'. Novo Nordisk: over 8.2 billion USD in R&D in 2024, use of digital twins and AI for drug discovery.",
        "McKinsey (December 2025), 'Accelerating Europe's AI Adoption'. The report observes that AI productivity gains are concentrated in 'lighthouse' companies, with gains reaching 40 percent in labor productivity and 50 percent in lead time reduction.",
        "Segler Consulting (June 2025), 'Europe's AI Gambit'. Total EU public capacity is estimated at about 57,000 accelerators in 2025, an order of magnitude lower than the infrastructure of a single US hyperscaler.",
        "Mistral AI (September 2025), Series C: 1.7 billion EUR raised, 11.7 billion EUR valuation. ASML lead investor (1.3 billion EUR for approx. 11%). Other investors: DST Global, a16z, Bpifrance, General Catalyst, Index Ventures, Lightspeed, Nvidia.",
        "Introl Blog (December 2025), 'France's AI Sovereignty Push'. Mistral Compute: 18,000 Grace Blackwell GPUs, 40 MW data center in Essonne (hosted by Scaleway/Eclairion), powered by nuclear energy. Planned launch 2026.",
        "Mistral AI / Wikipedia FR (February 2026). Borlänge data center (Sweden): 1.2 billion EUR, planned for 2027, via EcoDataCenter (renewable energy). Acquisition of Koyeb (February 17, 2026) to strengthen Mistral Compute's serverless offering.",
        "Dealroom (2025), cited in FinTech Weekly. AI funding in Europe +55% in Q1 2025, 12 new unicorns in H1 2025. France has been the #1 EU destination for foreign AI investments since 2020.",
        "Ministry of the Armed Forces (February 2025), launch of GenIAl.intradef. Secure conversational agent based on Mistral AI, deployed on sovereign infrastructure.",
        "Martens, B. (2024), Working Paper 18/2024, Bruegel, op. cit. AI personnel cost (salaries + equity) is often the most important component of model development, and US companies offer structurally superior packages.",
        "Martens, B. (2025), 'The European Union Needs More Than the Digital Omnibus to Make Digital Services Competitive', Bruegel. The AI Omnibus, intended to accelerate regulatory changes, is likely to take at least a year to be adopted, plus another year for complementary guidelines.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapter VI",
    filename="Chapter_VI_Consequences_France_Europe_EN.docx"
)

# ---------------------------------------------------------------------------
# Content - FRENCH (Reference)
# ---------------------------------------------------------------------------

FR = LangPack(
    code="FR",
    label="CHAPITRE VI",
    title="Consequences pour la France et l'Europe",
    intro=(
        "Les chapitres precedents ont etabli le diagnostic (III), les mecanismes (IV) et les "
        "trajectoires possibles (V). Ce chapitre decline les consequences concretes pour les "
        "acteurs francais et europeens, en distinguant trois niveaux d'analyse : la declinaison "
        "sectorielle (quels secteurs sont les plus exposes ?), la differenciation par type d'acteur "
        "(grands groupes, PME, startups, secteur public), et les effets de second ordre (brain "
        "drain, delocalisation de la R&D, fragmentation normative). L'analyse s'appuie principalement "
        "sur le scenario A (le plus probable) et le scenario B (le plus severe), tout en signalant "
        "les bifurcations propres aux scenarios C et D."
    ),
    sections=[
        ("6.1 Analyse sectorielle : exposition differenciee a l'asymetrie de compute", []),
        ("6.1.1 Services financiers : dependance avancee", [
            "Le secteur financier francais est le plus avance dans l'adoption de l'IA et, paradoxalement, le plus expose au risque de vendor lock-in geopolitique. BNP Paribas, Societe Generale, Credit Agricole et AXA deploient massivement des solutions IA pour la detection de fraude, le scoring credit, le trading algorithmique et l'optimisation des risques. AXA et BNP Paribas comptent parmi les premiers clients entreprises de Mistral AI en France.[1] Ces deploiements reposent en grande partie sur l'infrastructure cloud US (AWS pour BNP Paribas, Azure pour Societe Generale). Les gains de productivite observes dans le secteur financier mondial sont parmi les plus eleves (le FMI cite des gains microeconomiques de 20 a 40 pour cent sur les taches de conformite et d'analyse), car il s'agit d'un secteur a forte intensite cognitive et a hauts salaires - deux facteurs qui maximisent le retour sur investissement de l'automatisation.[2]",
            "Le risque specifique au secteur financier est double. D'une part, les regulations europeennes (DORA, AI Act, RGPD) imposent des exigences de localisation et d'auditabilite qui creent une tension avec la dependance au cloud US : les banques francaises doivent garantir que les donnees de leurs clients ne sont pas accessibles aux autorites americaines (CLOUD Act), tout en dependant d'AWS et Azure pour la puissance de calcul. D'autre part, sous scenario B, un rencherissement de l'acces au cloud IA de pointe frapperait directement les applications les plus intensives en compute (modeles de risque, simulations Monte Carlo, entrainement de LLM specialises). L'ecart de productivite avec les banques americaines (JPMorgan, Goldman Sachs, qui investissent chacune plusieurs milliards par an dans l'IA) se creuserait de 3 a 5 points supplementaires par an.",
        ]),
        ("6.1.2 Industrie automobile et aeronautique : compute-intensif et vulnerable", [
            "L'industrie automobile europeenne a deja subi un precedent revelateur : la penurie de semi-conducteurs de 2022 a coute environ 100 milliards d'euros au seul secteur auto UE (chapitre IV). L'IA transforme ce secteur sur trois axes : conduite autonome (entrainement de modeles de perception, necessitant des dizaines de milliers de GPU), optimisation de la production (digital twins, maintenance predictive), et conception assistee (simulation aerodynamique, crash tests virtuels). Stellantis (issu de PSA) a signe un partenariat de 100 millions d'euros avec Mistral AI pour integrer l'IA dans l'ensemble de ses metiers, du transport a la logistique.[3]",
            "L'aeronautique (Airbus, Safran, Thales, Dassault Aviation) presente un profil similaire mais aggrave par la dimension defense. Les simulations aerodynamiques complexes, la maintenance predictive de flottes et la conception de systemes d'armes autonomes sont des applications extremement intensives en compute. Airbus s'appuie sur AWS et Azure pour ses workloads cloud. Sous scenario B, les restrictions sur les GPU avancees toucheraient directement les capacites de simulation ; sous scenario D, la pression pour rapatrier les workloads sur infrastructure souveraine creerait des couts de transition considerables mais reduirait la vulnerabilite strategique.",
        ]),
        ("6.1.3 Sante et sciences de la vie : enjeu de souverainete des donnees", [
            "Le secteur de la sante presente une vulnerabilite differente : l'intensite en compute est moindre (sauf pour la decouverte de medicaments par IA, qui necessite des clusters GPU massifs), mais la sensibilite des donnees est maximale. L'Espace europeen des donnees de sante (EHDS) encadre strictement le traitement des donnees medicales. Sanofi, l'un des premiers groupes pharmaceutiques mondiaux, a investi 1 milliard de dollars dans des partenariats IA (dont OpenAI et Owkin, startup francaise specialisee en IA pour la recherche clinique).[4] Novo Nordisk, bien que danois, illustre l'enjeu europeen : plus de 8,2 milliards de dollars de R&D en 2024, avec un recours croissant a l'IA pour les digital twins du corps humain et l'acceleration de la decouverte de medicaments.[5]",
            "L'impact des scenarios de protectionnisme est ici indirect mais structurel. Si l'acces aux GPU de pointe est restreint, les projets de drug discovery par IA (qui necessitent des entrainements de modeles de plusieurs semaines sur des milliers de GPU) seront ralentis ou delocalises vers les Etats-Unis. Owkin, fonde a Paris, a deja ouvert des bureaux a New York et pourrait y transferer ses workloads les plus intensifs en compute si les couts europeens devenaient prohibitifs.",
        ]),
        ("6.1.4 Robotique et industrie manufacturiere : le facteur energie", [
            "La robotique IA et l'automatisation industrielle ajoutent une dimension energetique supplementaire. L'entrainement de modeles de perception et de controle pour robots industriels est compute-intensif, mais c'est surtout le deploiement a grande echelle de robots equipes d'IA (edge computing, inference embarquee) qui multiplie la demande energetique industrielle. La convergence data centers + edge compute + robots pourrait ajouter 20 a 30 pour cent a la demande energetique industrielle d'ici 2030 (chapitre III), une estimation encore peu quantifiee mais reconnue comme variable de sensibilite critique.",
            "La France possede des acteurs significatifs : Exotec (robotique logistique, valorisee a plus de 2 milliards d'euros), Wandercraft (exosquelettes), Aldebaran/SoftBank Robotics (robots humanoides, fonde en France). Ces entreprises dependent du hardware IA (GPU Nvidia, puces specialisees) pour entrainer et deployer leurs systemes. Sous scenario B, les quotas de GPU affecteraient directement le rythme d'innovation ; sous les scenarios C et D, l'investissement dans les Gigafactories europeennes fournirait le compute necessaire, mais avec un retard de 2 a 3 ans sur les concurrents americains.",
        ]),
        ("6.2 Differenciation par type d'acteur", []),
        ("6.2.1 Grands groupes : beneficiaires contraints", [
            "Les grandes entreprises francaises (CAC 40 et SBF 120) sont les premieres beneficiaires de l'IA a court terme et les plus exposees a la dependance a moyen terme. Elles disposent des budgets pour acceder au cloud US et des equipes pour deployer l'IA, mais cette adoption renforce le vendor lock-in a chaque iteration. Le cout de migration (switching cost) d'un ecosysteme cloud complet (AWS vers OVHcloud, par exemple) est estime a 12-18 mois de developpement et des millions d'euros de rearchitecture, ce qui le rend economiquement irrationnel sauf contrainte reglementaire forte. Sous scenario A, ils continuent d'adopter l'IA via le cloud US, accumulant une dependance croissante mais beneficiant de gains de productivite reels. Sous scenario B, le rencherissement soudain du compute les place face a un dilemme : absorber les surcouts (compression des marges) ou ralentir les projets IA (perte de competitivite).",
        ]),
        ("6.2.2 PME et ETI industrielles : exclusion progressive", [
            "Les PME et entreprises de taille intermediaire representent le tissu industriel francais (4 000 ETI, 140 000 PME). Leur acces a l'IA de pointe est deja contrait par les couts : un entrainement de modele specialise coute plusieurs centaines de milliers d'euros, hors de portee de la plupart des PME sans subvention. McKinsey (decembre 2025) observe que les gains de productivite IA sont concentres dans les grandes entreprises, creant un fosse de productivite intra-europeen entre les entreprises adoptees et les non-adoptees.[6] Sous scenario B, la hausse des couts de compute elargit ce fosse : les PME renoncent a l'IA de pointe et optent pour des solutions degradees (modeles open-source legers, inference locale sur hardware limite), perdant progressivement en competitivite face aux PME americaines qui beneficient du compute domestique exempte de tarifs.",
            "Les AI Factories EuroHPC, concues pour donner la priorite d'acces aux startups et PME, pourraient attenuer cet effet (scenarios C et D). Mais leur capacite totale (environ 475 000 GPU, ordre de grandeur d'un seul hyperscaler US) est insuffisante pour servir l'ensemble du tissu economique europeen. Le gap entre l'offre publique de compute et la demande du marche est structurellement deficitaire.[7]",
        ]),
        ("6.2.3 Startups IA francaises : entre championnat et dependance", [
            "L'ecosysteme startup IA francais est le plus dynamique d'Europe. Mistral AI, valorisee a 11,7 milliards d'euros (serie C de septembre 2025, menee par ASML), est le champion europeen de l'IA generative.[8] L'entreprise a leve 2,8 milliards d'euros au total, emploie environ 700 personnes, et developpe Mistral Compute, une plateforme cloud souveraine avec 18 000 GPU Nvidia Grace Blackwell deployees dans un data center de 40 MW en Essonne, alimente par l'energie nucleaire francaise.[9] En fevrier 2026, Mistral a annonce un investissement de 1,2 milliard d'euros pour un data center en Suede (Borlange), et l'acquisition de la startup Koyeb pour renforcer Mistral Compute.[10]",
            "Le cas Mistral illustre a la fois le potentiel et les limites de la souverainete IA europeenne. Cote potentiel : l'entreprise prouve qu'une startup europeenne peut atteindre l'echelle mondiale, attirer des investissements massifs (ASML, Nvidia, Bpifrance, a16z), et construire une infrastructure compute propre. Cote limites : Mistral reste dependante des GPU Nvidia (pas d'alternative europeenne pour les accelerateurs IA), a initialement utilise Microsoft Azure et Google Cloud pour l'entrainement, et son investisseur Microsoft detient une position strategique (conversion d'un investissement de 15 millions EUR). L'entreprise illustre la souverainete de niveau applicatif (modeles, plateformes, services) sans souverainete de niveau hardware - precisement la position de junior partner decrite dans le scenario C.",
            "Au-dela de Mistral, l'ecosysteme francais comprend Hugging Face (valorise a 4,5 milliards de dollars, plateforme d'hebergement de modeles, siege a Paris mais infrastructure aux Etats-Unis), LightOn (modeles specialises pour l'entreprise), H Company (anciennement Holistic AI), Owkin (IA pour la sante), et Scaleway (cloud souverain francais, premier acces europeen aux GPU Nvidia Blackwell). Le financement IA en Europe a progresse de 55 pour cent au premier trimestre 2025, avec 12 nouvelles licornes au premier semestre. La France est pour la cinquieme annee consecutive la premiere destination europeenne pour les investissements etrangers en IA.[11]",
        ]),
        ("6.2.4 Secteur public et defense : l'imperatif de souverainete", [
            "Le secteur public francais represente un cas a part. Le ministere des Armees a lance en fevrier 2025 GenIAl.intradef, un agent conversationnel securise base sur Mistral AI.[12] La Direction generale de l'armement (DGA) et l'ANSSI travaillent sur des cadres de classification pour l'IA souveraine. Pour la defense et le renseignement, la dependance au cloud US est inacceptable quel que soit le scenario : les workloads classifies doivent etre executes sur infrastructure nationale. Ce marche captif fournit un socle de demande garanti pour les fournisseurs cloud souverains (OVHcloud S3ns, Thales S3ns, Scaleway), mais sa taille reste limitee par rapport au marche commercial.",
        ]),
        ("6.3 Effets de second ordre", []),
        ("6.3.1 Brain drain et captation du talent IA", [
            "L'asymetrie de compute produit un effet d'attraction du talent vers les Etats-Unis. Les chercheurs et ingenieurs IA europeens sont attires par : (i) les packages de remuneration americains (salaire + equity), qui sont structurellement superieurs aux standards europeens ; (ii) l'acces au compute de pointe, condition necessaire pour la recherche frontier ; (iii) l'ecosysteme (proximite des Big Tech, VC, communaute de recherche). Martens (Bruegel) note que le cout du personnel (salaires + equity) est souvent la composante la plus importante du cout de developpement d'un modele IA, et que les entreprises US se livrent une concurrence feroce pour recruter les meilleurs talents mondiaux.[13]",
            "Ce brain drain affaiblit directement le facteur L(r) du CACI europeen. Il est partiellement compense par l'excellence des formations francaises (ENS, Polytechnique, INRIA, universites parisiennes) qui forment un flux continu de talents - mais une proportion significative part aux Etats-Unis apres leur doctorat. Mistral AI, fondee par des alumni de DeepMind et Meta, illustre la possibilite de retenir (ou rapatrier) des talents, mais c'est l'exception plutot que la regle. Sous scenarios C et D, le deploiement de Gigafactories et de Mistral Compute pourrait creer un ecosysteme suffisamment attractif pour retenir davantage de talents.",
        ]),
        ("6.3.2 Delocalisation de la R&D", [
            "L'asymetrie de compute produit une pression a la delocalisation des activites de R&D les plus intensives en calcul. Ce phenomene est deja observable : les plus grands centres de R&D IA des entreprises europeennes sont souvent situes aux Etats-Unis (Bosch AI a Sunnyvale, SAP AI a Palo Alto, DeepMind a Londres mais propriete de Google). Sous scenario B, cette pression s'intensifie : 15 a 20 pour cent des projets IA critiques pourraient etre delocalises vers les Etats-Unis (notamment vers les zones a proximite des fabs Nvidia/TSMC en Arizona, ou des data centers de Virginie). Sous scenarios C et D, la delocalisation est attenuee par la disponibilite de compute local, mais ne disparait pas completement car l'ecart de cout FLOP reste positif en faveur des Etats-Unis dans tous les scenarios.",
        ]),
        ("6.3.3 Fragmentation normative : l'AI Act comme arme a double tranchant", [
            "L'AI Act europeen, entre en application progressive depuis 2024, produit des effets ambivalents dans le contexte du protectionnisme americain. D'un cote, il cree des couts de conformite supplementaires pour les entreprises europeennes (transparence des modeles, gestion des droits d'auteur dans les donnees d'entrainement, audits de securite). Draghi (2024) a observe que les restrictions europeennes sur les donnees creent des couts eleves et freinent l'entrainement des modeles. Martens (Bruegel, 2025) note que l'AI Omnibus risque de prolonger l'incertitude reglementaire pendant au moins deux ans supplementaires.[14]",
            "De l'autre cote, l'AI Act cree une barriere a l'entree pour les concurrents americains - un effet protectionniste involontaire qui pourrait favoriser les acteurs europeens conformes par design (Mistral, dont les modeles transparents et auditables sont naturellement alignes sur l'AI Act). Le Code of Practice sur les droits d'auteur et les donnees d'entrainement, publie en juillet 2025, impose des contraintes que les modeles fermes (OpenAI, Anthropic) ont plus de difficulte a satisfaire. Sous scenarios B et D, ou la mefiance geopolitique est maximale, l'AI Act pourrait devenir un outil de facto de preference europeenne, de maniere analogue au RGPD qui a favorise l'emergence de solutions europeennes dans le traitement des donnees personnelles.",
        ]),
        ("6.4 L'ecosysteme France IA : atouts uniques et vulnerabilites structurelles", [
            "L'analyse differenciee des sections precedentes permet de dresser un bilan des atouts et vulnerabilites specifiques de la France dans le contexte du protectionnisme IA, presente dans le Tableau 15.",
            "Cote atouts, la France dispose d'avantages comparatifs uniques en Europe : un parc nucleaire (65-70 pour cent du mix electrique) qui produit une electricite competitive et bas-carbone, un champion IA generative (Mistral AI valorise 11,7 milliards EUR) avec ASML comme partenaire industriel, des formations d'excellence (ENS, Polytechnique, INRIA, CNRS/IDRIS, plus de 150 startups passees par Jean Zay), 109 milliards EUR d'engagements prives IA annonces lors du Sommet de fevrier 2025, et la premiere destination europeenne pour les investissements IA etrangers (cinq annees consecutives).",
            f"Cote vulnerabilites, la France reste structurellement dependante : absence de champion hardware IA (pas de GPU/ASIC design), compute installe limite (environ 5 pour cent du global pour la France seule, ratio US/France de l'ordre de 30:1 - cohérent avec le ratio US/EU(13) brut de {fmt_fr(us_eu_raw, 1)}:1 puisque la France represente la majorite du compute UE installe), brain drain post-doctoral vers les US, permitting lent (24+ mois), reseau electrique sous tension (+10 GW necessaires selon RTE), dependance cloud US sur 70-80 pour cent des charges IA, et surcouts de conformite AI Act dans un contexte d'incertitude reglementaire (omnibus 2+ ans).",
        ]),
        ("6.5 Synthese : la France face a trois futurs", [
            "L'analyse de ce chapitre converge vers trois configurations possibles pour la France a l'horizon 2030, correspondant aux trajectoires des scenarios du chapitre V.",
            "Configuration 1 : Consommatrice dependante (scenarios A et B). La France adopte l'IA via le cloud US, gagne en productivite a court terme, mais accumule une dependance structurelle qui la place en position de vulnerabilite face a tout durcissement americain. Les grands groupes prosperent mais sont captifs ; les PME sont progressivement exclues de l'IA de pointe ; les startups les plus prometteuses delocalisent leur infrastructure aux Etats-Unis. Le brain drain s'accelere. L'ecart de productivite avec les Etats-Unis se creuse de 5 a 15 points cumules sur cinq ans.",
            f"Configuration 2 : Hub energetique et applicatif (scenario C). La France exploite son avantage nucleaire pour devenir le centre de gravite energetique de l'IA en Europe. Mistral Compute et les Gigafactories fournissent un compute local competitif pour l'inference et le fine-tuning. Les entreprises francaises sont souveraines dans l'application mais dependantes du hardware US. Sur le compute brut, le ratio US/UE descend de {fmt_fr(us_eu_raw, 1)}:1 en 2025 vers 8-10:1 en 2030 ; sur le CACI Power Mode, l'ecart se referme de {fmt_fr(us_eu_caci, 2)}:1 vers 2,0-2,5:1. Le brain drain est ralenti par l'existence d'un ecosysteme local attractif.",
            "Configuration 3 : Pilier de la souverainete europeenne (scenario D). Le protectionnisme americain catalyse une mobilisation inedite. La France, grace a son nucleaire, ses formations d'excellence et Mistral, devient le pilier d'un effort de souverainete technologique europeen. L'investissement massif (20 GW nucleaire dedie, RISC-V/DARE, alliances Japon-Coree) cree les conditions d'un rattrapage a long terme, mais la periode de transition (2026-2028) est douloureuse. Le risque d'execution est maximal : chaque annee de retard dans les infrastructures prolonge la vulnerabilite.",
            "Le chapitre VII elaborera les recommandations strategiques correspondant a chacune de ces configurations, en distinguant les mesures de court terme (adaptees quel que soit le scenario) des investissements structurels (dependants de la trajectoire choisie).",
        ]),
    ],
    tables=[
        ("Tableau 14. Exposition sectorielle francaise a l'asymetrie de compute IA.",
         "Source : construction de l'auteur, calibration sur le tableau de bord public (avril 2026).",
         [
             ["Secteur", "Intensite compute", "Sensibilite donnees", "Dependance cloud US", "Risque scenario B"],
             ["Finance", "Elevee", "Tres elevee", "70-80 pct", "Lock-in + surcouts : -3 a -5 pts productivite/an"],
             ["Auto/Aero", "Tres elevee", "Elevee", "60-70 pct", "Simulations ralenties, delocalisation R&D"],
             ["Sante/Pharma", "Haute (drug disc.)", "Maximale", "40-60 pct", "Drug discovery delocalisee US"],
             ["Robotique/Indus.", "Elevee", "Moderee", "50-65 pct", "Ralentissement innovation + surcout energie"],
             ["Defense/Spatial", "Tres elevee", "Critique", "Variable", "Vulnerabilite strategique maximale"],
         ]),
        ("Tableau 15. Bilan atouts / vulnerabilites de la France dans le contexte du protectionnisme IA.",
         "Source : synthese de l'auteur, calibration sur le tableau de bord public (avril 2026).",
         [
             ["Atouts France", "Vulnerabilites France"],
             ["Energie nucleaire (65-70 pct du mix) : cout competitif, bas carbone, deploiement data centers",
              "Absence de champion hardware IA (pas de GPU/ASIC design) : dependance Nvidia/AMD"],
             ["Champion IA generative : Mistral AI (11,7 Md EUR valoris., Mistral Compute, ASML partenaire)",
              "Compute installe : France environ 5 pct du global ; ratio US/France brut de l'ordre de 30:1"],
             ["Formation d'excellence : ENS, X, INRIA, CNRS/IDRIS (Jean Zay, 150+ startups)",
              "Brain drain post-doctorat vers US (salaires + equity + compute)"],
             ["109 Md EUR d'engagements prives IA (Sommet fevrier 2025)",
              "Permitting lent (24+ mois), reseau electrique sature (+10 GW besoin RTE)"],
             ["1ere destination UE investissements IA etrangers (5 ans consecutifs)",
              "Dependance cloud US : 70-80 pct workloads IA sur AWS/Azure/GCP"],
             ["AI Act : conformite par design de Mistral (open-source, auditabilite)",
              "AI Act : surcouts conformite, incertitude reglementaire (omnibus 2+ ans)"],
         ]),
    ],
    notes=[
        "Mistral AI (2025), communiques de partenariats. AXA et BNP Paribas figurent parmi les premiers adoptants entreprises de Mistral en France. Voir NVIDIA Blog (juin 2025), 'France Bolsters National AI Strategy With NVIDIA Infrastructure'.",
        "FMI (mars 2025), op. cit. Les services financiers sont parmi les secteurs a plus forte exposition IA (indices Felten et Eloundou), avec des gains microeconomiques documentes de 20-40 pour cent sur les taches de conformite et d'analyse de risque.",
        "Mistral AI / Wikipedia FR (2026). Stellantis (issu de PSA et Fiat-Chrysler) a signe un partenariat de 100 millions EUR avec Mistral AI en avril 2025. CMA CGM a egalement conclu un partenariat de 100 millions EUR.",
        "Sanofi (2024-2025), communiques de presse. Owkin, fonde a Paris en 2016, est specialise dans l'IA pour la recherche clinique et la decouverte de medicaments.",
        "McKinsey (janvier 2026), 'Transforming Europe: Bold Moves to Lift a Continent'. Novo Nordisk : plus de 8,2 milliards USD de R&D en 2024, utilisation de digital twins et d'IA pour la drug discovery.",
        "McKinsey (decembre 2025), 'Accelerating Europe's AI Adoption'. Le rapport observe que les gains de productivite IA sont concentres dans les entreprises lighthouse, avec des gains atteignant 40 pour cent de productivite du travail et 50 pour cent de reduction des delais.",
        "Segler Consulting (juin 2025), 'Europe's AI Gambit'. La capacite publique totale UE est estimee a environ 57 000 accelerateurs en 2025, soit un ordre de grandeur inferieur a l'infrastructure d'un seul hyperscaler US.",
        "Mistral AI (septembre 2025), serie C : 1,7 milliard EUR leves, valorisation 11,7 milliards EUR. ASML investisseur principal (1,3 milliard EUR pour environ 11 pct). Autres investisseurs : DST Global, a16z, Bpifrance, General Catalyst, Index Ventures, Lightspeed, Nvidia.",
        "Introl Blog (decembre 2025), 'France's AI Sovereignty Push'. Mistral Compute : 18 000 GPU Grace Blackwell, data center 40 MW en Essonne (heberge par Scaleway/Eclairion), alimente par energie nucleaire. Lancement prevu 2026.",
        "Mistral AI / Wikipedia FR (fevrier 2026). Data center de Borlange (Suede) : 1,2 milliard EUR, prevu pour 2027, via EcoDataCenter (energie renouvelable). Acquisition de Koyeb (17 fevrier 2026) pour renforcer l'offre serverless de Mistral Compute.",
        "Dealroom (2025), cite dans FinTech Weekly. Financement IA en Europe +55 pct au T1 2025, 12 nouvelles licornes au S1 2025. La France est 1ere destination UE pour les investissements etrangers en IA depuis 2020.",
        "Ministere des Armees (fevrier 2025), lancement de GenIAl.intradef. Agent conversationnel securise base sur Mistral AI, deploye sur infrastructure souveraine.",
        "Martens, B. (2024), Working Paper 18/2024, Bruegel, op. cit. Le cout du personnel IA (salaires + equity) est souvent la composante la plus importante du developpement d'un modele, et les entreprises americaines offrent des packages structurellement superieurs.",
        "Martens, B. (2025), 'The European Union Needs More Than the Digital Omnibus to Make Digital Services Competitive', Bruegel. L'AI Omnibus, cense accelerer les changements reglementaires, risque de prendre au moins un an pour etre adopte, plus un an pour les lignes directrices complementaires.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapitre VI",
    filename="Chapitre_VI_Consequences_France_Europe_FR.docx"
)

# ---------------------------------------------------------------------------
# Content - PORTUGUESE (BRAZIL)
# ---------------------------------------------------------------------------

BR = LangPack(
    code="PT-BR",
    label="CAPITULO VI",
    title="Consequencias para a Franca e a Europa",
    intro=(
        "Os capitulos anteriores estabeleceram o diagnostico (III), os mecanismos (IV) e as "
        "trajetorias possiveis (V). Este capitulo descreve as consequencias concretas para os "
        "atores franceses e europeus, distinguindo tres niveis de analise: decomposicao setorial "
        "(quais setores estao mais expostos?), diferenciacao por tipo de ator (grandes grupos, "
        "PMEs, startups, setor publico) e efeitos de segunda ordem (fuga de cerebros, offshoring "
        "de P&D, fragmentacao normativa). A analise baseia-se principalmente no cenario A "
        "(o mais provavel) e no cenario B (o mais severo), sinalizando bifurcacoes especificas "
        "para os cenarios C e D."
    ),
    sections=[
        ("6.1 Analise setorial: exposicao diferenciada a assimetria de compute", []),
        ("6.1.1 Servicos financeiros: dependencia avancada", [
            "O setor financeiro frances e o mais avancado na adocao de IA e, paradoxalmente, o mais exposto ao risco de vendor lock-in geopolitico. BNP Paribas, Société Générale, Crédit Agricole e AXA estao implantando massivamente solucoes de IA para deteccao de fraude, analise de credito, trading algoritmico e otimizacao de riscos. AXA e BNP Paribas estao entre os primeiros clientes corporativos da Mistral AI na Franca.[1] Essas implantacoes dependem em grande parte da infraestrutura de nuvem dos EUA (AWS para o BNP Paribas, Azure para a Société Générale). Os ganhos de produtividade observados no setor financeiro global estao entre os mais altos (o FMI cita ganhos microeconomicos de 20 a 40 por cento em tarefas de conformidade e analise), pois e um setor cognitivamente intensivo e com altos salarios - dois fatores que maximizam o retorno sobre o investimento da automacao.[2]",
            "O risco especifico ao setor financeiro e duplo. Por um lado, as regulamentacoes europeias (DORA, AI Act, GDPR) impoem requisitos de localizacao e auditabilidade que criam tensao com a dependencia da nuvem dos EUA: os bancos franceses devem garantir que os dados de seus clientes nao sejam acessiveis as autoridades dos EUA (CLOUD Act), enquanto dependem da AWS e Azure para poder computacional. Por outro lado, sob o cenario B, um aumento no custo de acesso a nuvem de IA de ponta atingiria diretamente as aplicacoes mais intensivas em computacao (modelos de risco, simulacoes de Monte Carlo, treinamento de LLMs especializados). A lacuna de produtividade com os bancos dos EUA (JPMorgan, Goldman Sachs, que investem cada um varios bilhoes por ano em IA) aumentaria em adicionais 3 a 5 pontos por ano.",
        ]),
        ("6.1.2 Industria automotiva e aeroespacial: intensiva em computacao e vulneravel", [
            "A industria automotiva europeia ja experimentou um precedente revelador: a escassez de semicondutores de 2022 custou ao setor automotivo da UE sozinho aproximadamente 100 bilhoes de euros (Capitulo IV). A IA transforma este setor em tres eixos: conducao autonoma (treinamento de modelos de percepcao, exigindo dezenas de milhares de GPUs), otimizacao de producao (gemeos digitais, manutencao preditiva) e design assistido (simulacao aerodinamica, testes de colisao virtuais). A Stellantis (antiga PSA) assinou uma parceria de 100 milhoes de euros com a Mistral AI para integrar IA em todos os seus negocios, do transporte a logistica.[3]",
            "A aeroespacial (Airbus, Safran, Thales, Dassault Aviation) apresenta um perfil semelhante, mas agravado pela dimensao de defesa. Simulacoes aerodinamicas complexas, manutencao preditiva de frotas e o design de sistemas de armas autonomos sao aplicacoes extremamente intensivas em computacao. A Airbus depende da AWS e Azure para suas cargas de trabalho na nuvem. Sob o cenario B, restricoes em GPUs avancadas afetariam diretamente as capacidades de simulacao; sob o cenario D, a pressao para repatriar cargas de trabalho para infraestrutura soberana criaria custos de transicao consideraveis, mas reduziria a vulnerabilidade estrategica.",
        ]),
        ("6.1.3 Saude e ciencias da vida: questao de soberania de dados", [
            "O setor de saude apresenta uma vulnerabilidade diferente: a intensidade de computacao e menor (exceto para a descoberta de medicamentos por IA, que requer clusters de GPU massivos), mas a sensibilidade dos dados e maxima. O Espaco Europeu de Dados de Saude (EHDS) regulamenta estritamente o processamento de dados medicos. A Sanofi, um dos principais grupos farmaceuticos do mundo, investiu 1 bilhao de dolares em parcerias de IA (incluindo OpenAI e Owkin, uma startup francesa especializada em IA para pesquisa clinica).[4] A Novo Nordisk, embora dinamarquesa, ilustra o desafio europeu: mais de 8,2 bilhoes de dolares em P&D em 2024, com uso crescente de IA para gemeos digitais do corpo humano e aceleracao da descoberta de medicamentos.[5]",
            "O impacto dos cenarios de protecionismo aqui e indireto, mas estrutural. Se o acesso a GPUs de ponta for restrito, os projetos de descoberta de medicamentos por IA (que exigem treinamento de modelos por varias semanas em milhares de GPUs) serao retardados ou transferidos para os Estados Unidos. A Owkin, fundada em Paris, ja abriu escritorios em Nova York e poderia transferir suas cargas de trabalho mais intensivas em computacao para la se os custos europeus se tornassem proibitivos.",
        ]),
        ("6.1.4 Robotica e industria manufatureira: o fator energia", [
            "A robotica de IA e a automacao industrial adicionam uma dimensao energetica adicional. O treinamento de modelos de percepcao e controle para robos industriais e intensivo em computacao, mas e especialmente a implantacao em larga escala de robos equipados com IA (computacao de borda, inferencia embarcada) que multiplica a demanda energetica industrial. A convergencia de data centers + computacao de borda + robos poderia adicionar 20 a 30 por cento a demanda energetica industrial ate 2030 (Capitulo III), uma estimativa que ainda e mal quantificada, mas reconhecida como uma variavel de sensibilidade critica.",
            "A Franca possui atores significativos: Exotec (robotica logistica, avaliada em mais de 2 bilhoes de euros), Wandercraft (exoesqueletos), Aldebaran/SoftBank Robotics (robos humanoides, fundada na Franca). Essas empresas dependem de hardware de IA (GPUs Nvidia, chips especializados) para treinar e implantar seus sistemas. Sob o cenario B, as cotas de GPU afetariam diretamente o ritmo de inovacao; sob os cenarios C e D, o investimento em Gigafactories europeias forneceria a computacao necessaria, mas com um atraso de 2 a 3 anos em relacao aos concorrentes dos EUA.",
        ]),
        ("6.2 Diferenciacao por tipo de ator", []),
        ("6.2.1 Grandes grupos: beneficiarios limitados", [
            "As grandes empresas francesas (CAC 40 e SBF 120) sao as principais beneficiarias da IA a curto prazo e as mais expostas a dependencia a medio prazo. Elas tem orcamentos para acessar a nuvem dos EUA e as equipes para implantar a IA, mas essa adocao reforca o vendor lock-in a cada iteracao. O custo de migracao (switching cost) de um ecossistema de nuvem completo (AWS para OVHcloud, por exemplo) e estimado em 12-18 meses de desenvolvimento e milhoes de euros em reestruturacao de arquitetura, tornando-o economicamente irracional, exceto sob forte restricao regulatoria. Sob o cenario A, elas continuam a adotar a IA via nuvem dos EUA, acumulando dependencia crescente, mas beneficiando-se de ganhos reais de produtividade. Sob o cenario B, o aumento repentino nos custos de computacao as coloca em um dilema: absorver os custos extras (compressao de margens) ou desacelerar projetos de IA (perda de competitividade).",
        ]),
        ("6.2.2 PMEs e mid-caps industriais: exclusao progressiva", [
            "PMEs e empresas de medio porte representam o tecido industrial frances (4.000 mid-caps, 140.000 PMEs). Seu acesso a IA de ponta ja e limitado pelos custos: o treinamento de um modelo especializado custa centenas de milhares de euros, fora do alcance da maioria das PMEs sem subsidios. A McKinsey (dezembro de 2025) observa que os ganhos de produtividade da IA estao concentrados em grandes empresas, criando uma lacuna de produtividade intra-europeia entre empresas adotantes e nao adotantes.[6] Sob o cenario B, o aumento dos custos de computacao amplia essa lacuna: as PMEs desistem da IA de ponta e optam por solucoes degradadas (modelos de codigo aberto leves, inferencia local em hardware limitado), perdendo progressivamente competitividade contra as PMEs dos EUA que se beneficiam da computacao domestica isenta de tarifas.",
            "As AI Factories da EuroHPC, projetadas para dar acesso prioritario a startups e PMEs, poderiam mitigar esse efeito (cenarios C e D). Mas sua capacidade total (aproximadamente 475.000 GPUs, a ordem de grandeza de um unico hyperscaler dos EUA) e insuficiente para atender a todo o tecido economico europeu. A lacuna entre a oferta publica de computacao e a demanda do mercado e estruturalmente deficitaria.[7]",
        ]),
        ("6.2.3 Startups francesas de IA: entre o campeonato e a dependencia", [
            "O ecossistema de startups de IA frances e o mais dinamico da Europa. A Mistral AI, avaliada em 11,7 bilhoes de euros (Serie C de setembro de 2025, liderada pela ASML), e a campea europeia de IA generativa.[8] A empresa arrecadou um total de 2,8 bilhoes de euros, emprega cerca de 700 pessoas e esta desenvolvendo a Mistral Compute, uma plataforma de nuvem soberana com 18.000 GPUs Nvidia Grace Blackwell implantadas em um data center de 40 MW em Essonne, alimentado por energia nuclear francesa.[9] Em fevereiro de 2026, a Mistral anunciou um investimento de 1,2 bilhao de euros para um data center na Suecia (Borlänge) e a aquisicao da startup Koyeb para fortalecer a Mistral Compute.[10]",
            "O caso Mistral ilustra tanto o potencial quanto os limites da soberania europeia de IA. Lado do potencial: a empresa prova que uma startup europeia pode alcancar escala global, atrair investimentos massivos (ASML, Nvidia, Bpifrance, a16z) e construir sua propria infraestrutura de computacao. Lado dos limites: a Mistral continua dependente de GPUs Nvidia (sem alternativa europeia para aceleradores de IA), usou inicialmente Microsoft Azure e Google Cloud para treinamento, e seu investidor Microsoft detem uma posicao estrategica (conversao de um investimento de 15 milhoes de EUR). A empresa ilustra a soberania em nivel de aplicacao (modelos, plataformas, servicos) sem soberania em nivel de hardware - precisamente a posicao de parceiro junior descrita no cenario C.",
            "Alem da Mistral, o ecossistema frances inclui Hugging Face (avaliada em 4,5 bilhoes de dolares, plataforma de hospedagem de modelos, com sede em Paris, mas infraestrutura nos EUA), LightOn (modelos especializados para empresas), H Company (anteriormente Holistic AI), Owkin (IA para saude) e Scaleway (nuvem soberana francesa, primeiro acesso europeu as GPUs Nvidia Blackwell). O financiamento de IA na Europa cresceu 55 por cento no primeiro trimestre de 2025, com 12 novos unicornios no primeiro semestre. A Franca e, pelo quinto ano consecutivo, o principal destino europeu para investimentos estrangeiros em IA.[11]",
        ]),
        ("6.2.4 Setor publico e defesa: o imperativo da soberania", [
            "O setor publico frances representa um caso especial. O Ministerio das Forcas Armadas lancou o GenIAl.intradef em fevereiro de 2025, um agente conversacional seguro baseado na Mistral AI.[12] A Direcao Geral de Armamentos (DGA) e a ANSSI estao trabalhando em estruturas de classificacao para IA soberana. Para defesa e inteligencia, a dependencia da nuvem dos EUA e inaceitavel, independentemente do cenario: as cargas de trabalho classificadas devem ser executadas em infraestrutura nacional. Este mercado cativo fornece uma base de demanda garantida para provedores de nuvem soberana (OVHcloud S3ns, Thales S3ns, Scaleway), mas seu tamanho continua limitado em comparacao com o mercado comercial.",
        ]),
        ("6.3 Efeitos de segunda ordem", []),
        ("6.3.1 Fuga de cerebros e captura de talentos de IA", [
            "A assimetria de computacao produz um efeito de atracao de talentos para os Estados Unidos. Pesquisadores e engenheiros de IA europeus sao atraidos por: (i) pacotes de remuneracao dos EUA (salario + equity), que sao estruturalmente superiores aos padroes europeus; (ii) acesso a computacao de ponta, uma condicao necessaria para a pesquisa de fronteira; (iii) o ecossistema (proximidade com Big Techs, VCs, comunidade de pesquisa). Martens (Bruegel) observa que o custo de pessoal (salarios + equity) e frequentemente o componente mais importante do custo de desenvolvimento de um modelo de IA, e que as empresas dos EUA competem ferozmente para recrutar os melhores talentos do mundo.[13]",
            "Essa fuga de cerebros enfraquece diretamente o fator L(r) do CACI europeu. E parcialmente compensado pela excelencia do treinamento frances (ENS, Polytechnique, INRIA, universidades parisienses) que forma um fluxo continuo de talentos - mas uma proporcao significativa parte para os Estados Unidos apos o doutorado. A Mistral AI, fundada por ex-alunos da DeepMind e Meta, ilustra a possibilidade de reter (ou repatriar) talentos, mas e a excecao e nao a regra. Sob os cenarios C e D, a implantacao de Gigafactories e Mistral Compute poderia criar um ecossistema atraente o suficiente para reter mais talentos.",
        ]),
        ("6.3.2 Offshoring de P&D", [
            "A assimetria de computacao produz pressao para o offshoring das atividades de P&D mais intensivas em calculo. Este fenomeno ja e observavel: os maiores centros de P&D em IA de empresas europeias estao frequentemente localizados nos EUA (Bosch AI em Sunnyvale, SAP AI em Palo Alto, DeepMind em Londres, mas propriedade do Google). Sob o cenario B, essa pressao se intensifica: 15 a 20 por cento dos projetos criticos de IA poderiam ser transferidos para os Estados Unidos (notadamente para areas proximas as fabricas da Nvidia/TSMC no Arizona ou data centers da Virginia). Sob os cenarios C e D, o offshoring e mitigado pela disponibilidade de computacao local, mas nao desaparece completamente porque a lacuna de custo de FLOP permanece positiva em favor dos Estados Unidos em todos os cenarios.",
        ]),
        ("6.3.3 Fragmentacao normativa: o AI Act como uma faca de dois gumes", [
            "O AI Act europeu, em aplicacao progressiva desde 2024, produz efeitos ambivalentes no contexto do protecionismo dos EUA. Por um lado, cria custos de conformidade adicionais para as empresas europeias (transparencia do modelo, gestao de direitos autorais em dados de treinamento, auditorias de seguranca). Draghi (2024) observou que as restricoes de dados europeias criam altos custos e desaceleram o treinamento de modelos. Martens (Bruegel, 2025) observa que o AI Omnibus corre o risco de prolongar a incerteza regulatoria por pelo menos mais dois anos.[14]",
            "Por outro lado, o AI Act cria uma barreira de entrada para os concorrentes dos EUA - um efeito protecionista nao intencional que poderia favorecer atores europeus em conformidade por design (Mistral, cujos modelos transparentes e auditaveis estao naturalmente alinhados com o AI Act). O Codigo de Conduta sobre direitos autorais e dados de treinamento, publicado em julho de 2025, impoe restricoes que modelos fechados (OpenAI, Anthropic) tem mais dificuldade em satisfazer. Sob os cenarios B e D, onde a desconfianca geopolitica e maxima, o AI Act poderia se tornar uma ferramenta de fato para a preferencia europeia, de forma analoga ao GDPR que favoreceu a emergencia de solucoes europeias no processamento de dados pessoais.",
        ]),
        ("6.4 O ecossistema Franca IA: ativos unicos e vulnerabilidades estruturais", [
            "A analise diferenciada das secoes anteriores permite estabelecer um balanco dos ativos e vulnerabilidades especificos da Franca no contexto do protecionismo de IA, apresentado na Tabela 15.",
            "No lado dos ativos, a Franca possui vantagens comparativas unicas na Europa: uma frota nuclear (65-70 por cento da matriz eletrica) que produz eletricidade competitiva e de baixo carbono, uma campea de IA generativa (Mistral AI avaliada em 11,7 bilhoes de EUR) com a ASML como parceira industrial, centros de excelencia em treinamento (ENS, Polytechnique, INRIA, CNRS/IDRIS, mais de 150 startups que passaram por Jean Zay), 109 bilhoes de EUR em compromissos privados de IA anunciados na Cupula de fevereiro de 2025 e o principal destino europeu para investimentos estrangeiros em IA (cinco anos consecutivos).",
            f"No lado das vulnerabilidades, a Franca continua estruturalmente dependente: ausencia de uma campea de hardware de IA (sem design de GPU/ASIC), computacao instalada limitada (cerca de 5 por cento do total global para a Franca sozinha, razao EUA/Franca da ordem de 30:1 - consistente com a razao bruta EUA/UE(13) de {fmt_fr(us_eu_raw, 1)}:1, ja que a Franca representa a maioria da computacao instalada da UE), fuga de cerebros pos-doutorado para os EUA, licenciamento lento (24+ meses), rede eletrica sob tensao (+10 GW necessarios de acordo com a RTE), dependencia da nuvem dos EUA em 70-80 por cento das cargas de trabalho de IA e sobretaxas de conformidade do AI Act em um contexto de incerteza regulatoria (omnibus 2+ anos).",
        ]),
        ("6.5 Sintese: a Franca diante de tres futuros", [
            "A analise neste capitulo converge para tres configuracoes possiveis para a Franca ate 2030, correspondendo as trajetorias dos cenarios do Capitulo V.",
            "Configuracao 1: Consumidor Dependente (cenarios A e B). A Franca adota a IA via nuvem dos EUA, ganha produtividade no curto prazo, mas acumula dependencia estrutural que a coloca em uma posicao de vulnerabilidade a qualquer endurecimento dos EUA. Grandes grupos prosperam, mas sao cativos; PMEs sao progressivamente excluidas da IA de ponta; as startups mais promissoras transferem sua infraestrutura para os Estados Unidos. A fuga de cerebros acelera. A lacuna de produtividade com os Estados Unidos aumenta de 5 a 15 pontos cumulativos ao longo de cinco anos.",
            f"Configuracao 2: Hub de Energia e Aplicacao (cenario C). A Franca explora sua vantagem nuclear para se tornar o centro de gravidade energetico para IA na Europa. A Mistral Compute e as Gigafactories fornecem computacao local competitiva para inferencia e ajuste fino. As empresas francesas sao soberanas na aplicacao, mas dependentes do hardware dos EUA. Na computacao bruta, a razao EUA/UE cai de {fmt_fr(us_eu_raw, 1)}:1 em 2025 para 8-10:1 em 2030; no CACI Power Mode, a lacuna fecha de {fmt_fr(us_eu_caci, 2)}:1 para 2,0-2,5:1. A fuga de cerebros e retardada pela existencia de um ecossistema local atraente.",
            "Configuracao 3: Pilar da Soberania Europeia (cenario D). O protecionismo dos EUA catalisa uma mobilizacao sem precedentes. A Franca, gracas a sua energia nuclear, seu excelente treinamento e a Mistral, torna-se o pilar de um esforco europeu de soberania tecnologica. O investimento massivo (20 GW nucleares dedicados, RISC-V/DARE, aliancas Japao-Coreia) cria as condicoes para uma recuperacao a longo prazo, mas o periodo de transicao (2026-2028) e doloroso. O risco de execucao e maximo: cada ano de atraso na infraestrutura prolonga a vulnerabilidade.",
            "O Capitulo VII elaborara as recomendacoes estrategicas correspondentes a cada uma dessas configuracoes, distinguindo as medidas de curto prazo (adequadas independentemente do cenario) dos investimentos estruturais (dependentes da trajetoria escolhida).",
        ]),
    ],
    tables=[
        ("Tabela 14. Exposicao setorial francesa a assimetria de computacao de IA.",
         "Fonte: Construcao do autor, calibracao no painel publico (abril de 2026).",
         [
             ["Setor", "Intensidade Compute", "Sensibilidade Dados", "Dependencia Nuvem EUA", "Risco Cenario B"],
             ["Financas", "Alta", "Muito alta", "70-80%", "Lock-in + sobretaxas: -3 a -5 pts produtividade/ano"],
             ["Auto/Aero", "Muito alta", "Alta", "60-70%", "Simulacoes lentas, offshoring de P&D"],
             ["Saude/Farma", "Alta (drug disc.)", "Maxima", "40-60%", "Drug discovery transferida para EUA"],
             ["Robotica/Indus.", "Alta", "Moderada", "50-65%", "Inovacao lenta + sobretaxa energia"],
             ["Defesa/Espacial", "Muito alta", "Critica", "Variavel", "Vulnerabilidade estrategica maxima"],
         ]),
        ("Tabela 15. Balanco de ativos/vulnerabilidades da Franca no contexto do protecionismo de IA.",
         "Fonte: Sintese do autor, calibracao no painel publico (abril de 2026).",
         [
             ["Ativos da Franca", "Vulnerabilidades da Franca"],
             ["Energia nuclear (65-70% da matriz): custo competitivo, baixo carbono, implantacao de DC",
              "Ausencia de campea de hardware de IA (sem design de GPU/ASIC): dependencia Nvidia/AMD"],
             ["Campea de IA generativa: Mistral AI (val. 11,7B EUR, Mistral Compute, parceira ASML)",
              "Computacao instalada: Franca cerca de 5% do global; razao bruta EUA/Franca em torno de 30:1"],
             ["Excelencia em treinamento: ENS, X, INRIA, CNRS/IDRIS (Jean Zay, 150+ startups)",
              "Fuga de cerebros pos-doutorado para os EUA (salarios + equity + compute)"],
             ["109B EUR em compromissos privados de IA (Cupula de fevereiro de 2025)",
              "Licenciamento lento (24+ meses), rede eletrica saturada (+10 GW necessidade RTE)"],
             ["1º destino da UE para investimentos estrangeiros em IA (5 anos consecutivos)",
              "Dependencia da nuvem dos EUA: 70-80% das cargas de trabalho de IA em AWS/Azure/GCP"],
             ["AI Act: conformidade por design da Mistral (codigo aberto, auditabilidade)",
              "AI Act: sobretaxas de conformidade, incerteza regulatoria (omnibus 2+ anos)"],
         ]),
    ],
    notes=[
        "Mistral AI (2025), comunicados de parceria. AXA e BNP Paribas estao entre os primeiros adotantes corporativos da Mistral na Franca. Veja o Blog da NVIDIA (junho de 2025), 'França Reforça Estratégia Nacional de IA com Infraestrutura NVIDIA'.",
        "FMI (marco de 2025), op. cit. Os servicos financeiros estao entre os setores com maior exposicao a IA (indices Felten e Eloundou), com ganhos microeconomicos documentados de 20-40 por cento em tarefas de conformidade e analise de risco.",
        "Mistral AI / Wikipedia FR (2026). A Stellantis (antiga PSA e Fiat-Chrysler) assinou uma parceria de 100 milhoes de euros com a Mistral AI em abril de 2025. A CMA CGM tambem concluiu uma parceria de 100 milhoes de euros.",
        "Sanofi (2024-2025), comunicados a imprensa. Owkin, fundada em Paris em 2016, especializa-se em IA para pesquisa clinica e descoberta de medicamentos.",
        "McKinsey (janeiro de 2026), 'Transforming Europe: Bold Moves to Lift a Continent'. Novo Nordisk: mais de 8,2 bilhoes de dolares em P&D em 2024, uso de gemeos digitais e IA para descoberta de medicamentos.",
        "McKinsey (dezembro de 2025), 'Accelerating Europe's AI Adoption'. O relatorio observa que os ganhos de produtividade da IA estao concentrados em empresas 'farol', com ganhos chegando a 40 por cento na produtividade do trabalho e 50 por cento na reducao de prazos.",
        "Segler Consulting (junho de 2025), 'Europe's AI Gambit'. A capacidade publica total da UE e estimada em cerca de 57.000 aceleradores em 2025, uma ordem de grandeza inferior a infraestrutura de um unico hyperscaler dos EUA.",
        "Mistral AI (setembro de 2025), Serie C: 1,7 bilhao de euros arrecadados, avaliacao de 11,7 bilhoes de euros. ASML principal investidora (1,3 bilhao de euros por aprox. 11%). Outros investidores: DST Global, a16z, Bpifrance, General Catalyst, Index Ventures, Lightspeed, Nvidia.",
        "Introl Blog (dezembro de 2025), 'O Impulso da Soberania de IA da França'. Mistral Compute: 18.000 GPUs Grace Blackwell, data center de 40 MW em Essonne (hospedado pela Scaleway/Eclairion), alimentado por energia nuclear. Lancamento planejado para 2026.",
        "Mistral AI / Wikipedia FR (fevereiro de 2026). Data center de Borlänge (Suecia): 1,2 bilhao de euros, planejado para 2027, via EcoDataCenter (energia renovavel). Aquisicao da Koyeb (17 de fevereiro de 2026) para fortalecer a oferta serverless da Mistral Compute.",
        "Dealroom (2025), citado no FinTech Weekly. Financiamento de IA na Europa +55% no 1º trimestre de 2025, 12 novos unicornios no 1º semestre de 2025. A Franca tem sido o destino numero 1 da UE para investimentos estrangeiros em IA desde 2020.",
        "Ministerio das Forcas Armadas (fevereiro de 2025), lancamento do GenIAl.intradef. Agente conversacional seguro baseado na Mistral AI, implantado em infraestrutura soberana.",
        "Martens, B. (2024), Working Paper 18/2024, Bruegel, op. cit. O custo de pessoal de IA (salarios + equity) e frequentemente o componente mais importante do desenvolvimento de modelos, e as empresas americanas oferecem pacotes estruturalmente superiores.",
        "Martens, B. (2025), 'The European Union Needs More Than the Digital Omnibus to Make Digital Services Competitive', Bruegel. O AI Omnibus, destinado a acelerar as mudancas regulatorias, provavelmente levara pelo menos um ano para ser adotado, mais um ano para as diretrizes complementares.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Capitulo VI",
    filename="Capitulo_VI_Consequencias_Franca_Europa_PT-BR.docx"
)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

LANGS = [EN, FR, BR]

def build_all(out_dir: Path) -> None:
    for lp in LANGS:
        log.info("Building Chapter VI [%s] -> %s", lp.code, lp.filename)
        doc = init_document()
        # Figures
        fig_dir = out_dir / "figures_ch6"
        
        # Build document
        add_cover(doc, lang=lp.code, chapter_label=lp.label, chapter_subtitle=lp.title)
        add_chapter_header(doc, label=lp.label, title=lp.title, intro=lp.intro)
        
        for i, (title, paragraphs) in enumerate(lp.sections):
            render_section(doc, title, paragraphs)
            
            # Insert images after specific sections
            if title.startswith("6.1"):
                img_path = fig_dir / f"Fig_6.1_Sectoral_Exposure_France_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
            elif title.startswith("6.2"):
                img_path = fig_dir / f"Fig_6.2_Three_Configurations_France_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.5)
        for caption, source, rows in lp.tables:
            render_table(doc, lang=lp.code, caption=caption, source=source, rows=rows)
        render_notes(doc, lang=lp.code, notes=lp.notes)
        render_license(doc, lang=lp.code, page_footer=lp.footer)
        
        out = out_dir / lp.filename
        doc.save(out)
        log.info("Saved %s", out)

if __name__ == "__main__":
    build_all(Path(__file__).parent)
