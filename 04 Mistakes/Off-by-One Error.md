---
mistake_name: "Off-by-One Error"
category: "Implementation Error"
occurrences: 0
severity: "High"
tags:
  - mistake
---

# Off-by-One Error

## 📌 Description & Root Cause
An error occurring when an iteration limit, index bound, or array slice range is off by 1 unit. Frequently seen in array indexing (`0` to `N-1` vs `1` to `N`), inclusive vs. exclusive range bounds in Binary Search, and string slice indices.

---

## 🛡️ Prevention Rule & Mental Checklist
- [ ] Explicitly check array bounds: `arr[0]` to `arr[len(arr) - 1]`.
- [ ] Binary search rule: Decide up front if `right` is `N-1` (inclusive `while left <= right`) or `N` (half-open `while left < right`). Never mix them.
- [ ] Dry run loop bounds with $N=1$ and $N=2$.

---

## 💻 Anti-Pattern vs Correct Pattern

### ❌ Incorrect Code Snippet
```python
# Accessing beyond bounds
for i in range(len(nums)):
    if nums[i] == nums[i+1]: # IndexError when i = len(nums)-1
        pass
```

### ✅ Correct Code Snippet
```python
for i in range(len(nums) - 1):
    if nums[i] == nums[i+1]:
        pass
```

---

## 🔗 Problems Where This Mistake Occurred
```dataview
TABLE title, difficulty, track, result, primary_pattern
FROM "02 Problems"
WHERE contains(file.outlinks, this.file.link)
```
