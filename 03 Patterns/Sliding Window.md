---
pattern_name: "Sliding Window"
category: "Algorithmic Pattern"
mastery_level: 3
attempted_count: 3
solved_count: 3
independent_solved_count: 1
hint_rate: "67%"
average_time: "13m 40s"
tags:
  - pattern
---

# Sliding Window

## 🚨 Recognition Signals
* **Signals**: Subarray/Substring problems with contiguous constraints, minimum/maximum length window meeting condition $K$.
* **Keywords**: "Longest substring without repeating characters", "Minimum window substring", "Maximum subarray of size K".

---

## 💡 Core Idea & Intuition
Maintain a contiguous range bounded by `L` and `R`. Expand `R` to satisfy the problem condition, and shrink `L` when the window violates constraints. Converts brute-force $O(N^2)$ to $O(N)$ amortized.

---

## 🛠️ Code Template / Mental Model

```python
def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```
