---
problem_id: "283"
title: "Move Zeroes"
platform: LeetCode
url: "https://leetcode.com/problems/move-zeroes/"
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
time_taken: 21m
first_attempt: 2026-08-09
last_attempt: 2026-08-09
next_review: 2026-08-10
confidence: 4
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - two-pointers
  - arrays
---

# Move Zeroes

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/move-zeroes/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Two Pointers]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade B`

---

## Problem Statement
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Notice that you must do this in-place without making a copy of the array.

### Examples
```text
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]
```

### Constraints
* `1 <= nums.length <= 10^4`
* `-2^31 <= nums[i] <= 2^31 - 1`

---

## My First Thought
> *"Find the first zero with a slow pointer, then use a fast pointer to locate non-zero elements and swap them forward. If a non-zero element is swapped into place, advance slow pointer on subsequent iteration."*

---

## My Solution
```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        while slow < len(nums) and nums[slow] != 0:
            slow += 1
        if not slow < len(nums):
            return
        fast = slow + 1
        while fast < len(nums) and slow < len(nums):
            if nums[slow] == 0:
                if nums[fast] != 0:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                else:
                    fast += 1
            else:
                slow += 1
```

---

## AI Analysis

### Code & Complexity Assessment
* **Correctness**: Functional and correct. In-place swaps correctly maintain relative non-zero ordering.
* **Submitted Time Complexity**: $\mathcal{O}(N)$ — Linear pass over array length $N$.
* **Submitted Space Complexity**: $\mathcal{O}(1)$ — In-place array modification.
* **Interview Readiness Grade**: **Grade B — Correct but Shaky Pointer State Control**
  * *Reasoning*: While functionally correct, the nested while loops rely on implicit state transitions across iterations (swapping without immediately incrementing pointers, relying on the next iteration's `else` branch). In interviews, a clean single-loop fast/slow pointer is expected.

### Refactored Canonical Solution (Clean Single Loop)
```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # slow tracks position for next non-zero element
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
```

---

## Review History

| Date | Result | Time Taken | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-09 | Accepted | 21m | none | Grade B | Solved independently in-place. Recommended refactoring to clean single-loop fast/slow pattern. |
