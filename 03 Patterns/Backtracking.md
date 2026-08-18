---
pattern_name: "Backtracking"
category: "Algorithmic Pattern"
mastery_level: 3
attempted_count: 3
solved_count: 3
independent_solved_count: 0
hint_rate: "100%"
average_time: "17m"
tags:
  - pattern
  - backtracking
---

# Backtracking

## 🚨 Recognition Signals
* **Signals**: Problems requiring finding all possible combinations, permutations, subsets, or valid configurations where decisions are made incrementally.
* **Keywords**: "Find all combinations", "Generate all subsets", "Permutations", "N-Queens", "Sudoku solver".
* **Constraint Triggers**: Small input sizes ($N \le 15 \dots 30$), pointing to exponential time complexity $\mathcal{O}(2^N)$ or $\mathcal{O}(N!)$.

---

## 💡 Core Idea & Intuition
Build solutions incrementally via Depth-First Search (DFS) on a decision tree. At each step:
1. **Choose**: Make a decision (add element to path or current subset).
2. **Explore**: Recurse down the branch to evaluate deeper decisions.
3. **Unchoose (Backtrack)**: Revert the decision (`curr.pop()` or restore state) before trying the next choice.

---

## 🛠️ Code Template / Mental Model

### Pattern 1: Subsets / Combinations (Include vs Exclude)
```python
def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    
    def dfs(i, curr):
        if i == len(nums):
            res.append(curr.copy())
            return
        
        # Choice 1: Include nums[i]
        curr.append(nums[i])
        dfs(i + 1, curr)
        curr.pop() # Backtrack step
        
        # Choice 2: Exclude nums[i]
        dfs(i + 1, curr)
        
    dfs(0, [])
    return res
```

### Pattern 2: Combination Sum (Element Reuse Allowed)
```python
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    
    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        if total > target or i == len(candidates):
            return
        
        # Choice 1: Include candidates[i] (can reuse index i)
        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])
        curr.pop() # Backtrack step
        
        # Choice 2: Exclude candidates[i] (move to i + 1)
        dfs(i + 1, curr, total)
        
    dfs(0, [], 0)
    return res
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```

* **Mastery Level**: `3 / 6` (Can solve with structural/backtrack cleanup hints)
* **Evidence Summary**: Solved 3 Backtracking Medium problems (`Generate Parentheses`, `Combination Sum`, `Subsets`). Common friction point is state tracking & remembering explicit `curr.pop()` cleanup.

---

## ⚠️ Systemic Weaknesses & Pitfalls
* **State Mutation**: Forgetting `curr.pop()` when mutating a shared list across recursion.
* **Index Control**: Confusing index increment `i + 1` (no reuse allowed) with same index `i` (reuse allowed).
* **Copying Results**: Appending `res.append(curr)` instead of `res.append(curr.copy())` or `res.append(list(curr))`.
