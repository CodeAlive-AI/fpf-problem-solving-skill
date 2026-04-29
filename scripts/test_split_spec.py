#!/usr/bin/env python3
"""Tests for split_spec.py.

Three rules being verified:

A. False H1s from markdown table rows ("# | col |") are filtered out.
B. Empty H1 wrappers (only heading + blank lines) merge with the next H1
   when the next H1's pattern ID matches the wrapper's letter.
C. Misplaced clusters (H1 between two top-level Parts whose pattern ID
   matches the previous Part's letter) become subfolders of that Part.

Plus regression tests that current correct behaviour is preserved.
"""

import io
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import split_spec as splitter


def list_dirs(root: Path) -> list[str]:
    return sorted(p.name for p in root.iterdir() if p.is_dir())


def list_md_files(folder: Path) -> list[str]:
    return sorted(
        p.name for p in folder.iterdir()
        if p.suffix == ".md" and p.name != "_index.md"
    )


class SplitSpecTestCase(unittest.TestCase):
    def run_splitter(self, spec_text: str) -> Path:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        spec = tmp / "FPF-Spec.md"
        out = tmp / "sections"
        spec.write_text(spec_text, encoding="utf-8")
        splitter.SPEC_FILE = spec
        splitter.OUTPUT_DIR = out
        with redirect_stdout(io.StringIO()):
            splitter.split_spec()
        return out


class TestRuleA_FilterFalseH1(SplitSpecTestCase):
    def test_table_row_starting_with_hash_pipe_is_not_a_heading(self):
        spec = (
            "# Real Section\n"
            "\n"
            "Some preamble.\n"
            "\n"
            "# | Block | FPF U.Type | Unified Tech name |\n"
            "  | BCC-1 | BCC-2 | BCC-3 |\n"
            "\n"
            "## H2 Pattern\n"
            "Body.\n"
        )
        out = self.run_splitter(spec)
        dirs = list_dirs(out)
        self.assertEqual(
            len(dirs), 1,
            f"Table row '# | Block ...' must not produce a folder. Got: {dirs}",
        )
        idx = (out / dirs[0] / "_index.md").read_text()
        self.assertIn(
            "| Block | FPF U.Type", idx,
            "Table content should stay in _index.md as preamble",
        )


class TestRuleB_WrapperMerge(SplitSpecTestCase):
    def test_empty_wrapper_followed_by_matching_child_merges(self):
        # Part E is empty wrapper; Section E-I is its only child by pattern ID.
        # Both H1 headings should appear in the merged _index.md, and the
        # H2 children of Section E-I become Part E's subsection files.
        spec = (
            "# Part E - Constitution Cluster\n"
            "\n"
            "# Section E-I - The FPF Constitution\n"
            "\n"
            "Some preamble.\n"
            "\n"
            "## E.1 First Pattern\n"
            "Body of E.1.\n"
            "\n"
            "## E.2 Second Pattern\n"
            "Body of E.2.\n"
        )
        out = self.run_splitter(spec)
        dirs = list_dirs(out)
        self.assertEqual(len(dirs), 1, f"Expected 1 merged folder, got {dirs}")
        idx = (out / dirs[0] / "_index.md").read_text()
        self.assertIn("Part E", idx, "Parent H1 must appear in merged _index.md")
        self.assertIn("Section E-I", idx, "Child H1 must appear in merged _index.md")
        self.assertIn("Some preamble.", idx, "Child preamble must be preserved")
        files = list_md_files(out / dirs[0])
        self.assertEqual(
            len(files), 2,
            f"Expected 2 sub-section files from child's H2s, got {files}",
        )


