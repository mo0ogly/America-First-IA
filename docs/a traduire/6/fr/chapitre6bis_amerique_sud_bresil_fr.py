"""
Chapitre VI bis - Consequences pour l'Amerique du Sud et le Bresil - FR.

Genere le .docx du Chapitre VI bis en francais. Preserve l'analyse
originale (position structurelle Sud global, Bresil hub emergent,
megaprojets US/Chine, scenarios A'-D', triple fracture) et met a jour
les chiffres consolides sur le snapshot avril 2026.

Numerotation des tableaux : continue avec Chap VI principal (Tab 16, 17).

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
log = logging.getLogger("chapitre6bis_fr")


CHAPTER_LABEL = "CHAPITRE VI BIS"
CHAPTER_TITLE = "Consequences pour l'Amerique du Sud et le Bresil"
CHAPTER_INTRO = (
    "L'analyse des chapitres precedents s'est concentree sur l'axe transatlantique US-Europe. "
    "Or, les consequences du protectionnisme IA americain s'etendent bien au-dela de l'OCDE. "
    "L'Amerique du Sud, et le Bresil en particulier, constituent un cas d'etude revelateur : "
    "a la fois marche dynamique pour l'IA, terrain de competition geopolitique US-Chine, et "
    "region structurellement dependante du compute etranger tout en disposant d'atouts "
    "energetiques uniques. Ce chapitre complementaire analyse les consequences specifiques "
    "du regime protectionniste sur l'Amerique du Sud, avec un focus approfondi sur le Bresil."
)


SECTIONS: list[tuple[str, list[str]]] = [
    ("6bis.1 Position structurelle : le Sud global face a l'asymetrie de compute", []),
    ("6bis.1.1 Un ecosysteme en croissance rapide mais structurellement dependant", [
        "L'Amerique latine represente 6,6 pour cent du PIB mondial, mais n'attire que 1,12 pour cent de l'investissement mondial en IA - un ratio de 5,9 qui mesure le deficit d'investissement de la region.[1] Pourtant, les indicateurs d'adoption sont remarquablement dynamiques. L'indice latino-americain de l'intelligence artificielle (ILIA 2025), publie par la CEPALC et le CENIA chilien, classe trois pays comme pionniers (Chile, Bresil, Uruguay), huit comme adoptants (dont Colombie, Equateur, Costa Rica), et un tiers comme explorateurs avec des ecosystemes naissants.[2] La region represente 14 pour cent des visites mondiales de solutions IA et se classe troisieme mondiale pour les telechargements d'applications d'IA generative.",
        "Cette dynamique d'adoption contraste avec un deficit infrastructurel considerable. Les pays a revenu eleve hebergent 77 pour cent de la capacite mondiale de data centers en colocation (juin 2025), contre 18 pour cent pour les pays a revenu intermediaire superieur et 5 pour cent pour les pays a revenu intermediaire inferieur.[3] Les pays a haut revenu concentrent egalement 87 pour cent des modeles IA notables, 86 pour cent des startups IA et 91 pour cent du capital-risque IA, alors qu'ils ne representent que 17 pour cent de la population mondiale. L'Amerique latine se situe dans la categorie intermediaire : consommatrice dynamique d'IA, mais quasi-entierement dependante de l'infrastructure etrangere (americaine et, de plus en plus, chinoise) pour le compute.",
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
        "Le Chili, classe pionnier par l'ILIA 2025, beneficie de temperatures favorables (reduction de la consommation energetique de refroidissement) et d'un ecosysteme de gouvernance IA avance. Microsoft a lance en juin 2025 Chile Central, sa premiere region cloud dans le pays, associee au programme Transforma Chile (180 000 personnes formees, 81 000 emplois crees). Mais le Chili reste entierement dependant du hardware et du cloud americain, sans l'alternative chinoise dont dispose le Bresil.",
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
]


TABLES = [
    ("Tableau 16. Principaux projets de data centers IA au Bresil (2025-2030).",
     "Source : compilation de l'auteur a partir de Bloomberg, IndustrialInfo, Introl.",
     [
         ["Projet", "Origine", "Investissement", "Capacite", "Caracteristique"],
         ["TikTok Pecem", "Chine", "~38 Md USD", "300 MW vers 1 GW", "100 pct eolien ; 1er projet LATAM ByteDance"],
         ["Scala AI City", "Bresil/US", "Multi-Md USD", "1,8 vers 5 GW", "Plus grande installation planifiee Am. du Sud"],
         ["Elea Rio AI City", "Bresil/US", "Multi-Md USD", "1,8 vers 3,2 GW", "Oracle + Nvidia partenaires technologiques"],
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
]


NOTES = [
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
]


def build(out_dir: Path) -> Path:
    """Build the FR Chapter VI bis (South America/Brazil) .docx."""
    log.info("Building Chapitre VI bis [FR/LATAM] -> Chapitre_VI_bis_Amerique_Sud_Bresil_FR.docx")
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
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Chapitre VI bis")

    out = out_dir / "Chapitre_VI_bis_Amerique_Sud_Bresil_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
