#!/usr/bin/env python3
"""
Forensic Audit Verification Suite for Milestone 4.1
Tests every aspect of:
1. scripts/update_problem_index.py
2. 07 Progress/NeetCode 150 Tracker.md
3. 02 Problems/Problem Index.md
"""

import os
import sys
import re
import glob
import json
import shutil
import tempfile
import subprocess
from datetime import datetime

VAULT_ROOT = "/mnt/Driver_E/My Files/projects/DSA-prep"
SCRIPTS_DIR = os.path.join(VAULT_ROOT, "scripts")
PROBLEMS_DIR = os.path.join(VAULT_ROOT, "02 Problems")
PATTERNS_DIR = os.path.join(VAULT_ROOT, "03 Patterns")
PROGRESS_DIR = os.path.join(VAULT_ROOT, "07 Progress")
TRACKER_PATH = os.path.join(PROGRESS_DIR, "NeetCode 150 Tracker.md")
INDEX_PATH = os.path.join(PROBLEMS_DIR, "Problem Index.md")
SCRIPT_PATH = os.path.join(SCRIPTS_DIR, "update_problem_index.py")

audit_results = {
    "total_tests": 0,
    "passed_tests": 0,
    "failed_tests": 0,
    "failures": [],
    "details": []
}

def log_test(name: str, passed: bool, message: str = ""):
    audit_results["total_tests"] += 1
    if passed:
        audit_results["passed_tests"] += 1
        audit_results["details"].append(f"[PASS] {name}: {message}")
        print(f"  ✅ [PASS] {name}")
    else:
        audit_results["failed_tests"] += 1
        audit_results["failures"].append(f"[FAIL] {name}: {message}")
        audit_results["details"].append(f"[FAIL] {name}: {message}")
        print(f"  ❌ [FAIL] {name}: {message}")

print("=" * 70)
print("🔍 STARTING FORENSIC INTEGRITY AUDIT (Milestone 4.1)")
print("=" * 70)

# ==============================================================================
# SECTION 1: SOURCE CODE AUDIT (scripts/update_problem_index.py)
# ==============================================================================
print("\n--- Phase 1: Source Code Static Analysis of update_problem_index.py ---")

with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    script_source = f.read()

# Check 1.1: Dynamic Scanning (No hardcoded solved lists)
has_glob_scan = "glob.glob(" in script_source and "02 Problems" in script_source
log_test("1.1 Dynamic Filesystem Scanning", has_glob_scan, "Script dynamically scans 02 Problems directory with glob")

# Check 1.2: Real parsing function
has_real_parser = "def parse_problem_note(" in script_source and "open(file_path" in script_source
log_test("1.2 Dynamic Note Parsing", has_real_parser, "Script opens and parses individual problem markdown notes")

# Check 1.3: Grade extraction logic
has_grade_extractor = "def extract_grade(" in script_source and "rev_rows" in script_source
log_test("1.3 Multi-Tier Grade Extraction", has_grade_extractor, "Script implements multi-tier priority grade extraction")

# Check 1.4: No mock pass shortcuts or dummy implementations
no_fake_pass = not re.search(r"def\s+\w+\(.*?\):\s*return\s+(?:True|False|None|\"Grade A\")\s*$", script_source, re.MULTILINE)
no_not_implemented = "NotImplementedError" not in script_source
log_test("1.4 No Dummy/Facade Logic", no_fake_pass and no_not_implemented, "No mock shortcuts or NotImplementedError found")

# ==============================================================================
# SECTION 2: CANONICAL NEETCODE 150 DATASET INTEGRITY
# ==============================================================================
print("\n--- Phase 2: Canonical NeetCode 150 Dataset Integrity ---")

sys.path.insert(0, SCRIPTS_DIR)
from update_problem_index import NEETCODE_150

# Check 2.1: Exactly 18 modules
log_test("2.1 Module Count", len(NEETCODE_150) == 18, f"Found {len(NEETCODE_150)} modules (expected 18)")

# Check 2.2: Total problems = 150
total_problems_in_dataset = sum(len(m["problems"]) for m in NEETCODE_150)
log_test("2.2 Total Problem Count", total_problems_in_dataset == 150, f"Found {total_problems_in_dataset} problems (expected 150)")

# Check 2.3: Module-by-module breakdown
expected_module_counts = {
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
    18: ("Bit Manipulation", 7)
}

