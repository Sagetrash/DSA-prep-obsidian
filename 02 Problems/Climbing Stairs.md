---
problem_id: "70"
title: "Climbing Stairs"
platform: LeetCode
url: "https://leetcode.com/problems/climbing-stairs/"
difficulty: Easy
track: Volume
primary_pattern: "[[Dynamic Programming]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 5m
first_attempt: 2026-08-13
last_attempt: 2026-08-13
next_review: 2026-08-14
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - dp
---

# Climbing Stairs

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/climbing-stairs/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Dynamic Programming]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-14`

---

## Problem Statement
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

### Examples
```text
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

### Constraints
* `1 <= n <= 45`

---

## My First Thought
For every $i$-th step, the total ways would simply be number of ways for $i-1$ (1 step) + $i-2$ (2 steps), so I can make an array of length $n+1$ which would store the number of ways for every $i$-th stair.

---

## My Solution
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range((n)+1)]
        for i in range((n)+1):
            if i == 0:
                dp[0] = 0
                continue
            if i == 1:
                dp[1] = 1
                continue
            if i == 2:
                dp[2] = 2
                continue
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
```

---

## Attempt Log & Metrics
* **Time Taken**: 5m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
The problem exhibits optimal substructure and overlapping subproblems: to land on step $i$, the final move must come from step $i-1$ (via a 1-step move) or step $i-2$ (via a 2-step move). Thus, the number of distinct ways to reach step $i$ is `dp[i] = dp[i-1] + dp[i-2]`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Dynamic Programming]] (1D Bottom-Up)
* **Time Complexity**: $\mathcal{O}(N)$ — single loop from $0$ to $N$.
* **Space Complexity**: $\mathcal{O}(N)$ — DP table of size $N+1$. (Can be optimized to $\mathcal{O}(1)$ space by maintaining 2 scalar variables `prev1` and `prev2`).

---

## Key Edge Cases
- [x] $N = 1 \implies$ Returns `1`
- [x] $N = 2 \implies$ Returns `2`
- [x] Maximum bound $N = 45 \implies$ Fits within standard 32-bit/64-bit integer limits without overflow.

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-13 | Accepted | 5m | none | Grade A | Initial DP solve! Clean 1D bottom-up table. |

---

## AI Analysis
* **Grade**: `Grade A`
* **Edge Cases Missed**: None — explicit base case checks for $i=0, 1, 2$ prevent out-of-bounds indexing.
* **Code Quality**: Clean and readable.
* **Optimization Opportunity**: In Python, instead of allocating a full `dp` array of size $N+1$, you can optimize space from $\mathcal{O}(N)$ to $\mathcal{O}(1)$ by keeping 2 variables:
  ```python
  def climbStairs(self, n: int) -> int:
      if n <= 2: return n
      prev2, prev1 = 1, 2
      for _ in range(3, n + 1):
          prev2, prev1 = prev1, prev2 + prev1
      return prev1
  ```
