---
title: "Generate Parentheses"
leetcode_url: "https://leetcode.com/problems/generate-parentheses/"
neetcode_url: "https://neetcode.io/problems/generate-parentheses"
difficulty: Medium
track: Volume
primary_pattern: "[[Stack]]"
secondary_patterns: ["[[Backtracking]]"]
neetcode_number: 24
result: ""
hint_used: none
independent_solves: 0
time_taken: ""
grade: ""
last_attempted: 2026-08-16
next_review: ""
mistakes: []
tags:
  - problem
  - stack
  - backtracking
  - medium
---

# Generate Parentheses

**Difficulty**: Medium | **Track**: Volume | **Pattern**: [[Stack]] / [[Backtracking]]
**LeetCode**: [#22](https://leetcode.com/problems/generate-parentheses/) | **NeetCode**: [Link](https://neetcode.io/problems/generate-parentheses)

---

## 📋 Problem Statement

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1:**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**
```
Input: n = 1
Output: ["()"]
```

**Constraints:**
- `1 <= n <= 8`

---

## 💭 My First Thought

*(Write here before attempting)*

---

## 🔍 My Reasoning & Approach

*(Step-by-step thought process, constraints checked, pattern identified)*

---

## 💻 My Solution

```python
# Write your solution here
```

**Time Complexity**: 
**Space Complexity**: 

---

## 🤖 AI Analysis

*(Auto-populated after submission)*

### Complexity Verification
- **Actual TC**: 
- **Actual SC**: 
- **Optimal TC**: $O(4^N / \sqrt{N})$ (Nth Catalan number × N for string construction) | **Optimal SC**: $O(N)$ (recursion depth)

### Grade
**Grade**: — | **Independent**: — | **Hints Used**: —

### Key Insight
**Decision tree backtracking with 2 rules**:
- Add `(` if `open_count < n`
- Add `)` if `close_count < open_count`
- Base case: `open_count == close_count == n` → valid combo, append to result

```python
def generateParentheses(n: int):
    result = []
    def dfs(open_c, close_c, current):
        if open_c == close_c == n:
            result.append(current)
            return
        if open_c < n:
            dfs(open_c + 1, close_c, current + "(")
        if close_c < open_c:
            dfs(open_c, close_c + 1, current + ")")
    dfs(0, 0, "")
    return result
```

**Why `close < open`?** — A closing paren is only valid if there's an unmatched open paren waiting.

### Cognitive Bridge to Backtracking Module
This problem is your first encounter with **backtracking on a decision tree**. The pattern generalizes:
- State = current partial solution
- Choices = valid next steps (constrained)
- Base case = complete valid solution
- Backtrack = return (Python garbage collects the string; explicit backtrack needed for mutable arrays)

### Edge Cases Checked
- [ ] `n = 1` → `["()"]`
- [ ] `n = 8` (max constraints — ensure recursion depth is fine)

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-16 | | | | |
