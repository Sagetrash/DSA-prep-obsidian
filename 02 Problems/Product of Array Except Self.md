---
problem_id: "238"
title: "Product of Array Except Self"
platform: LeetCode
url: "https://leetcode.com/problems/product-of-array-except-self/"
difficulty: Medium
track: High Value
primary_pattern: "[[Arrays & Hashing]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 3
independent_solves: 3
hint_used: none
time_taken: 12m 14s
first_attempt: 2026-08-08
last_attempt: 2026-08-14
next_review: 2026-08-21
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - arrays
  - prefix-sum
---

# Product of Array Except Self

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/product-of-array-except-self/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Arrays & Hashing]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(N)` time and without using the division operation.

### Examples
```text
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

### Constraints
* `2 <= nums.length <= 10^4`
* `-30 <= nums[i] <= 30`
* The product of any prefix or suffix fits in 32-bit integer.

---

## My First Thought
Since I need the product of all elements except self for each index `i`, I can use a prefix product array and a postfix (suffix) product array. `answer[i]` will equal the prefix product of all elements to the left of `i` multiplied by the postfix product of all elements to the right of `i`.

---

## My Solution
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in nums]
        n = len(nums)
        for i in range(n):
            if i == 0:
                continue
            res[i] = res[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        return res
```

---

## Attempt Log & Metrics
* **Time Taken**: 11m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Constructs prefix products directly into output array `res`. Uses a single scalar integer `postfix` running variable during backward iteration to multiply prefix product by suffix product in-place, achieving optimal $O(1)$ extra space complexity.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Prefix & Suffix Products with Scalar Accumulator
* **Time Complexity**: `O(N)` — Two linear passes over array of size $N$.
* **Space Complexity**: `O(1)` — Only uses a single scalar `postfix` integer variable (output array `res` does not count towards extra space complexity).

---

## Key Edge Cases
- [x] Contains single zero `nums = [-1, 1, 0, -3, 3]` $\implies$ Output is `[0, 0, 9, 0, 0]`.
- [x] Contains multiple zeros `nums = [0, 0]` $\implies$ Output is `[0, 0]`.
- [x] Negative elements `nums = [-1, -2, -3]` $\implies$ Correct sign handling.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-08 | Accepted | 11m | none | Grade A | Solved independently via prefix/postfix array multiplication. |
| 2026-08-08 | Accepted | 11m | none | Grade A | Refactored to O(1) extra space scalar postfix approach. |
| 2026-08-14 | Accepted | 12m 14s | none | Grade A | Mock OA 1 timed solve (12m 14s prefix/postfix pass). |

---

## AI Analysis
* **Grade**: **Grade A — Excellent Production & Interview Quality**
* **Correctness**: 100% correct logic and clean boundary handling.
* **Complexity**: $O(N)$ Time & $O(1)$ Extra Space — Fully optimal!
