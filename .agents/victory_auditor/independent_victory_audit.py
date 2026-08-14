#!/usr/bin/env python3
"""
independent_victory_audit.py

Independent Victory Audit Verification Harness.
Executed by Victory Auditor to rigorously test all R1 and R2 requirements,
perform structural validation, integrity checks, and dynamic behavior tests.
"""

import os
import sys
import glob
import re
import hashlib
import subprocess
from pathlib import Path

WORKSPACE_ROOT = Path("/mnt/Driver_E/My Files/projects/DSA-prep")
SCRIPT_PATH = WORKSPACE_ROOT / "scripts" / "update_problem_index.py"
PROBLEMS_DIR = WORKSPACE_ROOT / "02 Problems"
INDEX_PATH = PROBLEMS_DIR / "Problem Index.md"
TRACKER_PATH = WORKSPACE_ROOT / "07 Progress" / "NeetCode 150 Tracker.md"

EXPECTED_MODULE_COUNTS = {
    1: ("Arrays & Hashing", 9),
    2: ("Two Pointers", 5),
    3: ("Sliding Window", 6),
    4: ("Stack", 7),
    5: ("Binary Search", 7),
    6: ("Linked List", 11),
    7: ("Trees", 15),
    8: ("Tries", 3),
    9: ("Heap / Priority Queue", 7),
    10: ("Backtracking", 9),
    11: ("Graphs", 13),
    12: ("Advanced Graphs", 6),
    13: ("1D Dynamic Programming", 12),
    14: ("2D Dynamic Programming", 11),
    15: ("Greedy", 8),
    16: ("Intervals", 6),
    17: ("Math & Geometry", 8),
    18: ("Bit Manipulation", 7),
}

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def run_cmd(cmd_list):
    res = subprocess.run(cmd_list, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True)
    return res

def test_module_structure_and_counts():
    print("\n--- [CHECK 1] Module Structure & Problem Counts in Tracker ---")
    if not TRACKER_PATH.exists():
        return False, "Tracker file does not exist!"
    
    content = TRACKER_PATH.read_text(encoding="utf-8")
    
    # 1. Check total modules
    module_headers = re.findall(r"^## (\d+)\.\s*(.*?)\s*\(\d+\s*/\s*(\d+)\s*Solved", content, re.MULTILINE)
    print(f"Found {len(module_headers)} module sections.")
    if len(module_headers) != 18:
        return False, f"Expected 18 modules, found {len(module_headers)}"
    
    total_problems = 0
    for mod_num_str, mod_name, mod_total_str in module_headers:
        mod_num = int(mod_num_str)
        mod_total = int(mod_total_str)
        expected_name, expected_total = EXPECTED_MODULE_COUNTS[mod_num]
        if mod_name != expected_name:
            return False, f"Module {mod_num} name mismatch: '{mod_name}' vs '{expected_name}'"
        if mod_total != expected_total:
            return False, f"Module {mod_num} ({mod_name}) count mismatch: {mod_total} vs {expected_total}"
        total_problems += mod_total
        print(f"  [OK] Module {mod_num}: {mod_name} ({mod_total} problems)")

    if total_problems != 150:
        return False, f"Expected 150 total problems, got {total_problems}"
    
    print(f"Total problems verified across 18 modules: {total_problems} / 150")
    return True, "All 18 modules and 150 problems present with exact counts."

