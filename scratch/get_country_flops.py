import csv
import os

DATA_DIR = r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main\caci-dashboard\public\data"
GPU_CLUSTERS = os.path.join(DATA_DIR, "gpu_clusters.csv")

COUNTRY_MAP = {
    'United States of America': 'USA',
    'United States': 'USA',
    'USA': 'USA',
    'China': 'Chine',
    'France': 'France',
    'Germany': 'Allemagne',
    'United Kingdom': 'UK',
    'UK': 'UK',
    'Japan': 'Japon',
    'Korea (Republic of)': 'Coree',
    'India': 'Inde',
    'Canada': 'Canada',
    'Netherlands': 'Pays-Bas',
    'Sweden': 'Suede',
    'Brazil': 'Bresil',
}

country_flops = {k: 0.0 for k in COUNTRY_MAP.values()}

with open(GPU_CLUSTERS, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        country = row.get('Country', '').strip()
        status = row.get('Status', '').strip().lower()
        if 'planned' in status or 'cancelled' in status:
            continue
        max_op_log = row.get('Max OP/s (log)', '')
        if not max_op_log:
            continue
        try:
            pflops = (10 ** float(max_op_log)) / 1e15
        except ValueError:
            continue
        
        mapped = COUNTRY_MAP.get(country)
        if mapped:
            country_flops[mapped] += pflops

for k, v in sorted(country_flops.items(), key=lambda x: x[1], reverse=True):
    print(f"{k}: {v:.2f} PF (approx {v/2.0:.2f} kH100-eq)")
