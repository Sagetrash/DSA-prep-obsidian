---
mistake_name: "Set Deduplication Overhead"
category: "Space Optimization & Pointer Discipline"
occurrences: 1
severity: "Medium"
tags:
  - mistake
  - two-pointers
  - space-complexity
---

# Set Deduplication Overhead

## 📌 Description & Root Cause
Relying on a `set()` data structure to prune duplicate output tuples instead of handling duplicate values in-place via pointer arithmetic. 
While functionally correct, this increases extra space complexity from $\mathcal{O}(1)$ to $\mathcal{O}(N^2)$ (to store output triplets in memory) and introduces hashing overhead that can lead to TLE or sub-optimal ratings in technical interviews.

---

## 🛡️ Prevention Rule & Mental Checklist
- [ ] In sorted 2-pointer problems, skip duplicate outer values: `if i > 0 and nums[i] == nums[i-1]: continue`.
- [ ] After finding a valid target, advance both pointers past duplicate values:
  ```python
  while low < high and nums[low] == nums[low + 1]: low += 1
  while low < high and nums[high] == nums[high - 1]: high -= 1
  ```
- [ ] Reserve `set()` for unordered frequency lookup, not for in-place array duplicate filtering.

---

## 🔗 Problems Where This Mistake Occurred
```dataview
TABLE title, difficulty, track, result, primary_pattern
FROM "02 Problems"
WHERE contains(file.outlinks, this.file.link)
```
