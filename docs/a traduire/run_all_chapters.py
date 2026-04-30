"""
Industrialize the trilingual generation of all thesis chapters.
Runs each chapter's generator script and organizes the output.
"""

import subprocess
import os
from pathlib import Path

BASE_DIR = Path(r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main\docs\a traduire")

GENERATORS = [
    BASE_DIR / "1" / "generate_chapter1_trilingual.py",
    BASE_DIR / "2" / "generate_chapter2_trilingual.py",
    BASE_DIR / "3" / "generate_chapter3_trilingual.py",
    BASE_DIR / "4" / "generate_chapter4_trilingual.py",
    BASE_DIR / "5" / "generate_chapter5_trilingual.py",
    BASE_DIR / "6" / "generate_chapter6_graphs_trilingual.py",
    BASE_DIR / "6" / "generate_chapter6_trilingual.py",
    BASE_DIR / "6" / "generate_chapter6bis_trilingual.py",
    BASE_DIR / "6" / "generate_chapter6ter_trilingual.py",
    BASE_DIR / "6" / "generate_chapter6quater_trilingual.py",
    BASE_DIR / "7" / "generate_chapter7_graphs_trilingual.py",
    BASE_DIR / "7" / "generate_chapter7_trilingual.py",
    BASE_DIR / "8" / "generate_conclusion_graphs_trilingual.py",
    BASE_DIR / "8" / "generate_conclusion_trilingual.py",
]

def run_generators():
    for gen in GENERATORS:
        if gen.exists():
            print(f"Running {gen.name} in {gen.parent}...")
            subprocess.run(["C:\\Python313\\python.exe", str(gen)], cwd=str(gen.parent), check=True)
        else:
            print(f"Warning: {gen} not found.")

if __name__ == "__main__":
    run_generators()
