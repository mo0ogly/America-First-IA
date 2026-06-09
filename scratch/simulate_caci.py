import sys
import os

# Base structure with new proposed GDP and Workforce numbers
# GDP: 2026 Projections (IMF WEO April 2026)
# Workforce (L): FTE R&D researchers (in millions) consistent with latest OECD/Eurostat/World Bank
base = {
    'USA': {'f_total': 2769706, 'f': 2769706, 'e': 85.0, 'l': 3.6, 'gdp': 31.9, 'r': 1.0},
    'China': {'f_total': 1004123, 'f': 1004123, 'e': 92.0, 'l': 4.8, 'gdp': 23.7, 'r': 0.1},
    'EU': {'f_total': 157640, 'f': 123925, 'e': 135.0, 'l': 3.1, 'gdp': 20.0, 'r': 1.0},
    'UK': {'f_total': 95340, 'f': 95340, 'e': 190.0, 'l': 0.5, 'gdp': 3.9, 'r': 1.0},
    'Asia (Ex-China)': {'f_total': 185120, 'f': 185120, 'e': 120.0, 'l': 1.8, 'gdp': 14.8, 'r': 0.5},
    'India': {'f_total': 150, 'f': 80, 'e': 88.0, 'l': 0.4, 'gdp': 5.6, 'r': 0.5},
    'UAE': {'f_total': 620, 'f': 85, 'e': 80.0, 'l': 0.15, 'gdp': 0.62, 'r': 0.5},
    'France': {'f_total': 36420, 'f': 27500, 'e': 115.0, 'l': 0.65, 'gdp': 3.4, 'r': 1.0},
    'Germany': {'f_total': 42000, 'f': 42000, 'e': 140.0, 'l': 0.85, 'gdp': 4.7, 'r': 1.0},
    'South America': {'f_total': 10, 'f': 10, 'e': 95.0, 'l': 0.6, 'gdp': 5.0, 'r': 0.5},
    'Africa': {'f_total': 10, 'f': 10, 'e': 110.0, 'l': 0.4, 'gdp': 3.6, 'r': 0.5},
}

# Formula exponents
wf, we, wl, wr = 0.40, 0.25, 0.20, 0.15

raw_power_phys = {}
raw_power_sov = {}

for k, d in base.items():
    f_p = d['f_total']
    f_s = d['f']
    l = d['l']
    r = d['r']
    e = d['e']
    
    raw_power_phys[k] = (f_p ** wf * l ** wl * r ** wr) / (e ** we)
    raw_power_sov[k] = (f_s ** wf * l ** wl * r ** wr) / (e ** we)

usa_power_phys = raw_power_phys['USA']

print("SIMULATED CACI SCORES (USA Physical = 100)")
print("=" * 80)
print(f"{'Country':<18} | {'CACI_Power_Phys':<15} | {'CACI_Power_Sov':<15}")
print("-" * 80)
for k in sorted(base.keys()):
    caci_p = (raw_power_phys[k] / usa_power_phys) * 100
    caci_s = (raw_power_sov[k] / usa_power_phys) * 100
    print(f"{k:<18} | {caci_p:<15.2f} | {caci_s:<15.2f}")

print("=" * 80)
print(f"US/EU CACI Power Ratio (Phys): {raw_power_phys['USA'] / raw_power_phys['EU']:.2f}:1")
print(f"US/EU CACI Power Ratio (Sov): {raw_power_sov['USA'] / raw_power_sov['EU']:.2f}:1")
print(f"US/France CACI Ratio (Phys): {raw_power_phys['USA'] / raw_power_phys['France']:.2f}:1")
print(f"US/Germany CACI Ratio (Phys): {raw_power_phys['USA'] / raw_power_phys['Germany']:.2f}:1")
print(f"US/China CACI Ratio (Phys): {raw_power_phys['USA'] / raw_power_phys['China']:.2f}:1")