class TestRuleC_MisplacedClusterNesting(SplitSpecTestCase):
    def test_cluster_with_matching_letter_becomes_subfolder(self):
        # Part A has its own H2s and is followed by Cluster A.IV.A
        # (a misplaced H1 whose pattern ID starts with "A.").
        # Cluster A.IV.A should become a subfolder of Part A,
        # and Part B should remain a separate top-level folder.
        spec = (
            "# Part A - Kernel Architecture\n"
            "\n"
            "## A.1 Holons\n"
            "Body of A.1.\n"
            "\n"
            "## A.2 Roles\n"
            "Body of A.2.\n"
            "\n"
            "# Cluster A.IV.A - Signature Stack\n"
            "\n"
            "## A.6 Signature Stack\n"
            "Body of A.6.\n"
            "\n"
            "## A.6.B Boundary Norm\n"
            "Body of A.6.B.\n"
            "\n"
            "# Part B - Reasoning\n"
            "\n"
            "## B.1 Gamma\n"
            "Body of B.1.\n"
        )
        out = self.run_splitter(spec)
        top = list_dirs(out)
        self.assertEqual(
            len(top), 2,
            f"Expected 2 top-level Parts (A, B); got {top}",
        )

        part_a = next(d for d in top if "part-a" in d)
        part_b = next(d for d in top if "part-b" in d)

        part_a_files = list_md_files(out / part_a)
        self.assertEqual(
            len(part_a_files), 2,
            f"Part A should have 2 direct H2 files, got {part_a_files}",
        )

        part_a_subdirs = list_dirs(out / part_a)
        self.assertEqual(
            len(part_a_subdirs), 1,
            f"Part A should have 1 subfolder for Cluster A.IV.A, got {part_a_subdirs}",
        )
        cluster_dir = out / part_a / part_a_subdirs[0]
        self.assertTrue(
            (cluster_dir / "_index.md").exists(),
            "Cluster subfolder must have its own _index.md",
        )
        cluster_files = list_md_files(cluster_dir)
        self.assertEqual(
            len(cluster_files), 2,
            f"Cluster A.IV.A should have 2 H2 files, got {cluster_files}",
        )

        part_b_files = list_md_files(out / part_b)
        self.assertEqual(
            len(part_b_files), 1,
            f"Part B should have 1 H2 file, got {part_b_files}",
        )


class TestRegression_PreserveCurrentBehaviour(SplitSpecTestCase):
    def test_h1_with_content_does_not_merge_with_next_h1(self):
        # Title page (heading + author + date) followed by another H1 must
        # NOT merge — first H1 has real content beyond the heading line.
        spec = (
            "# Title Page\n"
            "by Author Name.\n"
            "April 2026.\n"
            "Pattern templates explained in E.8.\n"
            "\n"
            "# Real Section\n"
            "\n"
            "## H2 Pattern\n"
            "Body.\n"
        )
        out = self.run_splitter(spec)
        dirs = list_dirs(out)
        self.assertEqual(
            len(dirs), 2,
            f"Title page with content must remain separate, got {dirs}",
        )

    def test_normal_h1_with_h2_children_unchanged(self):
        spec = (
            "# Section A\n"
            "\n"
            "Preamble text.\n"
            "\n"
            "## H2.1 First\n"
            "Body.\n"
            "\n"
            "## H2.2 Second\n"
            "Body.\n"
        )
        out = self.run_splitter(spec)
        dirs = list_dirs(out)
        self.assertEqual(len(dirs), 1)
        self.assertEqual(len(list_md_files(out / dirs[0])), 2)

    def test_h1_with_preamble_no_h2_does_not_merge_with_unrelated_h1(self):
        # Part H pattern: real preamble (overview table), no H2 children,
        # followed by Part I (different letter — not a misplaced cluster).
        # Both should remain separate top-level folders.
        spec = (
            "# Part H - Glossary\n"
            "\n"
            "| Section | Title |\n"
            "| --- | --- |\n"
            "| H.1 | Glossary |\n"
            "\n"
            "# Part I - Annexes\n"
            "\n"
            "## I.2 Walkthrough\n"
            "Body.\n"
        )
        out = self.run_splitter(spec)
        dirs = list_dirs(out)
        self.assertEqual(
            len(dirs), 2,
            f"Part H and Part I are unrelated peers, got {dirs}",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
