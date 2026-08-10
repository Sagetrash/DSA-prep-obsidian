---
problem_id: "875"
title: "Koko Eating Bananas"
platform: LeetCode
url: "https://leetcode.com/problems/koko-eating-bananas/"
difficulty: Medium
track: High Value
primary_pattern: "[[Binary Search]]"
secondary_patterns: []
status: Attempted
result: Wrong Answer
attempts: 1
independent_solves: 0
hint_used: none
time_taken: 13m
first_attempt: 2026-08-10
last_attempt: 2026-08-10
next_review: 2026-08-11
confidence: 3
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
* **Status**: `Attempted` | **Result**: `Wrong Answer (Boundary Return Bug)`

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
            speed = low + (high-low)//2
            hours = self.hoursRequired(speed,piles)
            if hours <= h:
                high = speed - 1
            else:
                low = speed + 1
        return speed  # ⚠️ Bug: returning `speed` instead of `low` or tracking `res`
    
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
| 2026-08-10 | Wrong Answer | 13m | none | Grade B | Excellent intuition & binary search structure, but returning `speed` fails when final loop iteration hits an invalid speed. |

---

## AI Analysis

### Interview Readiness Grade: **B (Correct Strategy, Subtle Boundary Return Bug)**

### Code Evaluation & Complexity
1. **Time Complexity**: $\mathcal{O}(N \log(\max(P)))$ — Binary search range $[1, \max(P)]$ takes $\log_2(\max(P))$ steps; each step iterates over $N$ piles.
2. **Space Complexity**: $\mathcal{O}(1)$ — Scalar variables only.
3. **Bug & Counter-Example Analysis**:
   * **The Flaw**: Returning `speed` at the end returns whichever value `speed` held on the **last iteration** of the `while low <= high:` loop. If the final iteration tests an invalid speed (`hours > h`), the loop executes `low = speed + 1` and terminates, but `speed` retains the invalid speed!
   * **Counter Example**: `piles = [3, 6]`, `h = 3`. Target minimum speed is `3`.
     - Pass 1: `low=1, high=6` $\to$ `speed=3`. `hours=3 <= 3` $\implies$ `high=2`.
     - Pass 2: `low=1, high=2` $\to$ `speed=1`. `hours=9 > 3` $\implies$ `low=2`.
     - Pass 3: `low=2, high=2` $\to$ `speed=2`. `hours=5 > 3` $\implies$ `low=3`. Loop ends (`low=3 > high=2`).
     - Function returns `speed` $\to$ **`2`** (which takes 5 hours > 3 hours! 💥).

### Optimal Fixes
1. **Option A (Return `low`)**: Return `low` instead of `speed` because `low` converges to the minimal valid speed.
2. **Option B (Track `res`)**: Initialize `res = high` and update `res = speed` inside `if hours <= h:`.
3. **Integer Ceiling Idiom**: Use `(pile + speed - 1) // speed` instead of `ceil(pile / speed)` to avoid floating-point inaccuracies on large values.

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        
        while low <= high:
            speed = low + (high - low) // 2
            hours = sum((pile + speed - 1) // speed for pile in piles)
            
            if hours <= h:
                res = speed
                high = speed - 1
            else:
                low = speed + 1
                
        return res
```

