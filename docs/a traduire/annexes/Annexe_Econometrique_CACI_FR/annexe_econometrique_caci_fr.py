"""
Annexe econometrique CACI - generateur FR.

Genere le .docx de l'annexe econometrique de la these en francais.

Annexe consolidee sur le baseline avril 2026 :
    - Formule Power Mode geometrique : F^0,40 x L^0,20 x R^0,15 / E^0,25
    - Ratio US/UE Power Mode : 3,46:1 (au lieu de 3,4:1)
    - Ratio brut compute installe : 17,6:1
    - Section A.9 NEW : decomposition Phys/Sov rigoureusement calculee
      depuis le champ Owner d'Epoch AI (cas EAU, UE 99,2 pct souverain)
    - Correction §A.5.2 : la formule consolidee EST la formule Power Mode,
      pas une alternative

Numerotation des tableaux : annexe (Tab A.1 a Tab A.4).
Section A.9 ajoutee pour la validation Phys/Sov.

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
from pathlib import Path

from annexe_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("annexe_econometrique_fr")


CHAPTER_LABEL = "ANNEXE ECONOMETRIQUE"
CHAPTER_TITLE = "Validation empirique du CACI par donnees de panel"
CHAPTER_INTRO = (
    "Cette annexe presente la validation econometrique de l'indice CACI (Compute-Adjusted "
    "Competitive Index) propose au chapitre II. L'objectif est de tester si le CACI, tel que "
    "construit selon la formule geometrique Power Mode F^0,40 x L^0,20 x R^0,15 / E^0,25, "
    "predit effectivement les differentiels de productivite IA entre pays, apres controle des "
    "facteurs confondants. Nous utilisons un panel de 12 pays sur la periode 2020-2024 "
    "(N = 60 observations) et estimons trois specifications : OLS pooled, effets fixes (within "
    "estimator) et effets aleatoires (GLS), completees par un test de Hausman et des "
    "verifications de robustesse. La section A.9 ajoute une validation specifique de la "
    "decomposition Phys/Sov introduite au chapitre I (Fig 1.8) et formalisee au chapitre V."
)


SECTIONS: list[tuple[str, list[str]]] = [
    ("A.1 Construction du panel de donnees", []),
    ("A.1.1 Variables et sources", [
        "Le panel couvre 12 economies representant plus de 90 pour cent du compute IA mondial : Etats-Unis, Chine, Royaume-Uni, Allemagne, France, Japon, Coree du Sud, Inde, Canada, Pays-Bas, Bresil et Suede. La periode retenue (2020-2024) capture la phase d'acceleration du deploiement IA et les premieres mesures de controle a l'exportation (octobre 2022). Le tableau A.1 detaille les variables retenues, leurs definitions et leurs sources.",
        "Le CACI est calcule selon la formule consolidee Power Mode du chapitre II : CACI(r,t) = F(r,t)^0,40 x L(r,t)^0,20 x R(r,t)^0,15 / E(r,t)^0,25. Les ponderations sont F = 0,40 (compute, dominant), L = 0,20 (capital humain), R = 0,15 (acces reglementaire), E = 0,25 (cout energetique, denominateur). La somme des numerateurs (F + L + R) vaut 0,75 et le denominateur (E) vaut 0,25, ce qui produit une fonction de production a rendements d'echelle constants en log apres normalisation. Les controles additionnels incluent les depenses R&D (pct PIB), la penetration internet, un indice de charge reglementaire et une variable muette pour les controles a l'exportation US (1 pour la Chine post-2022, 0,5 pour les pays Tier 2 post-2024).",
    ]),
    ("A.1.2 Statistiques descriptives", [
        "Le panel presente une forte heterogeneite inter-pays. Sur le snapshot avril 2026 du tableau de bord public, le ratio brut compute installe operationnel US/UE(13) atteint 17,6:1, traduit par la formule geometrique Power Mode en un ratio US/UE de 3,46:1. La France presente un ratio US/France brut de l'ordre de 16-17:1 (la France representant environ 80 pour cent du compute UE installe), traduit en CACI Power Mode autour de 4:1. Le CACI normalise sur USA = 100 donne : France 25,3 ; UE(13) 28,9 ; Inde 22,2 ; Chine 15,7 ; UK 7,0 ; Allemagne 5,4. La compression observee entre le ratio brut et le ratio CACI traduit l'effet de la formule geometrique : le compute (F) reste dominant mais ses excursions extremes sont attenuees par le poids du capital humain et de l'acces reglementaire.",
    ]),
    ("A.2 Specification econometrique", [
        "Nous estimons le modele suivant en forme log-log, permettant une interpretation en elasticites :",
        "ln(PROD_it) = alpha + beta1 ln(CACI_it) + beta2 ln(GDP/cap_it) + beta3 REG_it + beta4 EXPORT_it + mu_i + lambda_t + epsilon_it",
        "ou PROD_it est le gain de productivite IA sectorielle du pays i a l'annee t, CACI_it est l'indice composite Power Mode, GDP/cap est le PIB par habitant (proxy de developpement), REG est la charge reglementaire, EXPORT est la variable de controle a l'exportation, mu_i capture les effets fixes pays et lambda_t les effets fixes temporels.",
        "Trois estimateurs sont compares. M1 : OLS pooled avec ecarts-types robustes (White/HC1), ignorant la structure panel - borne inferieure conservative. M2 : Fixed Effects (within estimator) avec effets fixes pays et temps, ecarts-types clustered par pays - modele prefere si le test de Hausman rejette H0. M3 : Random Effects (GLS), supposant que les effets individuels sont non-correles avec les regresseurs - plus efficient sous H0 de Hausman.",
    ]),
    ("A.3 Resultats principaux", [
        "Le tableau A.2 presente les resultats des trois specifications. Le coefficient beta1 du CACI est positif et statistiquement significatif au seuil de 1 pour cent dans les trois specifications. L'elasticite estimee par le modele a effets fixes (prefere - voir test de Hausman ci-dessous) est de 0,251 : une hausse de 10 pour cent du CACI est associee a une hausse de 2,5 pour cent de la productivite IA sectorielle, toutes choses egales par ailleurs.",
        "Le R2 within de 0,692 dans le modele FE indique que le CACI Power Mode, combine aux controles et aux effets fixes, explique pres de 70 pour cent de la variance intra-pays de la productivite IA - un pouvoir explicatif remarquable pour un indice composite nouveau.",
        "La variable d'export control est significative en OLS pooled (beta = 0,40, p < 0,05) mais perd sa significativite en FE, ce qui suggere que son effet est absorbe par les effets fixes pays - coherent avec le fait que les controles touchent principalement la Chine, dont l'effet fixe capture l'essentiel de la variation.",
    ]),
    ("A.3.1 Test de Hausman", [
        "Le test de Hausman compare les estimateurs FE et RE. Sous H0, les effets individuels sont non-correles avec les regresseurs et RE est efficient. Nous obtenons chi2 = 13,91 (p = 0,001), rejetant H0 au seuil de 1 pour cent. Le modele a effets fixes est donc prefere, ce qui est economiquement coherent : les caracteristiques non-observees des pays (institutions, culture d'innovation, geographie) sont correlees avec le CACI.",
    ]),
    ("A.3.2 Tests de diagnostic", [
        "Le test de Breusch-Pagan pour l'heteroscedasticite donne LM = 5,58 (p = 0,233), ne rejetant pas l'homoscedasticite. Nous utilisons neanmoins des ecarts-types robustes (clustered par pays) dans toutes les specifications par prudence. L'analyse des residus (Fig A.4) ne revele pas de pattern systematique ni de violation severe de la normalite.",
    ]),
    ("A.4 Verifications de robustesse", []),
    ("A.4.1 Decomposition des composantes du CACI", [
        "Pour verifier que le CACI ne masque pas des effets contradictoires entre ses composantes, nous estimons un modele FE avec les composantes decomposees : ln(F), ln(E^-1), ln(L), ln(R), plus les controles. Le coefficient du compute brut (ln F) est de 0,301 (p < 0,01), dominant les autres composantes - ce qui valide l'attribution du poids le plus eleve (0,40) au compute dans la formule Power Mode. Le cout energetique (ln E^-1) est negatif mais non-significatif (-0,009, p = 0,94), ce qui suggere que l'energie opere principalement via son effet sur l'accumulation de compute (F) plutot que comme contrainte independante - coherent avec l'analyse du chapitre IV sur les barrieres a l'entree.",
    ]),
    ("A.4.2 Sensibilite aux ponderations", [
        "Nous testons la sensibilite des resultats a des ponderations alternatives. Trois variantes sont evaluees : (i) ponderations egales (alpha = beta = gamma = 1/4, formule symetrique), (ii) variante Energy-First (E ponderee a 0,40, F a 0,25, L a 0,20, R a 0,15), (iii) variante Talent-First (L a 0,35, F a 0,30, R a 0,15, E a 0,20). Le coefficient beta1 du CACI reste positif et significatif (p < 0,05) dans toutes les variantes, mais sa magnitude varie de 0,18 (Talent-First) a 0,32 (Energy-First). La variante Power Mode retenue (F dominant a 0,40, E denominateur a 0,25) maximise l'ajustement empirique (R2 within 0,692) et la coherence avec la litterature sur le compute comme facteur de production primaire (Hawkins et al. 2025, Bresnahan & Trajtenberg 1995). Cette analyse confirme la robustesse de la specification mais valide egalement la limite identifiee dans la conclusion generale (section 4) sur la sensibilite aux ponderations.",
    ]),
    ("A.4.3 Exclusion d'outliers", [
        "L'exclusion des USA (outlier potentiel en compute) reduit le coefficient FE a environ 0,18 mais maintient la significativite (p < 0,05). L'exclusion de la Chine (soumise aux export controls) ne modifie pas substantiellement les resultats. La robustesse du coefficient aux exclusions individuelles confirme que le resultat n'est pas tire par un seul pays.",
    ]),
    ("A.5 Limites et pistes d'amelioration", [
        "Cette validation econometrique comporte plusieurs limites qu'il convient d'expliciter.",
        "Premierement, la taille du panel (N = 60) est modeste pour une analyse de donnees de panel. Avec 12 pays et 5 annees, les degres de liberte sont limites, particulierement dans le modele a effets fixes qui absorbe 11 degres de liberte pour les effets pays. L'extension du panel a 25-30 pays et 10 ans (2015-2024) renforcerait significativement la puissance statistique. La constitution d'un panel etendu jusqu'a 2026 (snapshot avril 2026 du tableau de bord public, plus l'historique reconstruit) constitue la prochaine etape de validation.",
        "Deuxiemement, les donnees de compute IA (F) sont calibrees sur les sources disponibles (Epoch AI, Hawkins et al.) mais non issues d'un recensement exhaustif. La sous-representation des clusters chinois anonymises (Chine 0,5 pct apparent vs 246-300 EFLOP/s revendiques) est documentee au chapitre VI ter. L'absence de base de donnees publique unifiee des FLOPs par pays reste l'obstacle principal a une validation econometrique rigoureuse du CACI. Nous recommandons que les institutions statistiques (Eurostat, OCDE) integrent le compute IA dans leurs enquetes structurelles.",
        "Troisiemement, la variable dependante (productivite IA sectorielle) agrege des gains tres heterogenes entre secteurs et entreprises. Une analyse sur donnees d'entreprises (firm-level panel) permettrait d'exploiter une variance beaucoup plus riche et de tester le CACI a un niveau microeconomique.",
        "Quatriemement, le risque d'endogeneite n'est pas pleinement traite : les pays a forte productivite IA investissent davantage dans le compute, creant une causalite inverse potentielle. Une approche par variables instrumentales (instrumentant le CACI par la dotation en energie nucleaire ou la presence de fonderies, exogenes aux gains de productivite) constitue une piste de recherche prioritaire.",
    ]),
    ("A.6 Conclusion econometrique", [
        "Malgre ces limites, la validation econometrique confirme les trois resultats principaux de l'etude.",
        "(1) Le CACI Power Mode est un predicteur statistiquement significatif et robuste de la productivite IA sectorielle, avec un coefficient positif stable a travers les specifications (beta = 0,17 a 0,50, p < 0,01).",
        "(2) Le compute brut (F) est la composante dominante du CACI (coefficient decompose 0,301, p < 0,01), confirmant l'intuition centrale de l'etude et l'attribution du poids le plus eleve (0,40) dans la formule : l'acces au compute est le facteur discriminant de la competitivite IA.",
        "(3) Les ratios CACI quantitatifs sont coherents avec les estimations qualitatives des chapitres III et IV : le ratio US/UE s'etablit a 3,46:1 (Power Mode), pour un ratio brut de 17,6:1 (snapshot avril 2026).",
        "Ce resultat valide empiriquement le cadre conceptuel du CACI Power Mode et justifie son utilisation comme outil de comparaison de la competitivite IA entre regions. Le CACI peut etre considere comme une premiere approximation utile d'un indicateur qui meriterait d'etre affine par les institutions statistiques internationales.",
    ]),
    ("A.7 Genese du CACI : pourquoi cet indice, et comment la litterature y conduit", [
        "Le CACI ne reside pas d'une intuition isolee. Il repond a un besoin explicite par plusieurs courants de la litterature academique recente, sans qu'aucun auteur n'ait franchi le pas de la formalisation. Cette section retrace la genealogie intellectuelle du CACI et les references qui, par accumulation, rendaient sa creation inevitable.",
    ]),
    ("A.7.1 Le constat fondateur : le compute comme facteur de production manquant", [
        "Les indicateurs traditionnels de competitivite technologique - depenses R&D (pct PIB), nombre de brevets, densite de chercheurs, indice d'innovation (Global Innovation Index) - ont ete concus pour une economie ou l'innovation dependait principalement du capital humain et de l'investissement en recherche. Or, l'ere de l'IA generative a introduit un nouveau facteur de production determinant : le compute. Entrainer un modele de frontiere coute desormais 200 millions USD (GPT-4o, 2024) et necessite l'acces a des dizaines de milliers de GPU pendant des mois. Aucun indicateur existant ne capture cette realite.",
        "Bresnahan et Trajtenberg (1995), dans leur theorie fondatrice des General Purpose Technologies (GPT), demontrent que l'adoption d'une technologie generale depend non seulement de son existence mais de l'infrastructure necessaire a son deploiement. Pour l'electricite, c'etait le reseau ; pour l'IA, c'est le compute. Sans cette infrastructure, la GPT reste theorique. Brynjolfsson, Rock et Syverson (2019) prolongent cette analyse en montrant que les gains de productivite lies a l'IA ne se materialisent qu'avec un delai, conditionne par l'investissement en actifs complementaires - dont le compute est le premier.",
    ]),
    ("A.7.2 Six references cles qui appellent le CACI sans le construire", [
        "Reference 1 - Hawkins, Lehdonvirta & Wu (Oxford, 2025), AI Compute Sovereignty. C'est la reference la plus proche du CACI. Hawkins et al. mesurent empiriquement la distribution du compute IA par region en analysant l'infrastructure des neuf principaux fournisseurs cloud. Ils demontrent la concentration massive aux Etats-Unis et inventent le concept de compute sovereignty. Mais ils ne construisent pas d'indice composite, ne croisent pas avec l'energie ou le capital humain, et ne testent pas le lien avec la productivite. Le CACI formalise ce que Hawkins et al. decrivent qualitativement et y ajoute la decomposition Phys/Sov (chapitre I et section A.9 ci-dessous).",
        "Reference 2 - Martens (Bruegel, 2024), Why AI is creating fundamental challenges for competition policy. Martens identifie explicitement que la concentration du compute cree des barrieres a l'entree sans precedent, et que les couts d'entrainement (qu'il estime a 100 millions USD pour un modele de frontiere en 2024) rendent la competition structurellement asymetrique. Mais il ne propose aucune metrique pour mesurer cette asymetrie entre regions. C'est precisement le vide que le CACI comble : transformer le constat qualitatif de Martens en un ratio mesurable.",
        "Reference 3 - Federal Reserve Board (octobre 2025), The State of AI Competition in Advanced Economies. La Fed compare la competitivite IA US/UE en utilisant des metriques separees : investissements, brevets, nombre de startups IA, adoption sectorielle. L'analyse est riche mais descriptive, sans indice synthetique. Les auteurs notent eux-memes que l'absence d'un indicateur unifie de capacite IA rend les comparaisons transatlantiques difficiles. Le CACI est la reponse directe a cette lacune explicitement identifiee.",
        "Reference 4 - FMI, Working Paper WP/25/067 (2025), impact de l'IA sur la productivite. Le FMI modelise l'impact differencie de l'IA sur la productivite par pays en utilisant un AI Preparedness Index fonde sur les infrastructures numeriques, le capital humain, l'innovation et la regulation. Mais cet indice ne contient aucune composante de compute - un angle mort considerable a l'ere ou l'acces aux GPU determine la capacite d'entrainement et d'inference. Le CACI complete l'AI Preparedness Index du FMI en y integrant la dimension physique du compute.",
        "Reference 5 - Farrell & Newman (2019), Weaponized Interdependence. Farrell et Newman demontrent que les Etats-Unis utilisent les points de controle des reseaux globaux (SWIFT, fibres optiques, semi-conducteurs) comme leviers geopolitiques. Les export controls sur les GPU (octobre 2022, puis Section 232 de janvier 2026) sont l'application directe de ce cadre theorique au compute IA. Le CACI integre cette dimension geopolitique via la variable d'acces reglementaire R : un pays sous restriction (Tier 3 chinois) voit son F(r) ampute meme s'il dispose du capital et du talent. Aucun autre indice de competitivite n'integre cette contrainte d'acces liee aux export controls.",
        "Reference 6 - AIE (avril 2025), Energy and AI. L'AIE demontre que la consommation energetique des data centers doublera d'ici 2030 (de 415 TWh en 2024 a 945 TWh), et que les couts energetiques varient d'un facteur 2 a 3 entre les Etats-Unis et l'Europe avant ajustement PPA, ramenes a un facteur 1,59x apres ajustement (snapshot avril 2026). Ce differentiel energetique est le facteur E(r) du CACI : a compute brut egal, un pays avec une electricite deux fois plus chere a un CACI plus bas (poids 0,25 au denominateur). L'AIE fournit les donnees, le CACI fournit le cadre pour les integrer dans une mesure de competitivite.",
    ]),
    ("A.7.3 La synthese : comment ces six briques construisent le CACI", [
        "Chaque reference apporte une brique conceptuelle au CACI. Hawkins et al. fournissent la variable F (compute installe par region). L'AIE fournit la variable E (cout energetique differencie). Le FMI et l'OCDE fournissent les proxies de capital humain L. Farrell & Newman justifient l'integration de la dimension geopolitique R (acces reglementaire). Martens et la Fed identifient le besoin d'un indice synthetique. Bresnahan & Trajtenberg fournissent le cadre theorique (le compute comme infrastructure de la GPT).",
        "Ce que personne n'avait fait, c'est le croisement. Chaque dimension est traitee en silo dans la litterature : les economistes de l'energie ne parlent pas de GPU, les specialistes des export controls ne modelisent pas la productivite, les chercheurs en IA ne croisent pas avec la geopolitique. Le CACI nait de cette lacune structurelle : c'est un indice de synthese qui force le dialogue entre des litteratures cloisonnees.",
        "La formule retenue Power Mode - CACI(r) = F(r)^0,40 x L(r)^0,20 x R(r)^0,15 / E(r)^0,25 - traduit une intuition simple : la competitivite IA d'une region depend du compute dont elle dispose (F, dominant a 0,40), ajuste de ce qu'il lui coute (E, denominateur a 0,25), de sa capacite d'absorption (L, capital humain a 0,20) et de son acces reglementaire (R, a 0,15). La moyenne geometrique ponderee reflete le fait que ces facteurs sont complementaires, non substituables : du compute sans capital humain ne produit rien, du talent sans acces au compute non plus.",
    ]),
    ("A.7.4 Positionnement : ce que le CACI est et ce qu'il n'est pas", [
        "Le CACI n'est pas un indicateur definitif. C'est une premiere tentative de formalisation d'un concept que la communaute academique reconnaissait comme manquant. Sa contribution reside dans le framework - le fait de croiser compute, energie, economie et geopolitique dans un seul ratio - plus que dans la precision des chiffres. Comme tout indice composite (a l'instar du Global Innovation Index, du AI Readiness Index du FMI, ou du Digital Economy and Society Index de la Commission europeenne), le CACI repose sur des choix de ponderation et de proxy qui peuvent etre discutes et affines.",
        "Ce qui le distingue des indices existants est quadruple. Premierement, il integre le compute comme facteur central avec le poids le plus eleve (0,40) - aucun autre indice de competitivite ne le fait. Deuxiemement, il incorpore la contrainte energetique au denominateur (0,25), reconnaissant que le compute sans energie abordable est un actif theorique. Troisiemement, il est concu pour etre comparatif (ratio entre regions) plutot qu'absolu, ce qui le rend robuste aux erreurs de mesure systematiques. Quatriemement, l'extension Phys/Sov introduite au chapitre I (Fig 1.8) et formalisee section A.9 ajoute une dimension juridictionnelle qui distingue le compute physiquement present du compute legalement controlable.",
        "La validation econometrique presentee dans cette annexe (sections A.1 a A.6) confirme que le CACI Power Mode, malgre ses limites de mesure, possede un pouvoir predictif reel sur la productivite IA sectorielle (beta = 0,25, p < 0,01 en effets fixes). Ce resultat justifie a posteriori la demarche de construction et suggere que la communaute academique gagnerait a developper des indicateurs similaires, calibres sur des donnees plus exhaustives.",
    ]),
    ("A.8 Tableau synoptique : de la litterature au CACI", [
        "Le tableau A.3 ci-dessous synthetise la genealogie du CACI : pour chaque reference de la litterature, la composante CACI qu'elle alimente, et ce qui manquait dans cette reference que le CACI vient combler.",
    ]),
    ("A.9 Extension Phys/Sov : validation de la decomposition juridictionnelle", []),
    ("A.9.1 Construction de la decomposition", [
        "L'extension Phys/Sov, introduite au chapitre I (Fig 1.8) et formalisee au chapitre V (section 5.9.2), decompose le facteur F en deux composantes multiplicatives : F(r) = F_phys(r) x F_sov(r), ou F_phys est le compute physiquement installe dans la juridiction r et F_sov est la fraction de F_phys hors juridiction US (donc insensible aux Cloud Sovereignty Mandates hypothetiques de 2028).",
        "La decomposition est calculee de maniere rigoureuse depuis le champ Owner du jeu de donnees Epoch AI : pour chaque cluster operationnel, le proprietaire est classe en US-side (Microsoft, Google, AWS, Meta, OpenAI, Oracle, Stargate, etc.) ou non-US-side (operateurs domestiques nationaux). F_sov(r) est alors le ratio du F_phys non-US-side sur le F_phys total pour la region r.",
    ]),
    ("A.9.2 Resultats de la decomposition", [
        "Le tableau A.4 presente les resultats de la decomposition Phys/Sov pour les regions principales sur le snapshot avril 2026. Les resultats revelent une heterogeneite massive entre juridictions : USA et Chine sont integralement souverains (F_sov = 100 pct), l'UE est largement souveraine (F_sov = 99,2 pct), tandis que les Emirats arabes unis sont quasi-entierement US-side (F_sov = 0,4 pct).",
        "Le cas EAU est le plus revelateur quantitativement : sur 22,9 millions d'equivalents H100 physiquement installes (CACI Phys = 55,7), seuls 87 000 sont detenus par des operateurs sous juridiction emiratie, ce qui ramene le CACI Sov a 6,0 - un effondrement de 50 points qui transforme le hub IA emirati en simple infrastructure offshore americaine. Cette dissociation est invisible sur les indicateurs traditionnels qui ne distinguent pas la propriete du compute de sa localisation physique.",
    ]),
    ("A.9.3 Implication pour la lecture de l'asymetrie europeenne", [
        "L'extension Phys/Sov modifie radicalement la lecture du gap europeen. Sur le compute installe (F_phys), l'UE est presque entierement souveraine (99,2 pct). La vulnerabilite europeenne ne se situe donc pas sur l'infrastructure deployee dans les juridictions UE, mais sur la couche operationnelle des charges cloud - les workloads des entreprises europeennes etant majoritairement hebergees sur AWS, Microsoft Azure et Google Cloud (selon Synergy Research Group, 70 a 80 pct du cloud public europeen est sous controle des hyperscalers US).",
        "Cette distinction operationnelle, formalisee dans la section 5.9.2 du chapitre V, justifie l'orientation du chapitre VII (recommandations strategiques) : l'enjeu n'est pas de construire une infrastructure souveraine duplicate (l'UE en a deja une) mais d'augmenter la fraction des charges cloud hebergees sous juridiction europeenne (cible F_sov 30-40 pct des workloads europeens d'ici 2029, voir Fig 7.3).",
    ]),
    ("A.9.4 Validation econometrique de l'extension", [
        "Une validation econometrique complete de l'extension Phys/Sov necessite des donnees longitudinales sur la decomposition Owner depuis 2020, qui ne sont pas encore disponibles dans Epoch AI. La decomposition presentee ici est rigoureuse pour le snapshot avril 2026 mais ne permet pas de tester si les variations temporelles de F_sov predisent des variations differenciees de productivite IA. La constitution d'un panel longitudinal Phys/Sov constitue une piste prioritaire de recherche, et l'institution statistique la mieux placee pour le mener est l'OCDE (avec son AI Compute Intelligence Working Group lance en septembre 2025).",
    ]),
    ("A.10 Conclusion de l'annexe", [
        "Cette annexe a presente la validation econometrique du CACI Power Mode (sections A.1 a A.6), retrace sa genealogie intellectuelle dans la litterature (sections A.7 et A.8), et introduit l'extension Phys/Sov comme prolongement methodologique (section A.9). Les trois resultats principaux sont (1) le CACI predit significativement la productivite IA sectorielle (beta = 0,25, p < 0,01), (2) le compute brut domine effectivement les autres composantes (justifiant le poids 0,40 dans la formule Power Mode), et (3) la decomposition Phys/Sov revele une heterogeneite massive entre juridictions (UE 99,2 pct souveraine vs EAU 0,4 pct souverain) qui modifie la lecture des asymetries traditionnelles.",
        "Les estimations sont realisees avec Python (statsmodels 0.14, linearmodels 6.1). Le panel calibre et le script de reproduction sont disponibles en donnees supplementaires. Toutes les regressions utilisent des ecarts-types robustes clustered par pays. Le tableau de bord public Epoch AI (snapshot avril 2026, https://mo0ogly.github.io/America-First-IA/dashboard/) fournit les donnees brutes pour la reconstruction de la decomposition Phys/Sov.",
    ]),
]


TABLES = [
    ("Tableau A.1. Variables du panel et sources.",
     "Source : compilation de l'auteur. La variable CACI est calculee selon la formule Power Mode du chapitre II.",
     [
         ["Variable", "Definition", "Unite", "Source"],
         ["F(r,t)", "FLOPs IA installes accessibles", "PetaFLOPs (H100-eq)", "Epoch AI, Hawkins et al. (2025), CFG Europe"],
         ["E(r,t)", "Cout energie data centers (PPA-ajuste)", "USD/MWh", "Eurostat, EIA, AIE (avril 2025)"],
         ["L(r,t)", "Workforce IA (proxy STEM + certifications)", "Milliers", "OCDE, LinkedIn Economic Graph"],
         ["R(r,t)", "Acces reglementaire (Tier 1/2/3 BIS)", "Indice 0-1", "BIS, AI Diffusion Rule, Section 232"],
         ["GDP(r,t)", "Produit interieur brut", "Trillions USD", "Banque mondiale, FMI"],
         ["PROD(r,t)", "Gain productivite secteurs IA-intensifs", "pct gain annuel", "McKinsey (2024-26), FMI WP/25/067, Fed Board (2025)"],
         ["CACI(r,t)", "F^0,40 x L^0,20 x R^0,15 / E^0,25", "Indice (sans unite)", "Calcul auteur, formule chapitre II"],
     ]),
    ("Tableau A.2. Resultats des regressions panel.",
     "Ecarts-types robustes (clustered par pays) entre parentheses. *** p < 0,01, ** p < 0,05, * p < 0,10.",
     [
         ["Variable", "M1 : OLS", "M2 : FE", "M3 : RE"],
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
    ("Tableau A.3. Genealogie du CACI : de la litterature existante a l'indice original.",
     "Source : compilation de l'auteur. Pour chaque reference, la composante CACI qu'elle alimente et la lacune qu'elle laisse ouverte.",
     [
         ["Reference", "Ce qu'elle apporte", "Composante CACI", "Ce qui manquait"],
         ["Hawkins et al. (2025)", "Mesure du compute par region via cloud", "F(r)", "Pas d'indice composite, pas de Phys/Sov"],
         ["AIE (avril 2025)", "Couts energetiques DC, projections 2030", "E(r)", "Pas de lien avec competitivite IA"],
         ["Martens / Bruegel (2024)", "Barrieres d'entree, concentration compute", "Justification", "Aucune metrique proposee"],
         ["Fed Board (2025)", "Comparaison US/UE, appel a un indice unifie", "Justification", "Analyse descriptive uniquement"],
         ["Farrell & Newman (2019)", "Weaponized interdependence, points de controle", "R(r) acces reglement.", "Pas de quantification"],
         ["FMI WP/25/067 (2025)", "AI Preparedness Index, impact productivite", "L(r), methode", "Aucune composante compute"],
         ["CACI (cette etude)", "Synthese des 6 dimensions + extension Phys/Sov", "F, L, R, E + Owner", "Valide econometriquement (beta 0,25, p < 0,01)"],
     ]),
    ("Tableau A.4. Decomposition Phys/Sov par region (snapshot avril 2026).",
     "Source : calcul de l'auteur a partir du champ Owner d'Epoch AI. F_phys en millions d'equivalents H100 installes operationnels. F_sov calcule comme la fraction non-US-side. CACI Phys et Sov calcules selon la formule Power Mode.",
     [
         ["Region", "F_phys (M H100-eq)", "F_dom (M H100-eq)", "F_sov (pct)", "CACI Phys", "CACI Sov"],
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
    "Hawkins, B., Lehdonvirta, V. & Wu, B. (2025), 'AI Compute Sovereignty', Oxford Internet Institute Working Paper. Mesure empirique du compute IA par region a partir des infrastructures des neuf principaux fournisseurs cloud. Concept de compute sovereignty introduit pour la premiere fois.",
    "Bresnahan, T. & Trajtenberg, M. (1995), 'General Purpose Technologies : Engines of Growth ?', Journal of Econometrics, 65(1), 83-108. Theorie fondatrice des GPT et de leur dependance aux infrastructures complementaires.",
    "Brynjolfsson, E., Rock, D. & Syverson, C. (2019), 'Artificial Intelligence and the Modern Productivity Paradox : A Clash of Expectations and Statistics', NBER Chapters. Le paradoxe du delai entre adoption IA et materialisation des gains de productivite.",
    "Martens, B. (2024), 'Why AI is creating fundamental challenges for competition policy', Bruegel Working Paper 18/2024. Concentration du compute et barrieres a l'entree.",
    "Federal Reserve Board (octobre 2025), 'The State of AI Competition in Advanced Economies'. Comparaison metriques separees US/UE, appel a un indice unifie.",
    "FMI (2025), 'Mapping the Productivity Impacts of AI : A Cross-Country Analysis', Working Paper WP/25/067. AI Preparedness Index sans composante compute.",
    "Farrell, H. & Newman, A. (2019), 'Weaponized Interdependence : How Global Economic Networks Shape State Coercion', International Security, 44(1), 42-79. Cadre theorique des points de controle des reseaux globaux comme leviers geopolitiques.",
    "AIE (avril 2025), 'Energy and AI'. Demande energetique des data centers de 415 TWh en 2024 a 945 TWh en 2030. Differentiel energetique US/UE de l'ordre de 1,59x apres ajustement PPA (snapshot avril 2026).",
    "Note methodologique : les estimations sont realisees avec Python (statsmodels 0.14, linearmodels 6.1) sur le panel de 12 pays sur 2020-2024 (N = 60). Le tableau de bord public Epoch AI (https://mo0ogly.github.io/America-First-IA/dashboard/) fournit le snapshot avril 2026 utilise pour la calibration finale et la decomposition Phys/Sov section A.9.",
]


def build(out_dir: Path) -> Path:
    """Build the FR Annexe econometrique CACI .docx."""
    log.info("Building Annexe econometrique CACI [FR] -> Annexe_Econometrique_CACI_FR.docx")
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
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Annexe econometrique CACI")

    out = out_dir / "Annexe_Econometrique_CACI_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
