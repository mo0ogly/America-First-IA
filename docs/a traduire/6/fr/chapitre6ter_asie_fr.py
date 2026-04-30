"""
Chapitre VI ter - Consequences pour l'Asie - generateur FR.

Genere le .docx du Chapitre VI ter en francais. Couvre Japon, Taiwan/Coree,
Inde, Chine, ASEAN+Golfe selon le decoupage original. Met a jour le
bandeau couverture sur les valeurs consolidees avril 2026.

Numerotation des tableaux : continue (Tab 18).

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
log = logging.getLogger("chapitre6ter_fr")


CHAPTER_LABEL = "CHAPITRE VI TER"
CHAPTER_TITLE = "Consequences pour l'Asie"
CHAPTER_INTRO = (
    "L'Asie occupe une position unique dans l'architecture du protectionnisme IA americain. "
    "Contrairement a l'Europe (alliee Tier 1 mais dependante) ou a l'Amerique du Sud (Tier 2, "
    "terrain de competition US-Chine), le continent asiatique concentre simultanement : les "
    "cibles principales des restrictions (Chine), les allies industriels critiques de la "
    "chaine de valeur (Japon, Coree du Sud, Taiwan), les candidats Tier 2 les plus ambitieux "
    "(Inde, Asie du Sud-Est), et le rival systemique en voie d'autonomisation (Chine via "
    "Huawei, SMIC, DeepSeek). Ce chapitre analyse les consequences differenciees du "
    "protectionnisme IA americain a travers cinq cas asiatiques structurants."
)


SECTIONS: list[tuple[str, list[str]]] = [
    ("6ter.1 Japon : allie strategique et co-investisseur", []),
    ("6ter.1.1 Le partenariat US-Japon en infrastructure IA", [
        "Le Japon illustre le modele de l'allie Tier 1 integre dans l'ecosysteme americain. En 2025-2026, le Japon a conclu avec les Etats-Unis un accord d'investissement de 550 milliards USD en infrastructure IA, energie et semi-conducteurs sur le sol americain, dont 332 milliards pour l'infrastructure energetique (centrales, reseaux de transmission) et le reste pour les semi-conducteurs et les data centers.[1] Mitsubishi Electric contribue a hauteur de 30 milliards USD en systemes d'alimentation pour data centers, TDK 25 milliards en modules de puissance, et Fujikura fournit les cables optiques. Le Japon emet 1 780 milliards de yens en obligations speciales pour financer les investissements japonais aux Etats-Unis dans le cadre de l'accord commercial bilateral.[2]",
        "Parallelement, le Japon investit massivement dans son propre ecosysteme IA. Le gouvernement a engage 10 000 milliards de yens (65 milliards USD) pour l'IA et les semi-conducteurs d'ici 2030, avec 330 milliards USD d'investissements public-prive projetes sur la decennie.[3] Le budget METI pour l'exercice 2026 atteint 1 230 milliards de yens (7,9 milliards USD), quasi-quadruple par rapport aux niveaux precedents, dont 387,3 milliards de yens pour les modeles fondation domestiques et l'infrastructure, et 150 milliards de yens pour Rapidus, le projet national de fonderie de puces 2 nm a Hokkaido.",
    ]),
    ("6ter.1.2 Avantages et risques du statut d'allie privilegie", [
        "Le Japon beneficie d'un acces illimite aux GPU americaines (Tier 1) et d'investissements massifs des hyperscalers US : Microsoft (2,9 milliards USD sur deux ans), AWS (15,2 milliards USD d'ici 2027), Google (730 millions USD incluant le premier data center dedie de Google au Japon).[4] Le marche japonais des data centers est le troisieme mondial, evalue a 12,76 milliards USD en 2025, projete a 38,92 milliards d'ici 2031 (croissance annuelle de 20,4 pour cent). SoftBank engage plus de 40 milliards USD via le projet Stargate (partenariat avec OpenAI), et le secteur prive japonais (NEC, Fujitsu, NTT, Sakura Internet) developpe des LLM domestiques (Sarashina, Cotomi, Tsuzumi).",
        "Cependant, le statut d'allie privilegie comporte un risque analogue au scenario C europeen (partenariat asymetrique). L'accord de 550 milliards USD represente un transfert massif de capital japonais vers les Etats-Unis, financement qui pourrait alternativement servir a construire l'infrastructure IA domestique. Le Japon devient co-financeur de la suprematie compute americaine tout en accelerant son propre ecosysteme - une dualite qui n'est soutenable que tant que le partenariat reste benefique aux deux parties. De plus, malgre les efforts de Rapidus, le Japon reste dependant de TSMC pour la fabrication de puces de pointe et de Nvidia/AMD pour les accelerateurs IA.",
    ]),
    ("6ter.2 Taiwan et Coree du Sud : maillons critiques et otages geopolitiques", []),
    ("6ter.2.1 Taiwan : le silicon shield sous pression", [
        "Taiwan occupe la position la plus critique de la chaine de valeur IA mondiale. TSMC fabrique environ 90 pour cent des puces de pointe (noeuds inferieurs a 7 nm), dont la totalite des GPU Nvidia et AMD. Cette concentration extreme confere a Taiwan un silicon shield (bouclier de silicium) : une protection geopolitique de facto car aucun acteur mondial ne peut se permettre de perturber la production. Mais ce meme positionnement fait de Taiwan un otage strategique : les Etats-Unis exigent la diversification de la production (TSMC Arizona, usine de 40 milliards USD, production prevue 2025-2026 sur le noeud 4 nm puis 2 nm), tandis que la Chine exerce une pression militaire croissante.[5]",
        "Le protectionnisme americain a des effets contradictoires sur Taiwan. D'un cote, les restrictions d'export vers la Chine reduisent les revenus de TSMC (la Chine representait environ 10 pour cent du chiffre d'affaires avant les restrictions). De l'autre, la demande americaine de chips IA explose, compensant largement les pertes chinoises. Le CHIPS Act americain et les tarifs Section 232 creent une pression pour que TSMC transfere une part croissante de sa production aux Etats-Unis, ce qui a terme pourrait eroder l'avantage competitif de Taiwan lui-meme. Taiwan est classe Tier 1 et ne souffre pas de restrictions sur les GPU, mais son modele economique fonde sur la fabrication de pointe est paradoxalement menace par le rapatriement americain de cette meme fabrication.",
    ]),
    ("6ter.2.2 Coree du Sud : semiconducteurs memoire et IA", [
        "La Coree du Sud, via Samsung Electronics et SK hynix, domine le marche mondial de la memoire avancee (DRAM, HBM - High Bandwidth Memory), composant critique des GPU IA. SK hynix fournit l'essentiel de la HBM pour les GPU Nvidia H100/H200/Blackwell. Le budget national IA 2026 de la Coree atteint 9 900 milliards de wons (environ 6,7 milliards USD), dont pres de la moitie dediee a l'infrastructure.[6]",
        "La Coree, comme le Japon, est classee Tier 1 et beneficie d'un acces libre. Mais les restrictions vers la Chine impactent significativement Samsung et SK hynix, qui avaient d'importantes operations de production en Chine. Samsung opere deux usines de memoire et une usine NAND a Xi'an, tandis que SK hynix a des capacites DRAM a Dalian et Wuxi. Les restrictions americaines limitent les mises a jour technologiques de ces usines, les confinant progressivement a des noeuds moins avances. L'Affiliates Rule, suspendue jusqu'en novembre 2026, menace d'etendre ces restrictions a d'autres entites. Le protectionnisme americain pousse Samsung et SK hynix a investir davantage aux Etats-Unis (Samsung : usine de 17 milliards USD au Texas ; SK hynix : emballage HBM en Indiana), accelerant le transfert industriel vers le territoire americain.",
    ]),
    ("6ter.3 Inde : la troisieme voie du compute souverain", []),
    ("6ter.3.1 Ambitions massives et fosse structurel", [
        "L'Inde s'est positionnee comme le porte-drapeau du Sud global pour l'IA lors du India AI Impact Summit de fevrier 2026 a New Delhi, accueillant pres de 20 chefs d'Etat ainsi que les PDG de Google, OpenAI et Anthropic. Les annonces d'investissement depassent 200 milliards USD sur deux ans, principalement du secteur prive : Reliance/Jio (110 milliards USD sur sept ans, data centers multi-GW a Jamnagar, premiers 120 MW en ligne au second semestre 2026), Tata Group (data centers IA de 100 MW a 1 GW, avec OpenAI comme premier locataire), et le groupe Adani (energie renouvelable pour data centers).[7]",
        "Mais le fosse entre ambition et realite reste considerable. La capacite installee de data centers en Inde est d'environ 1,4 GW (2025), contre 53,7 GW aux Etats-Unis et 19,6 GW en Chine. L'IndiaAI Mission, dotee de 10 372 crores de roupies (environ 1,2 milliard USD sur cinq ans), a deploye 38 000 GPU a acces subventionne, avec 20 000 GPU supplementaires annonces.[8] Pour comparaison, Baidu seul a annonce un cluster de 30 000 GPU en 2025, et la capacite nationale de compute IA de la Chine atteignait environ 246 EFLOP/s a mi-2024. L'investissement public indien, bien que significatif dans le contexte national, represente ce que les grandes entreprises americaines depensent en quelques mois.",
    ]),
    ("6ter.3.2 Classification Tier 2 et strategie de contournement", [
        "Comme le Bresil, l'Inde est classee Tier 2, soumise aux caps quantitatifs de GPU. Brookings identifie l'Inde, avec le Bresil, comme l'un des pays Tier 2 les plus defavorises par les restrictions.[9] Cependant, l'Inde adopte une strategie de contournement sophistiquee : elle se positionne comme exportatrice de compute. Le budget 2026 introduit un cadre fiscal a zero impot jusqu'en 2047 pour les services cloud exportes depuis des data centers indiens.[10] L'idee est d'attirer les hyperscalers americains a construire sur le sol indien pour servir le marche indien et les marches voisins, contournant ainsi les caps d'import de GPU en hebergeant le compute US localement.",
        "Cette strategie rejoint la troisieme voie que revendique l'Inde : cooperer avec les Etats-Unis (acces aux GPU, partenariats OpenAI/Google/Microsoft) tout en construisant des capacites souveraines (IndiaAI Mission, modeles domestiques comme BharatGen) et en amplifiant la voix du Sud global. Le risque est le meme que pour le scenario C europeen : une souverainete applicative sans souverainete hardware, puisque l'Inde reste entierement dependante des GPU americaines et que ses projets de fabrication de semi-conducteurs (India Semiconductor Mission, 10 milliards USD d'incitations) ne produiront pas de puces IA de pointe avant 2028-2030.",
    ]),
    ("6ter.4 Chine : l'autonomisation forcee", []),
    ("6ter.4.1 Impact et adaptation", [
        "La Chine est la cible principale et directe du protectionnisme IA americain (Tier 3, acces interdit aux GPU avancees depuis octobre 2022, etendu en 2023 et 2024). Les resultats sont ambivalents. D'un cote, les restrictions ont ralenti l'acces de la Chine au compute de pointe : les GPU Nvidia H100/H200/Blackwell sont interdites, le chip degrade H20 a necessite une licence speciale (approuvee en juillet 2025), et plus de 65 entites chinoises ont ete ajoutees a l'Entity List en 2025.[11]",
        "De l'autre, la Chine a accelere sa course a l'autonomisation avec des resultats notables. Huawei a developpe l'Ascend 910c (performances approchant le Nvidia H100, a 60-70 pour cent du cout selon les analystes) et poursuit le 910d. SMIC, bien que privee d'acces aux machines EUV d'ASML, progresse vers la fabrication en 5 nm. DeepSeek-V3, modele chinois de langage, a atteint des performances competitives sur les benchmarks mondiaux malgre les contraintes de compute.[12] La Chine a investi plus de 125 milliards USD en infrastructure IA en 2025, vise 70 milliards supplementaires en data centers pour 2026, et projette 300 EFLOP/s de capacite de calcul IA avec plus de 250 installations dediees. La part chinoise de la capacite mondiale de fonderies devrait passer de 21 pour cent a 30 pour cent d'ici 2030, depassant Taiwan.[13]",
        "Note importante : le ratio brut US/Chine apparent dans le tableau de bord public d'avril 2026 (US 76,9 pour cent operationnel, Chine 0,5 pour cent F_total) sous-represente significativement la capacite chinoise reelle. Epoch AI ne capture qu'une fraction des clusters chinois (anonymisation, opacite des fournisseurs Huawei/Cambricon/Biren), et la capacite annoncee de 246-300 EFLOP/s suggere un ratio reel beaucoup plus proche de 5-10:1 que des 150:1 implicites dans les donnees publiquement consolidees.",
    ]),
    ("6ter.4.2 Le paradoxe strategique pour les Etats-Unis", [
        "Le cas chinois revele un paradoxe fondamental du protectionnisme IA americain. En limitant l'acces de la Chine aux GPU, les Etats-Unis ont accelere (plutot que freine) la construction d'une chaine de valeur IA chinoise alternative. Comme le note l'ITIF, les restrictions poussent des concurrents a combler le fosse : Huawei, Biren Technology, MetaX et Enflame innovent dans la conception de puces IA.[14] Le resultat a moyen terme pourrait etre l'emergence d'un deuxieme ecosysteme IA mondial completement independant de la technologie americaine, creant les conditions d'une bifurcation technologique permanente. Ce deuxieme ecosysteme est precisement celui qui s'exporte vers le Bresil (ByteDance a Pecem), l'Asie du Sud-Est (ByteDance en Malaisie et Thailande), et l'Afrique, creant la fragmentation technologique mondiale analysee dans les chapitres precedents.",
    ]),
    ("6ter.5 Asie du Sud-Est et Golfe : les nouveaux terrains de competition", []),
    ("6ter.5.1 Singapour, Malaisie, Thailande : le corridor IA de l'ASEAN", [
        "L'Asie du Sud-Est est classee Tier 2 et represente un terrain de competition croissante entre investissements US et chinois en infrastructure IA. Singapour, malgre ses contraintes de taille et d'energie (environ 1 GW de capacite DC), s'est etabli comme hub regional grace a sa stabilite reglementaire et ses investissements en R&D (5 milliards de dollars singapouriens pour l'IA). La Malaisie est devenue un point chaud : ByteDance y investit 2,1 milliards USD dans un hub IA, tandis que Microsoft, Google et AWS y deploient des data centers.[15] La Thailande a recu 8,8 milliards USD de ByteDance pour des data centers. Ces investissements chinois creent en Asie du Sud-Est une concentration d'infrastructure IA chinoise qui pourrait susciter des restrictions secondaires americaines a terme.",
    ]),
    ("6ter.5.2 Emirats et Arabie Saoudite : compute comme diversification economique", [
        "Les Etats du Golfe representent un cas different : des pays Tier 2 a tres haute capacite d'investissement, pour lesquels l'IA est un instrument de diversification post-petrole. Les Emirats arabes unis developpent le plus grand campus IA hors des Etats-Unis (26 km2, 5 GW prevus, Abu Dhabi). L'Arabie Saoudite a annonce plus de 15 milliards USD de nouveaux investissements IA au LEAP 2025, dont 10 milliards via un partenariat PIF-Google Cloud et 500 MW chacun de puces AMD et Nvidia via son initiative HUMAIN.[16] L'administration Trump a assoupli les restrictions vers le Moyen-Orient, reconnaissant le potentiel d'alliance strategique et financier. Ces pays Tier 2 deviennent ainsi des partenaires financiers de l'ecosysteme IA americain (le fonds MGX d'Abu Dhabi a co-investi dans Mistral AI), une dynamique de compute-for-capital qui transforme le protectionnisme en un levier de financement de l'infrastructure US.",
        "Le cas des EAU illustre quantitativement cette dynamique : la Fig 1.8 du chapitre I a documente que 99,6 pour cent du F_total des EAU (22,9 millions d'equivalents H100) est detenu par des acteurs US-side (Stargate UAE, Microsoft, OpenAI), faisant s'effondrer le CACI souverain de 55,7 (Physique) a seulement 6,0 (Souverain). Cette distinction entre compute physiquement present et compute legalement controlable est centrale pour comprendre la pseudo-souverainete des hubs du Golfe.",
    ]),
    ("6ter.6 Synthese comparative Asie", [
        "Le Tableau 18 synthetise les positions relatives des principaux acteurs asiatiques face au protectionnisme IA americain.",
    ]),
    ("6ter.7 Le reequilibrage geopolitique asiatique de l'IA", [
        "L'analyse de l'Asie revele que le protectionnisme IA americain produit un reequilibrage geopolitique profond, articule autour de trois dynamiques.",
        "Dynamique 1 : Consolidation de l'alliance technologique US-Japon-Coree-Taiwan. Les allies Tier 1 asiatiques ne sont pas simplement des beneficiaires passifs. Ils deviennent des co-investisseurs massifs dans l'infrastructure US (Japon : 550 milliards, Samsung/SK hynix : dizaines de milliards en usines americaines), tout en accelerant leur propre ecosysteme. Cette alliance est structurellement plus integree que le partenariat US-Europe, car le Japon et la Coree controlent des segments critiques de la chaine de valeur (memoire HBM, equipements, materiaux) que les Etats-Unis ne peuvent pas facilement substituer.",
        "Dynamique 2 : Emergence d'un ecosysteme IA chinois independant. Contrairement a ce que prevoyaient les architectes des export controls, les restrictions n'ont pas neutralise la capacite d'innovation IA chinoise. DeepSeek, Huawei Ascend, et les investissements massifs en infrastructure (125 milliards USD en 2025) montrent que la Chine construit un ecosysteme parallele. Le retard en GPU de pointe (environ 2-3 generations) est partiellement compense par l'optimisation logicielle, les architectures alternatives et l'acces au marche interieur (1,4 milliard d'utilisateurs). Cet ecosysteme s'exporte en Amerique du Sud (chapitre VI bis), en Asie du Sud-Est et en Afrique.",
        "Dynamique 3 : L'Inde comme pivot du Sud global. L'AI Impact Summit 2026 a consacre l'Inde comme le pont entre les economies avancees et le Sud global. Avec 200+ milliards USD d'engagements, 1,4 milliard d'habitants, un vivier de talent technique et une strategie de compute comme export, l'Inde se positionne pour capter une part significative de l'infrastructure IA mondiale. Cependant, sa classification Tier 2 cree une tension fondamentale avec cette ambition : les caps de GPU limitent la capacite de l'Inde a construire l'infrastructure qu'elle projette. La resolution de cette tension - promotion au Tier 1, VEU (Validated End User) pour les groupes indiens, ou construction d'alternatives non-US - sera l'un des points de bifurcation majeurs de la geopolitique IA 2026-2030.",
        "Pour l'Europe et la France (objet principal de cette etude), les dynamiques asiatiques creent a la fois des opportunites et des risques. Opportunites : alliances technologiques avec le Japon et la Coree (l'investissement d'ASML dans Mistral, le partenariat TSMC-Dresde), acces aux marches indiens et sud-est asiatiques pour les solutions IA europeennes. Risques : si le bloc US-Japon-Coree-Taiwan se consolide en un ecosysteme ferme, l'Europe pourrait etre marginalisee comme alliee technologique de second rang, d'autant que les investissements japonais massifs aux Etats-Unis accelerent la concentration du compute americain que l'Europe cherche precisement a reduire.",
    ]),
]


TABLES = [
    ("Tableau 18. Synthese comparative de la position asiatique face au protectionnisme IA americain.",
     "Source : compilation de l'auteur, calibration sur baseline avril 2026.",
     [
         ["Pays/Region", "Tier", "Cap. DC (GW) 2025", "Invest. IA (Md USD)", "Atout principal", "Risque principal"],
         ["Japon", "1", "~12,8", "135 (public+prive)", "Alliance US + industrie + R&D", "Co-financement US + dependance GPU"],
         ["Taiwan", "1", "~3", "N/A (producteur)", "TSMC 90 pct chips pointe", "Transfert production vers US + pression Chine"],
         ["Coree du Sud", "1", "~5", "6,7 (budget 2026)", "HBM (SK hynix) + Samsung", "Usines Chine gelees + transfert US"],
         ["Inde", "2", "~1,4", "200+ (2 ans)", "Marche 1,4 Md hab. + talent", "Fosse compute + Tier 2 caps"],
         ["Chine", "3", "~19,6", "125+ (2025)", "Autonomisation forcee", "Retard GPU + isolement technologique"],
         ["ASEAN", "2", "~3", "15+ (US+CN combine)", "Couts bas + position geographique", "Bifurcation US-Chine"],
         ["Golfe", "2 (vers 1 ?)", "~2", "15+ (Arabie) + 5 GW (EAU)", "Capital souverain massif", "Dependance technologique + eau/energie + sov. illusoire (EAU 99,6 pct US-side)"],
     ]),
]


NOTES = [
    "Construction Today (novembre 2025), 'Billion-Dollar AI Build Begins as Japan Backs US Data and Energy Push'. Accord US-Japon : 550 Md USD, dont 332 Md USD energie, Bechtel et Kiewit maitres d'oeuvre.",
    "Taipei Times (decembre 2025). Obligations speciales japonaises de 1 780 Md JPY via NEXI. Mitsubishi Electric : 30 Md USD, TDK : 25 Md USD, Fujikura : cables optiques.",
    "The Economy (novembre 2025), 'Japan Revives State-Led Growth Strategy'. 66 Md USD fonds publics IA/semiconducteurs d'ici 2030, 330 Md USD public-prive sur la decennie. METI budget 2026 : 1 230 Md JPY.",
    "Introl Blog (aout 2025), 'Japan 135B USD AI Push'. Microsoft : 2,9 Md USD ; AWS : 15,2 Md USD d'ici 2027 ; Google : 730 M USD incl. DC dedie Inzai. SoftBank : 40 Md USD via Stargate. Arizton : marche DC Japon 12,76 Md USD (2025) vers 38,92 Md USD (2031).",
    "TSMC Arizona : usine de 40 Md USD, production prevue 2025-2026 (4 nm), extension 2 nm. Samsung Austin : usine de 17 Md USD. Donnees : sources multiples industrielles.",
    "Futurum (fevrier 2026), 'AI Capex 2026 : The 690B USD Infrastructure Sprint'. Budget national IA Coree 2026 : 9 900 Md KRW (~6,7 Md USD).",
    "IBTimes India (fevrier 2026), 'India's AI Awakening'. Reliance : 110 Md USD sur 7 ans ; Tata : DC 100 MW-1 GW avec OpenAI ; Adani : energie renouvelable pour DC. Total : 310+ Md USD.",
    "Medium / Durgesh Kumar (fevrier 2026). IndiaAI Mission : 10 372 crores roupies, 38 000 GPU + 20 000 annonces, subvention 65 INR/heure. Mind2Markets (fevrier 2026) : capacite DC Inde 1,4 GW, US 53,7 GW, Chine 19,6 GW.",
    "Brookings (janvier 2025), op. cit. Inde et Bresil : plus grands marches Tier 2, mais caps insuffisants.",
    "Constellation Research (fevrier 2026), 'Compute as an Export : India's Strategy'. Budget 2026 : cadre zero-impot jusqu'en 2047 pour services cloud exportes depuis l'Inde.",
    "Introl Blog (janvier 2026), 'AI Export Controls : Navigating Chip Restrictions Globally'. H100/H200/Blackwell interdits Tier 3. 65+ entites ajoutees Entity List en 2025.",
    "EastPost (fevrier 2026), 'India's AI Impact Summit Highlights Broad Gaps'. DeepSeek-V3 : performances competitives sous contraintes. Chine : 246 EFLOP/s mi-2024, objectif 300 EFLOP/s. Huawei Ascend 910c : ~H100 a 60-70 pct du cout.",
    "IBTimes India (fevrier 2026), op. cit. Chine : 125 Md USD infrastructure IA 2025, 70 Md USD DC 2026, 300 EFLOP/s, 250+ installations. Tom's Hardware (2025) : part fonderies Chine 21 pct vers 30 pct (2030).",
    "ITIF (mai 2025), 'Overly Stringent Export Controls Chip Away at US AI Leadership'. Huawei Ascend, Biren, MetaX, Enflame : chaine de valeur alternative en construction.",
    "ByteDance : 2,1 Md USD Malaisie (hub IA), 8,8 Md USD Thailande (data centers). Microsoft, Google, AWS : regions cloud en Malaisie, Singapour, Indonesie.",
    "Futurum (fevrier 2026), op. cit. Arabie Saoudite : 15 Md USD LEAP 2025, 10 Md USD PIF-Google Cloud, HUMAIN 500 MW AMD + 500 MW Nvidia. EAU : campus 26 km2, 5 GW, Abu Dhabi. Voir aussi chapitre I Fig 1.8 pour la decomposition Phys/Sov des EAU (99,6 pct US-side).",
]


def build(out_dir: Path) -> Path:
    """Build the FR Chapter VI ter (Asia) .docx."""
    log.info("Building Chapitre VI ter [FR/Asia] -> Chapitre_VI_ter_Asie_FR.docx")
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
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Chapitre VI ter")

    out = out_dir / "Chapitre_VI_ter_Asie_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
