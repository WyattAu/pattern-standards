# ADR-0001: X5 pilot (conservation-spanning domain operators)

Status: PILOT (in progress), started 2026-11-16. Originally PROPOSED 2026-11-15. Pilot contract for frontier construct X5
(`references/frontier.md`); adoption of X5 beyond the pilot requires the
evidence defined in §4.

## 1. Context

X5 (gauge-symmetric domain operators) claims: a domain module that
exposes only invariant-spanning group actions makes conservation by
construction, removing the post-hoc validator class of bugs. The
pattern has proven special cases (double-entry ledgers T27, CRDT
semilattices T23, OCap attenuation T8) but no estate pilot on a
general quota/entitlement surface. PATTERN-CORE §5 gates X-series
adoption on one bounded pilot plus this ADR.

## 2. Scope

Candidate surface: `accessctl` (capability grants are inherently
conserved: an issued grant is split, transferred, attenuated, or
revoked; it never appears from nothing). Secondary candidate if
accessctl has no near-term work: quota accounting in a broker/crawl
budget module.

The pilot wraps one module; it does not migrate existing storage.

## 3. Decision

The pilot module exposes exactly six operators and no setters:

| Operator | Signature shape | Conservation effect |
|---|---|---|
| issue | principal -> Grant | +1 active |
| split | Grant -> (Grant, Grant) | count +1, amount conserved |
| transfer | (Grant, principal) -> Grant | holder changes, amount conserved |
| attenuate | Grant -> Grant | amount decreases, delta recorded |
| revoke | Grant -> () | -1 active |
| merge | (Grant, Grant) -> Grant | count -1, amount conserved |

Invariant tested: for any sequence of these operations, the sum of
active grant amounts equals total issued minus total revoked/attenuated
delta, exactly, at every step.

## 4. Evidence and exit criteria

1. Property-based test (proptest or fast-check) driving 10,000 random
   operator sequences with conservation asserted at every step; zero
   failures across a 24-hour fuzz window in CI.
2. Escape audit: `grep` for direct state mutation in the module returns
   only the six operator implementations; no `set_`, no public mutable
   fields.
3. One real feature (a permission check in accessctl) shipped on the
   operator surface, reviewed by a second reader.
4. Write-up appended to this ADR: what the operator-only surface cost
   in ergonomics, and which parts of X5's mechanism line needed
   adjustment.

Exit: criteria 1-3 green moves X5 from Pilot to adopted-in-canon for
conserved-quantity domains (references/catalog.md stance update,
CHANGELOG entry). Criterion 4 feeds `references/frontier.md` X5 Analysis.

## 4a. Evidence log

- 2026-11-16: operator surface implemented as `accessctl` 0.2.0
  `src/grants.rs` (f1d2a7e): six operators, private ledger fields, zero
  setters, `GrantError` for every rejected parameter, state unchanged
  after any `Err` (unit-tested).
- Criterion 2 (escape audit) PASS: 0 `pub fn set_*`/`pub fn with_*`;
  `GrantLedger` fields all private; mutating methods are exactly the six
  operators (read helpers `amount_of`/`is_active`/`outstanding`/
  `active_amount_for`/`authorize` are private or pure reads). Cargo
  clippy clean.
- Criterion 1 (property test) PASS at CI scale: 512 proptest seeds x
  250-operation sequences + a 10,000-step deterministic xorshift soak
  (`long_walk_single_seed`), conservation asserted after every step;
  17/17 tests green, replayable from seed. The 24-hour fuzz window is
  deferred to a nightly CI soak (not yet wired: pending M1-style
  workflow addition to accessctl).
- Criterion 1 addendum: nightly soak WIRED (accessctl
  `.github/workflows/nightly-soak.yml`, cron 03:30 UTC, PROPTEST_CASES=4096);
  each run is one window of the cumulative evidence.
- Criterion 3 (shipped feature) PARTIAL: `authorize(subject, required)`
  + `active_amount_for` shipped on the operator surface; consumer
  adoption and second-reader review pending.

## 5. Rejected alternatives

- CRUD setters plus validators: the exact failure mode X5 removes;
  validators cannot catch what an illegal mutation spanned.
- CRDT semilattice: proven and related, but solves replica convergence,
  not authority conservation; wrong tool for single-node accessctl.
- Waiting for framework support: X5 is discipline-only (no new
  tooling), so waiting buys nothing.
