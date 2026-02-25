import React, { useState } from 'react';
import CaciFormula from './components/CaciFormula';
import CountryComparison from './components/CountryComparison';
import DataHub from './components/DataHub';
import './index.css';

function App() {
  const [activeTab, setActiveTab] = useState('formula');

  return (
    <div className="app-layout">
      <header className="app-header">
        <div className="container header-container">
          <div className="logo-area">
            <h1>CACI <span className="glow" style={{ color: 'var(--gold-light)' }}>Dashboard</span></h1>
            <p className="subtitle" style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>
              Compute-Adjusted Competitiveness Index Explorer
            </p>
          </div>
          <nav className="main-nav">
            <button
              className={`nav-btn ${activeTab === 'formula' ? 'active' : ''}`}
              onClick={() => setActiveTab('formula')}
            >
              Methodology & Parameters
            </button>
            <button
              className={`nav-btn ${activeTab === 'compare' ? 'active' : ''}`}
              onClick={() => setActiveTab('compare')}
            >
              Comparative Analysis
            </button>
            <button
              className={`nav-btn ${activeTab === 'data' ? 'active' : ''}`}
              onClick={() => setActiveTab('data')}
            >
              Data Hub & Source Processing
            </button>
          </nav>
        </div>
      </header>

      <main className="container content-area" style={{ marginTop: '40px', paddingBottom: '80px' }}>
        {activeTab === 'formula' && <CaciFormula />}
        {activeTab === 'compare' && <CountryComparison />}
        {activeTab === 'data' && <DataHub />}
      </main>

      <style>{`
        .app-header {
          background: linear-gradient(175deg, var(--navy) 0%, var(--accent-light) 100%);
          padding: 30px 0;
          color: white;
          box-shadow: var(--shadow-md);
        }
        .header-container {
          display: flex;
          justify-content: space-between;
          align-items: flex-end;
          flex-wrap: wrap;
          gap: 20px;
        }
        .logo-area h1 {
          color: white;
          margin-bottom: 4px;
          font-family: var(--font-heading);
          letter-spacing: -0.5px;
        }
        .main-nav {
          display: flex;
          gap: 10px;
          background: rgba(0,0,0,0.2);
          padding: 6px;
          border-radius: 12px;
          backdrop-filter: blur(10px);
        }
        .nav-btn {
          background: transparent;
          border: none;
          color: rgba(255,255,255,0.7);
          padding: 8px 16px;
          border-radius: 8px;
          font-family: var(--font);
          font-size: 0.9rem;
          font-weight: 500;
          cursor: pointer;
          transition: all 0.2s;
        }
        .nav-btn:hover {
          color: white;
          background: rgba(255,255,255,0.1);
        }
        .nav-btn.active {
          color: var(--accent);
          background: white;
          box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
      `}</style>
    </div>
  );
}

export default App;
