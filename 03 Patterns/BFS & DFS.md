---
pattern_name: "BFS & DFS"
category: "Algorithmic Pattern"
mastery_level: 3
attempted_count: 1
solved_count: 1
independent_solved_count: 0
hint_rate: "100%"
average_time: "8m 35s"
tags:
  - pattern
---

# BFS & DFS

## 🚨 Recognition Signals
* **Signals**: Level-order traversal, shortest path in unweighted graphs/grids, connected components, graph traversal, flood fill.
* **Keywords**: "Level order traversal", "Number of islands", "Shortest path", "Rotting oranges", "Word ladder".

---

## 💡 Core Idea & Intuition
* **BFS (Breadth-First Search)**: Uses a Queue (`collections.deque`) to explore nodes level-by-level (guarantees shortest path in unweighted graphs).
* **DFS (Depth-First Search)**: Uses Recursion or a Stack to explore deep paths before backtracking.

---

## 🛠️ Code Template / Mental Model

### BFS Level Order Traversal
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(level)
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
