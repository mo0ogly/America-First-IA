"""
Chapitre VII - Recommandations strategiques pour la France et l'Europe - FR.

Genere le .docx du Chapitre VII en francais. Articule 5 axes de
recommandations (compute, energie, alliances, regulation, talent) sur
trois horizons (2026-2027, 2027-2029, 2029-2032) plus une synthese
des conditions de succes.

Met a jour les chiffres consolides sur le snapshot avril 2026 :
    - Bandeau couverture : 76,9 / 1,59x / 3,46:1
    - Intro : 76,9 pct compute IA operationnel mondial, CACI Power Mode 3,46:1
    - §7.1.1 : ratios brut UE 17,6:1 et CACI 3,46:1 explicitement cites
    - §7.4 : reference au CACI souverain Phys/Sov (Chap I Fig 1.8)
    - §7.7 Condition 4 : 2028 = point de bascule confirme par Chap V
    - Tableau 23 (anciennement 17) : numerotation continue avec Chap VI

Numerotation des tableaux : continue (Tab 23).

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
from pathlib import Path

from chap7_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("chapitre7_fr")


CHAPTER_LABEL = "CHAPITRE VII"
CHAPTER_TITLE = "Recommandations strategiques pour la France et l'Europe"
CHAPTER_INTRO = (
    "Les chapitres precedents ont etabli que le protectionnisme IA americain cree un avantage "
    "competitif structurel mesurable (CACI Power Mode US/UE de 3,46:1 sur le snapshot avril 2026, "
    "ratio brut compute installe operationnel de 17,6:1), accelere par les tarifs Trump de 2026 "
    "et la concentration du compute aux Etats-Unis (76,9 pct du compute IA operationnel mondial, "
    "660-690 milliards USD de capex annuel des seuls hyperscalers). Ce chapitre formule des "
    "recommandations strategiques articulees en trois horizons temporels et cinq axes structurants, "
    "en s'appuyant sur les avantages comparatifs specifiques de la France (nucleaire, Mistral, "
    "regulation) et les instruments europeens existants (AI Continent Action Plan, Chips Act, "
    "InvestAI)."
)


SECTIONS: list[tuple[str, list[str]]] = [
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
        "Le Tableau 23 ci-apres recapitule les recommandations en croisant trois horizons (2026-2027, 2027-2029, 2029-2032) avec les axes Compute, Energie, et Alliances. Les axes Regulation et Talent se deploient transversalement sur les trois horizons et ne sont pas detailles ligne par ligne dans la matrice.",
    ]),
    ("7.7 Conditions de succes et limites", [
        "Plusieurs conditions determineront l'efficacite de ces recommandations.",
        "Condition 1 : la competitivite de Mistral. L'ensemble de la strategie francaise de souverainete IA repose en partie sur la capacite de Mistral a maintenir des performances competitives face a OpenAI, Anthropic et Google DeepMind. Si l'ecart de capacite se creuse, l'infrastructure francaise servira des besoins de conformite (hebergement souverain de modeles US) plutot que de veritable souverainete technologique.[18] La levee de fonds de 1,7 milliard EUR (evaluation 11,7 milliards) et l'etablissement de Mistral Compute sont des signaux positifs, mais l'echelle de competition (OpenAI : 20 milliards USD de revenus recurrents 2025) reste demesuree.",
        "Condition 2 : l'execution industrielle. Les programmes d'infrastructure IA europeens ont historiquement souffert de retards (EuroHPC, Chips Act). Les 13 AI Factories doivent etre operationnelles, pas simplement annoncees. L'experience du Japon (programme Rapidus 2 nm) et de l'Inde (fosse entre annonces de 200+ milliards et capacite installee de 1,4 GW) illustrent les risques de decalage entre ambition et realisation.",
        "Condition 3 : la coherence europeenne. La fragmentation intra-europeenne (27 regimes energetiques, positions divergentes sur le nucleaire, approches nationales de souverainete concurrentes) reste le principal obstacle. Le scenario C du chapitre V (partenariat asymetrique, baseline 3,46:1 vers 2,0-2,5:1) ne fonctionne pour l'Europe que si elle parle d'une seule voix dans les negociations avec Washington.",
        "Condition 4 : le facteur temps. Le point de basculement identifie au chapitre V (2028, saturation compute plus energie UE, et activation potentielle des Cloud Sovereignty Mandates) impose un calendrier contraint. Si les AI Factories ne sont pas operationnelles et les sites EDF non raccordes a cette date, le gap de compute se solidifiera en dependance structurelle. La fenetre d'action strategique se situe entre 2026 et 2028 - apres quoi les positions se cristallisent autour de la baseline 17,6:1 brut / 3,46:1 CACI Power Mode.",
    ]),
    ("7.8 Conclusion du chapitre", [
        "La France dispose d'un ensemble d'atouts uniques en Europe pour repondre au protectionnisme IA americain : un parc nucleaire incomparable (70 pct de l'electricite, en cours d'extension), un champion IA competitif (Mistral, 11,7 milliards EUR de valorisation, infrastructure compute propre), un ecosysteme cloud souverain en formation (S3NS, Bleu, OVHcloud, Scaleway, OUTSCALE), et une capacite d'attraction d'investissements etrangers (109 milliards EUR en 2025).",
        "Mais ces atouts ne constituent pas une garantie. L'ecart de capex avec les Etats-Unis (660-690 milliards USD annuels contre 200 milliards EUR sur cinq ans), l'ecart de compute (CACI Power Mode 3,46:1 et brut operationnel 17,6:1), et la dependance structurelle aux GPU americaines (Nvidia : 80 pct du marche des accelerateurs IA) definissent le perimetre realiste de l'autonomie atteignable. L'objectif n'est pas l'autarcie technologique - elle est impossible a horizon 2030 - mais une autonomie strategique suffisante pour que le protectionnisme americain ne se traduise pas en dependance irreversible. La distinction Phys/Sov etablie au chapitre I est ici operationnelle : l'Europe est deja largement souveraine sur le compute installe, le travail consiste a securiser la couche des charges cloud avant que les Cloud Sovereignty Mandates 2028 ne transforment cette dependance en levier geopolitique.",
        "Les lecons comparatives sont claires. Le Japon investit 550 milliards USD aux Etats-Unis pour securiser son acces au compute, au prix d'un co-financement de la suprematie americaine. L'Inde promet 200 milliards USD mais ne dispose que de 1,4 GW installe. La Chine, sous restriction maximale, construit un ecosysteme parallele avec un retard de 2-3 generations en GPU mais une capacite reelle (246-300 EFLOP/s) significativement superieure aux 0,5 pct apparents dans les donnees Epoch AI consolidees. Le Bresil hesite entre les deux blocs et risque la fragmentation. L'Afrique cumule l'asymetrie compute la plus extreme (deficit x44 a x417 selon les indicateurs) et le risque de bifurcation imposee. La France, avec son atout nucleaire et Mistral, dispose d'une trajectoire mediane credible : ni alignement total (Japon), ni confrontation (Chine), ni hesitation (Bresil), mais construction methodique d'une autonomie energetique et compute qui garantit la capacite de choix. Le temps pour agir est mesure : la fenetre 2026-2028 est decisive.",
    ]),
]


TABLES = [
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
]


NOTES = [
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
]


def build(out_dir: Path) -> Path:
    """Build the FR Chapter VII (Recommendations) .docx."""
    log.info("Building Chapitre VII [FR] -> Chapitre_VII_Recommandations_FR.docx")
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
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Chapitre VII")

    out = out_dir / "Chapitre_VII_Recommandations_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
