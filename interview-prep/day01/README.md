# Day 1 · Fri 30 Oct 2026 · Resume deep-dive: multi-tenancy, SQS and Spring

**Goal:** Fix the resume numbers you'll be questioned on, and redo the two prefix-sum problems the right way.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 50 min | 2. DSA | Subarray Sum Equals K, Product of Array Except Self (C++, files in `dsa/`) |
| 40 min | 3. Resume fix-up + 2-minute stories | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · Multi-tenancy · Medium

Your resume says you routed 50+ tenants with AbstractRoutingDataSource and a ThreadLocal tenant context set in a custom filter. Walk me through one HTTP request from the moment it hits the filter to the SQL query running on the right tenant's database. Then: what happens to the tenant context when that request kicks off an @Async export job?

<details><summary>Must cover</summary>

- Filter extracts tenant from the JWT/Cognito claim, validates it, sets ThreadLocal, and clears it in a finally block
- determineCurrentLookupKey() reads the ThreadLocal; a DataSource (and connection pool) per tenant in the target map
- ThreadLocal does not carry over to @Async threads: pass tenantId explicitly or use a TaskDecorator that copies and clears it
- Risk of tenant leaking to the next request on a pooled thread if not cleared
- Connection pool sizing: 50 pools x N connections vs MySQL max_connections

**Likely follow-ups**

- How do you add a new tenant without restarting the service?
- How do you run a schema migration across all 50 databases?
- Why database-per-tenant instead of a tenant_id column?

</details>

### Q2 · AWS · SQS consumers · Medium

Your SQS consumers handle order-lifecycle events. A Lambda consumer processes an 'order paid' message, updates MySQL, then times out before deleting the message. What happens next, and how did you (or would you) make sure the order isn't processed twice?

<details><summary>Must cover</summary>

- Message becomes visible again after the visibility timeout and is redelivered (at-least-once delivery)
- Idempotent consumer: a processed-events table keyed by message/event id, or a conditional update on order status
- Visibility timeout set above the function timeout (AWS suggests about 6x for Lambda event sources)
- DLQ with maxReceiveCount for poison messages, plus an alarm on DLQ depth
- Partial batch failure reporting (ReportBatchItemFailures) so one bad message doesn't retry the whole batch

**Likely follow-ups**

- Standard or FIFO queue for order events, and why?
- How would you replay messages from the DLQ safely?

</details>

### Q3 · Java & Spring · @Transactional · Medium

In a billing service, a method generateInvoice() calls this.saveAuditLog() which is annotated @Transactional(propagation = REQUIRES_NEW). The audit log rolls back whenever the invoice fails. Why, and how do you fix it?

<details><summary>Must cover</summary>

- Spring transactions work through a proxy; a call via 'this' bypasses the proxy, so REQUIRES_NEW is ignored
- Fixes: move the method to another bean, inject self via the proxy, or use TransactionTemplate
- What REQUIRES_NEW does: suspends the outer transaction and commits independently
- Rollback rules: runtime exceptions roll back by default, checked exceptions do not unless rollbackFor is set

**Likely follow-ups**

- Does @Transactional work on a private method?
- What isolation level does MySQL InnoDB use by default, and what anomaly does it still allow?

</details>

### Q4 · Resume deep-dive · Caching · Medium

You cut DB traffic 70% by caching tenant, pricing and offer settings in Redis. A seller updates a floor price, and for the next few minutes some buyers still see the old price. Explain how that can happen with your caching pattern and how you would close the gap.

<details><summary>Must cover</summary>

- Names the pattern used (cache-aside with eviction on update) and the race: a read repopulates stale data between DB write and eviction
- Order matters: write DB first, then delete the key (not update it); consider delayed double-delete
- TTL as a safety net, and shorter TTL for price data than for tenant settings
- Multiple instances: eviction must hit shared Redis, not a local in-memory cache
- Pricing guardrail should read from the DB (source of truth) when accepting an offer, not from cache

**Likely follow-ups**

- What happens to your APIs if Redis goes down?
- How do you avoid a cache stampede on a hot tenant key?

</details>

### Q5 · HLD · Async jobs · Medium

Design the async report export you built: the API returns 202, a separate Lambda builds the file, and status sits in Redis. Now the business wants exports up to 500 MB and 200 concurrent requests at month-end. What breaks first and how would you redesign it?

<details><summary>Must cover</summary>

- API Gateway 29 s limit is why it's async; Lambda limits next: 15 min max, memory, /tmp size
- Stream rows from MySQL (cursor/pagination) and stream-write to S3 with multipart upload instead of building in memory
- Put a queue (SQS) between API and workers to control concurrency and protect the DB; read replica for reports
- Durable job status (DynamoDB or MySQL) rather than only Redis; retries and idempotent job ids
- Deliver via a short-lived pre-signed S3 URL; notify by polling, WebSocket or email
- Consider ECS/Fargate or Step Functions for very long jobs

**Likely follow-ups**

- How does the client know the job failed?
- How do you stop one tenant's huge export from starving others?

</details>

### Q6 · DSA · Hashing · Medium

Given an unsorted array of integers, return the length of the longest run of consecutive numbers, e.g. [100, 4, 200, 1, 3, 2] gives 4. Your solution must be O(n). Explain the approach, the complexity, and the edge cases, then write the code (C++ is fine) in the box.

<details><summary>Must cover</summary>

- Brute force (sort, O(n log n)) stated first, then the O(n) set approach
- Only start counting from numbers where n-1 is not in the set, so each number is visited at most twice
- Edge cases: empty array, duplicates, negative numbers, Integer.MAX_VALUE
- Time O(n), space O(n); clean code with a HashSet<Integer>

**Likely follow-ups**

- Can you do it without extra space if modifying the input is allowed?
- How would you return the sequence itself, not just its length?

</details>

## 2. DSA (50 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (#560)** · pattern: Prefix sum + hashmap of counts
    - What to say: Brute force is O(n^2) over all subarrays (your Day 6 code). Store how many times each prefix sum appeared; for each new prefix p, add count[p - k]. Seed count[0] = 1. O(n) time, O(n) space. Works with negatives, which is why sliding window fails here.
    - File: [`dsa/subarray-sum-equals-k.cpp`](dsa/subarray-sum-equals-k.cpp)
- [ ] **[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (#238)** · pattern: Prefix and suffix products
    - What to say: Division is not allowed and breaks on zeros. Pass 1 fills ans[i] with the product of everything left of i; pass 2 multiplies in a running product from the right. O(n) time, O(1) extra space besides the output.
    - File: [`dsa/product-of-array-except-self.cpp`](dsa/product-of-array-except-self.cpp)

## 3. Resume fix-up + 2-minute stories (40 min)

- [ ] Pick ONE true number for SQS volume (3,000+/day vs 5 lakh/day) and write how it was measured
- [ ] Pick ONE number for the Lambda cost saving (35% vs 60%) and name the baseline
- [ ] Change 'Architected a multi-tenant marketplace' to 'Architected backend modules of' in every version
- [ ] Decide: keep or drop the MFA '10% fewer unauthorized attempts' and the 99.98% uptime figure
- [ ] Write a 2-minute story for your top 5 bullets: problem, my part, design, what broke, the number and how it was measured

**Explain out loud in 2 minutes**

- [ ] Explain the database-per-tenant design in 2 minutes without notes
- [ ] Explain the billing Step Functions flow in 2 minutes

**Output:** Save the 5 stories in this folder as stories.md

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

[All days](../README.md) · [Day 2 ->](../day02/README.md)
