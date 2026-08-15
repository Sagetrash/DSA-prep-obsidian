---
problem_id: "167"
title: "Two Sum II - Input Array Is Sorted"
platform: LeetCode
url: "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"
difficulty: Medium
track: High Value
primary_pattern: "[[Two Pointers]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 3m
first_attempt: 2026-08-15
last_attempt: 2026-08-15
next_review: 2026-08-16
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - two-pointers
  - medium
---

# Two Sum II - Input Array Is Sorted

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Two Pointers]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `[index1, index2]`, as an integer array of length 2.

The tests are generated such that there is **exactly one solution**. You may not use the same element twice.

Your solution **must use only constant extra space** $\mathcal{O}(1)$.

### Examples
```text
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3. We return [1, 3].

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

### Constraints
* `2 <= numbers.length <= 3 * 10^4`
* `-1000 <= numbers[i] <= 1000`
* `numbers` is sorted in non-decreasing order.
* `-1000 <= target <= 1000`
* Exactly one valid solution exists.

---

## My First Thought
We can use two pointers and the sum of those values, squeezing inward like in 3Sum. Since the array is sorted, `low` starts at `0` and `high` starts at `len(numbers) - 1`. If `numbers[low] + numbers[high] < target`, increment `low`; if greater, decrement `high`; if equal, return `[low + 1, high + 1]`.

---

## My Solution
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            val = numbers[low] + numbers[high]
            if val == target:
                return [low+1,high+1]
            if val < target:
                low += 1
            else:
                high -= 1
```

---

## Attempt Log & Metrics
* **Time Taken**: 3m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Uses two pointers `low` and `high` pointing to the start and end of the sorted array `numbers`. In a `while low < high` loop, calculates `val = numbers[low] + numbers[high]`. If `val == target`, returns 1-based indices `[low + 1, high + 1]`. If `val < target`, increments `low` to increase sum. Otherwise decrements `high` to decrease sum. Exactly one solution is guaranteed.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Two Pointers (Squeeze from ends)
* **Time Complexity**: `O(N)` — Single linear scan where `low` and `high` move towards each other at most $N$ steps total.
* **Space Complexity**: `O(1)` — Only two scalar pointers (`low`, `high`) and integer variable (`val`) used.

---

## Key Edge Cases
- [x] Negative target values (`numbers = [-1, 0]`, target `-1`) — Handled correctly.
- [x] Duplicate values (`numbers = [2, 3, 4]`, target `6`) — Returns `[1, 3]`.
- [x] Minimum length array ($N = 2$) — Loops once and returns.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-15 | Accepted | 3m | none | Grade A | Initial unassisted pass. Flawless 2-pointer squeeze. |

---

## AI Analysis
* **Grade**: **Grade A — Strong Independent Solution**
* **Correctness**: 100% correct logic and boundary condition. Correctly converts 0-indexed pointers to 1-indexed output `[low + 1, high + 1]`.
* **Complexity**: Optimal $O(N)$ Time & $O(1)$ Extra Space match expected benchmarks.
* **Pattern Verification**: Optimal Two-Pointer Squeeze pattern executed flawlessly. Avoided set/hashmap overhead.
* **Interview Readiness**: 10/10. Clean variable naming, optimal complexity, instantaneous pattern recognition.
