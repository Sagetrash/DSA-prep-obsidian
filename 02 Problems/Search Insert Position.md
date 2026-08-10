---
problem_id: "35"
title: "Search Insert Position"
platform: LeetCode
url: "https://leetcode.com/problems/search-insert-position/"
difficulty: Easy
track: Volume
primary_pattern: "[[Binary Search]]"
secondary_patterns:
  - "[[Arrays & Hashing]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 11m
first_attempt: 2026-08-08
last_attempt: 2026-08-08
next_review: 2026-08-09
confidence: 5
expected_time_complexity: "O(log N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - binary-search
  - volume
---

# Search Insert Position

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/search-insert-position/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Binary Search]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log N)` runtime complexity.

### Examples
```text
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
```

### Constraints
* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `nums` contains **distinct** values sorted in **ascending** order.
* `-10^4 <= target <= 10^4`

---

## My First Thought
Use binary search to find the target in $O(\log N)$ time. If the target is not found in the array, the pointers will adjust such that `left` naturally ends up at the exact index where `target` should be inserted.

---

## My Solution
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
```

---

## Attempt Log & Metrics
* **Time Taken**: 3m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Standard binary search setup. Halves search domain on each iteration. If `target` matches `nums[mid]`, returns `mid`. When loop terminates (`low > high`), `low` marks the insertion boundary where all elements before it are `< target` and all elements from `low` onwards are `> target`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Binary Search
* **Time Complexity**: `O(log N)` — Halves array of length $N$ on each iteration.
* **Space Complexity**: `O(1)` — Uses standard two-pointer variables `low` and `high`.

---

## Key Edge Cases
- [x] Target smaller than all elements (`target = 0`, `nums = [1, 3, 5]`) $\implies$ Returns `0`.
- [x] Target larger than all elements (`target = 7`, `nums = [1, 3, 5]`) $\implies$ Returns `3`.
- [x] Target present in array (`target = 5`) $\implies$ Returns exact index `2`.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-08 | Accepted | 11m | none | Grade A | Solved independently via standard binary search pointer termination. |

---

## AI Analysis
* **Grade**: **Grade A — Strong Independent Solution**
* **Correctness**: 100% correct logic and clean overflow-safe mid calculation `low + (high - low)//2`.
* **Complexity**: $O(\log N)$ Time, $O(1)$ Space.
