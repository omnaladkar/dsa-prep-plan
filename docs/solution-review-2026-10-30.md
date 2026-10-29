# DSA Solution Review (30 Oct 2026)

Reviewed every solution file and README in this repo (43 commits, 31 Aug to 22 Oct 2026).

## Where you are

- **Solved:** 40 of 49 problems, all in C++ (saved inside `.py` files).
- **Not done:** Day 5 Maximum Subarray file is empty (the Kadane code sits in the Day 4 file), Day 19 Min Stack, Day 31 Clone Graph, Day 48 Jump Game.
- **Skipped:** every review day (7, 14, 21, 28, 35, 42, 49) and all of Week 8 (company-tagged + timed mocks).
- **Never filled in:** the Pattern Trigger, Approach and Time/Space Complexity in any file, the "Mistakes / Gotchas" in any README, and `docs/mistakes-log.md`.
- **Last commit:** 22 Oct (8 days ago).

The code itself is mostly correct. The gap is interview behaviour: in a live round you must say the brute force, the pattern, and the complexity before coding. Your repo has none of that written down, so it has never been practised.

## Problem-by-problem

| Day | Problem | Verdict | What an interviewer would push on |
| --- | --- | --- | --- |
| 1 | Two Sum | Good | - |
| 2 | Best Time to Buy/Sell | Good | - |
| 3 | Contains Duplicate | OK | `set` is O(log n) per insert; use `unordered_set` and return early on the first repeat |
| 4 | Product Except Self | **Redo** | Uses division, which the problem forbids. Learn prefix/suffix products, O(1) extra space |
| 5 | Maximum Subarray | **Redo** | File empty; Kadane code is in Day 4's file. Move it and explain why resetting works |
| 6 | Subarray Sum Equals K | **Redo** | O(n²) brute force. The point was prefix sum + hashmap count, O(n). Handle negatives |
| 8 | Valid Palindrome | OK | Builds a copy (O(n) space). Interviewers want two pointers skipping non-alnum in place |
| 9 | 3Sum | OK | Hashmap version, O(n² log n). Learn sort + two pointers, the pattern this day targeted |
| 10 | Container With Most Water | Good | Be ready to prove why moving the shorter side is safe |
| 11 | Longest Substring No Repeat | Good | Know the last-index map version that jumps `i` forward |
| 12 | Minimum Window Substring | Good | Strong. Explain the `count` trick out loud |
| 13 | Sliding Window Maximum | **Redo** | Multiset is O(n log k). Expected answer is a monotonic deque, O(n) |
| 15-18, 20 | Lists, parentheses, temperatures | Good | Day 17: mention you free the dummy node; Day 20: say why it's O(n) amortised |
| 19 | Min Stack | **Missing** | Common in machine-coding warm-ups. Do it (two stacks or pair stack) |
| 22-25, 27 | Tree basics, LCA of BST | Good | Day 25: the single-node special case is unnecessary |
| 26 | Validate BST | OK | Inorder into a vector is O(n) space. Also know the min/max bounds version (use `long` for INT_MIN/INT_MAX) |
| 29 | Kth Smallest in BST | OK | Stop the inorder at k instead of collecting all nodes |
| 30 | Number of Islands | OK | Style differs from your other files. Rewrite it yourself from a blank page, and know the BFS version |
| 31 | Clone Graph | **Missing** | Do it: DFS/BFS + hashmap old to new node |
| 32-33 | Course Schedule I/II | Good | You did both DFS colouring and Kahn's. Good interview material |
| 34 | Number of Provinces | OK | Solved with DFS; the plan said union-find. Learn the union-find template (path compression + rank) |
| 36-37, 40-41 | DP basics, LCS, Partition | Good | Day 41: explain why the inner loop runs backwards (0/1 knapsack) |
| 38 | LIS | OK | O(n²). Know the O(n log n) patience-sort version; it's a common follow-up |
| 39 | Coin Change | OK | Works, but a `vector<int> dp(amount+1, INF)` is the standard; `map` and the sort are unnecessary |
| 43-45 | Binary search set | Good | Code was pasted into README instead of `solution.py`; Day 43 should use `left + (right-left)/2` |
| 46 | Kth Largest | Good | Know quickselect (average O(n)) as the follow-up |
| 47 | Top K Frequent | OK | Pushes every element into a max-heap, O(n log n). Use a size-k min-heap or bucket sort, O(n) |
| 48 | Jump Game | **Missing** | Greedy reach |

## Patterns interviews ask that this repo doesn't cover yet

- Backtracking: Subsets, Permutations, Combination Sum, Word Search, N-Queens
- Intervals: Merge Intervals, Insert Interval, Meeting Rooms II
- Tries: Implement Trie, Word Search II
- Shortest paths: Dijkstra (Network Delay Time), BFS on grids (Rotting Oranges)
- Monotonic stack Hard: Largest Rectangle in Histogram
- Design-style: LRU Cache, LFU Cache (often asked in Java/backend loops)
- 2D DP: Edit Distance, Unique Paths, Word Break
- Linked list Hard: Reverse Nodes in k-Group, Merge K Sorted Lists

## What to change in how you practise

1. **Fill the header every time** (pattern trigger, approach, complexity) before you commit. This is the part you will be asked to say out loud.
2. **Write one line in `mistakes-log.md`** whenever your first idea was wrong or slower than needed. Days 4, 6, 9, 13 and 47 above are your first entries.
3. **Rename files to `.cpp`** (or keep a `.java` copy for Java roles) so they compile and run with tests.
4. **Do the review days.** Redo the 7 "Redo" rows above from a blank file, timed at 20 minutes each.
5. **Language:** C++ is fine for DSA rounds almost everywhere. Use Java for machine-coding and LLD rounds when the role is Java/Spring.

## Next 4 weeks of DSA (45 min/day, alongside the daily mock interview)

| Week | Dates | Focus |
| --- | --- | --- |
| 1 | 2-8 Nov | Fix list: Days 4, 5, 6, 13 redone; Min Stack, Clone Graph, Jump Game done; fill all headers for Days 1-13 |
| 2 | 9-15 Nov | Backtracking (5 problems) + intervals (3); redo Days 9 and 47 the optimal way |
| 3 | 16-22 Nov | Tries, Dijkstra, grid BFS, union-find template, Largest Rectangle |
| 4 | 23-29 Nov | Week 8 of this plan: company-tagged problems + 2 timed 45-min mocks per week |
