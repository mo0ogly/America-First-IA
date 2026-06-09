import os
import re

BASE_DIR = r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main"
DOCS_DIR = os.path.join(BASE_DIR, "docs", "a traduire")

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

ANNEXES = [
    os.path.join(DOCS_DIR, "annexes", "Annexe_Econometrique_CACI_FR", "generate_annexe_a_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_b_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_c_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_d_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "generate_annexe_e_trilingual.py"),
    os.path.join(DOCS_DIR, "annexes", "annexes_helpers.py"),
]

def get_import_block(parent_level):
    return f"""import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[{parent_level}]))
import caci_data_helper
m = caci_data_helper.get_metrics()
us_share = m['us_compute_share']
us_eu_caci = m['us_eu_caci_power_ratio']
us_eu_raw = m['us_eu_raw_ratio']
eu_sov = m['eu_sovereignty_ratio']
caci_scores = {{k: v['caci_power_phys'] for k, v in m['country_results'].items()}}

def fmt_fr(val, decimals=1):
    return f"{{val:.{{decimals}}f}}".replace(".", ",")

def fmt_en(val, decimals=1):
    return f"{{val:.{{decimals}}f}}"
"""

# Whole-token replacements (with quotes)
WHOLE_REPLACEMENTS = [
    # Cover banner lines
    ('"76.9% global operational AI compute = USA"', 'f"{fmt_en(us_share, 1)}% global operational AI compute = USA"'),
    ('"76.9% of global operational AI compute = USA"', 'f"{fmt_en(us_share, 1)}% of global operational AI compute = USA"'),
    ('"76,9 pct du compute IA operationnel mondial = USA"', 'f"{fmt_fr(us_share, 1)} pct du compute IA operationnel mondial = USA"'),
    ('"76,9% da computacao de IA operacional global = EUA"', 'f"{fmt_fr(us_share, 1)}% da computacao de IA operacional global = EUA"'),
    ('"76,9% do compute IA operacional mondial = EUA"', 'f"{fmt_fr(us_share, 1)}% do compute IA operacional mundial = EUA"'),
    ('"76,9% do compute IA operacional mundial = EUA"', 'f"{fmt_fr(us_share, 1)}% do compute IA operacional mundial = EUA"'),
    ('"3.46:1 CACI ratio US/EU (Power Mode)"', 'f"{fmt_en(us_eu_caci, 2)}:1 CACI ratio US/EU (Power Mode)"'),
    ('"3.46:1 US/EU CACI ratio (Power Mode)"', 'f"{fmt_en(us_eu_caci, 2)}:1 US/EU CACI ratio (Power Mode)"'),
    ('"3,46:1 ratio CACI US/EU (Power Mode)"', 'f"{fmt_fr(us_eu_caci, 2)}:1 ratio CACI US/EU (Power Mode)"'),
    ('"3,46:1 ratio CACI EUA/UE (Power Mode)"', 'f"{fmt_fr(us_eu_caci, 2)}:1 ratio CACI EUA/UE (Power Mode)"'),

    # Other specific lines with double quotes
    ('"76.9 percent"', 'f"{fmt_en(us_share, 1)} percent"'),
    ('"76,9 pour cent"', 'f"{fmt_fr(us_share, 1)} pour cent"'),
    ('"76,9 pourcent"', 'f"{fmt_fr(us_share, 1)} pour cent"'),
    ('"76.9%"', 'f"{fmt_en(us_share, 1)}%"'),
    ('"76,9%"', 'f"{fmt_fr(us_share, 1)}%"'),
    ('"76.9 pct"', 'f"{fmt_en(us_share, 1)} pct"'),
    ('"76,9 pct"', 'f"{fmt_fr(us_share, 1)} pct"'),
    
    ('"3.46:1"', 'f"{fmt_en(us_eu_caci, 2)}:1"'),
    ('"3,46:1"', 'f"{fmt_fr(us_eu_caci, 2)}:1"'),
    ('"3.46 to 1"', 'f"{fmt_en(us_eu_caci, 2)} to 1"'),
    ('"3,46 a 1"', 'f"{fmt_fr(us_eu_caci, 2)} a 1"'),
    
    ('"17.6:1"', 'f"{fmt_en(us_eu_raw, 1)}:1"'),
    ('"17,6:1"', 'f"{fmt_fr(us_eu_raw, 1)}:1"'),
    ('"17.6 to 1"', 'f"{fmt_en(us_eu_raw, 1)} to 1"'),
    ('"17,6 a 1"', 'f"{fmt_fr(us_eu_raw, 1)} a 1"'),
    
    ('"99.2%"', 'f"{fmt_en(eu_sov, 1)}%"'),
    ('"99,2%"', 'f"{fmt_fr(eu_sov, 1)}%"'),
    ('"99.2 percent"', 'f"{fmt_en(eu_sov, 1)} percent"'),
    ('"99,2 pour cent"', 'f"{fmt_fr(eu_sov, 1)} pour cent"'),
    ('"99.2 pct"', 'f"{fmt_en(eu_sov, 1)} pct"'),
    ('"99,2 pct"', 'f"{fmt_fr(eu_sov, 1)} pct"'),

    # Scores as whole tokens in tables
    ('"28.9"', "fmt_en(caci_scores['EU'], 1)"),
    ('"28,9"', "fmt_fr(caci_scores['EU'], 1)"),
    ('"25.3"', "fmt_en(caci_scores['France'], 1)"),
    ('"25,3"', "fmt_fr(caci_scores['France'], 1)"),
    ('"22.2"', "fmt_en(caci_scores['India'], 1)"),
    ('"22,2"', "fmt_fr(caci_scores['India'], 1)"),
    ('"15.7"', "fmt_en(caci_scores['China'], 1)"),
    ('"15,7"', "fmt_fr(caci_scores['China'], 1)"),
    ('"7.0"', "fmt_en(caci_scores['UK'], 1)"),
    ('"7,0"', "fmt_fr(caci_scores['UK'], 1)"),
    ('"5.4"', "fmt_en(caci_scores['Germany'], 1)"),
    ('"5,4"', "fmt_fr(caci_scores['Germany'], 1)"),
]

# Substring replacements inside string literals
SUBSTRING_REPLACEMENTS = [
    # Compute Share
    ("76,9 pour cent", "{fmt_fr(us_share, 1)} pour cent"),
    ("76,9 pourcent", "{fmt_fr(us_share, 1)} pour cent"),
    ("76,9%", "{fmt_fr(us_share, 1)}%"),
    ("76,9 pct", "{fmt_fr(us_share, 1)} pct"),
    ("76.9 percent", "{fmt_en(us_share, 1)} percent"),
    ("76.9%", "{fmt_en(us_share, 1)}%"),
    ("76.9 pct", "{fmt_en(us_share, 1)} pct"),

    # CACI Power Ratio US/EU
    ("3,46:1", "{fmt_fr(us_eu_caci, 2)}:1"),
    ("3,46 a 1", "{fmt_fr(us_eu_caci, 2)} a 1"),
    ("3.46:1", "{fmt_en(us_eu_caci, 2)}:1"),
    ("3.46 to 1", "{fmt_en(us_eu_caci, 2)} to 1"),

    # Raw Ratio
    ("17,6:1", "{fmt_fr(us_eu_raw, 1)}:1"),
    ("17,6 a 1", "{fmt_fr(us_eu_raw, 1)} a 1"),
    ("17.6:1", "{fmt_en(us_eu_raw, 1)}:1"),
    ("17.6 to 1", "{fmt_en(us_eu_raw, 1)} to 1"),

    # EU Sovereignty
    ("99,2%", "{fmt_fr(eu_sov, 1)}%"),
    ("99,2 pour cent", "{fmt_fr(eu_sov, 1)} pour cent"),
    ("99,2 pct", "{fmt_fr(eu_sov, 1)} pct"),
    ("99.2%", "{fmt_en(eu_sov, 1)}%"),
    ("99.2 percent", "{fmt_en(eu_sov, 1)} percent"),
    ("99.2 pct", "{fmt_en(eu_sov, 1)} pct"),

    # Country scores (only when surrounded by spaces or punctuation to avoid matching inside other numbers)
    # E.g. "UE(13) = 28,9" or "France = 25,3"
    ("UE(13) = 28,9", "UE(13) = {fmt_fr(caci_scores['EU'], 1)}"),
    ("UE(13) = 28.9", "UE(13) = {fmt_en(caci_scores['EU'], 1)}"),
    ("EU(13) = 28.9", "EU(13) = {fmt_en(caci_scores['EU'], 1)}"),
    ("UE = 28.9", "UE = {fmt_en(caci_scores['EU'], 1)}"),
    
    ("France = 25,3", "France = {fmt_fr(caci_scores['France'], 1)}"),
    ("France = 25.3", "France = {fmt_en(caci_scores['France'], 1)}"),
    
    ("Allemagne = 5,4", "Allemagne = {fmt_fr(caci_scores['Germany'], 1)}"),
    ("Germany = 5.4", "Germany = {fmt_en(caci_scores['Germany'], 1)}"),
    
    ("Chine = 15,7", "Chine = {fmt_fr(caci_scores['China'], 1)}"),
    ("China = 15.7", "China = {fmt_en(caci_scores['China'], 1)}"),
    
    ("Royaume-Uni = 7,0", "Royaume-Uni = {fmt_fr(caci_scores['UK'], 1)}"),
    ("UK = 7.0", "UK = {fmt_en(caci_scores['UK'], 1)}"),
    
    ("Inde = 22,2", "Inde = {fmt_fr(caci_scores['India'], 1)}"),
    ("India = 22.2", "India = {fmt_en(caci_scores['India'], 1)}"),
]

def convert_file(filepath, parent_level):
    if not os.path.exists(filepath):
        print(f"Skipping (not found): {filepath}")
        return

    print(f"Processing: {os.path.basename(filepath)}")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    import_inserted = False

    for line_idx, line in enumerate(lines):
        # Insert import block after the first docstring or right at the top
        if not import_inserted:
            # We can insert after the first comment/docstring block ends
            # Let's check if the line has the end of docstring """ or '''
            if '"""' in line or "'''" in line or line_idx > 10:
                new_lines.append(line)
                new_lines.append("\n" + get_import_block(parent_level) + "\n")
                import_inserted = True
                continue

        # Check if this line starts with a comment
        stripped = line.strip()
        if stripped.startswith("#"):
            new_lines.append(line)
            continue

        # Check for whole replacements first
        line_modified = False
        temp_line = line
        for target, replacement in WHOLE_REPLACEMENTS:
            if target in temp_line:
                temp_line = temp_line.replace(target, replacement)
                line_modified = True

        # Check for substring replacements
        for target, replacement in SUBSTRING_REPLACEMENTS:
            if target in temp_line:
                # We need to turn this line into an f-string!
                # Replace the substring
                temp_line = temp_line.replace(target, replacement)
                line_modified = True

                # Check if it has a string literal and doesn't start with f already
                # Find the first quote: " or '
                # E.g.    "Some text..."
                # We want to change to f"Some text..."
                # Use regex to find first quote on the line
                match = re.search(r"(['\"]+)", temp_line)
                if match:
                    quote_pos = match.start()
                    # Check if there is already an 'f' or 'r' before it
                    before = temp_line[:quote_pos]
                    if not before.rstrip().endswith('f') and not before.rstrip().endswith('r'):
                        # Insert 'f' immediately before the quote
                        temp_line = temp_line[:quote_pos] + 'f' + temp_line[quote_pos:]

        new_lines.append(temp_line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Successfully modified: {os.path.basename(filepath)}")

def main():
    print("Converting Chapters...")
    for ch in CHAPTERS:
        # Determine parent level
        rel = os.path.relpath(ch, DOCS_DIR)
        parts = rel.split(os.sep)
        level = len(parts) - 1
        convert_file(ch, level)

    print("\nConverting Annexes...")
    for ax in ANNEXES:
        rel = os.path.relpath(ax, DOCS_DIR)
        parts = rel.split(os.sep)
        level = len(parts) - 1
        convert_file(ax, level)

if __name__ == "__main__":
    main()
