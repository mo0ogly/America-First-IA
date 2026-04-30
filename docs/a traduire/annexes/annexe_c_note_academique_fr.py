"""
Annexe C - Note Academique de synthese - generateur FR.

Genere le .docx de l'Annexe C (Note Academique de synthese) en francais.

Note Academique de synthese de la these qui en condense l'argument
principal, avec un addendum prospectif sur le Grand Decouplage 2028
(Cloud Sovereignty Mandates) et la decomposition C(r) = C_phys(r)
x F_sov(r).

Annexe C consolidee sur le baseline avril 2026 :
    - Bandeau couverture : 76,9 / 1,59x / 3,46:1
    - Ratio CACI US/UE Power Mode : 3,46:1 (au lieu de 3,4:1)
    - Ratio brut compute installe : 17,6:1
    - 76,9 pct du compute IA operationnel mondial = USA
      (au lieu de 74 pct du compute IA mondial)
    - Section 3.4 addendum Grand Decouplage : valeurs F_sov rigoureusement
      calculees depuis le champ Owner d'Epoch AI (UE 99,2 pct souverain
      sur compute installe ; EAU 99,6 pct US-side ; ces valeurs different
      du F_sov pour la couche workloads cloud, voir clarification)
    - Recapitulatif chapitres : 11 chapitres (incl. Chap VI quater Afrique)
    - §6 Limites : retrait de "Afrique absente" (Chap VI quater couvre)

Numerotation des tableaux : annexe C (Tab C.1, C.2, C.3).

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
from pathlib import Path

from note_acad_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("annexe_c_note_acad_fr")


CHAPTER_LABEL = "ANNEXE C - NOTE ACADEMIQUE"
CHAPTER_TITLE = (
    "AI for Americans First : protectionnisme IA americain, recomposition de l'ordre "
    "technologique mondial et consequences pour la France et l'Europe (2026-2030)"
)
CHAPTER_INTRO = (
    "Cette annexe presente la Note Academique de synthese de la these. Cette etude analyse les "
    "mecanismes et les consequences du protectionnisme IA americain sous l'administration "
    "Trump 2.0, en integrant quatre dimensions habituellement traitees separement dans la "
    "litterature : energie, semi-conducteurs, compute et regulation. A partir d'un diagnostic "
    "empirique 2020-2026, de la construction d'un indice de competitivite ajuste au compute "
    "(CACI) et d'une matrice scenarielle 2x2, la recherche demontre que la combinaison tarifs "
    "douaniers (25 pct, Section 232) et controles a l'export cree un avantage competitif "
    "structurel mesurable (ratio CACI US/UE de 3,46:1, mode Power, pour un ratio brut compute "
    "installe de 17,6:1, snapshot avril 2026), accelere paradoxalement la construction d'un "
    "ecosysteme IA chinois alternatif, et fragmente l'ordre technologique mondial en blocs "
    "competitifs. L'analyse comparative des reponses regionales (Europe, Amerique du Sud, Asie, "
    "Afrique) revele des trajectoires de dependance fondamentalement differenciees. Un addendum "
    "prospectif formalise un cinquieme scenario transversal, le Grand Decouplage 2028, fonde "
    "sur les Cloud Sovereignty Mandates americains et la dissociation entre facteur physique "
    "et facteur souverain dans le compute IA, revelant que la France et l'Europe doivent "
    "distinguer capacite physiquement installee et compute operationnellement souverain. Pour "
    "la France, l'etude identifie une fenetre d'action strategique 2026-2028 et recommande une "
    "autonomie strategique ciblee fondee sur l'avantage nucleaire, le champion IA Mistral et "
    "le cadre reglementaire europeen. Mots-cles : intelligence artificielle, protectionnisme "
    "technologique, semi-conducteurs, export controls, compute souverain, geopolitique de "
    "l'IA, France, Etats-Unis, Chine, Cloud Sovereignty Mandates, Grand Decouplage, facteur "
    "souverain F_sov, CLOUD Act, CADA, sovereignty washing, blocs d'IA juridictionnels."
)


SECTIONS: list[tuple[str, list[str]]] = [
    ("C.1 Objet et problematique", [
        "L'intelligence artificielle s'est imposee depuis 2023 comme le principal vecteur d'innovation economique et de competition geopolitique. Or, la chaine de valeur IA presente une concentration sans precedent : sur le snapshot avril 2026 du tableau de bord public, les Etats-Unis controlent 76,9 pour cent du compute IA operationnel mondial (49,9 pct en incluant les capacites planifiees), cinq hyperscalers americains (Microsoft, Amazon, Alphabet, Meta, Oracle) prevoient 660 a 690 milliards USD de capital expenditure pour la seule annee 2026, et Nvidia detient environ 80 pour cent du marche des accelerateurs IA.[1]",
        "Dans ce contexte, l'administration Trump 2.0 a transforme les controles a l'export inities par Biden (2022-2025) en un regime protectionniste hybride, combinant tarifs douaniers et restrictions reglementaires. Cette etude pose la question suivante : dans quelle mesure le protectionnisme IA americain cree-t-il un avantage competitif structurel mesurable, et quelles en sont les consequences differenciees pour la France, l'Europe et les autres regions du monde ?",
        "L'originalite de la recherche reside dans l'integration de quatre dimensions traitees separement dans la litterature : les trajectoires energetiques des data centers, le marche des semi-conducteurs, la distribution du compute IA et la chronologie reglementaire americaine. Aucune etude economique n'avait formalise un scenario integre Trump 2.0, protectionnisme IA ; cette recherche comble ce vide.",
    ]),
    ("C.2 Cadre methodologique", [
        "La methodologie repose sur trois piliers. Premierement, un diagnostic empirique longitudinal (2020-2026) fonde sur des donnees AIE, McKinsey, SIA, Epoch AI et des sources reglementaires (BIS, White House, Parlement europeen). Trois courbes critiques sont reconstruites : consommation energetique des data centers par region (TWh), marche des semi-conducteurs (valeur, part IA) et distribution du compute IA (GW IT load, FLOPs par region).",
        "Deuxiemement, la construction d'un indice de competitivite ajuste au compute (CACI), indice composite geometrique consolide selon la formule Power Mode : CACI(r,t) = F^0,40 x L^0,20 x R^0,15 / E^0,25, integrant quatre variables : FLOPs IA disponibles (poids 0,40, dominant), capital humain L (0,20), acces reglementaire R (0,15), et cout energetique E (0,25, denominateur). Le CACI permet de quantifier l'asymetrie structurelle entre regions et de projeter les trajectoires de divergence.[2]",
        "Troisiemement, une matrice scenarielle 2x2 croisant deux axes (intensite du protectionnisme US : moderee/forte ; reponse europeenne : passive/active) pour generer quatre scenarios 2026-2030, chacun calibre sur le CACI et confronte a trois points de basculement empiriques (saturation energetique UE 2028, consolidation fonderies Chine 2029, maturite chips alternatifs 2030). Un addendum prospectif etend le modele CACI par une decomposition du facteur compute : F(r) = F_phys(r) x F_sov(r), ou F_sov(r) mesure la fraction du compute regional opere hors juridiction americaine. Cette extension revele que la variable F(r) utilisee dans les scenarios A-D mesure la capacite physiquement installee, non la capacite operationnellement souveraine, deux metriques qui divergent considerablement dans les regions dominees par les hyperscalers americains.",
    ]),
    ("C.3 Resultats principaux", []),
    ("C.3.1 Un protectionnisme a trois etages", [
        "L'analyse identifie une architecture protectionniste a trois niveaux cumulatifs.",
        "Le premier etage est constitue par les controles a l'export (herites de Biden, transformes par Trump) qui segmentent le monde en trois tiers : acces illimite pour 20 allies proches (Tier 1), caps quantitatifs pour le reste (Tier 2), interdiction pour les adversaires (Tier 3).",
        "Le deuxieme etage, innovation propre a Trump, reside dans les tarifs douaniers de 25 pct (Section 232, 15 janvier 2026) sur les semi-conducteurs IA avances, creant un differentiel de cout direct entre entreprises americaines (exemptees) et non-americaines.[3]",
        "Le troisieme etage est l'effet de gravite capitalistique : 660-690 milliards USD de capex annuel, investissements japonais (550 milliards) et emiratis convergent vers le sol americain, auto-renforcant la concentration du compute sans intervention reglementaire supplementaire.",
        "Un quatrieme etage potentiel se profile a l'horizon 2028 : les Cloud Sovereignty Mandates analyses dans l'addendum (section C.3.4), qui transformeraient les hyperscalers US operant offshore en intermediaires conditionnels du compute mondial.",
    ]),
    ("C.3.2 Avantage competitif mesure", [
        "Le CACI Power Mode quantifie un ratio US/UE de 3,46:1 (snapshot avril 2026), pour un ratio brut compute installe de 17,6:1, refletant un compute gap (US : environ 53,7 GW IT, UE : environ 35 GW), un differentiel de cout des FLOPs (en faveur des US d'un facteur 5 a 10 sur le training de modeles frontier) et un ecart de productivite IA (gains plus eleves dans les economies a forte densite compute selon le Federal Reserve Board 2025 et le FMI WP/25/067).",
        "Quatre mecanismes de transmission sont identifies : l'asymetrie des couts de training (training d'un modele frontier 5 a 10 fois plus cher en UE qu'aux US apres ajustement PPA), la concentration du cloud (70 a 80 pct des workloads IA europeens sur hyperscalers US selon Synergy Research Group), l'ecart de productivite, et la capture des rentes d'innovation (effets d'echelle plus effets de reseau).[4]",
    ]),
    ("C.3.3 Effets paradoxaux systemiques", [
        "L'etude demontre que le protectionnisme produit trois effets paradoxaux. Premierement, les restrictions accelerent la construction d'un ecosysteme IA chinois autonome (Huawei Ascend 910c et 910d, DeepSeek-V3, investissements de plus de 125 milliards USD en 2025, capacite reelle revendiquee 246-300 EFLOP/s contre 0,5 pct apparent dans les donnees Epoch AI consolidees) plutot que de la neutraliser. Deuxiemement, les pays Tier 2 (Bresil, Inde, ASEAN, et continent africain) sont pousses vers des partenariats technologiques chinois (ByteDance : 38 milliards USD au Bresil/Pecem, 8,8 milliards en Thailande, Huawei dominant 70 pct du backbone 4G africain), creant une bifurcation technologique mondiale. Troisiemement, les allies Tier 1 (Japon, Coree) co-financent la suprematie US (Japon : 550 milliards USD investis sur le sol americain) plutot que de construire une autonomie propre. Le resultat n'est pas un ordre unipolaire mais un monde fragmente en blocs technologiques.[5]",
    ]),
    ("C.3.4 Le Grand Decouplage 2028, un cinquieme scenario transversal", [
        "Un addendum prospectif modelise un basculement qualitatif distinct des quatre scenarios initiaux : le Cloud Nationality Pivot. Alors que les scenarios A-D analysent des degres de protectionnisme dans un cadre de controle physique des semi-conducteurs, ce scenario modelise un changement de nature : le passage du controle par les flux (export controls sur les puces) au controle par la couche juridictionnelle (souverainete d'exploitation des clusters en place). Ses fondements juridico-techniques sont deja operationnels en 2026 : le CLOUD Act (2018) etablit qu'un cluster H100 physiquement installe en Irlande ou a Dubai reste juridiquement americain[10] ; l'AI Action Plan americain du 23 juillet 2025 introduit des location verification features embarques dans les puces IA avancees, premier substrat technique du throttling a distance.[11]",
        "Le paradoxe central du scenario reside dans la dissociation entre facteur physique et facteur souverain. La decomposition rigoureuse F(r) = F_phys(r) x F_sov(r) calculee a partir du champ Owner d'Epoch AI (chapitre I, Fig 1.8) revele deux metriques distinctes selon la couche analysee.",
        "Sur le compute installe (cluster ownership), les Etats-Unis et la Chine sont integralement souverains (F_sov = 1,00). L'UE est largement souveraine sur ses clusters domestiques (F_sov = 0,992 sur F_phys 2,6 millions H100-eq). Le cas extreme est celui des Emirats arabes unis : sur 22,9 millions H100-eq physiquement installes, seuls 87 000 sont detenus par des operateurs sous juridiction emiratie (F_sov = 0,004), faisant chuter le CACI souverain de 55,7 (Physique) a 6,0 - un effondrement de 50 points qui transforme le hub IA emirati en simple infrastructure offshore americaine.",
        "Sur la couche operationnelle des charges cloud (workloads), les ratios sont radicalement differents. Selon Synergy Research Group, les hyperscalers americains controlent environ 72 pct du cloud public europeen (donc F_sov_workloads UE environ 0,28), 88 pct aux Emirats arabes unis (F_sov_workloads environ 0,12), 60 pct en Inde (F_sov_workloads environ 0,40), et seulement 2 pct en Chine (F_sov_workloads environ 0,98).[12] Ces deux metriques s'accordent la ou les clusters domestiques sont detenus par des operateurs domestiques (US, Chine, France via Fluidstack/Sesterce). Elles divergent fortement pour les juridictions ou les clusters physiquement localises sont detenus par des operateurs US-side (cas EAU sur compute installe) ou ou les workloads sont massivement hebergees a l'etranger (cas UE sur charges cloud).",
        "Le scenario B (Fracture plus Cloud Sovereignty Mandates 2028) produit un double effet de ciseaux : chips rares et compute conditionnel simultanement, poussant le ratio CACI US/UE potentiellement au-dela de 8:1. Le scenario C (Gigafactories sous juridiction europeenne) est le seul a absorber le choc en augmentant structurellement F_sov_workloads vers 0,45-0,55. Ce resultat demontre que la politique europeenne actuelle d'attraction des data centers confond la metrique de compute installe avec la metrique de compute souverain operationnel, une confusion que le CADA (Cloud and AI Development Act, propose par la Commission en Q1 2026) commence seulement a formaliser.[13]",
    ]),
    ("C.4 Analyse comparative regionale", [
        "L'etude conduit une analyse differenciee de l'impact du protectionnisme IA sur six regions, revelant des trajectoires de dependance structurellement distinctes. Le tableau C.1 ci-dessous synthetise les positions.",
        "L'analyse revele que la position geopolitique (Tier 1/2/3), la dotation energetique et la proximite avec les chaines de valeur determinent des trajectoires irreductibles a un modele unique. La France beneficie de son statut Tier 1 et d'un cout PPA-ajuste 1,35x USA (115 vs 85 USD/MWh) mais souffre d'un compute gap structurel. Le Bresil, classe Tier 2, est le theatre direct de la rivalite US-Chine. Le Japon, allie le plus integre, co-finance la suprematie americaine. L'Inde tente une troisieme voie. La Chine construit un ecosysteme parallele. L'Afrique, deficit compute le plus extreme (x44 a x417 selon les indicateurs), fait face au double bind US/Chine.",
    ]),
    ("C.5 Recommandations strategiques pour la France", [
        "L'etude formule des recommandations structurees en cinq axes et trois horizons temporels.",
        "Axe 1 - Infrastructure compute. Accelerer les 13 AI Factories europeennes (operationnelles fin 2027), mettre en oeuvre les Special Compute Zones (permis acceleres, fiscalite allegee), deployer les 5 AI Gigafactories InvestAI (20 milliards EUR). Objectif : 30 a 40 pct des workloads IA sensibles sur cloud souverain certifie d'ici 2029. La distinction F_sov impose une reformulation de la metrique de succes : l'indicateur decisif n'est pas combien de GPU en Europe mais combien de GPU sous juridiction europeenne et combien de workloads sous juridiction europeenne.[14] Le phenomene de sovereignty washing (hyperscalers americains commercialisant du cloud souverain sur sol europeen tout en restant soumis au CLOUD Act) constitue le risque systemique principal de la politique d'attraction des investissements actuelle.[6]",
        "Axe 2 - Energie nucleaire. Exploiter l'avantage unique francais (70 pct d'electricite nucleaire decarbonee, cout PPA 115 USD/MWh contre 135 USD/MWh moyenne UE et 85 USD/MWh USA, ratio France/USA 1,35x). EDF a identifie quatre sites industriels totalisant 2 GW, avec l'initiative Nuclear for AI (250 MW d'ici fin 2026). Accelerer les 6 EPR 2 (Penly, Bugey, 9 900 MW, construction 2027), confirmer les 8 reacteurs optionnels, soutenir les SMR (NUWARD, Newcleo, Stellaria).[7]",
        "Axe 3 - Alliances technologiques. Consolider le partenariat ASML-Mistral (1,3 milliard EUR, ASML premier actionnaire a 11 pct). Negocier un second investissement TSMC en Europe sur noeuds avances. Conclure des accords bilateraux UE-Japon et UE-Coree sur la securite d'approvisionnement (memoire HBM, equipements). Constituer des reserves strategiques de GPU (6 a 12 mois).",
        "Axe 4 - Regulation offensive. Transformer l'AI Act en levier competitif : priorite aux modeles europeens dans les AI Factories publiques, effet Bruxelles via accords de reconnaissance mutuelle, creation d'un CLOUD Act Shield europeen alignant le reglement sur le niveau SOV-3 du Cloud Sovereignty Framework.",
        "Axe 5 - Talent. Bourses IA et visas talents europeens (avant fin 2026), garantie d'acces au compute frontier pour les chercheurs europeens (Fluidstack 500 000 GPU, Mistral Compute, AI Factories EuroHPC).[8]",
        "La fenetre d'action critique se situe entre 2026 et 2028 : au-dela, le point de basculement energetique et compute identifie cristallise les dependances autour de la baseline 17,6:1 brut / 3,46:1 CACI Power Mode.",
    ]),
    ("C.6 Contributions, limites et prolongements", [
        "Cette recherche contribue a la litterature sur cinq plans.",
        "(i) L'integration analytique de trajectoires habituellement cloisonnees (energie, semi-conducteurs, compute, regulation, productivite).",
        "(ii) La proposition de l'indice CACI Power Mode comme cadre de mesure de la competitivite ajustee au compute (formule geometrique F^0,40 x L^0,20 x R^0,15 / E^0,25 validee econometriquement avec beta = 0,251, p < 0,01 en effets fixes, R2 within 0,692).",
        "(iii) La demonstration des effets paradoxaux systemiques du protectionnisme IA (acceleration de l'ecosysteme chinois, push des Tier 2 vers la Chine, co-financement de la suprematie US par les allies).",
        "(iv) L'analyse comparative inedite des reponses regionales (Europe, Amerique du Sud, Asie, Afrique) revelant des trajectoires de dependance structurellement distinctes.",
        "(v) La formalisation de la decomposition F(r) = F_phys(r) x F_sov(r) qui revele la distinction entre compute physiquement installe et compute operationnellement souverain, distinction absente de la litterature existante et aux implications directes pour les politiques d'investissement en Gigafactories, en data centers et en energie nucleaire.",
        "Les limites tiennent a l'incertitude reglementaire (la regle finale BIS de janvier 2026 pourrait etre modifiee d'ici juillet 2026), a l'heterogeneite des donnees de compute (le CACI reste un indice exploratoire, validation econometrique sur N = 60 dans l'annexe A), a l'horizon temporel (des ruptures technologiques post-2030 pourraient redistribuer les avantages), et a la sensibilite aux ponderations CACI (analyse de robustesse documentee dans l'annexe A).",
        "Quatre prolongements s'imposent : le calibrage empirique du CACI sur donnees d'enquete avec un panel etendu a 25-30 pays et 10 ans, l'approfondissement sectoriel de la couverture Afrique (chapitre VI quater), la modelisation dynamique via des modeles d'equilibre general calculable (CGE) integrant le compute comme facteur de production, et la constitution d'un panel longitudinal Phys/Sov (champ Owner d'Epoch AI) pour tester si les variations temporelles de F_sov predisent des variations differenciees de productivite IA.",
    ]),
    ("C.7 Conclusion", [
        "Le compute IA est en passe de devenir le quatrieme facteur de production, structurant l'acces aux gains de productivite et a l'innovation. L'AI Action Plan americain de juillet 2025 traite desormais le stack IA comme un instrument d'alliance geopolitique, comparable au Plan Marshall : l'acces au compute est conditionne a l'alignement strategique.[9]",
        "Face a cette recomposition, trois options se presentent pour la France : l'integration subordonnee (modele Japon, 550 milliards USD investis aux US), la confrontation souverainiste (modele Chine, irrealiste a horizon 2030 pour l'Europe), ou l'autonomie strategique ciblee que cette etude recommande : souverainete sur les segments d'avantage comparatif (nucleaire 70 pct du mix, ASML, Mistral 11,7 milliards EUR de valorisation, AI Act) combinee a l'interoperabilite avec l'ecosysteme americain. L'objectif n'est pas l'autarcie technologique mais la capacite de choix.",
        "La distinction Phys/Sov etablie au chapitre I est ici operationnelle : l'Europe est deja largement souveraine sur le compute installe (99,2 pct), le travail consiste a securiser la couche des charges cloud (cible 30 a 40 pct de F_sov_workloads d'ici 2029) avant que les Cloud Sovereignty Mandates 2028 ne transforment cette dependance en levier geopolitique. La question n'est plus de savoir si la recomposition de l'ordre technologique mondial aura lieu - elle est en cours - mais de determiner si la France et l'Europe en seront les architectes ou les sujets.",
    ]),
]


TABLES = [
    ("Tableau C.1. Synthese des consequences regionales du protectionnisme IA americain.",
     "Source : construction de l'auteur, calibration sur snapshot avril 2026 (US 76,9 pct compute IA operationnel, ratio brut UE 17,6:1, CACI Power Mode 3,46:1).",
     [
         ["Region", "Tier", "Dynamique principale", "Atout strategique", "Risque principal"],
         ["France / Europe", "1",
          "Dependance GPU + cloud US (72 pct workloads) ; reponse InvestAI 200 Md EUR",
          "Nucleaire (70 pct mix), Mistral, ASML, AI Act, cout PPA 1,35x USA",
          "Vendor lock-in geopolitique ; F_sov workloads bas ; CSM 2028"],
         ["Bresil / Am. Sud", "2",
          "Terrain de competition US-Chine ; megaprojets TikTok/Scala 38 Md USD",
          "Mix energetique 83 pct renouvelable ; marche fintech dynamique",
          "Triple fracture (Nord-Sud, Est-Ouest, intra-regionale)"],
         ["Japon / Coree / Taiwan", "1",
          "Co-investissement US (Japon 550 Md USD) ; transfert production",
          "HBM (SK hynix), TSMC 90 pct chips pointe, materiaux",
          "Partenariat asymetrique ; erosion silicon shield Taiwan"],
         ["Inde", "2",
          "Pivot Sud global ; ambition 200+ Md USD ; strategie compute export",
          "1,4 Md habitants, talent tech, politique zero-impot cloud 2047",
          "Fosse structurel (1,4 GW vs 53,7 US) ; caps GPU Tier 2"],
         ["Chine", "3",
          "Autonomisation forcee ; ecosysteme alternatif Huawei/DeepSeek",
          "Marche interieur 1,4 Md ; investissements 125+ Md USD/an ; 246-300 EFLOP/s",
          "Retard 2-3 generations GPU ; isolement technologique"],
         ["Afrique", "2/3",
          "Asymetrie compute extreme (deficit x44-x417) ; double bind US/Chine",
          "Geothermie Kenya, solaire Maroc, marche fintech naissant",
          "Bifurcation imposee ; surveillance Huawei/DeepSeek ; cas EAU"],
     ]),
    ("Tableau C.2. Decomposition Phys/Sov du compute IA (snapshot avril 2026).",
     "Source : calcul de l'auteur a partir du champ Owner d'Epoch AI (compute installe) et Synergy Research Group / Statista (workloads cloud).",
     [
         ["Region", "F_phys (M H100-eq)", "F_sov compute installe", "F_sov workloads cloud", "CACI Phys", "CACI Sov installe"],
         ["USA", "39,6", "1,00", "1,00", "100", "100"],
         ["Chine", "0,4", "1,00", "0,98", "15,7", "15,7"],
         ["UE(13)", "2,6", "0,99", "0,28", "28,9", "28,8"],
         ["France", "2,4", "1,00", "~0,30", "25,3", "25,3"],
         ["Inde", "1,8", "0,94", "0,40", "22,2", "21,0"],
         ["EAU", "22,9", "0,004", "0,12", "55,7", "6,0"],
     ]),
    ("Tableau C.3. Recapitulatif des chapitres de l'etude (11 chapitres).",
     "Source : construction de l'auteur. Les pages indicatives incluent figures et tableaux mais excluent les annexes operationnelles.",
     [
         ["Chap.", "Titre", "Pages", "Notes"],
         ["I", "Cadre theorique : protectionnisme technologique et IA", "12", "22"],
         ["II", "Methodologie : matrice scenarielle et indice CACI", "8", "10"],
         ["III", "Diagnostic empirique 2020-2026", "11", "20"],
         ["IV", "Mecanismes de l'avantage competitif US", "9", "19"],
         ["V", "Scenarios prospectifs 2026-2030 et Cloud Sovereignty Mandates", "14", "29"],
         ["VI", "Consequences pour la France et l'Europe", "10", "14"],
         ["VI bis", "Consequences pour l'Amerique du Sud et le Bresil", "11", "19"],
         ["VI ter", "Consequences pour l'Asie", "12", "16"],
         ["VI quater", "Consequences pour l'Afrique", "13", "26"],
         ["VII", "Recommandations strategiques", "11", "18"],
         ["Concl.", "Du protectionnisme IA a la recomposition de l'ordre technologique", "9", "3"],
         ["Total", "11 chapitres", "~120", "196"],
     ]),
]


NOTES = [
    "Euronews (fevrier 2026), 'Will Big Tech's AI Spending Crush Europe's Data Sovereignty ?'. Capex 2026 : Amazon 200 Md USD, Alphabet 185 Md USD, Microsoft 145 Md USD, Meta 135 Md USD, Oracle 50 Md USD. Total : 660-690 Md USD. Snapshot avril 2026 du tableau de bord public : USA 76,9 pct du compute IA operationnel mondial.",
    "L'indice CACI Power Mode est developpe au chapitre II et valide econometriquement dans l'annexe A (beta = 0,251, p < 0,01, R2 within 0,692). Il s'inspire des metriques de compute-adjusted competitiveness identifiees comme manquantes par McKinsey (2024) et le World Economic Forum (2025).",
    "Pillsbury Law (janvier 2026), 'Trump Admin Targets Advanced AI Semiconductors'. Section 232 : tarif 25 pct sur Nvidia H200, AMD MI325X pour reexportation Chine. Exemptions domestiques US. Regle finale BIS du 15 janvier 2026.",
    "Bruegel (2025), 'Why Artificial Intelligence Is Creating Fundamental Challenges for Competition Policy'. Couts training exponentiels comme barriere a l'entree. Snapshot avril 2026 : compute IA UE(13) 3,3 pct vs US 76,9 pct ; ratio brut 17,6:1 ; ratio CACI Power Mode 3,46:1.",
    "Carnegie Endowment (mai 2025) : trilemme controle/promotion/levier. IBTimes India (fevrier 2026) : Chine 125+ Md USD infrastructure IA 2025, capacite revendiquee 246-300 EFLOP/s. Construction Today (novembre 2025) : Japon 550 Md USD investis aux US. Bloomberg/DCD (2025) : ByteDance 38 Md USD Bresil/Pecem.",
    "Commission europeenne (avril 2025), AI Continent Action Plan. 13 AI Factories, InvestAI 200 Md EUR. CFG (octobre 2025), 'Special Compute Zones : Europe's Recipe'. Julien Simon, Medium (janvier 2026), 'AI Sovereignty in Europe : A Decision Framework'. Sovereignty washing : phenomene de commercialisation par les hyperscalers US de produits 'cloud souverain' en sol europeen tout en restant soumis au CLOUD Act US.",
    "World Nuclear News (fevrier 2025) : EDF 4 sites, 2 GW. Enki AI (fevrier 2026) : EPR 2 (9 900 MW), 20 reacteurs extension vie (26 GW). Introl Blog (2025) : investissements IA France 109 Md EUR, Fluidstack 10 Md EUR / 1 GW. Cout PPA-ajuste France 115 USD/MWh, ratio 1,35x USA (vs ratio UE moyen 1,59x).",
    "McKinsey (decembre 2025), 'Accelerating Europe's AI Adoption : The Role of Sovereign AI'. Bourses IA et visas talents a lancer avant fin 2026. 44 pct des leaders tech europeens citent la securite des donnees comme frein.",
    "CM Trade Law (juillet 2025), 'America's AI Action Plan'. Pilier III : exporter le full AI technology stack aux pays disposes a rejoindre l'alliance IA americaine. Quatre principes : export allies, enforcement, alignement global, protection mesures.",
    "CLOUD Act (Clarifying Lawful Overseas Use of Data Act), Pub. L. 115-141 (23 mars 2018), titre III, paragraphe 103(a), codifie a 18 U.S.C. paragraphe 2713 : un fournisseur doit se conformer aux obligations du chapitre quel que soit le lieu de stockage. Microsoft a reconnu devant le Tribunal judiciaire de Paris (2024) qu'il ne peut garantir la souverainete des donnees europeennes en cas d'injonction legalement fondee aux Etats-Unis ; cite dans The Register (22 decembre 2025), 'Europe gets serious about cutting US digital umbilical cord'.",
    "White House, America's AI Action Plan (23 juillet 2025), Pilier III, 'Strengthen AI Compute Export Control Enforcement'. Michael Kratsios (OSTP Director) : discussions sur des modifications logicielles ou physiques des puces pour ameliorer le location-tracking, explicitement incluses dans le plan (APEC Digital and AI Ministerial Meeting, Seoul, aout 2025, cite dans TechResearchOnline, 5 aout 2025). Le BIS AI Action Plan charge le Department of Commerce d'identifier ces location verification features en collaboration avec l'industrie.",
    "Decomposition Phys/Sov rigoureusement calculee depuis le champ Owner d'Epoch AI (snapshot avril 2026, voir chapitre I Fig 1.8) : F_sov sur compute installe atteint 1,00 pour USA et Chine, 0,99 pour UE(13), 1,00 pour France, 0,94 pour Inde, et 0,004 pour les EAU (99,6 pct US-side). F_sov sur workloads cloud calcule a partir des parts de marche des hyperscalers americains (Synergy Research Group T3 2025, Statista Enterprise Cloud Market Share EU 2025) : EAU environ 0,12, UE environ 0,28, Inde environ 0,40, Chine environ 0,98. Une calibration empirique rigoureuse sur donnees d'enquete pour la couche workloads est identifiee comme prolongement de recherche prioritaire.",
    "Commission europeenne, Programme de travail 2026, Cloud and AI Development Act (CADA), prevu Q1 2026. Cloud Sovereignty Framework (octobre 2025) : trois niveaux SOV-1 a SOV-3, le niveau SOV-3 exigeant protection totale contre les legislations extraterritoriales non europeennes. Cristina Caffarra (Fondation Eurostack), citee dans The Register (22 decembre 2025) : une entreprise soumise aux lois extraterritoriales des Etats-Unis ne peut etre consideree comme souveraine pour l'Europe.",
    "Cas concrets de sovereignty washing : Microsoft France (2024, cf. note 10) pour les limites du cloud souverain en sol europeen ; accord G42/Microsoft (2024) ou Abu Dhabi a du accepter de rompre ses liens avec des entites chinoises comme condition d'acces aux puces NVIDIA avancees (Department of Commerce US, declarations de la secretaire Gina Raimondo) ; acquisition de Solvinity (fournisseur cloud neerlandais) par Kyndryl (groupe americain) en novembre 2025, annulant de facto la souverainete de clients publics neerlandais qui l'avaient specifiquement choisie (The Register, decembre 2025).",
]


SOURCES_LINE = (
    "Sources principales mobilisees - Institutions internationales : AIE (2025-2026), Banque "
    "mondiale (2025), World Economic Forum (2025-2026), CEPALC/CENIA (ILIA 2025), Union "
    "africaine (Strategie continentale IA). Think tanks et recherche : Bruegel, Brookings "
    "Institution, Carnegie Endowment for International Peace, CSIS, Hudson Institute, ITIF, "
    "Centre for Future Generations (CFG), Epoch AI, New Lines Institute, Atlantic Council "
    "DFRLab. Cabinets et analystes : McKinsey & Company, S&P Global, Arizton, Gartner, Futurum "
    "Group, Deloitte, Synergy Research Group, Statista. Sources reglementaires : White House / "
    "BIS (AI Diffusion Rule, AI Action Plan, Section 232), Parlement europeen, Commission "
    "europeenne (AI Continent Action Plan, Apply AI Strategy, Chips Act, CADA), ANSSI "
    "(SecNumCloud), USTDA. Presse specialisee : Euronews, Bloomberg, DCD, Financial Times, "
    "Foreign Policy, Pillsbury Law, CM Trade Law, Introl, The Register. Donnees primaires : "
    "tableau de bord public Epoch AI snapshot avril 2026 "
    "(https://mo0ogly.github.io/America-First-IA/dashboard/)."
)


def build(out_dir: Path) -> Path:
    """Build the FR Annexe C Note Academique de synthese .docx."""
    log.info("Building Annexe C Note Academique [FR] -> Annexe_C_Note_Academique_FR.docx")
    doc = init_document()
    add_cover(doc, chapter_label=CHAPTER_LABEL,
              chapter_subtitle="Note academique de synthese")
    add_chapter_header(doc, label=CHAPTER_LABEL,
                       title=CHAPTER_TITLE, intro=CHAPTER_INTRO)

    for title, paragraphs in SECTIONS:
        render_section(doc, title, paragraphs)

    for caption, source, rows in TABLES:
        render_table(doc, caption, source, rows)

    # Sources line at the very end before notes
    from note_acad_helpers import add_paragraph, GREY
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    add_paragraph(doc, SOURCES_LINE,
                  align=WD_ALIGN_PARAGRAPH.LEFT,
                  size=9, italic=True, color=GREY, space_after=6)

    render_notes(doc, NOTES)
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Annexe C Note academique")

    out = out_dir / "Annexe_C_Note_Academique_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
