---
mistake_name: "Subtree Recursion Scope Error"
category: "Logic Error"
occurrences: 1
severity: "Medium"
tags:
  - mistake
  - logic-error
  - trees
---

# Subtree Recursion Scope Error

## 📌 Description & Root Cause
Calling an exact-match helper function (like `isSameTree`) on immediate child nodes (`root.left`, `root.right`) instead of calling the main recursive function (`isSubtree`). This limits depth traversal to 1 level below `root` instead of exploring all deeper levels of the tree.

---

## 🛡️ Prevention Rule & Mental Checklist
- [ ] When searching for a matching subtree at **any** depth, ensure the outer recursive call delegates to `isSubtree(root.left, subRoot)` so deeper descendents are explored.
- [ ] Ask: *"Does `isSameTree(root.left, subRoot)` search 2+ levels deep?"* No, `isSameTree` assumes the current node is the root of the match.

---

## 💻 Anti-Pattern vs Correct Pattern

### ❌ Incorrect Code Snippet
```python
# Only checks root, root.left, and root.right; fails for subtrees at depth >= 2
return self.isSameTree(root, subRoot) or self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot)
```

### ✅ Correct Code Snippet
```python
# Recursively searches all nodes in the tree
return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

---

## 🔗 Problems Where This Mistake Occurred
```dataview
TABLE title, difficulty, track, result, primary_pattern
FROM "02 Problems"
WHERE contains(file.outlinks, this.file.link)
```
