# Day 2 · Sat 31 Oct 2026 · Java collections + Parking Lot machine coding

**Goal:** Know HashMap and ConcurrentHashMap internals cold, and build your first timed machine-coding solution.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 30 min | 2. DSA | Maximum Subarray, Sliding Window Maximum (C++, files in `dsa/`) |
| 60 min | 3. Machine coding: Parking Lot (Java, 60 min) | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · Payments · Medium

You say Stripe PaymentIntents ran with zero duplicate charges. Where exactly was the idempotency key generated and stored, and what happens when Stripe's webhook for the same payment arrives twice, or arrives before your own API call returns?

<details><summary>Must cover</summary>

- Key derived from a stable business id (invoice/order id + attempt), not a random value per retry
- Key stored with the payment record before calling Stripe, so a retry reuses it
- Webhook handler is idempotent: store processed event ids, or update status with a condition (only if not already paid)
- Order of events is not guaranteed: treat the webhook as the source of truth and reconcile both paths into one state machine
- Reconciliation job comparing Stripe and DB for drift

**Likely follow-ups**

- How long does Stripe keep an idempotency key?
- What does your reconciliation job do when it finds a mismatch?

</details>

### Q2 · Java & Spring · HashMap internals · Medium

Walk me through what happens inside a Java HashMap when you call put(key, value), including collisions and resizing. Then tell me what goes wrong if someone uses a mutable object as a key and changes it after inserting.

<details><summary>Must cover</summary>

- hashCode() spread, index = (n - 1) & hash, table of buckets
- Collision: linked list in the bucket, converted to a red-black tree at 8 entries (table size at least 64)
- Resize when size exceeds capacity x load factor 0.75: table doubles and entries are redistributed
- equals() is used to find the key inside a bucket; equals/hashCode contract
- Mutable key: hash changes, entry sits in the wrong bucket, get() returns null and the entry leaks

**Likely follow-ups**

- Why is the capacity always a power of two?
- What is the worst-case lookup time before and after treeification?

</details>

### Q3 · Java & Spring · Concurrent collections · Medium

Your Spring service keeps an in-memory map of tenant settings that many request threads read and a background refresher writes. Compare HashMap, Collections.synchronizedMap and ConcurrentHashMap for this, and show how you'd do a safe 'load if missing' without two threads both loading.

<details><summary>Must cover</summary>

- HashMap is not thread-safe: lost updates, corrupted state, visibility issues
- synchronizedMap locks the whole map on every call; compound check-then-put is still racy without external locking
- ConcurrentHashMap: fine-grained locking/CAS, lock-free reads, weakly consistent iterators
- computeIfAbsent does an atomic load-if-missing; keep the loader short and don't modify the map inside it
- For refresh, swap a whole immutable map via a volatile reference or AtomicReference

**Likely follow-ups**

- Why does ConcurrentHashMap not allow null keys or values?
- When would you use Caffeine instead of a map?

</details>

### Q4 · LLD · Parking lot · Medium

Design the classes for a multi-floor parking lot with bike, car and truck spots, tickets, and hourly pricing that the business changes often. Name your classes and their relationships, show where the design patterns go, and explain how you stop two cars getting the same last spot.

<details><summary>Must cover</summary>

- Entities: ParkingLot, Floor, Spot (type), Vehicle (type), Ticket, Payment/fee
- PricingStrategy interface (hourly, weekend, flat) so pricing changes don't touch core classes
- SpotAllocationStrategy (nearest, by floor) chosen at construction
- Concurrency: lock per floor/spot, synchronized allocate, or an atomic compare-and-set on the spot's free flag
- Clear flows: park -> ticket, unpark(ticket) -> fee; validation and errors for full lot

**Likely follow-ups**

- How do you add EV charging spots?
- How would this change if the lot state lives in a database shared by 4 entry gates?

</details>

### Q5 · DSA · Monotonic deque · Hard

Given an array nums and a window size k, return the maximum of every window of size k as it slides from left to right. Example: nums = [1,3,-1,-3,5,3,6,7], k = 3 gives [3,3,5,5,6,7]. Constraints: n up to 10^5. Give the brute force, then an O(n) solution, explain why it's O(n), and write the code.

<details><summary>Must cover</summary>

- Brute force O(n*k); a multiset/heap is O(n log k)
- Deque of indices with values in decreasing order
- Pop back while nums[back] <= new value; pop front when its index leaves the window; front is the max
- Each index is pushed and popped at most once: O(n) time, O(k) space
- Edge cases: k = 1, k = n, all equal values

**Likely follow-ups**

- How would you return the minimum instead?
- Where does the monotonic idea show up in other problems?

</details>

### Q6 · Redis · Rate limiting · Medium

Your MFA system rate-limits OTP requests across many Lambda instances. Design the Redis-based limiter: the keys, the commands, how you avoid race conditions, and what happens if Redis is unavailable.

<details><summary>Must cover</summary>

- Key per user/phone (and per IP) with a window, e.g. otp:{phone}:{minute}
- Fixed window with INCR + EXPIRE, or sliding window with a sorted set (ZADD/ZREMRANGEBYSCORE/ZCARD)
- Atomicity: INCR is atomic; set the expiry in the same step (Lua script or SET NX EX) so a key never lives forever
- Return 429 with retry-after; separate limits for send and verify attempts
- Redis down: fail closed for OTP send (security) or a conservative local fallback, plus alarms

**Likely follow-ups**

- Fixed window vs sliding window: what burst does fixed window allow?
- How would you stop someone cycling through many phone numbers?

</details>

## 2. DSA (30 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (#53)** · pattern: Kadane's running sum
    - What to say: At each index, either extend the previous subarray or start fresh: cur = max(x, cur + x); best = max(best, cur). O(n), O(1). Your Kadane code is sitting in the Day 4 file of week 1; move it here and write the header.
    - File: [`dsa/maximum-subarray.cpp`](dsa/maximum-subarray.cpp)
- [ ] **[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (#239)** · pattern: Monotonic deque of indices
    - What to say: Your multiset version is O(n log k). Keep a deque of indices with decreasing values: pop from the back while smaller than the new value, pop from the front when it leaves the window, the front is the max. Each index enters and leaves once, so O(n).
    - File: [`dsa/sliding-window-maximum.cpp`](dsa/sliding-window-maximum.cpp)

## 3. Machine coding: Parking Lot (Java, 60 min) (60 min)

- [ ] Requirements (5 min): multiple floors, spot types (bike, car, truck), entry/exit, ticket, hourly pricing that can change
- [ ] Entities (10 min): ParkingLot, Floor, Spot, Vehicle, Ticket, PricingStrategy, SpotAllocationStrategy
- [ ] Core flows (30 min): park(vehicle) -> Ticket, unpark(ticket) -> fee
- [ ] Driver (5 min): a main() that parks 3 vehicles, unparks 1, prints the fee
- [ ] Extension check (10 min): could you add EV charging spots without editing existing classes?

**Explain out loud in 2 minutes**

- [ ] Why is pricing a Strategy and not an if/else?
- [ ] What happens if two cars try to take the last spot at the same time?

**Output:** Save the code in this folder as parking-lot/

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

[<- Day 1](../day01/README.md) · [All days](../README.md) · [Day 3 ->](../day03/README.md)