module_counts_match = True
for mod in NEETCODE_150:
    mid = mod["module_id"]
    mname = mod["name"]
    pcount = len(mod["problems"])
    exp_name, exp_count = expected_module_counts.get(mid, ("Unknown", -1))
    if mname != exp_name or pcount != exp_count:
        module_counts_match = False
        log_test(f"2.3 Module {mid} ({mname})", False, f"Expected '{exp_name}' with {exp_count} probs, got '{mname}' with {pcount} probs")
log_test("2.3 Module Category & Count Breakdown", module_counts_match, "All 18 modules have correct canonical names and problem counts")

# Check 2.4: Difficulty distribution: 28 Easy, 101 Medium, 21 Hard
diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0}
all_ids = []
all_names = set()
valid_urls = True
for mod in NEETCODE_150:
    for p in mod["problems"]:
        diff_counts[p["diff"]] = diff_counts.get(p["diff"], 0) + 1
        all_ids.append(p["id"])
        all_names.add(p["name"])
        if not p["lc"].startswith("https://leetcode.com/problems/"):
            valid_urls = False
        if not p["nc"].startswith("https://neetcode.io/problems/"):
            valid_urls = False

log_test("2.4 Difficulty Counts (28E / 101M / 21H)",
         diff_counts == {"Easy": 28, "Medium": 101, "Hard": 21},
         f"Easy: {diff_counts.get('Easy')}, Medium: {diff_counts.get('Medium')}, Hard: {diff_counts.get('Hard')}")

# Check 2.5: IDs sequential 1 to 150
ids_sequential = all_ids == list(range(1, 151))
log_test("2.5 Problem IDs Sequential 1..150", ids_sequential, "IDs are strictly 1..150 without duplicates or gaps")

# Check 2.6: Authentic URLs
log_test("2.6 Canonical URL Verification", valid_urls, "All 150 problems have valid LeetCode and NeetCode canonical URLs")

# ==============================================================================
# SECTION 3: GROUND TRUTH PARSING & DATA CONSISTENCY
# ==============================================================================
print("\n--- Phase 3: Ground Truth Vault Data Cross-Verification ---")

# Directly parse all 34 problem notes on disk
raw_files = [f for f in glob.glob(os.path.join(PROBLEMS_DIR, "*.md")) if not f.endswith("Problem Index.md")]
ground_truth_map = {}

for fpath in raw_files:
    fname = os.path.splitext(os.path.basename(fpath))[0]
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    
    # Ground truth extraction
    nr = re.search(r"next_review:\s*\"?([\d-]+|null)\"?", c)
    la = re.search(r"last_attempt:\s*\"?([\d-]+|null)\"?", c)
    diff = re.search(r"difficulty:\s*\"?(\w+)\"?", c)
    track = re.search(r"track:\s*\"?(.*?)\"?\n", c)
    pat = re.search(r"primary_pattern:\s*\"?\[\[(.*?)\]\]\"?", c)
    url = re.search(r"url:\s*\"?(.*?)\"?\n", c)
    
    # Extract latest review grade
    rev_rows = re.findall(r"\|\s*\d{4}-\d{2}-\d{2}\s*\|.*?\|\s*(Grade [A-E])\s*\|", c)
    if rev_rows:
        gt_grade = rev_rows[-1]
    else:
        ai_grade = re.search(r"\*\s*\*\*Grade\*\*:\s*`?(Grade [A-E])", c)
        gt_grade = ai_grade.group(1) if ai_grade else "Grade A"

    ground_truth_map[fname] = {
        "name": fname,
        "next_review": nr.group(1) if nr else "null",
        "last_attempt": la.group(1) if la else "Unknown",
        "difficulty": diff.group(1) if diff else "Unknown",
        "track": track.group(1).strip() if track else "Unknown",
        "pattern": pat.group(1).strip() if pat else "Unknown",
        "url": url.group(1).strip() if url else "",
        "grade": gt_grade
    }

log_test("3.1 Ground Truth File Count", len(ground_truth_map) == 34, f"Found {len(ground_truth_map)} solved problem notes in 02 Problems/")

# Cross-verify with 07 Progress/NeetCode 150 Tracker.md
with open(TRACKER_PATH, "r", encoding="utf-8") as f:
    tracker_content = f.read()

