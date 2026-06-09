import os
import re

BASE_DIR = r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main"
DOCS_DIR = os.path.join(BASE_DIR, "docs", "a traduire")

# All files we need to check
FILES = [
    os.path.join(DOCS_DIR, "1", "generate_chapter1_trilingual.py"),
    os.path.join(DOCS_DIR, "2", "generate_chapter2_trilingual.py"),
    os.path.join(DOCS_DIR, "3", "generate_chapter3_trilingual.py"),
    os.path.join(DOCS_DIR, "4", "generate_chapter4_trilingual.py"),
    os.path.join(DOCS_DIR, "5", "generate_chapter5_trilingual.py"),
    os.path.join(DOCS_DIR, "6", "generate_chapter6_trilingual.py"),
    os.path.join(DOCS_DIR, "6", "generate_chapter6bis_trilingual.py"),
    os.path.join(DOCS_DIR, "6", "generate_chapter6ter_trilingual.py"),
    os.path.join(DOCS_DIR, "6", "generate_chapter6quater_trilingual.py"),
    os.path.join(DOCS_DIR, "7", "generate_chapter7_trilingual.py"),
    os.path.join(DOCS_DIR, "8", "generate_conclusion_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "Annexe_Econometrique_CACI_FR", "generate_annexe_a_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_b_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_c_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_d_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_e_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "annexes_helpers.py"),
]

def fix_file(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for the broken pattern: from __future__ import sys ... import annotations
    pattern = r"from __future__ import sys\s+from pathlib import Path\s+sys\.path\.append\(str\(Path\(__file__\)\.resolve\(\)\.parents\[(\d+)\]\)\)\s+import caci_data_helper\s+m = caci_data_helper\.get_metrics\(\)\s+us_share = m\['us_compute_share'\]\s+us_eu_caci = m\['us_eu_caci_power_ratio'\]\s+us_eu_raw = m\['us_eu_raw_ratio'\]\s+eu_sov = m\['eu_sovereignty_ratio'\]\s+caci_scores = \{k: v\['caci_power_phys'\] for k, v in m\['country_results'\]\.items\(\)\}\s+import annotations"
    
    # We want to replace it with:
    # from __future__ import annotations
    # import sys
    # from pathlib import Path
    # sys.path.append(str(Path(__file__).resolve().parents[X]))
    # import caci_data_helper
    # ...

    match = re.search(pattern, content)
    if match:
        parent_level = match.group(1)
        replacement = f"""from __future__ import annotations

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[{parent_level}]))
import caci_data_helper
m = caci_data_helper.get_metrics()
us_share = m['us_compute_share']
us_eu_caci = m['us_eu_caci_power_ratio']
us_eu_raw = m['us_eu_raw_ratio']
eu_sov = m['eu_sovereignty_ratio']
caci_scores = {{k: v['caci_power_phys'] for k, v in m['country_results'].items()}}"""

        # Replace exactly
        content = content[:match.start()] + replacement + content[match.end():]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed imports in: {os.path.basename(filepath)}")
    else:
        print(f"Pattern not matched in: {os.path.basename(filepath)}")

def main():
    for filepath in FILES:
        fix_file(filepath)

if __name__ == "__main__":
    main()
