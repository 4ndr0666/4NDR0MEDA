#!/usr/bin/env python3
"""4NDR0MEDA manifest tool — build / verify the tree hash manifest (A.N.D.R.O.).

The manifest excludes itself (a file cannot pin itself) and excludes
runtime/ephemera. Build re-stamps after ANY edit: the bootstrap is
self-stamping, and so is the tree it ships in.

Usage:
  python3 tools/manifest.py build
  python3 tools/manifest.py verify [--report-only]
Exit: 0 clean; 1 any MISSING/CHANGED/EXTRA (fail-closed unless --report-only).
"""
import argparse, hashlib, sys
from pathlib import Path

MANIFEST = "MANIFEST.sha256"
EXCLUDE_DIRS = {".git", "__pycache__", "memory", "dist", ".tmp-drill"}
EXCLUDE_FILES = {MANIFEST, ".bootstrap-journal", ".liveness"}
EXCLUDE_SUFFIX = {".pyc"}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def walk(root: Path):
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root)
        if p.is_dir():
            continue
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if rel.name in EXCLUDE_FILES or rel.suffix in EXCLUDE_SUFFIX:
            continue
        yield rel


def build(root: Path) -> int:
    lines = []
    for rel in walk(root):
        lines.append(f"{digest(root / rel)}  {rel.as_posix()}")
    (root / MANIFEST).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"MANIFEST BUILD: {len(lines)} entries -> {MANIFEST}")
    return 0


def verify(root: Path, report_only: bool) -> int:
    mf = root / MANIFEST
    if not mf.exists():
        print("MANIFEST VERIFY: FAIL — manifest absent (run: python3 tools/manifest.py build)")
        return 1
    recorded = {}
    for line in mf.read_text(encoding="utf-8").splitlines():
        if line.strip():
            dg, _, rel = line.partition("  ")
            recorded[rel] = dg
    bad = 0
    for rel, dg in sorted(recorded.items()):
        p = root / rel
        if not p.exists():
            print(f"MISSING  {rel}")
            bad += 1
        elif digest(p) != dg:
            print(f"CHANGED  {rel}")
            bad += 1
    on_disk = {rel.as_posix() for rel in walk(root)}
    for rel in sorted(on_disk - set(recorded)):
        print(f"EXTRA    {rel}  (unpinned — rebuild manifest)")
        bad += 1
    ok = len(recorded) - sum(1 for r in recorded if not (root / r).exists() or digest(root / r) != recorded[r])
    print(f"MANIFEST VERIFY: {'FAIL' if bad else 'OK'} — {ok}/{len(recorded)} pinned files match"
          + (f", {bad} defect(s)" if bad else ""))
    if bad and not report_only:
        return 1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "verify"])
    ap.add_argument("--report-only", action="store_true")
    args = ap.parse_args()
    root = Path(__file__).resolve().parent.parent
    if args.cmd == "build":
        return build(root)
    return verify(root, args.report_only)


if __name__ == "__main__":
    sys.exit(main())
