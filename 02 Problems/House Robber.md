---
problem_id: "198"
title: "House Robber"
platform: LeetCode
url: "https://leetcode.com/problems/house-robber/"
difficulty: Medium
track: High Value
primary_pattern: "[[Dynamic Programming]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 8m
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

# House Robber

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/house-robber/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Dynamic Programming]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-14`

---

## Problem Statement
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Examples
```text
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1). Total = 2 + 9 + 1 = 12.
```

### Constraints
* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 400`

---

## My First Thought
I can compare the two options for every house `curr`: robbing house `curr` (`nums[curr] + dp[curr-2]`) vs skipping house `curr` (`dp[curr-1]`). Taking the maximum of these two decisions at each step builds up the optimal answer array.

---

## My Solution
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
                continue
            if i == 1:
                dp[i] = max(nums[i], nums[i-1])
                continue
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
```

---

## Attempt Log & Metrics
* **Time Taken**: 8m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
At each house $i$, we must decide whether to rob it or skip it.
1. **Rob house $i$**: We add `nums[i]` to the maximum money robbed up to house $i-2$ (`dp[i-2]`), because house $i-1$ cannot be robbed.
2. **Skip house $i$**: The maximum money robbed remains the maximum achieved up to house $i-1$ (`dp[i-1]`).

The recurrence relation is `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Dynamic Programming]] (1D Bottom-Up)
* **Time Complexity**: $\mathcal{O}(N)$ — single pass iterating through array `nums`.
* **Space Complexity**: $\mathcal{O}(N)$ — 1D DP table of size $N$. (Can be optimized to $\mathcal{O}(1)$ space using two variables `rob1` and `rob2`).

---

## Key Edge Cases
- [x] $N = 1 \implies$ Returns `nums[0]` directly via `dp[0]`
- [x] $N = 2 \implies$ Returns `max(nums[0], nums[1])` via `dp[1]`
- [x] All zero array $\implies$ Returns `0`
- [x] Alternating high/low values $\implies$ Evaluated correctly via `max()` at each step

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-13 | Accepted | 8m | none | Grade A | Solved Medium DP problem independently! Clean 1D DP implementation. |

---

## AI Analysis
* **Grade**: `Grade A`
* **Edge Cases Missed**: None — explicit base case checks for `i == 0` and `i == 1` handle array lengths of 1 and 2 cleanly without index errors.
* **Code Quality**: Concise, readable, and logically clear.
* **Optimization Opportunity**: Space can be reduced from $\mathcal{O}(N)$ to $\mathcal{O}(1)$ by maintaining 2 variables tracking the last 2 optimal choices:
  ```python
  def rob(self, nums: List[int]) -> int:
      rob1, rob2 = 0, 0
      for num in nums:
          temp = max(num + rob1, rob2)
          rob1 = rob2
          rob2 = temp
      return rob2
  ```
