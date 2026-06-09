import os
import re

# Workspace directory
BASE_DIR = r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main"
DOCS_DIR = os.path.join(BASE_DIR, "docs", "a traduire")

# List of chapter files
CHAPTERS = [
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
]

# List of annexes files
ANNEXES = [
    os.path.join(DOCS_DIR, "annexes", "Annexe_Econometrique_CACI_FR", "generate_annexe_a_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_b_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_c_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_d_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_e_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "annexes_helpers.py"),
]

IMPORT_BLOCK_CHAPTER = """
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
import caci_data_helper
m = caci_data_helper.get_metrics()
us_share = m['us_compute_share']
us_eu_caci = m['us_eu_caci_power_ratio']
us_eu_raw = m['us_eu_raw_ratio']
eu_sov = m['eu_sovereignty_ratio']
caci_scores = {k: v['caci_power_phys'] for k, v in m['country_results'].items()}
"""

IMPORT_BLOCK_ANNEXE = """
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
import caci_data_helper
m = caci_data_helper.get_metrics()
us_share = m['us_compute_share']
us_eu_caci = m['us_eu_caci_power_ratio']
us_eu_raw = m['us_eu_raw_ratio']
eu_sov = m['eu_sovereignty_ratio']
caci_scores = {k: v['caci_power_phys'] for k, v in m['country_results'].items()}
"""

IMPORT_BLOCK_ANNEXE_HELPERS = """
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
import caci_data_helper
m = caci_data_helper.get_metrics()
us_share = m['us_compute_share']
us_eu_caci = m['us_eu_caci_power_ratio']
us_eu_raw = m['us_eu_raw_ratio']
eu_sov = m['eu_sovereignty_ratio']
caci_scores = {k: v['caci_power_phys'] for k, v in m['country_results'].items()}
"""

def make_file_dynamic(filepath, import_block):
    if not os.path.exists(filepath):
        print(f"Skipping (not found): {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already modified
    if "caci_data_helper" in content:
        print(f"Already dynamic: {os.path.basename(filepath)}")
        return

    # Add import block after docstring or first imports
    # Find position after imports
    match = re.search(r"import\s+\w+", content)
    if match:
        pos = match.start()
        content = content[:pos] + import_block.strip() + "\n" + content[pos:]
    else:
        # Fallback to top
        content = import_block.strip() + "\n" + content

    # Perform string replacements for metrics
    # US Share
    content = content.replace('"76.9% global operational AI compute = USA"', 'f"{us_share:.1f}% global operational AI compute = USA"')
    content = content.replace('"76.9% of global operational AI compute = USA"', 'f"{us_share:.1f}% of global operational AI compute = USA"')
    content = content.replace('"76,9 pct du compute IA operationnel mondial = USA"', 'f"{us_share:.1f}".replace(".", ",") + " pct du compute IA operationnel mondial = USA"')
    content = content.replace('"76,9% da computacao de IA operacional global = EUA"', 'f"{us_share:.1f}".replace(".", ",") + "% da computacao de IA operacional global = EUA"')
    content = content.replace('"76,9% do compute IA operacional mondial = EUA"', 'f"{us_share:.1f}".replace(".", ",") + "% do compute IA operacional mundial = EUA"')
    content = content.replace('"76,9% do compute IA operacional mundial = EUA"', 'f"{us_share:.1f}".replace(".", ",") + "% do compute IA operacional mundial = EUA"')
    content = content.replace('76.9 percent', 'f"{us_share:.1f} percent"')
    content = content.replace('76,9 pour cent', 'f"{us_share:.1f}".replace(".", ",") + " pour cent"')
    content = content.replace('76,9 pourcent', 'f"{us_share:.1f}".replace(".", ",") + " pour cent"')
    content = content.replace('76,9%', 'f"{us_share:.1f}".replace(".", ",") + "%"')
    content = content.replace('76.9%', 'f"{us_share:.1f}%"')
    content = content.replace('76,9 pct', 'f"{us_share:.1f}".replace(".", ",") + " pct"')
    content = content.replace('76.9 pct', 'f"{us_share:.1f} pct"')
    
    # CACI Power ratio US/EU
    content = content.replace('"3.46:1 CACI ratio US/EU (Power Mode)"', 'f"{us_eu_caci:.2f}:1 CACI ratio US/EU (Power Mode)"')
    content = content.replace('"3.46:1 US/EU CACI ratio (Power Mode)"', 'f"{us_eu_caci:.2f}:1 US/EU CACI ratio (Power Mode)"')
    content = content.replace('"3,46:1 ratio CACI US/EU (Power Mode)"', 'f"{us_eu_caci:.2f}".replace(".", ",") + ":1 ratio CACI US/EU (Power Mode)"')
    content = content.replace('"3,46:1 ratio CACI EUA/UE (Power Mode)"', 'f"{us_eu_caci:.2f}".replace(".", ",") + ":1 ratio CACI EUA/UE (Power Mode)"')
    content = content.replace('3.46:1', 'f"{us_eu_caci:.2f}:1"')
    content = content.replace('3,46:1', 'f"{us_eu_caci:.2f}".replace(".", ",") + ":1"')
    content = content.replace('3.46 to 1', 'f"{us_eu_caci:.2f} to 1"')
    content = content.replace('3,46 a 1', 'f"{us_eu_caci:.2f}".replace(".", ",") + " a 1"')
    content = content.replace('3.46', 'f"{us_eu_caci:.2f}"')
    
    # Raw Compute ratio
    content = content.replace('17.6:1', 'f"{us_eu_raw:.1f}:1"')
    content = content.replace('17,6:1', 'f"{us_eu_raw:.1f}".replace(".", ",") + ":1"')
    content = content.replace('17.6 to 1', 'f"{us_eu_raw:.1f} to 1"')
    content = content.replace('17,6 a 1', 'f"{us_eu_raw:.1f}".replace(".", ",") + " a 1"')
    
    # EU sovereignty
    content = content.replace('99.2%', 'f"{eu_sov:.1f}%"')
    content = content.replace('99,2%', 'f"{eu_sov:.1f}".replace(".", ",") + "%"')
    content = content.replace('99.2 percent', 'f"{eu_sov:.1f} percent"')
    content = content.replace('99,2 pour cent', 'f"{eu_sov:.1f}".replace(".", ",") + " pour cent"')
    content = content.replace('99.2 pct', 'f"{eu_sov:.1f} pct"')
    content = content.replace('99,2 pct', 'f"{eu_sov:.1f}".replace(".", ",") + " pct"')

    # Country CACI scores (normalized)
    content = content.replace('28.9', 'f"{caci_scores[\'EU\']:.1f}"')
    content = content.replace('25.3', 'f"{caci_scores[\'France\']:.1f}"')
    content = content.replace('22.2', 'f"{caci_scores[\'India\']:.1f}"')
    content = content.replace('15.7', 'f"{caci_scores[\'China\']:.1f}"')
    content = content.replace('7.0', 'f"{caci_scores[\'UK\']:.1f}"')
    content = content.replace('5.4', 'f"{caci_scores[\'Germany\']:.1f}"')

    # Fix potential python syntax errors due to nesting double quotes
    # Ensure f-strings are formatted correctly
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully converted: {os.path.basename(filepath)}")

def main():
    print("MIGRATING CHAPTERS...")
    for ch in CHAPTERS:
        make_file_dynamic(ch, IMPORT_BLOCK_CHAPTER)

    print("\nMIGRATING ANNEXES...")
    for ax in ANNEXES[:-1]:
        make_file_dynamic(ax, IMPORT_BLOCK_ANNEXE)
    
    # helper has a different parent level
    make_file_dynamic(ANNEXES[-1], IMPORT_BLOCK_ANNEXE_HELPERS)

if __name__ == "__main__":
    main()
