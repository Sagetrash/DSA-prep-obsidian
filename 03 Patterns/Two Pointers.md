---
pattern_name: "Two Pointers"
category: "Algorithmic Pattern"
mastery_level: 5
attempted_count: 7
solved_count: 7
independent_solved_count: 7
hint_rate: "0%"
average_time: "9.6m"
tags:
  - pattern
---

# Two Pointers

## 🚨 Recognition Signals
* **Signals**: Array/String is sorted, finding pairs/triplets with specific target sum, reversing in-place, removing duplicates in-place, palindrome checking.
* **Keywords**: "Sorted array", "In-place", "Pair with target sum", "3Sum", "Container with most water".

---

## 💡 Core Idea & Intuition
Iterate two reference pointers (either converging from opposite ends `left=0, right=N-1` or fast/slow starting together `slow=0, fast=0`) to process linear data in $O(N)$ time with $O(1)$ extra space.

---

## 🛠️ Code Template / Mental Model

### Converging Pointers (Sorted Data)
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```
