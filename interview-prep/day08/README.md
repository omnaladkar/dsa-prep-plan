# Day 8 · Fri 6 Nov 2026 · LLD: SOLID and design patterns

**Goal:** Turn your payment and offer-engine work into clean LLD answers, and start backtracking.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 45 min | 2. DSA | Subsets, Subsets II (C++, files in `dsa/`) |
| 45 min | 3. SOLID + core patterns in Java | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · Payment providers · Medium

Your platform integrates Stripe and PayPal. Show how you'd structure the code so a third provider (say Razorpay) can be added without changing the Stripe or PayPal classes or the checkout flow.

<details><summary>Must cover</summary>

- PaymentGateway interface: createPayment, capture, refund, parseWebhook
- StripeGateway / PayPalGateway / RazorpayGateway implementations (Strategy) chosen by a factory/registry from config
- Common domain model (PaymentRequest, PaymentResult, statuses) mapped from each provider's API (Adapter)
- Webhook handling normalised to internal events
- Open/Closed: new provider = new class + registration, no edits to existing ones

**Likely follow-ups**

- How do you test this without hitting the real providers?
- Where does idempotency live: per provider or in your domain layer?

</details>

### Q2 · LLD · SOLID · Medium

Explain each SOLID principle with an example from code you've written. Then give a Liskov Substitution violation and how you'd fix it.

<details><summary>Must cover</summary>

- S: one reason to change (e.g. invoice calculation separate from PDF rendering)
- O: extend via new classes (payment providers, pricing strategies)
- L: subtypes usable wherever the base is, without surprises
- I: small focused interfaces instead of one fat interface
- D: depend on abstractions, inject implementations (Spring DI)
- LSP example: ReadOnlyList throwing on add(), or Square extends Rectangle; fix by redesigning the hierarchy

**Likely follow-ups**

- Which principle does Spring's dependency injection help most with?
- Can following SOLID too strictly hurt a small codebase?

</details>

### Q3 · Java & Spring · Singleton · Medium

Write a thread-safe lazy Singleton in Java two different ways and explain the trade-offs. Then explain why you almost never write one by hand in a Spring application.

<details><summary>Must cover</summary>

- Double-checked locking with a volatile instance (and why volatile is required)
- Initialization-on-demand holder class, or enum singleton (serialization and reflection safe)
- Eager static final instance as the simplest option
- Spring beans are singletons per container by default and are injected, which keeps them testable
- Singletons with mutable state are a shared-state risk

**Likely follow-ups**

- Why does double-checked locking break without volatile?
- How can reflection or serialization break a singleton?

</details>

### Q4 · LLD · Offer engine · Hard

Design the offer/negotiation engine for your B2B marketplace: a buyer makes an offer, the seller can accept, reject or counter, offers expire, and nobody can accept below the seller's floor price. Show the classes and how state transitions are enforced.

<details><summary>Must cover</summary>

- Offer entity with status: PENDING, COUNTERED, ACCEPTED, REJECTED, EXPIRED
- State pattern or a transition table; invalid transitions throw
- Floor-price guardrail checked on accept and counter, reading the floor from the source of truth
- Expiry via scheduled job or check-on-read; concurrency so accept and expire can't both win (version column)
- Domain events (offer updated, accepted) published for notifications

**Likely follow-ups**

- How would you keep a history of counters?
- What if the seller changes the floor while an offer is pending?

</details>

### Q5 · DSA · Backtracking · Medium

Given an integer array that may contain duplicates, return all possible subsets without duplicate subsets. Example: [1,2,2] gives [[],[1],[1,2],[1,2,2],[2],[2,2]]. Explain the backtracking, exactly how duplicates are skipped, the complexity, and write the code.

<details><summary>Must cover</summary>

- Sort first so equal values are adjacent
- Backtrack(start, path): add path to result, loop i from start
- Skip when i > start and nums[i] == nums[i-1]
- O(n * 2^n) time in the worst case, O(n) recursion depth
- Why a set of vectors is a worse fix

**Likely follow-ups**

- How would you return only subsets of size k?
- How does the same skip rule work in Combination Sum II?

</details>

### Q6 · Java & Spring · CompletableFuture · Medium

An order-details API must call pricing, inventory and shipping services. Called one after another it takes 900 ms. Show how you'd call them in parallel with CompletableFuture, give each a timeout and a fallback, and which thread pool you'd use.

<details><summary>Must cover</summary>

- supplyAsync for each call on a dedicated bounded executor (not the common pool for blocking I/O)
- allOf / thenCombine to join results
- orTimeout / completeOnTimeout per call; exceptionally/handle for fallbacks
- Total latency ~ slowest call instead of the sum
- Propagate tenant/trace context to the pool threads (TaskDecorator or explicit passing)

**Likely follow-ups**

- What happens if you call join() inside another async stage?
- How would virtual threads (Java 21) change this?

</details>

## 2. DSA (45 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **[Subsets](https://leetcode.com/problems/subsets/) (#78)** · pattern: Backtracking: include / exclude
    - What to say: Recursive choose/not-choose, or loop-from-start building the path. 2^n subsets, O(n * 2^n) total. First backtracking problem in your repo.
    - File: [`dsa/subsets.cpp`](dsa/subsets.cpp)
- [ ] **[Subsets II](https://leetcode.com/problems/subsets-ii/) (#90)** · pattern: Backtracking with duplicate skip
    - What to say: Sort first, then in the loop skip nums[i] == nums[i-1] when i > start. Explain why that removes duplicates without a set.
    - File: [`dsa/subsets-ii.cpp`](dsa/subsets-ii.cpp)

## 3. SOLID + core patterns in Java (45 min)

- [ ] S, O, L, I, D with one example each from your own code
- [ ] Strategy, Factory, Builder, Observer, State, Decorator: one Java snippet each
- [ ] Singleton: enum vs double-checked locking; why Spring beans make it rare
- [ ] Composition over inheritance, interface vs abstract class
- [ ] Where your code already uses patterns: AbstractRoutingDataSource, Spring events, payment providers

**Explain out loud in 2 minutes**

- [ ] How would you add PayPal next to Stripe without touching the Stripe class?
- [ ] Give a Liskov violation and how you'd fix it

**Output:** patterns.md in this folder with the 6 snippets

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

[<- Day 7](../day07/README.md) · [All days](../README.md) · [Day 9 ->](../day09/README.md)
