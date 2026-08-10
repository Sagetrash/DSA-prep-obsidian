# DSA Complexity & Pattern Quick Reference ⚡

Quick reference for data structure operations, time/space complexity expectations, and pattern recognition triggers during placement interviews.

---

## ⏱️ Big-O Time Complexity Expectations

| Input Size ($N$) | Max Allowed Complexity | Typical Algorithmic Patterns |
| :--- | :--- | :--- |
| $N \le 10$ | $O(N!)$ or $O(2^N)$ | Backtracking, Subsets, Permutations |
| $N \le 20$ | $O(2^N)$ | Bitmask DP, Recursion with Memoization |
| $N \le 100$ | $O(N^3)$ | 3-Loop Floyd-Warshall, Matrix Multiplication |
| $N \le 1,000$ | $O(N^2)$ | Dynamic Programming, Nested Loops, $O(N^2)$ Sorting |
| $N \le 10^5$ | $O(N \log N)$ or $O(N)$ | Sorting, Two Pointers, Binary Search, Hashmap, Sliding Window, Heap |
| $N \le 10^6$ | $O(N)$ or $O(N \log N)$ | Single pass Hashmap, Prefix Sum, Monotonic Stack |
| $N \ge 10^9$ | $O(\log N)$ or $O(1)$ | Binary Search on Answer, Mathematical Formula |

---

## 🎯 Pattern Recognition Cheat Sheet

| Symptom / Signal in Problem Statement | Primary Pattern | Key Data Structure |
| :--- | :--- | :--- |
| Sorted Array + Find target / pair | [[Binary Search]] / [[Two Pointers]] | Arrays, Pointers |
| Contiguous Subarray / Substring + Min/Max Length | [[Sliding Window]] | Hashmap / Hashset |
| Pair matching + $O(1)$ lookup | [[Arrays & Hashing]] | Hashmap / Hashset |
| LIFO order, Nested matching, Next Greater Element | [[Stack]] | Monotonic Stack |
| In-place linked list reversal, cycle detection | [[Linked List]] | Dummy head, Fast/Slow Pointers |
| Level-by-level traversal, shortest path unweighted | [[BFS & DFS]] | Queue (`collections.deque`) |
| Top $K$ elements, min/max stream | [[Heap & Priority Queue]] | Binary Heap (`heapq`) |
| Subproblems, counting ways, min/max cost | [[Dynamic Programming]] | 1D/2D DP table |
| Local optimal choices $\implies$ Global optimum | [[Greedy]] | Sorting / Heap |
