---
title: "Min Cost Climbing Stairs"
leetcode_url: "https://leetcode.com/problems/min-cost-climbing-stairs/"
neetcode_url: "https://neetcode.io/problems/min-cost-climbing-stairs"
difficulty: Easy
track: Volume
primary_pattern: "[[Dynamic Programming]]"
secondary_patterns: []
neetcode_number: 100
result: "Accepted"
hint_used: none
independent_solves: 2
time_taken: "11m"
grade: "A"
last_attempted: 2026-08-18
next_review: 2026-08-21
mistakes: []
tags:
  - problem
  - dynamic-programming
  - easy
---

# Min Cost Climbing Stairs

**Difficulty**: Easy | **Track**: Volume | **Pattern**: [[Dynamic Programming]]
**LeetCode**: [#746](https://leetcode.com/problems/min-cost-climbing-stairs/) | **NeetCode**: [Link](https://neetcode.io/problems/min-cost-climbing-stairs)

---

## 💭 My First Thought

Iterate backwards from `len(cost) - 1` down to `0` using 2 scalar variables `one` and `two` initialized to `0`, accumulating `temp = cost[i] + min(one, two)` at each step to maintain optimal subproblem costs in $\mathcal{O}(1)$ space.

---

## 🔍 My Reasoning & Approach

1. **Bottom-Up 1D DP Recurrence**:
   - `dp[i] = cost[i] + min(dp[i+1], dp[i+2])`
2. **Space Optimization ($\mathcal{O}(1)$ Space)**:
   - Instead of maintaining a full array of size $N$, use 2 scalar variables (`one` and `two`) representing the minimum cost to reach the top from steps $i+1$ and $i+2$.
   - Iterate backwards from index `len(cost) - 1` to `0`.
   - Update `temp = cost[i] + min(one, two)`, then shift state: `two = one`, `one = temp`.
3. **Return Value**:
   - Return `min(one, two)`.

---

## 💻 My Solution

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        one = 0
        two = 0
        for i in range(len(cost) - 1, -1, -1):
            temp = cost[i] + min(one, two)
            two = one
            one = temp
        return min(one, two)
```

**Time Complexity**: $\mathcal{O}(N)$ linear scan of `cost` array.  
**Space Complexity**: $\mathcal{O}(1)$ constant extra space using 2 scalar variables.

---

## 🤖 AI Analysis

### Code Analysis Checklist
1. **Correctness**: Fully correct. Operates backwards in $\mathcal{O}(N)$ time.
2. **Complexity**: Optimal $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.
3. **Pattern Verification**: Classic 1D Bottom-Up Dynamic Programming state reduction.
4. **Code Quality**: Clean, intuitive implementation of 1D DP state rolling.

### Interview Readiness Grade
**Grade: A — Strong independent solution**
* Zero hints used. Solved independently in 11 minutes with optimal $\mathcal{O}(1)$ space DP recurrence. Mastery jump from Grade B $\to$ Grade A!

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-17 | Accepted | 6m | small | B |
| 2 | 2026-08-18 | Accepted | 11m | none | A |
