"""
Chapter VI bis - Consequences for South America and Brazil - trilingual generator.

Generates the .docx for Chapter VI bis in English, French, and Brazilian Portuguese.
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
log = logging.getLogger("chapter6bis_trilingual")

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
    label="CHAPTER VI BIS",
    title="Consequences for South America and Brazil",
    intro=(
        "The analysis of previous chapters has focused on the US-Europe transatlantic axis. "
        "However, the consequences of American AI protectionism extend far beyond the OECD. "
        "South America, and Brazil in particular, constitute a revealing case study: "
        "simultaneously a dynamic market for AI, a terrain of US-China geopolitical competition, "
        "and a region structurally dependent on foreign compute while possessing unique energy assets. "
        "This complementary chapter analyzes the specific consequences of the protectionist regime "
        "on South America, with an in-depth focus on Brazil."
    ),
    sections=[
        ("6bis.1 Structural position: the Global South facing compute asymmetry", []),
        ("6bis.1.1 A rapidly growing but structurally dependent ecosystem", [
            "Latin America represents 6.6 percent of global GDP, but only attracts 1.12 percent of global AI investment—a ratio of 5.9 that measures the region's investment deficit.[1] Yet, adoption indicators are remarkably dynamic. The Latin American Artificial Intelligence Index (ILIA 2025), published by ECLAC and the Chilean CENIA, ranks three countries as pioneers (Chile, Brazil, Uruguay), eight as adopters (including Colombia, Ecuador, Costa Rica), and one-third as explorers with nascent ecosystems.[2] The region represents 14 percent of global visits to AI solutions and ranks third globally for generative AI application downloads.",
            "This adoption dynamic contrasts with a considerable infrastructural deficit. High-income countries host 77 percent of global colocation data center capacity (June 2025), compared to 18 percent for upper-middle-income countries and 5 percent for lower-middle-income countries.[3] High-income countries also concentrate 87 percent of notable AI models, 86 percent of AI startups, and 91 percent of AI venture capital, while representing only 17 percent of the global population. Latin America falls into the intermediate category: a dynamic consumer of AI, but almost entirely dependent on foreign infrastructure (American and, increasingly, Chinese) for compute.",
        ]),
        ("6bis.1.2 Tier 2 classification: compute access caps from the US", [
            "Under the January 2025 AI Diffusion Rule (Biden administration), all of Latin America—including Brazil, Mexico, and Chile—is classified as Tier 2, meaning it is subject to quantitative caps on advanced GPU imports. Tier 1 (unlimited access) is reserved for 20 close allies (Australia, Canada, France, Germany, Japan, etc.). Tier 3 (prohibited access) targets China, Russia, and about twenty other countries.[4]",
            "For South America, this Tier 2 classification means that large-scale AI data center projects are capped in terms of importable GPU volume. Initial caps under the AI Diffusion Rule were approximately 50,000 GPUs between 2025 and 2027 for all Tier 2 countries (individually), a volume clearly insufficient to power the announced megaprojects. Brookings observes that even for the most favored Tier 2 countries (Brazil, India), American caps mean that their compute needs will likely not be consistently met.[5] Although the Trump administration rescinded the AI Diffusion Rule in May 2025 without yet publishing a replacement rule, regulatory uncertainty creates a supply risk that weighs on investment decisions. The BIS published America's AI Action Plan in July 2025, which promotes the export of full-stack AI export packages to allies while hardening enforcement toward adversaries.[6]",
        ]),
        ("6bis.2 Brazil: emerging hub between two blocs", []),
        ("6bis.2.1 Brazil's structural assets for AI", [
            "Brazil possesses objective competitive advantages for AI infrastructure. Its electricity mix is 83 percent renewable (essentially hydroelectric, supplemented by rapidly growing wind and solar), with a competitive electricity cost of approximately 0.08 USD/kWh. The national interconnected grid (SIN) has surplus capacity, and the country possesses a base of telecommunications submarine cables (notably the Fortaleza hub) offering one of the shortest routes to Europe and Africa.[7]",
            "The Brazilian data center market is the largest in Latin America, representing more than 41 percent of regional investments. Installed IT capacity reached approximately 1 GW by the end of 2025, with 202 active projects and 23 scheduled completions by the end of 2026. The AI data center market specifically is valued at 0.55 billion USD in 2025, projected to reach 1.24 billion by 2030 (annual growth of 17.5 percent).[8] The Brazilian Data Center Association (ABDC) projects that data center energy demand could reach 13.7 GW by 2035.",
            "The Lula government has taken concrete steps to accelerate development. In September 2025, the Redata provisional measure was adopted, creating a special tax regime that reduces the cost of capital for data centers by 50 percent through exemption from taxes on IT assets, with benefits valid until December 2026. The Brazilian Artificial Intelligence Plan (PBIA) aims to transform the country into a global data center hub, and BNDES (National Development Bank) has launched a dedicated AI and data center fund with initial capital of 500 million to 1 billion reais (93-187 million USD).[9]",
        ]),
        ("6bis.2.2 Megaprojects and US-China duality", [
            "Brazil has become the theater of direct competition between American and Chinese investments in AI infrastructure, a duality that reveals the dynamics created by US protectionism.",
            "On the Chinese side, the most spectacular project is the TikTok-ByteDance data center in Pecém (Ceará), announced in December 2025: 200 billion reais (approximately 38 billion USD), in partnership with developer Omnia (Pátria Investments) and renewable energy producer Casa dos Ventos.[10] The project, construction of which is to begin in April 2026, will be powered entirely by wind energy (300 MW initially, expandable to 900 MW or even 1 GW). It constitutes the largest private data center investment ever announced in Brazil and ByteDance's first project in Latin America. The investment comes in a context where TikTok faces threats of blocking in the United States and where China seeks to diversify its compute infrastructure outside its direct geopolitical risk zone.",
            "On the American side, Microsoft has announced a 2.7 billion USD investment over three years in cloud and AI infrastructure in Brazil, as part of its 50 billion USD global commitment to the Global South by 2030.[11] AWS and Google already have cloud regions in Brazil (São Paulo). US hyperscalers control approximately 55 percent of the Brazilian cloud market (AWS, Azure, GCP), a smaller dominance than in Europe (70 percent) but enough to structure dependence.",
            "Other megaprojects illustrate the scale of ambitions. Scala Data Centers announced Eldorado do Sul's AI City (Rio Grande do Sul), with 1,800 MW of capacity and a potential for 5,000 MW by 2033. Elea Data Centers is developing Rio AI City, presented as the largest data center campus in Latin America, with 1.8 GW of capacity by 2027 and 3.2 GW by 2032, with Oracle and Nvidia as technology partners.[12]",
        ]),
        ("6bis.3 Impact of US protectionism on South America", []),
        ("6bis.3.1 The double bind of Tier 2 classification", [
            "The Tier 2 position of Brazil and South America creates a strategic double bind. On one hand, GPU import caps limit countries' ability to build sovereign AI infrastructure and realize announced megaprojects. On the other, American restrictions toward China (Tier 3) push ByteDance and other Chinese actors to invest heavily in Latin America as an alternative infrastructure deployment zone. Brazil thus becomes a substitution terrain in the US-China rivalry.",
            "Brookings warns that this situation could push Tier 2 countries to develop supply chains independent of the United States, including stronger technological ties with China.[13] Brazil, whose primary trading partner is China, perfectly illustrates this dynamic. The TikTok-Pecém investment, the largest Chinese technological investment in Latin America, is part of a deepening of China-Brazil ties that predated Trump's reelection but accelerated in the face of American trade policies.",
        ]),
        ("6bis.3.2 Five channels of impact", [
            "The impact of American AI protectionism on South America is transmitted through five distinct channels, some of which are specific to the region.",
            "Channel 1 - Direct constraint on AI hardware. Tier 2 caps on cutting-edge GPUs limit construction capacity. Even if the AI Diffusion Rule is rescinded, regulatory uncertainty weighs: projects requiring 10,000 to 100,000 GPUs (like Scala AI City or Elea Rio AI City) depend entirely on American willingness to deliver Nvidia or AMD accelerators. The GAIN AI Act, currently under discussion in the US Congress, proposes to give priority access to advanced semiconductors to American consumers before satisfying international orders—which would further degrade the region's supply.[14]",
            "Channel 2 - Reinforced US cloud dependence. In the absence of sufficient local infrastructure, Brazilian companies resort heavily to the US cloud. The Brazilian financial sector (Itaú, Nubank, Bradesco) is the most digitized in Latin America, with 95 percent of transactions processed digitally at Itaú Unibanco. Brazilian Open Banking connects 800 institutions. This digitization relies largely on US hyperscalers, creating the same dependence pattern as for Europe (Chapter IV), but with less bargaining power.",
            "Channel 3 - US-China technological bifurcation. Brazil is faced with a specific risk: the fragmentation of its AI infrastructure between American and Chinese ecosystems. The Pecém data centers (ByteDance), although powered by Brazilian renewable energy, will likely use Huawei hardware or non-US alternatives if American restrictions prevent the export of Nvidia GPUs to Chinese projects. This hardware duality creates issues of interoperability, data sovereignty (US CLOUD Act versus Chinese data security law), and standardization. Brazil risks becoming a space where two incompatible technological ecosystems coexist, fragmented and each dependent on an external power.",
            "Channel 4 - Amplified brain drain. ILIA 2025 signals a widening of the AI talent gap in Latin America since 2022, associated with an acceleration of the brain drain of specialists.[15] Brazil trains excellent engineers (USP, Unicamp, ITA), but the compensation differential with the United States is even more marked than for Europe. Compute asymmetry aggravates this drain: AI researchers who stay in Brazil do not have access to the compute necessary for frontier research, which reinforces the attractiveness of American laboratories.",
            "Channel 5 - Widened productivity gap. The World Bank and the ILO observe that Latin America suffers from a persistent productivity deficit, largely linked to barriers to innovation and technological adoption.[16] If high-income countries capture AI productivity gains (IMF: TFP gains significantly higher in advanced economies), AI protectionism risks transforming what was an adoption delay (temporary buffer) into a structural barrier (bottleneck). Constrained access to cutting-edge compute prevents Latin American companies from realizing the theoretical productivity gains of AI, widening the gap with the United States.",
        ]),
        ("6bis.4 Specific scenarios for Brazil", [
            "By applying the 2x2 scenario matrix from Chapter V, the scenarios for Brazil differ from Europe because Brazil has an additional variable: the possibility of playing the Chinese card as an alternative to the US ecosystem. Table 17 details the four possible trajectories.",
            "Scenario A' (Dual Neutral Hub) is the most likely in the short term. Brazil maintains close trade relations with both blocs and has no interest in aligning exclusively. However, this scenario is inherently unstable: the United States could impose conditions (restrictions on the use of Nvidia GPUs in data centers also hosting Chinese workloads), forcing Brazil to choose. Trump's designation of drug cartels as foreign terrorist organizations has already increased the exposure of companies operating in Brazil and Mexico to US export control rules.[17]",
            "Scenario B' (Secondary Sanctions) represents the maximum risk. If the United States decided to apply secondary sanctions against countries hosting significant Chinese AI infrastructure, Brazil would face an existential dilemma: lose access to the American technological ecosystem (Nvidia, AWS, Azure) or renounce massive Chinese investments. This scenario, although unlikely in the short term, is not hypothetical: the United States has already applied secondary sanctions on Russian and Venezuelan oil, and the Affiliates Rule (suspended until November 2026) extends restrictions to subsidiaries of listed entities.[18]",
        ]),
        ("6bis.5 South America beyond Brazil", [
            "The other economies of South America undergo the same dynamics as Brazil, but with less bargaining weight and fewer structural assets.",
            "Chile, classified as a pioneer by ILIA 2025, benefits from favorable temperatures (reducing cooling energy consumption) and an advanced AI governance ecosystem. Microsoft launched Chile Central in June 2025, its first cloud region in the country, associated with the Transforma Chile program (180,000 people trained, 81,000 jobs created). But Chile remains entirely dependent on American hardware and cloud, without the Chinese alternative that Brazil has.",
            "Mexico, the United States' immediate neighbor, presents a different profile. Nearshoring (relocating production from Asia) has transformed the economic landscape, and data centers benefit from proximity to the US market. However, Mexico is more vulnerable to American protectionism due to USMCA (renewable in July 2026) and the designation of cartels as terrorist organizations. Its energy infrastructure for data centers is also less competitive than Brazil's.",
            "Colombia, Argentina, and Peru, classified as adopters, face even stronger constraints: fragile electrical infrastructure, limited AI human capital, and near-zero bargaining power with GPU providers. For these countries, American AI protectionism translates primarily into delayed and more expensive access to AI tools, widening the productivity gap not only with the United States but also with Brazil and Chile within the region itself.",
        ]),
        ("6bis.6 Synthesis: a risk of triple fracture", [
            "The analysis in this chapter reveals that American AI protectionism produces a risk of triple fracture in South America, specific to the region and distinct from the European scenario.",
            "North-South Fracture. The compute gap between the United States and South America is much more pronounced than the US-Europe gap. While the raw US/EU(13) ratio is 17.6:1 on installed operational compute and the CACI(US)/CACI(EU) ratio is 3.46:1 (Chapter III, April 2026 baseline), an equivalent CACI(US)/CACI(Brazil) ratio would be in the range of 30-50:1 in CACI Power Mode and well over 100:1 in raw compute, reflecting the combination of a deficit in installed computing capacity, more limited AI human capital, and a higher cost of capital (Brazilian Selic at 14.25 percent at the end of 2025). This gap is such that catching up is almost impossible by 2030 without massive external help.",
            "East-West Fracture. The US-China rivalry for AI infrastructure in South America creates a risk of technological fragmentation unparalleled in Europe. Brazil could find itself with two incompatible parallel ecosystems (US cloud versus Chinese infrastructure), each responding to its own geopolitical logic rather than the needs of the local economy. Europe, as a Tier 1 ally, does not face this direct bifurcation on compute, even if the Cloud-Nationality pivot analyzed in Chapter V creates a distinct vulnerability on cloud workloads.",
            "Intra-regional Fracture. Within South America, Brazil attracts most AI investments (41 percent of the LATAM market), followed by Chile and Mexico. 'Explorer' countries (one-third of the region according to ILIA 2025) risk being entirely excluded from the AI economy, reproducing a dependence pattern analogous to that of raw materials. The WEF suggests a regional multi-stakeholder consortium (GAVI model) to pool compute resources and democratize AI access.[19]",
            "For Brazil specifically, the main strategic challenge is to transform its energy assets (83 percent renewable mix) into compute sovereignty, avoiding the US-China competition from fragmenting its ecosystem. The comparison with France is enlightening: both countries possess a distinctive energy asset (nuclear for France, renewable for Brazil), an emerging national technological champion (Mistral for France, fintech/Nubank ecosystem for Brazil), and a regional AI hub ambition. But Brazil faces additional constraints (Tier 2 classification, cost of capital, amplified brain drain) that make its trajectory more uncertain and its vulnerability to protectionism more acute.",
        ]),
    ],
    tables=[
        ("Table 16. Major AI data center projects in Brazil (2025-2030).",
         "Source: Author's compilation from Bloomberg, IndustrialInfo, Introl.",
         [
             ["Project", "Origin", "Investment", "Capacity", "Feature"],
             ["TikTok Pecém", "China", "~38B USD", "300 MW to 1 GW", "100% wind; ByteDance's 1st LATAM project"],
             ["Scala AI City", "Brazil/US", "Multi-B USD", "1.8 to 5 GW", "Largest planned installation in South America"],
             ["Elea Rio AI City", "Brazil/US", "Multi-B USD", "1.8 to 3.2 GW", "Oracle + Nvidia technology partners"],
             ["Microsoft Azure", "US", "2.7B USD (3 yrs)", "N/A", "Cloud + AI + ConectaAI program"],
             ["AWS São Paulo", "US", "N/A", "Multiple AZ", "Active cloud region since 2011"],
         ]),
        ("Table 17. Brazil-specific scenarios facing US AI protectionism 2026-2030.",
         "Source: Author's construction, calibration on April 2026 baseline (raw US/EU(13) 17.6:1, CACI Power Mode 3.46:1).",
         [
             ["Brazil Scenario", "Probability", "Positive Consequences", "Risks"],
             ["A': Dual US-China Neutral Hub", "35-45%",
              "Inflow of investments from both blocs; renewable energy as an asset; supplier diversification",
              "Ecosystem fragmentation; US pressure to limit Chinese access; data vulnerability"],
             ["B': Secondary Sanctions", "15-20%",
              "Acceleration of substitutive Chinese investment",
              "Loss of US ecosystem access (Nvidia, cloud); partial technological isolation"],
             ["C': Pro-US Alignment", "20-25%",
              "Negotiated Tier 1 access; unlimited GPUs; increased Microsoft/AWS investment",
              "Total US dependence; loss of Chinese investment (Pecém threatened)"],
             ["D': Regional LATAM Sovereignty", "10-15%",
              "Regional compute consortium; dependence reduction; energy pooling",
              "Limited execution capacity; insufficient capital; 5-10 year delay"],
         ]),
    ],
    notes=[
        "ECLAC/CENIA (October 2025), Latin American Artificial Intelligence Index (ILIA 2025). Latin America represents 6.6% of global GDP and 1.12% of global AI investment.",
        "ECLAC/CENIA (2025), ibid. Three categories: pioneers (Chile, Brazil, Uruguay, over 60 pts), adopters (Colombia, Ecuador, Costa Rica, Dominican Republic), explorers (nascent ecosystems).",
        "World Bank (November 2025), Digital Progress and Trends Report 2025: Strengthening AI Foundations. High-income countries: 77% colocation DC capacity, 87% notable AI models, 86% AI startups, 91% AI VC.",
        "BIS (January 2025), Framework for Artificial Intelligence Diffusion. Tier 1: 20 ally countries (unlimited access). Tier 2: ~140 countries including the whole American continent outside US/Canada (quantitative caps). Tier 3: ~20 countries (prohibited access). Rule rescinded in May 2025 by Trump administration, replacement pending.",
        "Brookings (2025), 'Trump's AI export controls and the AI Diffusion Rule'. Initial caps: ~50,000 GPUs per Tier 2 country over 2025-2027.",
        "BIS (July 2025), America's AI Action Plan. Promoting full-stack AI export packages to allies, hardening toward adversaries.",
        "ABDC (2025), Brazilian Data Center Association. Brazilian electricity mix: 83% renewable. Fortaleza hub: submarine cable connections to Europe and Africa.",
        "ABDC (2025); Mordor Intelligence (2026). Brazil AI DC market: 0.55B USD (2025) to 1.24B USD (2030), CAGR 17.5%.",
        "BNDES (2025); Redata provisional measure (September 2025): 50% reduction in DC capital cost via IT tax exemption, valid until Dec 2026.",
        "Bloomberg (December 2025), 'ByteDance Plans 200 Billion-Real Brazilian Data Center'. Partnership Omnia (Pátria Investments) + Casa dos Ventos. 300 MW initial, expandable to 1 GW.",
        "Microsoft (2025), 50B USD commitment for Global South by 2030. 2.7B USD specifically for Brazil over 3 years.",
        "Scala Data Centers (2025); Elea Data Centers (2025). Rio AI City: Oracle + Nvidia partnership.",
        "Brookings (January 2025), op. cit. Tier 2 countries risk developing supply chains independent of US, including reinforced technological ties with China.",
        "GAIN AI Act (2025), discussion in US Congress. Priority access to advanced semiconductors for US consumers before international orders.",
        "ILIA 2025 (ECLAC/CENIA), AI talent section. Acceleration of specialist brain drain since 2022.",
        "World Bank and ILO (2024-2025): persistent productivity deficit in Latin America. IMF (March 2025): AI TFP gains significantly higher in advanced economies.",
        "Designation of drug cartels as foreign terrorist organizations (Trump, 2025). Increased exposure of companies operating in Brazil and Mexico to US export control rules.",
        "BIS, Suspension of the Affiliates Rule for One Year (November 10, 2025). Affiliates Rule extends restrictions to subsidiaries of listed entities.",
        "WEF (2025), regional multi-stakeholder consortium proposal (GAVI model) to pool compute resources in Latin America.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapter VI bis",
    filename="Chapter_VI_bis_Americas_Brazil_EN.docx"
)

# ---------------------------------------------------------------------------
# Content - FRENCH (Reference)
# ---------------------------------------------------------------------------

FR = LangPack(
    code="FR",
    label="CHAPITRE VI BIS",
    title="Consequences pour l'Amerique du Sud et le Bresil",
    intro=(
        "L'analyse des chapitres precedents s'est concentree sur l'axe transatlantique US-Europe. "
        "Or, les consequences du protectionnisme IA americain s'etendent bien au-dela de l'OCDE. "
        "L'Amerique du Sud, et le Bresil en particulier, constituent un cas d'etude revelateur : "
        "a la fois marche dynamique pour l'IA, terrain de competition geopolitique US-Chine, et "
        "region structurellement dependante du compute etranger tout en disposant d'atouts "
        "energetiques uniques. Ce chapitre complementaire analyse les consequences specifiques "
        "du regime protectionniste sur l'Amerique du Sud, avec un focus approfondi sur le Bresil."
    ),
    sections=[
        ("6bis.1 Position structurelle : le Sud global face a l'asymetrie de compute", []),
        ("6bis.1.1 Un ecosysteme en croissance rapide mais structurellement dependant", [
            "L'Amerique latine represente 6,6 pour cent du PIB mondial, mais n'attire que 1,12 pour cent de l'investissement mondial en IA - un ratio de 5,9 qui mesure le deficit d'investissement de la region.[1] Pourtant, les indicateurs d'adoption sont remarquablement dynamiques. L'indice latino-americain de l'intelligence artificielle (ILIA 2025), publie par la CEPALC et le CENIA chilien, classe trois pays comme pionniers (Chile, Bresil, Uruguay), huit comme adoptants (dont Colombie, Equateur, Costa Rica), et un tiers comme explorateurs avec des ecosystemes naissants.[2] La region represente 14 pour cent des visites mondiales de solutions IA et se classe troisieme mondiale pour les telechargements d'applications d'IA generative.",
            "Ce dynamique d'adoption contraste avec un deficit infrastructurel considerable. Les pays a revenu eleve hebergent 77 pour cent de la capacite mondiale de data centers en colocation (juin 2025), contre 18 pour cent pour les pays a revenu intermediaire superieur et 5 pour cent pour les pays a revenu intermediaire inferieur.[3] Les pays a haut revenu concentrent egalement 87 pour cent des modeles IA notables, 86 pour cent des startups IA et 91 pour cent du capital-risque IA, alors qu'ils ne representent que 17 pour cent de la population mondiale. L'Amerique latine se situe dans la categorie intermediaire : consommatrice dynamique d'IA, mais quasi-entierement dependante de l'infrastructure etrangere (americaine et, de plus en plus, chinoise) pour le compute.",
        ]),
        ("6bis.1.2 Classification Tier 2 : les caps d'acces au compute US", [
            "Dans le cadre de l'AI Diffusion Rule de janvier 2025 (administration Biden), l'ensemble de l'Amerique latine - y compris le Bresil, le Mexique et le Chili - est classe Tier 2, c'est-a-dire soumis a des caps quantitatifs sur les importations de GPU avancees. Le Tier 1 (acces illimite) est reserve a 20 allies proches (Australie, Canada, France, Allemagne, Japon, etc.). Le Tier 3 (acces interdit) vise la Chine, la Russie et une vingtaine de pays.[4]",
            "Pour l'Amerique du Sud, cette classification Tier 2 signifie que les projets de data centers IA de grande envergure sont plafonnes en volume de GPU importables. Les caps initiaux de l'AI Diffusion Rule etaient d'environ 50 000 GPU entre 2025 et 2027 pour l'ensemble des pays Tier 2 (individuellement), un volume nettement insuffisant pour alimenter les megaprojets annonces. Brookings observe que meme pour les pays Tier 2 les plus favorises (Bresil, Inde), les caps americains signifient que leurs besoins en compute ne seront vraisemblablement pas satisfaits de maniere constante.[5] Bien que l'administration Trump ait rescinde l'AI Diffusion Rule en mai 2025 sans encore publier de regle de remplacement, l'incertitude reglementaire cree un risque d'approvisionnement qui pese sur les decisions d'investissement. Le BIS a publie en juillet 2025 l'America's AI Action Plan qui promeut l'export de full-stack AI export packages vers les allies, tout en durcissant l'application vers les adversaires.[6]",
        ]),
        ("6bis.2 Le Bresil : hub emergent entre deux blocs", []),
        ("6bis.2.1 Atouts structurels du Bresil pour l'IA", [
            "Le Bresil possede des avantages competitifs objectifs pour l'infrastructure IA. Son mix electrique est renouvelable a 83 pour cent (essentiellement hydroelectrique, complete par l'eolien et le solaire en forte croissance), avec un cout de l'electricite competitif a environ 0,08 USD/kWh. Le reseau electrique national interconnecte (SIN) dispose de capacites excedentaires, et le pays possede une base de cables sous-marins de telecommunications (notamment le hub de Fortaleza) offrant l'une des routes les plus courtes vers l'Europe et l'Afrique.[7]",
            "Le marche bresilien des data centers est le plus important d'Amerique latine, representant plus de 41 pour cent des investissements regionaux. La capacite IT installee a atteint environ 1 GW fin 2025, avec 202 projets actifs et 23 acheves prevus d'ici fin 2026. Le marche des data centers IA specifiquement est evalue a 0,55 milliard USD en 2025, projete a 1,24 milliard d'ici 2030 (croissance annuelle de 17,5 pour cent).[8] L'Association bresilienne des data centers (ABDC) projette que la demande d'energie des data centers pourrait atteindre 13,7 GW d'ici 2035.",
            "Le gouvernement Lula a pris des mesures concretes pour accelerer le developpement. En septembre 2025, la mesure provisoire Redata a ete adoptee, creant un regime fiscal special qui reduit de 50 pour cent le cout du capital pour les data centers via l'exoneration des impots sur les actifs IT, avec des avantages valides jusqu'a decembre 2026. Le Plan bresilien d'intelligence artificielle (PBIA) vise a transformer le pays en hub mondial de data centers, et la BNDES (Banque nationale de developpement) a lance un fonds dedie IA et data centers avec un capital initial de 500 millions a 1 milliard de reaux (93-187 millions USD).[9]",
        ]),
        ("6bis.2.2 Megaprojets et dualite US-Chine", [
            "Le Bresil est devenu le theatre d'une competition directe entre investissements americains et chinois en infrastructure IA, une dualite qui revele les dynamiques creees par le protectionnisme US.",
            "Cote chinois, le projet le plus spectaculaire est le data center TikTok-ByteDance de Pecem (Ceara), annonce en decembre 2025 : 200 milliards de reaux (environ 38 milliards USD), en partenariat avec le developpeur Omnia (Patria Investments) et le producteur d'energie renouvelable Casa dos Ventos.[10] Le projet, dont la construction doit debuter en avril 2026, sera alimente entierement par de l'energie eolienne (300 MW initiaux, extensibles a 900 MW voire 1 GW). Il constitue le plus gros investissement prive en data center jamais annonce au Bresil et le premier projet de ByteDance en Amerique latine. L'investissement s'inscrit dans un contexte ou TikTok fait face a des menaces de blocage aux Etats-Unis et ou la Chine cherche a diversifier ses infrastructures de compute hors de sa zone de risque geopolitique directe.",
            "Cote americain, Microsoft a annonce un investissement de 2,7 milliards USD sur trois ans en infrastructure cloud et IA au Bresil, dans le cadre de son engagement global de 50 milliards USD pour le Sud global d'ici 2030.[11] AWS et Google disposent deja de regions cloud au Bresil (Sao Paulo). Les hyperscalers US controlent environ 55 pour cent du marche bresilien du cloud (AWS, Azure, GCP), une domination moindre qu'en Europe (70 pour cent) mais suffisante pour structurer la dependance.",
            "D'autres megaprojets illustrent l'ampleur des ambitions. Scala Data Centers a annonce l'AI City d'Eldorado do Sul (Rio Grande do Sul), avec 1 800 MW de capacite et un potentiel de 5 000 MW d'ici 2033. Elea Data Centers developpe la Rio AI City, presentee comme le plus grand campus de data centers d'Amerique latine, avec 1,8 GW de capacite d'ici 2027 et 3,2 GW d'ici 2032, avec Oracle et Nvidia comme partenaires technologiques.[12]",
        ]),
        ("6bis.3 Impact du protectionnisme US sur l'Amerique du Sud", []),
        ("6bis.3.1 Le double bind de la classification Tier 2", [
            "La position Tier 2 du Bresil et de l'Amerique du Sud cree un double bind strategique. D'un cote, les caps d'importation de GPU limitent la capacite des pays a construire une infrastructure IA souveraine et a realiser les megaprojets annonces. De l'autre, les restrictions americaines vers la Chine (Tier 3) poussent ByteDance et d'autres acteurs chinois a investir massivement en Amerique latine comme zone alternative de deploiement d'infrastructure. Le Bresil devient ainsi un terrain de substitution dans la rivalite sino-americaine.",
            "Brookings avertit que cette situation pourrait pousser les pays Tier 2 a developper des chaines d'approvisionnement independantes des Etats-Unis, y compris des liens technologiques plus forts avec la Chine.[13] Le Bresil, dont la Chine est le premier partenaire commercial, illustre parfaitement cette dynamique. L'investissement TikTok-Pecem, le plus gros investissement technologique chinois en Amerique latine, s'inscrit dans un approfondissement des liens Chine-Bresil qui preexistait a la reelection de Trump mais qui s'est accelere face aux politiques commerciales americaines.",
        ]),
        ("6bis.3.2 Cinq canaux d'impact", [
            "L'impact du protectionnisme IA americain sur l'Amerique du Sud se transmet par cinq canaux distincts, dont certains sont propres a la region.",
            "Canal 1 - Contrainte directe sur le hardware IA. Les caps Tier 2 sur les GPU de pointe limitent la capacite de construction. Meme si l'AI Diffusion Rule est rescindee, l'incertitude reglementaire pese : les projets necessitant 10 000 a 100 000 GPU (comme Scala AI City ou Elea Rio AI City) dependent entierement de la volonte americaine de livrer des accelerateurs Nvidia ou AMD. Le GAIN AI Act, actuellement en discussion au Congres americain, propose de donner la priorite d'acces aux semi-conducteurs avances aux consommateurs americains avant de satisfaire les commandes internationales - ce qui degraderait encore l'approvisionnement de la region.[14]",
            "Canal 2 - Dependance au cloud US renforcee. En l'absence d'infrastructure locale suffisante, les entreprises bresiliennes recourent massivement au cloud US. Le secteur financier bresilien (Itau, Nubank, Bradesco) est le plus numerise d'Amerique latine, avec 95 pour cent des transactions traitees numeriquement chez Itau Unibanco. L'Open Banking bresilien connecte 800 institutions. Cette numerisation repose en grande partie sur les hyperscalers US, creant le meme schema de dependance que pour l'Europe (chapitre IV), mais avec moins de capacite de negociation.",
            "Canal 3 - Bifurcation technologique US-Chine. Le Bresil est confronte a un risque specifique : la fragmentation de son infrastructure IA entre ecosystemes americain et chinois. Les data centers de Pecem (ByteDance), bien qu'alimentes par de l'energie renouvelable bresilienne, utiliseront vraisemblablement du hardware Huawei ou des alternatives non-US si les restrictions americaines empechent l'export de GPU Nvidia vers des projets chinois. Cette dualite hardware cree des problemes d'interoperabilite, de souverainete des donnees (CLOUD Act americain versus loi chinoise sur la securite des donnees), et de standardisation. Le Bresil risque de devenir un espace ou deux ecosystemes technologiques incompatibles coexistent, fragmentes et chacun dependant d'une puissance exterieure.",
            "Canal 4 - Brain drain amplifie. L'ILIA 2025 signale un elargissement du fosse de talent IA en Amerique latine depuis 2022, associe a une acceleration du brain drain de specialistes.[15] Le Bresil forme d'excellents ingenieurs (USP, Unicamp, ITA), mais le differentiel de remuneration avec les Etats-Unis est encore plus marque que pour l'Europe. L'asymetrie de compute aggrave ce drain : les chercheurs IA qui restent au Bresil n'ont pas acces au compute necessaire pour la recherche frontier, ce qui renforce l'attractivite des laboratoires americains.",
            "Canal 5 - Fosse de productivite elargi. La Banque mondiale et l'OIT observent que l'Amerique latine souffre d'un deficit de productivite persistant, en grande partie lie aux barrieres a l'innovation et a l'adoption technologique.[16] Si les pays a revenu eleve captent les gains de productivite IA (FMI : gains TFP significativement plus eleves dans les economies avancees), le protectionnisme IA risque de transformer ce qui etait un retard d'adoption (buffer temporaire) en barriere structurelle (bottleneck). L'acces contraint au compute de pointe empeche les entreprises latino-americaines de realiser les gains de productivite theoriques de l'IA, creusant l'ecart avec les Etats-Unis.",
        ]),
        ("6bis.4 Scenarios specifiques pour le Bresil", [
            "En reprenant la matrice 2x2 du chapitre V, les scenarios pour le Bresil se declinent differemment de l'Europe, car le Bresil dispose d'une variable supplementaire : la possibilite de jouer la carte chinoise comme alternative a l'ecosysteme US. Le Tableau 17 detaille les quatre trajectoires possibles.",
            "Le scenario A' (Hub neutre dual) est le plus probable a court terme. Le Bresil entretient des relations commerciales etroites avec les deux blocs et n'a aucun interet a s'aligner exclusivement. Cependant, ce scenario est intrinsequement instable : les Etats-Unis pourraient imposer des conditions (restrictions sur l'usage de GPU Nvidia dans des data centers accueillant egalement des workloads chinois), forcant le Bresil a choisir. La designation par Trump des cartels de drogue comme organisations terroristes etrangeres a deja accru l'exposition des entreprises operant au Bresil et au Mexique aux regles de controle des exportations US.[17]",
            "Le scenario B' (Sanctions secondaires) represente le risque maximal. Si les Etats-Unis decidaient d'appliquer des sanctions secondaires contre les pays hebergeant des infrastructures IA chinoises significatives, le Bresil se trouverait face a un dilemme existentiel : perdre l'acces a l'ecosysteme technologique americain (Nvidia, AWS, Azure), ou renoncer aux investissements chinois massifs. Ce scenario, bien que peu probable a court terme, n'est pas hypothetique : les Etats-Unis ont deja applique des sanctions secondaires sur le petrole russe et venezuelien, et l'Affiliates Rule (suspendue jusqu'en novembre 2026) etend les restrictions aux filiales d'entites listees.[18]",
        ]),
        ("6bis.5 L'Amerique du Sud au-dela du Bresil", [
            "Les autres economies d'Amerique du Sud subissent les memes dynamiques que le Bresil, mais avec moins de poids de negociation et moins d'atouts structurels.",
            "Le Chili, classe pionnier par l'ILIA 2025, beneficie d'un environnement climatique favorable (reduction de la consommation energetique de refroidissement) et d'un ecosysteme de gouvernance IA avance. Microsoft a lance en juin 2025 Chile Central, sa premiere region cloud dans le pays, associee au programme Transforma Chile (180 000 personnes formees, 81 000 emplois crees). Mais le Chili reste entierement dependant du hardware et du cloud americain, sans l'alternative chinoise dont dispose le Bresil.",
            "Le Mexique, voisin immediat des Etats-Unis, presente un profil different. Le nearshoring (relocalisation de la production depuis l'Asie) a transforme le paysage economique, et les data centers beneficient de la proximite du marche US. Cependant, le Mexique est plus vulnerable au protectionnisme americain du fait de l'USMCA (renouvelable en juillet 2026) et de la designation des cartels comme organisations terroristes. Son infrastructure energetique pour data centers est aussi moins competitive que celle du Bresil.",
            "La Colombie, l'Argentine et le Perou, classes adoptants, font face a des contraintes encore plus fortes : infrastructure electrique fragile, capital humain IA limite, capacite de negociation quasi nulle avec les fournisseurs de GPU. Pour ces pays, le protectionnisme IA americain se traduit principalement par un acces retarde et rencheri aux outils IA, elargissant le fosse de productivite non seulement avec les Etats-Unis, mais aussi avec le Bresil et le Chili au sein meme de la region.",
        ]),
        ("6bis.6 Synthese : un risque de triple fracture", [
            "L'analyse de ce chapitre revele que le protectionnisme IA americain produit en Amerique du Sud un risque de triple fracture, specifique a la region et distinct du scenario europeen.",
            "Fracture Nord-Sud. L'ecart de compute entre les Etats-Unis et l'Amerique du Sud est bien plus prononce que l'ecart US-Europe. Si le ratio brut US/UE(13) est de 17,6:1 sur le compute installe operationnel et le ratio CACI(US)/CACI(UE) de 3,46:1 (chapitre III, baseline avril 2026), un ratio equivalent CACI(US)/CACI(Bresil) serait de l'ordre de 30-50:1 en CACI Power Mode et bien superieur a 100:1 en compute brut, refletant la combinaison d'un deficit de capacite de calcul installee, d'un capital humain IA plus limite, et d'un cout du capital plus eleve (Selic bresilien a 14,25 pour cent fin 2025). Ce fosse est tel que le rattrapage est quasi impossible a l'horizon 2030 sans aide exterieure massive.",
            "Fracture Est-Ouest. La rivalite US-Chine pour l'infrastructure IA en Amerique du Sud cree un risque de fragmentation technologique sans equivalent en Europe. Le Bresil pourrait se retrouver avec deux ecosystemes paralleles incompatibles (cloud US versus infrastructure chinoise), chacun repondant a une logique geopolitique propre plutot qu'aux besoins de l'economie locale. L'Europe, en tant qu'alliee Tier 1, ne fait pas face a cette bifurcation directe sur le compute, meme si le pivot Cloud-Nationalite analyse au chapitre V cree une vulnerabilite distincte sur les charges cloud.",
            "Fracture intra-regionale. Au sein de l'Amerique du Sud, le Bresil attire l'essentiel des investissements IA (41 pour cent du marche LATAM), suivi du Chili et du Mexique. Les pays explorateurs (un tiers de la region selon l'ILIA 2025) risquent d'etre entierement exclus de l'economie IA, reproduisant un schema de dependance analogue a celui des matieres premieres. Le WEF suggere un consortium multi-parties prenantes regional (modele GAVI) pour mutualiser les ressources de compute et democratiser l'acces a l'IA.[19]",
            "Pour le Bresil specifiquement, l'enjeu strategique principal est de transformer ses atouts energetiques (mix 83 pour cent renouvelable) en souverainete de compute, en evitant que la competition US-Chine ne fragmente son ecosysteme. La comparaison avec la France est eclairante : les deux pays possedent un atout energetique distinctif (nucleaire pour la France, renouvelable pour le Bresil), un champion technologique national en emergence (Mistral pour la France, ecosysteme fintech/Nubank pour le Bresil), et une ambition de hub regional IA. Mais le Bresil fait face a des contraintes supplementaires (classification Tier 2, cout du capital, brain drain amplifie) qui rendent sa trajectoire plus incertaine et sa vulnerabilite au protectionnisme plus aigue.",
        ]),
    ],
    tables=[
        ("Tableau 16. Principaux projets de data centers IA au Bresil (2025-2030).",
         "Source : compilation de l'auteur a partir de Bloomberg, IndustrialInfo, Introl.",
         [
             ["Projet", "Origine", "Investissement", "Capacite", "Caracteristique"],
             ["TikTok Pecem", "Chine", "~38 Md USD", "300 MW vers 1 GW", "100 pct eolien ; 1er projet LATAM ByteDance"],
             ["Scala AI City", "Bresil/US", "Multi-Md USD", "1,8 vers 5 GW", "Plus grande installation planifiee Am. du Sud"],
             ["Elea Rio AI City", "Bresil/US", "Multi-B USD", "1,8 vers 3,2 GW", "Oracle + Nvidia partenaires technologiques"],
             ["Microsoft Azure", "US", "2,7 Md USD (3 ans)", "N/D", "Cloud + IA + programme ConectaAI"],
             ["AWS Sao Paulo", "US", "N/D", "Multiple AZ", "Region cloud active depuis 2011"],
         ]),
        ("Tableau 17. Scenarios specifiques du Bresil face au protectionnisme IA americain 2026-2030.",
         "Source : construction de l'auteur, calibration sur baseline avril 2026 (US/UE(13) brut 17,6:1, CACI Power Mode 3,46:1).",
         [
             ["Scenario Bresil", "Probabilite", "Consequences positives", "Risques"],
             ["A' : Hub neutre dual US-Chine", "35-45 pct",
              "Afflux d'investissements des deux blocs ; energie renouvelable comme atout ; diversification fournisseurs",
              "Fragmentation ecosysteme ; pressions US pour limiter acces chinois ; vulnerabilite donnees"],
             ["B' : Sanctions secondaires", "15-20 pct",
              "Acceleration investissement chinois substitutif",
              "Perte acces ecosysteme US (Nvidia, cloud) ; isolement technologique partiel"],
             ["C' : Alignement pro-US", "20-25 pct",
              "Acces Tier 1 negocie ; GPU illimitees ; investissement Microsoft/AWS accru",
              "Dependance US totale ; perte investissement chinois (Pecem menace)"],
             ["D' : Souverainete regionale LATAM", "10-15 pct",
              "Consortium regional compute ; reduction dependance ; mutualisation energie",
              "Capacite d'execution limitee ; capital insuffisant ; retard 5-10 ans"],
         ]),
    ],
    notes=[
        "CEPALC/CENIA (octobre 2025), Latin American Artificial Intelligence Index (ILIA 2025). L'Amerique latine represente 6,6 pct du PIB mondial et 1,12 pct de l'investissement mondial en IA.",
        "CEPALC/CENIA (2025), ibid. Trois categories : pionniers (Chile, Bresil, Uruguay, plus de 60 pts), adoptants (Colombie, Equateur, Costa Rica, Republique Dominicaine), explorateurs (ecosystemes naissants).",
        "Banque mondiale (novembre 2025), Digital Progress and Trends Report 2025 : Strengthening AI Foundations. Pays a revenu eleve : 77 pct capacite DC en colocation, 87 pct modeles IA notables, 86 pct startups IA, 91 pct capital-risque IA.",
        "BIS (janvier 2025), Framework for Artificial Intelligence Diffusion. Tier 1 : 20 pays allies (acces illimite). Tier 2 : environ 140 pays dont tout le continent americain hors US/Canada (caps quantitatifs). Tier 3 : environ 20 pays (acces interdit). Regle rescindee en mai 2025 par l'administration Trump, remplacement en attente.",
        "Brookings (2025), 'Trump's AI export controls and the AI Diffusion Rule'. Caps initiaux : environ 50 000 GPU par pays Tier 2 sur 2025-2027.",
        "BIS (juillet 2025), America's AI Action Plan. Promotion d'export de full-stack AI export packages aux allies, durcissement vers les adversaires.",
        "ABDC (2025), Brazilian Data Center Association. Mix electrique bresilien : 83 pct renouvelable. Hub Fortaleza : connexions cables sous-marins vers Europe et Afrique.",
        "ABDC (2025) ; Mordor Intelligence (2026). Marche DC IA Bresil : 0,55 Md USD (2025) vers 1,24 Md USD (2030), CAGR 17,5 pct.",
        "BNDES (2025) ; Mesure provisoire Redata (septembre 2025) : reduction 50 pct du cout du capital DC via exoneration impots IT, valide jusqu'a decembre 2026.",
        "Bloomberg (decembre 2025), 'ByteDance Plans 200 Billion-Real Brazilian Data Center'. Partenariat Omnia (Patria Investments) + Casa dos Ventos. 300 MW initiaux, extensibles a 1 GW.",
        "Microsoft (2025), engagement 50 Md USD pour le Sud global d'ici 2030. 2,7 Md USD specifiquement Bresil sur 3 ans.",
        "Scala Data Centers (2025) ; Elea Data Centers (2025). Rio AI City : partenariat Oracle + Nvidia.",
        "Brookings (janvier 2025), op. cit. Pays Tier 2 risquent de developper chaines d'approvisionnement independantes des US, dont liens technologiques renforces avec la Chine.",
        "GAIN AI Act (2025), discussion au Congres americain. Priorite d'acces aux semi-conducteurs avances aux consommateurs americains avant les commandes internationales.",
        "ILIA 2025 (CEPALC/CENIA), section sur le talent IA. Acceleration brain drain de specialistes depuis 2022.",
        "Banque mondiale et OIT (2024-2025) : deficit de productivite persistant en Amerique latine. FMI (mars 2025) : gains TFP IA significativement plus eleves dans les economies avancees.",
        "Designation des cartels de drogue comme organisations terroristes etrangeres (Trump, 2025). Exposition accrue des entreprises operant au Bresil et au Mexique aux regles de controle des exportations US.",
        "BIS, Suspension of the Affiliates Rule for One Year (10 novembre 2025). Affiliates Rule etend restrictions aux filiales d'entites listees.",
        "WEF (2025), proposition de consortium multi-parties prenantes regional (modele GAVI) pour mutualiser les ressources de compute en Amerique latine.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Chapitre VI bis",
    filename="Chapitre_VI_bis_Amerique_Sud_Bresil_FR.docx"
)

# ---------------------------------------------------------------------------
# Content - PORTUGUESE (BRAZIL)
# ---------------------------------------------------------------------------

BR = LangPack(
    code="PT-BR",
    label="CAPITULO VI BIS",
    title="Consequencias para a America do Sul e o Brasil",
    intro=(
        "A analise dos capitulos anteriores concentrou-se no eixo transatlantico EUA-Europa. "
        "No entanto, as consequencias do protecionismo de IA americano estendem-se muito alem da OCDE. "
        "A America do Sul, e o Brasil em particular, constituem um estudo de caso revelador: "
        "simultaneamente um mercado dinamico para a IA, um terreno de competicao geopolitica EUA-China "
        "e uma regiao estruturalmente dependente de computacao estrangeira, ao mesmo tempo em que possui "
        "ativos energeticos unicos. Este capitulo complementar analisa as consequencias especificas "
        "do regime protecionista na America do Sul, com um foco aprofundado no Brasil."
    ),
    sections=[
        ("6bis.1 Posicao estrutural: o Sul Global diante da assimetria de computacao", []),
        ("6bis.1.1 Um ecossistema em crescimento rapido, mas estruturalmente dependente", [
            "A America Latina representa 6,6 por cento do PIB mundial, mas atrai apenas 1,12 por cento do investimento mundial em IA - uma razao de 5,9 que mede o deficit de investimento da regiao.[1] No entanto, os indicadores de adocao sao notavelmente dinamicos. O Indice Latino-Americano de Inteligencia Artificial (ILIA 2025), publicado pela CEPAL e pelo CENIA chileno, classifica tres paises como pioneiros (Chile, Brasil, Uruguai), oito como adotantes (incluindo Colombia, Equador, Costa Rica) e um terco como exploradores com ecossistemas nascentes.[2] A regiao representa 14 por cento das visitas globais a solucoes de IA e ocupa o terceiro lugar mundial em downloads de aplicativos de IA generativa.",
            "Essa dinamica de adocao contrasta com um deficit infraestrutural consideravel. Os paises de alta renda abrigam 77 por cento da capacidade mundial de data centers de colocation (junho de 2025), em comparacao com 18 por cento para os paises de renda media-alta e 5 por cento para os paises de renda media-baixa.[3] Os paises de alta renda tambem concentram 87 por cento dos modelos de IA notaveis, 86 por cento das startups de IA e 91 por cento do capital de risco de IA, embora representem apenas 17 por cento da populacao mundial. A America Latina situa-se na categoria intermediaria: consumidora dinamica de IA, mas quase inteiramente dependente da infraestrutura estrangeira (americana e, cada vez mais, chinesa) para computacao.",
        ]),
        ("6bis.1.2 Classificacao Tier 2: limites de acesso a computacao dos EUA", [
            "Sob a AI Diffusion Rule de janeiro de 2025 (administracao Biden), toda a America Latina - incluindo Brasil, Mexico e Chile - e classificada como Tier 2, o que significa que esta sujeita a limites quantitativos nas importacoes de GPUs avancadas. O Tier 1 (acesso ilimitado) e reservado para 20 aliados proximos (Australia, Canada, Franca, Alemanha, Japao, etc.). O Tier 3 (acesso proibido) visa a China, a Russia e cerca de vinte outros paises.[4]",
            "Para a America do Sul, essa classificacao Tier 2 significa que os projetos de data centers de IA de grande escala sao limitados em termos de volume de GPU importavel. Os limites iniciais sob a AI Diffusion Rule foram de aproximadamente 50.000 GPUs entre 2025 e 2027 para todos os paises Tier 2 (individualmente), um volume claramente insuficiente para alimentar os megaprojetos anunciados. A Brookings observa que, mesmo para os paises Tier 2 mais favorecidos (Brasil, India), os limites americanos significam que suas necessidades de computacao provavelmente nao serao atendidas de forma consistente.[5] Embora a administracao Trump tenha revogado a AI Diffusion Rule em maio de 2025 sem ainda publicar uma regra de substituicao, a incerteza regulatoria cria um risco de fornecimento que pesa sobre as decisoes de investimento. O BIS publicou o Plano de Acao de IA da America em julho de 2025, que promove a exportacao de pacotes de exportacao de IA full-stack para aliados, ao mesmo tempo em que endurece a fiscalizacao em relacao aos adversarios.[6]",
        ]),
        ("6bis.2 Brasil: hub emergente entre dois blocos", []),
        ("6bis.2.1 Ativos estruturais do Brasil para a IA", [
            "O Brasil possui vantagens competitivas objetivas para a infraestrutura de IA. Sua matriz eletrica e 83 por cento renovavel (essencialmente hidroeletrica, complementada pela energia eolica e solar em rapido crescimento), com um custo de eletricidade competitivo de aproximadamente 0,08 USD/kWh. O Sistema Interligado Nacional (SIN) possui capacidade excedente, e o pais possui uma base de cabos submarinos de telecomunicacoes (notadamente o hub de Fortaleza) que oferece uma das rotas mais curtas para a Europa e a Africa.[7]",
            "O mercado brasileiro de data centers e o maior da America Latina, representando mais de 41 por cento dos investimentos regionais. A capacidade de TI instalada atingiu aproximadamente 1 GW ate o final de 2025, com 202 projetos ativos e 23 conclusoes planejadas ate o final de 2026. O mercado de data centers de IA especificamente e avaliado em 0,55 bilhao de USD em 2025, projetado para alcancar 1,24 bilhao ate 2030 (crescimento anual de 17,5 por cento).[8] A Associacao Brasileira de Data Centers (ABDC) projeta que a demanda de energia dos data centers pode chegar a 13,7 GW ate 2035.",
            "O governo Lula tomou medidas concretas para acelerar o desenvolvimento. Em setembro de 2025, foi adotada a medida provisoria Redata, criando um regime tributario especial que reduz o custo de capital para data centers em 50 por cento por meio da isencao de impostos sobre ativos de TI, com beneficios validos ate dezembro de 2026. O Plano Brasileiro de Inteligencia Artificial (PBIA) visa transformar o pais em um hub global de data centers, e o BNDES lancou um fundo dedicado a IA e data centers com capital inicial de 500 milhoes a 1 bilhao de reais (93-187 milhoes de USD).[9]",
        ]),
        ("6bis.2.2 Megaprojetos e dualidade EUA-China", [
            "O Brasil tornou-se palco de competicao direta entre investimentos americanos e chineses em infraestrutura de IA, uma dualidade que revela as dinamicas criadas pelo protecionismo dos EUA.",
            "No lado chines, o projeto mais espetacular e o data center do TikTok-ByteDance em Pecem (Ceara), anunciado em dezembro de 2025: 200 bilhoes de reais (aproximadamente 38 bilhoes de USD), em parceria com a desenvolvedora Omnia (Patria Investments) e a produtora de energia renovavel Casa dos Ventos.[10] O projeto, cuja construcao deve comecar em abril de 2026, sera alimentado inteiramente por energia eolica (300 MW iniciais, expansiveis para 900 MW ou ate 1 GW). Constitui o maior investimento privado em data center ja anunciado no Brasil e o primeiro projeto da ByteDance na America Latina. O investimento ocorre em um contexto em que o TikTok enfrenta ameacas de bloqueio nos Estados Unidos e onde a China busca diversificar sua infraestrutura fora de sua zona de risco geopolitico direto.",
            "No lado americano, a Microsoft anunciou um investimento de 2,7 bilhoes de USD ao longo de tres anos em infraestrutura de nuvem e IA no Brasil, como parte de seu compromisso global de 50 bilhoes de USD para o Sul Global ate 2030.[11] AWS e Google ja possuem regioes de nuvem no Brasil (Sao Paulo). Os hyperscalers dos EUA controlam aproximadamente 55 por cento do mercado de nuvem brasileiro (AWS, Azure, GCP), uma dominancia menor do que na Europa (70 por cento), mas suficiente para estruturar a dependencia.",
            "Outros megaprojetos ilustram a escala das ambicoes. A Scala Data Centers anunciou a AI City de Eldorado do Sul (Rio Grande do Sul), com 1.800 MW de capacidade e um potencial de 5.000 MW ate 2033. A Elea Data Centers esta desenvolvendo a Rio AI City, apresentada como o maior campus de data centers da America Latina, com 1,8 GW de capacidade ate 2027 e 3,2 GW ate 2032, com a Oracle e a Nvidia como parceiras tecnologicas.[12]",
        ]),
        ("6bis.3 Impacto do protecionismo dos EUA na America do Sul", []),
        ("6bis.3.1 O duplo vinculo da classificacao Tier 2", [
            "A posicao Tier 2 do Brasil e da America do Sul cria um duplo vinculo estrategico. Por um lado, os limites de importacao de GPU restringem a capacidade dos paises de construir infraestrutura de IA soberana e realizar os megaprojetos anunciados. Por outro lado, as restricoes americanas em relacao a China (Tier 3) empurram a ByteDance e outros atores chineses a investir pesadamente na America Latina como zona alternativa de implantacao de infraestrutura. O Brasil torna-se, assim, um terreno de substituicao na rivalidade EUA-China.",
            "A Brookings alerta que essa situacao pode levar os paises Tier 2 a desenvolver cadeias de suprimentos independentes dos Estados Unidos, incluindo lacos tecnologicos mais fortes com a China.[13] O Brasil, cujo principal parceiro comercial e a China, ilustra perfeitamente essa dinamica. O investimento TikTok-Pecem, o maior investimento tecnologico chines na America Latina, faz parte de um aprofundamento dos lacos China-Brasil que antecedeu a reeleicao de Trump, mas acelerou diante das politicas comerciais americanas.",
        ]),
        ("6bis.3.2 Cinco canais de impacto", [
            "O impacto do protecionismo de IA americano na America do Sul e transmitido atraves de cinco canais distintos, alguns dos quais sao especificos da regiao.",
            "Canal 1 - Restricao direta ao hardware de IA. Os limites Tier 2 em GPUs de ponta restringem a capacidade de construcao. Mesmo que a AI Diffusion Rule seja revogada, a incerteza regulatoria pesa: projetos que exigem de 10.000 a 100.000 GPUs (como Scala AI City ou Elea Rio AI City) dependem inteiramente da disposicao americana em entregar aceleradores Nvidia ou AMD. O GAIN AI Act, atualmente em discussao no Congresso dos EUA, propoe dar prioridade de acesso a semicondutores avancados aos consumidores americanos antes de atender aos pedidos internacionais - o que degradaria ainda mais o fornecimento da regiao.[14]",
            "Canal 2 - Dependencia reforçada da nuvem dos EUA. Na ausencia de infraestrutura local suficiente, as empresas brasileiras recorrem pesadamente a nuvem dos EUA. O setor financeiro brasileiro (Itau, Nubank, Bradesco) e o mais digitalizado da America Latina, com 95 por cento das transacoes processadas digitalmente no Itau Unibanco. O Open Banking brasileiro conecta 800 instituicoes. Essa digitalizacao depende em grande parte dos hyperscalers dos EUA, criando o mesmo padrao de dependencia da Europa (Capitulo IV), mas com menos poder de barganha.",
            "Canal 3 - Bifurcacao tecnologica EUA-China. O Brasil depara-se com um risco especifico: a fragmentacao da sua infraestrutura de IA entre os ecossistemas americano e chines. Os data centers de Pecem (ByteDance), embora alimentados por energia renovavel brasileira, provavelmente usarao hardware da Huawei ou alternativas nao-EUA se as restricoes americanas impedirem a exportacao de GPUs Nvidia para projetos chineses. Essa dualidade de hardware cria problemas de interoperabilidade, soberania de dados (Lei CLOUD dos EUA versus lei de seguranca de dados chinesa) e padronizacao. O Brasil corre o risco de se tornar um espaco onde coexistem dois ecossistemas tecnologicos incompativeis, fragmentados e cada um dependente de uma potencia externa.",
            "Canal 4 - Fuga de cerebros amplificada. O ILIA 2025 sinaliza um alargamento do fosso de talentos de IA na America Latina desde 2022, associado a uma aceleracao da fuga de cerebros de especialistas.[15] O Brasil forma excelentes engenheiros (USP, Unicamp, ITA), mas o diferencial de remuneracao com os Estados Unidos e ainda mais acentuado do que na Europa. A assimetria de computacao agrava essa fuga: pesquisadores de IA que permanecem no Brasil nao tem acesso a computacao necessaria para pesquisa de fronteira, o que reforca a atratividade dos laboratorios americanos.",
            "Canal 5 - Fosso de produtividade ampliado. O Banco Mundial e a OIT observam que a America Latina sofre de um deficit de produtividade persistente, em grande parte ligado a barreiras a inovacao e adocao tecnologica.[16] Se os paises de alta renda captarem os ganhos de produtividade da IA (FMI: ganhos de PTF significativamente maiores em economias avancadas), o protecionismo de IA corre o risco de transformar o que era um atraso na adocao (buffer temporario) em uma barreira estrutural (gargalo). O acesso restrito a computacao de ponta impede que as empresas latino-americanas realizem os ganhos teoricos de produtividade da IA, ampliando a lacuna com os Estados Unidos.",
        ]),
        ("6bis.4 Cenarios especificos para o Brasil", [
            "Ao aplicar a matriz de cenarios 2x2 do Capitulo V, os cenarios para o Brasil diferem da Europa porque o Brasil possui uma variavel adicional: a possibilidade de jogar a carta chinesa como alternativa ao ecossistema dos EUA. A Tabela 17 detalha as quatro trajetorias possiveis.",
            "Cenario A' (Hub Neutro Dual) e o mais provavel no curto prazo. O Brasil mantem relacoes comerciais estreitas com ambos os blocos e nao tem interesse em alinhar-se exclusivamente. No entanto, este cenario e inerentemente instavel: os Estados Unidos podem impor condicoes (restricoes ao uso de GPUs Nvidia em data centers que tambem hospedam cargas de trabalho chinesas), forcando o Brasil a escolher. A designacao dos carteis de drogas como organizacoes terroristas estrangeiras por Trump ja aumentou a exposicao das empresas que operam no Brasil e no Mexico as regras de controle de exportacao dos EUA.[17]",
            "Cenario B' (Sancoes Secundarias) representa o risco maximo. Se os Estados Unidos decidissem aplicar sancoes secundarias contra paises que hospedam infraestrutura de IA chinesa significativa, o Brasil enfrentaria um dilema existencial: perder o acesso ao ecossistema tecnologico americano (Nvidia, AWS, Azure) ou renunciar a investimentos chineses massivos. Este cenario, embora improvavel no curto prazo, nao e hipotetico: os Estados Unidos ja aplicaram sancoes secundarias ao petroleo russo e venezuelano, e a Affiliates Rule (suspensa ate novembro de 2026) estende as restricoes a subsidiarias de entidades listadas.[18]",
        ]),
        ("6bis.5 America do Sul alem do Brasil", [
            "As outras economias da America do Sul passam pelas mesmas dinamicas que o Brasil, mas com menos peso de barganha e menos ativos estruturais.",
            "O Chile, classificado como pioneiro pelo ILIA 2025, beneficia-se de temperaturas favoraveis (reduzindo o consumo de energia para resfriamento) e de um ecossistema de governanca de IA avancado. A Microsoft lancou o Chile Central em junho de 2025, sua primeira regiao de nuvem no pais, associada ao programa Transforma Chile (180.000 pessoas treinadas, 81.000 empregos criados). Mas o Chile continua inteiramente dependente do hardware e da nuvem americanos, sem a alternativa chinesa que o Brasil possui.",
            "O Mexico, vizinho imediato dos Estados Unidos, apresenta um perfil diferente. O nearshoring (relocalizacao da producao da Asia) transformou o cenario economico, e os data centers beneficiam-se da proximidade com o mercado dos EUA. No entanto, o Mexico e mais vulneravel ao protecionismo americano devido ao USMCA (renovavel em julho de 2026) e a designacao dos carteis como organizacoes terroristas. Sua infraestrutura energetica para data centers tambem e menos competitiva que a do Brasil.",
            "A Colombia, a Argentina e o Peru, classificados como adotantes, enfrentam restricoes ainda maiores: infraestrutura eletrica fragil, capital humano de IA limitado e poder de barganha quase nulo com os provedores de GPU. Para esses paises, o protecionismo de IA americano traduz-se principalmente em acesso atrasado e mais caro as ferramentas de IA, ampliando o fosso de produtividade nao apenas com os Estados Unidos, mas tambem com o Brasil e o Chile dentro da propria regiao.",
        ]),
        ("6bis.6 Sintese: um risco de tripla fratura", [
            "A analise neste capitulo revela que o protecionismo de IA americano produz um risco de tripla fratura na America do Sul, especifico da regiao e distinto do cenario europeu.",
            "Fratura Norte-Sul. O fosso de computacao entre os Estados Unidos e a America do Sul e muito mais pronunciado do que o fosso EUA-Europa. Enquanto a razao bruta EUA/UE(13) e de 17,6:1 na computacao instalada operacional e a razao CACI(EUA)/CACI(UE) e de 3,46:1 (Capitulo III, linha de base de abril de 2026), uma razao equivalente CACI(EUA)/CACI(Brasil) estaria na faixa de 30-50:1 no CACI Power Mode e bem acima de 100:1 na computacao bruta, refletindo a combinacao de um deficit na capacidade computacional instalada, capital humano de IA mais limitado e um custo de capital mais elevado (Selic brasileira a 14,25 por cento no final de 2025). Esta lacuna e tal que a recuperacao e quase impossivel ate 2030 sem ajuda externa massiva.",
            "Fratura Leste-Oeste. A rivalidade EUA-China pela infraestrutura de IA na America do Sul cria um risco de fragmentacao tecnologica sem paralelo na Europa. O Brasil pode encontrar-se com dois ecossistemas paralelos incompativeis (nuvem dos EUA versus infraestrutura chinesa), cada um respondendo a sua propria logica geopolitica em vez das necessidades da economia local. A Europa, como aliada Tier 1, nao enfrenta essa bifurcacao direta na computacao, mesmo que o pivo Nuvem-Nacionalidade analisado no Capitulo V crie uma vulnerabilidade distinta nas cargas de trabalho na nuvem.",
            "Fratura intra-regional. Dentro da America do Sul, o Brasil atrai a maioria dos investimentos em IA (41 por cento do mercado LATAM), seguido pelo Chile e pelo Mexico. Os paises 'exploradores' (um terco da regiao de acordo com o ILIA 2025) correm o risco de serem inteiramente excluidos da economia de IA, reproduzindo um padrao de dependencia analogo ao das materias-primas. O WEF sugere um consorcio regional de multiplas partes interessadas (modelo GAVI) para agrupar recursos de computacao e democratizar o acesso a IA.[19]",
            "Para o Brasil especificamente, o principal desafio estrategico e transformar seus ativos energeticos (matriz 83 por cento renovavel) em soberania de computacao, evitando que a competicao EUA-China fragmente seu ecossistema. A comparacao com a Franca e esclarecedora: ambos os paises possuem um ativo energetico distintivo (nuclear para a Franca, renovavel para o Brasil), um campeao tecnologico nacional emergente (Mistral para a Franca, ecossistema fintech/Nubank para o Brasil) e uma ambicao de hub regional de IA. Mas o Brasil enfrenta restricoes adicionais (classificacao Tier 2, custo de capital, fuga de cerebros amplificada) que tornam sua trajetoria mais incerta e sua vulnerabilidade ao protecionismo mais aguda.",
        ]),
    ],
    tables=[
        ("Tabela 16. Principais projetos de data centers de IA no Brasil (2025-2030).",
         "Fonte: Compilacao do autor a partir de Bloomberg, IndustrialInfo, Introl.",
         [
             ["Projeto", "Origem", "Investimento", "Capacidade", "Caracteristica"],
             ["TikTok Pecem", "China", "~38 Bi USD", "300 MW a 1 GW", "100% eolica; 1º projeto LATAM da ByteDance"],
             ["Scala AI City", "Brasil/EUA", "Multi-Bi USD", "1,8 a 5 GW", "Maior instalacao planejada na America do Sul"],
             ["Elea Rio AI City", "Brasil/EUA", "Multi-Bi USD", "1,8 a 3,2 GW", "Oracle + Nvidia parceiras tecnologicas"],
             ["Microsoft Azure", "EUA", "2,7 Bi USD (3 anos)", "N/D", "Nuvem + IA + programa ConectaAI"],
             ["AWS Sao Paulo", "EUA", "N/D", "Multiplas AZ", "Regiao de nuvem ativa desde 2011"],
         ]),
        ("Tabela 17. Cenarios especificos do Brasil diante do protecionismo de IA dos EUA 2026-2030.",
         "Fonte: Construcao do autor, calibracao na linha de base de abril de 2026 (EUA/UE(13) bruto 17,6:1, CACI Power Mode 3,46:1).",
         [
             ["Cenario Brasil", "Probabilidade", "Consequencias Positivas", "Riscos"],
             ["A': Hub Neutro Dual EUA-China", "35-45%",
              "Entrada de investimentos de ambos os blocos; energia renovavel como ativo; diversificacao de fornecedores",
              "Fragmentacao do ecossistema; pressao dos EUA para limitar acesso chines; vulnerabilidade de dados"],
             ["B': Sancoes Secundarias", "15-20%",
              "Aceleracao do investimento chines substitutivo",
              "Perda de acesso ao ecossistema dos EUA (Nvidia, nuvem); isolamento tecnologico parcial"],
             ["C': Alinhamento Pro-EUA", "20-25%",
              "Acesso Tier 1 negociado; GPUs ilimitadas; aumento do investimento Microsoft/AWS",
              "Dependencia total dos EUA; perda de investimento chines (Pecem ameacado)"],
             ["D': Soberania Regional LATAM", "10-15%",
              "Consorcio regional de computacao; reducao da dependencia; pooling de energia",
              "Capacidade de execucao limitada; capital insuficiente; atraso de 5-10 anos"],
         ]),
    ],
    notes=[
        "CEPAL/CENIA (outubro de 2025), Latin American Artificial Intelligence Index (ILIA 2025). A America Latina representa 6,6% do PIB mundial e 1,12% do investimento mundial em IA.",
        "CEPAL/CENIA (2025), ibid. Tres categorias: pioneiros (Chile, Brasil, Uruguai, mais de 60 pts), adotantes (Colombia, Equador, Costa Rica, Republica Dominicana), exploradores (ecossistemas nascentes).",
        "Banco Mundial (novembro de 2025), Digital Progress and Trends Report 2025: Strengthening AI Foundations. Paises de alta renda: 77% capacidade DC de colocation, 87% modelos de IA notaveis, 86% startups de IA, 91% VC de IA.",
        "BIS (janeiro de 2025), Framework for Artificial Intelligence Diffusion. Tier 1: 20 paises aliados (acesso ilimitado). Tier 2: ~140 paises, incluindo todo o continente americano fora EUA/Canada (limites quantitativos). Tier 3: ~20 paises (acesso proibido). Regra revogada em maio de 2025 pela administracao Trump, substituicao pendente.",
        "Brookings (2025), 'Trump's AI export controls and the AI Diffusion Rule'. Limites iniciais: ~50.000 GPUs por pais Tier 2 ao longo de 2025-2027.",
        "BIS (julho de 2025), America's AI Action Plan. Promocao de pacotes de exportacao de IA full-stack para aliados, endurecimento em relacao aos adversarios.",
        "ABDC (2025), Associacao Brasileira de Data Centers. Matriz eletrica brasileira: 83% renovavel. Hub de Fortaleza: conexoes de cabos submarinos para Europa e Africa.",
        "ABDC (2025); Mordor Intelligence (2026). Mercado de DC de IA no Brasil: 0,55 Bi USD (2025) a 1,24 Bi USD (2030), CAGR 17,5%.",
        "BNDES (2025); medida provisoria Redata (setembro de 2025): reducao de 50% no custo de capital de DC via isencao de impostos de TI, valida ate dez de 2026.",
        "Bloomberg (dezembro de 2025), 'ByteDance Plans 200 Billion-Real Brazilian Data Center'. Parceria Omnia (Patria Investments) + Casa dos Ventos. 300 MW iniciais, expansiveis para 1 GW.",
        "Microsoft (2025), compromisso de 50 Bi USD para o Sul Global ate 2030. 2,7 Bi USD especificamente para o Brasil em 3 anos.",
        "Scala Data Centers (2025); Elea Data Centers (2025). Rio AI City: parceria Oracle + Nvidia.",
        "Brookings (janeiro de 2025), op. cit. Paises Tier 2 correm o risco de desenvolver cadeias de suprimentos independentes dos EUA, incluindo lacos tecnologicos reforcados com a China.",
        "GAIN AI Act (2025), discussao no Congresso dos EUA. Prioridade de acesso a semicondutores avancados para consumidores americanos antes de pedidos internacionais.",
        "ILIA 2025 (CEPAL/CENIA), secao de talentos de IA. Aceleracao da fuga de cerebros de especialistas desde 2022.",
        "Banco Mundial e OIT (2024-2025): deficit de produtividade persistente na America Latina. FMI (marco de 2025): ganhos de PTF de IA significativamente maiores em economias avancadas.",
        "Designacao dos carteis de drogas como organizacoes terroristas estrangeiras (Trump, 2025). Aumento da exposicao das empresas que operam no Brasil e no Mexico as regras de controle de exportacao dos EUA.",
        "BIS, Suspension of the Affiliates Rule for One Year (10 de novembro de 2025). Affiliates Rule estende restricoes a subsidiarias de entidades listadas.",
        "WEF (2025), proposta de consorcio regional de multiplas partes interessadas (modelo GAVI) para agrupar recursos de computacao na America Latina.",
    ],
    footer="AI for Americans First - Fabrice Pizzi - Capitulo VI bis",
    filename="Capitulo_VI_bis_Americas_Brasil_PT-BR.docx"
)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

LANGS = [EN, FR, BR]

def build_all(out_dir: Path) -> None:
    for lp in LANGS:
        log.info("Building Chapter VI bis [%s] -> %s", lp.code, lp.filename)
        doc = init_document()
        # Figures
        fig_dir = out_dir / "figures_ch6"
        
        # Build document
        add_cover(doc, lang=lp.code, chapter_label=lp.label, chapter_subtitle=lp.title)
        add_chapter_header(doc, label=lp.label, title=lp.title, intro=lp.intro)
        
        for title, paragraphs in lp.sections:
            render_section(doc, title, paragraphs)
            
            # Insert images after specific sections
            if title.startswith("6bis.1 "):
                img_path = fig_dir / f"Fig_6bis.2_LATAM_Deficit_{lp.code}.png"
                render_image(doc, img_path, width_inches=6.0)
            elif title.startswith("6bis.4"):
                img_path = fig_dir / f"Fig_6bis.1_Brazil_Scenarios_{lp.code}.png"
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
