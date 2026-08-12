---
problem_id: "141"
title: "Linked List Cycle"
platform: LeetCode
url: "https://leetcode.com/problems/linked-list-cycle/"
difficulty: Easy
track: Volume
primary_pattern: "[[Linked List]]"
secondary_patterns:
  - "[[Two Pointers]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 3m
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
  - fast-slow-pointers
---

# Linked List Cycle

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/linked-list-cycle/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Linked List]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-15`

---

## Problem Statement
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Examples
```text
Input: head = [3,2,0,-4], pos = 1
Output: true

Input: head = [1,2], pos = 0
Output: true

Input: head = [1], pos = -1
Output: false
```

### Constraints
* Number of nodes in list is in range `[0, 10^4]`.
* `-10^5 <= Node.val <= 10^5`
* `pos` is `-1` or a valid index in the linked list.

---

## My First Thought
Use two pointers, `slow` and `fast`. `fast` moves two steps at a time while `slow` moves one step. If they ever collide, the linked list has a cycle. If `fast` reaches `None`, there is no cycle, so return `False`.

---

## My Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast != None:
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
                continue
            if slow:
                slow = slow.next
            if slow == fast:
                return True
        return False
```

---

## Attempt Log & Metrics
* **Time Taken**: `3m`
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `5`

---

## Reasoning & Explanation
Using Floyd's Cycle-Finding Algorithm (Tortoise and Hare), if there is a cycle, the distance between the `fast` pointer (moving 2 steps/iter) and `slow` pointer (moving 1 step/iter) decreases by 1 in every iteration until they inevitably meet. If no cycle exists, `fast` reaches the end (`None`) in $\mathcal{O}(N)$ operations.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Linked List]] (Floyd's Fast & Slow Pointers)
* **Time Complexity**: $\mathcal{O}(N)$ — Linear pass; if a cycle exists, `fast` catches `slow` within 1 cycle loop.
* **Space Complexity**: $\mathcal{O}(1)$ — Uses only two pointer references (`slow` and `fast`).

---

## Key Edge Cases
- [x] Empty list (`head = None`) $\to$ Handled (`while fast != None` fails, returns `False`).
- [x] Single node no cycle (`head = [1], pos = -1`) $\to$ Handled (`fast.next` is `None`, exits loop, returns `False`).
- [x] Two nodes cyclic (`head = [1, 2], pos = 0`) $\to$ Handled (`slow == fast` meets on 2nd iteration).

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 3m | none | Grade A | Flawless 1st-pass Floyd's cycle detection in 3m. |

---

## AI Analysis
* **Grade**: `Grade A — Strong independent solution`
* **Idiomatic Refactoring Tip**:
  Standard Python loop condition `while fast and fast.next:` avoids internal `if/else/continue` checks:
  ```python
  class Solution:
      def hasCycle(self, head: Optional[ListNode]) -> bool:
          slow = fast = head
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
              if slow == fast:
                  return True
          return False
  ```
* **Actionable Advice**: Excellent execution. Level 5/6 mastery for Floyd's Cycle Detection.
