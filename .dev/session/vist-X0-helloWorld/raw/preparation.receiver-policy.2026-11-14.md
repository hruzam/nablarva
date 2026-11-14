---
kind: candidate-policy-and-oracle-appendix
author: nablarva.cartan
date: 2026-11-14
scope: documentary U03–U06 reasoning only
adoption: none; no envelope, receiver component owner, shared schema or implementation selected
---

# Receiver policy is separate from VIST observations

The carry-over includes expiry, misaddress/path scope, request authority and finite hop/retry
criteria. These concern a **candidate receiver/controller policy**, not properties a passive sensor
can establish. Neither carrier acceptance nor an idle/busy transition proves that a request was
authorized, executed safely or completed. No field names, schema, policy owner or transport are
adopted here.

Before U03–U06 execution, a future scoped design must answer:

| Question to freeze | Independent evidence needed |
|---|---|
| What identifies this logical request, recipient and its deduplication domain? | Independently bound target/native lifetime, exact request and actual receiver work/attempt correlation; pane label or nonce alone is not authentication |
| Which clock, expiry interpretation and allowed path/action scope apply? | Chosen clock oracle and request scope, native refusal/result, independently checked authorized side effects; byte-pointer validation is insufficient |
| What can the pointer authorize, and what needs a separate native action permission? | Exact user/receiver scope, actual native tools/results and disclosed interventions; tool permission and semantic authorization are separate questions |
| Which clean failures permit a retry, and how do hop/attempt budgets terminate? | Exact parent/child IDs, prior submission certainty, native duplicate/work counts and a finite observation interval; preserve uncertainty across carriers |

Expected refusal needs an affirmative, correlated refusal or bounded explicit unknown; missing
receipt alone is not a refusal. An authorized counterpart tests that a refusal is discriminating,
not just a broken receiver. A pending native security/permission decision is left to Majkee; no
automatic answer, alternate executor, forced resume or scope renewal is part of the oracle.

The six-row matrix supplies candidate finite bounds, not released behavior. Authoritative scope,
concrete schemas, execution permissions, independent instrumentation and operation-specific L21
release must precede a live test or implementation. Historical semantic/grant/notice examples retain
their limited meaning and do not receive new PASSes from this appendix.
