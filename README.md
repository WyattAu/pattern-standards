# pattern-standards

The WyattAu canon for design patterns: 120 constructs across three
series, 8 named refusals, and a 25-pattern baseline tier, per
2026-11 standards. Projection source for the `wyattau-patterns`
skill (standards-dist); consumable directly by reading
[`PATTERN-CORE.md`](PATTERN-CORE.md).

| Series | Range | Stance | Patterns |
|---|---|---|---|
| Foundations (T) | T1–T50 | proven primitives, default-adopt where domain applies | 50 |
| Field constructs (P) | P1–P63 | problem-driven, adopt on named trigger | 63 |
| Frontier (X) | X1–X7 | research-grade, pilot + ADR only | 7 |

**120 patterns. 8 named refusals. 25 baseline-tier defaults.**

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
| [`field-security.md`](references/field-security.md) | RLS scopes, wide events, crypto-shredding, burn-rate gates (P41–P50) |
| [`field-operations.md`](references/field-operations.md) | circuit breaker, bulkheads, DLQs, webhook receivers, drain, trace context (P51–P54, P62–P63) |
| [`field-data-evolution.md`](references/field-data-evolution.md) | OCC, backfills, contract tests, strangler, ACLs, IDs, rollups (P55–P61) |
| [`frontier.md`](references/frontier.md) | epistemic types, choreography, constraint manifolds, spec-as-source (X1–X7) |
| [`decision-graph.md`](references/decision-graph.md) | task-type routing: 18 nodes, MANDATORY sets, ASK branches, REFUSE edges (§9) |

## Status

CURRENT. Changes require a dated `CHANGELOG.md` entry; series-level
changes, baseline-tier changes, and new refusals require an ADR in
`adr/`.

## Adoption

Per-repo adoption follows PATTERN-CORE §5: find patterns by failure
mode, baseline tier is default-adopt, field patterns record their
trigger in an ADR, frontier patterns stay pilot-only until a second
pilot succeeds.
