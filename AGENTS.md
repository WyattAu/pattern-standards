# AGENTS.md

The canon is PATTERN-CORE.md; references/ expand it; nothing else is
normative. Rules for agents editing this repo:

1. Every pattern addition gets an ID in its series, a Failure line
   naming the concrete failure mode, and a maturity stamp.
2. Refusals are named explicitly — a standard that only lists virtues
   is not a standard. New refusals need an `adr/` entry.
3. No filler: tables for enumerable facts, prose only for causal
   chains (DOC-STYLE). One pattern, one block: Failure, Mechanism,
   Analysis, Links.
4. Maturity stamps are judgments, not vibes: cite the primary source
   (paper, vendor doc, production system) in the same line when a
   claim is load-bearing.
5. Cross-references use series IDs (`T27`, `P11`, `X6`) and must
   resolve; grep the ID before inventing a new one.
6. Date-stamped changes in CHANGELOG.md; series-level changes, new
   baseline-tier entries, or new refusals need an `adr/` entry.
7. llms.txt regenerates whenever PATTERN-CORE structure changes.
