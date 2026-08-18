---
title: "Subsets"
leetcode_url: "https://leetcode.com/problems/subsets/"
neetcode_url: "https://neetcode.io/problems/subsets"
difficulty: Medium
track: Volume
primary_pattern: "[[Backtracking]]"
secondary_patterns: []
neetcode_number: 71
result: "Accepted"
hint_used: none
independent_solves: 1
time_taken: "7m"
grade: "A"
last_attempted: 2026-08-18
next_review: 2026-08-21
mistakes: []
tags:
  - problem
  - backtracking
  - medium
---

# Subsets

**Difficulty**: Medium | **Track**: Volume | **Pattern**: [[Backtracking]]
**LeetCode**: [#78](https://leetcode.com/problems/subsets/) | **NeetCode**: [Link](https://neetcode.io/problems/subsets)

---

## 💭 My First Thought

At any time for element at index `i`, we can either include the element or not include it, creating a 2-way decision tree with $2^N$ total leaves.

---

## 🔍 My Reasoning & Approach

1. **Backtracking Decision Tree**:
   - At each index `i` of `nums`, make a binary decision: **Include `nums[i]`** or **Exclude `nums[i]`**.
2. **Base Case**:
   - When `i == len(nums)`, we have traversed a full branch of the decision tree. Append a copy of `sub` (`sub[:]`) to `res`.
3. **State Backtracking**:
   - `sub.append(nums[i])` $\to$ `dfs(i + 1)` (Include branch).
   - `sub.pop()` $\to$ backtrack state.
   - `dfs(i + 1)` (Exclude branch).

---

## 💻 My Solution

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        
        def dfs(i):
            if i == len(nums):
                res.append(sub[:])
                return
            
            # Choice 1: Include nums[i]
            sub.append(nums[i])
            dfs(i + 1)
            
            # Backtrack
            sub.pop()
            
            # Choice 2: Exclude nums[i]
            dfs(i + 1)
            
        dfs(0)
        return res
```

**Time Complexity**: $\mathcal{O}(N \cdot 2^N)$ — $2^N$ subsets total, copying each subset takes up to $\mathcal{O}(N)$ time.  
**Space Complexity**: $\mathcal{O}(N)$ — Recursion call stack depth up to $N$.

---

## 🤖 AI Analysis

### Code Analysis Checklist
1. **Correctness**: 100% correct implementation of 0/1 decision tree recursion.
2. **Complexity**: Optimal $\mathcal{O}(N \cdot 2^N)$ time and $\mathcal{O}(N)$ space.
3. **Pattern Verification**: Flawless unassisted execution of Backtracking decision tree.
4. **Key Takeaway**: The slice copy `sub[:]` is a clean, idiomatic Python equivalent to `sub.copy()`.

### Interview Readiness Grade
**Grade: A — Strong independent solution**
* Zero hints used. Solved in 7 minutes with clean, bug-free recursion and explicit backtrack state management. Mastery jump from Grade D $\to$ Grade A!

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-17 | Accepted | 12m | substantial | D |
| 2 | 2026-08-18 | Accepted | 7m | none | A |
