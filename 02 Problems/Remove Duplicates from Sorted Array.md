---
problem_id: "26"
title: "Remove Duplicates from Sorted Array"
platform: LeetCode
url: "https://leetcode.com/problems/remove-duplicates-from-sorted-array/"
difficulty: Easy
track: Volume
primary_pattern: "[[Two Pointers]]"
secondary_patterns:
  - "[[Arrays & Hashing]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 2m
first_attempt: 2026-08-09
last_attempt: 2026-08-09
next_review: 2026-08-10
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - two-pointers
  - arrays
---

# Remove Duplicates from Sorted Array

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Two Pointers]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade A`

---

## Problem Statement
Given an integer array `nums` sorted in **non-decreasing** order, remove the duplicates **in-place** such that each unique element appears only once. The **relative order** of the elements should be kept the same.

Return `k` after placing the final result in the first `k` slots of `nums`.

### Examples
```text
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

### Constraints
* `1 <= nums.length <= 3 * 10^4`
* `-100 <= nums[i] <= 100`
* `nums` is sorted in non-decreasing order.

---

## My First Thought
> *"Use fast and slow pointers. `slow` maintains the position of the last unique element found. Iterate `fast` across `nums`, and whenever `nums[fast] != nums[slow]`, advance `slow` and swap/overwrite `nums[slow] = nums[fast]`. Return `slow + 1`."*

---

## My Solution
```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
        return slow + 1
```

---

## AI Analysis

### Code & Complexity Assessment
* **Correctness**: Flawless implementation of the canonical fast/slow pointer pattern.
* **Submitted Time Complexity**: $\mathcal{O}(N)$ — Single pass through array length $N$.
* **Submitted Space Complexity**: $\mathcal{O}(1)$ — Pure in-place modification.
* **Interview Readiness Grade**: **Grade A — Strong Independent Solution**
  * *Reasoning*: Optimal time and space complexity, solved unassisted in under 3 minutes.

---

## Review History

| Date | Result | Time Taken | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-09 | Accepted | 2m | none | Grade A | Solved unassisted on 1st pass in 2.5m using fast/slow pointers. |
