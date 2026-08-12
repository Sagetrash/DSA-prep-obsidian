---
pattern_name: "Trees"
category: "Data Structures"
mastery_level: 5
attempted_count: 3
solved_count: 3
independent_solved_count: 2
hint_rate: "33%"
average_time: "3m 20s"
tags:
  - pattern
---

# Trees

## 🚨 Recognition Signals
* **Signals**: Hierarchical structure, recursive subtree evaluations, Binary Search Trees (BST), root-to-leaf paths, depth/height calculations.
* **Keywords**: "Maximum depth", "Invert binary tree", "Subtree of another tree", "Lowest common ancestor", "Path sum".

---

## 💡 Core Idea & Intuition
Break tree problems down recursively into subtree subproblems: evaluate left child, evaluate right child, combine results at root.

---

## 🛠️ Code Template / Mental Model

```python
def max_depth(root) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```
