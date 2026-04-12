import React, { useState } from 'react';
import './CaciFormula.css';

const CaciFormula = () => {
  const [activeTooltip, setActiveTooltip] = useState(null);

  const tooltips = {
    caci: {
      title: "CACI Index (Weighted)",
      desc: "Compute-Adjusted Competitiveness Index. A weighted geometric composite indicator (40/25/20/15) capturing the interaction between compute stock, energy constraints, human capital, and geopolitical access.",
      source: "Sorbonne 2026 — Power: F^0.40 × L^0.20 × R^0.15 / E^0.25 | Intensity: ÷ GDP"
    },
    f: {
      title: "Factor F: Sovereign Compute (40%)",
      desc: "Total operational compute capacity (PetaFLOPs) under jurisdictional control. Weight reflects compute as the primary 'silicon floor' of AI capability.",
      source: "Data: Epoch AI / NIST 2026"
    },
    e: {
      title: "Factor E: Energy Cost (25%)",
      desc: "Industrial electricity cost (€/MWh). Acts as a structural constraint: the 'Energy Chokepoint' documented in the 2028 simulation.",
      source: "Data: IEA / Eurostat (Ajusté 2026)"
    },
    l: {
      title: "Factor L: Human Capital (20%)",
      desc: "STEM workforce and AI talent density. Captures the 'Absorptive Capacity'—the ability to convert raw compute into economic output.",
      source: "Data: OECD / LinkedIn AI Index"
    },
    r: {
      title: "Factor R: Regulation & Access (15%)",
      desc: "Geopolitical access factor (Tier 1/2/3). Measures the impact of US export controls, Section 232 tariffs, and 'Cloud Act' jurisdictional reach.",
      source: "Source: BIS / Trump 2.0 AI Action Plan"
    },
    gdp: {
      title: "GDP: Economic Normalizer",
      desc: "Gross Domestic Product. Normalizes capability into intensity, ensuring small nations with high 'AI Concentration' can be compared to superpowers.",
      source: "Data: World Bank / IMF WEO"
    }
  };

  return (
    <div className="formula-container">
      <div className="glass-card mb-4">
        <h2 className="section-title">The Compute-Adjusted Competitiveness Index (CACI)</h2>
        <p className="text-muted" style={{ fontSize: '0.9rem', marginBottom: '8px' }}>
          <em>Methodology: University Paris Sorbonne (2026)</em>
        </p>
        <hr className="section-bar" />
        <p className="text-muted mb-4">
          The CACI is a <strong>weighted geometric index</strong> that captures the interaction between five pillars of AI power: sovereign compute (F), human capital (L), regulatory access (R), energy cost (E), and GDP normalization. Unlike raw metrics, it penalizes energy dependence and rewards jurisdictional sovereignty and human capital.
        </p>

        <div className="formula-display">
          <div
            className="formula-block result-block"
            onMouseEnter={() => setActiveTooltip('caci')}
            onMouseLeave={() => setActiveTooltip(null)}
          >
            CACI
            <span className="power">(r,t)</span>
          </div>

          <div className="formula-equals">=</div>

          <div className="formula-fraction">
            <div className="numerator">
              <span className="bracket">[</span>
              <span
                className="formula-var var-f"
                onMouseEnter={() => setActiveTooltip('f')}
                onMouseLeave={() => setActiveTooltip(null)}
              >F<span className="sub">sov</span><sup style={{fontSize: '0.6em'}}>0.40</sup></span>
              <span className="formula-op">×</span>
              <span
                className="formula-var var-l"
                onMouseEnter={() => setActiveTooltip('l')}
                onMouseLeave={() => setActiveTooltip(null)}
              >L<sup style={{fontSize: '0.6em'}}>0.20</sup></span>
              <span className="formula-op">×</span>
              <span
                className="formula-var var-r"
                onMouseEnter={() => setActiveTooltip('r')}
                onMouseLeave={() => setActiveTooltip(null)}
              >R<sup style={{fontSize: '0.6em'}}>0.15</sup></span>
              <span className="bracket">]</span>
            </div>
            <div className="fraction-line"></div>
            <div className="denominator">
              <span className="bracket">[</span>
              <span
                className="formula-var var-e"
                onMouseEnter={() => setActiveTooltip('e')}
                onMouseLeave={() => setActiveTooltip(null)}
              >E<sup style={{fontSize: '0.6em'}}>0.25</sup></span>
              <span className="formula-op">×</span>
              <span
                className="formula-var var-gdp"
                onMouseEnter={() => setActiveTooltip('gdp')}
                onMouseLeave={() => setActiveTooltip(null)}
              >GDP</span>
              <span className="bracket">]</span>
            </div>
          </div>
        </div>

        {/* Dynamic Tooltip Display Area */}
        <div className="tooltip-viewer mb-4">
          {activeTooltip ? (
            <div className="tooltip-content active">
              <h4>{tooltips[activeTooltip].title}</h4>
              <p>{tooltips[activeTooltip].desc}</p>
              <div className="source-tag">{tooltips[activeTooltip].source}</div>
            </div>
          ) : (
            <div className="tooltip-content empty">
              Hover over a variable in the 2026 Weighted Formula to see weights and sources.
            </div>
          )}
        </div>

        {/* Methodological Section */}
        <div className="theory-section mt-4" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
          <div style={{ borderLeft: '3px solid var(--gold)', paddingLeft: '16px', background: 'rgba(184, 146, 47, 0.05)', padding: '16px', borderRadius: '0 var(--radius) var(--radius) 0' }}>
            <h4 style={{ color: 'var(--gold)' }}>Dual Paradigms: Capacity vs Intensity</h4>
            <p className="text-muted" style={{ fontSize: '0.85rem' }}>
              The CACI serves two econometric purposes. <strong>Absolute Power mode</strong> models global hegemony and total hard leverage (USA dominance). <strong>Economic Intensity mode</strong> normalizes by GDP to capture ecosystem concentration and efficiency (e.g. France's high compute-to-GDP ratio).
            </p>
          </div>

          <div style={{ borderLeft: '3px solid var(--accent)', paddingLeft: '16px', background: 'rgba(61, 107, 153, 0.05)', padding: '16px', borderRadius: '0 var(--radius) var(--radius) 0' }}>
            <h4 style={{ color: 'var(--accent)' }}>Geopolitical Tiering (Factor R)</h4>
            <p className="text-muted" style={{ fontSize: '0.85rem' }}>
              Introduced to reflect <strong>Trump 2.0 Export Controls</strong>. Tier 1 (Allies) benefit from R=1.0, while Tier 3 (Chokepoint) faces structural handicaps (R=0.1).
            </p>
          </div>
        </div>

        {/* Documentation Links Section */}
        <div className="theory-section mt-4" style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <h3 className="section-title" style={{ fontSize: '1.2rem' }}>Methodological Sources</h3>
          <p className="text-muted">This implementation aligns the dashboard with the research findings of the following publications:</p>

          <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', marginTop: '8px' }}>
            <a href="https://mo0ogly.github.io/America-First-IA/pdf/Working_Paper_CACI_AI_Competitiveness.pdf" target="_blank" rel="noreferrer" className="btn btn-primary" style={{ textDecoration: 'none' }}>
              Working Paper: CACI (Sorbonne 2026)
            </a>
            <a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024" target="_blank" rel="noreferrer" className="btn btn-ghost" style={{ textDecoration: 'none', border: '1px solid var(--border)' }}>
              McKinsey AIPI Reference
            </a>
            <a href="https://www.weforum.org/reports/global-ai-readiness-index-2025" target="_blank" rel="noreferrer" className="btn btn-ghost" style={{ textDecoration: 'none', border: '1px solid var(--border)' }}>
              WEF 2025 Benchmarks
            </a>
          </div>
        </div>


      </div>
    </div>
  );
};

export default CaciFormula;
