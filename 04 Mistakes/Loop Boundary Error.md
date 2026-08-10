---
mistake_name: "Loop Boundary Error"
category: "Implementation Error"
occurrences: 0
severity: "High"
tags:
  - mistake
---

# Loop Boundary Error

## 📌 Description & Root Cause
Failing to properly terminate loops (`while` or `for`), resulting in infinite loops, skipped elements, or TLE (Time Limit Exceeded). Common in Two Pointer techniques, Binary Search, and Linked List traversal.

---

## 🛡️ Prevention Rule & Mental Checklist
- [ ] Every pointer updated inside a `while` loop MUST guarantee progression toward the termination condition.
- [ ] Verify `while left < right` vs `while left <= right`.
- [ ] Check linked list traversal loop condition (`while curr` vs `while curr and curr.next`).

---

## 💻 Anti-Pattern vs Correct Pattern

### ❌ Incorrect Code Snippet
```python
while left < right:
    # Missing left += 1 or right -= 1 under certain conditions -> Infinite Loop!
    if nums[left] + nums[right] == target:
        return [left, right]
```

### ✅ Correct Code Snippet
```python
while left < right:
    s = nums[left] + nums[right]
    if s == target:
        return [left, right]
    elif s < target:
        left += 1
    else:
        right -= 1
```

---

## 🔗 Problems Where This Mistake Occurred
```dataview
TABLE title, difficulty, track, result, primary_pattern
FROM "02 Problems"
WHERE contains(file.outlinks, this.file.link)
```
