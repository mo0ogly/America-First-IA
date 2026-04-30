"""
Batch convert the newly generated trilingual docx files to PDF.
Outputs directly to docs/pdf/
"""

import subprocess
import os
from pathlib import Path

BASE_DIR = Path(r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main\docs\a traduire")
PDF_DIR = Path(r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main\docs\pdf")
CONVERTER = Path(r"c:\Users\pizzif\Documents\GitHub\America-First-IA-main\scripts\docx_to_pdf.py")

# Groups of files to convert
TARGETS = [
    BASE_DIR / "these",  # Master Thesis
    BASE_DIR / "annexes", # Annexes B, C, D, E
    BASE_DIR / "annexes" / "Annexe_Econometrique_CACI_FR", # Annexe A
    BASE_DIR / "1",
    BASE_DIR / "2",
    BASE_DIR / "3",
    BASE_DIR / "4",
    BASE_DIR / "5",
    BASE_DIR / "6",
    BASE_DIR / "7",
    BASE_DIR / "8",
]

def run_conversion():
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    
    for target in TARGETS:
        if target.exists():
            print(f"Converting files in {target}...")
            # We use --flat to put all PDFs in one folder, but we want them in PDF_DIR
            # Actually docx_to_pdf.py --output expects a directory.
            # If we use --flat, it prefixes with the folder name.
            # Maybe it's better to just call it on each folder with --output PDF_DIR
            subprocess.run([
                "C:\\Python313\\python.exe", 
                str(CONVERTER), 
                str(target), 
                "--output", str(PDF_DIR),
                "--flat" # Use flat to avoid subfolders like 'en', 'fr', 'br' if the script tries to be smart
            ], check=True)

if __name__ == "__main__":
    run_conversion()