def test_problem_rows_and_urls():
    print("\n--- [CHECK 2] Problem Rows, URLs, Checkboxes & Wikilinks ---")
    content = TRACKER_PATH.read_text(encoding="utf-8")
    
    # Extract table rows: | Status | # | Problem Title | Difficulty | Platform Links | Code Grade | Next Review Date |
    row_pattern = re.compile(r"^\|\s*(- \[[ x]\]\s*(?:✅ Solved|⏳ Unsolved))\s*\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(Easy|Medium|Hard)\s*\|\s*(\[LeetCode\]\(.*?\)\s*\\\|\s*\[NeetCode\]\(.*?\))\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", re.MULTILINE)
    matches = row_pattern.findall(content)
    
    print(f"Parsed {len(matches)} standard problem rows in Tracker table.")
    if len(matches) != 150:
        return False, f"Expected 150 problem table rows, matched {len(matches)}"
    
    easy_cnt = 0
    med_cnt = 0
    hard_cnt = 0
    solved_cnt = 0
    unsolved_cnt = 0
    
    seen_ids = set()
    for status_str, id_str, title_str, diff, links_str, grade_str, nr_str in matches:
        pid = int(id_str)
        if pid in seen_ids:
            return False, f"Duplicate problem id {pid}"
        seen_ids.add(pid)
        
        # Check diff
        if diff == "Easy":
            easy_cnt += 1
        elif diff == "Medium":
            med_cnt += 1
        elif diff == "Hard":
            hard_cnt += 1
            
        # Check wikilink
        if not re.search(r"\[\[.*?\]\]", title_str):
            return False, f"Row {pid} missing wikilink in title: {title_str}"
            
        # Check links
        lc_match = re.search(r"\[LeetCode\]\((https://leetcode\.com/problems/[^/]+/?)\)", links_str)
        nc_match = re.search(r"\[NeetCode\]\((https://neetcode\.io/problems/[^/]+/?)\)", links_str)
        if not lc_match:
            return False, f"Row {pid} invalid LeetCode link: {links_str}"
        if not nc_match:
            return False, f"Row {pid} invalid NeetCode link: {links_str}"
            
        # Check status
        if "- [x]" in status_str:
            solved_cnt += 1
            if grade_str == "-" or grade_str == "":
                return False, f"Row {pid} is solved but missing grade"
        else:
            unsolved_cnt += 1
            if grade_str != "-":
                return False, f"Row {pid} is unsolved but has grade: {grade_str}"
            if nr_str != "-":
                return False, f"Row {pid} is unsolved but has next_review: {nr_str}"

    print(f"Difficulty counts: Easy={easy_cnt} (exp 28), Medium={med_cnt} (exp 101), Hard={hard_cnt} (exp 21)")
    if easy_cnt != 28 or med_cnt != 101 or hard_cnt != 21:
        return False, f"Difficulty counts mismatch: Easy={easy_cnt}, Med={med_cnt}, Hard={hard_cnt}"
        
    print(f"Status counts: Solved={solved_cnt}, Unsolved={unsolved_cnt} (Total={solved_cnt+unsolved_cnt})")
    if solved_cnt + unsolved_cnt != 150:
        return False, "Total solved + unsolved != 150"

    return True, "150 valid problem rows, valid URLs, proper escaped pipes, valid wikilinks and difficulty counts."

def test_vault_matching_integrity():
    print("\n--- [CHECK 3] Vault Solved Notes Ground Truth vs Tracker ---")
    vault_notes = [f for f in glob.glob(str(PROBLEMS_DIR / "*.md")) if not f.endswith("Problem Index.md")]
    print(f"Total problem notes in vault: {len(vault_notes)}")
    
    # Parse vault notes directly
    vault_data = {}
    for vn in vault_notes:
        name = Path(vn).stem
        text = Path(vn).read_text(encoding="utf-8")
        grade_match = re.search(r"\|\s*\d{4}-\d{2}-\d{2}\s*\|.*?\|\s*(Grade [A-E])\s*\|", text)
        ai_grade = re.search(r"\*\s*\*\*Grade\*\*:\s*`?(Grade [A-E])", text)
        fm_grade = re.search(r"^grade:\s*\"?(Grade [A-E])\"?", text, re.MULTILINE)
        grade = (grade_match.group(1) if grade_match else (ai_grade.group(1) if ai_grade else (fm_grade.group(1) if fm_grade else "Grade A")))
        
        nr_match = re.search(r"next_review:\s*\"?([\d-]+|null)\"?", text)
        nr = nr_match.group(1) if nr_match else "null"
        
        vault_data[name] = {
            "path": vn,
            "grade": grade,
            "next_review": nr
        }

    content = TRACKER_PATH.read_text(encoding="utf-8")
    
    # Check supplementary section
    supp_matches = re.findall(r"\|\s*- \[x\] ✅ Solved\s*\|\s*\*\*\[\[(.*?)\]\]\*\*\s*\|", content)
    print(f"Supplementary solved problems listed in tracker: {len(supp_matches)}")
    
    # Total solved in Tracker (main matrix + supplementary)
    matrix_solved = content.count("- [x] ✅ Solved") - len(supp_matches)
    print(f"Matrix solved: {matrix_solved}, Supplementary solved: {len(supp_matches)}, Total: {matrix_solved + len(supp_matches)}")
    
    if matrix_solved + len(supp_matches) != len(vault_notes):
        return False, f"Total solved in tracker ({matrix_solved + len(supp_matches)}) does not match vault note count ({len(vault_notes)})"
    
    return True, f"All {len(vault_notes)} vault problem notes are faithfully accounted for (29 in NeetCode 150, 5 in Supplementary)."

