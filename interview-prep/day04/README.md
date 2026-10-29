# Day 4 · Mon 2 Nov 2026 · Node.js event loop and Lambda

**Goal:** Explain the event loop well enough to predict output order, and fix two two-pointer/stack problems.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 45 min | 2. DSA | Min Stack, 3Sum (C++, files in `dsa/`) |
| 45 min | 3. Node.js event loop and async | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · Lambda platform · Medium

You built services across a 40+ function Lambda platform with independent deployments. How was shared code (DB clients, auth, models) packaged, how did you deploy one function without breaking others, and how did you trace a request that crossed several functions?

<details><summary>Must cover</summary>

- Shared code as an internal npm package or Lambda layer, versioned; trade-offs of each
- AWS SAM templates per service/stack, CodeBuild pipeline, deploy only changed stacks
- Backward-compatible contracts for events and APIs; versioned event schemas
- Tracing: correlation id passed through headers and SQS message attributes, structured logs, X-Ray
- Reusing DB connections outside the handler; RDS Proxy for connection limits

**Likely follow-ups**

- How did you keep 40 functions on the same Node version?
- What made you choose Lambda over containers here?

</details>

### Q2 · Node.js · Event loop order · Medium

What does this print, and why?  
  
console.log('A');  
setTimeout(() => console.log('B'), 0);  
setImmediate(() => console.log('C'));  
Promise.resolve().then(() => console.log('D'));  
process.nextTick(() => console.log('E'));  
console.log('F');

<details><summary>Must cover</summary>

- Synchronous first: A, F
- process.nextTick queue runs before promise microtasks: E, then D
- Then timers vs check phase: B and C, whose order is not guaranteed from the main module (it depends on process timing)
- Inside an I/O callback, setImmediate always runs before setTimeout(0)
- Names the event loop phases: timers, poll, check

**Likely follow-ups**

- Why can heavy use of process.nextTick starve I/O?
- Where do async/await continuations run?

</details>

### Q3 · Node.js · Blocking the loop · Medium

An Express API generates Excel and PDF reports in the request handler. When one large report runs, every other endpoint's latency jumps. Explain why, how you'd confirm it, and three ways to fix it.

<details><summary>Must cover</summary>

- Node runs JS on one thread; CPU-heavy work blocks the event loop for every request
- Confirm with event-loop lag metrics (perf_hooks monitorEventLoopDelay), profiling (clinic, --prof)
- Fix 1: move generation to worker_threads or a worker pool (e.g. piscina)
- Fix 2: make it async: return 202, queue the job (SQS), process in a separate worker/Lambda (what you built)
- Fix 3: stream output instead of building in memory; paginate DB reads

**Likely follow-ups**

- How is worker_threads different from cluster mode?
- Why doesn't async/await alone fix this?

</details>

### Q4 · LLD · Rate limiter · Medium

Design the classes for an in-process rate limiter library that supports token bucket and sliding-window algorithms, configurable per API and per user. Show the interface, the classes, and how you keep it thread-safe.

<details><summary>Must cover</summary>

- RateLimiter interface: allow(key) -> boolean (or a result with retry-after)
- TokenBucketLimiter and SlidingWindowLimiter implementations (Strategy); a factory or config picks one per API
- Per-key state in a ConcurrentHashMap; refill computed lazily from timestamps instead of a timer thread
- Thread safety per key: synchronized on the bucket, or atomics/CAS
- Clock injected for testing; eviction of idle keys

**Likely follow-ups**

- How would you move this to Redis for many instances?
- Token bucket vs leaky bucket: what's the difference?

</details>

### Q5 · DSA · Two pointers · Medium

Given an integer array, return all unique triplets [a, b, c] with a + b + c = 0. Example: [-1,0,1,2,-1,-4] gives [[-1,-1,2],[-1,0,1]]. n up to 3000. Give the brute force, then the sort + two-pointer solution, explain exactly how you avoid duplicate triplets, and write the code.

<details><summary>Must cover</summary>

- Brute force O(n^3); hashmap approach O(n^2) extra space
- Sort, fix i, left = i+1, right = n-1, move by the sign of the sum
- Skip duplicate values of i; after a match, move left and right past equal values
- Early break when nums[i] > 0
- O(n^2) time, O(1) extra space besides output

**Likely follow-ups**

- How would you solve 3Sum Closest?
- How does this generalise to 4Sum?

</details>

### Q6 · AWS · Lambda cold starts · Medium

Users complain the first login of the morning takes 3-4 seconds on your Lambda-based auth API. Explain what causes Lambda cold starts, what makes them worse, and the options you have to reduce them, with trade-offs.

<details><summary>Must cover</summary>

- Cold start = new execution environment: download code, start runtime, run init code outside the handler
- Worse with large bundles, heavy init (SDK clients, DB connections), Java runtimes, more memory pressure
- Fixes: smaller bundles (esbuild, tree-shaking), lazy init, more memory (more CPU)
- Provisioned concurrency for predictable traffic (costs money even when idle); SnapStart for Java
- Measure with Init Duration in CloudWatch logs / X-Ray before and after

**Likely follow-ups**

- Does a Lambda in a VPC still add big cold-start time today?
- When would you move this API off Lambda?

</details>

## 2. DSA (45 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **[Min Stack](https://leetcode.com/problems/min-stack/) (#155)** · pattern: Stack of (value, min so far)
    - What to say: Push pairs (x, min(x, currentMin)) or keep a second stack of mins. All operations O(1). Missing from your week 3.
    - File: [`dsa/min-stack.cpp`](dsa/min-stack.cpp)
- [ ] **[3Sum](https://leetcode.com/problems/3sum/) (#15)** · pattern: Sort + two pointers
    - What to say: Your hashmap version works but is O(n^2 log n) with a map. Sort, fix i, move left/right inward by the sum's sign, skip duplicates on i, left and right. O(n^2), O(1) extra.
    - File: [`dsa/3sum.cpp`](dsa/3sum.cpp)

## 3. Node.js event loop and async (45 min)

- [ ] Event loop phases: timers, pending callbacks, poll, check, close
- [ ] Microtasks (Promise.then, queueMicrotask) vs process.nextTick vs setImmediate vs setTimeout(0)
- [ ] async/await error handling, Promise.all vs allSettled vs race
- [ ] What blocks the loop: sync crypto, JSON.parse of huge payloads, CPU loops
- [ ] worker_threads vs cluster vs child_process

**Explain out loud in 2 minutes**

- [ ] Predict the output order of a script mixing all four timer/microtask kinds
- [ ] Why does one slow request make every request on a Node server slow?

**Output:** Write event-loop.js in this folder that prints the order, run it, and check your prediction

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

[<- Day 3](../day03/README.md) · [All days](../README.md) · [Day 5 ->](../day05/README.md)
