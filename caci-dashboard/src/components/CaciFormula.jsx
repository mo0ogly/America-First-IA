import React, { useState } from 'react';
import './CaciFormula.css';

const CaciFormula = () => {
  const [activeTooltip, setActiveTooltip] = useState(null);

  const tooltips = {
    caci: {
      title: "CACI Index",
      desc: "Compute-Adjusted Competitiveness Index. A parsimonious yet theoretically grounded indicator capturing the multiplicative interaction between accessible compute, energy cost constraints, and economic absorptive capacity.",
      source: "Eq: CACI(r,t) = [ F(r,t) × E(r,t)⁻¹ ] / [ GDP(r,t) × L(r,t) ]"
    },
    f: {
      title: "Factor F: Installed Compute Capacity",
      desc: "Installed and accessible AI compute capacity in region r at period t, measured in aggregate PetaFLOP/s (16-bit performance). Includes domestic cloud capacities and authorized access quotas to foreign clouds.",
      source: "Data: Epoch AI GPU Clusters / OECD / Hyperscalers"
    },
    e: {
      title: "Factor E: Energy Cost",
      desc: "Average energy cost of compute in region r, in €/MWh for data centers. Adjusts raw compute for its energy constraint: at equal FLOPs, a country with electricity twice as expensive has a CACI twice as low.",
      source: "Data: Eurostat / EIA / IEA"
    },
    gdp: {
      title: "GDP: Economic Mass",
      desc: "Gross domestic product of region r. Normalization ensures comparability across economies of very different sizes: without it, the US and China would mechanically dominate any ranking by sheer economic mass.",
      source: "Data: World Bank / Eurostat"
    },
    l: {
      title: "Factor L: Absorptive Capacity",
      desc: "Working population with AI competencies (proxy: STEM graduates + certified AI training). Captures absorptive capacity: abundant compute without human capital to exploit it does not produce competitiveness.",
      source: "Data: OECD (Education at a Glance) / LinkedIn / Certifications"
    }
  };

  return (
    <div className="formula-container">
      <div className="glass-card mb-4">
        <h2 className="section-title">The Compute-Adjusted Competitiveness Index (CACI)</h2>
        <hr className="section-bar" />
        <p className="text-muted mb-4">
          The CACI proposes a parsimonious yet theoretically grounded indicator that captures the multiplicative interaction between three factors: <strong>accessible compute</strong>, the <strong>energy cost</strong> constraining it, and the <strong>economic and human capacity</strong> to exploit it.
          Hover over the variables below for detailed methodological definitions.
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
              >F<span className="power">(r,t)</span></span>
              <span className="formula-op">×</span>
              <span className="formula-group">
                <span
                  className="formula-var var-e"
                  onMouseEnter={() => setActiveTooltip('e')}
                  onMouseLeave={() => setActiveTooltip(null)}
                >E<span className="power">(r,t)⁻¹</span></span>
              </span>
              <span className="bracket">]</span>
            </div>
            <div className="fraction-line"></div>
            <div className="denominator">
              <span className="bracket">[</span>
              <span
                className="formula-var var-gdp"
                onMouseEnter={() => setActiveTooltip('gdp')}
                onMouseLeave={() => setActiveTooltip(null)}
              >GDP<span className="power">(r,t)</span></span>
              <span className="formula-op">×</span>
              <span
                className="formula-var var-l"
                onMouseEnter={() => setActiveTooltip('l')}
                onMouseLeave={() => setActiveTooltip(null)}
              >L<span className="power">(r,t)</span></span>
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
              Hover over a variable in the formula to see its definition and source.
            </div>
          )}
        </div>

        {/* Methodological Limitations Section */}
        <div className="theory-section mt-4" style={{ borderLeft: '3px solid var(--gold)', paddingLeft: '16px', background: 'var(--bg)', padding: '16px', borderRadius: '0 var(--radius) var(--radius) 0' }}>
          <h4 style={{ color: 'var(--gold)' }}>Methodological Limits: Small Economy Normalization Bias</h4>
          <p className="text-muted" style={{ fontSize: '0.9rem', marginBottom: '8px' }}>
            As highlighted by the <strong>OECD/JRC Handbook on Constructing Composite Indicators (2008)</strong>, geometric indicators normalized by economic mass (GDP × L) are susceptible to the <em>Small Economy Bias</em>.
          </p>
          <p className="text-muted" style={{ fontSize: '0.9rem' }}>
            In the CACI framework, countries with a very small denominator (e.g., South Africa or Iceland) can experience artificially inflated scores if they possess even a fraction of tier-1 compute (F) combined with cheap industrial energy (E). To prevent this mathematical distortion, the real-world application of the CACI requires a <strong>Critical Mass Threshold (Minimum F)</strong>. Economies below this compute threshold are excluded from the primary tier ranking.
          </p>
        </div>

        {/* Documentation Links Section */}
        <div className="theory-section mt-4" style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <h3 className="section-title" style={{ fontSize: '1.2rem' }}>Comprehensive Documentation</h3>
          <p className="text-muted">For a deep dive into the mathematical proofs, econometric justifications, and extended FAQs, please refer to the official <a href="https://mo0ogly.github.io/America-First-IA/" target="_blank" rel="noreferrer">America-First-IA</a> publications:</p>

          <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', marginTop: '8px' }}>
            <a href="https://mo0ogly.github.io/America-First-IA/Chapitre_II_Methodologie" target="_blank" rel="noreferrer" className="btn btn-primary" style={{ textDecoration: 'none' }}>
              Chapitre II: Méthodologie
            </a>
            <a href="https://mo0ogly.github.io/America-First-IA/FAQ_Volume3_Comprendre_le_Ratio_CACI" target="_blank" rel="noreferrer" className="btn btn-primary" style={{ textDecoration: 'none' }}>
              FAQ Vol 3: Comprendre le Ratio CACI
            </a>
            <a href="https://mo0ogly.github.io/America-First-IA/Working_Paper_CACI" target="_blank" rel="noreferrer" className="btn btn-gold" style={{ textDecoration: 'none' }}>
              Working Paper CACI
            </a>
          </div>
        </div>

      </div>
    </div>
  );
};

export default CaciFormula;