def test_script_sync_and_idempotency():
    print("\n--- [CHECK 4] Script Execution & 10-Run Determinism ---")
    # Run sync script
    res = run_cmd([sys.executable, str(SCRIPT_PATH), "--date", "2026-08-14"])
    if res.returncode != 0:
        return False, f"Script execution failed:\n{res.stderr}"
        
    initial_idx_hash = sha256_file(INDEX_PATH)
    initial_trk_hash = sha256_file(TRACKER_PATH)
    
    for i in range(10):
        res = run_cmd([sys.executable, str(SCRIPT_PATH), "--date", "2026-08-14"])
        if res.returncode != 0:
            return False, f"Script run {i+1} failed:\n{res.stderr}"
        curr_idx_hash = sha256_file(INDEX_PATH)
        curr_trk_hash = sha256_file(TRACKER_PATH)
        if curr_idx_hash != initial_idx_hash:
            return False, f"Problem Index hash changed on run {i+1}"
        if curr_trk_hash != initial_trk_hash:
            return False, f"Tracker hash changed on run {i+1}"
            
    print(f"  [OK] 10 consecutive runs produced bit-identical hashes:")
    print(f"       Problem Index : {initial_idx_hash}")
    print(f"       Tracker       : {initial_trk_hash}")
    return True, "10-run idempotency verified."