# Check total solved in tracker frontmatter
tm_solved = re.search(r"total_solved:\s*(\d+)", tracker_content)
log_test("3.2 Tracker Total Solved Frontmatter", tm_solved and int(tm_solved.group(1)) == 29, f"total_solved = {tm_solved.group(1) if tm_solved else 'None'} (expected 29)")

# Check total target in tracker frontmatter
tm_target = re.search(r"total_target:\s*(\d+)", tracker_content)
log_test("3.3 Tracker Total Target Frontmatter", tm_target and int(tm_target.group(1)) == 150, f"total_target = {tm_target.group(1) if tm_target else 'None'} (expected 150)")

# Check checkboxes count in tracker
checked_boxes = len(re.findall(r"- \[x\]", tracker_content))
unchecked_boxes = len(re.findall(r"- \[ \]", tracker_content))
log_test("3.4 Tracker Checkboxes Count", checked_boxes == 34 and unchecked_boxes == 121,
         f"Checked: {checked_boxes} (29 core + 5 supplementary = 34), Unchecked: {unchecked_boxes} (121)")

# Check that all 29 solved NeetCode problems in tracker match ground truth grade & next review
tracker_solve_mismatches = []
for mod in NEETCODE_150:
    for p in mod["problems"]:
        pname = p["name"]
        match_row = re.search(rf"\|\s*(- \[[ x]\]\s*(?:✅ Solved|⏳ Unsolved))\s*\|\s*{p['id']}\s*\|\s*(.*?)\s*\|\s*{p['diff']}\s*\|.*?\|\s*(Grade [A-E]|-)\s*\|\s*(`[\d-]+`|-)\s*\|", tracker_content)
        if not match_row:
            tracker_solve_mismatches.append(f"Row formatting mismatch for prob {p['id']}: {pname}")
            continue
        
        status_str, title_str, grade_str, nr_str = match_row.group(1), match_row.group(2), match_row.group(3), match_row.group(4)
        is_checked = "- [x]" in status_str
        
        # Check if in ground truth
        gt = ground_truth_map.get(pname)
        if not gt:
            for al in p.get("aliases", []):
                if al in ground_truth_map:
                    gt = ground_truth_map[al]
                    break
        
        if gt:
            if not is_checked:
                tracker_solve_mismatches.append(f"Problem {pname} is solved in vault but unchecked in tracker")
            if grade_str != gt["grade"]:
                tracker_solve_mismatches.append(f"Grade mismatch for {pname}: tracker '{grade_str}' vs ground truth '{gt['grade']}'")
            exp_nr_str = f"`{gt['next_review']}`" if gt['next_review'] not in ["null", ""] else "-"
            if nr_str != exp_nr_str:
                tracker_solve_mismatches.append(f"Next review mismatch for {pname}: tracker '{nr_str}' vs ground truth '{exp_nr_str}'")
        else:
            if is_checked:
                tracker_solve_mismatches.append(f"Problem {pname} is NOT solved in vault but checked in tracker")
            if grade_str != "-":
                tracker_solve_mismatches.append(f"Unsolved problem {pname} has non-empty grade '{grade_str}'")
            if nr_str != "-":
                tracker_solve_mismatches.append(f"Unsolved problem {pname} has non-empty next_review '{nr_str}'")

log_test("3.5 Tracker Problem-by-Problem Ground Truth Consistency", len(tracker_solve_mismatches) == 0,
         "All 150 tracker rows match vault ground truth: " + "; ".join(tracker_solve_mismatches[:3]))

# Check Supplementary Section
supp_rows = re.findall(r"\|\s*- \[x\] ✅ Solved\s*\|\s*\*\*\[\[(.*?)\]\]\*\*", tracker_content[tracker_content.find("Supplementary"):])
log_test("3.6 Supplementary Solved Section (5 Problems)", len(supp_rows) == 5, f"Supplementary section contains {len(supp_rows)} practice notes (expected 5)")

# ==============================================================================
# SECTION 4: PROBLEM INDEX.MD VERIFICATION
# ==============================================================================
print("\n--- Phase 4: Problem Index.md Spaced Repetition Consistency ---")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index_content = f.read()

# Check Active Revision Queue (Due <= 2026-08-14)
expected_due = [k for k, v in ground_truth_map.items() if v["next_review"] != "null" and v["next_review"] <= "2026-08-14"]
expected_scheduled = [k for k, v in ground_truth_map.items() if v["next_review"] == "null" or v["next_review"] > "2026-08-14"]

