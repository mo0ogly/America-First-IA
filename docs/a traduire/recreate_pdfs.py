"""
Robust PDF conversion using PowerShell COM automation.
Converts newly generated thesis, annexes, and chapters to docs/pdf/
"""

import subprocess
import os
from pathlib import Path

BASE_DIR = Path(r"C:\Users\pizzif\Documents\GitHub\America-First-IA-main\docs\a traduire")
PDF_DIR = Path(r"C:\Users\pizzif\Documents\GitHub\America-First-IA-main\docs\pdf")

def convert_to_pdf(docx_path: Path, pdf_path: Path):
    """Call PowerShell to convert a single docx to pdf."""
    print(f"Converting: {docx_path.name} ...")
    ps_cmd = f"""
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Open("{docx_path}")
    $doc.SaveAs("{pdf_path}", 17)
    $doc.Close()
    $word.Quit()
    """
    try:
        subprocess.run(["powershell", "-Command", ps_cmd], check=True, capture_output=True)
        print(f"  OK -> {pdf_path.name}")
    except Exception as e:
        print(f"  FAILED -> {docx_path.name}: {e}")

def main():
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Collect Thesis
    thesis_dir = BASE_DIR / "these"
    for f in thesis_dir.glob("*.docx"):
        if not f.name.startswith("~$"):
            convert_to_pdf(f, PDF_DIR / f.with_suffix(".pdf").name)
            
    # 2. Collect Annexes (from subfolders en/fr/br)
    # Annexe A
    annexe_a_dir = BASE_DIR / "annexes" / "Annexe_Econometrique_CACI_FR"
    for lang in ["en", "fr", "br"]:
        for f in (annexe_a_dir / lang).glob("*.docx"):
            convert_to_pdf(f, PDF_DIR / f.with_suffix(".pdf").name)
            
    # Annexes B, C, D, E
    annexes_dir = BASE_DIR / "annexes"
    for lang in ["en", "fr", "br"]:
        for f in (annexes_dir / lang).glob("*.docx"):
            convert_to_pdf(f, PDF_DIR / f.with_suffix(".pdf").name)
            
    # 3. Collect Chapters
    for i in range(1, 9): # Folders 1 to 8
        chapter_dir = BASE_DIR / str(i)
        # Check subfolders en/fr/br if they exist
        for lang in ["en", "fr", "br"]:
            lang_dir = chapter_dir / lang
            if lang_dir.exists():
                for f in lang_dir.glob("*.docx"):
                    convert_to_pdf(f, PDF_DIR / f.with_suffix(".pdf").name)
        # Also check root of chapter folder (some might be there)
        for f in chapter_dir.glob("*.docx"):
            if not f.name.startswith("~$"):
                convert_to_pdf(f, PDF_DIR / f.with_suffix(".pdf").name)

    # 4. Collect FAQs
    docs_root = Path(r"C:\Users\pizzif\Documents\GitHub\America-First-IA-main\docs")
    for lang in ["en", "fr", "br"]:
        lang_dir = docs_root / lang
        if lang_dir.exists():
            for f in lang_dir.glob("FAQ*.docx"):
                convert_to_pdf(f, PDF_DIR / f.with_suffix(".pdf").name)

if __name__ == "__main__":
    main()
