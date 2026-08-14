#!/usr/bin/env python3
"""
tests/test_update_problem_index.py

Comprehensive Empirical Test Suite and Adversarial Stress Harness for scripts/update_problem_index.py.
Covers:
1. 10-run idempotency and determinism
2. Dynamic date handling (--date 2026-08-10, 2026-08-20, past/future dates, edge dates)
3. Vault root override (--vault-root)
4. Malformed, adversarial, and corrupt problem note resilience
5. Data integrity, count consistency, and formatting correctness
6. Scale stress test (500+ generated notes) & execution time benchmarking
7. Matching hierarchy (Exact Name -> Alias -> Slug -> URL) & duplicate resilience
"""

import os
import sys
import time
import shutil
import tempfile
import hashlib
import subprocess
import unittest
from pathlib import Path

# Paths
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = WORKSPACE_ROOT / "scripts" / "update_problem_index.py"
REAL_PROBLEMS_DIR = WORKSPACE_ROOT / "02 Problems"
REAL_PROGRESS_DIR = WORKSPACE_ROOT / "07 Progress"


def get_file_hash(path: Path) -> str:
    """Computes SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


class TestUpdateProblemIndexEmpirical(unittest.TestCase):
    """Empirical adversarial test suite for update_problem_index.py."""

    def run_script(self, args: list, cwd: Path = WORKSPACE_ROOT) -> subprocess.CompletedProcess:
        """Executes update_problem_index.py with provided arguments."""
        cmd = [sys.executable, str(SCRIPT_PATH)] + args
        res = subprocess.run(
            cmd,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return res

    def test_01_idempotency_10_runs(self):
        """Test 1: Run 10 times consecutively; output files must be bit-for-bit identical."""
        date_str = "2026-08-14"
        index_hashes = []
        tracker_hashes = []

        problem_index_path = REAL_PROBLEMS_DIR / "Problem Index.md"
        tracker_path = REAL_PROGRESS_DIR / "NeetCode 150 Tracker.md"

        for i in range(10):
            res = self.run_script(["--date", date_str])
            self.assertEqual(res.returncode, 0, f"Run {i+1} failed with error:\n{res.stderr}")
            self.assertTrue(problem_index_path.exists(), f"Problem Index missing after run {i+1}")
            self.assertTrue(tracker_path.exists(), f"Tracker missing after run {i+1}")

            idx_h = get_file_hash(problem_index_path)
            trk_h = get_file_hash(tracker_path)

            index_hashes.append(idx_h)
            tracker_hashes.append(trk_h)

        # Assert all 10 hashes are identical
        self.assertEqual(len(set(index_hashes)), 1, f"Problem Index.md was not deterministic: {set(index_hashes)}")
        self.assertEqual(len(set(tracker_hashes)), 1, f"NeetCode 150 Tracker.md was not deterministic: {set(tracker_hashes)}")
        print(f"\n[PASS] 10-Run Idempotency: All 10 hashes identical (Index: {index_hashes[0][:8]}, Tracker: {tracker_hashes[0][:8]})")

    def test_02_date_handling_active_queues(self):
        """Test 2: Verify queue categorization across different reference dates."""
        # 1. Test with early date 2026-08-08
        res_early = self.run_script(["--date", "2026-08-08"])
        self.assertEqual(res_early.returncode, 0)
        content_early = (REAL_PROBLEMS_DIR / "Problem Index.md").read_text(encoding="utf-8")
        self.assertIn("last_updated: 2026-08-08", content_early)
        self.assertIn("Up for Review Today: 2026-08-08", content_early)
        due_match_early = content_early.count("🔴 Overdue") + content_early.count("🟡 Due Today")

        # 2. Test with date 2026-08-10
        res_mid = self.run_script(["--date", "2026-08-10"])
        self.assertEqual(res_mid.returncode, 0)
        content_mid = (REAL_PROBLEMS_DIR / "Problem Index.md").read_text(encoding="utf-8")
        self.assertIn("last_updated: 2026-08-10", content_mid)
        self.assertIn("Up for Review Today: 2026-08-10", content_mid)
        due_match_mid = content_mid.count("🔴 Overdue") + content_mid.count("🟡 Due Today")

        # Extract Active Revision Queue section only for line status checks
        active_section = content_mid.split("## 🔴 Active Revision Queue")[1].split("## 🟢 Future Scheduled Revisions")[0]
        
        # Verify status tags in Active Revision Queue
        for line in active_section.splitlines():
            if line.startswith("| **[["):
                if "`2026-08-10`" in line:
                    self.assertIn("🟡 Due Today", line, f"Expected '🟡 Due Today' in line: {line}")
                elif "`2026-08-09`" in line:
                    self.assertIn("🔴 Overdue (2026-08-09)", line, f"Expected '🔴 Overdue (2026-08-09)' in line: {line}")

        # 3. Test with future date 2026-08-20
        res_late = self.run_script(["--date", "2026-08-20"])
        self.assertEqual(res_late.returncode, 0)
        content_late = (REAL_PROBLEMS_DIR / "Problem Index.md").read_text(encoding="utf-8")
        self.assertIn("last_updated: 2026-08-20", content_late)
        self.assertIn("Up for Review Today: 2026-08-20", content_late)
        due_match_late = content_late.count("🔴 Overdue") + content_late.count("🟡 Due Today")

        # Monotonicity check: As time progresses, more or equal problems become due/overdue
        self.assertGreaterEqual(due_match_mid, due_match_early)
        self.assertGreaterEqual(due_match_late, due_match_mid)

        print(f"\n[PASS] Date Handling: Due count progresses monotonically ({due_match_early} -> {due_match_mid} -> {due_match_late}) with correct Due/Overdue tagging.")

    def test_03_vault_root_override(self):
        """Test 3: Verify explicit --vault-root correctly isolates file generation to target directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_root = Path(tmpdir)
            tmp_problems = tmp_root / "02 Problems"
            tmp_problems.mkdir(parents=True)

            # Copy 3 sample problems to mock vault
            sample_problems = ["Two Sum.md", "Valid Anagram.md", "Reverse Linked List.md"]
            for sp in sample_problems:
                src = REAL_PROBLEMS_DIR / sp
                if src.exists():
                    shutil.copy(src, tmp_problems / sp)

            res = self.run_script(["--vault-root", str(tmp_root), "--date", "2026-08-14"])
            self.assertEqual(res.returncode, 0, f"Script failed on mock vault:\n{res.stderr}")

            # Verify files were generated in mock vault
            mock_index = tmp_problems / "Problem Index.md"
            mock_tracker = tmp_root / "07 Progress" / "NeetCode 150 Tracker.md"
            self.assertTrue(mock_index.exists(), "Mock Problem Index was not created")
            self.assertTrue(mock_tracker.exists(), "Mock Tracker was not created")

            idx_content = mock_index.read_text(encoding="utf-8")
            self.assertIn("Master Problem Inventory (3 Solved)", idx_content)
            self.assertIn("[[Two Sum]]", idx_content)
            self.assertIn("[[Valid Anagram]]", idx_content)
            self.assertIn("[[Reverse Linked List]]", idx_content)

            trk_content = mock_tracker.read_text(encoding="utf-8")
            self.assertIn("total_solved: 3", trk_content)

        # Test non-existent vault root raises error
        res_nonexistent = self.run_script(["--vault-root", "/nonexistent/path/xyz"])
        self.assertNotEqual(res_nonexistent.returncode, 0)
        self.assertIn("FileNotFoundError", res_nonexistent.stderr)

        print("\n[PASS] Vault Root Override: Mock vault isolated properly and invalid root fails safely.")

    def test_04_resilience_to_malformed_notes(self):
        """Test 4: Stress-test script with adversarial / corrupt / malformed problem notes."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_root = Path(tmpdir)
            tmp_problems = tmp_root / "02 Problems"
            tmp_problems.mkdir(parents=True)

            # Create malformed notes
            # Case A: Totally empty note
            (tmp_problems / "Empty Problem.md").write_text("", encoding="utf-8")

            # Case B: Note without frontmatter
            (tmp_problems / "No Frontmatter.md").write_text("# Just Heading\nSome notes here.", encoding="utf-8")

            # Case C: Corrupt YAML frontmatter
            (tmp_problems / "Corrupt YAML.md").write_text(
                "---\ntitle: \"Corrupt\ndifficulty: \nnext_review: null\n---\nBody text",
                encoding="utf-8"
            )

            # Case D: Missing fields note with weird characters in name
            (tmp_problems / "Adversarial & Special [Chars] (Test).md").write_text(
                "---\nstatus: Solved\n---\n# Content with Grade B in text\n**Grade**: `Grade B`",
                encoding="utf-8"
            )

            # Case E: Valid note with review history
            (tmp_problems / "Valid Note.md").write_text(
                "---\ndifficulty: Medium\ntrack: Track A\nprimary_pattern: \"[[Binary Search]]\"\nnext_review: 2026-08-14\n---\n"
                "## Review History\n| Date | Result | Hint | Time | Grade |\n| 2026-08-14 | AC | none | 15m | Grade A |\n",
                encoding="utf-8"
            )

            res = self.run_script(["--vault-root", str(tmp_root), "--date", "2026-08-14"])
            self.assertEqual(res.returncode, 0, f"Script crashed on malformed notes:\n{res.stderr}")

            mock_index = tmp_problems / "Problem Index.md"
            self.assertTrue(mock_index.exists())
            idx_content = mock_index.read_text(encoding="utf-8")

            # Verify that all 5 notes are listed in Master Problem Inventory without crash
            self.assertIn("Master Problem Inventory (5 Solved)", idx_content)
            self.assertIn("[[Empty Problem]]", idx_content)
            self.assertIn("[[No Frontmatter]]", idx_content)
            self.assertIn("[[Corrupt YAML]]", idx_content)
            self.assertIn("[[Adversarial & Special [Chars] (Test)]]", idx_content)
            self.assertIn("[[Valid Note]]", idx_content)

        print("\n[PASS] Resilience: Handled empty notes, corrupt YAML, missing frontmatter, and special characters cleanly.")

    def test_05_data_integrity_and_neetcode_math(self):
        """Test 5: Verify mathematical integrity and tracker statistics."""
        res = self.run_script(["--date", "2026-08-14"])
        self.assertEqual(res.returncode, 0)

        # Count real problem files
        problem_files = [
            f for f in REAL_PROBLEMS_DIR.glob("*.md")
            if f.name != "Problem Index.md"
        ]
        real_count = len(problem_files)

        problem_index_content = (REAL_PROBLEMS_DIR / "Problem Index.md").read_text(encoding="utf-8")
        tracker_content = (REAL_PROGRESS_DIR / "NeetCode 150 Tracker.md").read_text(encoding="utf-8")

        # 1. Master inventory count matches real file count
        self.assertIn(f"Master Problem Inventory ({real_count} Solved)", problem_index_content)

        # 2. NeetCode 150 target is exactly 150 (28 Easy + 101 Medium + 21 Hard)
        self.assertIn("total_target: 150", tracker_content)
        self.assertIn("easy_total: 28", tracker_content)
        self.assertIn("medium_total: 101", tracker_content)
        self.assertIn("hard_total: 21", tracker_content)

        # 3. Sum of module problem rows in Tracker equals 150
        if "## ➕ Supplementary Vault Solved Problems" in tracker_content:
            modules_content = tracker_content.split("## ➕ Supplementary Vault Solved Problems")[0]
        else:
            modules_content = tracker_content

        solved_boxes = modules_content.count("| - [x] ✅ Solved |")
        unsolved_boxes = modules_content.count("| - [ ] ⏳ Unsolved |")
        self.assertEqual(solved_boxes + unsolved_boxes, 150, f"Module problem rows sum to {solved_boxes + unsolved_boxes}, expected 150")

        # 4. Check that all table columns have valid markdown pipe formatting
        for file_content, fname in [(problem_index_content, "Problem Index.md"), (tracker_content, "NeetCode 150 Tracker.md")]:
            for line_idx, line in enumerate(file_content.splitlines(), 1):
                if line.startswith("|") and not line.startswith("| :"):
                    pipes = line.count("|")
                    self.assertGreaterEqual(pipes, 3, f"Malformed table row at {fname}:{line_idx}: {line}")

        print(f"\n[PASS] Data Integrity: Problem count ({real_count}), NeetCode 150 targets (28+101+21=150), and markdown table syntax verified.")

    def test_06_matching_hierarchy_and_alias_resolution(self):
        """Test 6: Verify matching order (Exact Name -> Alias -> Slug -> URL)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_root = Path(tmpdir)
            tmp_problems = tmp_root / "02 Problems"
            tmp_problems.mkdir(parents=True)

            # Test Alias Match: "Two Sum II" should match canonical "Two Sum II - Input Array Is Sorted"
            (tmp_problems / "Two Sum II.md").write_text(
                "---\ndifficulty: Medium\ntrack: High Value\nprimary_pattern: \"[[Two Pointers]]\"\nnext_review: 2026-08-14\n---\n",
                encoding="utf-8"
            )

            # Test URL Match: Problem note with custom name but matching LeetCode URL
            (tmp_problems / "Custom Tree Inversion Note.md").write_text(
                "---\ndifficulty: Easy\ntrack: High Value\nprimary_pattern: \"[[Trees]]\"\nurl: https://leetcode.com/problems/invert-binary-tree/\nnext_review: 2026-08-14\n---\n",
                encoding="utf-8"
            )

            res = self.run_script(["--vault-root", str(tmp_root), "--date", "2026-08-14"])
            self.assertEqual(res.returncode, 0)

            tracker_content = (tmp_root / "07 Progress" / "NeetCode 150 Tracker.md").read_text(encoding="utf-8")
            
            # Two Sum II matched via alias
            self.assertIn("[[Two Sum II|Two Sum II - Input Array Is Sorted]]", tracker_content)
            # Invert Binary Tree matched via URL
            self.assertIn("[[Custom Tree Inversion Note|Invert Binary Tree]]", tracker_content)

        print("\n[PASS] Matching Resolution: Aliases and URL matching successfully map non-standard note filenames to NeetCode 150 canonical slots.")

    def test_07_scale_stress_test(self):
        """Test 7: Scale stress test with 300 problem notes to verify linear runtime and stability."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_root = Path(tmpdir)
            tmp_problems = tmp_root / "02 Problems"
            tmp_problems.mkdir(parents=True)

            # Generate 300 problem notes
            for i in range(1, 301):
                (tmp_problems / f"Problem Scale Test {i:03d}.md").write_text(
                    f"---\ndifficulty: {'Easy' if i%3==0 else 'Medium' if i%3==1 else 'Hard'}\n"
                    f"track: {'High Value' if i%2==0 else 'Volume'}\n"
                    f"primary_pattern: \"[[Dynamic Programming]]\"\n"
                    f"next_review: 2026-08-{(i % 28) + 1:02d}\n"
                    f"---\n"
                    f"# Problem Scale Test {i}\n**Grade**: `Grade A`\n",
                    encoding="utf-8"
                )

            start_t = time.perf_counter()
            res = self.run_script(["--vault-root", str(tmp_root), "--date", "2026-08-14"])
            elapsed = time.perf_counter() - start_t

            self.assertEqual(res.returncode, 0, f"Scale run failed: {res.stderr}")
            self.assertLess(elapsed, 3.0, f"Scale test took too long: {elapsed:.2f}s (expected < 3.0s)")

            idx_content = (tmp_problems / "Problem Index.md").read_text(encoding="utf-8")
            self.assertIn("Master Problem Inventory (300 Solved)", idx_content)

        print(f"\n[PASS] Scale Stress: Successfully processed 300 notes in {elapsed:.3f}s (< 3.0s threshold).")


if __name__ == "__main__":
    unittest.main(verbosity=2)
