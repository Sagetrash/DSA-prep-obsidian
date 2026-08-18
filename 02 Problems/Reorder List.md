---
problem_id: "143"
title: "Reorder List"
platform: LeetCode
url: "https://leetcode.com/problems/reorder-list/"
difficulty: Medium
track: High Value
primary_pattern: "[[Linked List]]"
secondary_patterns: ["[[Two Pointers]]"]
status: Unsolved
result: Untested
attempts: 0
independent_solves: 0
hint_used: none
time_taken: 0m
first_attempt: null
last_attempt: null
next_review: 2026-08-18
confidence: 0
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - linked-list
  - medium
---

# Reorder List

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/reorder-list/) | [NeetCode](https://neetcode.io/problems/reorder-linked-list)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Linked List]]
* **Status**: `Unsolved` | **Result**: `Untested`
* **Next Review**: `2026-08-18`

---

## Problem Statement
You are given the head of a singly linked-list. The list can be represented as:
$$L_0 \to L_1 \to \dots \to L_{n - 1} \to L_n$$

Reorder the list to be on the following form:
$$L_0 \to L_n \to L_1 \to L_{n - 1} \to L_2 \to L_{n - 2} \to \dots$$

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

### Examples
```text
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

### Constraints
* The number of nodes in the list is in the range `[1, 5 * 10^4]`.
* `1 <= Node.val <= 1000`

---

## My First Thought
*(Write your initial approach & reasoning HERE BEFORE looking at solutions)*

---

## My Solution
```python
# Paste your code submission here
```

---

## Attempt Log & Metrics
* **Time Taken**: 
* **Hint Used**: `none` / `small` / `substantial` / `solution`
* **Result**: `Accepted` / `Wrong Answer` / `TLE`
* **Self Confidence (1–5)**: 

---

## Reasoning & Explanation
*(Explain WHY your code works and how the optimal pattern applies)*

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Fast & Slow Pointers (Find Mid) -> Reverse Second Half -> Interleave
* **Time Complexity**: `O(N)`
* **Space Complexity**: `O(1)`

---

## Key Edge Cases
- [ ] Single node (`head.next == None`)
- [ ] Two nodes (`head.next.next == None`)
- [ ] Odd vs Even list lengths

---

## Linked Mistakes
* None logged yet

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## AI Analysis
*(Pending user solution submission)*
