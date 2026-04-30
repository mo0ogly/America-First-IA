"""
Annexe B - Working Paper CACI - generateur FR.

Genere le .docx de l'Annexe B (Working Paper CACI) en francais.

Working Paper academique formalisant l'indice CACI au format article
de revue economique, avec codes JEL et structure standard
(introduction, revue de litterature, cadre theorique, donnees,
resultats, scenarios, recommandations, conclusion).

Annexe B consolidee sur le baseline avril 2026 :
    - Formule Power Mode geometrique : F^0,40 x L^0,20 x R^0,15 / E^0,25
    - Ratio US/UE Power Mode : 3,46:1 (au lieu de 3,4:1)
    - Ratio brut compute installe : 17,6:1
    - Section 3.4 NEW : extension Phys/Sov (Chap I Fig 1.8)
    - Couts energie PPA-ajustes : USA 85 USD/MWh, UE 135 USD/MWh,
      France 115 USD/MWh, ratio 1,59x (au lieu de 50-65 vs 110-145)
    - Correction §5.3.2 : la formule consolidee EST la formule Power
      Mode, pas une alternative

Numerotation des tableaux : annexe B (Tab B.1, B.2, B.3, B.4).

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
from pathlib import Path

from wp_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("annexe_b_wp_caci_fr")


CHAPTER_LABEL = "ANNEXE B - WORKING PAPER"
CHAPTER_TITLE = (
    "Le Compute-Adjusted Competitiveness Index (CACI) : "
    "mesurer l'impact du protectionnisme IA americain sur la competitivite mondiale en IA"
)
CHAPTER_INTRO = (
    "Cette annexe presente le Working Paper formalisant l'indice CACI au format article de "
    "revue economique. Il introduit le Compute-Adjusted Competitiveness Index (CACI), un "
    "indicateur composite inedit concu pour mesurer la competitivite nationale en IA en "
    "capturant l'interaction entre la capacite de calcul installee, les couts energetiques, "
    "le PIB et la main-d'oeuvre IA. Codes JEL : F13 (Politique commerciale), L63 "
    "(Semi-conducteurs), O33 (Changement technologique), O38 (Politique publique). "
    "Mots-cles : competitivite IA, ecart de compute, protectionnisme technologique, controles "
    "a l'export, CACI, donnees de panel, semi-conducteurs, politique energetique, Section 232, "
    "souverainete numerique europeenne, Cloud Sovereignty Mandates, decomposition Phys/Sov."
)


SECTIONS: list[tuple[str, list[str]]] = [
    ("B.1 Introduction", [
        "L'intelligence artificielle remodele les fondements de la competitivite economique mondiale. Depuis le lancement de ChatGPT en novembre 2022 et la vague d'investissements dans les modeles de fondation qui a suivi, l'IA generative est apparue comme une technologie de transformation transversale. Pourtant, l'acces a l'infrastructure necessaire pour entrainer et deployer des modeles frontier - en particulier les GPU avances et l'energie abordable pour les centres de donnees - est devenu profondement asymetrique.",
        "Dans ce contexte, les Etats-Unis ont progressivement erige un regime de controle sur l'acces aux technologies IA de pointe. A partir d'octobre 2022, le Bureau of Industry and Security (BIS) a impose des restrictions sur les exportations de GPU avances vers la Chine. En janvier 2025, l'AI Diffusion Rule a segmente le monde en trois niveaux d'acces. En mai 2025, l'administration Trump a abroge cette regle et l'a remplacee en janvier 2026 par une regle finale combinant des tarifs de 25 pour cent (Section 232) sur les semi-conducteurs IA avances avec des controles a l'export revises.",
        "Ces mesures, officiellement motivees par des imperatifs de securite nationale, produisent de facto un avantage concurrentiel structurel pour les entreprises americaines : celles-ci jouissent d'un acces illimite au compute de pointe, tandis que les acteurs d'autres regions - y compris les allies europeens - font face a des contraintes croissantes en termes de cout, de disponibilite et de certitude reglementaire.",
        "Malgre l'ampleur de ces evolutions, la litterature economique manque d'un cadre quantitatif pour mesurer l'ecart de competitivite qui en resulte. Les indicateurs existants - depenses de R&D, nombre de brevets, metriques de publications IA - ne capturent pas l'infrastructure materielle qui determine de plus en plus la capacite productive en IA. Cet article comble cette lacune en proposant le Compute-Adjusted Competitiveness Index (CACI), un indicateur composite qui integre la capacite de calcul installee, le cout energetique, le PIB et la main-d'oeuvre IA dans un cadre analytique unique.",
        "Nos contributions sont quadruples. Premierement, nous formalisons le compute comme quatrieme facteur de production a l'ere de l'IA, en nous appuyant sur la theorie des technologies a usage general de Bresnahan et Trajtenberg (1995). Deuxiemement, nous construisons et validons le CACI par des methodes econometriques a l'aide de donnees de panel couvrant 12 economies (2020-2024), demontrant sa significativite statistique en tant que predicteur de la productivite sectorielle IA. Troisiemement, nous appliquons le cadre CACI pour quantifier l'ecart de competitivite IA entre les Etats-Unis et l'Europe (ratio brut 17,6:1, ratio CACI Power Mode 3,46:1 sur snapshot avril 2026) et proposer des scenarios prospectifs pour 2026-2030. Quatriemement, nous introduisons la decomposition Phys/Sov (section 3.4) qui dissocie le compute physiquement installe du compute legalement controlable, distinction operationnelle des le snapshot avril 2026 (cas EAU 99,6 pct US-side) et systemique sous regime Cloud Sovereignty Mandates 2028.",
        "L'article est structure comme suit. La section 2 passe en revue la litterature pertinente. La section 3 presente le cadre CACI, sa definition formelle et l'extension Phys/Sov. La section 4 decrit nos donnees et notre methodologie empirique. La section 5 rapporte les resultats econometriques. La section 6 analyse l'ecart de compute US-UE. La section 7 developpe des scenarios prospectifs. La section 8 discute les implications politiques.",
    ]),
    ("B.2 Revue de litterature", []),
    ("B.2.1 L'IA comme technologie a usage general", [
        "L'intuition fondatrice de notre cadre provient de la theorie des technologies a usage general (TUG) de Bresnahan et Trajtenberg (1995). Les TUG se caracterisent par leur omnipresence, leur potentiel inherent d'amelioration et leurs complementarites d'innovation. L'IA - en particulier les grands modeles de langage et les modeles de fondation - satisfait clairement ces criteres. Cependant, contrairement aux TUG precedentes (vapeur, electricite, semi-conducteurs), l'IA necessite une infrastructure de calcul massive dont le cout et la distribution sont tres inegaux.",
        "Brynjolfsson, Rock et Syverson (2019) apportent le complement crucial avec leur theorie de la courbe en J : les gains de productivite des TUG sont retardes car les entreprises doivent investir dans des actifs complementaires - restructuration organisationnelle, formation des travailleurs, refonte des processus - avant de recolter les benefices. Cela implique que les pays ayant un acces precoce au compute ont un avantage doublement croissant : ils debutent la courbe en J plus tot et accumulent des actifs complementaires que les retardataires ne peuvent pas facilement dupliquer.",
    ]),
    ("B.2.2 Interdependance instrumentalisee et controle des points d'etranglement", [
        "Farrell et Newman (2019) introduisent le concept d'interdependance instrumentalisee : les Etats peuvent exploiter la structure asymetrique des reseaux mondiaux pour contraindre d'autres acteurs. Ils identifient deux mecanismes : l'effet panoptique (surveillance via le controle des noeuds d'information) et l'effet d'etranglement (perturbation via le controle des goulots d'approvisionnement). Le monopole de conception de Nvidia (plus de 80 pct des GPU d'entrainement IA) et le monopole d'ASML en lithographie EUV constituent deux points d'etranglement exploitables.",
        "Les controles a l'export d'octobre 2022, l'AI Diffusion Rule et la Section 232 instrumentalisent explicitement ces points d'etranglement. L'administration Trump a propose de monetiser ce levier (25 pct des revenus des ventes chinoises, septembre 2025), marquant une transition du deni d'acces vers l'extraction de rentes - une evolution theoriquement significative que les cadres de securite nationale seuls ne peuvent expliquer.",
    ]),
    ("B.2.3 La lacune de mesure", [
        "Les indices de competitivite existants ne capturent pas la dimension compute. Le Global AI Index (Tortoise), le AI Index de Stanford HAI et le Digital Economy Outlook de l'OCDE utilisent des proxies comme les depenses de R&D, le nombre de publications et les depots de brevets. Ceux-ci sont utiles mais ne mesurent pas le facteur qui determine de plus en plus la capacite productive : l'infrastructure de calcul installee et son cout d'exploitation. Le CACI est concu pour combler cette lacune.",
    ]),
    ("B.3 Le cadre CACI", []),
    ("B.3.1 Fondement conceptuel", [
        "Nous soutenons que la competitivite IA au niveau national est determinee par quatre facteurs en interaction : (i) la capacite de calcul installee F, (ii) le cout energetique pour les centres de donnees E, (iii) la main-d'oeuvre qualifiee en IA L, et (iv) l'acces reglementaire R (classification Tier 1/2/3 du regime BIS). Le CACI capture leur interaction dans une structure multiplicative geometrique qui reflete les complementarites entre facteurs.",
        "L'intuition est la suivante. La capacite IA effective d'un pays est croissante en compute (plus de FLOPs signifie que plus de modeles peuvent etre entraines et plus d'inferences traitees), croissante en main-d'oeuvre (sans operateurs qualifies, le compute reste un actif theorique), croissante en acces reglementaire (un pays Tier 3 perd l'acces aux GPU de pointe), et decroissante en cout energetique (une electricite moins chere rend chaque FLOP plus abordable et donc plus productif).",
    ]),
    ("B.3.2 Definition formelle Power Mode", [
        "Nous adoptons la formulation Power Mode geometrique avec ponderations consolidees :",
        "CACI(r,t) = F(r,t)^0,40 x L(r,t)^0,20 x R(r,t)^0,15 / E(r,t)^0,25",
        "ou F(r,t) est la capacite de calcul IA installee de la region r au temps t mesuree en H100-equivalents (source : Epoch AI, Hawkins et al. 2025, CFG Europe), E(r,t) est le cout energetique pour les centres de donnees en USD/MWh ajuste-PPA (source : Eurostat, EIA, AIE 2025), L(r,t) est la main-d'oeuvre IA en millions, approchee par les diplomes STEM plus certifications IA (source : OCDE, LinkedIn Economic Graph), et R(r,t) est l'indice d'acces reglementaire (1,0 pour Tier 1, 0,6 pour Tier 2, 0,2 pour Tier 3, source : BIS, AI Diffusion Rule).",
        "Les ponderations sont F = 0,40 (compute, dominant), L = 0,20 (capital humain), R = 0,15 (acces reglementaire), E = 0,25 (cout energetique, denominateur). La somme des numerateurs (F + L + R) vaut 0,75 et le denominateur (E) vaut 0,25, ce qui produit une fonction de production a rendements d'echelle constants en log apres normalisation. Le CACI est interpretable comme le ratio de l'offre effective de compute a la demande economique de compute. Un CACI plus eleve indique une plus grande intensite de compute IA par rapport a la taille economique - un avantage structurel a l'ere de l'IA.",
    ]),
    ("B.3.3 Proprietes et limites", [
        "La structure multiplicative capture les complementarites entre composantes : un pays avec un compute eleve mais une energie prohibitivement chere obtient un score inferieur a celui ayant un compute modere et une energie bon marche. La formulation geometrique evite un pur effet de taille : les petites economies avancees (Suede, Canada) peuvent obtenir des scores comparables a ceux de grandes economies avec un compute absolu moindre mais mieux distribue.",
        "Nous reconnaissons plusieurs limites. Premierement, le CACI standard ne capture pas la dimension juridictionnelle du compute - un cluster physiquement localise dans la juridiction A mais detenu par un operateur de la juridiction B est traite comme du compute de A. La section 3.4 ci-dessous introduit la decomposition Phys/Sov pour traiter cette limitation. Deuxiemement, la qualite de la main-d'oeuvre est imparfaitement approchee par la quantite. Troisiemement, les effets reglementaires operent avec des decalages que notre indice statique ne capture pas entierement.",
    ]),
    ("B.3.4 Extension Phys/Sov : decomposition juridictionnelle", [
        "L'experience documentee au chapitre VI ter de l'etude principale (cas des Emirats arabes unis : 99,6 pct du F_total emirati detenu par des operateurs US-side) revele que la simple localisation physique du compute peut masquer une dependance juridictionnelle critique. Pour traiter cette dimension, nous decomposons F en deux composantes multiplicatives :",
        "F(r,t) = F_phys(r,t) x F_sov(r,t)",
        "ou F_phys est le compute physiquement installe dans la juridiction r et F_sov est la fraction de F_phys hors juridiction US (donc insensible aux Cloud Sovereignty Mandates hypothetiques de 2028). La decomposition est calculee de maniere rigoureuse depuis le champ Owner du jeu de donnees Epoch AI : pour chaque cluster operationnel, le proprietaire est classe en US-side (Microsoft, Google, AWS, Meta, OpenAI, Oracle, Stargate, etc.) ou non-US-side (operateurs domestiques nationaux).",
        "Le CACI Power Mode admet ainsi deux variantes : CACI_Phys utilise F = F_phys (mesure physique pure) et CACI_Sov utilise F = F_phys x F_sov (mesure souveraine, integrant la juridiction). Les deux metriques s'accordent la ou le compute installe est detenu par des operateurs domestiques (US, Chine, France domestique Fluidstack/Sesterce) ; elles divergent fortement pour les juridictions ou les clusters domestiquement localises sont detenus par des operateurs US-side. Le tableau B.4 presente la decomposition pour les regions principales sur le snapshot avril 2026.",
    ]),
    ("B.4 Donnees et strategie empirique", []),
    ("B.4.1 Construction du panel", [
        "Nous construisons un panel equilibre couvrant 12 economies sur la periode 2020-2024 (N = 60 observations). L'echantillon comprend les Etats-Unis, la Chine, le Royaume-Uni, l'Allemagne, la France, le Japon, la Coree du Sud, l'Inde, le Canada, les Pays-Bas, le Bresil et la Suede. La selection reflete la couverture des donnees et la diversite geographique.",
        "Le tableau B.1 detaille les variables retenues et leurs sources. Les controles supplementaires incluent les depenses de R&D (pct du PIB), la penetration d'Internet, un indice de charge reglementaire, et une variable muette pour les controles a l'export americains (1 pour la Chine post-2022, 0,5 pour les pays Tier 2 post-2024).",
    ]),
    ("B.4.2 Specification econometrique", [
        "Nous estimons le modele log-log suivant, permettant une interpretation en termes d'elasticites :",
        "ln(PROD_it) = alpha + beta1 ln(CACI_it) + beta2 ln(GDP/cap_it) + beta3 REG_it + beta4 EXPORT_it + mu_i + lambda_t + epsilon_it",
        "ou PROD_it est le gain de productivite sectorielle IA du pays i au temps t, CACI_it est l'indice composite Power Mode, GDP/cap est un proxy de developpement, REG capture la charge reglementaire, EXPORT est la variable de controle a l'export, mu_i sont les effets fixes pays, et lambda_t sont les effets fixes temporels.",
        "Nous comparons trois estimateurs : (M1) MCO groupes avec erreurs-types robustes a l'heteroscedasticite (White/HC1), fournissant une borne inferieure conservative ; (M2) Effets Fixes (estimateur intra) avec effets entite et temps, erreurs-types regroupees par pays ; et (M3) Effets Aleatoires (GLS), compare aux EF via le test de Hausman.",
    ]),
    ("B.5 Resultats econometriques", []),
    ("B.5.1 Resultats principaux", [
        "Le tableau B.2 presente les resultats des trois specifications. Le coefficient de ln(CACI) est positif et statistiquement significatif au seuil de 1 pour cent dans les trois specifications. L'estimateur a effets fixes - privilegie par le test de Hausman (chi2 = 13,91, p = 0,001) - donne une elasticite de 0,251 : une augmentation de 10 pour cent du CACI est associee a une hausse de 2,5 pour cent de la productivite sectorielle IA.",
        "Le R2 intra de 0,692 dans le modele EF indique que le CACI Power Mode, combine aux controles et aux effets fixes, explique pres de 70 pour cent de la variance intra-pays de la productivite IA - un pouvoir explicatif remarquable pour un indice composite inedit.",
        "La variable de controle a l'export est significative en MCO groupes (beta = 0,40, p < 0,05) mais perd sa significativite en EF, suggerant que son effet est absorbe par les effets fixes pays - coherent avec des controles affectant principalement la Chine, dont l'effet fixe capture l'essentiel de la variation.",
    ]),
    ("B.5.2 Test de Hausman", [
        "Le test de Hausman compare les estimateurs EF et EA. Sous H0, les effets individuels ne sont pas correles avec les regresseurs, rendant les EA efficients. Nous obtenons chi2 = 13,91 (p = 0,001), rejetant H0 au seuil de 1 pour cent. Le modele a effets fixes est donc prefere, ce qui est theoriquement coherent : la competitivite IA des pays est correlee avec des facteurs non observes (qualite institutionnelle, culture d'innovation) qui sont probablement correles avec les regresseurs.",
    ]),
    ("B.5.3 Tests de robustesse", [
        "Decomposition des composantes du CACI. Nous estimons un modele EF avec composantes decomposees : ln(F), ln(E^-1), ln(L), ln(R), plus controles. Le coefficient du compute brut (ln F) est de 0,301 (p < 0,01), dominant les autres composantes - ce qui valide l'attribution du poids le plus eleve (0,40) au compute dans la formule Power Mode. L'energie est significative et du signe attendu (beta = 0,12, p < 0,05). Le coefficient de main-d'oeuvre est positif mais non significatif (beta = 0,08, p = 0,22), probablement en raison de l'erreur de mesure dans notre proxy.",
        "Sensibilite aux ponderations. Trois variantes alternatives sont evaluees : (i) ponderations egales (alpha = beta = gamma = 1/4, formule symetrique), (ii) variante Energy-First (E ponderee a 0,40, F a 0,25, L a 0,20, R a 0,15), (iii) variante Talent-First (L a 0,35, F a 0,30, R a 0,15, E a 0,20). Le coefficient beta1 du CACI reste positif et significatif (p < 0,05) dans toutes les variantes, mais sa magnitude varie de 0,18 (Talent-First) a 0,32 (Energy-First). La variante Power Mode retenue (F dominant a 0,40, E denominateur a 0,25) maximise l'ajustement empirique (R2 within 0,692) et la coherence avec la litterature sur le compute comme facteur de production primaire.",
        "Exclusion des valeurs aberrantes. L'exclusion des Etats-Unis (potentielle valeur aberrante en compute) reduit le coefficient EF a environ 0,18 mais maintient la significativite (p < 0,05). L'exclusion de la Chine (soumise aux controles a l'export) ne modifie pas substantiellement les resultats. La robustesse aux exclusions individuelles confirme que les resultats ne dependent d'aucun pays unique.",
    ]),
    ("B.6 L'ecart de compute US-UE : structure et determinants", []),
    ("B.6.1 Quantification de l'ecart", [
        "Le cadre CACI permet une quantification precise des avantages de compute entre pays. Sur le snapshot avril 2026 du tableau de bord public, le ratio brut compute installe operationnel US/UE(13) atteint 17,6:1, traduit par la formule geometrique Power Mode en un ratio US/UE de 3,46:1. Le ratio moyen US/Allemagne, France, Pays-Bas, Suede s'etablit autour de 4-6:1 (Power Mode), avec une heterogeneite intra-UE marquee : France 3,95:1 (proche de la moyenne UE grace au nucleaire bas-cout), Allemagne 18,5:1 (cout energie eleve, sortie nucleaire), UK 14,3:1 (cout energie le plus eleve d'Europe).",
        "Ce ratio est coherent avec des estimations independantes : Hawkins et al. (2025) documentent un ecart brut de compute de l'ordre de 15-20:1 ; le Federal Reserve Board (2025) estime que les gains de productivite de l'IA aux Etats-Unis sont significativement superieurs a ceux observes dans les economies comparables de l'UE. La compression observee entre le ratio brut (17,6:1) et le ratio CACI (3,46:1) traduit l'effet de la formule geometrique : le compute reste dominant mais ses excursions extremes sont attenuees par le poids du capital humain et de l'acces reglementaire.",
    ]),
    ("B.6.2 Protectionnisme a trois niveaux", [
        "Nous identifions trois couches de protectionnisme technologique americain, chacune renforcant les autres.",
        "Niveau 1 : Deni d'acces. Les controles a l'export (octobre 2022, AI Diffusion Rule, Entity List) restreignent l'acces aux GPU de pointe pour les adversaires (Chine, Russie, Iran). Cela cree un plafond absolu de compute pour les pays cibles.",
        "Niveau 2 : Tarification. Les tarifs Section 232 (25 pct sur les semi-conducteurs IA, janvier 2026) imposent un surcout a tous les importateurs. Bien que ciblant actuellement les reexportations chinoises, le mecanisme est en place pour une extension a toutes les origines - signalee pour juillet 2026.",
        "Niveau 3 : Attraction gravitationnelle. Les exemptions domestiques des tarifs, le cout energetique 1,59x inferieur aux Etats-Unis (USA 85 USD/MWh PPA-ajuste contre UE 135 USD/MWh, France 115 USD/MWh), et l'agglomeration de talents creent un effet de gravite : capitaux, chercheurs et entreprises convergent vers les Etats-Unis, renforcant leur avantage en compute par des forces de marche plutot que par decret.",
        "Un quatrieme niveau potentiel se profile a l'horizon 2028 : les Cloud Sovereignty Mandates, qui transformeraient les hyperscalers US operant offshore en intermediaires conditionnels du compute mondial. La decomposition Phys/Sov (section 3.4) operationnalise ce risque pour les juridictions ou les clusters localises sont majoritairement detenus par des operateurs US-side (cas EAU 99,6 pct).",
        "L'enseignement critique est que les niveaux 2 et 3 affectent les allies, pas seulement les adversaires. Les entreprises europeennes font face au meme surcout tarifaire et a la meme attraction gravitationnelle, bien qu'elles ne soient pas les cibles visees. La consequence structurelle est un elargissement de l'ecart de competitivite qui ne peut etre comble par les seuls mecanismes de politique industrielle conventionnels.",
    ]),
    ("B.6.3 Trajectoires CACI", [
        "Les trajectoires CACI 2020-2024 revelent deux dynamiques critiques. Premierement, le CACI americain accelere fortement apres 2022, refletant l'explosion de l'investissement en GPU (le capex des cinq principales entreprises technologiques americaines a atteint 660-690 milliards USD en 2026 selon les projections AIE et Euronews). Deuxiemement, le CACI chinois stagne malgre des investissements domestiques massifs (125 milliards USD en infrastructure IA en 2025, 70 milliards USD supplementaires programmes pour 2026), confirmant l'efficacite des controles a l'export pour plafonner la capacite de compute frontier - meme si la Chine compense partiellement via des solutions alternatives (Huawei Ascend, chiplets, capacite reelle revendiquee 246-300 EFLOP/s vs 0,5 pct apparent dans les donnees Epoch AI consolidees).",
    ]),
    ("B.7 Scenarios prospectifs 2026-2030", [
        "En nous appuyant sur la methodologie de scenarios de Schwartz (1991), nous construisons quatre scenarios organises selon deux axes : (i) intensite du protectionnisme IA americain (modere vs agressif) et (ii) capacite de reponse europeenne (passive vs proactive). Le tableau B.3 presente la matrice scenarielle.",
        "Scenario A (Derive controlee) est la ligne de base la plus probable (probabilite estimee : 40-45 pct). L'ecart CACI reste a 3,46:1 (mode Power) et le ratio brut a 17,6:1. Les entreprises europeennes accroissent leur dependance a l'infrastructure cloud americaine. Investissements europeens incrementaux mais insuffisants dans les Usines IA. La France deploie ses sites nucleaires EDF mais sans coordination UE.",
        "Scenario B (Vassalisation numerique) represente le pire cas pour la souverainete europeenne (probabilite : 20-25 pct). Declenche par l'extension de la Section 232 a toutes les importations de semi-conducteurs plus application des Cloud Sovereignty Mandates aux entreprises de l'UE (activation 2028). Les charges de travail IA de l'UE deviennent structurellement dependantes des plateformes americaines. Le CACI ratio passe a 6-8:1 (Power Mode) et le ratio brut depasse 25:1.",
        "Scenario C (Guerre froide technologique) implique une fragmentation maximale (probabilite : 10-15 pct). Certains Etats de l'UE explorent des alternatives chinoises (Huawei Ascend, cloud ByteDance). L'ecosysteme IA mondial se fragmente en blocs concurrents - dommageable pour tous mais particulierement pour l'Europe, coincee entre les deux.",
        "Scenario D (Rattrapage strategique) est le plus favorable pour l'Europe (probabilite : 20-25 pct). Necessite que l'UE deploie des Zones Speciales de Compute, securise 250 plus MW de capacite nucleaire-IA d'ici 2027, investisse 20 plus milliards EUR dans des Gigafactories IA, et utilise l'AI Act comme avantage competitif. Le CACI ratio se reduit a 2,0-2,5:1 d'ici 2030 et le ratio brut a 8-10:1.",
    ]),
    ("B.8 Implications politiques", [
        "Notre analyse produit cinq recommandations prioritaires pour les decideurs europeens.",
        "Premierement, etablir des Zones Speciales de Compute. Des zones geographiques designees avec des tarifs energetiques derogatoires (50-60 USD/MWh via PPA nucleaires, soit la parite avec le baseline US 85 USD/MWh), des procedures d'autorisation accelerees (6-12 mois contre 3-5 ans), des volumes de GPU garantis via des contrats-cadres UE, et une souverainete reglementaire (conformite AI Act integree). L'objectif est d'atteindre la parite des couts compute avec les Etats-Unis sur les sites designes d'ici 2028.",
        "Deuxiemement, integrer la planification energetique nucleaire-IA. La France detient un avantage unique avec 63 GW de capacite nucleaire existante. EDF a identifie 2 GW dediables aux centres de donnees via son initiative Nuclear for AI (250 MW d'ici fin 2026). Les 6 reacteurs EPR 2 programmes pourraient ajouter 10 GW d'ici 2035-2038, dont 2-3 GW explicitement orientes IA. Cela necessite un engagement immediat a integrer la demande IA dans la planification de capacite nucleaire.",
        "Troisiemement, constituer des reserves strategiques de GPU. Sur le modele des reserves strategiques de petrole, ce mecanisme securiserait des approvisionnements de 18-36 mois en puces IA avancees via des contrats-cadres UE avec Nvidia, AMD, et a terme Intel Foundry. L'objectif est de decoupler l'approvisionnement europeen en compute de la politique commerciale americaine.",
        "Quatriemement, transformer l'AI Act en levier competitif. Plutot que de considerer l'AI Act uniquement comme un cout de conformite, l'UE devrait l'utiliser offensivement : conditionner l'acces au marche UE a des engagements de localisation du compute, negocier des accords de reconnaissance mutuelle avec le Japon et la Coree du Sud, et certifier les modeles IA europeens (Mistral, Aleph Alpha) comme conformes AI Act sur les marches mondiaux.",
        "Cinquiemement, augmenter F_sov sur la couche operationnelle des charges cloud. La decomposition Phys/Sov (section 3.4) revele que la vulnerabilite europeenne ne se situe pas sur l'infrastructure deployee dans les juridictions UE (UE 99,2 pct souveraine sur F installe) mais sur la couche operationnelle des charges cloud - les workloads des entreprises europeennes etant majoritairement hebergees sur AWS, Microsoft Azure et Google Cloud (70 a 80 pct du cloud public europeen). L'objectif strategique est d'atteindre 30 a 40 pct des workloads sous juridiction UE d'ici 2029, via la combinaison Mistral Compute, Cloud souverain SOV-3 et AI Gigafactories.",
    ]),
    ("B.9 Conclusion", [
        "Cet article a introduit le Compute-Adjusted Competitiveness Index (CACI) comme premier cadre quantitatif pour mesurer la competitivite nationale en IA a travers le prisme de l'infrastructure de calcul. Notre validation econometrique demontre quatre resultats cles.",
        "Premierement, le CACI Power Mode est un predicteur statistiquement significatif et robuste de la productivite sectorielle IA, avec un coefficient positif stable a travers les specifications (beta = 0,17 a 0,50, p < 0,01). Deuxiemement, le compute brut (F) est la composante dominante (coefficient decompose 0,301, p < 0,01), confirmant notre these centrale selon laquelle l'infrastructure de calcul est le facteur critique de la competitivite IA et justifiant l'attribution du poids le plus eleve (0,40) dans la formule Power Mode. Troisiemement, le ratio CACI US/UE de 3,46:1 (Power Mode) pour un ratio brut de 17,6:1 quantifie un ecart structurel que les mecanismes conventionnels de politique industrielle ne peuvent combler a eux seuls. Quatriemement, l'extension Phys/Sov revele une heterogeneite massive entre juridictions (UE 99,2 pct souveraine sur F installe vs EAU 0,4 pct souverain) qui modifie la lecture des asymetries traditionnelles et oriente strategiquement l'action vers la couche operationnelle des charges cloud.",
        "La fenetre d'action politique est etroite. L'action europeenne dans la periode 2026-2028 determinera si le continent devient architecte de sa position dans l'ordre technologique mondial ou spectateur. Le cadre CACI fournit l'outil de mesure ; les scenarios cartographient les trajectoires possibles ; les recommandations politiques identifient les leviers concrets. Ce qui reste requis est la volonte politique de les actionner.",
        "Nous recommandons quatre pistes de recherche future. Premierement, elargir le panel a 25-30 pays et 10 ans pour augmenter la puissance statistique. Deuxiemement, developper un CACI au niveau de l'entreprise a l'aide de microdonnees sur les depenses cloud et l'approvisionnement en GPU. Troisiemement, integrer le CACI dans un modele d'equilibre general calculable (CGE) pour modeliser les boucles de retroaction entre politique commerciale, investissement en compute et dynamiques de productivite. Quatriemement, constituer un panel longitudinal Phys/Sov (champ Owner d'Epoch AI) pour tester si les variations temporelles de F_sov predisent des variations differenciees de productivite IA.",
    ]),
]


TABLES = [
    ("Tableau B.1. Variables du panel et sources.",
     "Source : compilation de l'auteur. La variable CACI est calculee selon la formule Power Mode geometrique.",
     [
         ["Variable", "Definition", "Unite", "Source"],
         ["F(r,t)", "FLOPs IA installes accessibles", "PetaFLOPs (H100-eq)", "Epoch AI, Hawkins et al. (2025), CFG Europe"],
         ["E(r,t)", "Cout energie data centers (PPA-ajuste)", "USD/MWh", "Eurostat, EIA, AIE (avril 2025)"],
         ["L(r,t)", "Workforce IA (proxy STEM + certifications)", "Milliers", "OCDE, LinkedIn Economic Graph"],
         ["R(r,t)", "Acces reglementaire (Tier 1/2/3 BIS)", "Indice 0-1", "BIS, AI Diffusion Rule, Section 232"],
         ["GDP(r,t)", "Produit interieur brut", "Trillions USD", "Banque mondiale, FMI"],
         ["PROD(r,t)", "Gain productivite secteurs IA-intensifs", "pct gain annuel", "McKinsey (2024-26), FMI WP/25/067, Fed Board (2025)"],
         ["CACI(r,t)", "F^0,40 x L^0,20 x R^0,15 / E^0,25", "Indice (sans unite)", "Calcul auteur, formule consolidee"],
     ]),
    ("Tableau B.2. Resultats des regressions de panel.",
     "Erreurs-types robustes (regroupees par pays) entre parentheses. *** p < 0,01, ** p < 0,05, * p < 0,10.",
     [
         ["Variable", "M1 : MCO groupes", "M2 : Effets Fixes", "M3 : Effets Aleatoires"],
         ["ln(CACI)", "0,173*** (0,038)", "0,251*** (0,075)", "0,504*** (0,020)"],
         ["ln(GDP/cap)", "0,071 (0,130)", "absorbe", "absorbe"],
         ["Regulation", "0,058 (0,203)", "0,002 (0,019)", "-0,010 (0,021)"],
         ["Export control", "0,401** (0,201)", "0,026 (0,051)", "0,060 (0,043)"],
         ["Constante", "4,127*** (1,439)", "absorbe", "9,963*** (0,233)"],
         ["N", "60", "60", "60"],
         ["R2", "0,227", "0,692 (within)", "0,920"],
         ["Effets fixes pays", "Non", "Oui", "Non (aleatoires)"],
         ["Effets fixes temps", "Non", "Oui", "Non"],
         ["Hausman chi2 (p-val)", "N/A", "13,91 (0,001)", "N/A"],
     ]),
    ("Tableau B.3. Matrice de scenarios prospectifs 2026-2030.",
     "Source : construction de l'auteur. Probabilites estimees a partir du diagnostic empirique avril 2026.",
     [
         ["Scenario", "Probabilite", "Ratio brut US/UE", "Ratio CACI US/UE", "Description"],
         ["A : Derive controlee", "40-45 pct", "17-18:1", "3,46:1 (baseline)", "Statu quo ; dependance cloud croissante"],
         ["B : Vassalisation numerique", "20-25 pct", ">25:1", "6-8:1", "Section 232 etendue + CSM 2028 actives"],
         ["C : Guerre froide tech", "10-15 pct", "Fragmente", "Fragmente", "Bifurcation US-Chine ; UE coincee"],
         ["D : Rattrapage strategique", "20-25 pct", "8-10:1", "2,0-2,5:1", "Zones Speciales Compute ; nucleaire-IA ; Mistral"],
     ]),
    ("Tableau B.4. Decomposition Phys/Sov par region (snapshot avril 2026).",
     "Source : calcul de l'auteur a partir du champ Owner d'Epoch AI. F_phys en millions d'equivalents H100. CACI Phys et Sov calcules selon la formule Power Mode.",
     [
         ["Region", "F_phys", "F_dom", "F_sov (pct)", "CACI Phys", "CACI Sov"],
         ["USA", "39,6", "39,6", "100", "100", "100"],
         ["Chine", "0,4", "0,4", "100", "15,7", "15,7"],
         ["UE(13)", "2,6", "2,6", "99,2", "28,9", "28,8"],
         ["France", "2,4", "2,4", "100", "25,3", "25,3"],
         ["Royaume-Uni", "1,2", "1,1", "91,7", "7,0", "6,4"],
         ["EAU", "22,9", "0,087", "0,4", "55,7", "6,0"],
         ["Inde", "1,8", "1,7", "94,4", "22,2", "21,0"],
     ]),
]


NOTES = [
    "Bresnahan, T.F. & Trajtenberg, M. (1995). General purpose technologies : Engines of growth ?, Journal of Econometrics, 65(1), 83-108.",
    "Brynjolfsson, E., Rock, D. & Syverson, C. (2019). Artificial intelligence and the modern productivity paradox, in The Economics of Artificial Intelligence, University of Chicago Press, 23-60.",
    "CFG Europe (2025), 'Special Compute Zones : Europe's Recipe for AI Infrastructure Leadership'.",
    "Deloitte (fevrier 2026), '2026 Semiconductor Industry Outlook'.",
    "Epoch AI (2025), 'Key trends and figures in machine learning', epochai.org. Snapshot avril 2026 publie sur https://mo0ogly.github.io/America-First-IA/dashboard/",
    "Farrell, H. & Newman, A. (2019), 'Weaponized interdependence : How global economic networks shape state coercion', International Security, 44(1), 42-79.",
    "Federal Reserve Board (2025), 'AI Adoption and Productivity in the US Economy', Finance and Economics Discussion Series.",
    "Hawkins, W. et al. (2025), 'Installed AI compute capacity by country : A first estimation', Working Paper, Oxford Internet Institute.",
    "AIE - Agence internationale de l'energie (avril 2025), 'Energy and AI', Rapport special AIE, Paris. Differentiel cout energie US/UE 1,59x apres ajustement PPA sur snapshot avril 2026.",
    "FMI (2025), 'AI and Productivity : Early Evidence from Firm-Level Data', IMF Working Paper WP/25/067.",
    "McKinsey & Company (2024-2026), 'Accelerating Europe's AI Adoption : The Role of Sovereign AI', McKinsey Digital.",
    "Mugge, D. (2024), 'The return of geo-economics : Technology competition and the fragmentation of global markets', Review of International Political Economy, 31(2), 345-367.",
    "OCDE (2025), 'Digital Economy Outlook 2025', Editions OCDE, Paris.",
    "Schoemaker, P.J.H. (1995), 'Scenario planning : A tool for strategic thinking', Sloan Management Review, 36(2), 25-40.",
    "Schwartz, P. (1991), 'The Art of the Long View', Currency Doubleday, New York.",
    "SIA - Semiconductor Industry Association / WSTS (2025-2026), 'Statistiques et previsions mondiales de ventes de semi-conducteurs'.",
    "Synergy Research Group (2025), 'Cloud infrastructure market share by provider and region'. 70 a 80 pct du cloud public europeen sous controle des hyperscalers US.",
    "White House / BIS (2025-2026), 'AI Diffusion Rule', 'America's AI Action Plan', 'Section 232 Proclamation 11002'.",
    "Note de disponibilite des donnees et du code : le jeu de donnees de panel calibre (CSV), les scripts Python pour toutes les estimations econometriques et figures, et un fichier requirements.txt pour la reproductibilite sont fournis dans les annexes operationnelles A (annexe econometrique CACI).",
]


def build(out_dir: Path) -> Path:
    """Build the FR Annexe B Working Paper CACI .docx."""
    log.info("Building Annexe B Working Paper CACI [FR] -> Annexe_B_Working_Paper_CACI_FR.docx")
    doc = init_document()
    add_cover(doc, chapter_label=CHAPTER_LABEL,
              chapter_subtitle=CHAPTER_TITLE)
    add_chapter_header(doc, label=CHAPTER_LABEL,
                       title=CHAPTER_TITLE, intro=CHAPTER_INTRO)
    for title, paragraphs in SECTIONS:
        render_section(doc, title, paragraphs)
    for caption, source, rows in TABLES:
        render_table(doc, caption, source, rows)
    render_notes(doc, NOTES)
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Annexe B Working Paper CACI")

    out = out_dir / "Annexe_B_Working_Paper_CACI_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
