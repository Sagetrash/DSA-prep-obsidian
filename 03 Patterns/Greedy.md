---
pattern_name: "Greedy"
category: "Algorithmic Pattern"
mastery_level: 5
attempted_count: 2
solved_count: 2
independent_solved_count: 2
hint_rate: "0%"
average_time: "7m"
tags:
  - pattern
---

# Greedy

## 🚨 Recognition Signals
* **Signals**: Making locally optimal choice at each step to reach global optimum, interval scheduling, max subarray sum (Kadane's).
* **Keywords**: "Maximum subarray", "Jump game", "Gas station", "Task scheduler", "Assign cookies".

---

## 💡 Core Idea & Intuition
Make the choice that looks best right now without reconsidering past decisions. Requires proving optimal substructure.

---

## 🛠️ Code Template / Mental Model

### Kadane's Algorithm
```python
def max_sub_array(nums):
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```
