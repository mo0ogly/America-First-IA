# FAQ — Volume 3 : Comprendre le Ratio CACI
## Compute-Adjusted Competitiveness Index — Méthodologie, Robustesse et Interprétation
**Fabrice Pizzi — Université Paris Sorbonne, Avril 2026 (Édition Révisée)**

---

> **Note sur cette édition révisée :** Ce document remplace la version de février 2026. La formule CACI a été affinée à la suite d'un audit interne : (1) l'architecture dual-paradigme (Puissance Absolue vs Intensité Économique) est désormais explicite ; (2) l'analyse de sensibilité aux poids est formalisée ; (3) le « Small Economy Normalization Bias » précédemment non documenté est maintenant explicitement documenté comme choix méthodologique délibéré, et non comme une erreur.

---

## Partie I — Fondements Conceptuels

### Q1. Qu'est-ce que le CACI et pourquoi a-t-il été créé ?

Le **Compute-Adjusted Competitiveness Index (CACI)** est un indice composite synthétique qui quantifie la puissance IA structurelle d'une nation en intégrant quatre piliers habituellement mesurés séparément mais jamais combinés dans la littérature académique existante :

| Pilier | Variable | Poids (référence) | Source |
|---|---|---|---|
| Capacité de Compute IA | F — PetaFLOPs (clusters existants) | 40% | Epoch AI (2025–2026) |
| Coût de l'infrastructure énergétique | E — $/MWh (moyenne industrielle) | 25% | AIE (2025) |
| Capital humain IA | L — M travailleurs STEM | 20% | Banque Mondiale / LinkedIn AI Talent |
| Accès géopolitique au compute | R — Tier de contrôle export (0,1/0,5/1,0) | 15% | BIS / White House AI Action Plan 2026 |

Le CACI a été créé parce que les benchmarks existants (IMF AI Preparedness Index, Tortoise Global AI Index, Stanford HAI) mesurent la **préparation** ou l'**adoption** — pas la puissance compute structurelle ancrée dans le matériel. Aucun n'explique l'écart de productivité IA de 7:1 à 12:1 entre les USA et l'UE identifié par McKinsey (2025).

---

### Q2. Quelle est la formule fondamentale ?

Le CACI utilise un **composite géométrique pondéré** — forme académique standard :

```
CACI = F^0,40 × L^0,20 × R^0,15 / E^0,25
```

