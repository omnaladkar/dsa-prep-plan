# Day 6 · Wed 4 Nov 2026 · MySQL: indexes, isolation and locking

**Goal:** Defend your EXPLAIN tuning story and reason about locks and isolation like a backend engineer.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 45 min | 2. DSA | Top K Frequent Elements, Valid Palindrome (C++, files in `dsa/`) |
| 45 min | 3. MySQL indexes, EXPLAIN, isolation, locking | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · Query tuning · Medium

Your intern bullet says you tuned queries with covering indexes and EXPLAIN, improving performance 30%. Take one real slow query: what did EXPLAIN show before, what index did you add, why was it 'covering', and how did you measure the 30%?

<details><summary>Must cover</summary>

- EXPLAIN before: type ALL or index, large rows estimate, Using filesort/temporary
- Composite index ordered for the WHERE equality columns first, then range/ORDER BY
- Covering: every selected column is in the index, so Extra shows Using index and no table lookup
- Measured with before/after latency (p50/p95) on realistic data, not one run
- Cost of the index on writes and storage

**Likely follow-ups**

- Why might MySQL ignore your index?
- What is the leftmost-prefix rule?

</details>

### Q2 · Databases · Isolation levels · Medium

Explain the four SQL isolation levels and the anomalies each allows. What is InnoDB's default, how does it avoid most phantom reads, and when would you still need SELECT ... FOR UPDATE?

<details><summary>Must cover</summary>

- READ UNCOMMITTED (dirty reads), READ COMMITTED (non-repeatable reads), REPEATABLE READ, SERIALIZABLE
- InnoDB default is REPEATABLE READ
- Consistent snapshot (MVCC) for plain SELECTs; next-key/gap locks for locking reads and writes prevent phantoms
- Plain SELECT then UPDATE can still lose updates; use FOR UPDATE or an atomic UPDATE ... WHERE
- Trade-off: stronger isolation means more locking and deadlocks

**Likely follow-ups**

- Why do many teams switch MySQL to READ COMMITTED?
- What is a lost update and how do you prevent it?

</details>

### Q3 · Databases · Deadlocks · Medium

Two order-placement requests update the same two inventory rows but in opposite order and one fails with 'Deadlock found when trying to get lock'. Explain how InnoDB detects and resolves this, and how you'd design the code so it stops happening.

<details><summary>Must cover</summary>

- Each transaction holds one row lock and waits for the other: a cycle
- InnoDB detects the cycle and rolls back one transaction (the victim) with error 1213
- Prevention: lock rows in a consistent order (sort by product id), keep transactions short
- Retry the victim transaction with backoff since it's safe to retry
- Investigate with SHOW ENGINE INNODB STATUS (latest deadlock section)

**Likely follow-ups**

- How do gap locks cause deadlocks even on inserts?
- Would optimistic locking avoid this?

</details>

### Q4 · LLD · Inventory reservation · Medium

Design stock reservation for your marketplace: when a cart is submitted, reserve quantities for 15 minutes; release them if payment doesn't complete. Two buyers can try to take the last 5 units at once. Describe the data model, the classes, and how you prevent overselling.

<details><summary>Must cover</summary>

- Reservation entity (sku, qty, cart/order id, expiresAt, status) separate from on-hand stock
- Atomic decrement: UPDATE stock SET available = available - ? WHERE sku = ? AND available >= ?, check rows affected
- Or optimistic locking with a version column and retry; compare with pessimistic FOR UPDATE
- Expiry: scheduled job or delayed message releases expired reservations; payment success converts reservation to order
- Idempotent operations keyed by cart id

**Likely follow-ups**

- What happens if the release job runs twice?
- How would this work with stock split across warehouses?

</details>

### Q5 · DSA · Bucket sort · Medium

Return the k most frequent elements of an integer array. Example: [1,1,1,2,2,3], k = 2 gives [1,2]. n up to 10^5. Your answer must beat O(n log n). Give two approaches with their complexity and code the faster one.

<details><summary>Must cover</summary>

- Count with a hashmap first, O(n)
- Size-k min-heap: O(n log k)
- Bucket sort: buckets indexed by frequency 0..n, walk from high to low: O(n)
- Full sort or full max-heap of all elements is O(n log n) and doesn't meet the bar
- Edge cases: k equals number of distinct values, ties

**Likely follow-ups**

- How would you do this on a stream that doesn't fit in memory?
- Quickselect version: average and worst case?

</details>

### Q6 · Redis · Caching patterns · Medium

Compare cache-aside, write-through and write-behind caching. For your pricing data in Redis, which did you use, and how do you stop a cache stampede when a hot tenant's key expires and 500 requests miss at once?

<details><summary>Must cover</summary>

- Cache-aside: app reads cache, on miss reads DB and fills; writes go to DB then invalidate
- Write-through: write cache and DB together; write-behind: cache first, DB async (risk of loss)
- Stampede fixes: per-key lock/single-flight (SET NX), serve stale while refreshing, jittered TTLs, early refresh
- Negative caching for missing keys
- Monitor hit ratio and eviction counts

**Likely follow-ups**

- What eviction policy would you set on Redis for a cache?
- When would you not cache at all?

</details>

## 2. DSA (45 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (#347)** · pattern: Count + bucket sort (or size-k min-heap)
    - What to say: Your version pushes every element into a max-heap, O(n log n). Buckets indexed by frequency give O(n); a size-k min-heap gives O(n log k).
    - File: [`dsa/top-k-frequent-elements.cpp`](dsa/top-k-frequent-elements.cpp)
- [ ] **[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (#125)** · pattern: Two pointers, in place
    - What to say: Don't build a cleaned copy. Move left/right inward, skipping non-alphanumerics, comparing tolower. O(n) time, O(1) space.
    - File: [`dsa/valid-palindrome.cpp`](dsa/valid-palindrome.cpp)

## 3. MySQL indexes, EXPLAIN, isolation, locking (45 min)

- [ ] B+tree index, clustered (primary) vs secondary index, covering index
- [ ] Composite index and the leftmost-prefix rule; when an index is ignored (functions, leading wildcard, type mismatch)
- [ ] EXPLAIN columns: type, key, rows, Extra (Using index, Using filesort, Using temporary)
- [ ] Isolation levels, InnoDB default REPEATABLE READ, phantom reads, gap and next-key locks
- [ ] Deadlocks: how InnoDB detects them, how to avoid (same lock order, short transactions)

**Explain out loud in 2 minutes**

- [ ] Walk through a query you sped up with EXPLAIN: before, index added, after
- [ ] Why does SELECT ... FOR UPDATE on a range lock rows that don't exist yet?

**Output:** Run EXPLAIN on 3 real queries from your work (scrub names) and note the type/rows before and after an index

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

[<- Day 5](../day05/README.md) · [All days](../README.md) · [Day 7 ->](../day07/README.md)