active_queue_match = re.search(r"## 🔴 Active Revision Queue.*? — (\d+) Problems", index_content)
future_queue_match = re.search(r"## 🟢 Future Scheduled Revisions.*? — (\d+) Problems", index_content)
master_inv_match = re.search(r"## 📊 Master Problem Inventory \((\d+) Solved\)", index_content)

log_test("4.1 Problem Index Active Queue Count",
         active_queue_match and int(active_queue_match.group(1)) == len(expected_due) == 20,
         f"Active queue count: {active_queue_match.group(1) if active_queue_match else 'None'} (expected {len(expected_due)})")

log_test("4.2 Problem Index Future Scheduled Count",
         future_queue_match and int(future_queue_match.group(1)) == len(expected_scheduled) == 14,
         f"Future scheduled count: {future_queue_match.group(1) if future_queue_match else 'None'} (expected {len(expected_scheduled)})")

log_test("4.3 Problem Index Master Inventory Count",
         master_inv_match and int(master_inv_match.group(1)) == len(ground_truth_map) == 34,
         f"Master inventory count: {master_inv_match.group(1) if master_inv_match else 'None'} (expected 34)")

# Check Specific High-Value Problem Grades
level_order_in_inv = re.search(r"\|\s*\*\*\[\[Binary Tree Level Order Traversal\]\]\*\*\s*\|.*?\|\s*(Grade [A-E])\s*\|", index_content)
log_test("4.4 Multi-Attempt Grade Accuracy (Binary Tree Level Order Traversal)",
         level_order_in_inv and level_order_in_inv.group(1) == "Grade A",
         f"Grade in Master Inventory: {level_order_in_inv.group(1) if level_order_in_inv else 'None'} (expected Grade A)")

invert_in_inv = re.search(r"\|\s*\*\*\[\[Invert Binary Tree\]\]\*\*\s*\|.*?\|\s*(Grade [A-E])\s*\|", index_content)
log_test("4.5 Multi-Attempt Grade Accuracy (Invert Binary Tree)",
         invert_in_inv and invert_in_inv.group(1) == "Grade B",
         f"Grade in Master Inventory: {invert_in_inv.group(1) if invert_in_inv else 'None'} (expected Grade B)")

subtree_in_inv = re.search(r"\|\s*\*\*\[\[Subtree of Another Tree\]\]\*\*\s*\|.*?\|\s*(Grade [A-E])\s*\|", index_content)
log_test("4.6 Multi-Attempt Grade Accuracy (Subtree of Another Tree)",
         subtree_in_inv and subtree_in_inv.group(1) == "Grade C",
         f"Grade in Master Inventory: {subtree_in_inv.group(1) if subtree_in_inv else 'None'} (expected Grade C)")

# ==============================================================================
# SECTION 5: BEHAVIORAL EXECUTION & DYNAMIC TEST HARNESS
# ==============================================================================
print("\n--- Phase 5: Dynamic Behavioral Verification ---")

# Test 5.1: Run script directly in production vault
res = subprocess.run([sys.executable, SCRIPT_PATH, "--date", "2026-08-14"], capture_output=True, text=True)
log_test("5.1 Standard Script Execution (Exit 0)", res.returncode == 0, f"Output: {res.stdout.strip()[:100]}...")

# Test 5.2: Dynamic isolation test in a sandbox directory
with tempfile.TemporaryDirectory() as tmpdir:
    test_vault = os.path.join(tmpdir, "mock_vault")
    test_problems = os.path.join(test_vault, "02 Problems")
    test_progress = os.path.join(test_vault, "07 Progress")
    os.makedirs(test_problems)
    os.makedirs(test_progress)
    
    # Copy exactly 2 problem notes to mock vault
    shutil.copy(os.path.join(PROBLEMS_DIR, "Contains Duplicate.md"), test_problems)
    shutil.copy(os.path.join(PROBLEMS_DIR, "Two Sum.md"), test_problems)
    
    res_mock = subprocess.run([
        sys.executable, SCRIPT_PATH,
        "--vault-root", test_vault,
        "--date", "2026-08-14"
    ], capture_output=True, text=True)
    
    mock_tracker_path = os.path.join(test_progress, "NeetCode 150 Tracker.md")
    mock_index_path = os.path.join(test_problems, "Problem Index.md")
    
    dynamic_success = False
    if res_mock.returncode == 0 and os.path.exists(mock_tracker_path) and os.path.exists(mock_index_path):
        m_tracker = open(mock_tracker_path).read()
        m_index = open(mock_index_path).read()
        m_solved = re.search(r"total_solved:\s*(\d+)", m_tracker)
        m_inv = re.search(r"Master Problem Inventory \((\d+) Solved\)", m_index)
        if m_solved and int(m_solved.group(1)) == 2 and m_inv and int(m_inv.group(1)) == 2:
            dynamic_success = True
    
    log_test("5.2 Dynamic Vault Isolation Test (Zero Hardcoding Proof)", dynamic_success,
             "Script dynamically evaluated mock vault with exactly 2 solved problems, generating accurate counts")