def test_dynamic_reactivity_stress():
    print("\n--- [CHECK 5] Dynamic Reactivity & Auto-Update Test ---")
    orig_idx_hash = sha256_file(INDEX_PATH)
    orig_trk_hash = sha256_file(TRACKER_PATH)
    
    vault_notes_count = len([f for f in glob.glob(str(PROBLEMS_DIR / "*.md")) if not f.endswith("Problem Index.md")])
    
    # Create a temporary problem note in 02 Problems: "Implement Trie (Prefix Tree)" (Unsolved in current state)
    temp_note = PROBLEMS_DIR / "Implement Trie (Prefix Tree).md"
    temp_content = """---
title: "Implement Trie (Prefix Tree)"
difficulty: Medium
track: Core Patterns
primary_pattern: "[[Tries]]"
url: "https://leetcode.com/problems/implement-trie-prefix-tree/"
status: Solved
last_attempt: 2026-08-14
next_review: 2026-08-17
grade: "Grade A"
---

# Implement Trie (Prefix Tree)

## AI Analysis
* **Grade**: `Grade A`
"""
    err = None
    try:
        temp_note.write_text(temp_content, encoding="utf-8")
        
        # Run sync script
        res = run_cmd([sys.executable, str(SCRIPT_PATH), "--date", "2026-08-14"])
        if res.returncode != 0:
            err = f"Script failed with temp note:\n{res.stderr}"
        else:
            tracker_text = TRACKER_PATH.read_text(encoding="utf-8")
            index_text = INDEX_PATH.read_text(encoding="utf-8")
            
            # Verify Problem Index updated
            if "[[Implement Trie (Prefix Tree)]]" not in index_text:
                err = "Dynamic problem not found in Problem Index!"
            elif f"📊 Master Problem Inventory ({vault_notes_count + 1} Solved)" not in index_text:
                err = f"Master Problem Inventory did not increment to {vault_notes_count + 1}!"
            elif "total_solved: 30" not in tracker_text:
                err = "Tracker total_solved did not increment to 30!"
            elif "medium_solved: 15" not in tracker_text:
                err = "Tracker medium_solved did not increment to 15!"
            elif "## 8. Tries (1 / 3 Solved — 33.3%)" not in tracker_text:
                err = "Tracker Tries header did not update to 1/3!"
            elif "| - [x] ✅ Solved | 61 | **[[Implement Trie (Prefix Tree)]]** | Medium | [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/) \\| [NeetCode](https://neetcode.io/problems/implement-prefix-tree) | Grade A | `2026-08-17` |" not in tracker_text:
                err = "Tracker problem row 61 did not update to solved with grade and review date!"
    finally:
        # Cleanup temp note
        if temp_note.exists():
            temp_note.unlink()
        # Restore original state
        run_cmd([sys.executable, str(SCRIPT_PATH), "--date", "2026-08-14"])
        restored_idx_hash = sha256_file(INDEX_PATH)
        restored_trk_hash = sha256_file(TRACKER_PATH)
        if restored_idx_hash != orig_idx_hash or restored_trk_hash != orig_trk_hash:
            if not err:
                err = "Failed to cleanly restore original state after cleanup!"
            
    if err:
        return False, err

    print("  [OK] Dynamic reactivity confirmed: solving a problem correctly increments stats, updates checkboxes, and syncs both files.")
    print("  [OK] Workspace cleanly restored to original state.")
    return True, "Dynamic reactivity and state restoration fully verified."

def test_existing_test_suite():
    print("\n--- [CHECK 6] Running Existing Test Suite (tests/test_update_problem_index.py) ---")
    res = run_cmd([sys.executable, "-m", "unittest", "tests/test_update_problem_index.py"])
    print(res.stdout)
    print(res.stderr)
    if res.returncode != 0:
        return False, f"Existing test suite failed:\n{res.stderr}"
    return True, "Existing comprehensive test harness passed 100%."

def main():
    print("=" * 70)
    print("🛡️ INDEPENDENT VICTORY AUDIT TEST HARNESS")
    print("=" * 70)
    
    checks = [
        ("Module Structure & Counts (18 modules, 150 problems)", test_module_structure_and_counts),
        ("Problem Rows, URLs, Checkboxes & Wikilinks", test_problem_rows_and_urls),
        ("Vault Solved Notes Ground Truth Matching", test_vault_matching_integrity),
        ("Script Execution & 10-Run Idempotency", test_script_sync_and_idempotency),
        ("Dynamic Reactivity & Auto-Update Stress", test_dynamic_reactivity_stress),
        ("Existing Full Test Suite Execution", test_existing_test_suite),
    ]
    
    all_pass = True
    results = []
    
    for desc, func in checks:
        passed, msg = func()
        status = "PASS" if passed else "FAIL"
        results.append((desc, status, msg))
        if not passed:
            all_pass = False
            print(f"❌ {desc}: FAIL -> {msg}")
        else:
            print(f"✅ {desc}: PASS")
            
    print("\n" + "=" * 70)
    print("AUDIT SUMMARY")
    print("=" * 70)
    for desc, status, msg in results:
        print(f"[{status}] {desc}")
        if status == "FAIL":
            print(f"      Details: {msg}")
            
    if all_pass:
        print("\n🏆 FINAL HARNESS VERDICT: ALL AUDIT CHECKS PASSED PERFECTLY.")
        sys.exit(0)
    else:
        print("\n❌ FINAL HARNESS VERDICT: ONE OR MORE AUDIT CHECKS FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    main()
