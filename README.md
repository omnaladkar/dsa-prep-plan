# 8-Week DSA Prep Plan (30-45 min/day)

> **Rule of thumb each day:** 25 min attempt → if stuck, peek at approach only → finish → 5-10 min writing the "pattern trigger" in the Notes column.
>
> Progress tracker: check off ✅ as you go. Don't skip the Notes — that's what makes this stick.

---

## Progress Tracker

### Week 1: Arrays, Hashing, Prefix Sums
| Day | Problem | Status | Pattern Trigger |
|-----|---------|--------|-----------------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | ⬜ | value + target → hashmap |
| 2 | [Best Time to Buy/Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | ⬜ | track running min/max |
| 3 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | ⬜ | hashset for existence check |
| 4 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | ⬜ | prefix/suffix product |
| 5 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | ⬜ | running sum reset logic (Kadane's) |
| 6 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | ⬜ | prefix sum + hashmap count |
| 7 | **Review day** — redo Day 3 & 6 without notes | ⬜ | — |

### Week 2: Two Pointers & Sliding Window
| Day | Problem | Status | Pattern Trigger |
|-----|---------|--------|-----------------|
| 8 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | ⬜ | two pointers from ends |
| 9 | [3Sum](https://leetcode.com/problems/3sum/) | ⬜ | sort + two pointers |
| 10 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | ⬜ | two pointers, move smaller side |
| 11 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | ⬜ | sliding window + hashset |
| 12 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | ⬜ | variable sliding window + counts |
| 13 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | ⬜ | monotonic deque |
| 14 | **Review day** — redo Day 9 & 12 | ⬜ | — |

### Week 3: Linked Lists, Stacks, Queues
| Day | Problem | Status | Pattern Trigger |
|-----|---------|--------|-----------------|
| 15 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | ⬜ | iterative pointer swap |
| 16 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | ⬜ | slow/fast pointer (Floyd's) |
| 17 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | ⬜ | dummy node technique |
| 18 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | ⬜ | stack for matching pairs |
| 19 | [Min Stack](https://leetcode.com/problems/min-stack/) | ⬜ | stack tracking running min |
| 20 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | ⬜ | monotonic stack |
| 21 | **Review day** — redo Day 16 & 20 | ⬜ | — |

### Week 4: Trees (Part 1)
| Day | Problem | Status | Pattern Trigger |
|-----|---------|--------|-----------------|
| 22 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | ⬜ | basic DFS recursion |
| 23 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | ⬜ | DFS swap children |
| 24 | [Same Tree](https://leetcode.com/problems/same-tree/) | ⬜ | DFS compare structure |
| 25 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | ⬜ | BFS with queue |
| 26 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | ⬜ | DFS with min/max bounds |
| 27 | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | ⬜ | BST property traversal |
| 28 | **Review day** — redo Day 25 & 26 | ⬜ | — |

### Week 5: Trees (Part 2) + Graphs
| Day | Problem | Status | Pattern Trigger |
|-----|---------|--------|-----------------|
| 29 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | ⬜ | inorder traversal |
| 30 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | ⬜ | grid DFS/BFS |
| 31 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | ⬜ | DFS + hashmap of visited |
| 32 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | ⬜ | topological sort / cycle detection |
| 33 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | ⬜ | topological sort output order |
| 34 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | ⬜ | union-find template |
| 35 | **Review day** — redo Day 30 & 32 | ⬜ | — |

### Week 6: Dynamic Programming
| Day | Problem | Status | Pattern Trigger |
|-----|---------|--------|-----------------|
| 36 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | ⬜ | fibonacci-style DP |
| 37 | [House Robber](https://leetcode.com/problems/house-robber/) | ⬜ | 1D DP, adjacent constraint |
| 38 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | ⬜ | 1D DP, O(n²) then think O(n log n) |
| 39 | [Coin Change](https://leetcode.com/problems/coin-change/) | ⬜ | unbounded knapsack |
| 40 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | ⬜ | 2D DP grid |
| 41 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | ⬜ | 0/1 knapsack template |
| 42 | **Review day** — redo Day 37 & 41 | ⬜ | — |

### Week 7: Binary Search, Greedy, Heaps
| Day | Problem | Status | Pattern Trigger |
|-----|---------|--------|-----------------|
| 43 | [Binary Search](https://leetcode.com/problems/binary-search/) | ⬜ | template refresh |
| 44 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | ⬜ | modified binary search |
| 45 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | ⬜ | binary search on rotation point |
| 46 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | ⬜ | heap (or quickselect) |
| 47 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | ⬜ | heap + hashmap count |
| 48 | [Jump Game](https://leetcode.com/problems/jump-game/) | ⬜ | greedy reachability |
| 49 | **Review day** — redo Day 44 & 46 | ⬜ | — |

### Week 8: Mocks + Company-Tagged Only
| Day | Focus | Status |
|-----|-------|--------|
| 50 | Company-tagged problem #1 | ⬜ |
| 51 | Company-tagged problem #2 | ⬜ |
| 52 | Company-tagged problem #3 | ⬜ |
| 53 | Timed mock #1 (45 min, 1-2 problems) | ⬜ |
| 54 | Redo weakest topic #1 | ⬜ |
| 55 | Redo weakest topic #2 | ⬜ |
| 56 | Timed mock #2 | ⬜ |

---

## Weekly Ritual (Week 4+)
- **Every Sunday:** one 45-min timed mock instead of a regular problem
- **Keep a running "mistakes log"**: one line per bug or wrong first approach — review it for 10 min each Sunday → [Mistakes Log](docs/mistakes-log.md)

---

## How to Use This Repo

```
dsa-prep-plan/
├── README.md                          # This file — progress tracker
├── docs/
│   └── mistakes-log.md                # Running log of bugs & wrong approaches
├── templates/
│   └── solution_template.py           # Copy this into each day's folder
├── week01-arrays-hashing/
│   ├── day01/
│   │   ├── README.md                  # Problem statement + notes
│   │   └── solution.py                # Your solution
│   ├── day02/
│   │   ├── README.md
│   │   └── solution.py
│   └── ...
├── week02-two-pointers-sliding-window/
├── week03-linked-lists-stacks-queues/
├── week04-trees-part1/
├── week05-trees-part2-graphs/
├── week06-dynamic-programming/
├── week07-binary-search-greedy-heaps/
└── week08-mocks-company-tagged/
```

### Daily Workflow
1. Open the day's folder (e.g., `week01-arrays-hashing/day01/`)
2. Read `README.md` for the problem
3. Attempt for 25 min in `solution.py`
4. If stuck → peek at approach only → finish
5. Write the pattern trigger in the day's `README.md` under "Notes"
6. Commit with message: `day01: two-sum ✅`

---

## Useful References
- [NeetCode 150](https://neetcode.io/practice) — same core patterns, free video explanations
- [Blind 75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions) — the original curated list
- [LeetCode Company Tags](https://leetcode.com/company/) (Premium) or search "[Company] interview questions site:leetcode.com"
- [Pramp](https://www.pramp.com/) — free mock interviews
- [interviewing.io](https://interviewing.io/) — anonymous mock interviews
