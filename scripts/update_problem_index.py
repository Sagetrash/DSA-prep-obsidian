#!/usr/bin/env python3
import os
import glob
import re

index_path = '/mnt/Driver_E/My Files/projects/DSA-prep/02 Problems/Problem Index.md'
problems_dir = '/mnt/Driver_E/My Files/projects/DSA-prep/02 Problems'
today = '2026-08-14'

files = [f for f in glob.glob(os.path.join(problems_dir, '*.md')) if not f.endswith('Problem Index.md')]

problems = []

for f in sorted(files):
    name = os.path.splitext(os.path.basename(f))[0]
    with open(f, 'r') as file_content:
        content = file_content.read()
    
    nr_match = re.search(r'next_review:\s*([\d-]+|null)', content)
    last_match = re.search(r'last_attempt:\s*([\d-]+|null)', content)
    diff_match = re.search(r'difficulty:\s*(\w+)', content)
    track_match = re.search(r'track:\s*(.*?)\n', content)
    pat_match = re.search(r'primary_pattern:\s*\"?\[\[(.*?)\]\]\"?', content)
    grade_match = re.search(r'Code Grade \| Notes \|.*?\n\|.*?\s*\|\s*.*?\s*\|\s*.*?\s*\|\s*(Grade [A-E])', content)
    
    nr = nr_match.group(1) if nr_match else 'null'
    last_att = last_match.group(1) if last_match else 'Unknown'
    diff = diff_match.group(1) if diff_match else 'Unknown'
    track = track_match.group(1).strip() if track_match else 'Unknown'
    pat = pat_match.group(1) if pat_match else 'Unknown'
    grade = grade_match.group(1) if grade_match else 'Grade A'
    
    is_due = (nr != 'null' and nr <= today)
    
    problems.append({
        'name': name,
        'next_review': nr,
        'last_attempt': last_att,
        'difficulty': diff,
        'track': track,
        'pattern': pat,
        'grade': grade,
        'is_due': is_due
    })

due_probs = [p for p in problems if p['is_due']]
due_probs.sort(key=lambda x: x['next_review'])

future_probs = [p for p in problems if not p['is_due']]
future_probs.sort(key=lambda x: x['next_review'])

lines = []
lines.append('---')
lines.append('title: "Problem Index & Revision Dashboard"')
lines.append(f'last_updated: {today}')
lines.append('tags:')
lines.append('  - index')
lines.append('  - problems')
lines.append('  - revision')
lines.append('---')
lines.append('')
lines.append('# 📚 Central Problem Index & Revision Dashboard')
lines.append('')
lines.append('This note dynamically tracks all problems in the vault, their attempt metrics, and their current **Spaced Repetition Revision Status**.')
lines.append('')
lines.append('---')
lines.append('')
lines.append(f'## 🔴 Active Revision Queue (Up for Review Today: {today}) — {len(due_probs)} Problems')
lines.append('')
lines.append('| Problem Title | Difficulty | Track | Primary Pattern | Last Attempt | Next Review Date | Status |')
lines.append('| :--- | :--- | :--- | :--- | :--- | :--- | :--- |')

for p in due_probs:
    status = '🟡 Due Today' if p['next_review'] == today else f"🔴 Overdue ({p['next_review']})"
    lines.append(f"| **[[{p['name']}]]** | {p['difficulty']} | {p['track']} | [[{p['pattern']}]] | {p['last_attempt']} | `{p['next_review']}` | {status} |")

lines.append('')
lines.append('---')
lines.append('')
lines.append(f'## 🟢 Future Scheduled Revisions (Upcoming Days) — {len(future_probs)} Problems')
lines.append('')
lines.append('| Problem Title | Difficulty | Track | Primary Pattern | Last Attempt | Next Review Date | Status |')
lines.append('| :--- | :--- | :--- | :--- | :--- | :--- | :--- |')

for p in future_probs:
    lines.append(f"| **[[{p['name']}]]** | {p['difficulty']} | {p['track']} | [[{p['pattern']}]] | {p['last_attempt']} | `{p['next_review']}` | 🟢 Scheduled |")

lines.append('')
lines.append('---')
lines.append('')
lines.append(f'## 📊 Master Problem Inventory ({len(problems)} Solved)')
lines.append('')
lines.append('| Problem Title | Difficulty | Track | Primary Pattern | Grade | Last Solved | Next Review Date |')
lines.append('| :--- | :--- | :--- | :--- | :--- | :--- | :--- |')

all_sorted = sorted(problems, key=lambda x: x['name'])
for p in all_sorted:
    lines.append(f"| **[[{p['name']}]]** | {p['difficulty']} | {p['track']} | [[{p['pattern']}]] | {p['grade']} | {p['last_attempt']} | `{p['next_review']}` |")

lines.append('')

with open(index_path, 'w') as f:
    f.write('\n'.join(lines))

print(f"Problem Index successfully generated with {len(due_probs)} due problems and {len(future_probs)} scheduled problems!")
