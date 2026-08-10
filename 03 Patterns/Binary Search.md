---
pattern_name: "Binary Search"
category: "Algorithmic Pattern"
mastery_level: 5
attempted_count: 2
solved_count: 2
independent_solved_count: 2
hint_rate: "0%"
average_time: "8m"
tags:
  - pattern
---

# Binary Search

## 🚨 Recognition Signals
* **Signals**: Sorted array, searching in $O(\log N)$ time, finding boundary condition (first bad version), searching answer space (binary search on answer).
* **Keywords**: "Sorted array", "O(log N) time complexity", "Search insert position", "First bad version".

---

## 💡 Core Idea & Intuition
Halve the search domain at each iteration by comparing the mid element `mid = left + (right - left) // 2` against the search condition.

---

## 🛠️ Code Template / Mental Model

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```
