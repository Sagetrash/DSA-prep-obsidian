---
problem_id: "155"
title: "Min Stack"
platform: LeetCode
url: "https://leetcode.com/problems/min-stack/"
difficulty: Medium
track: High Value
primary_pattern: "[[Stack]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 7m
first_attempt: 2026-08-12
last_attempt: 2026-08-12
next_review: 2026-08-15
confidence: 5
expected_time_complexity: "O(1)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - leetcode
  - stack
---

# Min Stack

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/min-stack/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Stack]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-15`

---

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
* `MinStack()` initializes the stack object.
* `void push(int val)` pushes the element `val` onto the stack.
* `void pop()` removes the element on the top of the stack.
* `int top()` gets the top element of the stack.
* `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

### Example
```text
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
```

### Constraints
* `-2^31 <= val <= 2^31 - 1`
* Methods `pop`, `top` and `getMin` will always be called on non-empty stacks.
* At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

---

## My First Thought
I'll just use two stacks: one normal stack and one `min_stack` that keeps the minimum element so far. On every push operation, we compare the new value to `min_stack` top; if it's less, we append the new value, otherwise we append the current minimum again to keep lengths synchronized.

---

## My Solution
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or self.min_stack[-1] > value:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

---

## Attempt Log & Metrics
* **Time Taken**: `7m`
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `5`

---

## Reasoning & Explanation
To retrieve the minimum element in $\mathcal{O}(1)$ time without searching through the stack, we maintain a secondary stack `min_stack` that records the minimum value at each depth of the primary stack. By keeping `min_stack` synchronized 1-to-1 in length with `stack`, popping from `stack` simply requires popping from `min_stack` as well. Thus `getMin()` is a simple $\mathcal{O}(1)$ peek (`self.min_stack[-1]`).

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Stack]] (1-to-1 Synchronized Stack pair)
* **Time Complexity**: $\mathcal{O}(1)$ for all operations (`push`, `pop`, `top`, `getMin`).
* **Space Complexity**: $\mathcal{O}(N)$ extra space for `min_stack`.

---

## Key Edge Cases
- [x] Duplicate minimum values (e.g. `push(2)`, `push(2)`) $\to$ Handled correctly (`else` branch appends current minimum again).
- [x] Negative values $\to$ Handled correctly.
- [x] Alternating push & pop sequences $\to$ Handled via synchronized pop operations.

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 7m | none | Grade A | Flawless 1st-pass solution under benchmark time (15m). |

---

## AI Analysis
* **Grade**: `Grade A — Strong independent solution`
* **Edge Cases Missed**: None. 1-to-1 stack synchronization handles duplicate minimums cleanly.
* **Code Quality**: Concise, readable, optimal Python.
* **Alternative Optimization**: Pushing tuples `(val, current_min)` onto a single stack avoids maintaining two separate list objects, though two lists is equally $\mathcal{O}(1)$ time & space.
* **Actionable Advice**: Outstanding implementation. Level 5/6 mastery.
