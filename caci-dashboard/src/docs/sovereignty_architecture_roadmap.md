# Sovereignty Audit: Technical Architecture & Future Roadmap

This document provides a detailed explanation of the **Sovereignty Audit** implementation in the CACI Dashboard, intended for future development (e.g., with Claude or other models).

## 1. Core Concept: The Sovereignty Gap
The CACI distinguishes between two compute factors:
- **$F_{phys}$ (Physical Factor)**: Total compute on a nation's soil, regardless of owner.
- **$F_{sov}$ (Sovereign Factor)**: Compute owned by the host nation OR non-"hyperscaler" entities (Microsoft, Google, Amazon, Oracle).

**The Sovereignty Gap** = $F_{phys} - F_{sov}$. 
In a "2028 AI Blockade" scenario, $F_{sov}$ is the only reliable compute factor for national competitiveness.

## 2. Technical Implementation

### Data Consolidation (`useDataConsolidation.js`)
The hook parses `gpu_clusters.csv` and preserves two separate properties for each nation:
```javascript
base[k].f_total = Math.round(base[k].f_total); // Physical presence
base[k].f = Math.round(base[k].f);             // Sovereign control
```
- **Filter logic**: Clusters owned by US Hyperscalers (Azure, AWS, GCP, Oracle) are automatically treated as "foreign" unless the location is 'USA'.
- **UAE Baseline**: Since UAE is building massive capacity quickly through Hyperscalers, we manually override its factor with a 2028 projection where only ~14% is sovereign.

### Visual Audit Component (`SovereignCake`)
The audit is visualized using the **NVIDIA 5-Layer AI Stack** model:
- **L5: Chips (Silicon)**: The hardware base.
- **L4: Networking**: The regional interconnectivity.
- **L3: Compute (Infrastructure)**: GPU data centers (Data-driven: $F_{sov}/F_{phys}$).
- **L2: Software Stack**: Frameworks and libraries.
- **L1: AI Services**: Deployed applications and APIs.

### Strategic Metadata (`LAYER_METADATA`)
Each nation is assigned a "Strategic Archetype" that determines the labels and colors in the Audit:
- **USA**: `Leader` status across all layers (Gold style).
- **China**: `Self-Sufficient` and `Leading` status (Red style).
- **UAE**: `Imported` and `Vulnerable` status (Vibrant style - high hyperscaler reliance).
- **EU**: `Dependent` on silicon, `Balanced` on software (Navy style).

## 3. The 5-Layer Accordion
To improve clarity, a `SovereigntyAccordion` was added to `CountryComparison.jsx`. It explains the "kill-switches" and jurisdictional boundaries of each layer.

## 4. Proposed Roadmap & Evolutions

### A. Dynamic Software Stack Maturity
- **Goal**: Instead of static labels ("Balanced", "Sovereign"), use a sub-index based on Hugging Face model downloads, local contributions to PyTorch/TensorFlow, or open-source volume.
- **Implementation**: Fetch data from GitHub/Hugging Face APIs to score software sovereignty.

### B. Silicon Supply Chain Integration
- **Goal**: Differentiate L5 (Chips) based on domestic EDA tools and fabrication node size (e.g., 2nm vs 14nm).
- **Implementation**: Map nations to their known semiconductor IP and assembly capabilities.

### C. Network Blockade Simulation
- **Goal**: In "Sovereign Mode", simulate the impact of losing L4 (Networking) on latency and bandwidth for cross-border AI inference.
- **Implementation**: Add a "Latency Penalty" variable to the CACI formula when sovereignty is <50%.

### D. Real-Time Geopolitical Risk Index
- **Goal**: Dynamically adjust the "Sovereignty" weight based on current geopolitical tension scores (e.g., Council on Foreign Relations data).

---
**How to resume with Claude:**
1. Point Claude to `CountryComparison.jsx` for the visual logic.
2. Review the `OWNER_COUNTRY_MAP` in `useDataConsolidation.js` to refine the definition of "foreign-controlled" clusters.
3. Update the `LAYER_METADATA` object in `CountryComparison.jsx` to reflect recent geopolitical shifts.
