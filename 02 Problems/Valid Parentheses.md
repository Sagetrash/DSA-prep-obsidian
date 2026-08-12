---
problem_id: "20"
title: "Valid Parentheses"
platform: LeetCode
url: "https://leetcode.com/problems/valid-parentheses/"
difficulty: Easy
track: High Value
primary_pattern: "[[Stack]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 5m 45s
first_attempt: 2026-08-12
last_attempt: 2026-08-12
next_review: 2026-08-15
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - leetcode
  - stack
---

# Valid Parentheses

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/valid-parentheses/)
* **Difficulty**: `Easy` | **Track**: `High Value`
* **Primary Pattern**: [[Stack]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-15`

---

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Examples
```text
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```

### Constraints
* `1 <= s.length <= 10^4`
* `s` consists of parentheses only `'()[]{}'`.

---

## My First Thought
Since I have done this before, I know I can just use a stack to put in starting parentheses, and when a closing parenthesis is found, we can pop the top.

---

## My Solution
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ']':'[',
            ')':'(',
            '}':'{',
        }
        for i in s:
            if i not in brackets:
                stack.append(i)
            else:
                if stack and stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
```

---

## Attempt Log & Metrics
* **Time Taken**: `5m 45s`
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `5`

---

## Reasoning & Explanation
The LIFO (Last-In-First-Out) property of a stack is ideal for matching nested structures like brackets. When an opening bracket is encountered, it is pushed onto the stack. When a closing bracket is encountered, it must match the most recently opened bracket (which is at the top of the stack). If the stack is empty when a closing bracket is found, or if the top of the stack does not match, the string is invalid. Finally, if the stack is non-empty after processing all characters, there are unclosed brackets, making the string invalid.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Stack]]
* **Time Complexity**: $\mathcal{O}(N)$ — Single pass through string of length $N$, all stack operations (push/pop) and dictionary lookups are $\mathcal{O}(1)$.
* **Space Complexity**: $\mathcal{O}(N)$ — Worst case space when all characters are opening brackets (e.g. `s = "((((("`).

---

## Key Edge Cases
- [x] Empty stack on closing bracket (e.g., `s = "]"` or `s = "()}"`) $\to$ Handled (`if stack and stack[-1] == brackets[i]`)
- [x] Mismatched bracket types (e.g., `s = "(]"`) $\to$ Handled
- [x] Leftover unclosed brackets (e.g., `s = "(()"`) $\to$ Handled (`if not stack: return True else: return False`)
- [x] Odd length string $\to$ Handled implicitly via loop and final stack check

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 5m 45s | none | Grade A | Flawless 1st-pass solution under benchmark time (10m). |

---

## AI Analysis
* **Grade**: `Grade A — Strong independent solution`
* **Edge Cases Missed**: None. Handled empty stack pops, mismatched types, and unclosed brackets cleanly.
* **Code Quality**: Clean, intuitive implementation. Python idiom tip: `return not stack` can concisely replace `if not stack: return True else: return False`.
* **Actionable Advice**: Excellent execution. Level 5/6 mastery achieved for basic stack bracket matching.
