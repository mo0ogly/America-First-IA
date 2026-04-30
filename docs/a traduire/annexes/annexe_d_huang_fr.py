"""
Annexe D - Note Densite Cognitive Huang - generateur FR.

Genere le .docx de l'Annexe D (Note de recherche sur la doctrine Huang
et l'economie de densite cognitive) en francais.

Note de recherche (mars 2026) qui propose une lecture d'intelligence
economique de la declaration de Jensen Huang du 20 mars 2026 sur la
consommation de tokens IA, en la replacant dans le contexte de
l'architecture protectionniste americaine (CACI) et en distinguant
densite cognitive managériale et densite cognitive geostrategique.

Annexe D consolidee sur le baseline avril 2026 :
    - Bandeau couverture : 76,9 / 1,59x / 3,46:1
    - Ratio CACI US/UE Power Mode : 3,46:1 (au lieu de 3,4:1)
    - Cout FLOPs : differentiel coherent avec ratio energie 1,59x PPA
    - Reference explicite a la decomposition Phys/Sov pour la lecture
      souverainiste de la consommation de tokens

Numerotation des tableaux : annexe D (Tab D.1).

Auteur : Fabrice Pizzi (Universite Paris-Sorbonne, M2 Intelligence Economique).
"""

from __future__ import annotations

import logging
from pathlib import Path

