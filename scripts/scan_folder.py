#!/usr/bin/env python3
"""
Scan an input folder and categorize files for deck generation.

Usage:
    python scan_folder.py /path/to/folder

Outputs a JSON report to stdout, grouping files into:
  - template:  the .pptx template to build on (picks one named like
               *template* / *模板* if multiple exist, else the first .pptx)
  - brief:     the user's PPT requirements description — the file that STEERS
               content.md generation (named brief/requirements/需求/outline/...)
  - documents: source content to turn into slides (.md .txt .docx .pdf etc.)
  - data:      tabular data for charts/tables (.csv .xlsx .xls .tsv)
  - images:    figures/logos/photos to place on slides
  - other:     unrecognized files (reported, not used)
"""
import json
import os
import sys

DOC_EXTS = {".md", ".markdown", ".txt", ".docx", ".doc", ".pdf", ".rtf"}
DATA_EXTS = {".csv", ".xlsx", ".xls", ".tsv"}
IMG_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"}
# The brief is the user's natural-language description of what the deck should
# be. Detected by filename so the user can just drop it in the folder.
BRIEF_STEMS = {
    "brief", "requirements", "spec", "instructions", "outline", "config",
    "需求", "要求", "说明", "大纲", "需求说明", "ppt需求", "做ppt",
}


def categorize(folder):
    result = {
        "folder": os.path.abspath(folder),
        "template": None,
        "template_candidates": [],
        "brief": None,
        "brief_candidates": [],
        "documents": [],
        "data": [],
        "images": [],
        "other": [],
    }
    if not os.path.isdir(folder):
        result["error"] = f"Not a directory: {folder}"
        return result

    pptx_files = []
    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        if not os.path.isfile(path) or name.startswith("."):
            continue
        stem, ext = os.path.splitext(name)
        ext = ext.lower()
        stem_l = stem.lower()

        if ext == ".pptx":
            pptx_files.append(path)
        elif (any(k in stem_l for k in BRIEF_STEMS)
              and ext in {".md", ".txt", ".markdown"}):
            result["brief_candidates"].append(path)
        elif ext in DOC_EXTS:
            result["documents"].append(path)
        elif ext in DATA_EXTS:
            result["data"].append(path)
        elif ext in IMG_EXTS:
            result["images"].append(path)
        else:
            result["other"].append(path)

    # Choose the brief: the most specific named requirements file.
    if result["brief_candidates"]:
        result["brief"] = result["brief_candidates"][0]

    # Choose the template: prefer a file whose name signals "template".
    result["template_candidates"] = pptx_files
    if pptx_files:
        preferred = [p for p in pptx_files
                     if any(k in os.path.basename(p).lower()
                            for k in ("template", "模板", "theme", "母版", "brand"))]
        result["template"] = (preferred or pptx_files)[0]

    return result


def main():
    if len(sys.argv) != 2:
        print("Usage: python scan_folder.py /path/to/folder", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(categorize(sys.argv[1]), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
