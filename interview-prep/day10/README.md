# Day 10 · Sun 8 Nov 2026 · HLD: URL shortener + timed mock

**Goal:** Run a full HLD answer with the 6-step framework, a timed DSA mock, and a 10-day retro.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 45 min | 2. DSA | Merge Intervals (timed mock, part 1), Insert Interval (timed mock, part 2) (C++, files in `dsa/`) |
| 45 min | 3. HLD: URL shortener + 10-day retro | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · Observability · Medium

You built AI-powered observability pipelines in n8n that cut MTTD by 50%. What exactly does the AI step do, how was MTTD measured before and after, and how do you keep false alerts and LLM cost under control?

<details><summary>Must cover</summary>

- Concrete flow: CloudWatch alarm / RDS metrics -> n8n -> LLM summarises or classifies -> Slack
- MTTD defined (issue start to detection) and measured from incident records before and after
- Thresholds and deduplication before calling the LLM, so it only runs on real signals
- Cost: tokens per alert, caps, cheaper model for classification
- Fallback: raw alert still sent if the LLM call fails

**Likely follow-ups**

- Why not just tune CloudWatch alarms?
- What would you never send to an external LLM?

</details>

### Q2 · HLD · URL shortener · Medium

Design a URL shortener: 100 million new links a month, 10x more redirects than creates. Cover requirements, API, key generation, storage, caching, and redirects.

<details><summary>Must cover</summary>

- Estimates: ~40 writes/s, ~400 reads/s average with peaks; storage for 5 years
- API: POST /shorten (with optional custom alias, expiry), GET /{code} redirect
- Key generation: base62 of a distributed counter/ID ranges, or a pre-generated key service; collision handling
- Store code -> long URL in a key-value store or MySQL with an index; Redis cache for hot codes
- 301 (cacheable, fewer hits) vs 302 (track every click); analytics written asynchronously

**Likely follow-ups**

- How do you stop abuse (spam, phishing links)?
- How do custom aliases change key generation?

</details>

### Q3 · HLD · Scaling reads · Medium

The URL shortener now serves 50,000 redirects per second at peak, and a few viral links take 30% of the traffic. How do you scale the read path, and what changes in the data layer?

<details><summary>Must cover</summary>

- CDN / edge caching of redirects where possible
- Redis cache in front of the DB with high hit ratio; local in-process cache for the hottest keys
- Read replicas; shard by code hash when one primary isn't enough
- Hot keys: replicate them across cache nodes or keep them in local caches
- Stateless app servers behind a load balancer, autoscaling, monitoring p99 latency

**Likely follow-ups**

- What happens when a hot key expires from cache?
- Consistent hashing: why use it for the cache cluster?

</details>

### Q4 · LLD · KV store with TTL · Medium

Design and code an in-memory key-value store with set(key, value, ttlSeconds), get(key) and delete(key). Expired keys must never be returned, and memory shouldn't grow forever with expired keys. Explain the data structures and how expiry is handled.

<details><summary>Must cover</summary>

- HashMap key -> (value, expiresAt)
- Lazy expiry on get (check and delete) so expired values are never returned
- Active cleanup: a min-heap/priority queue by expiry, or periodic sampling like Redis
- Thread safety: ConcurrentHashMap, careful compound operations
- Clock injected for testing

**Likely follow-ups**

- How would you add transactions (begin, commit, rollback)?
- How would you persist it across restarts?

</details>

### Q5 · DSA · Intervals · Medium

Given a list of intervals [start, end], merge all overlapping intervals. Example: [[1,3],[2,6],[8,10],[15,18]] gives [[1,6],[8,10],[15,18]]. Then: the intervals are already sorted and non-overlapping, insert a new interval and merge. Give both approaches with complexity and code the second.

<details><summary>Must cover</summary>

- Merge: sort by start, extend the last merged end with max, O(n log n)
- Touching intervals ([1,4],[4,5]) count as overlapping per the problem
- Insert: add all that end before the new start, merge all that overlap into the new one, add the rest: O(n)
- No sort needed for insert because input is sorted
- Edge cases: empty list, new interval before all or after all

**Likely follow-ups**

- How would you find the minimum meeting rooms needed?
- How would you merge intervals arriving as a stream?

</details>

### Q6 · AWS · Messaging choices · Medium

Compare SQS, SNS, Kinesis and Kafka. Your resume mentions publishing domain events to SQS, SNS and Kinesis. When would you choose each, and when would a team move to Kafka?

<details><summary>Must cover</summary>

- SQS: queue, one consumer group per queue, at-least-once, no replay after delete
- SNS: pub/sub fan-out to many subscribers (often SNS -> multiple SQS)
- Kinesis: ordered shards, replay within retention, multiple consumers reading the same stream
- Kafka (MSK): partitions, consumer groups, long retention and replay, rich ecosystem; more ops work
- Choose by ordering, replay, fan-out, throughput and ops cost

**Likely follow-ups**

- How does ordering work in Kinesis vs SQS FIFO?
- How would you migrate from SQS to Kafka without downtime?

</details>

## 2. DSA (45 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **[Merge Intervals (timed mock, part 1)](https://leetcode.com/problems/merge-intervals/) (#56)** · pattern: Sort by start, merge overlaps
    - What to say: Timed: 20 minutes for both problems together with Insert Interval. Sort by start, extend the last merged interval while it overlaps. O(n log n).
    - File: [`dsa/merge-intervals.cpp`](dsa/merge-intervals.cpp)
- [ ] **[Insert Interval (timed mock, part 2)](https://leetcode.com/problems/insert-interval/) (#57)** · pattern: Three-phase sweep
    - What to say: Add intervals ending before the new one, merge all that overlap, add the rest. O(n), no sort needed since input is sorted.
    - File: [`dsa/insert-interval.cpp`](dsa/insert-interval.cpp)

## 3. HLD: URL shortener + 10-day retro (45 min)

- [ ] Requirements and scale: writes/day, reads/day, read:write ratio, storage for 5 years
- [ ] APIs: POST /shorten, GET /{code}; 301 vs 302 and why it matters for analytics
- [ ] Key generation: base62 counter vs hash vs pre-generated key service; collisions
- [ ] Storage + cache: key-value store, Redis for hot codes, TTL/expiry
- [ ] Scaling and failure: read replicas, sharding by code, rate limiting abuse
- [ ] Retro: fill the 10-day summary in LOG.md and pick the 3 weakest areas for days 11-20

**Explain out loud in 2 minutes**

- [ ] Present the whole design in 15 minutes out loud
- [ ] What changes if links must expire and be deletable by their owner?

**Output:** hld-url-shortener.md in this folder with the design

## 4. Log (fill before you sleep)

| Item | Entry |
| --- | --- |
| Date | |
| Time spent (mock / DSA / topic) | |
| Mock questions answered (of 6) | |
| Mock score (from next morning's feedback, avg /4) | |
| DSA solved without help | |
| DSA mistakes (also add to docs/mistakes-log.md) | |
| Topic checklist done (of 6) | |
| What I couldn't explain | |
| Fix tomorrow | |

[<- Day 9](../day09/README.md) · [All days](../README.md)
