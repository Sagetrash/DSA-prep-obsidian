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
hint_used: small
independent_solves: 1
time_taken: "6m"
grade: "B"
last_attempted: 2026-08-17
next_review: 2026-08-18
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

Asked whether cost is paid for the step currently stood on, then recognized we can iterate backwards from `len(cost) - 1` down to `0` to accumulate the optimal subproblem costs bottom-up.

---

## 🔍 My Reasoning & Approach

1. **Bottom-Up 1D DP Recurrence**:
   - `dp[i] = cost[i] + min(dp[i+1], dp[i+2])`
2. **Space Optimization ($\mathcal{O}(1)$ Space)**:
   - Instead of maintaining a full array of size $N$, use 2 scalar variables (`one` and `two`) representing the minimum cost to reach the top from steps $i+1$ and $i+2$.
   - Iterate backwards from index `len(cost) - 1` to `0`.
   - Update `temp = cost[i] + min(one, two)`, then shift state: `two = one`, `one = temp`.
3. **Return Value Refinement**:
   - Starting from `len(cost) - 1` down to `0`, `one` will hold the cost starting at index `0`, and `two` will hold the cost starting at index `1`.
   - Return `min(one, two)`.

---

## 💻 My Solution

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
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
3. **Pattern Verification**: Classic 1D Bottom-Up Dynamic Programming state reduction (Fibonacci/Climbing Stairs pattern family).
4. **Code Quality Note**: If iterating backwards through `range(len(cost) - 1, -1, -1)`, `cost.append(0)` is unnecessary when `one` and `two` are initialized to `0`.

### Interview Readiness Grade
**Grade: B — Correct but needed minor clarification**
* Clarified requirement on step-cost payment and starting index choices. Clean $\mathcal{O}(1)$ space bottom-up DP logic!

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-17 | Accepted | 6m | small | B |

