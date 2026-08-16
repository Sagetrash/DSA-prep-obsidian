---
title: "Generate Parentheses"
leetcode_url: "https://leetcode.com/problems/generate-parentheses/"
neetcode_url: "https://neetcode.io/problems/generate-parentheses"
difficulty: Medium
track: Volume
primary_pattern: "[[Stack]]"
secondary_patterns: ["[[Backtracking]]"]
neetcode_number: 24
result: "Accepted"
hint_used: solution
independent_solves: 0
time_taken: "10m"
grade: "Grade D"
last_attempted: 2026-08-16
next_review: 2026-08-17
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

Maintain state to know when we can add brackets. If open, we can add open or close. Use recursion to explore all paths in decision tree.

---

## 🔍 My Reasoning & Approach

Decision tree backtracking using recursive DFS:
- Maintain state: `open_c` (count of open brackets used) and `close_c` (count of close brackets used).
- **Rule 1**: Add `(` if `open_c < n`.
- **Rule 2**: Add `)` if `close_c < open_c` (can only close if there is an unmatched open bracket).
- **Base Case**: `open_c == n and close_c == n` → valid combination of length $2N$, append `curr_s` to `res`.

---

## 💻 My Solution

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open_c, close_c, curr_s):
            if open_c == n and close_c == n:
                res.append(curr_s)
                return
            if open_c < n:
                dfs(open_c + 1, close_c, curr_s + "(")
            if close_c < open_c:
                dfs(open_c, close_c + 1, curr_s + ")")
        dfs(0, 0, "")
        return res
```

**Time Complexity**: $\mathcal{O}\left(\frac{4^N}{\sqrt{N}}\right)$ — Bounded by the $N$-th Catalan number $C_N = \frac{1}{N+1}\binom{2N}{N}$, each string construction takes $\mathcal{O}(N)$ time.
**Space Complexity**: $\mathcal{O}(N)$ — Maximum recursion stack depth is $2N$.

---

## 🤖 AI Analysis

### Complexity Verification
- **Actual TC**: $\mathcal{O}\left(\frac{4^N}{\sqrt{N}}\right)$
- **Actual SC**: $\mathcal{O}(N)$
- **Optimal TC**: $\mathcal{O}\left(\frac{4^N}{\sqrt{N}}\right)$ | **Optimal SC**: $\mathcal{O}(N)$

### Grade
**Grade**: Grade D | **Independent**: No | **Hints Used**: solution (AI provided boilerplate structure in chat)

### Key Insight
- Backtracking constraints prevent generating invalid parenthetical combinations (pruning invalid branches early).
- Passing immutable string concatenation (`curr_s + "("`) implicitly handles string backtracking via Python's call stack.

### Edge Cases Checked
- [x] `n = 1` → `["()"]`
- [x] `n = 8` (max constraint — recursion depth $16 \ll 1000$ limit)

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-16 | Accepted | 10m | solution | Grade D |
