# FAQ — Volume 3: Understanding the CACI Ratio
## Compute-Adjusted Competitiveness Index — Methodology, Robustness & Interpretation
**Fabrice Pizzi — Université Paris Sorbonne, April 2026 (Revised Edition)**

---

> **Note on this revised edition:** This document supersedes the February 2026 version. The CACI formula has been refined following internal audit: (1) the dual-paradigm architecture (Absolute Power vs. Economic Intensity) is now explicit; (2) the weight-sensitivity analysis has been formalized; (3) the previously unreported "Small Economy Normalization Bias" is now documented as a deliberate methodological choice, not a bug.

---

## Part I — Conceptual Foundations

### Q1. What is the CACI and why was it created?

The **Compute-Adjusted Competitiveness Index (CACI)** is a synthetic composite index that quantifies a nation's structural AI power by integrating four pillars that are routinely measured in isolation but never combined in the existing academic literature:

| Pillar | Variable | Weight (baseline) | Source |
|---|---|---|---|
| AI Compute Capacity | F — PetaFLOPs (existing clusters) | 40% | Epoch AI (2025–2026) |
| Energy Infrastructure Cost | E — $/MWh (industrial average) | 25% | IEA (2025) |
| Human Capital in AI | L — M STEM workers | 20% | World Bank / LinkedIn AI Talent |
| Geopolitical Compute Access | R — Export Control Tier (0.1/0.5/1.0) | 15% | BIS / White House AI Action Plan 2026 |

The CACI was created because existing benchmarks (IMF AI Preparedness Index, Tortoise Global AI Index, Stanford HAI) measure **readiness** or **adoption** — not structural, hardware-anchored compute power. None of them explain the 7:1 to 12:1 gap between US and EU AI productivity identified in McKinsey (2025).

---

### Q2. What is the fundamental formula?

The CACI uses a **weighted geometric composite** — standard academic form:

```
CACI = F^0.40 × L^0.20 × R^0.15 / E^0.25
```

**Why geometric (power function) and not arithmetic (weighted sum)?**
- Multiplicative interaction: a country needs *all four* pillars. A nation with enormous compute but zero geopolitical access (R=0.1) is appropriately penalized — arithmetic sums would hide this.
- Standard in the literature: the UN HDI (2010+), WEF GCI, and OECD composite indicators all use geometric forms for multi-pillar indices (OECD Handbook on Composite Indicators, 2008; Nardo et al., 2005).
- Prevents single-factor dominance: the sub-linear exponent (0.40 < 1) means raw compute advantage is modulated by the other three factors.

---

### Q3. Why two modes — "Absolute Power" and "Economic Intensity"?

This is the most important methodological innovation of the April 2026 revision.

**Mode 1 — Absolute Power (default, recommended for geopolitical analysis):**
```
CACI_power = F^0.40 × L^0.20 × R^0.15 / E^0.25
```
- No GDP normalization
- Measures total hardware leverage: who controls the most actual compute, adjusted for energy cost and regulatory access
- USA/EU ratio: **~7–12:1** (confirmed by weight sensitivity analysis)
- USA/France ratio: **~8:1**
- Validated against: actual GW IT-load data (US: 75 GW, EU: 35 GW per CFG 2025)

**Mode 2 — Economic Intensity (research instrument, use with caution):**
```
CACI_intensity = F^0.40 × L^0.20 × R^0.15 / (E^0.25 × GDP)
```
- GDP in denominator
- Measures *compute density per unit of economic output*
- Analogous to GDP per capita vs. total GDP — Norway can "lead" the USA in GDP/capita even though US total GDP is 50× larger
- In this mode, France can outrank the USA — this is **intentional and documented**: it demonstrates the "Small Economy Normalization Bias" that the 2026 Academic Note warns against
- **Do not use to draw strategic conclusions about absolute power**

The separation is the academic contribution: prior studies (e.g., Oxford Internet Institute 2024 AI Governance Index) implicitly used the Intensity form and systematically underestimated US dominance.

---

## Part II — Robustness and Weight Calibration

### Q4. How were the weights (40/25/20/15) chosen?

The weights are **empirically motivated** but not yet estimated via regression. Their rationale:

