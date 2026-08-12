---
pattern_name: "Stack"
category: "Data Structures"
mastery_level: 5
attempted_count: 2
solved_count: 2
independent_solved_count: 2
hint_rate: "0%"
average_time: "6m 22s"
tags:
  - pattern
---

# Stack

## 🚨 Recognition Signals
* **Signals**: LIFO (Last-In-First-Out) evaluation, matching nested parentheses, monotonic stack for next greater/smaller element, expression evaluation.
* **Keywords**: "Valid parentheses", "Evaluate reverse polish notation", "Daily temperatures", "Next greater element".

---

## 💡 Core Idea & Intuition
Store elements in a stack to process contextually nested or reverse-order dependencies. Use monotonic stacks to maintain elements in sorted order to answer range queries in $O(N)$.

---

## 🛠️ Code Template / Mental Model

```python
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```
