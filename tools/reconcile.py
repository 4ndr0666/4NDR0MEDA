#!/usr/bin/env python3
"""4NDR0MEDA reconcile tool — two-tree divergence triage.

Reports ONLY_IN_A / ONLY_IN_B / DIFFER (with both digests) / SAME.
NEVER mutates anything: human adjudicates merges, never silent ones
(lived incident: two-repo uncertainty, 2026-10-19).

Usage:
  python3 tools/reconcile.py <dirA> <dirB> [--report <out.md>]
"""
import argparse, hashlib, sys
from pathlib import Path

EXCLUDE_DIRS = {".git", "__pycache__", "memory", "dist", "node_modules"}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def tree_map(root: Path) -> dict:
    out = {}
    if not root.is_dir():
        return out
    for p in root.rglob("*"):
        rel = p.relative_to(root)
        if p.is_dir() or any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        out[rel.as_posix()] = digest(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("dir_a")
    ap.add_argument("dir_b")
    ap.add_argument("--report", default=None, help="write markdown report to this path")
    args = ap.parse_args()
    a, b = Path(args.dir_a), Path(args.dir_b)
    if not a.is_dir() or not b.is_dir():
        print(f"[reconcile] unreachable input(s): {a if not a.is_dir() else ''} {b if not b.is_dir() else ''}")
        return 2
    ma, mb = tree_map(a), tree_map(b)
    only_a = sorted(set(ma) - set(mb))
    only_b = sorted(set(mb) - set(ma))
    differ = sorted(k for k in set(ma) & set(mb) if ma[k] != mb[k])
    same = len(set(ma) & set(mb)) - len(differ)

    lines = [
        "# Reconciliation triage",
        "",
        f"- A: `{a}` ({len(ma)} files)",
        f"- B: `{b}` ({len(mb)} files)",
        f"- SAME: {same} · ONLY_IN_A: {len(only_a)} · ONLY_IN_B: {len(only_b)} · DIFFER: {len(differ)}",
        "",
        "## DIFFER (both digests — human adjudicates)",
        "",
        "| path | sha256 A | sha256 B |",
        "|------|----------|----------|",
    ]
    lines += [f"| {k} | `{ma[k][:16]}…` | `{mb[k][:16]}…` |" for k in differ]
    lines += ["", "## ONLY_IN_A", ""] + [f"- {k} (`{ma[k][:16]}…`)" for k in only_a]
    lines += ["", "## ONLY_IN_B", ""] + [f"- {k} (`{mb[k][:16]}…`)" for k in only_b]
    report = "\n".join(lines) + "\n"

    if args.report:
        Path(args.report).write_text(report, encoding="utf-8")
        print(f"[reconcile] report -> {args.report}")
    print(f"[reconcile] SAME={same} ONLY_A={len(only_a)} ONLY_B={len(only_b)} DIFFER={len(differ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
