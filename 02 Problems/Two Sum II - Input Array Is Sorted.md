---
problem_id: "167"
title: "Two Sum II - Input Array Is Sorted"
platform: LeetCode
url: "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"
difficulty: Medium
track: High Value
primary_pattern: "[[Two Pointers]]"
secondary_patterns: []
status: Unsolved
result: Pending
attempts: 0
independent_solves: 0
hint_used: none
time_taken: "-"
first_attempt: null
last_attempt: null
next_review: null
confidence: 0
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
* **Status**: `Unsolved` | **Result**: `Pending`

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
*(Pending submission)*

---

## My Solution
```python
# Pending solution
```

---

## Attempt Log & Metrics
* **Time Taken**: -
* **Hint Used**: `none`
* **Result**: `Pending`
* **Self Confidence (1–5)**: -

---

## Reasoning & Explanation
*(Pending submission)*

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Two Pointers (Squeeze from ends)
* **Time Complexity**: `O(N)` — Linear scan with two pointers moving towards each other.
* **Space Complexity**: `O(1)` — Only constant extra variables for left and right pointers.

---

## Key Edge Cases
- [ ] Negative target values (`numbers = [-10, -5, -2, 0]`, target `-7`)
- [ ] Two identical numbers (`numbers = [0, 0, 3, 4]`, target `0`)
- [ ] Elements at extreme bounds ($N = 3 \cdot 10^4$)

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## AI Analysis
*(Pending completion)*
