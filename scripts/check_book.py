"""Small, dependency-free checks for the Jura fra bunden source tree."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
main = ROOT / "main.tex"
text = main.read_text(encoding="utf-8")

chapters = re.findall(r"\\include\{([^}]+)\}", text)
missing = [p for p in chapters if not (ROOT / f"{p}.tex").exists()]
if missing:
    print("Missing included files:", ", ".join(missing))
    sys.exit(1)

source_paths = [ROOT / "main.tex", ROOT / "references.bib", ROOT / "README.md"]
source_paths.extend(ROOT.glob("chapters/*.tex"))
source_paths.extend(ROOT.glob("figures/*.tex"))
all_source = "\n".join(p.read_text(encoding="utf-8") for p in source_paths)

for bad in ["turn0search", "turn1search", "TODO", "PLACEHOLDER", "\u2011", "\u2013", "\u2014"]:
    if bad in all_source:
        print(f"Forbidden or unfinished token found: {bad!r}")
        sys.exit(1)

course_framing = re.compile(
    r"(?:undervisningsmateriale|undervisningsstof|\bECTS\b|\bAAU\b|Aalborg|\bMSc\b|\bOER\b|course catalogue|\bkursus\b)",
    re.IGNORECASE,
)
match = course_framing.search(all_source)
if match:
    print(f"Course/programme framing found: {match.group(0)!r}")
    sys.exit(1)

for path in ROOT.glob("chapters/*.tex"):
    value = path.read_text(encoding="utf-8")
    if value.count("\\begin{document}") or value.count("\\end{document}"):
        print(f"Document boundary found inside chapter: {path}")
        sys.exit(1)

pdf = ROOT / "output/pdf/main.pdf"
if pdf.exists():
    result = subprocess.run(["pdfinfo", str(pdf)], text=True, capture_output=True)
    if result.returncode != 0 or "Pages:" not in result.stdout:
        print("Built PDF failed pdfinfo inspection")
        sys.exit(1)

    log = pdf.with_suffix(".log")
    if log.exists():
        log_text = log.read_text(encoding="utf-8", errors="replace")
        layout_error = re.search(r"Overfull \\hbox|Overfull \\vbox|Emergency stop|Fatal error|Undefined control sequence|There were undefined references|Citation .* undefined", log_text)
        if layout_error:
            print(f"PDF build warning/error found: {layout_error.group(0)}")
            sys.exit(1)

print(f"Checked {len(chapters)} included source files and {len(source_paths)} source assets; source tree and PDF are structurally clean.")
