---
problem_id: "875"
title: "Koko Eating Bananas"
platform: LeetCode
url: "https://leetcode.com/problems/koko-eating-bananas/"
difficulty: Medium
track: High Value
primary_pattern: "[[Binary Search]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 2
independent_solves: 1
hint_used: small
time_taken: 13m
first_attempt: 2026-08-10
last_attempt: 2026-08-10
next_review: 2026-08-11
confidence: 5
expected_time_complexity: "O(N log(max(P)))"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - binary-search
---

# Koko Eating Bananas

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/koko-eating-bananas/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Binary Search]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her banana-eating speed of `k` bananas per hour. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

### Examples
```text
Input: piles = [3,6,7,11], h = 8
Output: 4

Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

### Constraints
* `1 <= piles.length <= 10^4`
* `piles.length <= h <= 10^9`
* `1 <= piles[i] <= 10^9`

---

## My First Thought
Apply binary search on the range of banana eating speed, where lower bound is `1` and upper bound is `max(piles)`. On this range binary search to minimize hours.

---

## My Solution
```python
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            speed = low + (high - low) // 2
            hours = self.hoursRequired(speed, piles)
            if hours <= h:
                high = speed - 1
            else:
                low = speed + 1
        return low  # Corrected: `low` converges to minimal valid speed
    
    def hoursRequired(self, speed, piles):
        hour = 0
        for pile in piles:
            hour += ceil(pile / speed)
        return hour
```

---

## Review History
| Date | Result | Time | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-10 | Wrong Answer | 13m | none | Grade B | Initial attempt — `return speed` returned invalid speed on boundary termination. |
| 2026-08-10 | Accepted | 2m | small | Grade A | Corrected return statement to `return low` — 100% optimal $\mathcal{O}(N \log(\max(P)))$ binary search on answer space. |

---

## AI Analysis

### Interview Readiness Grade: **A (Strong Solution Post-Correction)**

### Code Evaluation & Complexity
1. **Time Complexity**: $\mathcal{O}(N \log(\max(P)))$ — Binary search range $[1, \max(P)]$ takes $\log_2(\max(P))$ steps; each step iterates over $N$ piles.
2. **Space Complexity**: $\mathcal{O}(1)$ — Scalar variables only.
3. **Correctness & Edge Cases**:
   * Binary Search on Answer Space is cleanly executed.
   * `return low` accurately yields the smallest speed `k` such that `hoursRequired(k, piles) <= h`.
   * When `hours <= h`, shrinking `high = speed - 1` pushes `low` to hold the exact lower bound of valid speeds at loop termination.

### Mastery Level Assessment
* **Assigned Level**: **Level 5 (Can solve independently + explain approach & complexity clearly)**.


