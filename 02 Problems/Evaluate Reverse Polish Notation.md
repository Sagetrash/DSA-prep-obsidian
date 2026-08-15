---
problem_id: "150"
title: "Evaluate Reverse Polish Notation"
platform: LeetCode
url: "https://leetcode.com/problems/evaluate-reverse-polish-notation/"
difficulty: Medium
track: High Value
primary_pattern: "[[Stack]]"
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
expected_space_complexity: "O(N)"
tags:
  - problem
  - leetcode
  - stack
  - medium
---

# Evaluate Reverse Polish Notation

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Stack]]
* **Status**: `Unsolved` | **Result**: `Pending`

---

## Problem Statement
You are given an array of strings `tokens` that represents an arithmetic expression in a **Reverse Polish Notation** (postfix expression).

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
* The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
* Each operand may be an integer or another expression.
* The division between two integers always **truncates toward zero**.
* There will not be any division by zero.
* The input represents a valid arithmetic expression in reverse polish notation.
* The answer and all intermediate calculations can be represented in a 32-bit integer.

### Examples
```text
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

### Constraints
* `1 <= tokens.length <= 10^4`
* `tokens[i]` is either an operator: `"+"`, `"-"`, `*`, or `"/"`, or an integer in the range `[-200, 200]`.

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
* **Optimal Pattern**: Stack evaluation for postfix notation
* **Time Complexity**: `O(N)` — Single pass over $N$ tokens.
* **Space Complexity**: `O(N)` — Stack stores up to $N/2 + 1$ operands.

---

## Key Edge Cases
- [ ] Division truncating toward zero (e.g. `int(a / b)` in Python vs `a // b`)
- [ ] Negative number operands (e.g. `"-11"`)
- [ ] Single element array (`tokens = ["18"]`)

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
