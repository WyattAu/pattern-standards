# pattern-standards

The WyattAu canon for design patterns: 176 constructs across three
series, 12 named refusals, and a 25-pattern baseline tier, per
2026-11 standards. Projection source for the `wyattau-patterns`
skill (standards-dist); consumable directly by reading
[`PATTERN-CORE.md`](PATTERN-CORE.md).

| Series | Range | Stance | Patterns |
|---|---|---|---|
| Foundations (T) | T1–T50 | proven primitives, default-adopt where domain applies | 50 |
| Field constructs (P) | P1–P119 | problem-driven, adopt on named trigger | 119 |
| Frontier (X) | X1–X7 | research-grade, pilot + ADR only | 7 |

**176 patterns. 12 named refusals. 25 baseline-tier defaults.**

Doctrine lives in PATTERN-CORE §1: every pattern here removes a
failure mode from human vigilance and embeds it in a type, an
algebraic operator, a compiler pass, or a runtime invariant. Deep
practice per domain lives in [`references/`](references/):

| File | Contents |
|---|---|
| [`foundations-types.md`](references/foundations-types.md) | parse-don't-validate, typestate, session types, OCap, effects (T1–T10) |
| [`foundations-execution.md`](references/foundations-execution.md) | structured concurrency, supervision, STM, salsa, durable coroutines (T11–T20) |
| [`foundations-state.md`](references/foundations-state.md) | event sourcing, CRDTs, bitemporal, double-entry, e-graphs (T21–T30) |
| [`foundations-distributed.md`](references/foundations-distributed.md) | sagas, outbox, fencing, DST, gossip, tail-latency (T31–T42) |
| [`foundations-interfaces.md`](references/foundations-interfaces.md) | declarative UI, HATEOAS, Datalog, constrained decoding, agent sandboxes (T43–T50) |
| [`field-fullstack.md`](references/field-fullstack.md) | version lenses, parity gates, snapshot cursors, temporal anchors (P1–P10) |
| [`field-numerical.md`](references/field-numerical.md) | partition operators, units, as-of guards, ledger checksums (P11–P20) |
| [`field-concurrency.md`](references/field-concurrency.md) | staleness contracts, retry budgets, criticality shedding, fault injection (P21–P30) |
| [`field-agentic.md`](references/field-agentic.md) | prompt quarantine, cascades, memoization, spend leases (P31–P40) |
| [`field-security.md`](references/field-security.md) | RLS scopes, wide events, crypto-shredding, JWT discipline, crypto agility, upload hardening (P41–P50, P114–P116) |
| [`field-operations.md`](references/field-operations.md) | circuit breaker, bulkheads, DLQs, webhook receivers, drain, trace context, chaos experiments, restore drills, cardinality budgets (P51–P54, P62–P63, P101, P117–P118) |
| [`field-data-evolution.md`](references/field-data-evolution.md) | OCC, backfills, contract tests, strangler, ACLs, IDs, rollups, ontology + lineage (P55–P61, P102) |
| [`field-testing.md`](references/field-testing.md) | property tests, golden masters, mutation, fuzzing, builders, flake quarantine, query-count gates (P64–P69, P109) |
| [`field-api.md`](references/field-api.md) | tolerant reader, schema registry, error envelope, list contract, deprecation (P70–P74) |
| [`field-deployment.md`](references/field-deployment.md) | canary, blue-green, shadow traffic, cohorts, attested artifacts, dress rehearsal (P75–P79, P98) |
| [`field-compliance.md`](references/field-compliance.md) | consent facts, DSAR pipeline, purpose tags, hash-chained audit, workload identity, rotation, break-glass (P80–P86) |
| [`field-execution.md`](references/field-execution.md) | order slicing, routing, fill reconciliation, TCA, data budgets, kill switch (P87–P92) |
| [`field-safety.md`](references/field-safety.md) | degraded modes, watchdogs, 2oo3 voting, margin budgets, cost budgets (P93–P95, P100, P119) |
| [`field-verification.md`](references/field-verification.md) | verify-every-layer, auto-blessed goldens, MC/DC gates (P96–P97, P99) |
| [`field-networking.md`](references/field-networking.md) | deadline propagation, DNS discipline, overlap-guarded cron (P103–P105) |
| [`field-data-layer.md`](references/field-data-layer.md) | session hygiene, consumer inbox, sticky read-after-write (P106–P108) |
| [`field-ml.md`](references/field-ml.md) | train/serve skew guards, model registry, experiment bucketing + SRM (P111–P113) |
| [`frontier.md`](references/frontier.md) | epistemic types, choreography, constraint manifolds, spec-as-source (X1–X7) |
| [`decision-graph.md`](references/decision-graph.md) | task-type routing: 31 nodes, MANDATORY sets, ASK branches, REFUSE edges (§6) |
| [`catalog.md`](references/catalog.md) | the full ID catalog with maturity stamps (mirrors all reference headings) |

## Status

CURRENT. Changes require a dated `CHANGELOG.md` entry; series-level
changes, baseline-tier changes, and new refusals require an ADR in
`adr/`.

## Adoption

Per-repo adoption follows PATTERN-CORE §5: find patterns by failure
mode, baseline tier is default-adopt, field patterns record their
trigger in an ADR, frontier patterns stay pilot-only until a second
pilot succeeds.
