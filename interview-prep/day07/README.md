# Day 7 · Thu 5 Nov 2026 · AWS: SQS, Lambda and Step Functions

**Goal:** Answer AWS questions from your own production experience, with the limits and failure modes interviewers probe.

| Time | Block | What |
| --- | --- | --- |
| 30 min | 1. Mock interview | 6 questions below (also on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2) from 10:30 AM). Say it out loud first, then type it on the page |
| 45 min | 2. DSA | Validate Binary Search Tree, Kth Smallest Element in a BST (C++, files in `dsa/`) |
| 45 min | 3. AWS deep-dive tied to your resume | Checklist below |
| 5 min | 4. Log | Fill the log at the bottom and one row in [`../LOG.md`](../LOG.md) |

## 1. Mock interview (30 min)

Answer each in about 4 minutes, out loud, as if an interviewer is listening. Type your answer on the [mock page](https://claude.ai/artifact/MxHsnw3hijPZhQRGoedXo2); it is graded the next morning on the 1-4 hiring scale. Open 'Must cover' only after answering.

### Q1 · Resume deep-dive · Billing orchestration · Hard

Draw (in words) the Step Functions state machine for your billing platform: the states from collecting shipped data to the PDF invoice and Stripe charge. Then: the Stripe charge succeeds but the next step that records it in MySQL fails. What does your workflow do?

<details><summary>Must cover</summary>

- Concrete states: gather data, compute totals, generate PDF (Puppeteer), charge via Stripe, record, notify
- Retry with backoff on transient errors; Catch to a failure/compensation path
- Charge is idempotent (idempotency key per invoice), so a retry of the charge step can't double charge
- Record step retried; if it keeps failing, flag for reconciliation instead of refunding blindly
- Standard workflow for long-running, auditable execution history

**Likely follow-ups**

- Why Step Functions instead of chaining Lambdas through SQS?
- How do you re-run billing for one tenant only?

</details>

### Q2 · AWS · SQS FIFO vs Standard · Medium

For order-lifecycle events (created, paid, shipped), would you use an SQS Standard or FIFO queue? Explain ordering, duplicates and throughput for each, and what the message group id would be.

<details><summary>Must cover</summary>

- Standard: at-least-once, best-effort ordering, very high throughput
- FIFO: ordered within a message group, exactly-once processing within the deduplication window (5 minutes)
- Message group id = order id, so events for one order are ordered while different orders process in parallel
- FIFO throughput limits (higher with batching or high-throughput mode); a failing message blocks its group
- Consumers still need idempotency either way

**Likely follow-ups**

- What happens to a FIFO group when one message keeps failing?
- How would you handle ordering with a Standard queue?

</details>

### Q3 · AWS · SQS + Lambda failures · Medium

A Lambda consumes SQS in batches of 10. One message in the batch has bad data and throws. What happens to the other 9 by default, how do you change that, and how do you get bad messages out of the way safely?

<details><summary>Must cover</summary>

- Default: the whole batch is considered failed and all 10 become visible again
- ReportBatchItemFailures: return only the failed message ids so the rest are deleted
- maxReceiveCount on the queue's redrive policy moves poison messages to a DLQ
- Alarm on DLQ depth; redrive from DLQ back to source after a fix
- Visibility timeout at least 6x the function timeout for Lambda event source mappings

**Likely follow-ups**

- How do you make the 9 good messages safe if they are retried anyway?
- How would you replay only some DLQ messages?

</details>

### Q4 · HLD · Monitoring job · Medium

Your EventBridge-scheduled Lambda checks per-tenant shipped-data freshness and emails alerts via SES. Scale it to 500 tenants with different billing schedules. How do you design it so it finishes on time, doesn't spam alerts, and doesn't hammer the database?

<details><summary>Must cover</summary>

- Fan out: scheduler enqueues one message per tenant to SQS; worker Lambdas process with bounded concurrency
- Read from a replica or a summary table; one indexed query per tenant
- Alert state stored (last alerted, open/closed) to deduplicate and send one alert until resolved
- Per-tenant thresholds/schedules stored in config
- Observability: job duration, failures, a heartbeat alarm if the job itself doesn't run

**Likely follow-ups**

- How do you test it without emailing real customers?
- What if a tenant's database is down during the check?

</details>

### Q5 · DSA · BST bounds · Medium

Check whether a binary tree is a valid BST without storing the inorder traversal in an array. Node values can be any 32-bit int, including INT_MIN and INT_MAX. Explain the approach, its space use, and write the code.

<details><summary>Must cover</summary>

- DFS passing (low, high) bounds; left child gets high = node.val, right gets low = node.val
- Strict inequalities per the problem's definition
- Use long or nullable bounds so INT_MIN/INT_MAX nodes aren't rejected
- O(n) time, O(h) recursion stack
- Alternative: iterative inorder comparing with the previous value only

**Likely follow-ups**

- Why is checking only node vs its children wrong?
- How would you find the two swapped nodes in an almost-BST?

</details>

### Q6 · AWS · IAM · Medium

Write (in words) a least-privilege IAM setup for a Lambda that reads report templates from one S3 prefix, writes jobs to one SQS queue, and reads one secret from Secrets Manager. What would you avoid, and how do resource policies fit in?

<details><summary>Must cover</summary>

- Execution role with only s3:GetObject on arn:...:bucket/templates/*, sqs:SendMessage on the one queue ARN, secretsmanager:GetSecretValue on the one secret
- No wildcards like s3:* or Resource *
- KMS decrypt permission if the secret/queue uses a customer-managed key
- Resource-based policies (bucket policy, queue policy) for cross-account or extra restriction
- Basic logging permissions for CloudWatch Logs; review with IAM Access Analyzer

**Likely follow-ups**

- Identity-based vs resource-based policy: when do both need to allow?
- How do you give a Lambda access to a bucket in another account?

</details>

## 2. DSA (45 min, C++)

For each: say brute force -> pattern -> complexity out loud BEFORE coding, then code, then test 2 edge cases. Fill the header in the file.

- [ ] **[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (#98)** · pattern: DFS with min/max bounds
    - What to say: Your inorder-into-a-vector works but uses O(n) extra space. Pass (low, high) bounds down; use long (or nullable bounds) so INT_MIN/INT_MAX values pass. O(n) time, O(h) stack.
    - File: [`dsa/validate-binary-search-tree.cpp`](dsa/validate-binary-search-tree.cpp)
- [ ] **[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (#230)** · pattern: Inorder with early stop
    - What to say: Don't collect the whole tree. Iterative inorder with a stack, decrement k, return when it hits 0. O(h + k). Follow-up: frequent inserts -> store subtree sizes.
    - File: [`dsa/kth-smallest-element-in-a-bst.cpp`](dsa/kth-smallest-element-in-a-bst.cpp)

## 3. AWS deep-dive tied to your resume (45 min)

- [ ] SQS: visibility timeout, DLQ + maxReceiveCount, long polling, Standard vs FIFO, message groups
- [ ] Lambda + SQS: batch size, partial batch failures (ReportBatchItemFailures), concurrency limits
- [ ] Step Functions: Standard vs Express, Retry and Catch, compensation steps
- [ ] API Gateway: 29 s integration timeout, throttling, why your report API went async
- [ ] Cognito: ID vs access vs refresh tokens, JWT validation via JWKS

**Explain out loud in 2 minutes**

- [ ] Draw your billing state machine and say what happens when the Stripe step times out
- [ ] How do you stop one bad message blocking a whole SQS batch?

**Output:** Sketch the billing state machine on paper and photo it into this folder

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

[<- Day 6](../day06/README.md) · [All days](../README.md) · [Day 8 ->](../day08/README.md)