# Test 5.3: Future Date Spaced Repetition Simulation
res_future = subprocess.run([sys.executable, SCRIPT_PATH, "--date", "2026-08-30"], capture_output=True, text=True)
if res_future.returncode == 0:
    future_index = open(INDEX_PATH).read()
    f_active = re.search(r"## 🔴 Active Revision Queue.*? — (\d+) Problems", future_index)
    f_future = re.search(r"## 🟢 Future Scheduled Revisions.*? — (\d+) Problems", future_index)
    all_due_on_future = (f_active and int(f_active.group(1)) == 34 and f_future and int(f_future.group(1)) == 0)
    log_test("5.3 Spaced Repetition Dynamic Queue Recalibration (--date 2026-08-30)", all_due_on_future,
             f"All 34 problems shifted to active queue under future date simulation (Active: {f_active.group(1) if f_active else '?'}, Future: {f_future.group(1) if f_future else '?'})")
else:
    log_test("5.3 Spaced Repetition Dynamic Queue Recalibration", False, "Script failed with --date")

# Re-run standard date sync to restore 2026-08-14 state
subprocess.run([sys.executable, SCRIPT_PATH, "--date", "2026-08-14"], capture_output=True, text=True)

# ==============================================================================
# SECTION 6: WIKILINKS & TABLE FORMATTING INTEGRITY
# ==============================================================================
print("\n--- Phase 6: Wikilinks & Markdown Formatting Integrity ---")

# Check all solved notes in tracker link to existing problem files
solved_links = re.findall(r"\|\s*- \[x\] ✅ Solved\s*\|\s*\d+\s*\|\s*\*\*\[\[(.*?)(?:\|.*?)?\]\]\*\*", tracker_content)
all_solved_files_exist = True
missing_files = []
for sl in solved_links:
    target_file = os.path.join(PROBLEMS_DIR, f"{sl}.md")
    if not os.path.exists(target_file):
        all_solved_files_exist = False
        missing_files.append(sl)

log_test("6.1 Solved Wikilinks Target Validation", all_solved_files_exist,
         f"All {len(solved_links)} solved wikilinks resolve to existing files on disk (Missing: {missing_files})")

# Check module pattern wikilinks format
pattern_links = re.findall(r"\*\*Pattern Note\*\*:\s*\[\[(.*?)\]\]", tracker_content)
log_test("6.2 Module Pattern Header Format", len(pattern_links) == 18,
         f"All 18 modules define canonical pattern wikilinks (e.g. [[Arrays & Hashing]], [[Two Pointers]], etc.)")

# Check markdown table pipe escaping
has_broken_pipes = re.search(r"\|\s*\[LeetCode\]\(.*?\)\s*\|\s*\[NeetCode\]\(.*?\)\s*\|", tracker_content)
log_test("6.3 Markdown Table Pipe Escaping", not has_broken_pipes,
         r"All platform link separators in tables use escaped pipes (\|) to prevent column corruption")

# ==============================================================================
# AUDIT SUMMARY & VERDICT GENERATION
# ==============================================================================
print("\n" + "=" * 70)
print(f"📊 FORENSIC AUDIT SUMMARY: {audit_results['passed_tests']} / {audit_results['total_tests']} Checks Passed")
if audit_results["failed_tests"] == 0:
    print("🏆 FINAL VERDICT: CLEAN")
else:
    print(f"🚨 FINAL VERDICT: INTEGRITY VIOLATION ({audit_results['failed_tests']} Failures)")
print("=" * 70)

# Save JSON result summary for report generation
with open(os.path.join(os.path.dirname(__file__), "audit_run_results.json"), "w", encoding="utf-8") as f:
    json.dump(audit_results, f, indent=2)
