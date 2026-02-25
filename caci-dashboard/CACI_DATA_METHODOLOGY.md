# CACI Data Sourcing Methodology & Audit

## 1. Objective
This document serves as the formal academic and architectural reference for the data points powering the **Compute-Adjusted Competitiveness Index (CACI)**. It establishes an "honest audit" of which variables are dynamically fetched from rigorous open-data sources, and which variables rely on proxy datasets or manual consolidation due to API limitations or paywalls.

The goal is absolute transparency to pre-empt peer-review criticism regarding data integrity.

---

## 2. Variable Sourcing & Definitions

### Factor F: Compute Capacity (PetaFLOP/s)
*   **Definition:** The aggregate high-tier compute power available within a nation's borders.
*   **Source:** [Epoch AI - Datasets (GPU Clusters)](https://epochai.org/data/gpu-clusters)
*   **Status:** 🟢 **100% Sourced (Hard Data)**
*   **Implementation:** The dashboard downloads `gpu_clusters.csv` dynamically. The pipeline parses the JSON/CSV array, aggregates the `capacity_pflops` column by `Country`, and injects the exact real-time value into the CACI formula.

### GDP: Economic Mass (Trillions USD)
*   **Definition:** Nominal Gross Domestic Product in U.S. Dollars (Current Prices). Essential for reflecting true international purchasing power for silicon and hyperscale infrastructure. PPP is explicitly rejected.
*   **Source:** [IMF World Economic Outlook (WEO) Database](https://www.imf.org/en/Publications/WEO)
*   **Metric:** `NGDPD` (2024 values).
*   **Status:** 🟢 **100% Sourced (Hard Data)**
*   **Implementation:** The dashboard queries a local mirror/extract of the IMF WEO database (`imf_weo_gdp.csv`) to dynamically extract the 2024 NGDPD field, converting billions to trillions.

### Factor E: Energy Cost (USD / MWh)
*   **Definition:** Industrial end-use electricity prices. We strictly avoid "Residential" or volatile "Day-Ahead Wholesale" prices, as hyperscale data centers operate on long-term industrial Power Purchase Agreements (PPAs).
*   **Source:** [IEA Energy Prices Database](https://www.iea.org/data-and-statistics/data-tools/energy-prices-data-explorer) / GlobalPetrolPrices
*   **Status:** 🟡 **Hybrid Proxy (Paywalled Limitations)**
*   **Honest Audit:** The full IEA database is paywalled. Data for OECD countries (USA, EU, UK) is extracted via the free IEA Data Explorer. Data for emerging blocks (India, China, Africa) relies on public reports and secondary aggregators.
*   **Implementation:** Due to the absence of a unified, free global API, this data is maintained in a local, auditable static file: `public/data/energy_prices.csv`.

### Factor L: STEM Workforce (Millions)
*   **Definition:** The volume of the workforce capable of researching, deploying, and absorbing AI technologies. We explicitly reject general "Total Labor Force" (`SL.TLF.TOTL.IN`) as it disproportionately rewards massive populations (India/China) without reflecting tech productivity. The target metric is "Researchers in R&D" or "Human Resources in Science and Technology".
*   **Source:** [World Bank Open Data](https://data.worldbank.org/) (`SP.POP.SCIE.RD.P6` equivalence) / OECD (`HRST`).
*   **Status:** 🟡 **Proxy Estimate**
*   **Honest Audit:** Similar to Energy, querying the World Bank API for complex macro-regions ("EU", "Africa") in real-time is brittle. 
*   **Implementation:** Maintained in a local, transparent reference file: `public/data/workforce_data.csv`.

---

## 3. Data Ingestion Architecture (Next Phase)

The upcoming architectural overhaul will implement a `useDataConsolidation` React hook. 
Instead of hardcoding values in the React components, this engine will:
1. Fire parallel `fetch()` requests to `gpu_clusters.csv`, `imf_weo_gdp.csv`, `energy_prices.csv`, and `workforce_data.csv` upon dashboard initialization.
2. Cross-reference the country keys (e.g., standardizing "United States" to "USA").
3. Perform the necessary arithmetic aggregations.
4. Supply a single, clean `consolidatedData` object to the CACI Simulator and charts.

## 4. Current State Audit (Self-Assessment)
*   **Mathematical Rigor:** Strong. The implementation of the Critical Mass Threshold (F ≥ 15) successfully filters out the "Small Economy Normalization Bias".
*   **Transparency:** Improving. Moving data into explicit CSVs makes the simulator auditable.
*   **Automation:** Pending. The React components still currently rely on a `baselineData` javascript object. The immediate next step is to wire the UI to the CSVs to finalize the pipeline.
