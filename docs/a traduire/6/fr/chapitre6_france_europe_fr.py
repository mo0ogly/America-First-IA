"""
Chapitre VI - Consequences pour la France et l'Europe - generateur FR.

Genere le .docx du Chapitre VI principal en francais. Preserve le contenu
original (analyse sectorielle, differenciation par acteur, effets de second
ordre, ecosysteme France IA, synthese 3 configurations) et met a jour
uniquement les chiffres consolides sur le snapshot avril 2026.

Numerotation des tableaux : continue avec Chap V (Tab 13).

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
log = logging.getLogger("chapitre6_fr_eu")


CHAPTER_LABEL = "CHAPITRE VI"
CHAPTER_TITLE = "Consequences pour la France et l'Europe"
CHAPTER_INTRO = (
    "Les chapitres precedents ont etabli le diagnostic (III), les mecanismes (IV) et les "
    "trajectoires possibles (V). Ce chapitre decline les consequences concretes pour les "
    "acteurs francais et europeens, en distinguant trois niveaux d'analyse : la declinaison "
    "sectorielle (quels secteurs sont les plus exposes ?), la differenciation par type d'acteur "
    "(grands groupes, PME, startups, secteur public), et les effets de second ordre (brain "
    "drain, delocalisation de la R&D, fragmentation normative). L'analyse s'appuie principalement "
    "sur le scenario A (le plus probable) et le scenario B (le plus severe), tout en signalant "
    "les bifurcations propres aux scenarios C et D."
)


SECTIONS: list[tuple[str, list[str]]] = [
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
        "Les PME et entreprises de taille intermediaire representent le tissu industriel francais (4 000 ETI, 140 000 PME). Leur acces a l'IA de pointe est deja contraint par les couts : un entrainement de modele specialise coute plusieurs centaines de milliers d'euros, hors de portee de la plupart des PME sans subvention. McKinsey (decembre 2025) observe que les gains de productivite IA sont concentres dans les grandes entreprises, creant un fosse de productivite intra-europeen entre les entreprises adoptees et les non-adoptees.[6] Sous scenario B, la hausse des couts de compute elargit ce fosse : les PME renoncent a l'IA de pointe et optent pour des solutions degradees (modeles open-source legers, inference locale sur hardware limite), perdant progressivement en competitivite face aux PME americaines qui beneficient du compute domestique exempte de tarifs.",
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
        "Cote vulnerabilites, la France reste structurellement dependante : absence de champion hardware IA (pas de GPU/ASIC design), compute installe limite (environ 5 pour cent du global pour la France seule, ratio US/France de l'ordre de 30:1 - cohérent avec le ratio US/EU(13) brut de 17,6:1 puisque la France represente la majorite du compute UE installe), brain drain post-doctoral vers les US, permitting lent (24+ mois), reseau electrique sous tension (+10 GW necessaires selon RTE), dependance cloud US sur 70-80 pour cent des charges IA, et surcouts de conformite AI Act dans un contexte d'incertitude reglementaire (omnibus 2+ ans).",
    ]),
    ("6.5 Synthese : la France face a trois futurs", [
        "L'analyse de ce chapitre converge vers trois configurations possibles pour la France a l'horizon 2030, correspondant aux trajectoires des scenarios du chapitre V.",
        "Configuration 1 : Consommatrice dependante (scenarios A et B). La France adopte l'IA via le cloud US, gagne en productivite a court terme, mais accumule une dependance structurelle qui la place en position de vulnerabilite face a tout durcissement americain. Les grands groupes prosperent mais sont captifs ; les PME sont progressivement exclues de l'IA de pointe ; les startups les plus prometteuses delocalisent leur infrastructure aux Etats-Unis. Le brain drain s'accelere. L'ecart de productivite avec les Etats-Unis se creuse de 5 a 15 points cumules sur cinq ans.",
        "Configuration 2 : Hub energetique et applicatif (scenario C). La France exploite son avantage nucleaire pour devenir le centre de gravite energetique de l'IA en Europe. Mistral Compute et les Gigafactories fournissent un compute local competitif pour l'inference et le fine-tuning. Les entreprises francaises sont souveraines dans l'application mais dependantes du hardware US. Sur le compute brut, le ratio US/UE descend de 17,6:1 en 2025 vers 8-10:1 en 2030 ; sur le CACI Power Mode, l'ecart se referme de 3,46:1 vers 2,0-2,5:1. Le brain drain est ralenti par l'existence d'un ecosysteme local attractif.",
        "Configuration 3 : Pilier de la souverainete europeenne (scenario D). Le protectionnisme americain catalyse une mobilisation inedite. La France, grace a son nucleaire, ses formations d'excellence et Mistral, devient le pilier d'un effort de souverainete technologique europeen. L'investissement massif (20 GW nucleaire dedie, RISC-V/DARE, alliances Japon-Coree) cree les conditions d'un rattrapage a long terme, mais la periode de transition (2026-2028) est douloureuse. Le risque d'execution est maximal : chaque annee de retard dans les infrastructures prolonge la vulnerabilite.",
        "Le chapitre VII elaborera les recommandations strategiques correspondant a chacune de ces configurations, en distinguant les mesures de court terme (adaptees quel que soit le scenario) des investissements structurels (dependants de la trajectoire choisie).",
    ]),
]


TABLES = [
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
]


NOTES = [
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
]


def build(out_dir: Path) -> Path:
    """Build the FR Chapter VI (France/Europe) .docx."""
    log.info("Building Chapitre VI [FR/EU] -> Chapitre_VI_Consequences_France_Europe_FR.docx")
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
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Chapitre VI")

    out = out_dir / "Chapitre_VI_Consequences_France_Europe_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
