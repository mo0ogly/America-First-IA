# AI for Americans First

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Status](https://img.shields.io/badge/Status-Active%20Research-blue.svg)]()
[![Language](https://img.shields.io/badge/Lang-FR%20%7C%20EN-informational.svg)]()

**Protectionnisme IA americain, recomposition de l'ordre technologique mondial et consequences pour la France et l'Europe (2026-2030)**

*Fabrice Pizzi — Universite Paris Sorbonne, 2026*

---

## Resume

Cette etude analyse les mecanismes et les consequences du protectionnisme IA americain sous l'administration Trump 2.0, en integrant quatre dimensions habituellement traitees separement dans la litterature : **energie**, **semi-conducteurs**, **compute** et **regulation**.

A partir d'un diagnostic empirique 2020-2026, de la construction d'un **indice de competitivite ajuste au compute (CACI)** et d'une matrice scenarielle 2x2, la recherche demontre que :

- La combinaison tarifs douaniers (25 %, Section 232) et controles a l'export cree un **avantage competitif structurel mesurable** (ratio CACI US/EU de 7 a 12:1)
- Les restrictions accelerent paradoxalement la construction d'un **ecosysteme IA chinois alternatif**
- L'ordre technologique mondial se fragmente en **blocs competitifs**

L'analyse comparative des reponses regionales (Europe, Amerique du Sud, Asie) revele des trajectoires de dependance fondamentalement differenciees.

---

## Acces rapide (sans installation Git)

| Document | Lien |
|----------|------|
| Chapitre I — Cadre theorique (FR, PDF) | [Chapitre_I_Introduction_Cadrage_Theorique.pdf](pdf/Chapitre_I_Introduction_Cadrage_Theorique.pdf) |
| Site web interactif | [Ouvrir le site](https://mo0ogly.github.io/America-First-IA/) |
| Dashboard CACI interactif | [Ouvrir le dashboard](https://mo0ogly.github.io/America-First-IA/dashboard/) |

---

## Structure de l'etude

| Ch. | Titre | Pages | Notes |
|-----|-------|-------|-------|
| I | Cadre theorique : protectionnisme technologique et IA | 12 | 22 |
| II | Methodologie : matrice scenarielle et indice CACI | 8 | 10 |
| III | Diagnostic empirique 2020-2026 | 11 | 20 |
| IV | Mecanismes de l'avantage competitif US | 9 | 19 |
| V | Scenarios prospectifs 2026-2030 et points de basculement | 11 | 16 |
| VI | Consequences pour la France et l'Europe | 10 | 14 |
| VI bis | Consequences pour l'Amerique du Sud et le Bresil | 11 | 19 |
| VI ter | Consequences pour l'Asie | 12 | 16 |
| VI quater | Consequences pour l'Afrique | — | — |
| VII | Recommandations strategiques | 11 | 18 |
| Concl. | Du protectionnisme IA a la recomposition de l'ordre technologique | 8 | 3 |
| **Total** | | **103** | **157** |

---

## Figures

Le dossier `figures/` contient 22 figures academiques en trois langues (FR, EN, PT-BR) :

- **Fig 1.1** — Consommation energetique des data centers par region
- **Fig 1.2** — Marche des semi-conducteurs (valeur, part IA)
- **Fig 1.3** — Compute gap : distribution du compute IA mondial
- **Fig 1.4** — AI Adoption Gap par region
- **Fig 1.5** — US Chokepoints : points de controle americains
- **Fig 1.6** — Cadre theorique integre

---

## Citation

```bibtex
@techreport{pizzi2026aifirst,
  author    = {Pizzi, Fabrice},
  title     = {AI for Americans First: Protectionnisme IA americain,
               recomposition de l'ordre technologique mondial
               et consequences pour la France et l'Europe (2026-2030)},
  institution = {Universite Paris Sorbonne},
  year      = {2026},
  month     = {February},
  type      = {Academic Research},
  note      = {103 pages, 157 notes, 22 figures}
}
```

---

## Maintenance du Dashboard Interactif

Le dashboard interactif CACI est developpé en React (via Vite) dans le dossier `caci-dashboard/`. 

Puisque le site principal est hébergé via GitHub Pages depuis le dossier `docs/`, les fichiers React compilés doivent y être placés. Pour appliquer des modifications au code source du dashboard et les publier :

1. Naviguer vers le dossier source du dashboard :
   ```bash
   cd caci-dashboard
   ```
2. Recompiler l'application pour la production :
   ```bash
   npm run build
   ```
3. Copier manuellement le contenu généré dans le dossier `dist/` vers le dossier cible `docs/dashboard/` :
   ```bash
   # Sur Windows (PowerShell)
   Copy-Item -Path "dist\*" -Destination "..\docs\dashboard\" -Recurse -Force
   
   # Ou sur Linux/macOS
   cp -R dist/* ../docs/dashboard/
   ```
   
Une fois poussés sur la branche `main`, les changements seront automatiquement visibles sur la page `https://mo0ogly.github.io/America-First-IA/dashboard/`.

---

## Licence et Avertissement

Ce travail, "America-First-IA", est mis a disposition selon les termes de la **Licence Creative Commons Attribution - Pas d'Utilisation Commerciale - Partage dans les Memes Conditions 4.0 International (CC BY-NC-SA 4.0)**.

Vous etes libre de partager et d'adapter le materiel a des fins non commerciales, a condition de crediter de maniere appropriee **Fabrice Pizzi (Universite Paris Sorbonne)** et de diffuser vos contributions avec la meme licence.

Ce document est fourni **a des fins educatives et de recherche uniquement**.

---

*Fabrice Pizzi — [GitHub](https://github.com/mo0ogly) — Universite Paris Sorbonne, 2026*
