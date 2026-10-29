# Day 9 · Sat 7 Nov 2026 · Concurrency + Splitwise machine coding

**Goal:** Size thread pools with reasons, and build a second timed machine-coding solution.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 30 min | 2. DSA | Combination Sum (C++, files in `dsa/`) |
| 60 min | 3. Machine coding: Splitwise (Java, 60 min) | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · Async bulk import · Medium

Your bulk processing handles 50K+ inventory records with @Async and ThreadPoolTaskExecutor. How did you size the pool and queue, what happens when the queue is full, and how does the user learn which rows failed?

<details><summary>Must cover</summary>

- Core/max pool size based on whether work is CPU or DB bound, and on DB connection pool size
- Bounded queue capacity; RejectedExecutionHandler (CallerRuns, abort with a 'try later' response)
- Chunk rows into batches; batch inserts; one transaction per chunk, not per row or for all 50K
- Track job status and per-row errors in a table; downloadable error report
- Tenant context passed explicitly to async threads

**Likely follow-ups**

- Why not just increase max pool size to 200?
- How would you resume a job that died halfway?

</details>

### Q2 · Java & Spring · Thread pools · Medium

Explain the parameters of ThreadPoolExecutor and how tasks flow through them. Why is Executors.newCachedThreadPool() or newFixedThreadPool() risky in a production service?

<details><summary>Must cover</summary>

- corePoolSize, maximumPoolSize, keepAliveTime, workQueue, ThreadFactory, RejectedExecutionHandler
- Flow: core threads first, then the queue, then extra threads up to max, then rejection
- Cached pool: unbounded threads, can exhaust memory/CPU under load
- Fixed pool: unbounded LinkedBlockingQueue, so tasks pile up and memory grows; max size is never used
- Name threads, bound queues, monitor queue depth

**Likely follow-ups**

- CPU-bound vs I/O-bound pool sizing rule of thumb?
- What is the ForkJoinPool common pool used for?

</details>

### Q3 · LLD · Splitwise · Hard

Design Splitwise's core: users, groups, expenses split EQUAL, EXACT or PERCENT, balances, and 'simplify debts'. Name the classes, show how a new split type is added, and describe the simplify algorithm.

<details><summary>Must cover</summary>

- User, Group, Expense, abstract Split with EqualSplit/ExactSplit/PercentSplit (or a SplitStrategy)
- Validation per type: exact amounts sum to total, percents sum to 100
- BalanceSheet: net balance per user pair or per user
- Simplify: compute each user's net amount, greedily match largest creditor with largest debtor (heaps)
- Money as integer paise/BigDecimal, rounding rule for equal splits

**Likely follow-ups**

- Why not use double for money?
- How do you keep balances correct if two expenses are added at the same time?

</details>

### Q4 · HLD · Distributed rate limiter · Medium

Design a rate limiter for your public B2B APIs: limits per tenant and per API key, enforced across 10 API instances, with under 5 ms overhead. Cover the algorithm, where it runs, the data store, and failure behaviour.

<details><summary>Must cover</summary>

- Where: API gateway (API Gateway usage plans) or middleware in each instance
- Algorithm: token bucket or sliding window counter; trade-offs
- Shared state in Redis with atomic Lua scripts; key per tenant/key per window
- Headers: 429, Retry-After, remaining quota
- Failure: fail open vs fail closed per API; local fallback limits; hot-key considerations

**Likely follow-ups**

- How do you give one premium tenant a higher limit without a deploy?
- How would you rate-limit by cost (heavy endpoints count more)?

</details>

### Q5 · DSA · Backtracking · Medium

Given distinct positive integers candidates and a target, return all unique combinations where the chosen numbers sum to target; a number may be used any number of times. Example: candidates [2,3,6,7], target 7 gives [[2,2,3],[7]]. Explain the recursion, pruning and complexity, and write the code.

<details><summary>Must cover</summary>

- Backtrack(start, remaining, path); recurse with i (not i+1) to allow reuse
- Stop when remaining == 0 (record) or < 0
- Sort and break early when candidates[i] > remaining
- Using start index avoids permutations of the same combination
- Exponential complexity; depth up to target / min(candidate)

**Likely follow-ups**

- What changes for Combination Sum II (each number once, duplicates in input)?
- Could DP count the combinations instead of listing them?

</details>

### Q6 · Databases · Multi-tenancy · Medium

Compare database-per-tenant (what you built), schema-per-tenant, and a shared schema with a tenant_id column. Then explain how you'd run a schema migration safely across 50+ tenant databases.

<details><summary>Must cover</summary>

- DB-per-tenant: strongest isolation, per-tenant backup/restore, noisy-neighbour isolation; cost and connection-pool overhead
- Shared schema: cheapest, easiest migrations; risk of cross-tenant leaks, needs tenant_id everywhere (row-level security)
- Schema-per-tenant in between
- Migrations: Flyway/Liquibase run per tenant in a loop or pipeline, tracked per DB
- Backward-compatible (expand/contract) changes so old and new code work during rollout; stop on failure

**Likely follow-ups**

- How do you onboard a new tenant DB automatically?
- How would you move one big tenant to its own server?

</details>

## 2. DSA (30 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **[Combination Sum](https://leetcode.com/problems/combination-sum/) (#39)** · pattern: Backtracking with reuse
    - What to say: Recurse with the same index to allow reuse, move to i+1 to stop reusing; prune when the remaining target goes below 0 (sort first to break early).
    - File: [`dsa/combination-sum.cpp`](dsa/combination-sum.cpp)

## 3. Machine coding: Splitwise (Java, 60 min) (60 min)

- [ ] Requirements (5 min): users, groups, add expense, split EQUAL / EXACT / PERCENT, show balances, simplify debts
- [ ] Entities (10 min): User, Group, Expense, Split (abstract) + EqualSplit/ExactSplit/PercentSplit, BalanceSheet
- [ ] Core flows (30 min): addExpense with validation (exact sums, percents = 100), showBalances
- [ ] Driver (5 min): 3 users, 3 expenses, print balances
- [ ] Extension (10 min): add a SHARES split type; how many classes change?

**Explain out loud in 2 minutes**

- [ ] Why is Split polymorphic instead of a switch on type?
- [ ] How would you make addExpense safe when two requests hit the same group?

**Output:** Save the code in this folder as splitwise/

## 4. Log (fill before you sleep)

| Item | Entry |
| --- | --- |
| Date | |
| Time spent (mock / DSA / topic) | |
| Mock questions answered (of 6) | |
| Mock score (from next morning's feedback, avg /4) | |
| DSA solved without help | |
| DSA mistakes (also add to docs/mistakes-log.md) | |
| Topic checklist done (of 5) | |
| What I couldn't explain | |
| Fix tomorrow | |

[<- Day 8](../day08/README.md) · [All days](../README.md) · [Day 10 ->](../day10/README.md)
