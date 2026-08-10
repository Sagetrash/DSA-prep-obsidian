---
review_date: {{date}}
problems_reviewed: 0
passed_count: 0
failed_count: 0
tags:
  - review-session
---

# Review Session — {{date}}

## 📋 Problems Queued For Review

```dataview
TABLE difficulty, track, result, hint_used, last_attempt, next_review
FROM "02 Problems"
WHERE next_review <= date(today) AND status != "Unsolved"
SORT next_review ASC
```

---

## 📝 Review Log & Re-Attempt Results

| Problem Link | Previous Result | Today's Result | Time Taken | Today's Hint Level | New Next Review | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

---

## 🧠 Memory Decay & Retention Notes
* **Patterns Retained**: 
* **Patterns Fading**: 
* **Adjustments Needed**: 
