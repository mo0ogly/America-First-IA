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

def get_correct_parent_level(filepath):
    # Determine level relative to "docs/a traduire"
    rel = os.path.relpath(filepath, DOCS_DIR)
    parts = rel.split(os.sep)
    # Number of directories above the file to reach "docs/a traduire"
    # For "1/generate_chapter1_trilingual.py", parts = ['1', 'filename'] -> length 2 -> level 1
    # For "annexes/Annexe_Econometrique_CACI_FR/gen.py", parts = ['annexes', 'Annexe_Econometrique_CACI_FR', 'filename'] -> length 3 -> level 2
    # For "annexes/gen.py", parts = ['annexes', 'filename'] -> length 2 -> level 1
    # For "these/gen.py", parts = ['these', 'filename'] -> length 2 -> level 1
    return len(parts) - 1

def main():
    print("Checking and fixing sys.path.append parent levels...")
    for filepath in FILES:
        if not os.path.exists(filepath):
            print(f"Skipping (not found): {filepath}")
            continue
            
        correct_level = get_correct_parent_level(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find sys.path.append(str(Path(__file__).resolve().parents[X]))
        pattern = r"sys\.path\.append\(str\(Path\(__file__\)\.resolve\(\)\.parents\[\d+\]\)\)"
        replacement = f"sys.path.append(str(Path(__file__).resolve().parents[{correct_level}]))"
        
        new_content, count = re.subn(pattern, replacement, content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}: parents[{correct_level}] (replaced {count} occurence(s))")
        else:
            # Check if there is a different pattern
            print(f"Pattern not found in: {os.path.basename(filepath)}")

if __name__ == "__main__":
    main()
