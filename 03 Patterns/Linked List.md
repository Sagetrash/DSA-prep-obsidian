---
pattern_name: "Linked List"
category: "Data Structures"
mastery_level: 1
attempted_count: 0
solved_count: 0
independent_solved_count: 0
hint_rate: "0%"
average_time: "0m"
tags:
  - pattern
---

# Linked List

## 🚨 Recognition Signals
* **Signals**: Pointer manipulation, dummy head nodes, fast & slow pointers (Floyd's Cycle Detection / Middle node), in-place list reversal.
* **Keywords**: "Reverse linked list", "Merge two sorted lists", "Linked list cycle", "Remove Nth node from end".

---

## 💡 Core Idea & Intuition
Manage pointer references without losing track of downstream nodes. Always utilize a `dummy` head node to eliminate edge cases around empty lists or head node modifications.

---

## 🛠️ Code Template / Mental Model

### In-Place Reversal
```python
def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```
