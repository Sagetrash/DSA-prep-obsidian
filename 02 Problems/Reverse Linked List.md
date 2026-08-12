---
problem_id: "206"
title: "Reverse Linked List"
platform: LeetCode
url: "https://leetcode.com/problems/reverse-linked-list/"
difficulty: Easy
track: High Value
primary_pattern: "[[Linked List]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 11m
first_attempt: 2026-08-12
last_attempt: 2026-08-12
next_review: 2026-08-15
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - linked-list
---

# Reverse Linked List

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/reverse-linked-list/)
* **Difficulty**: `Easy` | **Track**: `High Value`
* **Primary Pattern**: [[Linked List]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-15`

---

## Problem Statement
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

### Examples
```text
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
```

### Constraints
* Number of nodes in list is in range `[0, 5000]`.
* `-5000 <= Node.val <= 5000`

---

## My First Thought
I could use three pointers: `prev`, `curr`, and `next`. As we traverse the linked list, `next` would store `curr.next`, then we set `curr.next` to `prev`, after which we move `prev` to `curr` and `curr` to `next`.

---

## My Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Curr = head
        Prev = None 
        while Curr != None:
            Next = Curr.next
            Curr.next = Prev
            Prev = Curr
            Curr = Next
        return Prev
```

---

## Attempt Log & Metrics
* **Time Taken**: `11m`
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `5`

---

## Reasoning & Explanation
Reversing a singly linked list in-place requires reversing the direction of each node's `next` pointer. Since changing `curr.next` overwrites the link to the rest of the list, we must temporarily cache `curr.next` in a `Next` pointer before mutating `curr.next = Prev`. After redirecting the pointer backwards, we advance `Prev` to `Curr` and `Curr` to `Next`. Once `Curr` becomes `None` (reaching the end of the original list), `Prev` points to the new head of the reversed list.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Linked List]] (In-Place Pointer Reversal)
* **Time Complexity**: $\mathcal{O}(N)$ — Single linear pass visiting each node exactly once.
* **Space Complexity**: $\mathcal{O}(1)$ — In-place pointer manipulation using scalar pointer variables.

---

## Key Edge Cases
- [x] Empty list (`head = None`) $\to$ Handled (`while Curr != None:` fails immediately, returns `Prev` which is `None`).
- [x] Single node list (`head = [1]`) $\to$ Handled (`Next = None`, `Curr.next = None`, `Prev` becomes node 1, returns node 1).
- [x] Two node list (`head = [1, 2]`) $\to$ Handled correctly.

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 11m | none | Grade A | Flawless in-place 3-pointer iterative reversal. |

---

## AI Analysis
* **Grade**: `Grade A — Strong independent solution`
* **Edge Cases Missed**: None. Handled empty list `head = None` and single node cleanly.
* **Code Quality**: Clean, explicit, optimal. Python naming convention tip: Use snake_case (`curr`, `prev`, `nxt`) for local variables rather than Capitalized names (`Curr`, `Prev`, `Next`) to adhere to PEP 8 standards.
* **Actionable Advice**: Excellent 3-pointer execution. Level 5/6 mastery achieved for Linked List reversal.
