"""
Conclusion generale FR - generateur.

Genere le .docx de la conclusion generale de la these en francais.

Met a jour les chiffres consolides sur le snapshot avril 2026 :
    - Bandeau couverture : 76,9 / 1,59x / 3,46:1
    - §2.1 : ratio brut UE 17,6:1, CACI Power Mode 3,46:1, 76,9 pct compute IA op.
    - §2.2 troisieme etage : Cloud Sovereignty Mandates 2028 ajoutes
    - §2.3 Tableau 24 (anciennement 18) : Afrique ajoutee + ratios consolides
    - §4 Limites : retrait de "Afrique absente" (couverture VI quater)
    - §5 : reference explicite Cloud Sovereignty Mandates 2028 + Phys/Sov
    - Tableau 25 (anciennement 19) : recapitulatif 11 chapitres (incl. VI quater)

Numerotation des tableaux : continue (Tab 24, Tab 25).

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
from pathlib import Path

from concl_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("conclusion_fr")


CHAPTER_LABEL = "CONCLUSION GENERALE"
CHAPTER_TITLE = "Du protectionnisme IA a la recomposition de l'ordre technologique mondial"
CHAPTER_INTRO = (
    "Cette conclusion synthetise les resultats de l'etude conduite sur la periode 2022-2026, "
    "valide l'hypothese centrale d'un regime protectionniste IA americain, expose les "
    "contributions a la litterature, identifie les limites et pistes de recherche, et "
    "argumente l'enjeu de civilisation que represente le compute IA comme quatrieme facteur "
    "de production. Elle se cloture par le tableau recapitulatif des onze chapitres et "
    "l'inventaire des sources principales mobilisees."
)


SECTIONS: list[tuple[str, list[str]]] = [
    ("1. Validation de l'hypothese centrale", [
        "Cette etude partait d'une hypothese precise : l'administration Trump 2.0 transformerait les controles a l'export Biden en un regime protectionniste plus large, utilisant le compute IA comme instrument de puissance economique et geopolitique - un decret implicite AI for Americans First. L'analyse empirique conduite sur la periode 2022-2026 valide cette hypothese de maniere substantielle.",
        "Le 15 janvier 2026, l'administration Trump a simultanement promulgue un tarif de 25 pour cent (Section 232) sur les semi-conducteurs IA avances (Nvidia H200, AMD MI325X) pour les reexportations vers la Chine, et publie la regle finale BIS regissant les exportations de puces IA. La combinaison tarifs plus controles a l'export constitue precisement le mecanisme hybride que nous anticipions : une taxe sur l'acces au compute de pointe qui genere des revenus pour le Tresor americain tout en ralentissant les concurrents, combinee a un acces domestique illimite qui renforce l'avantage competitif des Big Tech US.[1]",
        "Plus encore, l'AI Action Plan de juillet 2025 formalise une doctrine qui depasse les simples controles de securite nationale : exporter le stack IA complet (hardware, modeles, logiciels, applications et standards) aux pays disposes a rejoindre l'alliance IA americaine, sous condition de conformite aux exigences de securite US.[2] L'IA n'est plus traitee comme une technologie parmi d'autres, mais comme un instrument de projection de puissance analogue au dollar dans le systeme monetaire ou au petrole dans le systeme energetique.",
    ]),
    ("2. Synthese des resultats", []),
    ("2.1 Un avantage competitif americain mesurable et croissant", [
        "L'indice CACI (Compute-Adjusted Competitive Index) developpe dans cette etude permet de quantifier l'asymetrie structurelle. Sur le snapshot du tableau de bord public d'avril 2026, le ratio brut compute installe operationnel US/UE(13) s'etablit a 17,6:1, traduit par une formule geometrique ponderee F^0,40 x L^0,20 x R^0,15 / E^0,25 en un ratio CACI Power Mode de 3,46:1. La concentration de 76,9 pour cent du compute IA operationnel mondial aux Etats-Unis (49,9 pour cent en incluant les capacites planifiees), un capex annuel des hyperscalers de 660-690 milliards USD (superieur au PIB de la Suede), et un cout de training des modeles frontier 5 a 10 fois inferieur au cout europeen confirment cette domination. L'avantage est auto-renforcant : les entreprises disposant d'un acces abondant au compute captent des rentes d'innovation et de donnees qui sont tres difficiles a rattraper ensuite (chapitre IV).",
        "Une nuance methodologique importante issue du chapitre I (Fig 1.8) : la decomposition Phys/Sov rigoureusement calculee a partir du champ Owner d'Epoch AI revele que l'asymetrie est differenciee selon les juridictions. Les Etats-Unis et la Chine sont integralement souverains sur leur compute installe (CACI Phys = CACI Sov). L'UE est aussi tres largement souveraine sur son F installe (99,2 pour cent UE-owned). Le cas extreme est celui des Emirats arabes unis : 99,6 pour cent du F_total emirati est detenu par des operateurs US-side (Stargate UAE, Microsoft, OpenAI), faisant chuter le CACI souverain de 55,7 (Physique) a 6,0. Cette dissociation Phys/Sov, formalisee au chapitre V section 5.9.2 sous l'hypothese d'activation des Cloud Sovereignty Mandates 2028, transforme radicalement la lecture de l'asymetrie : la vulnerabilite europeenne se situe non sur le compute installe mais sur la couche operationnelle des charges cloud (majoritairement hebergees sur AWS/Azure/GCP).",
    ]),
    ("2.2 Une architecture protectionniste a trois etages", [
        "L'analyse revele que le protectionnisme IA americain opere a trois niveaux distincts mais cumulatifs.",
        "Premier etage : les controles a l'export (herites de Biden, maintenus et transformes par Trump). Le systeme de tiers (Tier 1/2/3) segmente le monde en fonction de l'alignement geopolitique : acces libre pour les allies proches (20 pays), caps quantitatifs pour le reste du monde, interdiction pour les adversaires (Chine, Russie). Meme apres l'abrogation formelle de l'AI Diffusion Rule en mai 2025, l'incertitude reglementaire pese sur les decisions d'investissement des pays Tier 2 (chapitre III).",
        "Deuxieme etage : les tarifs douaniers (innovation Trump). Le tarif de 25 pour cent sur les semi-conducteurs IA avances (Section 232, janvier 2026) constitue une rupture : les controles a l'export visaient la securite nationale, les tarifs visent explicitement les revenus et l'avantage concurrentiel. La combinaison tarifs plus exemptions domestiques cree un differentiel de cout direct entre entreprises americaines et non-americaines (chapitre V).",
        "Troisieme etage : la gravite capitalistique. La concentration du capex (660-690 milliards USD chez cinq entreprises en 2026), combinee a l'acces energetique (les Etats-Unis acceptent un recours accru aux fossiles, 53,7 GW de capacite DC installee), cree un effet gravitationnel : les investissements japonais (550 milliards), des Emirats, de SoftBank/Stargate convergent vers le sol americain, renforcant le hub compute sans intervention reglementaire supplementaire (chapitre VI ter).",
        "Un quatrieme etage potentiel se profile a l'horizon 2028 : les Cloud Sovereignty Mandates analyses au chapitre V section 5.9. En etendant les obligations du Framework for AI Diffusion a la couche cloud, ils transformeraient les hyperscalers US operant offshore en intermediaires conditionnels du compute mondial. La fenetre de vulnerabilite europeenne (CADA operationnel au mieux 2027-2028, Mandates US activables 2028) est maximale entre 2028 et 2030.",
    ]),
    ("2.3 Consequences differenciees par region", [
        "Le Tableau 24 ci-apres synthetise les positions structurelles et les risques specifiques de chaque region etudiee, en integrant l'extension a l'Afrique developpee au chapitre VI quater.",
    ]),
    ("3. Contributions de cette etude", [
        "Cette recherche apporte cinq contributions a la litterature economique et geostrategique.",
        "Premierement, l'integration analytique de trajectoires habituellement traitees separement - energie, semi-conducteurs, compute, regulation, productivite - dans un cadre unifie. L'essentiel des travaux academiques traite separement ces dimensions ; notre analyse montre qu'elles forment un systeme d'interdependances ou chaque contrainte amplifie les autres (l'energie contraint le compute, le compute contraint la productivite, la productivite determine la competitivite).",
        "Deuxiemement, la proposition de l'indice CACI (Compute-Adjusted Competitive Index), qui offre un cadre de mesure pour comparer la competitivite IA entre regions en integrant FLOPs disponibles, capital humain, regulation et cout energetique selon une formule geometrique ponderee. Si cet indice reste a affiner empiriquement, il constitue une premiere tentative de synthetiser le concept de compute-adjusted competitiveness identifie comme manquant dans la litterature (chapitre II). L'extension Phys/Sov introduite au chapitre I et formalisee au chapitre V (F = F_phys x F_sov) ajoute une dimension juridictionnelle qui distingue le compute physiquement present du compute legalement controlable - distinction operationnelle des le snapshot avril 2026 (cas EAU 99,6 pct US-side) et systemique sous regime Cloud Sovereignty Mandates 2028.",
        "Troisiemement, la demonstration que le protectionnisme IA americain produit des effets paradoxaux systemiques. Les restrictions destinees a maintenir l'avantage US accelerent la construction d'un ecosysteme chinois alternatif (DeepSeek, Huawei Ascend, capacite reelle 246-300 EFLOP/s contre 0,5 pct apparent dans les donnees Epoch AI consolidees), poussent les pays Tier 2 vers la Chine (ByteDance au Bresil, en ASEAN, en Afrique), et incitent les allies Tier 1 a co-financer la suprematie US plutot qu'a construire une autonomie veritable (Japon : 550 milliards vers les Etats-Unis). Le protectionnisme IA ne produit pas un monde unipolaire mais un monde fragmente en blocs technologiques.",
        "Quatriemement, l'analyse comparative inedite des reponses regionales au protectionnisme IA (Europe, Amerique du Sud, Asie, Afrique), montrant que la position geopolitique, la dotation energetique et la proximite avec les chaines de valeur determinent des trajectoires de dependance fondamentalement differentes, irreductibles a un modele unique de rattrapage ou de decrochage.",
        "Cinquiemement, l'extension a l'Afrique (chapitre VI quater) documente l'asymetrie compute la plus extreme au monde (deficit x44 a x417 selon les indicateurs) et montre comment le protectionnisme americain cree pour ce continent un double bind specifique : restriction d'acces au compute frontier US d'un cote, exposition aux risques de surveillance et de sanctions secondaires du recours a l'alternative chinoise de l'autre.",
    ]),
    ("4. Limites et pistes de recherche", [
        "Cette etude comporte plusieurs limites qu'il convient d'expliciter.",
        "Incertitude reglementaire. L'environnement des export controls evolue rapidement. L'AI Diffusion Rule de Biden a ete abrogee en mai 2025 ; la regle finale Trump de janvier 2026 pourrait elle-meme etre modifiee (Commerce doit fournir une mise a jour au President d'ici juillet 2026). Les scenarios proposes au chapitre V refletent cette incertitude, mais l'espace des possibles est plus large que les quatre scenarios formalises.",
        "Donnees fragmentaires. Les donnees de compute IA par region restent incompletes malgre le snapshot rigoureux du tableau de bord public d'avril 2026. Les estimations Epoch AI sous-representent significativement la capacite chinoise reelle (Chine 0,5 pct apparent vs 246-300 EFLOP/s revendiques) en raison de l'anonymisation des clusters chinois et de l'opacite des fournisseurs Huawei/Cambricon/Biren. Le CACI est un indice exploratoire, calibre sur le snapshot avril 2026 mais non encore valide sur series temporelles longues.",
        "Horizon temporel. L'analyse porte sur 2026-2030, mais des ruptures technologiques (quantum computing, noeuds sub-2 nm, architectures neuromorphiques) pourraient redistribuer les cartes apres 2030. L'avantage actuel de Nvidia en GPU pourrait etre conteste par des ASIC specialises (Google TPU, Amazon Trainium, Huawei Ascend) ou des architectures radicalement differentes (DARE/RISC-V europeen, horizon 2030-2032).",
        "Sensibilite aux ponderations CACI. Les ponderations de la formule geometrique (F^0,40 x L^0,20 x R^0,15 / E^0,25) ont ete choisies au chapitre II en fonction de la litterature mais ne sont pas issues d'une calibration econometrique. Une analyse de sensibilite systematique sur ces ponderations pourrait reveler des trajectoires alternatives non explorees.",
        "Pistes de recherche futures. Quatre prolongements s'imposent. Premierement, le calibrage empirique du CACI sur donnees d'enquete (productivite sectorielle par acces au compute) permettrait de valider ou ajuster les ponderations actuelles. Deuxiemement, l'approfondissement sectoriel de la couverture Afrique (chapitre VI quater) - notamment l'analyse pays par pays des 16 strategies IA nationales recensees et de la mise en oeuvre de la Strategie continentale UA Phase II 2028. Troisiemement, la modelisation dynamique de l'interaction energie-compute-productivite via des modeles d'equilibre general calculable (CGE) integrant les contraintes de compute comme facteur de production. Quatriemement, l'observation longitudinale du regime Cloud Sovereignty Mandates 2028 (s'il s'active effectivement) et de ses effets sur la trajectoire F_sov des differentes juridictions.",
    ]),
    ("5. L'enjeu de civilisation", [
        "Au-dela des metriques economiques et des scenarios geopolitiques, cette etude revele un enjeu plus fondamental. Le compute IA est en passe de devenir le quatrieme facteur de production (apres le capital, le travail et la terre/energie), structurant l'acces aux gains de productivite, a l'innovation, et in fine a la prosperite. Comme le petrole au XXe siecle, le controle du compute au XXIe siecle determinera quelles nations et quelles entreprises captent les rentes de l'innovation.",
        "Les Etats-Unis l'ont compris. L'AI Action Plan de juillet 2025 traite explicitement le stack IA comme un instrument d'alliance geopolitique, comparable au Plan Marshall ou au systeme de Bretton Woods : l'acces au compute americain est conditionne a l'alignement strategique, creant un systeme de dependances hierarchisees. Carnegie note que la regle visait a utiliser les exportations d'IA comme levier sur les Etats pivots geopolitiques, en etablissant des incitations pour que d'autres gouvernements adoptent les standards et protections technologiques americains en echange de puces US.[3]",
        "Face a ce nouveau systeme, la France et l'Europe disposent d'un choix strategique qui se resume, au fond, a trois options. La premiere est l'integration subordonnee : accepter le statut de junior partner technologique dans le bloc americain, comme le Japon l'a choisi en investissant 550 milliards USD sur le sol US. Cette option minimise le risque de rupture d'acces mais maximise la dependance. La deuxieme est la confrontation souverainiste : construire un ecosysteme IA entierement autonome, comme la Chine y est contrainte. Cette option est irrealiste a l'horizon 2030 pour l'Europe, qui ne dispose ni de la base industrielle de semi-conducteurs ni de la capacite de marche interieur suffisantes.",
        "La troisieme option - celle que cette etude recommande au chapitre VII - est l'autonomie strategique ciblee. Elle consiste a batir une souverainete sur les segments ou l'Europe possede un avantage comparatif (energie nucleaire francaise au cout PPA 1,35x USA, equipements de lithographie ASML, modeles IA ouverts Mistral, cadre reglementaire AI Act) tout en maintenant l'interoperabilite avec l'ecosysteme americain. L'objectif n'est pas l'autarcie mais la capacite de choix : disposer d'alternatives credibles (cloud souverain SOV-3, compute local sous juridiction UE, modeles ouverts) pour ne jamais etre captif d'un fournisseur dont les interets geopolitiques pourraient diverger des notres. La distinction Phys/Sov etablie au chapitre I est ici operationnelle : il s'agit d'augmenter F_sov sur la couche des charges cloud, pas seulement F_phys sur l'infrastructure installee.",
        "Le temps presse. Le point de basculement identifie dans cette etude se situe en 2028 : convergence de la saturation compute et energie UE (chapitre V section 5.7.3), activation potentielle des Cloud Sovereignty Mandates (chapitre V section 5.9), et fin probable de la fenetre de vulnerabilite avant cristallisation des positions. Apres cette date, les positions se rigidifient autour de la baseline 17,6:1 brut / 3,46:1 CACI Power Mode et les dependances deviennent structurelles. La fenetre d'action strategique 2026-2028 est etroite. Les 109 milliards EUR d'investissements IA annonces pour la France, le programme InvestAI de 200 milliards EUR, la montee en puissance de Mistral Compute, et les sites nucleaires EDF dedies constituent les elements d'une reponse. Mais entre l'annonce et l'execution, il y a la distance qui separe la strategie du reel. L'Inde promet 200 milliards USD mais ne dispose que de 1,4 GW installe. L'Europe ne peut pas se permettre un ecart comparable entre ambition et realisation.",
        "En definitive, AI for Americans First n'est pas seulement un scenario de politique commerciale. C'est le signal d'une recomposition de l'ordre technologique mondial comparable aux grandes restructurations du XXe siecle - Bretton Woods, le choc petrolier, la fin de la guerre froide. Chacune de ces ruptures a cree des gagnants et des perdants pour des decennies. La question pour la France et l'Europe n'est plus de savoir si cette recomposition aura lieu - elle est en cours - mais de determiner si nous en serons les architectes ou les sujets.",
        "Fabrice Pizzi, Paris, fevrier 2026.",
    ]),
]


TABLES = [
    ("Tableau 24. Synthese des consequences regionales du protectionnisme IA americain.",
     "Source : construction de l'auteur, calibration sur le snapshot avril 2026 (US 76,9 pct compute IA operationnel, ratio brut UE 17,6:1, CACI Power Mode 3,46:1).",
     [
         ["Region", "Position structurelle", "Impact principal", "Risque specifique"],
         ["Europe / France", "Tier 1, dependante GPU + cloud US (72-80 pct workloads)",
          "Compute gap 17,6:1 brut / 3,46:1 CACI ; couts training x5-10",
          "Vendor lock-in geopolitique ; marginalisation si bloc US-Asie se ferme ; vulnerabilite F_sov sur charges cloud"],
         ["Amerique du Sud / Bresil", "Tier 2, terrain de competition US-Chine",
          "Bifurcation technologique ; brain drain amplifie",
          "Triple fracture (Nord-Sud, Est-Ouest, intra-regionale)"],
         ["Japon / Coree / Taiwan", "Tier 1, maillons critiques chaine de valeur",
          "Co-financement suprematie US (550 Md USD Japon) ; transfert production",
          "Partenariat asymetrique ; erosion avantage Taiwan ; investissement japonais aux US plutot qu'en UE"],
         ["Inde", "Tier 2, pivot Sud global",
          "Tension caps GPU vs ambition hub compute",
          "Souverainete applicative sans souverainete hardware"],
         ["Chine", "Tier 3, autonomisation forcee",
          "Ecosysteme IA parallele (Huawei/DeepSeek) ; capacite reelle 246-300 EFLOP/s ; retard 2-3 generations GPU",
          "Bifurcation technologique permanente ; exportation aux Tier 2/3 (Bresil, ASEAN, Afrique)"],
         ["Afrique", "Tier 2/3, deficit compute x44-x417",
          "Asymetrie extreme ; double bind US/Chine",
          "Dependance Huawei/DeepSeek ; surveillance ; enfermement structurel ; cas EAU 99,6 pct US-side"],
     ]),
    ("Tableau 25. Recapitulatif des chapitres, volume et appareil critique de l'etude.",
     "Source : construction de l'auteur. Le volume (en pages indicatives) inclut figures et tableaux mais exclut les annexes econometriques.",
     [
         ["Chapitre", "Titre", "Pages indicatives", "Notes"],
         ["I", "Cadre theorique : protectionnisme technologique et IA", "~12", "22"],
         ["II", "Methodologie : matrice scenarielle et indice CACI", "~8", "10"],
         ["III", "Diagnostic empirique 2020-2026 : energie, semi-conducteurs, compute", "~11", "20"],
         ["IV", "Mecanismes de l'avantage competitif US", "~9", "19"],
         ["V", "Scenarios prospectifs 2026-2030 et Cloud Sovereignty Mandates", "~14", "29"],
         ["VI", "Consequences pour la France et l'Europe", "~10", "14"],
         ["VI bis", "Consequences pour l'Amerique du Sud et le Bresil", "~11", "19"],
         ["VI ter", "Consequences pour l'Asie", "~12", "16"],
         ["VI quater", "Consequences pour l'Afrique", "~13", "26"],
         ["VII", "Recommandations strategiques pour la France et l'Europe", "~11", "18"],
         ["Conclusion", "Du protectionnisme IA a la recomposition de l'ordre technologique mondial", "~9", "3"],
         ["TOTAL", "11 chapitres", "~120", "196"],
     ]),
]


NOTES = [
    "Pillsbury Law (janvier 2026), 'Trump Admin Targets Advanced AI Semiconductors'. Section 232 : tarif 25 pct sur Nvidia H200, AMD MI325X pour reexportation Chine. Exemptions domestiques US. Regle finale BIS simultanee. Mise a jour marche DC prevue juillet 2026.",
    "White House / CM Trade Law (juillet 2025), 'America's AI Action Plan'. Pilier III : exporter le full AI technology stack aux allies. Quatre principes : export aux allies, renforcement enforcement, alignement global, protection mesures.",
    "Carnegie Endowment for International Peace (mai 2025), 'The Trump Administration May Be About to Repeal the AI Diffusion Rule'. Analyse du trilemme controle/promotion/levier. Recommandation : elargir le groupe Tier 1, augmenter les allocations Inde, renforcer les exigences de localisation.",
]


SOURCES_LINE = (
    "Sources principales mobilisees : AIE, McKinsey, Bruegel, Brookings, Carnegie Endowment, "
    "Commission europeenne, White House/BIS, Parlement europeen, CSIS, S&P Global, Epoch AI, "
    "Centre for Future Generations (CFG), Euronews, CEPALC/CENIA (ILIA 2025), Banque mondiale, "
    "Futurum, Introl, World Nuclear News, Arizton, Pillsbury Law, ITIF, Foreign Policy, Hudson "
    "Institute, Mordor Intelligence, McKinsey Global Institute, FMI. Donnees complementaires : "
    "Bloomberg, DCD, Morgan Lewis, Tom's Hardware, Serrari Group, Data Center Knowledge, "
    "WEF, Africa Defense Forum, Atlantic Council DFRLab, Carnegie Endowment, New Lines Institute, "
    "RTE, EDF, ANSSI, USTDA. Donnees primaires : tableau de bord public Epoch AI snapshot "
    "avril 2026 (https://mo0ogly.github.io/America-First-IA/dashboard/)."
)


def build(out_dir: Path) -> Path:
    """Build the FR Conclusion .docx."""
    log.info("Building Conclusion FR -> Conclusion_Generale_FR.docx")
    doc = init_document()
    add_cover(doc, chapter_label=CHAPTER_LABEL,
              chapter_subtitle="Conclusion generale")
    add_chapter_header(doc, label=CHAPTER_LABEL,
                       title=CHAPTER_TITLE, intro=CHAPTER_INTRO)

    for title, paragraphs in SECTIONS:
        render_section(doc, title, paragraphs)

    for caption, source, rows in TABLES:
        render_table(doc, caption, source, rows)

    # Sources line at the very end
    from concl_helpers import add_paragraph, GREY
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    add_paragraph(doc, SOURCES_LINE,
                  align=WD_ALIGN_PARAGRAPH.LEFT,
                  size=9, italic=True, color=GREY, space_after=6)

    render_notes(doc, NOTES)
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Conclusion generale")

    out = out_dir / "Conclusion_Generale_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
