#!/usr/bin/env python3
"""
DOCX to PDF batch converter — Virtual Printer
Uses Microsoft Word via COM automation (docx2pdf/win32com).

Usage:
    python scripts/docx_to_pdf.py docs/en/                              # One folder
    python scripts/docx_to_pdf.py docs/en/Chapter_I.docx                # One file
    python scripts/docx_to_pdf.py --batch docs/en,docs/fr,docs/br       # Multi-folder
    python scripts/docx_to_pdf.py --batch docs/en,docs/fr,docs/br --output dist/pdf/
    python scripts/docx_to_pdf.py --batch docs/en,docs/fr,docs/br --flat # All PDFs in one folder
"""

import argparse
import os
import sys
import time
from pathlib import Path


def find_docx_files(path: Path) -> list[Path]:
    """Find all .docx files in a path, excluding Word temp files (~$)."""
    if path.is_file():
        if path.suffix.lower() == ".docx" and not path.name.startswith("~$"):
            return [path]
        return []
    if path.is_dir():
        return sorted(
            f for f in path.glob("*.docx")
            if not f.name.startswith("~$")
        )
    return []


def convert_single(input_path: Path, output_path: Path) -> tuple[bool, str]:
    """Convert a single DOCX to PDF. Returns (success, message)."""
    try:
        from docx2pdf import convert
        output_path.parent.mkdir(parents=True, exist_ok=True)
        convert(str(input_path), str(output_path))
        if output_path.exists():
            size_mb = output_path.stat().st_size / (1024 * 1024)
            return True, f"OK ({size_mb:.1f} MB)"
        return False, "PDF not created (unknown error)"
    except ImportError:
        return False, "docx2pdf not installed. Run: pip install docx2pdf"
    except PermissionError:
        return False, "LOCKED (file open in Word?)"
    except Exception as e:
        return False, f"ERROR: {e}"


def resolve_output_path(
    input_file: Path,
    input_root: Path,
    output_dir: Path | None,
    flat: bool
) -> Path:
    """Determine output PDF path based on mode."""
    pdf_name = input_file.with_suffix(".pdf").name

    if output_dir:
        if flat:
            # All PDFs in one flat folder, prefix with lang to avoid collisions
            lang = input_root.name  # en, fr, br
            return output_dir / f"{lang}_{pdf_name}"
        else:
            # Preserve folder structure: output/en/file.pdf, output/fr/file.pdf
            lang = input_root.name
            return output_dir / lang / pdf_name
    else:
        # Same folder as source, in pdf/ subfolder
        return input_root / "pdf" / pdf_name


def run_batch(
    folders: list[Path],
    output_dir: Path | None,
    flat: bool
):
    """Run batch conversion across multiple folders."""
    # Collect all files
    all_files: list[tuple[Path, Path]] = []  # (input_file, input_root)
    for folder in folders:
        folder = folder.resolve()
        if not folder.exists():
            print(f"  WARNING: {folder} does not exist, skipping")
            continue
        files = find_docx_files(folder)
        for f in files:
            root = folder if folder.is_dir() else folder.parent
            all_files.append((f, root))

    if not all_files:
        print("No .docx files found.")
        return

    total = len(all_files)
    success_count = 0
    error_count = 0
    errors: list[tuple[str, str]] = []

    print(f"\n{'='*60}")
    print(f"  DOCX to PDF — Virtual Printer")
    print(f"  {total} files to convert")
    print(f"{'='*60}\n")

    start_time = time.time()

    for i, (input_file, input_root) in enumerate(all_files, 1):
        output_path = resolve_output_path(input_file, input_root, output_dir, flat)
        lang_tag = input_root.name.upper()

        print(f"  [{i:>{len(str(total))}}/{total}] [{lang_tag:>2}] {input_file.name} ", end="", flush=True)

        ok, msg = convert_single(input_file, output_path)

        if ok:
            success_count += 1
            print(f"-> {msg}")
        else:
            error_count += 1
            errors.append((input_file.name, msg))
            print(f"-> {msg}")

    elapsed = time.time() - start_time

    # Summary
    print(f"\n{'='*60}")
    print(f"  DONE in {elapsed:.1f}s")
    print(f"  {success_count} converted | {error_count} errors | {total} total")
    if output_dir:
        print(f"  Output: {output_dir}")
    else:
        print(f"  Output: pdf/ subfolder in each source directory")
    print(f"{'='*60}")

    if errors:
        print(f"\n  ERRORS:")
        for name, msg in errors:
            print(f"    - {name}: {msg}")

    return success_count, error_count


def main():
    parser = argparse.ArgumentParser(
        description="DOCX to PDF batch converter (Microsoft Word via COM)"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="Input file or directory (use --batch for multiple dirs)"
    )
    parser.add_argument(
        "--batch",
        type=str,
        help="Comma-separated list of directories (e.g. docs/en,docs/fr,docs/br)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Output directory for PDFs (default: pdf/ subfolder in source dir)"
    )
    parser.add_argument(
        "--flat",
        action="store_true",
        help="Put all PDFs in one flat output folder (prefix with lang)"
    )

    args = parser.parse_args()

    if not args.input and not args.batch:
        parser.print_help()
        sys.exit(1)

    output_dir = Path(args.output).resolve() if args.output else None

    if args.batch:
        folders = [Path(d.strip()) for d in args.batch.split(",")]
        run_batch(folders, output_dir, args.flat)
    elif args.input:
        input_path = Path(args.input)
        if input_path.is_file():
            # Single file
            out = output_dir / input_path.with_suffix(".pdf").name if output_dir else input_path.with_suffix(".pdf")
            ok, msg = convert_single(input_path, out)
            print(f"  {input_path.name} -> {msg}")
            if ok:
                print(f"  Output: {out}")
        else:
            run_batch([input_path], output_dir, args.flat)


if __name__ == "__main__":
    main()
