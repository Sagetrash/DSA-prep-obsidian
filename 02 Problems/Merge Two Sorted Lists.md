---
problem_id: "21"
title: "Merge Two Sorted Lists"
platform: LeetCode
url: "https://leetcode.com/problems/merge-two-sorted-lists/"
difficulty: Easy
track: Volume
primary_pattern: "[[Linked List]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 5m 42s
first_attempt: 2026-08-12
last_attempt: 2026-08-12
next_review: 2026-08-15
confidence: 5
expected_time_complexity: "O(N + M)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - linked-list
---

# Merge Two Sorted Lists

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Linked List]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-15`

---

## Problem Statement
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Examples
```text
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
```

### Constraints
* Number of nodes in both lists is in range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both lists are sorted in non-decreasing order.

---

## My First Thought
Create a new head `ListNode()` object, and iteratively check `list1` and `list2`, adding the smaller element to the new linked list.

---

## My Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 or list2:
            if not list1 and not list2:
                return dummy
            if not list1:
                tail.next = list2
                break
            if not list2:
                tail.next = list1
                break
            if list1.val > list2.val:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            else:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            tail = tail.next
        return dummy.next
```

---

## Attempt Log & Metrics
* **Time Taken**: `5m 42s`
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `5`

---

## Reasoning & Explanation
Using a `dummy` head node avoids checking special conditional branches when creating the merged list head. While both `list1` and `list2` have nodes, we compare their current values and append the smaller node to `tail.next`. Once one list becomes empty, we directly link `tail.next` to the remaining non-empty list and break. Returning `dummy.next` yields the merged list head.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Linked List]] (Dummy Head Iterative Merge)
* **Time Complexity**: $\mathcal{O}(N + M)$ — Single pass traversing nodes in both lists.
* **Space Complexity**:
  * **Current Code**: $\mathcal{O}(N + M)$ — Allocating `ListNode(val)` creates new nodes.
  * **In-Place Optimization**: $\mathcal{O}(1)$ auxiliary space by directly attaching existing nodes (`tail.next = list1` / `tail.next = list2`).

---

## Key Edge Cases
- [x] Both lists empty (`list1 = [], list2 = []`) $\to$ Handled (`dummy.next = None`).
- [x] One list empty (`list1 = [], list2 = [0]`) $\to$ Handled (`tail.next = list2`).
- [x] Equal node values (`list1.val == list2.val`) $\to$ Handled (`else` branch handles ties).

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 5m 42s | none | Grade A | Flawless 1st-pass solution under benchmark time (10m). |

---

## AI Analysis
* **Grade**: `Grade A — Strong independent solution`
* **Optimization Tip**:
  Rather than instantiating new nodes (`ListNode(list1.val)`), splice the existing nodes directly in-place:
  ```python
  class Solution:
      def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
          dummy = tail = ListNode()
          while list1 and list2:
              if list1.val <= list2.val:
                  tail.next = list1
                  list1 = list1.next
              else:
                  tail.next = list2
                  list2 = list2.next
              tail = tail.next
          tail.next = list1 or list2
          return dummy.next
  ```
  This reduces auxiliary space from $\mathcal{O}(N + M)$ to $\mathcal{O}(1)$.
* **Actionable Advice**: Outstanding job. Level 5/6 mastery.