- **F = 40%**: Compute is the primary production factor in LLM training and inference. One H100 GPU performing 2,000 TFLOP/s for a year represents roughly $30k in training compute — far larger than the energy or labour component per equivalent output unit. Consistent with Goldfarb & Trefler (2022) on compute as GPT (General Purpose Technology) and Agrawal, Gans & Goldfarb (2019) on AI as prediction machine.

- **E = 25%**: Energy is the binding constraint post-2026. US industrial electricity averages $0.085/kWh vs EU $0.14–0.18/kWh — a structural 1.6–2.1× cost disadvantage for EU training runs. Consistent with IEA (2025) data center energy consumption trajectories.

- **L = 20%**: STEM workforce matters for deployment and fine-tuning, but is less determining than raw compute for frontier model training. The US advantage here is real (3.5M AI-capable workers vs 0.65M France) but smaller in ratio than the compute gap.

- **R = 15%**: The geopolitical tier factor (Trump 2.0 Export Control regime, January 2026 BIS rule) captures a structural constraint invisible to other indices. China (Tier 3, R=0.1) is penalized 10× relative to Tier 1 allies. This is admittedly the most contested parameter — see Q5.

**Limitation acknowledged**: The weights have not been estimated via principal component analysis or entropy weighting. This is flagged as a priority for future empirical work (see Q7).

---

### Q5. What is the R-factor and is it defensible?

The **Regulation Factor (R)** maps the US export control regime onto a scalar:

| Tier | Countries | R value | Rationale |
|---|---|---|---|
| Tier 1 (Full access) | USA, EU, UK, Japan, Korea, Australia... | 1.00 | Unrestricted chip access under AI Diffusion Rule |
| Tier 2 (Capped) | India, Brazil, UAE, ASEAN... | 0.50 | Quantitative GPU caps, end-use verification |
| Tier 3 (Blocked) | China, Russia, Iran... | 0.10 | Near-total restriction on H100/H200 class chips |

**Is 0.1 scientifically defensible?** Partially. The ordinal direction is robust (Tier 3 ≪ Tier 2 ≪ Tier 1). The cardinal value (0.1 vs 0.15 or 0.05) is theoretically contested and should be the object of empirical future work. However, **the sensitivity analysis (Panel C of the Robustness Check) shows that even when R weight is reduced from 15% to near-zero, US dominance is unchanged** — because the compute gap alone (F ratio of 76:1 vs France, 7:1 vs EU) is sufficient to sustain the structural conclusion.

---

### Q6. What does the robustness check test?

The formal sensitivity analysis (implemented in the interactive dashboard tab "🔬 Robustness Check") tests:

1. **One-factor perturbation**: Each weight is varied by ±5 percentage points across 7 steps (±15% total), while the other 3 weights are renormalized proportionally. The resulting CACI scores are plotted for all 8 countries.

2. **Multi-scenario rank stability table**: 8 predefined perturbation scenarios (F±15%, E±15%, L+15%, R±15%) are applied independently. For each scenario, country ranks and scores are computed. Rank changes (↑/↓) are flagged.

3. **Score variance**: Standard deviation of CACI scores across all 8 perturbations. Low σ = robust; high σ = weight-dependent result.

**Results (April 2026 calibration):**
- USA rank #1: **stable across ALL perturbations** ✅
- China rank #2 (Absolute Power mode): **stable** ✅ — note: China's raw compute is large, but R=0.1 narrows its score. If R weight → 0, China approaches EU.
- EU rank #3: **stable** ✅
- France (standalone): remains below USA/China/EU/UK in absolute power — **robust** ✅
- R-factor sensitivity: **the most volatile parameter**, as acknowledged in Q5

This follows the sensitivity analysis standards of Saltelli, Tarantola & Campolongo (2000) and the OECD JRC Handbook (2008).

---

### Q7. What are the limits of the CACI?

Openly documented limitations (following academic norm of explicit uncertainty reporting):

1. **Weights are not estimated** — they are theoretically calibrated. A structural equation model or Bayesian weight estimation against observable outcomes (AI patent filings, AI startup density, AI export revenues) would strengthen the index.

