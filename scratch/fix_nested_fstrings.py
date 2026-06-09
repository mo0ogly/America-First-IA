import os
import re

BASE_DIR = r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main"
DOCS_DIR = os.path.join(BASE_DIR, "docs", "a traduire")

# Files list from fix_imports.py
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
    os.path.join(DOCS_DIR, "these", "master_thesis_trilingual.py"),
]

def fix_line(line):
    # 1. Clean up nested double-quoted f-strings on this single line
    count1 = 0
    double_pattern = r'("([^"\\]|\\.)*)f"\{([^}]+)\}([^"]*)"'
    while True:
        line, c = re.subn(double_pattern, r'f\1{\3}\4', line)
        if c == 0:
            break
        count1 += c

    # 2. Clean up nested single-quoted f-strings on this single line
    count2 = 0
    single_pattern = r"('([^'\\]|\\.)*)f'\{([^}]+)\}([^']*)'"
    while True:
        line, c = re.subn(single_pattern, r'f\1{\3}\4', line)
        if c == 0:
            break
        count2 += c

    # 3. Clean up double f-prefixes if any were created (e.g. ff"..." -> f"...")
    line, count3 = re.subn(r'\bff"([^"]*)"', r'f"\1"', line)
    line, count4 = re.subn(r"\bff'([^']*)'", r"f'\1'", line)

    # 4. Clean up triple f-prefixes or other combinations just in case
    line, count5 = re.subn(r'\bfff"([^"]*)"', r'f"\1"', line)
    line, count6 = re.subn(r"\bfff'([^']*)'", r"f'\1'", line)

    return line, (count1 + count2, count3 + count4 + count5 + count6)

def fix_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping (not found): {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    new_lines = []
    total_nested = 0
    total_cleaned = 0
    
    for line in lines:
        new_line, (nested, cleaned) = fix_line(line)
        new_lines.append(new_line)
        total_nested += nested
        total_cleaned += cleaned
        
    new_content = '\n'.join(new_lines)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {os.path.basename(filepath)}: nested_fixed={total_nested}, double_f_cleaned={total_cleaned}")
    else:
        print(f"No changes needed for {os.path.basename(filepath)}")

def main():
    print("=== Line-by-line nested f-string syntax repair tool ===")
    for filepath in FILES:
        fix_file(filepath)
    print("\nRepair completed!")

if __name__ == "__main__":
    main()
