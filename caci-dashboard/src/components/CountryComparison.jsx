import React, { useState, useMemo } from 'react';
import {
    BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip as RechartsTooltip,
    Legend, ResponsiveContainer, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar,
    LineChart, Line
} from 'recharts';
import './CountryComparison.css';

import { useDataConsolidation } from '../hooks/useDataConsolidation';

// Default keys to initialize the UI state before data loads
const DEFAULT_COUNTRIES = ['USA', 'China', 'EU', 'India', 'UAE', 'Asia (Ex-China)', 'UK', 'France', 'Germany'];

const INDICES = {
    caci: { name: 'CACI Score (Relative to Leader)', color: 'var(--gold)' },
    imf: { name: 'IMF AIPI', color: 'var(--accent-light)' },
    tortoise: { name: 'Tortoise AI Index', color: 'var(--text-muted)' }
};

// ═══════════════ SOVEREIGNTY VISUAL COMPONENTS ═══════════════

const SovereigntyTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
        const data = payload[0].payload;
        const total = data.f_total || 0;
        const sov = data.f || 0;
        const percent = total > 0 ? ((sov / total) * 100).toFixed(1) : "0.0";

        return (
            <div className="custom-tooltip glass-card" style={{ padding: '15px', border: '1px solid var(--gold)' }}>
                <h4 style={{ color: 'var(--gold)', marginBottom: '10px' }}>{data.name}</h4>
                <p><strong>Physical (F_phys):</strong> {Math.round(total).toLocaleString()} PF</p>
                <p><strong>Sovereign (F_sov):</strong> {Math.round(sov).toLocaleString()} PF</p>
                <p style={{ color: sov >= total ? 'var(--gold)' : 'var(--red)', fontWeight: 'bold' }}>
                    Sovereignty Ratio: {percent}%
                </p>
                <p className="text-muted" style={{ fontSize: '0.8rem', marginTop: '10px' }}>
                    {sov >= total
                        ? "No foreign-controlled clusters detected."
                        : `⚠️ ${ Math.round(total - sov).toLocaleString() } PF controlled by external jurisdictions.`}
                </p>
            </div>
        );
    }
    return null;
};

const SovereignCake = ({ sovereign, total, ratio }) => {
    const layers = [
        { id: 5, name: 'L5: Chips (Silicon)', status: 'Globalized', color: '#1a2744' },
        { id: 4, name: 'L4: Networking', status: 'Globalized', color: '#1a2744' },
        { id: 3, name: 'L3: Compute (Infrastructure)', status: ratio < 1 ? 'Vulnerable' : 'Sovereign', color: ratio < 1 ? 'var(--red)' : 'var(--gold)' },
        { id: 2, name: 'L2: Software Stack', status: ratio < 0.5 ? 'Dependent' : 'Balanced', color: ratio < 1 ? 'var(--red)' : 'var(--accent)' },
        { id: 1, name: 'L1: AI Services', status: ratio < 0.5 ? 'Dependent' : 'Sovereign', color: ratio < 1 ? 'var(--red)' : 'var(--gold)' },
    ];

    return (
        <div className="cake-visual">
            {layers.map(layer => (
                <div
                    key={layer.id}
                    className={`cake-layer layer-${layer.id}`}
                    style={{
                        backgroundColor: layer.color,
                        opacity: layer.id === 3 ? 1 : 0.8,
                        border: layer.id === 3 && ratio < 1 ? '2px solid var(--red)' : 'none'
                    }}
                >
                    <span className="layer-label">{layer.name}</span>
                    <span className="layer-status">
                        {layer.id === 3 && ratio < 1 ? `${Math.round(ratio*100)}% Sov.` : layer.status}
                    </span>
                </div>
            ))}
            <div className="cake-base">Sovereignty Audit</div>
        </div>
    );
};