**Pourquoi géométrique (fonction puissance) et non arithmétique (somme pondérée) ?**
- Interaction multiplicative : un pays a besoin des *quatre* piliers en même temps. Une nation disposant d'un compute énorme mais sans accès géopolitique (R=0,1) est correctement pénalisée — les sommes arithmétiques masqueraient cela.
- Standard dans la littérature : l'IDH de l'ONU (2010+), l'ICI du WEF et les indicateurs composites de l'OCDE utilisent tous des formes géométriques pour les indices multi-piliers (Manuel de l'OCDE sur les indicateurs composites, 2008 ; Nardo et al., 2005).
- Évite la domination d'un seul facteur : l'exposant sous-linéaire (0,40 < 1) amortit l'avantage brut en compute.

---

### Q3. Pourquoi deux modes — « Puissance Absolue » et « Intensité Économique » ?

Il s'agit de l'innovation méthodologique la plus importante de la révision d'avril 2026.

**Mode 1 — Puissance Absolue (mode par défaut, recommandé pour l'analyse géopolitique) :**
```
CACI_power = F^0,40 × L^0,20 × R^0,15 / E^0,25
```
- Pas de normalisation par le PIB
- Mesure l'effet de levier matériel total : qui contrôle le plus de compute réel, ajusté pour le coût énergétique et l'accès réglementaire
- Ratio USA/UE : **~7–12:1** (confirmé par l'analyse de sensibilité aux poids)
- Ratio USA/France : **~8:1**
- Validé par rapport aux données réelles de charge IT en GW (USA : 75 GW, UE : 35 GW, selon CFG 2025)

**Mode 2 — Intensité Économique (instrument de recherche, à utiliser avec précaution) :**
```
CACI_intensity = F^0,40 × L^0,20 × R^0,15 / (E^0,25 × PIB)
```
- PIB au dénominateur
- Mesure la *densité de compute par unité de production économique*
- Analogue au PIB par habitant vs PIB total — la Norvège peut « dominer » les USA en PIB/habitant même si le PIB total américain est 50× supérieur
- Dans ce mode, la France peut dépasser les USA — c'est **intentionnel et documenté** : cela démontre le « Small Economy Normalization Bias » contre lequel la Note Académique 2026 met en garde
- **Ne pas utiliser pour tirer des conclusions stratégiques sur la puissance absolue**

La séparation constitue la contribution académique : des études antérieures (ex. Oxford Internet Institute AI Governance Index 2024) utilisaient implicitement la forme Intensité et sous-estimaient systématiquement la domination américaine.

---

## Partie II — Robustesse et Calibration des Poids

### Q4. Comment les poids (40/25/20/15) ont-ils été choisis ?

Les poids sont **motivés empiriquement** mais pas encore estimés par régression. Leur rationalité :

- **F = 40%** : Le compute est le principal facteur de production dans l'entraînement et l'inférence des LLM. Un GPU H100 produisant 2 000 TFLOP/s pendant un an représente environ 30 000 $ de compute d'entraînement — bien supérieur aux composantes énergétique ou salariale par unité de production équivalente. Cohérent avec Goldfarb & Trefler (2022) sur le compute comme GPT (Technologie à Usage Général) et Agrawal, Gans & Goldfarb (2019) sur l'IA comme machine de prédiction.

- **E = 25%** : L'énergie est la contrainte structurelle post-2026. L'électricité industrielle américaine moyenne est de 0,085 $/kWh contre 0,14–0,18 $/kWh dans l'UE — un désavantage structurel de 1,6–2,1× pour les runs d'entraînement européens. Cohérent avec les trajectoires de consommation énergétique des data centers de l'AIE (2025).

- **L = 20%** : La main-d'œuvre STEM est importante pour le déploiement et le fine-tuning, mais moins déterminante que le compute brut pour l'entraînement de modèles frontières. L'avantage américain est réel (3,5M de travailleurs IA contre 0,65M pour la France) mais plus faible en ratio que l'écart de compute.

- **R = 15%** : Le facteur de tier géopolitique (régime de contrôle export Trump 2.0, règle BIS de janvier 2026) capture une contrainte structurelle invisible dans les autres indices. La Chine (Tier 3, R=0,1) est pénalisée 10× par rapport aux alliés de Tier 1. C'est le paramètre le plus contesté — voir Q5.

**Limite reconnue** : Les poids n'ont pas été estimés par analyse en composantes principales ou pondération par entropie. C'est signalé comme priorité pour des recherches empiriques futures (voir Q7).

---

### Q5. Qu'est-ce que le facteur R et est-il défendable ?

Le **Facteur Réglementaire (R)** traduit le régime de contrôle export américain en un scalaire :

| Tier | Pays | Valeur R | Rationalité |
|---|---|---|---|
| Tier 1 (accès total) | USA, UE, Royaume-Uni, Japon, Corée, Australie... | 1,00 | Accès illimité aux puces selon l'AI Diffusion Rule |
| Tier 2 (plafonné) | Inde, Brésil, Émirats, ASEAN... | 0,50 | Plafonds GPU quantitatifs, vérification d'utilisation finale |
| Tier 3 (bloqué) | Chine, Russie, Iran... | 0,10 | Restriction quasi-totale sur les puces de classe H100/H200 |

**La valeur 0,1 est-elle scientifiquement défendable ?** Partiellement. La direction ordinale est robuste (Tier 3 ≪ Tier 2 ≪ Tier 1). La valeur cardinale (0,1 vs 0,15 ou 0,05) est théoriquement contestée et devrait faire l'objet de travaux empiriques futurs. Cependant, **l'analyse de sensibilité (Panneau C du Robustness Check) montre que même quand le poids de R est réduit vers zéro, la domination américaine est inchangée** — car l'écart de compute seul (ratio F de 76:1 vs France, 7:1 vs UE) suffit à maintenir la conclusion structurelle.

---

### Q6. Que teste le Robustness Check ?

L'analyse de sensibilité formelle (implémentée dans l'onglet interactif « 🔬 Robustness Check » du dashboard) teste :

1. **Perturbation mono-facteur** : Chaque poids varie de ±5 points de pourcentage sur 7 étapes (±15% au total), les 3 autres poids étant renormalisés proportionnellement. Les scores CACI résultants sont tracés pour les 8 pays.

2. **Tableau de stabilité des rangs multi-scénarios** : 8 scénarios de perturbation prédéfinis (F±15%, E±15%, L+15%, R±15%) sont appliqués indépendamment. Pour chaque scénario, les rangs et scores des pays sont calculés. Les changements de rang (↑/↓) sont signalés.

3. **Variance des scores** : Écart-type des scores CACI sur l'ensemble des 8 perturbations. σ faible = résultat robuste ; σ élevé = résultat dépendant des poids.

**Résultats (calibration Avril 2026) :**
- USA rang #1 : **stable sur TOUTES les perturbations** ✅
- Chine rang #2 (mode Puissance Absolue) : **stable** ✅
- UE rang #3 : **stable** ✅
- France (isolée) : reste sous USA/Chine/UE/Royaume-Uni en puissance absolue — **robuste** ✅
- Sensibilité au facteur R : **paramètre le plus volatile**, reconnu en Q5.

Suit les standards d'analyse de sensibilité de Saltelli, Tarantola & Campolongo (2000) et du Guide JRC-OCDE (2008).

---

### Q7. Quelles sont les limites du CACI ?

Limites ouvertement documentées (conformément à la norme académique de transparence sur l'incertitude) :

1. **Les poids ne sont pas estimés** — ils sont calibrés théoriquement. Un modèle d'équations structurelles ou une estimation bayésienne des poids contre des résultats observables (dépôts de brevets IA, densité de startups IA, revenus export IA) renforcerait l'indice.

2. **La cardinalité du facteur R est contestée** — les valeurs de Tier (1,0/0,5/0,1) sont des jugements qualitatifs. Un score continu basé sur les volumes réels d'importation de puces serait plus rigoureux.

3. **Incertitude sur les données de compute** — Epoch AI trace les clusters connus ; le compute militaire/gouvernemental non divulgué est exclu. Cela sous-estime probablement la capacité réelle de la Chine et des USA.

4. **Instantané statique** — le CACI est calculé à un instant donné. Une version dynamique suivant le déploiement trimestriel de compute améliorerait la validité temporelle.

5. **Déflateur PIB** — en mode Intensité, le PIB n'est pas corrigé en PPA. L'utilisation de la PPA réduirait légèrement l'écart France vs USA.

6. **Pas d'intervalles de confiance** — étant donné l'incertitude des données, un intervalle de confiance bootstrappé sur le ratio CACI serait le standard académique. Cible : USA/UE = 10:1 ± 2 (IC à 95%).

---

## Partie III — Résultats Empiriques et Interprétation

### Q8. Quels sont les résultats clés ?

**Mode Puissance Absolue (Analyse Géopolitique) :**

| Rang | Pays | Score CACI (USA=100) | Ratio USA/X |
|---|---|---|---|
| 1 | USA | 100 | — |
| 2 | Chine | ~25–35 | ~3–4:1 |
| 3 | UE (agrégé) | ~10–15 | ~7–10:1 |
| 4 | Asie Hors-Chine | ~8–12 | ~8–12:1 |
| 5 | Royaume-Uni | ~5–8 | ~12–20:1 |
| 6 | Inde | ~3–5 | ~20–30:1 |
| 7 | France (isolée) | ~2–3 | ~35–50:1 |

Note : Les scores varient légèrement selon le scénario de perturbation — les plages ci-dessus reflètent l'intervalle de robustesse.

### Q9. Pourquoi la France dépasse-t-elle parfois les USA en mode Intensité ? Est-ce une erreur ?

Ce n'est pas une erreur — c'est une **démonstration méthodologique délibérée**. La Note Académique 2026 avertit que « les indices normalisant par le PIB sous-estiment systématiquement la domination structurelle américaine ». Le mode Intensité rend ce biais *visible et quantifiable*.

Analogie : La Norvège a un PIB par habitant plus élevé que les USA. Cela ne signifie pas que la Norvège est économiquement plus puissante — cela signifie qu'elle est *plus efficiente par personne*. La France ayant un ratio compute/PIB plus élevé que les USA ne signifie pas que la France domine l'IA — cela signifie que le stock de compute français est important relativement à sa taille économique. L'implication stratégique est opposée : la France est une économie de compute efficiente et concentrée qui reste un acteur de petite taille en termes absolus.

---

## Partie IV — Contexte Académique et Citation

### Q10. Comment le CACI se compare-t-il aux indices existants ?

| Indice | Mesure | Normalisé PIB? | Compute explicite? | Facteur R? |
|---|---|---|---|---|
| IMF AI Preparedness Index | Préparation (4 piliers) | Oui | Non | Non |
| Tortoise Global AI Index | Adoption + investissement | Partiellement | Non | Non |
| Stanford HAI Index | Recherche + politique | Non | Partiel | Non |
| Oxford OII AI Governance | Capacité de gouvernance | Oui | Non | Non |
| **CACI (ce travail)** | **Puissance compute absolue** | **Non (mode Power)** | **Oui (PetaFLOPs)** | **Oui (tiers BIS)** |

Le différenciateur du CACI est l'inclusion explicite du **compute physique comme facteur de production primaire** et de **l'accès géopolitique comme contrainte structurelle** — aucun des deux n'apparaît dans un index majeur existant.

### Q11. Quelle est la citation recommandée ?

```
Pizzi, F. (2026). Compute-Adjusted Competitiveness Index (CACI) : 
Construction, Architecture Dual-Paradigme et Analyse de Robustesse. 
Working Paper, Université Paris Sorbonne. Dashboard interactif :
https://mo0ogly.github.io/America-First-IA/dashboard/

Méthodologie d'analyse de sensibilité aux poids :
Saltelli, A., Tarantola, S., & Campolongo, F. (2000). Sensitivity analysis 
as an ingredient of modeling. Statistical Science, 15(4), 377–395.

OCDE/JRC (2008). Guide de construction d'indicateurs composites :
méthodologie et guide d'utilisation. Éditions OCDE.
```

---

*Dernière mise à jour : Avril 2026 — Remplace FAQ Volume 3 (Édition Février 2026)*
*Dashboard : [https://mo0ogly.github.io/America-First-IA/dashboard/](https://mo0ogly.github.io/America-First-IA/dashboard/)*
