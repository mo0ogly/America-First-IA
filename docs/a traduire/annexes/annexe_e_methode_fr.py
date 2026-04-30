"""
Annexe E - IA comme amplificateur de methode - generateur FR.

Genere le .docx de l'Annexe E (Note de recherche sur l'ingenierie
comportementale du modele et l'economie de densite cognitive
au niveau individuel/organisationnel) en francais.

Note de recherche (mars 2026) qui analyse pourquoi la competence rare
de l'economie IA sera le cadrage, pas la production. Complementaire de
l'Annexe D (lecture geostrategique de la doctrine Huang) en proposant
la lecture individuelle/organisationnelle de l'economie de densite
cognitive, illustree par le cas LIA-Scan.

Annexe E consolidee sur le baseline avril 2026 :
    - Bandeau couverture : 76,9 / 1,59x / 3,46:1
    - Ratio CACI US/UE Power Mode : 3,46:1 (au lieu de 3,4:1)
    - Reference these AI for Americans First : 11 chapitres, ~120 pages,
      196 notes (au lieu de 103 pages / 157 notes)
    - Reference croisee a l'Annexe D pour la lecture geostrategique

Numerotation des tableaux : annexe E (pas de tableau ; note breve).

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
from pathlib import Path

from method_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("annexe_e_methode_fr")


CHAPTER_LABEL = "ANNEXE E - NOTE DE RECHERCHE"
CHAPTER_TITLE = (
    "L'IA comme amplificateur de methode : pourquoi la competence rare de l'economie IA "
    "sera le cadrage, pas la production"
)
CHAPTER_INTRO = (
    "Cette annexe presente la note de recherche de mars 2026 sur l'IA comme amplificateur "
    "de methode. La democratisation des outils d'IA generative depuis 2023 a produit un "
    "paradoxe : des outils plus puissants ont, dans un premier temps, industrialise une "
    "nouvelle categorie de mediocrite professionnelle. Cette note analyse les causes de ce "
    "phenomene (absence de methode de pilotage, deficit de controle qualite, confusion entre "
    "production et validation) et propose un cadre d'analyse fonde sur le concept d'ingenierie "
    "comportementale du modele. En s'appuyant sur un cas d'usage concret (LIA-Scan, plateforme "
    "d'audit cybersecurite, 160+ frameworks) et sur le modele a cinq couches de Jensen Huang "
    "(energie, puces, infrastructure, modeles, applications), la note demontre que la "
    "competence rare dans l'economie IA ne sera pas la capacite a produire, mais la capacite "
    "a cadrer, verifier, orchestrer et arbitrer les sorties de modeles a cadence industrielle. "
    "Le concept d'economie de densite cognitive est introduit pour designer ce nouveau regime "
    "de travail, complementaire de la lecture geostrategique developpee dans l'annexe D. "
    "Mots-cles : ingenierie comportementale, IA generative, cadrage, densite cognitive, "
    "pipeline agentique, audit cybersecurite, LIA-Scan, methode, CACI."
)


SECTIONS: list[tuple[str, list[str]]] = [
    ("E.1 Le paradoxe de la premiere phase : puissance d'outil, pauvrete de methode", [
        "Depuis 2023, la democratisation rapide des LLM et des outils d'IA generative a mis des capacites de production considerables entre les mains de professionnels qui ne disposaient d'aucune methode structuree pour les piloter. Le resultat, largement documente dans la litterature et dans les retours d'experience industriels, est previsible : analyses superficielles, code fragile, syntheses plausibles mais creuses, livrables qui passent les revues initiales mais echouent en production.",
        "Ce phenomene a ete massivement attribue aux hallucinations des modeles. Or, une analyse plus rigoureuse montre qu'une large part du probleme releve de l'humain : absence de cadrage du probleme en amont, absence de verification des sorties, absence de comparaison entre sources, absence de questionnement critique. La machine a amplifie une mauvaise methode de travail. Elle ne l'a pas creee.",
        "Cette phase va se terminer, non pas parce que les modeles seront parfaits, mais parce que les organisations vont apprendre, souvent a un cout eleve, ce que represente un livrable IA non controle deploye en environnement de production, notamment dans les contextes a forte exigence : securite, finance, sante, droit, decision strategique.",
    ]),
    ("E.2 Le modele a cinq couches et la chaine de dependances", [
        "Jensen Huang a propose, au GTC de San Jose (mars 2026), un modele a cinq couches pour decrire l'infrastructure IA : energie, puces, infrastructure physique, modeles et applications.[1] Ce modele exprime une realite souvent ignoree dans le debat sur l'IA : derriere chaque output IA se cache une chaine de dependances industrielles complete. Cette chaine coute, elle contraint, et elle cree des asymetries massives entre ceux qui la controlent et ceux qui en dependent.",
        "L'indice CACI Power Mode (Compute-Adjusted Competitiveness Index), construit dans le cadre de la recherche AI for Americans First (Pizzi, Universite Paris-Sorbonne, 2026), quantifie cette asymetrie en integrant quatre dimensions : energie, semi-conducteurs, compute et regulation, selon la formule geometrique F^0,40 x L^0,20 x R^0,15 / E^0,25. Sur le snapshot avril 2026 du tableau de bord public, le ratio brut compute installe operationnel US/UE(13) atteint 17,6:1, traduit en un ratio CACI Power Mode US/UE de 3,46:1.[2]",
        "Ce ratio a une consequence directe sur le monde du travail : les professionnels qui operent dans des ecosystemes structurellement sous-dotes en compute devront compenser par une maitrise operationnelle superieure. La ressource rare ne sera pas l'acces a l'outil. Ce sera la capacite a en tirer un resultat fiable malgre les contraintes.",
    ]),
    ("E.3 Redistribution des competences : methode contre anciennete", [
        "L'IA redistribue les avantages concurrentiels de facon contre-intuitive. L'anciennete brute, definie comme l'accumulation d'experience sans structure de raisonnement explicite, perd de sa valeur relative. Un professionnel experimente qui pilote l'IA de facon approximative sera depasse par un profil junior dote d'une structure de reflexion rigoureuse : capable de decomposer un probleme, d'orchestrer plusieurs outils en parallele, de comparer leurs sorties, d'identifier les angles morts et de valider avant de livrer.",
        "Ce constat rejoint un principe pedagogique plus large : un esprit bien construit et rigoureux sera toujours superieur a un esprit plein d'informations et d'experience mais qui ne dispose pas de ce schema de fonctionnement. L'IA ne modifie pas cette verite. Elle l'accelere et la rend plus visible qu'elle ne l'a jamais ete. L'avantage n'est pas lie a l'age ni au titre. Il est lie a la methode.",
    ]),
    ("E.4 Ingenierie comportementale du modele : illustration par LIA-Scan", [
        "LIA-Scan est une plateforme d'audit de configuration cybersecurite couvrant plus de 200 technologies et 160+ frameworks (GRC, SMSI). Pour automatiser la generation de regles de detection CVE, un pipeline nocturne agentique a ete concu via n8n.[3]",
        "L'agent ne produit pas une regle YAML en sortie directe. Il traverse une boucle structuree obligatoire : decomposition du probleme, planification de l'approche, action de generation, observation du resultat, evaluation avec scoring explicite. Ce scoring fonctionne comme un signal de controle de flux : sous un certain seuil, l'agent repart en boucle, replanifie et change d'approche en integrant une phase de retour d'experience. Au-dessus du seuil, la regle est committee. Le journal de chaque action est append-only et auditable.",
        "Sans ce mecanisme, le taux de regles inexploitables en production etait inacceptable. Avec lui, le pipeline produit des regles testables, tracables, deployables sur des environnements bancaires (DORA, NIS2/ReCyF). Lorsqu'une regle echoue, l'erreur est localisable dans le journal a l'etape precise ou le raisonnement a devie.",
        "Ce n'est pas de l'utilisation d'IA. C'est de l'ingenierie comportementale du modele : la conception de contraintes structurelles qui forcent le modele a produire de facon controlee, evaluable et tracable. C'est precisement cette competence que l'economie de l'IA va rendre rare et valorisee.",
    ]),
    ("E.5 Economie de densite cognitive : definition et portee", [
        "Le travail ne disparait pas avec l'IA. Il se deplace : du faire vers le cadrer, verifier, orchestrer et arbitrer. Les organisations qui s'habituent a des livrables IA de qualite relevent le niveau attendu de facon permanente. Le volume supplementaire produit par l'IA ne sera pas synonyme de confort : il sera synonyme d'exigence accrue en continu.",
        "Le concept d'economie de densite cognitive designe ce nouveau regime : une economie ou la competence rare n'est pas la capacite a produire, mais la capacite a produire juste, de facon coherente, a une cadence industrielle, avec une tracabilite complete. La puissance de l'outil amplifie les erreurs de cadrage autant qu'elle amplifie les bonnes decisions.",
        "Ce concept admet une double lecture. Au niveau individuel et organisationnel (objet de la presente annexe E), il decrit l'intensification du travail cognitif et l'emergence de l'ingenierie comportementale du modele comme discipline. Au niveau geostrategique (developpe dans l'annexe D - Densite cognitive et doctrine Huang), il designe un nouveau regime de puissance ou la richesse d'un pays se mesure par sa capacite a transformer du compute en resultat fiable, verifiable et souverain.[4]",
    ]),
    ("E.6 Conclusion", [
        "La premiere phase de deploiement de l'IA generative en entreprise (2023-2026) a mis en evidence un deficit structurel de methode, masque par la puissance des outils. La phase suivante sera caracterisee par une montee en exigence dans tous les contextes a forte valeur, ou les livrables non controles ne seront plus toleres.",
        "La competence differenciante ne sera pas l'acces a l'IA ni la capacite a produire du volume, mais la maitrise du cadrage, de la verification et de l'orchestration des sorties de modeles. L'ingenierie comportementale du modele, illustree ici par le cas LIA-Scan, constitue une premiere formalisation de cette discipline.",
        "Nous n'entrons pas dans une economie de la paresse assistee. Nous entrons dans une economie de densite cognitive, et le niveau d'exigence va continuer a monter aussi vite que les modeles progressent. La conjugaison de cette montee d'exigence individuelle avec l'asymetrie geostrategique documentee dans le cadre CACI (ratio US/UE 3,46:1 Power Mode, ratio brut 17,6:1) cree un imperatif specifique pour les professionnels europeens : compenser l'asymetrie d'infrastructure par une superiorite methodologique. La methode devient l'arme strategique de la juridiction sous-dotee en compute.",
    ]),
]


NOTES = [
    "Jensen Huang, keynote GTC 2026, San Jose, 18 mars 2026 ; blog NVIDIA, mars 2026. Modele a 5 couches : energie, puces, infrastructure physique, modeles et applications.",
    "Pizzi, F. (2026), 'AI for Americans First : Protectionnisme IA americain, recomposition de l'ordre technologique mondial et consequences pour la France et l'Europe (2026-2030)', Universite Paris-Sorbonne, 11 chapitres, environ 120 pages, 196 notes. Tableau de bord public : https://mo0ogly.github.io/America-First-IA/dashboard/. Depot : https://github.com/mo0ogly/America-First-IA. Snapshot avril 2026 : USA 76,9 pct du compute IA operationnel mondial, ratio brut compute installe US/UE(13) 17,6:1, ratio CACI Power Mode US/UE 3,46:1. Formule geometrique consolidee : F^0,40 x L^0,20 x R^0,15 / E^0,25.",
    "LIA-Scan : plateforme d'audit de configuration cybersecurite, 200+ technologies, 160+ frameworks (GRC, SMSI). Pipeline agentique nocturne via n8n pour la generation automatique de regles de detection CVE. Boucle obligatoire : decomposition, planification, action, observation, evaluation avec scoring. Journal append-only auditable.",
    "Pizzi, F. (2026), 'Economie de densite cognitive et structuration de marche : lecture d'intelligence economique de la doctrine Huang sur la consommation de tokens IA', Annexe D de la these AI for Americans First, Universite Paris-Sorbonne. La presente annexe E (lecture individuelle et organisationnelle) est complementaire de l'annexe D (lecture geostrategique).",
]


def build(out_dir: Path) -> Path:
    """Build the FR Annexe E IA amplificateur de methode .docx."""
    log.info("Building Annexe E Methode [FR] -> Annexe_E_IA_Amplificateur_Methode_FR.docx")
    doc = init_document()
    add_cover(doc, chapter_label=CHAPTER_LABEL,
              chapter_subtitle="Note de recherche - IA, methode et densite cognitive")
    add_chapter_header(doc, label=CHAPTER_LABEL,
                       title=CHAPTER_TITLE, intro=CHAPTER_INTRO)
    for title, paragraphs in SECTIONS:
        render_section(doc, title, paragraphs)
    render_notes(doc, NOTES)
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Annexe E IA amplificateur de methode")

    out = out_dir / "Annexe_E_IA_Amplificateur_Methode_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
