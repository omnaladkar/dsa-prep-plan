# Day 3 · Sun 1 Nov 2026 · Review day: JVM, strings and your weakest answers

**Goal:** Redo this week's problems from a blank file and repair the two lowest-scored mock answers.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 45 min | 2. DSA | Redo Days 1-2 from blank files (10 min each), Maximum Product Subarray (C++, files in `dsa/`) |
| 45 min | 3. JVM memory + review | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · MFA / OTP · Medium

Walk me through your MFA flow for 6 lakh users from the moment the user enters a password to the moment they get a session: where the OTP is generated, how it is stored and expires, and how you stop someone brute-forcing a 6-digit code.

<details><summary>Must cover</summary>

- Generate with a secure random source; 6 digits; short expiry (minutes)
- Store a hash of the OTP (not plaintext) with expiry and attempt count, keyed by user/session
- Verify: constant-time compare, increment attempts, lock or invalidate after N failures
- Rate limit sends and verifies per user and per IP; resend cooldown
- After success issue tokens (Cognito/JWT) and invalidate the OTP; audit logging

**Likely follow-ups**

- Why is SMS OTP considered weak, and what is SIM swap?
- How did you test this before rolling out to 6 lakh users?

</details>

### Q2 · Java & Spring · JVM memory · Medium

Your Spring Boot service on a 2 GB container gets OOM-killed every few days. Explain the JVM memory areas, what usually causes each kind of OutOfMemoryError, and how you'd investigate this one.

<details><summary>Must cover</summary>

- Heap (young/old), thread stacks, metaspace, direct/off-heap buffers, code cache
- Container kills can come from total RSS above the limit even when the heap looks fine; set -Xmx/MaxRAMPercentage below the limit
- Heap OOM causes: unbounded caches/maps, large collections, leaks via static references or ThreadLocals
- Investigate: GC logs, heap dump on OOM (-XX:+HeapDumpOnOutOfMemoryError), jcmd/jmap, Eclipse MAT dominator tree
- Metaspace OOM from classloader leaks; thread-related OOM from too many threads

**Likely follow-ups**

- What does G1 do differently from the old parallel collector?
- How could your ThreadLocal tenant context leak memory?

</details>

### Q3 · Java & Spring · Strings · Easy

Explain why Java Strings are immutable, what the string pool is, and why building a 50,000-row CSV with s += line in a loop is slow. What would you use instead?

<details><summary>Must cover</summary>

- Immutability: safe sharing, hashCode caching, security, thread safety
- Pool: literals are interned; new String creates a separate object; == compares references, equals compares content
- s += in a loop creates a new String each time: O(n^2) copying
- Use StringBuilder (not synchronized StringBuffer) or stream rows to a Writer
- For 50K rows, write directly to an output stream instead of one big string

**Likely follow-ups**

- When would you call intern() and why is it rarely worth it?
- What changed with compact strings in Java 9?

</details>

### Q4 · LLD · LRU cache · Medium

Design and code an LRU cache class with get(key) and put(key, value) in O(1), with a fixed capacity. Then explain how you'd make it thread-safe for a multi-threaded service.

<details><summary>Must cover</summary>

- HashMap of key -> node plus a doubly linked list ordered by recency
- get: move node to front; put: update or insert at front, evict from tail when over capacity
- Sentinel head/tail nodes to avoid null checks
- Java shortcut: LinkedHashMap with accessOrder = true and removeEldestEntry, and saying why you'd still write it by hand in an interview
- Thread safety: a single lock around get/put (get mutates order), or segment the cache; mention Caffeine for production

**Likely follow-ups**

- How would you add a per-entry TTL?
- Why is a read-write lock not enough here?

</details>

### Q5 · DSA · Kadane variant · Medium

Given an integer array (can contain negatives and zeros), return the largest product of a contiguous subarray. Example: [2,3,-2,4] gives 6; [-2,0,-1] gives 0. Explain how this differs from maximum sum subarray, then give an O(n) solution with code.

<details><summary>Must cover</summary>

- Brute force O(n^2) over all subarrays
- Track both curMax and curMin because a negative flips them
- At each x: candidates x, curMax*x, curMin*x; update both, then best
- Zeros reset naturally since x itself is a candidate
- O(n) time, O(1) space; edge cases single element, all negatives

**Likely follow-ups**

- Can you do it with a prefix-and-suffix product scan instead?
- What if the product can overflow 64 bits?

</details>

### Q6 · Security · XSS · Medium

You fixed 5 XSS/CSRF findings with sanitize-html. Explain stored, reflected and DOM-based XSS, why sanitizing on input alone is not enough, and what else you'd put in place.

<details><summary>Must cover</summary>

- Stored: payload saved and shown to others; reflected: echoed from the request; DOM: client JS writes untrusted data to the DOM
- Output encoding per context (HTML body, attribute, JS, URL) is the primary defence; sanitize only where rich HTML is truly needed
- Content-Security-Policy to block inline scripts; HttpOnly cookies so scripts can't read session cookies
- CSRF: SameSite cookies, CSRF tokens; JWT in Authorization header is not sent automatically, cookies are
- Verify with the retest and add regression tests for the payloads

**Likely follow-ups**

- Why can sanitizing on input corrupt data or still be bypassed?
- What does SameSite=Lax allow and block?

</details>

## 2. DSA (45 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **Redo Days 1-2 from blank files (10 min each)** · pattern: Prefix sum, prefix/suffix product, Kadane, monotonic deque
    - What to say: No notes. Say brute force, pattern and complexity out loud first. Any problem over 10 minutes goes in docs/mistakes-log.md.
- [ ] **[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (#152)** · pattern: Kadane variant tracking max and min
    - What to say: A negative number flips the smallest product into the largest, so carry both curMax and curMin; swap them when x < 0. O(n), O(1).
    - File: [`dsa/maximum-product-subarray.cpp`](dsa/maximum-product-subarray.cpp)

## 3. JVM memory + review (45 min)

- [ ] Heap vs stack vs metaspace: what lives where
- [ ] Young/old generation, what G1 does, what a stop-the-world pause is
- [ ] Kinds of OutOfMemoryError (heap space, metaspace, GC overhead) and one cause of each
- [ ] String pool, immutability, == vs equals, StringBuilder
- [ ] Re-answer the 2 lowest-scored questions from the mock page without notes

**Explain out loud in 2 minutes**

- [ ] Explain a memory leak you could cause in a long-running Spring service
- [ ] Why are Strings immutable in Java?

**Output:** Write 3 lines in docs/mistakes-log.md from this week

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

[<- Day 2](../day02/README.md) · [All days](../README.md) · [Day 4 ->](../day04/README.md)
