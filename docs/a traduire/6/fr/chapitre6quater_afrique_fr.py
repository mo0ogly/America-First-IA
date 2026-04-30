"""
Chapitre VI quater - Consequences pour l'Afrique - generateur FR.

Genere le .docx du Chapitre VI quater en francais. Couvre la cartographie
des poles africains (Afrique du Sud, Nigeria, Kenya, Maroc, Egypte, Rwanda),
la rivalite US-Chine, les 5 canaux de transmission du protectionnisme,
les atouts strategiques et les scenarios S1-S4 sous matrice 2x2.

Numerotation des tableaux : continue (Tab 19, 20, 21, 22).

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
from pathlib import Path

from chap6_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("chapitre6quater_fr")


CHAPTER_LABEL = "CHAPITRE VI QUATER"
CHAPTER_TITLE = "Consequences pour l'Afrique"
CHAPTER_INTRO = (
    "L'analyse menee dans les chapitres precedents a couvert l'Europe, l'Amerique du Sud et "
    "l'Asie. Or, l'Afrique - identifiee dans la conclusion generale comme un prolongement de "
    "recherche necessaire - constitue desormais un terrain de competition geopolitique decisif. "
    "Representant 18 pour cent de la population mondiale mais moins de 1 pour cent de la "
    "capacite mondiale de data centers, le continent cumule un deficit structurel de compute "
    "avec un potentiel energetique (geothermie, solaire, hydroelectricite) et un dynamisme "
    "demographique qui en font un enjeu majeur de la recomposition de l'ordre technologique "
    "mondial. Ce chapitre complementaire analyse les consequences specifiques du protectionnisme "
    "IA americain sur l'Afrique, en distinguant les dynamiques sous-regionales et les effets "
    "differencies de la rivalite US-Chine."
)


SECTIONS: list[tuple[str, list[str]]] = [
    ("6quat.1 Position structurelle : le continent du compute paradox", []),
    ("6quat.1.1 Un ecart infrastructurel sans equivalent", [
        "L'Afrique presente l'asymetrie compute la plus extreme au monde. Mi-2025, le continent compte 223 data centers repartis dans 38 pays - moins de 2 pour cent du total mondial (11 800+). La capacite installee est estimee entre 780 MW et 1 170 MW, soit l'equivalent d'un seul campus hyperscale americain.[1] La distribution est elle-meme fortement concentree : l'Afrique du Sud (56 data centers), le Kenya (19) et le Nigeria (17) hebergent 41 pour cent de l'infrastructure continentale. L'Egypte et le Maroc dominent l'Afrique du Nord.",
        "En termes de GPU IA - le facteur determinant pour le compute frontier - l'ecart est encore plus brutal. Seuls 5 pour cent des innovateurs IA africains ont acces a du compute avance, tandis que le deficit de demande non satisfaite est estime a 7 millions d'heures GPU sur trois ans.[2] Cet ecart ne reflete pas une absence de demande mais une absence d'offre : le paradoxe du compute africain reside dans la coexistence d'une demande latente croissante et d'une infrastructure insuffisante pour la satisfaire. Le WEF estime que briser ce paradoxe pourrait liberer 1 200 a 1 500 milliards USD de valeur economique d'ici 2030.",
        "La croissance est neanmoins rapide. McKinsey (novembre 2025) projette la demande en data centers africains entre 1,5 et 2,2 GW a horizon 2030, avec un taux de croissance annuel compose de 14,5 a 24 pour cent selon les segments. Le marche africain des data centers, evalue a 1,94 milliard USD en 2025, devrait atteindre 4,36 milliards en 2031.[3] Le marche nigerian seul est evalue a 288 millions USD en 2025 avec une projection a 1,09 milliard en 2031 (CAGR 25 pour cent).",
    ]),
    ("6quat.1.2 Classification Tier et acces au compute US", [
        "Dans l'architecture de controle a l'export americaine, la quasi-totalite des pays africains releve du Tier 2 (acces restreint avec caps quantitatifs), voire du Tier 3 pour les pays sous sanctions. Aucun pays africain ne figure dans le Tier 1 (acces illimite), reserve aux 20 allies proches des Etats-Unis. Cette classification a des consequences directes : les caps GPU imposent un plafond structurel a l'infrastructure de compute frontier accessible aux acteurs africains, meme lorsque le financement est disponible. Le cout d'acces aux GPU Nvidia sur le marche secondaire est estime entre 45 000 et 60 000 USD l'unite.[4]",
        "Paradoxalement, cette restriction americaine ouvre un espace strategique pour les fournisseurs chinois. Huawei, present sur le continent depuis les annees 1990 via ses equipements telecom, controle environ 70 pour cent du backbone 4G africain et mene le deploiement 5G dans 30 marches. L'entreprise propose desormais des solutions data center integrees (FusionModule2000, UPS5000-E) incluant des accelerateurs IA Ascend, a des prix significativement inferieurs a ceux de Nvidia.[5] La classification Tier 2 cree donc un push factor vers l'ecosysteme technologique chinois, reproduisant en Afrique le mecanisme identifie pour l'Amerique du Sud (chapitre VI bis).",
    ]),
    ("6quat.2 Les poles emergents : cartographie differenciee", []),
    ("6quat.2.1 Afrique du Sud : hub principal et point d'ancrage des hyperscalers", [
        "L'Afrique du Sud detient 40,8 pour cent de la part de marche africaine des data centers en 2025. Le marche sud-africain de l'IA dans les data centers croit a 42 pour cent par an (de 70 millions en 2025 a 572 millions en 2031). Les trois hyperscalers americains ont consolide leur presence : Microsoft (5,4 milliards de rands, environ 300 millions USD d'ici 2027, apres 20,4 milliards de rands investis sur trois ans), AWS (1,7 milliard USD dans la region du Cap), Google (region cloud Johannesburg).[6] Le pays beneficie d'une National AI Strategy, du Centre for AI Research (CAIR) et d'un reseau electrique relativement developpe, malgre des episodes recurrents de load shedding. C'est aussi le siege de la premiere AI Factory africaine de Cassava Technologies/Nvidia (3 000 GPU deployes mi-2025).",
    ]),
    ("6quat.2.2 Nigeria : moteur de croissance de l'Afrique de l'Ouest", [
        "Le Nigeria emerge comme le marche data center a la croissance la plus rapide d'Afrique. Lagos concentre l'essentiel des investissements : Equinix (plan d'expansion de 100 millions USD sur le continent), Africa Data Centres, Digital Realty, Rack Centre.[7] Le pays beneficie de sa connectivite sous-marine (cables WACS, ACE, MainOne, Glo-1) et d'un ecosysteme fintech dynamique (13 banques de depot integrant des chatbots IA des 2024). Microsoft s'engage a former un million de Nigerians a l'IA, le pays ayant identifie un potentiel de 15 milliards USD de contribution de l'IA au PIB d'ici 2030. Le National Centre for AI and Robotics (NCAIR) structure l'ecosysteme de recherche.",
    ]),
    ("6quat.2.3 Kenya : la Silicon Savannah et l'atout geothermique", [
        "Le Kenya se distingue par la combinaison unique d'un ecosysteme tech dynamique (Silicon Savannah) et d'un avantage energetique structurel : plus de 60 pour cent de son electricite provient de sources renouvelables, dont la geothermie de la zone de Naivasha. C'est cet atout qui a attire l'investissement de 1 milliard USD de Microsoft et G42 (EAU) pour un data center geothermique de 100 MW a Olkaria, extensible a 1 GW.[8] Le gouvernement offre des incitations fiscales en zones economiques speciales (exemption de 10 pour cent d'impot sur les societes pendant 10 ans). Le campus IXAfrica de Nairobi, en partenariat strategique avec Safaricom, fournit deja une infrastructure AI-ready. La strategie IA nationale (mars 2025) positionne le Kenya comme leader regional de la recherche et de l'innovation IA.",
        "Le Kenya est egalement un terrain d'experimentation pour les partenariats US-Kenya en semi-conducteurs : le USTDA a noue un partenariat avec Kenya Semiconductor Technologies Limited pour etablir une installation de fabrication de semi-conducteurs a Nairobi, initiative sans precedent en Afrique subsaharienne.[9]",
    ]),
    ("6quat.2.4 Maroc : le noeud de compute Europe-Afrique", [
        "Le Maroc occupe une position strategique unique : situe a 15 km de l'Europe, connecte par de multiples cables sous-marins, il se positionne comme hub d'export de compute IA plutot que comme marche domestique. En juin 2025, un consortium mene par Naver (Coree du Sud) avec Nvidia a annonce un projet de data center de 500 MW alimente par energies renouvelables, avec une premiere phase de 40 MW equipee de GPU Blackwell GB200. Le Maroc represente environ 35 pour cent de la capacite data center continentale (soit environ 140 MW).[10] L'objectif gouvernemental est ambitieux : 40 milliards de dirhams de revenus en services numeriques avances d'ici 2030, servant principalement des clients europeens et moyen-orientaux. Iozera (Texas) avait deja annonce un investissement de 500 millions USD pour un data center de 386 MW a Tetouan. Le Centre international d'IA affilie a l'Universite Mohammed VI Polytechnique, designe centre UNESCO de categorie II fin 2023, ancre la recherche.",
    ]),
    ("6quat.2.5 Egypte : ambition regionale et strategie gouvernementale", [
        "L'Egypte a adopte l'une des strategies IA les plus structurees du continent, avec un cadre d'evaluation fonde sur trois criteres (faisabilite technologique, impact societal, retour sur investissement). Le pays beneficie de sa position geographique comme point de connexion entre Europe, Afrique et Moyen-Orient via les principales dorsales internet. L'Egypte figure parmi les cinq pays cibles de la AI Factory Cassava/Nvidia (12 000 GPU au total sur trois a quatre ans).[11]",
    ]),
    ("6quat.2.6 Rwanda : le laboratoire IA de l'Afrique", [
        "Le Rwanda se positionne comme le laboratoire IA de l'Afrique (formulation officielle de sa National Policy on AI). Le pays a accueilli en avril 2025 le premier Sommet mondial de l'IA sur l'Afrique a Kigali, reunissant des participants de 40+ pays. Le Rwanda est le seul pays africain a disposer d'une politique nationale IA (distincte d'une strategie). Le Centre for the Fourth Industrial Revolution (C4IR Rwanda), en partenariat avec le WEF, experimente des solutions IA en sante, agriculture, education et services publics. L'initiative Masakhane, hebergee en partie au Rwanda, developpe des modeles NLP pour les langues africaines.[12]",
    ]),
    ("6quat.3 La rivalite US-Chine en Afrique : l'IA comme nouveau terrain de competition", []),
    ("6quat.3.1 L'offensive americaine : Nvidia, Microsoft et le modele AI Factory", [
        "L'engagement americain le plus structurant est le partenariat Cassava Technologies-Nvidia, annonce en mars 2025. Ce projet constitue l'un des plus importants engagements d'infrastructure technologique privee en Afrique : jusqu'a 720 millions USD pour deployer 12 000 GPU Nvidia dans cinq pays (Afrique du Sud, Egypte, Nigeria, Kenya, Maroc) sur trois a quatre ans. Nvidia a ensuite realise un investissement en capital dans Cassava en octobre 2025.[13] Le modele est l'AI-as-a-Service (AIaaS) : rendre les GPU accessibles en location aux startups, universites et gouvernements africains, permettant de contourner partiellement le cout prohibitif d'acquisition directe.",
        "Parallelement, les hyperscalers americains intensifient leur presence : Microsoft (300 millions USD en Afrique du Sud, 1 milliard au Kenya avec G42), Google (37 millions USD specifiquement pour l'IA pour l'Afrique, dans un engagement global de 1 milliard pour la tech africaine). Microsoft a forme plus de 4 millions de jeunes Africains en competences numeriques en cinq ans et s'engage a connecter 124 millions de personnes en Afrique a internet.[14] L'AI Action Plan americain (juillet 2025) integre explicitement l'Afrique dans sa strategie d'exportation du full AI technology stack.",
    ]),
    ("6quat.3.2 La penetration chinoise : Huawei, DeepSeek et les Belt and Road numeriques", [
        "La presence chinoise en Afrique precede de loin la competition IA. Huawei a construit l'essentiel de l'infrastructure telecom du continent dans le cadre des Belt and Road Initiatives et domine 70 pour cent du backbone 4G africain avec des operations dans 30+ marches.[15] Cette base installee confere un avantage structurel considerable pour la couche IA. Huawei deploie desormais des data centers IA integres : en Ethiopie, le FusionModule2000 a ete installe a la Cooperative Bank of Oromia (24,7 milliards USD de transactions digitales), faisant de Huawei le premier a deployer une infrastructure IA operationnelle en Afrique subsaharienne, devant Schneider Electric, Vertiv et Eaton encore en phase pilote.",
        "Le chatbot chinois DeepSeek se repand rapidement au Kenya, ou des startups l'utilisent pour l'analyse economique et l'evaluation des risques d'investissement, a un cout inferieur de 94 pour cent a ChatGPT. Huawei a forme 120 000 Africains et developpe des chaines d'approvisionnement locales.[16] Le FOCAC 2024 (Forum on China-Africa Cooperation) a annonce le developpement d'un centre de cooperation numerique Chine-Afrique et 20 projets d'infrastructure et de transformation numerique. Le parallele avec les Belt and Road physiques est direct : les infrastructures IA chinoises ameliorent l'acces mais creent une dependance technologique et politique.",
    ]),
    ("6quat.3.3 Le double bind africain", [
        "L'Afrique est prise dans un double bind structurel. D'un cote, le protectionnisme americain (classification Tier 2, tarifs 25 pour cent Section 232) restreint l'acces au compute frontier Nvidia. De l'autre, le recours a l'alternative chinoise (Huawei Ascend, DeepSeek) expose a des risques de surveillance, de dependance geopolitique et de sanctions secondaires americaines. Les donnees des utilisateurs de DeepSeek sont stockees sur des serveurs accessibles au gouvernement chinois. Pour les pays africains qui aspirent a maintenir des relations avec les deux blocs, chaque choix d'infrastructure est un choix d'alignement.[17]",
    ]),
    ("6quat.4 Impact du protectionnisme US sur l'Afrique : cinq canaux de transmission", [
        "Le protectionnisme IA americain affecte le continent africain a travers cinq canaux structurels.",
        "Premier canal : la restriction d'acces au compute frontier. La classification Tier 2 impose des plafonds quantitatifs sur les exportations de GPU avances. Pour un continent ou le deficit de compute est deja le plus aigu au monde, ces restrictions exacerbent l'ecart. Les 12 000 GPU du projet Cassava/Nvidia representent un volume modeste compare aux millions de GPU deployes par les hyperscalers americains. L'acces au training de modeles frontier (GPT-5, Claude, Gemini) reste tributaire du cloud US, creant une dependance structurelle.",
        "Deuxieme canal : la bifurcation technologique. Les pays africains incapables d'acceder au compute americain se tournent vers les solutions chinoises. Cette bifurcation est deja visible : les startups kenyanes utilisent DeepSeek et Qwen, l'Ethiopie deploie Huawei, le FOCAC structure la cooperation numerique Chine-Afrique. A terme, deux ecosystemes IA incompatibles pourraient coexister sur le continent, avec des implications en termes d'interoperabilite, de standards et de gouvernance des donnees.[18]",
        "Troisieme canal : l'amplification de la fuite des cerveaux. L'Afrique ne represente que 3 pour cent du talent IA mondial. L'absence de compute local pousse les chercheurs les plus qualifies vers les Etats-Unis, l'Europe ou les Emirats. Le protectionnisme americain, en concentrant le compute frontier sur le sol US, renforce la force gravitationnelle du hub americain pour les talents africains. Le programme Deep Learning Indaba en Afrique du Sud et les initiatives Masakhane tentent de contrer cette tendance, mais la disparite des moyens est considerable.[19]",
        "Quatrieme canal : le risque energetique asymetrique. Le developpement de data centers IA necessite une electricite fiable et abondante. Or, 600 millions d'Africains n'ont toujours pas acces a l'electricite. Les operateurs de data centers comme Raxio (Ouganda, Ethiopie, Mozambique, Cote d'Ivoire, RDC, Angola) doivent investir dans leurs propres lignes electriques et maintenir des generateurs diesel de secours (90 000 litres stockes pour un data center de 1,5 MW).[20] L'avantage geothermique du Kenya et renouvelable du Maroc sont des exceptions, non la regle.",
        "Cinquieme canal : le deficit reglementaire. Seuls 16 pays africains sur 54 avaient lance des strategies IA nationales en juillet 2025. La Strategie continentale IA de l'Union africaine (2025-2030) structure un cadre commun en deux phases, mais l'absence de regulation harmonisee cree un vide que les acteurs exterieurs (US et Chine) exploitent pour imposer leurs standards.[21] Le contraste avec l'AI Act europeen est frappant : la ou l'Europe impose des conditions, l'Afrique subit.",
    ]),
    ("6quat.5 Atouts strategiques et fenetres d'opportunite", [
        "Malgre ces contraintes, l'Afrique dispose d'atouts specifiques que le protectionnisme IA americain pourrait, paradoxalement, valoriser.",
        "Avantage energetique selectif. Le Kenya (geothermie), le Maroc (solaire et eolien), l'Afrique du Sud (nucleaire et renouvelables) et la Cote d'Ivoire (solaire : 37,5 MWp a Boundiali, objectif 45 pour cent renouvelable d'ici 2030) offrent des corridors energetiques competitifs pour les data centers. La puissance de l'energie comme moat pour les data centers est desormais reconnue : McKinsey note que la disponibilite energetique, et non la densite de la demande, determine de plus en plus les decisions d'implantation.[22]",
        "Position de noeud geographique. Le Maroc (15 km de l'Europe, hub EMEA) et l'Egypte (carrefour Europe-Afrique-Moyen-Orient) peuvent devenir des noeuds d'export de compute IA, servant les workloads europeens et moyen-orientaux a cout energetique inferieur. Ce positionnement nearshore est comparable a celui de l'Inde pour les services IT, transpose a l'infrastructure IA.",
        "Diversite linguistique comme opportunite NLP. Avec plus de 1 000 langues parlees, l'Afrique represente un terrain d'innovation unique pour les modeles de traitement du langage naturel. Les projets Masakhane (NLP pour langues africaines) et UlizaLlama developpent des modeles specifiques pour le kinyarwanda, le swahili, le yoruba, le xhosa et le zoulou. Microsoft a engage 5,5 millions USD dans le programme LINGUA Africa.[23]",
        "Marche fintech et donnees mobiles. L'ecosysteme fintech africain (M-Pesa, OPay, Flutterwave) genere des volumes de donnees transactionnelles massifs, exploitables pour l'entrainement de modeles IA specifiques (scoring credit, detection de fraude, inclusion financiere). L'Afrique comptera 2 400+ entreprises specialisees en IA, dont 41 pour cent de startups, et le marche IA continental devrait passer de 4,5 milliards en 2025 a 16,5 milliards en 2030 (croissance annuelle de 27 pour cent).[24]",
    ]),
    ("6quat.6 Scenarios specifiques pour l'Afrique", [
        "L'application de la matrice scenarielle 2x2 (chapitre V) au continent africain genere quatre trajectoires, presentees dans le Tableau 22.",
        "Le scenario S4 (non-alignement numerique) constituerait la reponse africaine la plus adaptee, conjuguant multi-sourcing technologique (Nvidia/Huawei/open-source), souverainete des donnees et developpement de modeles ouverts specifiques (langues africaines, agriculture, sante). Cependant, sa realisation suppose une coherence reglementaire continentale (Strategie UA) et un investissement massif estime a plus de 7 milliards USD pour combler les deficits en donnees, compute et competences. Le scenario S3 (bifurcation imposee) est le plus probable en l'absence d'action coordonnee, reproduisant pour l'IA la dependance telecom deja installee par Huawei.[25]",
    ]),
    ("6quat.7 Synthese : le continent de la derniere chance numerique", [
        "L'Afrique concentre les paradoxes les plus aigus de la recomposition technologique mondiale. Continent le plus deficitaire en compute (moins de 1 pour cent de la capacite mondiale), mais dote du plus fort potentiel demographique (1,4 milliard d'habitants, age median environ 19 ans) et de ressources energetiques strategiques (geothermie, solaire, hydro). Marche le plus convoite par les deux blocs (US et Chine), mais le moins equipe reglementairement pour negocier les conditions de cette competition. Le Tableau 23 synthetise la position africaine en regard du baseline mondial.",
        "Le protectionnisme IA americain agit sur l'Afrique comme un amplificateur d'inegalite numerique. En limitant l'acces au compute frontier pour les pays Tier 2 (quasi-totalite de l'Afrique) tout en concentrant le compute, le talent et l'innovation sur le sol americain, il creuse un ecart deja abyssal. Simultanement, il ouvre un boulevard strategique a la Chine, qui dispose de la base installee (Huawei telecom) et de l'offre alternative (Ascend, DeepSeek) pour capter ce marche.",
        "Pour l'Afrique, l'enjeu n'est pas de choisir entre les Etats-Unis et la Chine, mais de construire une capacite de negociation vis-a-vis des deux. Cela suppose quatre conditions : (i) accelerer la Strategie continentale IA de l'UA (Phase I 2025-2026), (ii) exploiter les corridors energetiques competitifs (geothermie Kenya, solaire Maroc), (iii) investir dans les modeles ouverts specifiques (NLP langues africaines, IA pour l'agriculture et la sante), et (iv) negocier collectivement les conditions d'acces au compute avec les fournisseurs US et chinois, plutot que de subir la competition.",
        "La fenetre d'opportunite est similaire a celle identifiee pour l'Europe (2026-2028) mais les enjeux sont differents : il ne s'agit pas de rattraper un avantage perdu, mais d'eviter qu'un retard structurel ne devienne un enfermement permanent. Comme le resume le New Lines Institute, la collaboration Cassava/Nvidia est moins une question de technologie que de determiner si l'Afrique sera productrice ou simple consommatrice dans l'economie IA mondiale.[26]",
    ]),
]


TABLES = [
    ("Tableau 19. Cartographie des poles IA africains.",
     "Source : compilation de l'auteur (Mordor Intelligence, McKinsey, Cassava Technologies, sources gouvernementales 2025-2026).",
     [
         ["Pole", "DC (nb)", "Investissement cle", "Atout distinctif", "Acteur dominant"],
         ["Afrique du Sud", "56", "MS 300 M USD ; AWS 1,7 Md USD ; Cassava/Nvidia 3 000 GPU", "1er marche DC africain (40,8 pct) ; CAIR ; National AI Strategy", "Hyperscalers US"],
         ["Nigeria", "17-20", "Equinix 100 M USD ; marche DC 288 M USD (2025) vers 1,09 Md USD (2031)", "Population 220 M ; fintech ; cables sous-marins Lagos", "Mix US/local"],
         ["Kenya", "19", "MS+G42 1 Md USD (geothermie 100 MW vers 1 GW) ; IXAfrica", "Geothermie 60 pct+ ; Silicon Savannah ; ZES", "MS / G42 (EAU)"],
         ["Maroc", "~15", "Naver/Nvidia 500 MW ; Iozera 500 M USD ; Cassava AI Factory", "Proximite Europe (15 km) ; renouvelables ; export compute", "Coree / US"],
         ["Egypte", "~12", "Cassava/Nvidia ; hub Moyen-Orient/Afrique", "Strategie IA mature ; position geographique carrefour", "Mix US/Golfe"],
         ["Rwanda", "3-5", "C4IR ; Sommet IA Kigali 2025 ; Masakhane NLP", "Politique IA formelle ; AI lab continental", "Multilateral/WEF"],
     ]),
    ("Tableau 20. Competition US-Chine en Afrique : cartographie des engagements IA.",
     "Source : compilation de l'auteur a partir des annonces officielles 2024-2026.",
     [
         ["Dimension", "Etats-Unis", "Chine"],
         ["Infrastructure",
          "Cassava/Nvidia (720 M USD, 12 000 GPU) ; MS (300 M USD ZA, 1 Md USD Kenya) ; AWS (1,7 Md USD ZA) ; Google (1 Md USD global)",
          "Huawei 70 pct backbone 4G ; DC integres Ethiopie ; 30 marches 5G ; FOCAC 20 projets numeriques"],
         ["Modeles IA",
          "ChatGPT (via cloud US) ; Nvidia AI stack ; OpenAI/Penda Health (reduction 16 pct erreurs diagnostiques Kenya)",
          "DeepSeek (-94 pct cout vs ChatGPT) ; Alibaba Qwen ; Huawei Pangu"],
         ["Talent / Skilling",
          "MS : 1M ZA + 1M Nigeria + 1M Kenya en AI skills ; Google : 100K bourses Ghana ; Intel/AfDB : 3M formes",
          "Huawei : 120K Africains formes ; FOCAC centre numerique Chine-Afrique"],
         ["Strategie",
          "AI Action Plan : export full stack a allies ; US-Africa Tech Collaboration ; BUILD Act vs BRI",
          "BRI numerique ; prix bas ; base installee telecom ; small & beautiful FOCAC 2024"],
     ]),
    ("Tableau 21. Scenarios specifiques pour l'Afrique sous matrice 2x2.",
     "Source : construction de l'auteur, application de la matrice du chapitre V au cas africain.",
     [
         ["", "Reponse africaine passive", "Reponse africaine active"],
         ["Protectionnisme US modere",
          "S1 - Stagnation dependante. Acces limite au compute US ; consommation passive de cloud importe ; brain drain continu ; IA environ 1 pct du PIB africain 2030",
          "S2 - Rattrapage cible. AI Factories operationnelles ; corridors energetiques Kenya/Maroc ; NLP langues africaines ; IA environ 3 pct PIB 2030"],
         ["Protectionnisme US intense",
          "S3 - Bifurcation imposee. Basculement vers ecosysteme chinois ; dependance Huawei/DeepSeek ; fragmentation standards ; risque surveillance",
          "S4 - Non-alignement numerique. Strategie continentale UA ; multi-sourcing US/Chine/open-source ; souverainete donnees ; modeles ouverts locaux"],
     ]),
    ("Tableau 22. Synthese CACI et position africaine.",
     "Source : construction de l'auteur ; baseline US sur snapshot avril 2026 (76,9 pct compute IA operationnel mondial).",
     [
         ["Indicateur", "Afrique (2025)", "US (2025)", "Ratio"],
         ["Capacite DC (GW IT)", "0,78-1,17", "53,7", "x46-69"],
         ["Investissement DC (Md USD)", "~2", "660-690", "x330-345"],
         ["GPU IA (Nvidia)", "12 000 (cible 3-4 ans)", "Plusieurs millions", "x100+"],
         ["Talent IA", "3 pct pool mondial", "~40 pct pool mondial", "x13"],
         ["Marche IA (Md USD)", "4,5 (2025) vers 16,5 (2030)", "~200 (2025)", "x44 (2025)"],
     ]),
]


NOTES = [
    "WEF (decembre 2025), 'Investment in green computing can unlock 1.5T USD in Africa'. Africa Data Centres Association : l'Afrique represente 18 pct de la population mondiale mais moins de 1 pct de la capacite DC mondiale.",
    "WEF (decembre 2025), ibid. 7 millions d'heures GPU de demande non satisfaite ; seuls 5 pct des innovateurs IA ont acces au compute avance.",
    "McKinsey (novembre 2025), 'Building data centers for Africa's unique market dynamics'. Projection 1,5-2,2 GW d'ici 2030. Mordor Intelligence (2026) : marche Africa DC evalue a 1,94 Md USD en 2025.",
    "Cassava Technologies / Bloomberg (avril 2025) : cout GPU Nvidia estime a 45 000-60 000 USD l'unite. Nvidia controle environ 93 pct du marche GPU mondial.",
    "Ecofin Agency (fevrier 2026), 'Huawei Expands Chinese AI-Integrated Data Centre Solutions to Ethiopian Banking Sector'. Huawei premier a deployer IA operationnelle en Afrique subsaharienne. Ainvest/GSMA : Huawei domine 70 pct du backbone 4G africain.",
    "Microsoft (mars 2025), annonce 5,4 Md ZAR d'ici 2027. AWS (2024) : 1,7 Md USD region du Cap. Mordor Intelligence : marche AI DC Afrique du Sud de 70 M USD (2025) a 572 M USD (2031), CAGR 42 pct.",
    "GlobeNewsWire (fevrier 2026), 'Nigeria Data Center Market Investment & Growth Report 2026-2031'. Equinix : 22 M USD pour LG3 Lagos (novembre 2025), plan d'expansion 100 M USD Afrique.",
    "DCD (mai 2024), 'Microsoft and G42 to build geothermal-powered data center in Kenya'. 1 Md USD d'investissement ; DC 100 MW extensible a 1 GW a Olkaria. Reseau kenyan 60 pct+ renouvelable.",
    "Atlantic Council DFRLab / Global Center AI (2025), 'African Countries Are Racing to Create AI Strategies'. Partenariat USTDA-Kenya Semiconductor Technologies.",
    "DCD (juin 2025), 'Naver plans 500MW data center campus in Morocco'. Consortium Naver/Nvidia/Nexus Core/Lloyds Capital. Phase 1 : 40 MW, GPU Blackwell GB200. Research & Markets : capacite DC Afrique environ 400 MW fin 2025, Maroc environ 35 pct.",
    "Carnegie Endowment (septembre 2025), 'Understanding Africa's AI Governance Landscape'. Cassava Technologies : 12 000 GPU dans 5 pays (ZA, Egypte, Nigeria, Kenya, Maroc).",
    "Future of Privacy Forum (2025), 'The African Union's Continental AI Strategy'. Rwanda : seul pays avec politique nationale IA. C4IR Rwanda en partenariat WEF.",
    "Bloomberg (avril 2025), 'Nvidia, Cassava's AI Factory in Africa Tie-Up to Cost 720 Million USD'. TechCabal (octobre 2025) : Nvidia investissement en capital dans Cassava. New Lines Institute (juillet 2025) : plus important engagement infrastructure tech privee en Afrique.",
    "Semafor (juillet 2025), 'Google raises African AI bet' : 37 M USD specifiquement pour IA en Afrique, dans engagement global de 1 Md USD. Microsoft (fevrier 2026) : 124 millions de personnes connectees en Afrique sur 299 millions mondialement.",
    "Rest of World (novembre 2025), 'Huawei pushes AI and cloud into emerging markets after U.S. ban'. Huawei present depuis les annees 1990. Forrester (novembre 2025) : Ascend 910C a une generation des offres US les plus avancees.",
    "Africa Defense Forum (novembre 2025), 'China's DeepSeek Chatbot Expansion in Africa Raises Alarms'. DeepSeek 94 pct moins cher que ChatGPT. Donnees stockees sur serveurs accessibles au gouvernement chinois. Ainvest (aout 2025) : Huawei 120 000 Africains formes.",
    "Africa Defense Forum, ibid. Parallele avec Belt and Road : amelioration d'acces mais dependance financiere et politique. New Lines Institute (2025) : FOCAC Action Plan 2025-2027, 20 projets numeriques.",
    "Rest of World (novembre 2025), ibid. Rebecca Arcesati, Mercator Institute : 'We are seeing a bifurcation of the global AI stack'.",
    "Union africaine (mai 2025), 'Africa Declares AI a Strategic Priority'. 83 pct du financement IA startups en Q1 2025 vers Kenya, Nigeria, Afrique du Sud, Egypte. Seuls 3 pct du talent IA mondial en Afrique.",
    "African Business (decembre 2025), 'Inside the race to fire up Africa's power-hungry data centres'. Raxio Group : 90 000 litres de diesel stockes pour DC 1,5 MW.",
    "Intelpoint (aout 2025) : 16 pays africains sur 54 avec strategie IA nationale. White & Case : Strategie continentale UA Phase I (2025-2026) focus gouvernance + mobilisation ressources.",
    "McKinsey (novembre 2025), ibid. 'Power availability, not demand density, increasingly determines siting decisions.' African Energy Chamber (2025) : Kenya 60 pct+ renouvelable ; Cote d'Ivoire 37,5 MWp solaire Boundiali.",
    "Microsoft LINGUA Africa : 5,5 M USD pour modeles IA langues africaines sous-representees. Mastercard (aout 2025), 'AI in Africa' : plus de 1 000 langues parlees, projets Masakhane et UlizaLlama.",
    "Tech In Africa (octobre 2025), 'North vs. Sub-Saharan Africa : AI Investment Trends'. Marche IA africain de 4,51 Md USD (2025) a 16,53 Md USD (2030), CAGR 27,42 pct. 2 400+ entreprises IA, 41 pct startups.",
    "Carnegie Endowment (2025), ibid. Estimation 7 Md USD+ necessaires pour combler deficits donnees, compute et competences. UA Continental AI Strategy : Phase II (2028) pour implementation projets core.",
    "New Lines Institute (juillet 2025), 'Accelerating U.S.-Africa Tech Collaboration'. Analyse du partenariat Cassava/Nvidia comme modele pour l'engagement technologique US-Afrique.",
]


def build(out_dir: Path) -> Path:
    """Build the FR Chapter VI quater (Africa) .docx."""
    log.info("Building Chapitre VI quater [FR/Africa] -> Chapitre_VI_quater_Afrique_FR.docx")
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
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Chapitre VI quater")

    out = out_dir / "Chapitre_VI_quater_Afrique_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
