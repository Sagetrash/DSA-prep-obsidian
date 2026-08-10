---
problem_id: "217"
title: "Contains Duplicate"
platform: LeetCode
url: "https://leetcode.com/problems/contains-duplicate/"
difficulty: Easy
track: Volume
primary_pattern: "[[Arrays & Hashing]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 6m
first_attempt: 2026-08-08
last_attempt: 2026-08-08
next_review: 2026-08-09
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - leetcode
  - arrays
  - volume
---

# Contains Duplicate

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/contains-duplicate/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Arrays & Hashing]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Examples
```text
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
```

### Constraints
* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

---

## My First Thought
Convert the array to a set using `set(nums)`. Since sets strip out duplicate values, if `len(set(nums)) < len(nums)`, then at least one duplicate existed and we can return `True`, otherwise `False`.

---

## My Solution
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        if len(numsSet) < len(nums):
            return True
        return False
```

---

## Attempt Log & Metrics
* **Time Taken**: 3m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Constructs a hash set from `nums`. The set constructor strips out duplicate elements in average $O(N)$ time. Comparing the length of the resulting set with the original array length detects duplicates immediately.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Hash Set length comparison / early-exit lookup
* **Time Complexity**: `O(N)` — Single pass C-level hash table insertion for $N$ elements.
* **Space Complexity**: `O(N)` — Stores up to $N$ unique elements in hash set.

---

## Key Edge Cases
- [x] All unique elements `[1, 2, 3, 4]` $\implies$ `False`.
- [x] Duplicates present `[1, 2, 3, 1]` $\implies$ `True`.
- [x] Single element `[1]` $\implies$ `False`.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-08 | Accepted | 3m | none | Grade A | Fast 1-line set length comparison. |

---

## AI Analysis
* **Grade**: **Grade A — Strong Independent Solution**
* **Correctness**: 100% correct logic.
* **Complexity**: $O(N)$ Time, $O(N)$ Space.
* **Micro-Optimizations**:
  1. **Direct Boolean Return**: Simplify `if len(set(nums)) < len(nums): return True; return False` to `return len(set(nums)) < len(nums)`.
  2. **Early-Exit Alternative**: A manual loop with a `seen` set allows early termination if duplicate appears near start of array (Best Case $O(1)$ Time):
     ```python
     class Solution:
         def containsDuplicate(self, nums: List[int]) -> bool:
             seen = set()
             for num in nums:
                 if num in seen:
                     return True
                 seen.add(num)
             return False
     ```
