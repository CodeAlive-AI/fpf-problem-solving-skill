#!/usr/bin/env python3
"""Split FPF-Spec.md into separate files by top-level (#) headings."""

import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SPEC_FILE = PROJECT_ROOT / "FPF" / "FPF-Spec.md"
OUTPUT_DIR = PROJECT_ROOT / "sections"


def heading_to_filename(index: int, heading: str) -> str:
    """Convert a heading line into a clean filename like '01-part-a-kernel-architecture-cluster.md'."""
    # Remove markdown formatting: **, *, backticks
    clean = heading.lstrip("# ").strip()
    clean = re.sub(r"[*`]", "", clean)
    # Remove content inside parentheses
    clean = re.sub(r"\(.*?\)", "", clean)
    # Replace special chars with spaces, collapse whitespace
    clean = re.sub(r"[^a-zA-Z0-9\s-]", " ", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    # Convert to kebab-case, truncate
    slug = clean.lower().replace(" ", "-")[:80].rstrip("-")
    return f"{index:02d}-{slug}.md"


def split_spec():
    if not SPEC_FILE.exists():
        print(f"Error: {SPEC_FILE} not found. Did you init the submodule?", file=sys.stderr)
        sys.exit(1)

    lines = SPEC_FILE.read_text(encoding="utf-8").splitlines(keepends=True)

    # Find all top-level heading positions (lines starting with exactly '# ')
    heading_positions = []
    for i, line in enumerate(lines):
        if re.match(r"^# ", line):
            heading_positions.append(i)

    print(f"Found {len(heading_positions)} top-level sections")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    files_created = []
    for idx, start in enumerate(heading_positions):
        end = heading_positions[idx + 1] if idx + 1 < len(heading_positions) else len(lines)
        heading_text = lines[start].rstrip("\n")
        filename = heading_to_filename(idx + 1, heading_text)
        content = "".join(lines[start:end])
        out_path = OUTPUT_DIR / filename
        out_path.write_text(content, encoding="utf-8")
        line_count = end - start
        files_created.append((filename, line_count, heading_text))
        print(f"  {filename} ({line_count} lines)")

    print(f"\nWrote {len(files_created)} files to {OUTPUT_DIR}")
    return files_created


if __name__ == "__main__":
    split_spec()
