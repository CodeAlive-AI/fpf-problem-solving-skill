#!/usr/bin/env python3
"""Split FPF-Spec.md into a hierarchical structure by # and ## headings.

Three structural rules are applied beyond raw heading splits:

A. False H1s from markdown table rows (`# | col |`) are skipped.
B. Empty H1 wrappers (heading + blank lines, immediately followed by another H1)
   merge with the next H1 — both headings appear in the merged _index.md, and
   the folder takes the wrapper's title (canonical Part name).
C. Misplaced clusters (H1 between two top-level Parts whose pattern ID matches
   the previous Part's letter, e.g., `Cluster A.IV.A` between Part A and Part B)
   become subfolders of that Part.

Output:
  sections/
    01-title-page/
      _index.md
    04-part-a-kernel-architecture-cluster/
      _index.md
      01-a-0-onboarding.md
      ...
      cluster-a-iv-a-signature-stack/
        _index.md
        01-a-6-signature-stack.md
        ...
"""

import re
import shutil
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SPEC_FILE = PROJECT_ROOT / "FPF" / "FPF-Spec.md"
OUTPUT_DIR = PROJECT_ROOT / "sections"

HEADING_RE = re.compile(r"^(#{1,2})\s+(?!\|)")
PART_LETTER_RE = re.compile(r"\bPart\s+([A-Z])\b")
CLUSTER_PATTERN_RE = re.compile(r"\b([A-Z])\.[IVX0-9]")