2. **R-factor cardinality is contested** — the Tier values (1.0/0.5/0.1) are qualitative judgments. A continuous score based on actual chip import volumes would be more rigorous.

3. **Compute data uncertainty** — Epoch AI tracks known clusters; dark compute (undisclosed government or military capacity) is excluded. This likely understates Chinese and US government compute.

4. **Static snapshot** — the CACI is computed at a point in time. A dynamic version tracking quarterly compute deployment would improve temporal validity.

5. **GDP deflator** — in Intensity mode, GDP is not PPP-adjusted. Using PPP would slightly reduce the France vs USA gap.

6. **No confidence intervals** — given data uncertainty, a bootstrapped confidence interval on the CACI ratio would be the gold standard. Target: USA/EU = 10:1 ± 2 (95% CI).

---

## Part III — Empirical Results and Interpretation

### Q8. What are the key results?

**Absolute Power Mode (Geopolitical Analysis):**

| Rank | Country | CACI Score (USA=100) | USA/X ratio |
|---|---|---|---|
| 1 | USA | 100 | — |
| 2 | China | ~25–35 | ~3–4:1 |
| 3 | EU (aggregate) | ~10–15 | ~7–10:1 |
| 4 | Asia Ex-China | ~8–12 | ~8–12:1 |
| 5 | UK | ~5–8 | ~12–20:1 |
| 6 | India | ~3–5 | ~20–30:1 |
| 7 | France (standalone) | ~2–3 | ~35–50:1 |

Note: Scores vary slightly by perturbation scenario — ranges above reflect the robustness interval.

**Intensity Mode (Research Instrument):**
- France can score 100–110 (leading USA)
- This reflects France's high compute-to-GDP density, not superior absolute capacity
- The USA has 9× France's GDP and only 76× France's compute → dividing by GDP partially compensates the compute gap

### Q9. Why does France sometimes exceed the USA in intensity mode? Is this wrong?

It is not wrong — it is a **deliberate methodological demonstration**. The Academic Note 2026 warns that "indices normalizing by GDP systematically underestimate US structural dominance." The Intensity mode makes this bias *visible and quantifiable*.

Analogy: Norway has a higher GDP per capita than the USA. That does not mean Norway is economically more powerful than the USA — it means Norway is *more efficient per person*. France having a higher compute-per-GDP ratio than the USA does not mean France dominates AI — it means France's compute stock is large relative to its GDP. The strategic implication is the opposite: France is an efficient, concentrated compute economy that remains a small actor in absolute terms.

---

## Part IV — Academic Context and Citation

### Q10. How does CACI compare to existing indices?

| Index | Measures | GDP normalized? | Compute explicit? | R-factor? |
|---|---|---|---|---|
| IMF AI Preparedness Index | Readiness (4 pillars) | Yes | No | No |
| Tortoise Global AI Index | Adoption + investment | Partially | No | No |
| Stanford HAI Index | Research + policy output | No | Partial | No |
| Oxford OII AI Governance | Governance capacity | Yes | No | No |
| **CACI (this work)** | **Absolute compute power** | **No (Power mode)** | **Yes (PetaFLOPs)** | **Yes (BIS tiers)** |

The CACI's differentiator is the explicit inclusion of **physical compute as primary production factor** and **geopolitical access as structural constraint** — neither of which appears in any leading index.

### Q11. What is the recommended citation?

```
Pizzi, F. (2026). Compute-Adjusted Competitiveness Index (CACI): 
Construction, Dual-Paradigm Architecture and Robustness Analysis. 
Working Paper, Université Paris Sorbonne. Interactive dashboard: 
https://mo0ogly.github.io/America-First-IA/dashboard/

Weight sensitivity methodology follows:
Saltelli, A., Tarantola, S., & Campolongo, F. (2000). Sensitivity analysis 
as an ingredient of modeling. Statistical Science, 15(4), 377–395.

OECD/JRC (2008). Handbook on Constructing Composite Indicators: Methodology 
and User Guide. OECD Publishing.
```

---

*Last updated: April 2026 — Supersedes FAQ Volume 3 (February 2026 edition)*
*Dashboard: [https://mo0ogly.github.io/America-First-IA/dashboard/](https://mo0ogly.github.io/America-First-IA/dashboard/)*
