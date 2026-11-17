# AGENTS.md

The canon is PATTERN-CORE.md; references/ expand it; nothing else is
normative. Rules for agents editing this repo:

1. Every pattern addition gets an ID in its series, a Failure line
   naming the concrete failure mode, and a maturity stamp.
2. Refusals are named explicitly; a standard that only lists virtues
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
8. `voice-lint.py --strict` (standards canon) passes on all Markdown:
   no em-dashes, no PR-6 fillers, no PR-8 hedges.
9. `make ci` (lint + scripts/check-canon.py) passes before every push:
   ID resolution, catalog mirror, node-set equality, and count claims
   are mechanical, not judgment calls.
10. Decision-graph node blocks use the fixed K:/M:/A:/R: line format;
    `scripts/route.py` parses it, so format drift breaks the router.
11. Estate repos declare pattern adoption in `PATTERN_ADOPTION.md`
    (format: references/adoption-format.md), validated by
    `scripts/adoption-check.py`; unknown IDs and path-less claims fail.
