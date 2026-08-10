---
mistake_name: "Hashmap Update Error"
category: "Logic Error"
occurrences: 0
severity: "Medium"
tags:
  - mistake
---

# Hashmap Update Error

## 📌 Description & Root Cause
Errors in frequency counts, missing key initialization, overwriting indices when duplicates occur, or updating hashmap state after checking condition instead of before (or vice versa).

---

## 🛡️ Prevention Rule & Mental Checklist
- [ ] Determine if hashmap stores single index, list of indices, or frequency count.
- [ ] For sliding window / subarray problems, update frequency count **after** shrink/expand condition dry run.
- [ ] Use `collections.defaultdict` or `hashmap.get(key, default)`.

---

## 💻 Anti-Pattern vs Correct Pattern

### ❌ Incorrect Code Snippet
```python
# Overwriting index without handling duplicates
seen = {}
for i, num in enumerate(nums):
    seen[num] = i # Overwrites previous index!
```

### ✅ Correct Code Snippet
```python
# Check BEFORE inserting current element if index distance matters
seen = {}
for i, num in enumerate(nums):
    if num in seen:
        # process duplicate
        pass
    seen[num] = i
```

---

## 🔗 Problems Where This Mistake Occurred
```dataview
TABLE title, difficulty, track, result, primary_pattern
FROM "02 Problems"
WHERE contains(file.outlinks, this.file.link)
```
