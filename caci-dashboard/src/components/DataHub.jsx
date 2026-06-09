import React, { useState, useEffect, useMemo } from 'react';
import Papa from 'papaparse';
import { fetchWorkforceLive, fetchEnergyLive, downloadCSV } from '../lib/liveSources';
import './DataHub.css';

const DataHub = ({ sovereignMode = false, setSovereignMode }) => {
  const [activeAccordion, setActiveAccordion] = useState(null);

  // Raw data states
  const [headers, setHeaders] = useState([]);
  const [rawData, setRawData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Other datasets
  const [gdpData, setGdpData] = useState([]);
  const [energyData, setEnergyData] = useState([]);
  const [workforceData, setWorkforceData] = useState([]);

  // Filters
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCountry, setFilterCountry] = useState('All');
  const [filterStatus, setFilterStatus] = useState('All');

  // Modes
  const [viewMode, setViewMode] = useState('raw');

  // Live refresh (fetch direct from source APIs, CSV as fallback)
  const [eiaKey, setEiaKey] = useState('');
  const [liveLoading, setLiveLoading] = useState(null); // 'E' | 'L' | null
  const [liveAudit, setLiveAudit] = useState({}); // { E: {...}, L: {...} }
  const [liveError, setLiveError] = useState(null);

  const handleRefreshWorkforceLive = async () => {
    setLiveLoading('L');
    setLiveError(null);
    try {
      const { rows, audit, error } = await fetchWorkforceLive();
      setWorkforceData(rows);
      setLiveAudit(prev => ({ ...prev, L: audit }));
      if (error) setLiveError(error);
    } catch (err) {
      setLiveError(err.message);
    } finally {
      setLiveLoading(null);
    }
  };

  const handleRefreshEnergyLive = async () => {
    setLiveLoading('E');
    setLiveError(null);
    try {
      const { rows, audit } = await fetchEnergyLive(eiaKey.trim() || undefined);
      setEnergyData(rows);
      setLiveAudit(prev => ({ ...prev, E: audit }));
    } catch (err) {
      setLiveError(err.message);
    } finally {
      setLiveLoading(null);
    }
  };

  // Fetch the data we just downloaded into the public folder
  const handleGrabData = () => {
    setLoading(true);
    setError(null);
    Papa.parse(`${import.meta.env.BASE_URL}data/gpu_clusters.csv`, {
      download: true,
      header: true,
      skipEmptyLines: true,
      complete: (results) => {
        if (results.data && results.data.length > 0) {
          setHeaders(Object.keys(results.data[0]));
          setRawData(results.data);
          setViewMode('raw');
        } else {
          setError("Dataset is empty or malformed");
        }
        setLoading(false);
      },
      error: (err) => {
        setError(err.message);
        setLoading(false);
      }
    });
  };

  const handleSimpleCSVGrab = (filename, setter) => {
    setLoading(true);
    setError(null);
    Papa.parse(`${import.meta.env.BASE_URL}data/${filename}`, {
      download: true,
      header: true,
      skipEmptyLines: true,
      complete: (results) => {
        if (results.data && results.data.length > 0) {
          setter(results.data);
        }
        setLoading(false);
      },
      error: (err) => {
        setError(err.message);
        setLoading(false);
      }
    });
  };

  // ═══════════════ SEARCH & FILTER (CHERCHER) ═══════════════
  const uniqueCountries = useMemo(() => {
    const c = new Set(rawData.map(r => r.Country).filter(Boolean));
    return ['All', ...Array.from(c).sort()];
  }, [rawData]);

  const uniqueStatuses = useMemo(() => {
    const s = new Set(rawData.map(r => r.Status).filter(Boolean));
    return ['All', ...Array.from(s).sort()];
  }, [rawData]);

  const filteredRawData = useMemo(() => {
    return rawData.filter(row => {
      const matchesSearch = !searchTerm ||
        Object.values(row).some(v => String(v).toLowerCase().includes(searchTerm.toLowerCase()));
      const matchesCountry = filterCountry === 'All' || row.Country === filterCountry;
      const matchesStatus = filterStatus === 'All' || row.Status === filterStatus;
      return matchesSearch && matchesCountry && matchesStatus;
    });
  }, [rawData, searchTerm, filterCountry, filterStatus]);

  // ═══════════════ PROCESSED VIEW ═══════════════
  const processedData = useMemo(() => {
    if (viewMode !== 'processed' || rawData.length === 0) return [];
    const aggregated = {};
    rawData.forEach(row => {
      const country = row.Country || 'Unknown';
      const status = row.Status ? row.Status.trim().toLowerCase() : '';
      const owner = row.Owner ? row.Owner.trim() : '';

      // Only count operational compute
      if (status.includes('planned') || status.includes('cancelled')) return;

      // --- INTERNAL SOVEREIGN FILTER (Matches hook logic) ---
      if (sovereignMode) {
        const isUsOwner = owner.toLowerCase().includes('microsoft') || 
                         owner.toLowerCase().includes('amazon') || 
                         owner.toLowerCase().includes('google') ||
                         owner.toLowerCase().includes('azure') ||
                         owner.toLowerCase().includes('oracle');
        if (isUsOwner && country !== 'United States of America' && country !== 'USA') return;
      }

      const flopsLog = parseFloat(row['16-bit OP/s (log)']);
      if (isNaN(flopsLog) || row.Certainty === 'Unlikely') return;
      const flops = Math.pow(10, flopsLog);
      if (!aggregated[country]) {
        aggregated[country] = { Country: country, Total_16bit_Flops: 0, Cluster_Count: 0, Primary_Status: {} };
      }
      aggregated[country].Total_16bit_Flops += flops;
      aggregated[country].Cluster_Count += 1;
      const s = row.Status || 'Unknown';
      aggregated[country].Primary_Status[s] = (aggregated[country].Primary_Status[s] || 0) + 1;
    });
    return Object.values(aggregated)
      .sort((a, b) => b.Total_16bit_Flops - a.Total_16bit_Flops)
      .map(entry => ({
        Country: entry.Country,
        Total_Clusters: entry.Cluster_Count,
        Estimated_PetaFLOPs: (entry.Total_16bit_Flops / 1e15).toLocaleString(undefined, { maximumFractionDigits: 0 }),
        Log_Flops: Math.log10(entry.Total_16bit_Flops).toFixed(2),
        Breakdown: Object.entries(entry.Primary_Status).map(([k, v]) => `${v} ${k}`).join(', ')
      }));
  }, [rawData, viewMode, sovereignMode]);

  const toggleAccordion = (section) => {
    setActiveAccordion(activeAccordion === section ? null : section);
  };

  return (
    <div className="data-hub">

      {/* ═══════════════ METHODOLOGY ACCORDIONS ═══════════════ */}
      <div className="glass-card mb-4">
        <h2 className="section-title">Data Provenance & Integration Hub</h2>
        <p className="text-muted" style={{ marginBottom: '30px', lineHeight: '1.7' }}>
          Expand the sections below to investigate the rigorous open-data sourcing methodologies underpinning the four crucial CACI parameters.
        </p>

        <div className="accordion-group">

          {/* ─────────── FACTOR F ACCORDION ─────────── */}
          <div className={`accordion-item ${activeAccordion === 'F' ? 'active' : ''}`}>
            <div className="accordion-header" onClick={() => toggleAccordion('F')}>
              <div className="accordion-title">
                <span className="factor-badge">F</span> Compute Capacity (Epoch AI)
              </div>
              <span className="accordion-icon">{activeAccordion === 'F' ? '−' : '+'}</span>
            </div>
            {activeAccordion === 'F' && (
              <div className="accordion-body fade-up">
                <p><strong>Source:</strong> Epoch AI GPU Clusters Database</p>
                <p><strong>Definition:</strong> Aggregate compute power by nation (PetaFLOP/s). Data is dynamically extracted and aggregated in this dashboard.</p>

                {/* --- NEW SOVEREIGN MODE TOGGLE --- */}
                <div className="sovereign-toggle-container glass-card" style={{ padding: '15px', border: '1px solid var(--gold)', background: 'rgba(184, 146, 47, 0.05)', marginBottom: '20px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <div>
                      <h6 style={{ color: 'var(--gold)', margin: 0 }}>🛡️ 2028 Sovereign Scenario (Blockade Simulation)</h6>
                      <p style={{ fontSize: '0.8rem', margin: '5px 0 0', color: 'var(--text-muted)' }}>
                        Removes foreign-controlled clusters (e.g., AWS in France, Microsoft in UAE).
                      </p>
                    </div>
                    <label className="switch">
                      <input 
                        type="checkbox" 
                        checked={sovereignMode} 
                        onChange={(e) => setSovereignMode(e.target.checked)} 
                      />
                      <span className="slider round"></span>
                    </label>
                  </div>
                </div>

                <div className="pipeline-container">
                  <h6>① Factor F Data Ingestion Pipeline</h6>
                  <div className="actions">
                    <button className="btn btn-primary" onClick={handleGrabData} disabled={loading}>
                      {loading ? '↻ Grabbing Data...' : '① Import Raw Data'}
                    </button>
                    <button
                      className="btn btn-gold"
                      onClick={() => setViewMode(viewMode === 'raw' ? 'processed' : 'raw')}
                      disabled={rawData.length === 0}
                    >
                      {viewMode === 'raw' ? '③ Process & Consolidate' : '← Back to Raw View'}
                    </button>
                  </div>
                </div>

                {error && <div className="error-alert" style={{ marginTop: '20px' }}><strong>Error:</strong> {error}</div>}

                {/* FACTOR F FILTERS */}
                {viewMode === 'raw' && rawData.length > 0 && (
                  <div className="filters-bar" style={{ marginTop: '24px' }}>
                    <h6 style={{ width: '100%', marginBottom: '10px', color: 'var(--navy)' }}>② Search & Filter</h6>
                    <div className="search-box">
                      <span>🔍</span>
                      <input
                        type="text"
                        placeholder="Search by cluster name, owner..."
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                      />
                    </div>
                    <select value={filterCountry} onChange={(e) => setFilterCountry(e.target.value)}>
                      {uniqueCountries.map(c => <option key={c} value={c}>{c}</option>)}
                    </select>
                    <select value={filterStatus} onChange={(e) => setFilterStatus(e.target.value)}>
                      {uniqueStatuses.map(s => <option key={s} value={s}>{s}</option>)}
                    </select>
                    <span className="results-count">{filteredRawData.length} records</span>
                  </div>
                )}

                {/* FACTOR F: RAW TABLE */}
                {rawData.length > 0 && viewMode === 'raw' && (
                  <div className="table-responsive" style={{ marginTop: '20px' }}>
                    <table className="data-table">
                      <thead>
                        <tr>
                          <th>Country</th>
                          <th>Cluster Name</th>
                          <th>Status</th>
                          <th>H100 Equivalents</th>
                          <th>Max OP/s (log)</th>
                          <th>Certainty</th>
                        </tr>
                      </thead>
                      <tbody>
                        {filteredRawData.slice(0, 50).map((row, i) => (
                          <tr key={i}>
                            <td><strong>{row.Country}</strong></td>
                            <td style={{ maxWidth: '300px', whiteSpace: 'normal' }}>{row.Name}</td>
                            <td>
                              <span className={`status-badge ${(row.Status || '').toLowerCase().includes('existing') ? 'existing' : 'planned'}`}>
                                {row.Status}
                              </span>
                            </td>
                            <td style={{ fontFamily: 'var(--mono, monospace)' }}>{row['H100 equivalents'] ? parseFloat(row['H100 equivalents']).toLocaleString() : '–'}</td>
                            <td style={{ fontFamily: 'var(--mono, monospace)' }}>{row['Max OP/s (log)'] || '–'}</td>
                            <td>{row.Certainty || '–'}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                    {filteredRawData.length > 50 && (
                      <p className="text-muted" style={{ padding: '12px 16px', fontSize: '0.85rem', margin: 0 }}>Showing first 50 of {filteredRawData.length} rows…</p>
                    )}
                  </div>
                )}

                {/* FACTOR F: PROCESSED TABLE */}
                {viewMode === 'processed' && processedData.length > 0 && (
                  <div style={{ marginTop: '24px' }}>
                    <div className="analysis-note" style={{ marginBottom: '20px' }}>
                      <h5>Factor F (Compute Capacity) — Synthesized</h5>
                      <p>
                        The econometric processing engine has parsed the raw cluster data. Log FLOPs have been exponentiated,
                        normalized by nation, and converted into PetaFLOP/s. Highly uncertain clusters have been filtered out.
                      </p>
                    </div>
                    <div className="table-responsive">
                      <table className="data-table">
                        <thead>
                          <tr>
                            <th>#</th>
                            <th>Nation</th>
                            <th>Sub-Clusters</th>
                            <th style={{ color: 'var(--gold)' }}>Factor F (Est. PetaFLOP/s)</th>
                            <th>Cluster Breakdown</th>
                          </tr>
                        </thead>
                        <tbody>
                          {processedData.map((row, i) => (
                            <tr key={i} style={i < 3 ? { backgroundColor: 'rgba(184, 146, 47, 0.05)' } : {}}>
                              <td style={{ fontWeight: i < 3 ? 'bold' : 'normal', color: i < 3 ? 'var(--gold)' : 'inherit' }}>{i + 1}</td>
                              <td><strong>{row.Country}</strong></td>
                              <td>{row.Total_Clusters}</td>
                              <td style={{ fontWeight: '700', color: 'var(--gold)', fontFamily: 'var(--mono, monospace)', fontSize: '1rem' }}>{row.Estimated_PetaFLOPs}</td>
                              <td style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>{row.Breakdown}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>

          {/* ─────────── GDP ACCORDION ─────────── */}
          <div className={`accordion-item ${activeAccordion === 'GDP' ? 'active' : ''}`}>
            <div className="accordion-header" onClick={() => toggleAccordion('GDP')}>
              <div className="accordion-title">
                <span className="factor-badge">GDP</span> Economic Mass (IMF WEO)
              </div>
              <span className="accordion-icon">{activeAccordion === 'GDP' ? '−' : '+'}</span>
            </div>
            {activeAccordion === 'GDP' && (
              <div className="accordion-body fade-up">
                <p><strong>Source:</strong> IMF World Economic Outlook (Indicator <code>NGDPD</code>)</p>
                <p><strong>Definition:</strong> Nominal GDP in Current USD. AI infrastructure and silicon are priced dynamically in standard global dollar markets, so PPP adjustments would be misleading. The dashboard targets the 2024 tranche.</p>

                <div className="pipeline-container">
                  <h6>Economic Mass Data Pipeline</h6>
                  <div className="actions">
                    <span className="status-badge existing">🟢 Dynamic Pipeline</span>
                    <button className="btn btn-primary" onClick={() => handleSimpleCSVGrab('gdp_data.csv', setGdpData)} disabled={loading}>
                      {loading ? '↻ Importing...' : 'Import IMF Dataset'}
                    </button>
                  </div>
                </div>

                {gdpData.length > 0 && (
                  <div className="table-responsive" style={{ marginTop: '20px' }}>
                    <table className="data-table">
                      <thead>
                        <tr><th>Country</th><th>GDP (Trillions USD)</th></tr>
                      </thead>
                      <tbody>
                        {gdpData.map((r, i) => (
                          <tr key={i}>
                            <td><strong>{r.Country}</strong></td>
                            <td style={{ fontFamily: 'var(--mono, monospace)', color: 'var(--navy)' }}>{r.GDP_Trillions_USD}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </div>
            )}
          </div>

          {/* ─────────── FACTOR E ACCORDION ─────────── */}
          <div className={`accordion-item ${activeAccordion === 'E' ? 'active' : ''}`}>
            <div className="accordion-header" onClick={() => toggleAccordion('E')}>
              <div className="accordion-title">
                <span className="factor-badge">E</span> Energy Cost (IEA)
              </div>
              <span className="accordion-icon">{activeAccordion === 'E' ? '−' : '+'}</span>
            </div>
            {activeAccordion === 'E' && (
              <div className="accordion-body fade-up">
                <p><strong>Source:</strong> International Energy Agency (IEA) & Public Reports</p>
                <p><strong>Definition:</strong> Industrial End-use Electricity prices (USD/MWh). Accurate modeling demands industrial rates tied to long-term PPAs, not volatile day-ahead wholesale or residential pricing.</p>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', fontStyle: 'italic' }}>
                  *Note: Since the full global IEA database is paywalled, this metric utilizes an explicit local auditable CSV proxy mapped in the dashboard repository.
                </p>

                <div className="pipeline-container">
                  <h6>Energy Cost Data Pipeline</h6>
                  <div className="actions">
                    <span className="status-badge planned">Hybrid (Eurostat live + proxy)</span>
                    <button className="btn btn-primary" onClick={() => handleSimpleCSVGrab('energy_prices.csv', setEnergyData)} disabled={loading}>
                      {loading ? 'Importing...' : 'Import CSV (committed)'}
                    </button>
                    <button className="btn btn-gold" onClick={handleRefreshEnergyLive} disabled={liveLoading === 'E'}>
                      {liveLoading === 'E' ? 'Refreshing live...' : 'Refresh Live (Eurostat / EIA)'}
                    </button>
                    <button className="btn btn-primary" onClick={() => downloadCSV('energy_prices.csv', energyData, ['Country', 'Industrial_Electricity_USD_per_MWh'])} disabled={energyData.length === 0}>
                      Download CSV
                    </button>
                  </div>
                  <div style={{ marginTop: '12px' }}>
                    <input
                      type="password"
                      placeholder="Optional EIA API key (for live US price)"
                      value={eiaKey}
                      onChange={(e) => setEiaKey(e.target.value)}
                      style={{ width: '100%', maxWidth: '420px', padding: '8px 10px', border: '1px solid var(--navy)', borderRadius: '6px' }}
                    />
                    <p className="text-muted" style={{ fontSize: '0.78rem', margin: '6px 0 0' }}>
                      Eurostat sources FR/DE/EU live. Without an EIA key, USA and other non-EU markets keep the committed CSV value (fallback). Key stays in your browser, never committed. After refresh, click Download CSV and commit it to persist.
                    </p>
                  </div>
                  {liveError && liveLoading !== 'E' && (
                    <div className="error-alert" style={{ marginTop: '12px' }}><strong>Live:</strong> {liveError}</div>
                  )}
                  {liveAudit.E && (
                    <div className="text-muted" style={{ marginTop: '12px', fontSize: '0.78rem', fontFamily: 'var(--mono, monospace)' }}>
                      {Object.entries(liveAudit.E).filter(([k]) => !k.startsWith('_')).map(([k, v]) => (
                        <div key={k}>{k}: {v}</div>
                      ))}
                    </div>
                  )}
                </div>

                {energyData.length > 0 && (
                  <div className="table-responsive" style={{ marginTop: '20px' }}>
                    <table className="data-table">
                      <thead>
                        <tr><th>Country</th><th>Industrial Electricity (USD/MWh)</th></tr>
                      </thead>
                      <tbody>
                        {energyData.map((r, i) => (
                          <tr key={i}>
                            <td><strong>{r.Country}</strong></td>
                            <td style={{ fontFamily: 'var(--mono, monospace)', color: 'var(--navy)' }}>{r.Industrial_Electricity_USD_per_MWh}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </div>
            )}
          </div>

          {/* ─────────── FACTOR L ACCORDION ─────────── */}
          <div className={`accordion-item ${activeAccordion === 'L' ? 'active' : ''}`}>
            <div className="accordion-header" onClick={() => toggleAccordion('L')}>
              <div className="accordion-title">
                <span className="factor-badge">L</span> STEM Workforce (World Bank)
              </div>
              <span className="accordion-icon">{activeAccordion === 'L' ? '−' : '+'}</span>
            </div>
            {activeAccordion === 'L' && (
              <div className="accordion-body fade-up">
                <p><strong>Source:</strong> World Bank WDI (Proxy derived from indicator <code>SP.POP.SCIE.RD.P6</code>)</p>
                <p><strong>Definition:</strong> Active volume of researchers/STEM professionals. Using total labor forces improperly skews variables for hyper-populations like India/China without representing high-tech absorptive capabilities.</p>

                <div className="pipeline-container">
                  <h6>STEM Workforce Data Pipeline</h6>
                  <div className="actions">
                    <span className="status-badge existing">World Bank live</span>
                    <button className="btn btn-primary" onClick={() => handleSimpleCSVGrab('workforce_data.csv', setWorkforceData)} disabled={loading}>
                      {loading ? 'Importing...' : 'Import CSV (committed)'}
                    </button>
                    <button className="btn btn-gold" onClick={handleRefreshWorkforceLive} disabled={liveLoading === 'L'}>
                      {liveLoading === 'L' ? 'Refreshing live...' : 'Refresh Live (World Bank)'}
                    </button>
                    <button className="btn btn-primary" onClick={() => downloadCSV('workforce_data.csv', workforceData, ['Country', 'Workforce_Millions'])} disabled={workforceData.length === 0}>
                      Download CSV
                    </button>
                  </div>
                  <p className="text-muted" style={{ fontSize: '0.78rem', margin: '10px 0 0' }}>
                    Live pull: SP.POP.SCIE.RD.P6 x SP.POP.TOTL, regions summed from member countries. If the World Bank API is unavailable, the committed CSV is used as fallback. After refresh, click Download CSV and commit it to persist.
                  </p>
                  {liveError && liveLoading !== 'L' && (
                    <div className="error-alert" style={{ marginTop: '12px' }}><strong>Live:</strong> {liveError}</div>
                  )}
                  {liveAudit.L && (
                    <div className="text-muted" style={{ marginTop: '12px', fontSize: '0.78rem', fontFamily: 'var(--mono, monospace)' }}>
                      {Object.entries(liveAudit.L).map(([k, v]) => (
                        <div key={k}>{k}: {v}</div>
                      ))}
                    </div>
                  )}
                </div>

                {workforceData.length > 0 && (
                  <div className="table-responsive" style={{ marginTop: '20px' }}>
                    <table className="data-table">
                      <thead>
                        <tr><th>Country</th><th>Workforce (Millions)</th></tr>
                      </thead>
                      <tbody>
                        {workforceData.map((r, i) => (
                          <tr key={i}>
                            <td><strong>{r.Country}</strong></td>
                            <td style={{ fontFamily: 'var(--mono, monospace)', color: 'var(--navy)' }}>{r.Workforce_Millions}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </div>
            )}
          </div>

        </div>
      </div>
    </div>
  );
};

export default DataHub;
