---
mistake_name: "Brute-Force Fixation"
category: "Pattern Recognition Failure"
occurrences: 0
severity: "High"
tags:
  - mistake
---

# Brute-Force Fixation

## 📌 Description & Root Cause
Getting stuck trying to optimize a nested $O(N^2)$ loop or brute-force recursion instead of stepping back to identify structural signals (e.g. sorted property $\implies$ Two Pointers/Binary Search, subarray sum $\implies$ Prefix Sum/Sliding Window, frequency $\implies$ Hashmap).

---

## 🛡️ Prevention Rule & Mental Checklist
- [ ] Read input constraints ($N \le 10^5 \implies O(N)$ or $O(N \log N)$ expected).
- [ ] If brute force is $O(N^2)$, list data structures that trade space for time ($O(N)$ Hashmap, Stack, Two Pointers).
- [ ] Stop coding if time limit exceeds 5 minutes without a clear optimal approach.

---

## 🔗 Problems Where This Mistake Occurred
```dataview
TABLE title, difficulty, track, result, primary_pattern
FROM "02 Problems"
WHERE contains(file.outlinks, this.file.link)
```
