---
pattern_name: "Dynamic Programming"
category: "Algorithmic Pattern"
mastery_level: 4
attempted_count: 1
solved_count: 1
independent_solved_count: 1
hint_rate: "0%"
average_time: "5m"
tags:
  - pattern
---

# Dynamic Programming

## 🚨 Recognition Signals
* **Signals**: Overlapping subproblems, optimal substructure, counting ways to reach a state, min/max cost to reach target.
* **Keywords**: "Climbing stairs", "House robber", "Coin change", "Longest increasing subsequence", "Partition equal subset sum".

---

## 💡 Core Idea & Intuition
Store results of smaller subproblems (memoization / bottom-up DP table) to avoid redundant recursive calculations.

---

## 🛠️ Code Template / Mental Model

### Bottom-Up DP (Space Optimized)
```python
def rob(nums):
    rob1, rob2 = 0, 0
    for num in nums:
        temp = max(num + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```
