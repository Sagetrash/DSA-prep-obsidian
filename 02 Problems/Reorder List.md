---
problem_id: "143"
title: "Reorder List"
platform: LeetCode
url: "https://leetcode.com/problems/reorder-list/"
difficulty: Medium
track: High Value
primary_pattern: "[[Linked List]]"
secondary_patterns: ["[[Two Pointers]]"]
status: Solved
result: Accepted
attempts: 1
independent_solves: 0
hint_used: small
time_taken: 25m
first_attempt: 2026-08-18
last_attempt: 2026-08-18
next_review: 2026-08-19
confidence: 4
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - linked-list
  - medium
  - two-pointers
---

# Reorder List

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/reorder-list/) | [NeetCode](https://neetcode.io/problems/reorder-linked-list)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Linked List]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-19`

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
First thought was to make a stack from $N/2$ to $N$ and then use that to reorder the linked list. Pivoted to $\mathcal{O}(1)$ space in-place reversal: finding the midpoint using fast & slow pointers, reversing the second half, and interleaving nodes in-place.

---

## My Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = slow
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            mid = slow.next
        else:
            mid = slow
        
        # reverse second half of linked list
        prev = None
        curr = mid
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        ptr = head
        temp = prev
        while ptr:
            ptr.next, temp = temp, ptr.next
            ptr = ptr.next
```

---

## Attempt Log & Metrics
* **Time Taken**: 25m
* **Hint Used**: `small` (Prompted to optimize stack from $\mathcal{O}(N)$ space to $\mathcal{O}(1)$ space in-place reversal)
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 4

---

## Reasoning & Explanation
1. **Find Middle**: Used slow and fast pointer runner technique (`fast.next and fast.next.next`) to locate the midpoint node `mid`.
2. **In-place Reversal**: Reversed the second half starting at `mid` in $\mathcal{O}(N)$ time using `prev`, `curr`, `nxt` standard pointer swaps.
3. **Interleave Swap Trick**: Interleaved the first half (`head`) and reversed second half (`prev`) by executing simultaneous Python tuple unpacking `ptr.next, temp = temp, ptr.next`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Fast & Slow Pointers -> In-place List Reversal -> Node Interleaving
* **Time Complexity**: $\mathcal{O}(N)$ — Single pass for midpoint, single pass for reversal, single pass for interleaving.
* **Space Complexity**: $\mathcal{O}(1)$ — In-place pointer manipulation without stack/array allocation.

---

## Key Edge Cases
- [x] Single node (`[1]`) — Handled cleanly (reverses single node, leaves list intact).
- [x] Two nodes (`[1, 2]`) — Reorders correctly to `[1, 2]`.
- [x] Odd vs Even list lengths — Midpoint detection correctly partitions both odd (`5`) and even (`4` / `6`) length lists.

---

## Linked Mistakes
* Initial intuition used $\mathcal{O}(N)$ extra space stack instead of recognizing $\mathcal{O}(1)$ in-place reversal structure.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-18 | Accepted | 25m | small | Grade C | Correct with conceptual $\mathcal{O}(1)$ space hint |

---

## AI Analysis
* **Grade**: **Grade C — Correct with hints**
* **Correctness**: 100% correct logic. The Python tuple unpacking swap `ptr.next, temp = temp, ptr.next` is an ingenious, concise way to weave two lists.
* **Complexity**: Optimal $\mathcal{O}(N)$ Time and $\mathcal{O}(1)$ Space.
* **Interview Readiness**: Strong implementation mechanics. Practice recognizing $\mathcal{O}(1)$ space linked list patterns directly without needing an interviewer nudge.
