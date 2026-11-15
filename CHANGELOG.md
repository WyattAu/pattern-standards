# CHANGELOG

## 2026-11-15

- Canon founded: PATTERN-CORE (doctrine, 24-pattern baseline tier,
  8 refusals, adoption procedure) plus the full catalog:
  foundations T1–T50 in five `references/foundations-*.md` files,
  field constructs P1–P50 in five `references/field-*.md` files,
  frontier constructs X1–X7 in `references/frontier.md`.
- Series scheme: T (proven structural primitives), P (problem-driven
  field constructs, numbered per source material), X (research-grade,
  pilot+ADR only). Cross-references use bare series IDs and resolve.
- `wyattau-patterns` skill projection landed via standards-dist
  (rev-pinned 8227cd1); installed at
  `~/.config/opencode/skills/wyattau-patterns`.
- Register conformance pass: 89 em-dashes removed estate-canon-wide
  (PRESENT PR-6/PR-8, DOC-STYLE character rule); `voice-lint.py
  --strict` now passes on all canon Markdown (AGENTS.md rule 8).
- ADR-0001 opened: X5 conservation-operator pilot contract (PROPOSED).
- Task routing graph added (PATTERN-CORE §9, `references/decision-graph.md`):
  18 task nodes with MANDATORY sets, ASK branches, REFUSE edges; pattern
  selection is now a deterministic traversal. Canon `llms.txt` created
  (AGENTS rule 7).
- Field series expanded P51–P63 (13 patterns, all Proven): runtime
  operations (circuit breaker, bulkhead, DLQ, webhook receiver
  hardening, graceful drain, trace context) in `field-operations.md`;
  data integrity and evolution (optimistic concurrency, checkpointed
  backfill, contract tests, strangler fig, anti-corruption layer,
  time-ordered IDs, bucketed rollups) in `field-data-evolution.md`.
  Baseline tier grows to 25 (P51). Graph grows to 21 nodes (N19-N21)
  plus four worked chain examples.
