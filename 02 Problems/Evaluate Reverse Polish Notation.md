---
problem_id: "150"
title: "Evaluate Reverse Polish Notation"
platform: LeetCode
url: "https://leetcode.com/problems/evaluate-reverse-polish-notation/"
difficulty: Medium
track: High Value
primary_pattern: "[[Stack]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 4m
first_attempt: 2026-08-15
last_attempt: 2026-08-15
next_review: 2026-08-16
confidence: 5
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
* **Status**: `Solved` | **Result**: `Accepted`

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
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22
```

### Constraints
* `1 <= tokens.length <= 10^4`
* `tokens[i]` is either an operator: `"+"`, `"-"`, `*`, or `"/"`, or an integer in the range `[-200, 200]`.

---

## My First Thought
Iterate through the tokens and push operands onto a stack. When an operator is encountered, pop two values from the stack: `b` (operand2, right) and `a` (operand1, left). Perform `a op b` and push the result back onto the stack. At the end, return the final value left on the stack.

---

## My Solution
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = {
            "+": lambda a,b:a+b,
            "-": lambda a,b:a-b,
            "/": lambda a,b:int(a/b),
            "*": lambda a,b:a*b
        }
        stack = []
        for token in tokens:
            if not token in opr:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(opr[token](a,b))
        return stack.pop()
```

---

## Attempt Log & Metrics
* **Time Taken**: 4m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Defines an operator dictionary `opr` mapping operator symbols `"+", "-", "/", "*"` to lambda functions. Iterates over each `token` in `tokens`. If `token` is an operand (not in `opr`), converts it to `int` and appends to `stack`. If `token` is an operator, pops `b` (right operand) and `a` (left operand), evaluates `opr[token](a, b)` (using `int(a / b)` for zero truncation), and appends the result. Finally returns `stack.pop()`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: LIFO Stack Evaluation for Postfix Expression
* **Time Complexity**: `O(N)` — Single pass over `tokens` array of length $N$. Each push and pop is $O(1)$.
* **Space Complexity**: `O(N)` — Stack stores at most $N$ integers in worst case.

---

## Key Edge Cases
- [x] Division truncation towards zero (`int(-3 / 2) == 0`) — Correctly handled via `int(a / b)`.
- [x] Negative number strings (`"-11"`) — Correctly parsed by `int("-11")`.
- [x] Single element array (`tokens = ["18"]`) — Pushes `18` and returns `18`.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-15 | Accepted | 4m | none | Grade A | Initial unassisted solve. Elegant dictionary lambda implementation. |

---

## AI Analysis
* **Grade**: **Grade A — Strong Independent Solution**
* **Correctness**: 100% correct logic. Correct operand popping order `b = pop()`, `a = pop()`, and evaluation `a op b`.
* **Complexity**: Optimal $O(N)$ Time & $O(N)$ Space.
* **Pattern Verification**: Masterful LIFO Stack implementation. Clean use of Python dictionary lambdas.
* **Interview Readiness**: 10/10. Highly clean, pythonic, and production-ready code.