def to_slug(text: str, max_len: int = 70) -> str:
    clean = re.sub(r"[*`]", "", text)
    clean = re.sub(r"\(.*?\)", "", clean)
    clean = re.sub(r"[^a-zA-Z0-9\s-]", " ", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean.lower().replace(" ", "-")[:max_len].rstrip("-")


def heading_to_dirname(index: int, heading: str) -> str:
    heading = heading.lstrip("# ").strip()
    return f"{index:02d}-{to_slug(heading)}"


def heading_to_filename(index: int, heading: str) -> str:
    heading = heading.lstrip("# ").strip()
    return f"{index:02d}-{to_slug(heading, 60)}.md"


def first_sentence(lines_block: list[str], max_chars: int = 200) -> str:
    for line in lines_block:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("|") or stripped.startswith("---"):
            continue
        desc = re.sub(r"[*`>]", "", stripped).strip()
        if len(desc) > 20:
            if len(desc) > max_chars:
                desc = desc[:max_chars].rsplit(" ", 1)[0] + "..."
            return desc
    return ""


def build_toc(h2_entries: list[tuple], sub_clusters: list[tuple] | None = None) -> str:
    toc_lines = []
    if sub_clusters:
        toc_lines += ["", "## Sub-clusters", ""]
        for subdir, title, sub_count, desc in sub_clusters:
            clean_title = re.sub(r"[*`]", "", title.lstrip("# ").strip())
            summary = f" — {desc}" if desc else ""
            toc_lines.append(
                f"- [{clean_title}]({subdir}/_index.md) ({sub_count} sub-sections){summary}"
            )
    toc_lines += ["", "## Contents", ""]
    for filename, title, line_count, desc in h2_entries:
        clean_title = re.sub(r"[*`]", "", title.lstrip("# ").strip())
        summary = f" — {desc}" if desc else ""
        toc_lines.append(f"- [{clean_title}]({filename}) ({line_count} lines){summary}")
    toc_lines.append("")
    return "\n".join(toc_lines)


def collect_headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """Rule A: collect H1/H2 headings, skipping false H1s from table rows."""
    headings = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if m:
            headings.append((i, len(m.group(1)), line.rstrip("\n")))
    return headings


def is_empty_wrapper(h_idx: int, headings: list, lines: list[str]) -> bool:
    """An H1 is an empty wrapper if its block contains only blank lines
    and it is immediately followed by another H1."""
    line_num, level, _ = headings[h_idx]
    if level != 1 or h_idx + 1 >= len(headings):
        return False
    next_line, next_level, _ = headings[h_idx + 1]
    if next_level != 1:
        return False
    return all(not line.strip() for line in lines[line_num + 1 : next_line])


def fold_wrappers(headings: list, lines: list[str]) -> list:
    """Rule B: empty H1 wrappers fold into the next H1.
    The wrapper's title is kept (canonical Part name) and its line number
    becomes the merged section's effective start, so the wrapper heading
    appears in the resulting preamble."""
    folded = []
    pending_start = None
    pending_title = None
    for idx, (line_num, level, title) in enumerate(headings):
        if is_empty_wrapper(idx, headings, lines):
            if pending_start is None:
                pending_start = line_num
                pending_title = title
            continue
        if level == 1 and pending_start is not None:
            folded.append((pending_start, level, pending_title))
            pending_start = None
            pending_title = None
        else:
            folded.append((line_num, level, title))
    return folded


def build_h1_sections(headings: list, lines: list[str]) -> list:
    h1_sections = []
    current_h1 = None
    current_h2s = []
    for idx, (line_num, level, title) in enumerate(headings):
        next_line = headings[idx + 1][0] if idx + 1 < len(headings) else len(lines)
        block = lines[line_num:next_line]
        if level == 1:
            if current_h1 is not None:
                h1_sections.append((current_h1, current_h2s))
            current_h1 = (line_num, title, block)
            current_h2s = []
        else:
            current_h2s.append((line_num, title, block))
    if current_h1 is not None:
        h1_sections.append((current_h1, current_h2s))
    return h1_sections


def extract_part_letter(title: str) -> str | None:
    m = PART_LETTER_RE.search(title)
    return m.group(1) if m else None


def extract_cluster_letter(title: str) -> str | None:
    m = CLUSTER_PATTERN_RE.search(title)
    return m.group(1) if m else None


def classify_for_nesting(h1_sections: list) -> list:
    """Rule C: misplaced clusters become children of the previous Part.
    Returns list of (h1_info, h2s, sub_clusters) where sub_clusters is a
    list of (h1_info, h2s) for clusters nested under this Part."""
    result = []
    current_part_idx = None
    current_part_letter = None
    for h1_info, h2s in h1_sections:
        _, title, _ = h1_info
        part_letter = extract_part_letter(title)
        if part_letter:
            result.append((h1_info, h2s, []))
            current_part_idx = len(result) - 1
            current_part_letter = part_letter
        else:
            cluster_letter = extract_cluster_letter(title)
            if cluster_letter and cluster_letter == current_part_letter and current_part_idx is not None:
                result[current_part_idx][2].append((h1_info, h2s))
            else:
                result.append((h1_info, h2s, []))
                current_part_idx = None
                current_part_letter = None
    return result


def write_section(dir_path: Path, h1_info: tuple, h2s: list, sub_clusters: list, lines: list[str]) -> tuple[int, int]:
    """Write a section folder: H2 files + nested cluster subdirs + _index.md.
    Returns (dir_count, file_count) for reporting."""
    h1_line, h1_title, h1_block = h1_info

    sub_cluster_entries = []
    extra_dirs = 0
    extra_files = 0
    for sc_h1_info, sc_h2s in sub_clusters:
        sc_h1_line, sc_h1_title, sc_h1_block = sc_h1_info
        sc_slug = to_slug(sc_h1_title.lstrip("# ").strip())
        sc_dir = dir_path / sc_slug
        sc_dir.mkdir(parents=True, exist_ok=True)
        sc_dirs, sc_files = write_section(sc_dir, sc_h1_info, sc_h2s, [], lines)
        extra_dirs += 1 + sc_dirs
        extra_files += sc_files
        desc = first_sentence(sc_h1_block[1:])
        sub_cluster_entries.append((sc_slug, sc_h1_title, len(sc_h2s), desc))

    if not h2s:
        content = "".join(h1_block)
        if sub_cluster_entries:
            content += build_toc([], sub_cluster_entries)
        (dir_path / "_index.md").write_text(content, encoding="utf-8")
        return extra_dirs, extra_files + 1

    first_h2_line = h2s[0][0]
    preamble = lines[h1_line:first_h2_line]

    h2_entries = []
    for h2_idx, (h2_line, h2_title, h2_block) in enumerate(h2s, 1):
        filename = heading_to_filename(h2_idx, h2_title)
        (dir_path / filename).write_text("".join(h2_block), encoding="utf-8")
        desc = first_sentence(h2_block[1:])
        h2_entries.append((filename, h2_title, len(h2_block), desc))

    index_content = "".join(preamble) + build_toc(h2_entries, sub_cluster_entries)
    (dir_path / "_index.md").write_text(index_content, encoding="utf-8")
    return extra_dirs, extra_files + len(h2s) + 1


def split_spec():
    if not SPEC_FILE.exists():
        print(f"Error: {SPEC_FILE} not found. Did you init the submodule?", file=sys.stderr)
        sys.exit(1)

    lines = SPEC_FILE.read_text(encoding="utf-8").splitlines(keepends=True)

    headings = collect_headings(lines)
    headings = fold_wrappers(headings, lines)
    h1_sections = build_h1_sections(headings, lines)
    classified = classify_for_nesting(h1_sections)

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    total_dirs = 0
    total_files = 0
    for h1_idx, (h1_info, h2s, sub_clusters) in enumerate(classified, 1):
        _, h1_title, _ = h1_info
        dirname = heading_to_dirname(h1_idx, h1_title)
        dir_path = OUTPUT_DIR / dirname
        dir_path.mkdir(parents=True, exist_ok=True)
        sc_dirs, files_written = write_section(dir_path, h1_info, h2s, sub_clusters, lines)
        sc_label = f" + {len(sub_clusters)} sub-cluster(s)" if sub_clusters else ""
        print(f"  {dirname}/ ({len(h2s)} sub-sections{sc_label})")
        total_dirs += 1 + sc_dirs
        total_files += files_written

    print(f"\nWrote {total_dirs} directories, {total_files} files to {OUTPUT_DIR}/")


if __name__ == "__main__":
    split_spec()
