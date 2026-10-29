# Day 5 · Tue 3 Nov 2026 · Spring Boot internals

**Goal:** Explain what Spring does at startup and on each request, and close two missing graph/greedy problems.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 45 min | 2. DSA | Clone Graph, Jump Game (C++, files in `dsa/`) |
| 45 min | 3. Spring Boot internals | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · Spring Security + Cognito · Medium

A request hits your Spring Boot API with a Cognito JWT. Walk through the Spring Security filter chain until the controller runs, how the token is validated, and how @PreAuthorize and your custom filter limited sales reps to their own customers.

<details><summary>Must cover</summary>

- Filter chain: security filters run before DispatcherServlet; bearer token filter -> authentication -> SecurityContext
- JWT validation: signature against Cognito JWKS (cached), iss, exp, token_use (access vs id), client_id/aud
- Authorities mapped from cognito:groups or custom claims
- @PreAuthorize with method security (proxy), e.g. hasRole or a custom bean check
- Object-level check (IDOR fix): rep can only load customers assigned to them, enforced in the query/service, not only the UI

**Likely follow-ups**

- Why validate token_use?
- Where would you put the tenant id check so no endpoint can forget it?

</details>

### Q2 · Java & Spring · IoC and scopes · Medium

Explain dependency injection and bean scopes in Spring. A singleton OrderService injects a prototype-scoped PriceCalculator, but every request seems to get the same calculator instance. Why, and how do you fix it?

<details><summary>Must cover</summary>

- IoC container creates and wires beans; constructor injection preferred (immutability, testability)
- Scopes: singleton (default), prototype, request, session
- Prototype is injected once when the singleton is created, so it never changes
- Fixes: ObjectProvider/Provider<T>.getObject(), @Lookup method, or a scoped proxy
- Thread-safety note: singletons must be stateless or safely shared

**Likely follow-ups**

- Field vs constructor injection: why does it matter for circular dependencies?
- What does @Scope(proxyMode = TARGET_CLASS) do?

</details>

### Q3 · Java & Spring · Auto-configuration · Medium

What happens between running java -jar app.jar and your Spring Boot app serving its first request? Include how auto-configuration decides which beans to create.

<details><summary>Must cover</summary>

- main -> SpringApplication.run: environment, application context creation
- Component scanning from the @SpringBootApplication package
- Auto-configuration classes from starters, guarded by @ConditionalOnClass / OnMissingBean / OnProperty
- Bean creation, injection, post-processors (proxies for @Transactional, @Async), @PostConstruct
- Embedded Tomcat starts, DispatcherServlet ready; --debug prints the condition report

**Likely follow-ups**

- How do you override an auto-configured DataSource?
- How could you speed up startup of a big app?

</details>

### Q4 · LLD · Notification service · Medium

Design the classes for a notification module that sends order updates by email (SES), SMS and push, with templates per event type, user channel preferences, and retries. Show the main interfaces and where patterns fit.

<details><summary>Must cover</summary>

- NotificationChannel interface with Email/SMS/Push implementations (Strategy); a factory/registry by channel type
- Template resolver per event type and locale; data model for the message
- Preference service decides which channels per user
- Retry with backoff, idempotency key per notification, dead-letter for permanent failures
- Async: publish an event, consumer sends; Observer or Spring events internally

**Likely follow-ups**

- How do you stop a user getting the same SMS twice after a retry?
- How would you add WhatsApp?

</details>

### Q5 · DSA · Graph clone · Medium

Given a reference to a node in a connected undirected graph (each node has a value and a list of neighbours), return a deep copy of the graph. Graphs can contain cycles. Explain the approach and complexity, and write the code.

<details><summary>Must cover</summary>

- Hashmap original -> clone, created before exploring neighbours
- DFS or BFS; for each neighbour, reuse its clone if already in the map
- Handles cycles and self-loops because of the map
- O(V + E) time, O(V) space
- Edge case: null input

**Likely follow-ups**

- Recursive DFS vs BFS: which risks a stack overflow on 10^5 nodes?
- How would you clone a graph with random pointers (like Copy List with Random Pointer)?

</details>

### Q6 · Databases · JPA N+1 · Medium

An endpoint lists 50 sales orders with their line items and takes 2 seconds. The logs show 51 SQL queries. Explain the N+1 problem in JPA/Hibernate, how you'd confirm it, and the fixes with their trade-offs.

<details><summary>Must cover</summary>

- Lazy association loaded per parent when accessed: 1 query for orders + N for items
- Confirm with SQL logging/statistics or a query counter in tests
- Fix: JOIN FETCH or @EntityGraph for this query
- Alternative: @BatchSize / hibernate.default_batch_fetch_size to load in IN batches
- Watch out: fetch join + pagination warns and paginates in memory; consider DTO projections

**Likely follow-ups**

- Why not make the association EAGER?
- How would you catch N+1 in CI?

</details>

## 2. DSA (45 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **[Clone Graph](https://leetcode.com/problems/clone-graph/) (#133)** · pattern: DFS/BFS + hashmap old -> new
    - What to say: Map each original node to its copy before visiting neighbours, so cycles reuse the copy. O(V + E). Missing from your week 5.
    - File: [`dsa/clone-graph.cpp`](dsa/clone-graph.cpp)
- [ ] **[Jump Game](https://leetcode.com/problems/jump-game/) (#55)** · pattern: Greedy farthest reach
    - What to say: Track the farthest index reachable; if i ever exceeds it, return false. O(n), O(1). Mention the DP version is O(n^2) and why greedy is safe.
    - File: [`dsa/jump-game.cpp`](dsa/jump-game.cpp)

## 3. Spring Boot internals (45 min)

- [ ] IoC container, DI by constructor vs field, bean scopes
- [ ] Bean lifecycle: instantiate, inject, @PostConstruct, proxies, @PreDestroy
- [ ] Auto-configuration: starters, @Conditional annotations, how to see the report (--debug)
- [ ] @Transactional proxies, propagation, rollback rules (you answered this on Day 1)
- [ ] JPA N+1 problem and fixes: fetch join, @EntityGraph, batch size

**Explain out loud in 2 minutes**

- [ ] What happens between 'java -jar app.jar' and the first request being served?
- [ ] Why does a singleton bean holding a prototype bean keep the same instance?

**Output:** Optional: tiny Spring Boot app that shows the @Transactional self-invocation bug

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

[<- Day 4](../day04/README.md) · [All days](../README.md) · [Day 6 ->](../day06/README.md)