from huang_helpers import (
    add_chapter_header, add_cover, init_document,
    render_license, render_notes, render_section, render_table,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("annexe_d_huang_fr")


CHAPTER_LABEL = "ANNEXE D - NOTE DE RECHERCHE"
CHAPTER_TITLE = (
    "Economie de densite cognitive et structuration de marche : lecture d'intelligence "
    "economique de la doctrine Huang sur la consommation de tokens IA"
)
CHAPTER_INTRO = (
    "Cette annexe presente la note de recherche de mars 2026 sur l'economie de densite "
    "cognitive, redigee suite a la declaration de Jensen Huang (CEO de NVIDIA) du 20 mars 2026 "
    "selon laquelle un ingenieur remunere 500 000 USD devrait consommer au minimum 250 000 USD "
    "de tokens IA par an. La note propose une lecture d'intelligence economique de cette "
    "declaration, en la replacant dans le contexte de la position dominante de NVIDIA sur le "
    "marche des accelerateurs IA (environ 80 pct de parts de marche) et de l'architecture "
    "protectionniste americaine documentee dans l'indice CACI Power Mode (ratio US/UE de "
    "3,46:1 sur snapshot avril 2026, ratio brut compute installe 17,6:1). L'analyse croise les "
    "donnees empiriques sur le retour sur investissement des projets GenAI en entreprise (MIT "
    "NANDA, PwC, Forrester, Gartner, IBM) avec le cadre geostrategique du CACI pour demontrer "
    "que la prescription de consommation massive de tokens releve davantage de la structuration "
    "de marche que du conseil managerial, et que le concept d'economie de densite cognitive "
    "doit etre compris comme un nouveau regime de puissance integrant quatre dimensions : "
    "energie, semi-conducteurs, compute et regulation. Mots-cles : intelligence economique, "
    "densite cognitive, CACI, NVIDIA, tokens IA, souverainete numerique, protectionnisme "
    "technologique, ROI GenAI, compute, geostrategie."
)


SECTIONS: list[tuple[str, list[str]]] = [
    ("D.1 Contexte : une declaration a forte resonance mediatique", [
        "Le 20 mars 2026, lors du GTC (GPU Technology Conference) de San Jose, Jensen Huang a participe au podcast All-In ou il a formule ce qui est rapidement devenu la citation la plus reprise de la semaine dans l'ecosysteme tech mondial : si cet ingenieur remunere 500 000 USD ne consommait pas au moins 250 000 USD de tokens IA, je serais profondement alarme.[1]",
        "Huang a precise que si cet ingenieur n'avait depense que 5 000 USD de tokens, il serait extremement mecontent. Interroge sur le fait que NVIDIA tentait de depenser 2 milliards USD en tokens pour son equipe d'ingenieurs, il a confirme : we are trying to. Il a egalement evoque, lors de sa keynote au GTC, l'idee d'integrer un budget tokens equivalent a environ la moitie du salaire de base comme composante d'attractivite dans le recrutement d'ingenieurs.[2]",
        "La reception mediatique et professionnelle de cette declaration s'est concentree quasi exclusivement sur sa dimension manageriale : l'injonction a la productivite individuelle via une consommation intensive d'IA. Cette note propose une lecture differente.",
    ]),
    ("D.2 Grille de lecture : qui parle, depuis quelle position, avec quel interet ?", [
        "Le premier reflexe en intelligence economique, face a une declaration publique d'un dirigeant d'entreprise, consiste a identifier la position structurelle de l'emetteur. Jensen Huang est le CEO de NVIDIA, premier fournisseur mondial d'accelerateurs IA, avec environ 80 pct de parts de marche sur les puces d'entrainement et d'inference IA.[3] NVIDIA est egalement le principal beneficiaire de la croissance de la consommation de tokens : chaque dollar de token consomme dans le monde genere, directement ou indirectement, de la demande pour du compute execute sur materiel NVIDIA.",
        "Dans ce cadre, la declaration consommez au moins la moitie de votre salaire en tokens ne constitue pas un conseil managerial neutre. Elle constitue un acte de structuration de la demande sur le propre marche de l'emetteur. Le fait que cette lecture soit quasiment absente du debat public sur l'IA suggere un deficit de maturite en intelligence economique appliquee au secteur technologique.",
    ]),
    ("D.3 Confrontation empirique : le decalage entre la prescription et les resultats observes", [
        "La prescription de Huang est coherente dans un contexte tres specifique : des profils d'elite operant dans des ecosystemes matures (NVIDIA, hyperscalers, pointe de la Silicon Valley), ou les agents IA tournent en continu et ou chaque dollar de compute se replique en valeur mesurable. Projetee sur l'ensemble du tissu economique, elle se heurte cependant aux donnees empiriques disponibles, synthetisees dans le tableau D.1.",
        "Le decalage entre la prescription (depensez 250 000 USD de tokens par ingenieur) et la realite empirique (95 pct d'absence de retour mesurable selon le MIT NANDA) pose une question structurelle. Si la majorite des organisations ne parviennent pas a convertir leur depense IA en valeur, le principal beneficiaire d'une augmentation de cette depense n'est pas l'entreprise consommatrice, mais le fournisseur d'infrastructure de compute.",
    ]),
    ("D.4 Le volume de tokens comme indicateur de dependance", [
        "Mesurer la consommation de tokens comme indicateur de productivite individuelle pose un probleme methodologique fondamental : cette metrique capture l'activite, pas la valeur creee. Elle est comparable a l'evaluation d'un developpeur par ses heures passees dans un environnement de developpement plutot que par les fonctionnalites livrees et validees.",
        "Plus problematique encore, cette metrique cree un incentive pervers : la maximisation du volume de tokens consommes, independamment de la valeur produite. Dans un contexte d'audit ou de cybersecurite, ce type de metrique serait immediatement ecarte au profit d'indicateurs de resultat : cycle time, findings exploitables, incidents evites, features livrees, couts de remediation reduits.",
        "Le ratio pertinent n'est pas le volume de tokens consomme, mais la valeur verifiable produite par unite de compute consommee. Ce changement de metrique, applique a l'echelle geostrategique, modifie profondement la lecture du concept de densite cognitive.",
    ]),
    ("D.5 Economie de densite cognitive : du sens managerial au sens geostrategique", [
        "Le concept d'economie de densite cognitive admet deux lectures.",
        "La premiere, manageriale, decrit l'intensification du travail cognitif par individu : chaque professionnel devra produire davantage de valeur par unite de temps, en s'appuyant sur l'IA comme levier. Cette lecture est correcte mais insuffisante.",
        "La seconde lecture, geostrategique, designe un nouveau regime de puissance mondial. La richesse et la competitivite d'un pays, d'un bloc ou d'une organisation ne se mesurent plus uniquement par les ressources naturelles, le PIB industriel ou le capital humain brut, mais par la capacite a transformer du compute en resultat fiable, verifiable et souverain.",
        "C'est cette seconde lecture que formalise l'indice CACI Power Mode (Compute-Adjusted Competitiveness Index), construit dans le cadre de la recherche AI for Americans First (Pizzi, Universite Paris-Sorbonne, fevrier 2026).[4] Le CACI integre quatre dimensions habituellement traitees separement dans la litterature : energie, semi-conducteurs, compute et regulation, selon la formule geometrique F^0,40 x L^0,20 x R^0,15 / E^0,25.",
    ]),
    ("D.5.1 Resultats du CACI Power Mode (snapshot avril 2026)", [
        "Sur le snapshot avril 2026 du tableau de bord public, le ratio brut compute installe operationnel US/UE(13) atteint 17,6:1 (USA 76,9 pct du compute IA operationnel mondial vs UE(13) 3,3 pct), traduit par la formule geometrique Power Mode en un ratio CACI US/UE de 3,46:1. Trois facteurs convergents portent cet ecart.",
        "Ecart de compute et d'energie. Sur le compute strict (clusters Epoch AI), les Etats-Unis disposent de 39,6 millions d'equivalents H100 installes operationnels contre 2,6 millions pour l'UE(13). Ce gap se traduit dans le cout des FLOPs via le differentiel energetique : USA 85 USD/MWh PPA-ajuste contre UE 135 USD/MWh moyenne (France 115 USD/MWh, Allemagne 140, Royaume-Uni 190), soit un ratio de 1,59x apres ajustement PPA. Sources : Epoch AI GPU Clusters Dataset (2025), AIE Electricity 2024 Report, tableau de bord public avril 2026.[5]",
        "Architecture protectionniste a trois etages. Le cadre reglementaire americain sous l'administration Trump 2.0 combine trois mecanismes : (i) les export controls herites de Biden et renforces, segmentant le monde en trois tiers d'acces ; (ii) les tarifs Section 232 de 25 pct sur les semi-conducteurs IA avances (janvier 2026), creant un differentiel de cout direct entre firmes americaines (exemptees) et non-americaines ; (iii) la gravite du capital, avec 660 a 690 milliards USD de capex annuel des cinq hyperscalers americains (Microsoft, Amazon, Alphabet, Meta, Oracle).[6]",
        "Convergence des investissements allies vers le sol americain. Les allies Tier 1 co-financent la suprematie americaine plutot que de construire leur propre autonomie. L'investissement japonais dirige vers les Etats-Unis atteint 550 milliards USD, renforcant la concentration du compute sur le territoire americain.[7]",
    ]),
    ("D.5.2 La distinction Phys/Sov : un quatrieme etage potentiel", [
        "L'extension Phys/Sov introduite au chapitre I de la these (Fig 1.8) et formalisee au chapitre V (Cloud Sovereignty Mandates 2028) ajoute une dimension critique a la lecture de la doctrine Huang. La decomposition F(r) = F_phys(r) x F_sov(r) revele que la consommation de tokens par un ingenieur europeen ne se reduit pas a une question de compute installe en Europe, mais releve aussi de la juridiction operationnelle des charges cloud.",
        "Sur le compute installe (cluster ownership Epoch AI), l'UE est largement souveraine (F_sov = 0,99 sur F_phys 2,6 M H100-eq). Sur la couche operationnelle des charges cloud, en revanche, les hyperscalers americains controlent environ 72 pct du cloud public europeen (Synergy Research Group T3 2025), soit F_sov_workloads UE environ 0,28. Lorsque l'ingenieur europeen suit la prescription de Huang, le token qu'il consomme transite presque exclusivement par cette couche operationnelle US-side.",
        "Sous regime hypothetique de Cloud Sovereignty Mandates 2028, ce ratio F_sov_workloads bas se transformerait en levier geopolitique : les Etats-Unis pourraient conditionner l'acces aux modeles frontier (GPT-5, Claude, Gemini) a l'alignement strategique de la juridiction beneficiaire. La consommation massive de tokens devient alors une consommation conditionnelle.",
    ]),
    ("D.5.3 Implications pour la lecture de la declaration Huang", [
        "Replacee dans ce cadre, la declaration de Jensen Huang acquiert une signification structurelle. Un ingenieur europeen qui brule des tokens selon la prescription de Huang consomme du compute americain, execute sur des modeles americains, alimente par une infrastructure qu'il ne controle pas, protegee par une regulation qui ne le protege pas, et tarifee a un cout structurellement superieur du fait de l'architecture protectionniste documentee ci-dessus.",
        "Sa productivite individuelle peut augmenter. Sa dependance augmente certainement. La question combien de tokens consommes-tu ne signifie donc pas es-tu productif mais quel est ton niveau de dependance envers une infrastructure que tu ne controles pas. Pour une entreprise, c'est une question de risque. Pour un Etat, c'est une question de souverainete.",
    ]),
    ("D.6 Indicateurs de densite cognitive : adoption vs maitrise", [
        "Le vrai indicateur de densite cognitive d'une nation n'est pas le taux d'adoption de l'IA ni le volume de tokens consommes par ses entreprises. C'est le ratio de maitrise operationnelle : la proportion d'organisations capables de transformer une unite de compute en valeur mesurable, dans un pipeline controle, tracable et auditable.",
        "Considerons deux organisations depensant chacune 100 000 EUR annuels en tokens IA. La premiere fait tourner des agents sans boucle de controle, sans scoring, sans tracabilite. Elle produit du volume dont 80 pct est inutilisable en production. La seconde a construit un pipeline discipline ou chaque output IA est decompose, evalue et auditable. Elle produit quatre fois moins de volume mais chaque livrable est deployable. La seconde organisation presente une densite cognitive superieure, bien que sa consommation de tokens soit identique ou inferieure.",
        "Ce ratio - maitrise operationnelle rapportee a la dependance infrastructure - constitue l'indicateur central de la competitivite dans l'economie de densite cognitive. Il s'applique a l'echelle individuelle, organisationnelle et geopolitique.",
    ]),
    ("D.7 Conclusion", [
        "La declaration de Jensen Huang sur la consommation de tokens constitue un objet d'etude pertinent pour l'intelligence economique appliquee au secteur de l'IA. Lue comme un conseil managerial, elle est recevable dans un contexte etroit. Lue comme un acte de structuration de marche par le premier fournisseur mondial de compute IA, elle revele une dynamique de dependance que le concept d'economie de densite cognitive permet de formaliser.",
        "Les donnees empiriques disponibles (MIT, PwC, Forrester, Gartner, IBM) montrent que la consommation massive de tokens ne se traduit pas, dans la grande majorite des cas, en valeur mesurable. Le principal beneficiaire de l'augmentation de cette consommation reste le fournisseur d'infrastructure, non l'organisation consommatrice.",
        "L'indice CACI Power Mode, en integrant les dimensions energie, semi-conducteurs, compute et regulation selon la formule geometrique F^0,40 x L^0,20 x R^0,15 / E^0,25, quantifie l'asymetrie structurelle (ratio US/UE de 3,46:1 pour un ratio brut compute installe de 17,6:1, snapshot avril 2026) qui sous-tend cette dynamique. La decomposition Phys/Sov complete la lecture en distinguant compute installe (UE 99 pct souveraine) et workloads cloud (UE environ 28 pct souveraine).",
        "Dans ce cadre, l'objectif pour la France et l'Europe n'est pas l'autarcie technologique, mais la capacite de choisir : maitriser le ratio entre valeur produite et dependance consentie, a chaque niveau de la chaine. La doctrine Huang sur la densite cognitive doit etre lue non comme une injonction productiviste universelle, mais comme un signal de structuration de marche dont les beneficiaires structurels (NVIDIA, hyperscalers US) sont identifies.",
    ]),
]


TABLES = [
    ("Tableau D.1. Donnees empiriques sur le ROI des projets GenAI en entreprise (2025-2026).",
     "Source : compilation de l'auteur a partir de cinq enquetes independantes.",
     [
         ["Source", "Annee", "Constat principal"],
         ["MIT NANDA 'The GenAI Divide'", "2025",
          "95 pct des projets GenAI en entreprise n'ont produit aucun impact mesurable sur le P&L"],
         ["PwC CEO Survey (Davos)", "2026",
          "56 pct des CEO declarent que l'IA n'a pas produit de benefices significatifs ; 12 pct rapportent des gains couts plus revenus"],
         ["Forrester", "2025",
          "15 pct des decideurs IA rapportent un impact positif sur la rentabilite ; 25 pct des depenses IA 2026 reportees a 2027"],
         ["Gartner", "2025",
          "60 pct des projets IA abandonnes d'ici fin 2026 (donnees non AI-ready)"],
         ["IBM IBV", "2025",
          "25 pct des initiatives IA ont livre le ROI attendu ; 16 pct deployees a l'echelle"],
     ]),
]


NOTES = [
    "Jensen Huang, All-In Podcast, GTC San Jose, 20 mars 2026. Citation directe confirmee par Business Insider, Yahoo Finance, CNBC, The Decoder.",
    "Jensen Huang, keynote GTC 2026, San Jose, 18 mars 2026. Reference au budget tokens equivalent a environ la moitie du salaire de base comme composante d'attractivite dans le recrutement d'ingenieurs.",
    "Estimations consolidees SIA (Semiconductor Industry Association), McKinsey, Epoch AI GPU Clusters Dataset (2025).",
    "Pizzi, F. (2026), 'AI for Americans First : Protectionnisme IA americain, recomposition de l'ordre technologique mondial et consequences pour la France et l'Europe (2026-2030)', Universite Paris-Sorbonne, 11 chapitres, environ 120 pages, 196 notes. Tableau de bord public : https://mo0ogly.github.io/America-First-IA/dashboard/. Depot : https://github.com/mo0ogly/America-First-IA",
    "Epoch AI GPU Clusters Dataset (2025) ; AIE Electricity 2024 Report. Snapshot avril 2026 : USA 76,9 pct du compute IA operationnel mondial, UE(13) 3,3 pct, ratio brut 17,6:1, ratio CACI Power Mode 3,46:1. Detail methodologique dans le chapitre II et l'annexe A (annexe econometrique CACI).",
    "Bureau of Industry and Security (BIS), rulings export controls ; Section 232 tariffs (janvier 2026). Capex 2026 hyperscalers US : Amazon 200 Md USD, Alphabet 185 Md USD, Microsoft 145 Md USD, Meta 135 Md USD, Oracle 50 Md USD, total 660-690 Md USD. Analyse detaillee dans le chapitre IV de AI for Americans First.",
    "Construction Today (novembre 2025), Japon 550 Md USD investis aux US. Analyse des flux d'investissement dans le chapitre VI ter (Consequences pour l'Asie) de AI for Americans First.",
    "MIT NANDA Initiative (2025), 'The GenAI Divide : State of AI in Business 2025'. 52 entretiens dirigeants, enquete aupres de 153 responsables, analyse de 300 deploiements publics.",
    "PwC, 28th Annual Global CEO Survey, presente a Davos, janvier 2026.",
    "Forrester, 'AI Investment & ROI Outlook', 2025.",
    "Gartner, IT Symposium 2025 et previsions CIO Survey 2026.",
    "IBM Institute for Business Value, CEO Study, mai 2025.",
    "Synergy Research Group (T3 2025), 'Hyperscaler Cloud Infrastructure'. Part des hyperscalers US dans le cloud public europeen : environ 72 pct (AWS, Azure, GCP), F_sov_workloads UE environ 0,28. Statista Enterprise Cloud Market Share EU (2025).",
]


def build(out_dir: Path) -> Path:
    """Build the FR Annexe D Note Densite Cognitive Huang .docx."""
    log.info("Building Annexe D Huang [FR] -> Annexe_D_Densite_Cognitive_Huang_FR.docx")
    doc = init_document()
    add_cover(doc, chapter_label=CHAPTER_LABEL,
              chapter_subtitle="Note de recherche - Economie de densite cognitive")
    add_chapter_header(doc, label=CHAPTER_LABEL,
                       title=CHAPTER_TITLE, intro=CHAPTER_INTRO)
    for title, paragraphs in SECTIONS:
        render_section(doc, title, paragraphs)
    for caption, source, rows in TABLES:
        render_table(doc, caption, source, rows)
    render_notes(doc, NOTES)
    render_license(doc, "AI for Americans First - Fabrice Pizzi - Annexe D Doctrine Huang")

    out = out_dir / "Annexe_D_Densite_Cognitive_Huang_FR.docx"
    doc.save(out)
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    build(Path(__file__).parent)
