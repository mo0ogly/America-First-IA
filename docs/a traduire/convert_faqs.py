"""
Convert only FAQs to PDF.
"""

import subprocess
from pathlib import Path

PDF_DIR = Path(r"C:\Users\pizzif\Documents\GitHub\America-First-IA-main\docs\pdf")
DOCS_ROOT = Path(r"C:\Users\pizzif\Documents\GitHub\America-First-IA-main\docs")

def convert_to_pdf(docx_path: Path, pdf_path: Path):
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
    for lang in ["en", "fr", "br"]:
        lang_dir = DOCS_ROOT / lang
        if lang_dir.exists():
            for f in lang_dir.glob("FAQ*.docx"):
                convert_to_pdf(f, PDF_DIR / f.with_suffix(".pdf").name)

if __name__ == "__main__":
    main()
