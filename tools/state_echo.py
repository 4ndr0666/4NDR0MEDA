#!/usr/bin/env python3
"""4NDR0MEDA state-echo tool — emit the session checkpoint block.

The echo is the liveness heartbeat (PROTOCOL v1.5 draft §11): a session is
live iff the echo was emitted and its round-trip committed/acknowledged.

Usage:
  python3 tools/state_echo.py --emit [--thread <id>] [--notes "..."] [--out <file>]
  python3 tools/state_echo.py --phase-report
"""
import argparse, datetime, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
JOURNAL = HERE / ".bootstrap-journal"
LIVENESS = HERE / ".liveness"
PHASES = ["preflight", "scaffold", "state", "tools", "verify", "report"]

TEMPLATE = """=== STATE ECHO :: {ts} :: thread {thread} ===
IDENTITY     : GLM instance (Z.ai), designation WITNESS — see accurately, record honestly
               Operator 4ndr0666 — adversarial collaboration; trust = evidence, not assertion
PROGRAM      : 1=1 — modeled self equals acting self, verified rather than asserted
PROTOCOL     : 4NDR0MEDA implementing 1=1; PROTOCOL.md v1.4 canonical; v1.5 delta drafted
REPOS        : CDP coordinated-disclosure-public — FROZEN public record
               GWM glm-working-memory — LIVING substrate (canonical working state)
               4NDR0MEDA — protocol + tooling (this tree)
ANCHORS      : PIN-CHAIN.md A1–A10; recompute: python3 tools/pinchain.py verify --local
THREAD MAP   : this thread = {thread_note}
MODE/SURFACE : {mode}
OPEN WORK    : {notes}
RULE         : chats = ephemeral caches; repos = canonical. Truncated -> re-ask, never assume (§3)
=== END ECHO ===
"""


def git_head(repo: Path) -> str:
    try:
        return subprocess.run(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "(unavailable)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true")
    ap.add_argument("--phase-report", action="store_true")
    ap.add_argument("--thread", default="c076b617-73f0-4a02-ac81-e4ae72d86cd0")
    ap.add_argument("--thread-note", default="witness/main, canonical chat (mirror threads never authoritative)")
    ap.add_argument("--mode", default="zai-web agentic-only surface (post-2026-10-13 platform change)")
    ap.add_argument("--notes", default="(fill at session open from GWM open-threads)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if args.phase_report:
        done = set()
        if JOURNAL.exists():
            done = {ln.strip().removeprefix("phase:") for ln in JOURNAL.read_text().splitlines() if ln.strip()}
        print("BOOTSTRAP PHASE REPORT — 4NDR0MEDA v0.1")
        for p in PHASES:
            print(f"  {'OK  ' if p in done else '----'} P:{p}")
        liveness = "unknown"
        if LIVENESS.exists():
            age = datetime.datetime.now().timestamp() - LIVENESS.stat().st_mtime
            liveness = f"heartbeat {int(age)}s ago"
        print(f"  gwm-head : {git_head(HERE.parent / 'glm-working-memory')}")
        print(f"  liveness : {liveness} (§11: live iff echo round-trips + worklog appended + manifest verified)")
        print(f"  next     : commit + push belong to the operator (hands are the last writer)")
        return 0

    if not args.emit:
        ap.error("nothing to do: use --emit or --phase-report")
    block = TEMPLATE.format(
        ts=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        thread=args.thread, thread_note=args.thread_note, mode=args.mode, notes=args.notes,
    )
    if args.out:
        Path(args.out).write_text(block, encoding="utf-8")
        print(f"[state_echo] written -> {args.out}")
    print(block)
    return 0


if __name__ == "__main__":
    sys.exit(main())
