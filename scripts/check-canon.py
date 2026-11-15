#!/usr/bin/env python3
"""check-canon: mechanical conformance gate for the pattern-standards canon.

Checks (AGENTS.md rules 5 and 8, mechanized):
  1. ID resolution      every referenced T/P/X/N ID resolves to a catalog
                        table row or reference heading. P0 (priority tier)
                        is whitelisted with a warning, not a violation.
  2. Catalog mirror     references/catalog.md table IDs == reference
                        heading IDs, exactly, per series.
  3. Node set equality  CORE §6 node rows == decision-graph index rows ==
                        decision-graph node headings.
  4. Count claims       "NNN patterns/constructs" in PATTERN-CORE.md,
                        README.md, llms.txt equal the actual heading totals.
  5. Baseline claim     the "-pattern baseline tier" claim equals the §3
                        table row count.
  6. Series ranges      the T1–Tmax / P1–Pmax / X1–Xmax range claims equal
                        the actual maximum IDs per series.

Usage: scripts/check-canon.py            exit 1 on violations
Diagnostics print file:line. Warnings never affect the exit code.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD_FILES = ["PATTERN-CORE.md", "README.md", "AGENTS.md", "PROVENANCE.md",
            "STANDARDS-INDEX.md", "CHANGELOG.md"]
GLOB_DIRS = ["references", "adr"]
WHITELIST = {"P0"}


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def scan_targets() -> list[Path]:
    files = [ROOT / f for f in MD_FILES if (ROOT / f).is_file()]
    files.append(ROOT / "llms.txt")
    for d in GLOB_DIRS:
        dp = ROOT / d
        if dp.is_dir():
            files += sorted(dp.rglob("*.md"))
    return [f for f in files if f.is_file()]


def headings() -> tuple[dict[str, list[str]], dict[str, str]]:
    """series -> IDs from ### headings; and ID -> defining file."""
    reg: dict[str, list[str]] = {"T": [], "P": [], "X": [], "N": []}
    where: dict[str, str] = {}
    for f in (ROOT / "references").glob("*.md"):
        for m in re.finditer(r"^### ([TPXN]\d+)", read(f), re.M):
            sid = m.group(1)
            s = sid[0]
            reg[s].append(sid)
            where[sid] = str(f.relative_to(ROOT))
    return reg, where


def catalog_ids() -> dict[str, set[str]]:
    cat = read(ROOT / "references" / "catalog.md")
    out: dict[str, set[str]] = {"T": set(), "P": set(), "X": set()}
    for m in re.finditer(r"^\| ([TPX]\d+) \|", cat, re.M):
        out[m.group(1)[0]].add(m.group(1))
    return out


def node_rows(core: str, graph: str) -> tuple[set[str], set[str], set[str]]:
    core_rows = set(re.findall(r"^\| (N\d+) \|", core, re.M))
    graph_rows = set(re.findall(r"^\| (N\d+) \|", graph, re.M))
    graph_heads = set(re.findall(r"^### (N\d+)", graph, re.M))
    return core_rows, graph_rows, graph_heads


def baseline_rows(core: str) -> int:
    m = re.search(r"## 3\. Baseline tier\n(.*?)\n## 4\.", core, re.S)
    if not m:
        return -1
    return len(re.findall(r"^\| [TP]\d+ \|", m.group(1), re.M))


