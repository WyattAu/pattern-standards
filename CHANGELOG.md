# CHANGELOG

## 2026-11-15
- ADR-0001 X5 pilot started: operator surface shipped in accessctl 0.2.0; escape audit + property-test criteria green (evidence in adr/0001 §4a); pending: consumer feature review + nightly soak.

- Graph traversal became a script: `scripts/route.py --task|--node|
  --list` parses decision-graph.md's fixed K:/M:/A:/R: node format and
  emits the node block (AGENTS.md rule 10; skill-forge doctrine:
  deterministic computation is a script, not prose). decision-graph.md
  rewritten in that format (3,086 to ~2,300 words); check-canon gained
  the block-format check; build.sh now vendors route.py into the skill.
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
- Field series expanded P64–P79 (16 patterns, all Proven) across three
  new pillars: test strategy (`field-testing.md`: property-based,
  golden masters, mutation, fuzzing, builders, flake quarantine), API
  surface (`field-api.md`: tolerant reader, schema registry, error
  envelope, list contract, deprecation protocol), and deployment
  (`field-deployment.md`: canary analysis, blue-green, shadow traffic,
  exposure cohorts, content-addressed attested artifacts). Graph grows
  to 24 nodes (N22 test suite, N23 API surface, N24 deploy/release).
- Field series expanded P80–P92 (13 patterns) across two more pillars:
  compliance and privacy (`field-compliance.md`: consent facts, DSAR
  pipeline, purpose tagging, hash-chained audit, workload identity,
  zero-downtime rotation, break-glass) and execution
  (`field-execution.md`: order slicing, smart routing, fill
  reconciliation, TCA, data-budget adaptation, kill switch). One
  Emerging stamp (P82), twelve Proven. Graph grows to 27 nodes (N25
  PII processing, N26 trading execution, N27 secrets/identity).
- Gap-close round P93–P102 (10 patterns, all Proven) from the
  industry-gap analysis (avionics/defense, LLVM, NVIDIA, SpaceX,
  Netflix, Palantir): safety and margins (`field-safety.md`: P93
  fail-operational modes, P94 watchdog + heartbeat, P95 2oo3 voting,
  P100 margin budgets), verification discipline
  (`field-verification.md`: P96 verify-every-layer, P97 auto-blessed
  goldens, P99 MC/DC gates), plus P98 dress-rehearsal gate
  (`field-deployment.md`), P101 scheduled chaos experiments
  (`field-operations.md`), P102 ontology + lineage
  (`field-data-evolution.md`). Graph grows to 29 nodes (N28 degraded
  modes, N29 release rehearsal). CORE §1 gains the Vulkan/LLVM
  grounding line. Canon gates mechanized: `scripts/check-canon.py`
  and `make ci` (AGENTS.md rule 9); catalog split to
  `references/catalog.md`.
- Third expansion round P103–P119 (17 patterns, all Proven) closing
  the residual gap analysis: networking and time discipline
  (`field-networking.md`: deadline propagation, DNS discipline,
  overlap-guarded jobs), data-layer discipline (`field-data-layer.md`:
  session hygiene, consumer inbox, sticky read-after-write), ML
  lifecycle (`field-ml.md`: train/serve skew guards, model registry,
  experiment bucketing + SRM), plus appends: query-count assertions
  (testing), data contracts (data evolution), JWT validation, crypto
  agility, upload hardening (security), restore drills and cardinality
  budgets (operations), cost budgets (safety). Refusals grow to 12
  (R9 org-process, R10 framework idioms, R11 hardware co-design, R12
  experiment peeking). Graph grows to 31 nodes (N30 time budgets, N31
  dataset publishing). `check-canon` now also enforces refusal-count
  claims.
- Canon gates mechanized: `scripts/check-canon.py` (ID resolution,
  catalog mirror, node-set equality, count/range/node-count claims) and
  a Makefile (`make ci` = lint + check), AGENTS.md rule 9. Catalog
  tables moved from PATTERN-CORE §6-§8 to `references/catalog.md`
  (CORE drops to ~1300 words; pointers updated).
- Industry-gap round closed: P93–P102 (safety, verification, rehearsal,
  chaos, margins, ontology + lineage), graph to 29 nodes (N28, N29),
  CORE §1 grounding line added. Gate caught and forced three claim
  drifts on first run (stale P range, two stale node counts).
