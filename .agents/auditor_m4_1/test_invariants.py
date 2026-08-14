#!/usr/bin/env python3
import os
import re

vault_root = '/mnt/Driver_E/My Files/projects/DSA-prep'
tracker_file = os.path.join(vault_root, '07 Progress/NeetCode 150 Tracker.md')
index_file = os.path.join(vault_root, '02 Problems/Problem Index.md')

t_content = open(tracker_file).read()
i_content = open(index_file).read()

# Assertions
assert 'total_solved: 29' in t_content, 'Tracker frontmatter total_solved mismatch'
assert 'total_target: 150' in t_content, 'Tracker frontmatter total_target mismatch'
assert 'completion_percentage: "19.3%"' in t_content, 'Tracker completion pct mismatch'
assert 'easy_solved: 15' in t_content, 'Easy solved mismatch'
assert 'medium_solved: 14' in t_content, 'Medium solved mismatch'
assert 'hard_solved: 0' in t_content, 'Hard solved mismatch'

# Check 150 problem rows in tracker
all_rows = re.findall(r'\|\s*(- \[[ x]\]\s*(?:✅ Solved|⏳ Unsolved))\s*\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(Easy|Medium|Hard)\s*\|', t_content)
assert len(all_rows) == 150, f'Expected 150 rows in module tables, found {len(all_rows)}'

# Check supplementary rows
supp_rows = re.findall(r'\|\s*- \[x\] ✅ Solved\s*\|\s*\*\*\[\[(.*?)\]\]\*\*\s*\|\s*(Easy|Medium|Hard)\s*\|', t_content)
assert len(supp_rows) == 5, f'Expected 5 supplementary rows, found {len(supp_rows)}'

# Check Problem Index queues
active_rows = re.findall(r'\|\s*\*\*\[\[(.*?)\]\]\*\*\s*\|\s*(Easy|Medium|Hard)\s*\|.*?\|\s*(`[\d-]+`)\s*\|\s*(🟡 Due Today|🔴 Overdue \([\d-]+\))\s*\|', i_content)
assert len(active_rows) == 20, f'Expected 20 active review rows, found {len(active_rows)}'

future_rows = re.findall(r'\|\s*\*\*\[\[(.*?)\]\]\*\*\s*\|\s*(Easy|Medium|Hard)\s*\|.*?\|\s*(`[\d-]+`)\s*\|\s*🟢 Scheduled\s*\|', i_content)
assert len(future_rows) == 14, f'Expected 14 future scheduled rows, found {len(future_rows)}'

inv_rows = re.findall(r'\|\s*\*\*\[\[(.*?)\]\]\*\*\s*\|\s*(Easy|Medium|Hard)\s*\|.*?\|\s*(Grade [A-E])\s*\|\s*([\d-]+)\s*\|\s*(`[\d-]+`)\s*\|', i_content)
assert len(inv_rows) == 34, f'Expected 34 master inventory rows, found {len(inv_rows)}'

print('All 7 Core Integrity Invariants EMPIRICALLY VALIDATED!')