const CountryComparison = ({ sovereignMode = false }) => {
    const { consolidatedData, loading, error } = useDataConsolidation(sovereignMode);
    const [viewMode, setViewMode] = useState('bar');
    const [simData, setSimData] = useState(null);

    // Sync the simulator state once the data loads or scenario changes
    React.useEffect(() => {
        if (consolidatedData) {
            // Deep copy to allow editing. We reset simData when scenario (sovereignMode) changes
            setSimData(JSON.parse(JSON.stringify(consolidatedData)));
        }
    }, [consolidatedData]);

    // Filtering States
    const [selectedCountries, setSelectedCountries] = useState(
        DEFAULT_COUNTRIES.reduce((acc, c) => ({ ...acc, [c]: ['USA', 'China', 'EU', 'India', 'Asia (Ex-China)'].includes(c) }), {})
    );
    const [selectedIndices, setSelectedIndices] = useState({
        caci: true,
        imf: true,
        tortoise: true
    });

    const handleInputChange = (country, field, value) => {
        setSimData(prev => ({
            ...prev,
            [country]: {
                ...prev[country],
                [field]: parseFloat(value) || 0
            }
        }));
    };

    const toggleCountry = (c) => {
        setSelectedCountries(prev => ({ ...prev, [c]: !prev[c] }));
    };

    const toggleIndex = (idx) => {
        setSelectedIndices(prev => ({ ...prev, [idx]: !prev[idx] }));
    };

    // ═══════════════ CACI CALCULATION ENGINE ═══════════════
    // IMPORTANT: These hooks MUST be above ANY early returns to satisfy Rules of Hooks
    const calculatedData = useMemo(() => {
        if (!simData) return [];
        const activeCountries = Object.keys(simData).filter(c => selectedCountries[c]);

        return activeCountries.map(country => {
            const data = simData[country] || { f: 0, f_total: 0, e: 1, gdp: 1, l: 1 };

            // Protect against divide by zero
            const eSafe = data.e > 0 ? data.e : 1;
            const gdpSafe = data.gdp > 0 ? data.gdp : 1;
            const lSafe = data.l > 0 ? data.l : 1;

            // Calculate TWO scores: One with total F (phys) and one with sovereign F (sov)
            const f_phys = data.f_total || data.f || 0;
            const f_sov = data.f || 0;

            const rawCaci_phys = f_phys >= 15 ? (f_phys * (1 / eSafe)) / (gdpSafe * lSafe) : 0;
            const rawCaci_sov = f_sov >= 15 ? (f_sov * (1 / eSafe)) / (gdpSafe * lSafe) : 0;

            return {
                name: country,
                rawCaci_phys,
                rawCaci_sov,
                imf: data.imf,
                tortoise: data.tortoise,
            };
        });
    }, [simData, selectedCountries]);

    // Secondary pass to normalize CACI scores so USA (or leader) = 100
    const finalChartData = useMemo(() => {
        if (calculatedData.length === 0 || !simData) return [];
        // Normalize both scores relative to the same leader (usually USA phys)
        const maxRaw = Math.max(...calculatedData.map(d => d.rawCaci_phys));

        return calculatedData.map(d => {
            const sData = simData[d.name] || { f: 0, f_total: 0 };
            return {
                ...d,
                caci_phys: maxRaw > 0 ? parseFloat(((d.rawCaci_phys / maxRaw) * 100).toFixed(1)) : 0,
                caci_sov: maxRaw > 0 ? parseFloat(((d.rawCaci_sov / maxRaw) * 100).toFixed(1)) : 0,
                caci: maxRaw > 0 ? parseFloat((( (sovereignMode ? d.rawCaci_sov : d.rawCaci_phys) / maxRaw) * 100).toFixed(1)) : 0,
                f: sData.f || 0,
                f_total: sData.f_total || 0,
                f_foreign: (sData.f_total || 0) - (sData.f || 0)
            };
        });
    }, [calculatedData, simData, sovereignMode]);

    // ═══════════════ LOADING / ERROR GUARDS ═══════════════
    if (loading) return (
        <div style={{ padding: '40px', textAlign: 'center', minHeight: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <div style={{ color: 'var(--gold)', fontSize: '1.2rem', fontWeight: 600 }}>
                ↻ Dynamically parsing and consolidating data (Epoch AI, IMF WEO, IEA, World Bank)...
            </div>
        </div>
    );
    if (error) return <div style={{ color: 'red', padding: '20px' }}>Data Consolidation Error: {error}</div>;
    if (!simData) return null;

    return (
        <div className="comparison-container">
            <div className="glass-card mb-4" style={{ minHeight: '500px' }}>
                <div className="header-flex">
                    <div>
                        <h2 className="section-title">Comparative Analysis & Simulator</h2>
                        <p className="text-muted">
                            Live econometric calculation of the CACI using the geometric formula:
                            <br /><strong>CACI = [ F × E⁻¹ ] / [ GDP × L ]</strong>. Adjust the foundational parameters below.
                        </p>
                    </div>
                    <div className="toggle-group" style={{ flexWrap: 'wrap' }}>
                        <button
                            className={`btn ${viewMode === 'bar' ? 'btn-primary' : 'btn-ghost'}`}
                            onClick={() => setViewMode('bar')}
                        >
                            Bar View
                        </button>
                        <button
                            className={`btn ${viewMode === 'sovereignty' ? 'btn-gold' : 'btn-ghost'}`}
                            onClick={() => setViewMode('sovereignty')}
                        >
                            Sovereignty Audit
                        </button>
                        <button
                            className={`btn ${viewMode === 'impact' ? 'btn-gold' : 'btn-ghost'}`}
                            onClick={() => setViewMode('impact')}
                        >
                            Sovereign Impact
                        </button>
                        <button
                            className={`btn ${viewMode === 'radar' ? 'btn-primary' : 'btn-ghost'}`}
                            onClick={() => setViewMode('radar')}
                        >
                            Radar View
                        </button>
                        <button
                            className={`btn ${viewMode === 'line' ? 'btn-primary' : 'btn-ghost'}`}
                            onClick={() => setViewMode('line')}
                        >
                            Line View
                        </button>
                    </div>
                </div>

                {/* ═══════════════ FILTER PANEL ═══════════════ */}
                <div className="filter-panel">
                    <div className="filter-group" style={{ flex: 2 }}>
                        <h5>Filter Entities</h5>
                        <div className="checkbox-row">
                            {Object.keys(simData).map(c => (
                                <label key={c} className="checkbox-label">
                                    <input
                                        type="checkbox"
                                        checked={selectedCountries[c]}
                                        onChange={() => toggleCountry(c)}
                                    />
                                    {c}
                                </label>
                            ))}
                        </div>
                    </div>
                    <div className="filter-group" style={{ flex: 1 }}>
                        <h5>Filter Indices</h5>
                        <div className="checkbox-row">
                            {Object.entries(INDICES).map(([key, config]) => (
                                <label key={key} className="checkbox-label" style={{ color: config.color === 'var(--text-muted)' ? '#666' : config.color, fontWeight: 600 }}>
                                    <input
                                        type="checkbox"
                                        checked={selectedIndices[key]}
                                        onChange={() => toggleIndex(key)}
                                    />
                                    {config.name.split(' ')[0]} {/* Short name for UI */}
                                </label>
                            ))}
                        </div>
                    </div>
                </div>

                <hr className="section-bar" />

                {/* ═══════════════ VISUALIZATION ═══════════════ */}
                <div className="chart-wrapper" style={{ height: '400px', marginTop: '30px' }}>
                    <ResponsiveContainer width="100%" height="100%">
                        {viewMode === 'bar' ? (
                            <BarChart data={finalChartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="rgba(26,39,68,0.1)" vertical={false} />
                                <XAxis dataKey="name" stroke="var(--text-muted)" tick={{ fontFamily: 'Inter', fontSize: 13 }} />
                                <YAxis stroke="var(--text-muted)" tick={{ fontFamily: 'Inter', fontSize: 13 }} />
                                <RechartsTooltip cursor={{ fill: 'rgba(61,107,153,0.05)' }} contentStyle={{ backgroundColor: 'rgba(255,255,255,0.95)', borderRadius: '12px', border: '1px solid var(--border)', boxShadow: 'var(--shadow-md)', fontFamily: 'Inter' }} />
                                <Legend iconType="circle" wrapperStyle={{ paddingTop: '20px', fontFamily: 'Inter', fontSize: '14px' }} />
                                {selectedIndices.caci && <Bar dataKey="caci" name={INDICES.caci.name} fill={INDICES.caci.color} radius={[4, 4, 0, 0]} />}
                                {selectedIndices.imf && <Bar dataKey="imf" name={INDICES.imf.name} fill={INDICES.imf.color} radius={[4, 4, 0, 0]} />}
                                {selectedIndices.tortoise && <Bar dataKey="tortoise" name={INDICES.tortoise.name} fill={INDICES.tortoise.color} radius={[4, 4, 0, 0]} />}
                            </BarChart>
                        ) : viewMode === 'sovereignty' ? (
                            <BarChart data={finalChartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="rgba(26,39,68,0.1)" vertical={false} />
                                <XAxis dataKey="name" stroke="var(--text-muted)" />
                                <YAxis stroke="var(--text-muted)" />
                                <RechartsTooltip content={<SovereigntyTooltip />} />
                                <Legend verticalAlign="top" height={36}/>
                                <Bar dataKey="f" name="Sovereign Compute" stackId="a" fill="var(--gold)" />
                                <Bar dataKey="f_foreign" name="Foreign-Controlled" stackId="a" fill="rgba(200, 50, 50, 0.4)" radius={[4, 4, 0, 0]} />
                            </BarChart>
                        ) : viewMode === 'impact' ? (
                            <BarChart data={finalChartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="rgba(26,39,68,0.1)" vertical={false} />
                                <XAxis dataKey="name" stroke="var(--text-muted)" />
                                <YAxis stroke="var(--text-muted)" />
                                <RechartsTooltip />
                                <Legend verticalAlign="top" height={36}/>
                                <Bar dataKey="caci_phys" name="Potential CACI (Physical)" fill="var(--text-muted)" opacity={0.5} radius={[4, 4, 0, 0]} />
                                <Bar dataKey="caci_sov" name="Sovereign CACI (Actual)" fill="var(--gold)" radius={[4, 4, 0, 0]} />
                            </BarChart>
                        ) : viewMode === 'radar' ? (
                            <RadarChart cx="50%" cy="50%" outerRadius="70%" data={finalChartData}>
                                <PolarGrid stroke="rgba(26,39,68,0.1)" />
                                <PolarAngleAxis dataKey="name" tick={{ fill: 'var(--text-hi)', fontSize: 14, fontWeight: 600 }} />
                                <PolarRadiusAxis angle={30} domain={[0, 100]} />
                                {selectedIndices.caci && <Radar name={INDICES.caci.name} dataKey="caci" stroke={INDICES.caci.color} fill={INDICES.caci.color} fillOpacity={0.5} />}
                                {selectedIndices.imf && <Radar name={INDICES.imf.name} dataKey="imf" stroke={INDICES.imf.color} fill={INDICES.imf.color} fillOpacity={0.3} />}
                                {selectedIndices.tortoise && <Radar name={INDICES.tortoise.name} dataKey="tortoise" stroke={INDICES.tortoise.color} fill={INDICES.tortoise.color} fillOpacity={0.2} />}
                                <Legend wrapperStyle={{ paddingTop: '20px' }} />
                                <RechartsTooltip />
                            </RadarChart>
                        ) : (
                            <LineChart data={finalChartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="rgba(26,39,68,0.1)" vertical={false} />
                                <XAxis dataKey="name" stroke="var(--text-muted)" tick={{ fontFamily: 'Inter', fontSize: 13 }} />
                                <YAxis stroke="var(--text-muted)" tick={{ fontFamily: 'Inter', fontSize: 13 }} />
                                <RechartsTooltip contentStyle={{ backgroundColor: 'rgba(255,255,255,0.95)', borderRadius: '12px', border: '1px solid var(--border)', boxShadow: 'var(--shadow-md)', fontFamily: 'Inter' }} />
                                <Legend iconType="circle" wrapperStyle={{ paddingTop: '20px', fontFamily: 'Inter', fontSize: '14px' }} />
                                {selectedIndices.caci && <Line type="monotone" dataKey="caci" name={INDICES.caci.name} stroke={INDICES.caci.color} strokeWidth={3} dot={{ r: 6 }} />}
                                {selectedIndices.imf && <Line type="monotone" dataKey="imf" name={INDICES.imf.name} stroke={INDICES.imf.color} strokeWidth={2} dot={{ r: 4 }} />}
                                {selectedIndices.tortoise && <Line type="monotone" dataKey="tortoise" name={INDICES.tortoise.name} stroke={INDICES.tortoise.color} strokeWidth={2} dot={{ r: 4 }} />}
                            </LineChart>
                        )}
                    </ResponsiveContainer>
                </div>

                {viewMode === 'sovereignty' && (
                    <div className="sovereignty-audit-grid mt-4">
                        {finalChartData.filter(d => d.f_total > 5).map(d => (
                            <div key={d.name} className="cake-panel glass-card">
                                <h4 style={{textAlign: 'center', marginBottom: '15px'}}>{d.name}</h4>
                                <SovereignCake 
                                    sovereign={d.f} 
                                    total={d.f_total} 
                                    ratio={d.f / (d.f_total || 1)} 
                                />
                            </div>
                        ))}
                    </div>
                )}

                <div className="analysis-note mt-4 mb-4">
                    <h5>⚠️ Reading the CACI: Intensity, Not Total Capacity</h5>
                    <p>
                        The CACI measures <strong>compute intensity relative to economic mass</strong> — not absolute capacity.
                        This is why a single nation (e.g., France at ~21) can score higher than the EU-28 aggregate (~7):
                        France concentrates significant GPU infrastructure (Scaleway, OVH) against a GDP of $3.2T,
                        while the EU-28 aggregate dilutes compute across $18.9T of GDP and 3.1M STEM workforce —
                        including member states with minimal compute but large economies.
                    </p>
                    <p style={{ fontSize: '0.88rem', color: 'var(--text-muted)', marginTop: '8px' }}>
                        This is analogous to GDP per capita: Norway scores higher than the EU average despite having a fraction of total EU GDP.
                        The CACI intentionally captures this <em>intensity effect</em> — the "Small Economy Normalization Bias"
                        documented in the <a href="https://mo0ogly.github.io/America-First-IA/" target="_blank" rel="noopener noreferrer" style={{ color: 'var(--gold)' }}>Econometric Annex</a>.
                    </p>
                </div>

                <hr className="section-bar" />

                {/* ═══════════════ INTERACTIVE VARIABLES ═══════════════ */}
                <h3 className="section-title mt-4" style={{ fontSize: '1.2rem' }}>Parameter Simulation Sandbox</h3>
                <p className="text-muted mb-4">Adjust the raw attributes below to immediately recalculate the geometric CACI for the selected nations.</p>

                <div className="data-grid">
                    {Object.keys(simData).filter(c => selectedCountries[c]).map(country => {
                        const cData = calculatedData.find(d => d.name === country);
                        return (
                            <div key={country} className="data-card">
                                <h4>{country}
                                    <span style={{ fontSize: '0.75rem', fontWeight: 'normal', color: 'var(--text-muted)', display: 'block', marginTop: '4px' }}>
                                        Raw CACI (Phys): {cData?.rawCaci_phys.toFixed(5)} <br/>
                                        Raw CACI (Sov): {cData?.rawCaci_sov.toFixed(5)}
                                    </span>
                                </h4>
                                <div className="input-group">
                                    <label title="PetaFLOP/s">Factor F (Compute)</label>
                                    <input type="number" value={simData[country].f} onChange={e => handleInputChange(country, 'f', e.target.value)} />
                                </div>
                                <div className="input-group">
                                    <label title="€/MWh">Factor E (Energy Cost)</label>
                                    <input type="number" value={simData[country].e} onChange={e => handleInputChange(country, 'e', e.target.value)} />
                                </div>
                                <div className="input-group">
                                    <label title="Trillions $">GDP (Mass)</label>
                                    <input type="number" step="0.1" value={simData[country].gdp} onChange={e => handleInputChange(country, 'gdp', e.target.value)} />
                                </div>
                                <div className="input-group">
                                    <label title="Millions of STEM workers">Factor L (Human Cap)</label>
                                    <input type="number" step="0.1" value={simData[country].l} onChange={e => handleInputChange(country, 'l', e.target.value)} />
                                </div>

                                {/* Threshold Warning and Result */}
                                {cData?.rawCaci_phys > 0 ? (
                                    <div className="caci-result">
                                        <span>Normalized CACI Index:</span>
                                        <span>{finalChartData.find(d => d.name === country)?.caci}</span>
                                    </div>
                                ) : (
                                    <div className="caci-result" style={{ color: 'var(--red)', borderTopColor: 'var(--red)' }}>
                                        <span style={{ fontSize: '0.8rem', display: 'flex', flexDirection: 'column' }}>
                                            <strong>Excluded (Small Economy Bias)</strong>
                                            Requires Critical Mass of F &ge; 15
                                        </span>
                                        <span>N/A</span>
                                    </div>
                                )}
                            </div>
                        );
                    })}
                </div>

            </div>
        </div>
    );
};

export default CountryComparison;
