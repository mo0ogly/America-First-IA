import React, { useState, useEffect, useMemo } from 'react';
import Papa from 'papaparse';
import './DataHub.css';

const DataHub = () => {
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
      const flopsLog = parseFloat(row['16-bit OP/s (log)']);
      if (isNaN(flopsLog) || row.Certainty === 'Unlikely') return;
      const flops = Math.pow(10, flopsLog);
      if (!aggregated[country]) {
        aggregated[country] = { Country: country, Total_16bit_Flops: 0, Cluster_Count: 0, Primary_Status: {} };
      }
      aggregated[country].Total_16bit_Flops += flops;
      aggregated[country].Cluster_Count += 1;
      const status = row.Status || 'Unknown';
      aggregated[country].Primary_Status[status] = (aggregated[country].Primary_Status[status] || 0) + 1;
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
  }, [rawData, viewMode]);

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
                <p><strong>Definition:</strong> Aggregate high-tier compute power available within a nation's borders (PetaFLOP/s). Raw capacities are fetched dynamically and aggregated in the dashboard.</p>

                <div className="pipeline-container">
                  <h6>Execute Factor F Ingestion Pipeline</h6>
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
                    <span className="status-badge planned">🟡 Hybrid Audit Pipeline</span>
                    <button className="btn btn-primary" onClick={() => handleSimpleCSVGrab('energy_prices.csv', setEnergyData)} disabled={loading}>
                      {loading ? '↻ Importing...' : 'Import IEA Reference Data'}
                    </button>
                  </div>
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
                    <span className="status-badge planned">🟡 Hybrid Audit Pipeline</span>
                    <button className="btn btn-primary" onClick={() => handleSimpleCSVGrab('workforce_data.csv', setWorkforceData)} disabled={loading}>
                      {loading ? '↻ Importing...' : 'Import World Bank Data'}
                    </button>
                  </div>
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