def main() -> int:
    violations: list[str] = []
    warnings: list[str] = []
    reg, _where = headings()
    targets = scan_targets()
    texts = {f: read(f) for f in targets}

    # 1. ID resolution
    ids = re.compile(r"\b([TPX]\d{1,2}|N\d{2})\b")
    known = {s for ids_ in reg.values() for s in ids_}
    for f, t in texts.items():
        for m in ids.finditer(t):
            sid = m.group(1)
            if sid in WHITELIST:
                warnings.append(f"{f.relative_to(ROOT)}:{t[:m.start()].count(chr(10)) + 1}: "
                                f"whitelisted ID {sid} (priority tier)")
            elif sid not in known:
                violations.append(f"{f.relative_to(ROOT)}:{t[:m.start()].count(chr(10)) + 1}: "
                                  f"unresolved ID {sid}")

    # 2. Catalog mirror
    cat = catalog_ids()
    for s in "TPX":
        head = set(reg[s])
        tab = cat[s]
        if head != tab:
            missing = sorted(head - tab, key=lambda x: int(x[1:]))
            extra = sorted(tab - head, key=lambda x: int(x[1:]))
            violations.append(f"catalog.md: {s}-series mirror broken; "
                              f"missing rows: {missing or 'none'}; extra rows: {extra or 'none'}")

    # 3. Node set equality + graph block format
    core = texts[ROOT / "PATTERN-CORE.md"]
    graph = texts[ROOT / "references" / "decision-graph.md"]
    c_rows, g_rows, g_heads = node_rows(core, graph)
    if not (c_rows == g_rows == g_heads):
        violations.append(f"node sets diverge: CORE §6 {len(c_rows)}, "
                          f"graph index {len(g_rows)}, graph headings {len(g_heads)}")
    blocks = re.split(r"^### (N\d+) · ", graph, flags=re.M)
    for i in range(1, len(blocks), 2):
        nid, body = blocks[i], blocks[i + 1]
        body = body.split("## ")[0]
        for key in ("K:", "M:", "A:", "R:"):
            if not re.search(rf"^{key} ", body, re.M):
                violations.append(f"decision-graph.md: node {nid} missing {key} line")

    # 3b. Node-count claims ("NN-node", "NN nodes") in living claim files only
    #     (CHANGELOG entries are historical; reference prose may discuss
    #     cluster sizes that are not decision-graph claims)
    for fname in ("PATTERN-CORE.md", "README.md", "llms.txt"):
        t = texts[ROOT / fname]
        rel = fname
        for m in re.finditer(r"(\d+)-node|\b(\d+) nodes\b", t):
            n = int(m.group(1) or m.group(2))
            if n != len(g_heads):
                line = t[:m.start()].count(chr(10)) + 1
                violations.append(f"{rel}:{line}: node-count claim {n} != {len(g_heads)}")

    # 4. Count claims
    total = sum(len(reg[s]) for s in "TPX")
    r_total = len(re.findall(r"^\| R\d+ \|", core, re.M))
    for fname, pat in [("PATTERN-CORE.md", r"(\d+) patterns in three series"),
                       ("README.md", r"(\d+) constructs"),
                       ("llms.txt", r"(\d+) constructs")]:
        m = re.search(pat, texts[ROOT / fname])
        if not m:
            violations.append(f"{fname}: no count claim matching {pat!r}")
        elif int(m.group(1)) != total:
            violations.append(f"{fname}: claims {m.group(1)} patterns, actual {total}")
    for fname in ("PATTERN-CORE.md", "README.md", "llms.txt"):
        for m in re.finditer(r"(\d+) named refusals|(\d+) refusals\b", texts[ROOT / fname]):
            n = int(m.group(1) or m.group(2))
            if n != r_total:
                line = texts[ROOT / fname][:m.start()].count(chr(10)) + 1
                violations.append(f"{fname}:{line}: refusal-count claim {n} != {r_total}")

    # 5. Baseline claim
    bm = re.search(r"a (\d+)-pattern baseline tier", core)
    rows = baseline_rows(core)
    if bm and rows >= 0 and int(bm.group(1)) != rows:
        violations.append(f"PATTERN-CORE.md: baseline claim {bm.group(1)} != table rows {rows}")

    # 6. Series ranges
    for s in "TPX":
        mx = max(int(x[1:]) for x in reg[s]) if reg[s] else 0
        for fname in ("PATTERN-CORE.md", "README.md", "llms.txt"):
            m = re.search(rf"{s}1–{s}(\d+)", texts[ROOT / fname])
            if m and int(m.group(1)) != mx:
                violations.append(f"{fname}: range {s}1–{s}{m.group(1)} but max is {s}{mx}")

    for w in warnings:
        print(f"W {w}")
    for v in violations:
        print(f"V {v}")
    print(f"check-canon: {'FAIL' if violations else 'PASS'} "
          f"({total} patterns, {len(g_heads)} nodes, "
          f"{len(violations)} violation(s), {len(warnings)} warning(s))")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
