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
hint_used: substantial
independent_solves: 0
time_taken: "12m"
grade: "D"
last_attempted: 2026-08-17
next_review: 2026-08-18
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

I knew I wanted to use a brute-force approach to push all possible subsets, but I struggled to formulate how to structure the recursive choices and when to append the subsets to the result list.

---

## 🔍 My Reasoning & Approach

1. **Backtracking Decision Tree**:
   - At each index `i` of `nums`, make a binary decision: **Include `nums[i]`** or **Exclude `nums[i]`**.
2. **Base Case**:
   - When `i == len(nums)`, we have traversed a full branch of the decision tree. Append a copy of `curr_sub` (`curr_sub.copy()`) to `res`.
3. **State Backtracking**:
   - `curr_sub.append(nums[i])` $\to$ `dfs(i + 1)` (Include branch).
   - `curr_sub.pop()` $\to$ backtrack state.
   - `dfs(i + 1)` (Exclude branch).

---

## 💻 My Solution

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_sub = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(curr_sub.copy())
                return
            
            # Choice 1: Include nums[i]
            curr_sub.append(nums[i])
            dfs(i + 1)
            
            # Backtrack
            curr_sub.pop()
            
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
3. **Pattern Verification**: Core foundational pattern for all Combinate/Subset Backtracking problems.
4. **Key Takeaway**: Always remember `res.append(curr_sub.copy())` instead of `res.append(curr_sub)`. In Python, lists are passed by reference, so appending without `.copy()` yields a list of empty lists at the end!

### Interview Readiness Grade
**Grade: D — Required substantial assistance / solution template**
* Needed structural guidance on formulating the decision tree and base case trigger. Scheduled for 1-day unassisted re-drill.

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-17 | Accepted | 12m | substantial | D |

