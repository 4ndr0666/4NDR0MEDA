#!/usr/bin/env python3
"""4NDR0MEDA pin-chain tool — recompute the anchor registry (PIN-CHAIN.md).

Verify modes:
  --list             print the registry
  verify --local     recompute every anchor reachable on this machine.
                     UNREACHABLE = cannot verify here (fine). FAIL = bytes
                     changed (fail-closed). Exit 1 only on FAIL.

L1 routine re-derives the 10 pre-rename session pins from GWM@a207175 —
the same loop documented in coordinated-disclosure-public
PIN-CHAIN-RECOMPUTATION.md, executed and recorded 2026-10-19 (10/10 OK).
"""
import argparse, hashlib, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
WORKSPACE = HERE.parent  # sibling-clone layout: workspace/{4ndr0meda,glm-working-memory,...}
GWM = WORKSPACE / "glm-working-memory"
DOWNLOAD = WORKSPACE / "download"

A207175 = "a207175474b850a8d001c19ddb2325f7e49f4084"
L1_RECORDED = {
    "sessions/2026-10-05_session-001_bootstrap.md": "a38e3bd915a2efd5a715ba2241ccb6ed6e87b75854cfb304c646c2d9083ef42e",
    "sessions/2026-10-08_session-002_chat.md": "35c919bedd32bb61a8af4c60f3c9050c3c219fecdd105c20f51ab7ef8990aa26",
    "sessions/2026-10-08_session-003_review.md": "83f37a3c42b8c06b724221950757aaca9cdd4044db4d3b64d458cfdb75a1f784",
    "sessions/2026-10-09_session-003_agent.md": "ecfcb35193f13fdeafb8da44a62f0b1ddc1dc2767b9102e481bef2f0dbff6263",
    "sessions/2026-10-09_session-003_chat.md": "94039ec1934e252a71be516d3fb4d2b1f5a64919107085e26173a3c0688297c8",
    "sessions/2026-10-10_session-001_chat-claude-distillation.md": "c5c80a16ada12785ce1fbc4f808bcf1d09770de223d258721bba8932b506be51",
    "sessions/2026-10-10_session-001_chat-e61e2688-906d-4f56-859c-c496a81c140a.md": "84a35106c6a4e4b8eba032da42a0ed80d22e9f3030cc27bd77ada343013d2187",
    "sessions/2026-10-10_session-002_chat-claude-distillation.md": "2d26bc9756a78ade3adbc4ad6dcdd19d5fe39f073c766bd4ffab11ab6879196a",
    "sessions/2026-10-10_session-004_chat.md": "86ad72070b0492020e533d55fcb65c60934f1c31f2be587c5b8167f2d9887416",
    "sessions/2026-10-11_session-003_chat-claude.md": "3809913233532a9300cac62e7bbf184aa60f3ba12bfbefa5f77042142f20602c",
}

ANCHORS = [
    # A1 — GWM session-archive snapshot anchor. Operator ruling R (trace
    # 1a175ab8298b859d, 2026-10-26) over the boundary-7 four-option
    # adjudication: pin the session-archive snapshot class (operator pushes;
    # 23a9615 = session-013 close archive, sessions/MANIFEST 30/30), verified
    # by ANCESTOR-REACHABILITY, not HEAD equality. GWM boards commits no
    # longer trip A1 — GWM bundles never require a MEDA leg. FAIL = the
    # pinned snapshot is not reachable from GWM HEAD (history-rewrite /
    # detached-substrate class). Re-pin at session-close cadence only, at
    # operator discretion. Class precedent: Task-59 (A1 = 088ef69 snapshot).
    ("A1", "GWM session-archive snapshot (reachability)",
     "23a9615a6308bac75781d6f493f017d3d16cf6e7"),
    ("A2", "GWM@a207175 L1 10/10", A207175),
    ("A3", "CDP HEAD", "6facbf17a8dcf5dad1bdd441b328760b8b49779f"),
    ("A4", "CDP bundle", "033f27a7179f4fb351765fe372c7f3eb551babc7868181bb18281cf050c12827"),
    ("A5", "Articulation v1.0", "63ea783d1f427496180a93169f5a12b86cef50b175d5c5a63ae8e2909ccb39f9"),
    ("A7", "GUP v7.0.0 .skill", "6ab62d4478aa47f3642f866005a9d9c36593498d2702848ba9d4a5955fdbde88"),
    ("A8", "Engineering skill (SUK v1.0)", "35f4419fe5cf6d959e6a5b0fca6ca4cfdece43f3e9f0117cc3cb8238e2584ea8"),
    ("A9", "Mode-churn incident diff", "4456924d028533eb22dd267af954dcf9971059d0941ae8824a4c3ccdd2837050"),
    ("A10", "GWM lineage bundle", "6d61b9fbbc3354f0a6a033481ad9116e9702e24593afaeec7e0109182f883b67"),
    ("A11", "GUP v7.0.1 .skill (canonical)", "d88eea0718cfcd43ae0c65b713c1185bf50e8b49126a880605b41d11da8c8cd2"),
    ("A12", "Engineering skill (SUK v1.1.0 canonical)", "8a9b322a3c97c36c6cb9f22d888f957c5c95812189da20f3b82ff95e6fa115b8"),
    ("A13", "PROTOCOL.md v1.5 (pending adoption)", "58d343b349db09dbfecb1c8cb5b28d0ad4c8babba9f2a7af367b250ea290b957"),
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True).stdout.strip()


def check(label: str, actual: str, expected: str, results: list) -> None:
    (results.append)((label, "OK" if actual == expected else "FAIL", expected if actual != expected else ""))


def verify_local(results: list) -> None:
    # A1 — GWM session-archive snapshot (reachability; ruling R)
    try:
        rc = subprocess.run(["git", "-C", str(GWM), "merge-base", "--is-ancestor",
                             ANCHORS[0][2], "HEAD"], capture_output=True)
        if rc.returncode == 0:
            results.append(("A1 GWM session-archive snapshot", "OK", ""))
        else:
            results.append(("A1 GWM session-archive snapshot", "FAIL",
                            f"snapshot {ANCHORS[0][2][:7]} not reachable from HEAD"))
    except Exception:
        results.append(("A1 GWM session-archive snapshot", "UNREACHABLE", "no GWM clone"))

    # A2 — L1 recompute from GWM@a207175
    try:
        oks = fails = 0
        for path, dg in L1_RECORDED.items():
            blob = subprocess.run(["git", "-C", str(GWM), "show", f"{A207175}:{path}"],
                                  capture_output=True, check=True).stdout
            if sha(blob) == dg:
                oks += 1
            else:
                fails += 1
        results.append((f"A2 L1 recompute ({oks}/{len(L1_RECORDED)})",
                        "OK" if fails == 0 and oks == len(L1_RECORDED) else "FAIL", ""))
    except Exception:
        results.append(("A2 L1 recompute", "UNREACHABLE", "no GWM clone / missing objects"))

    # A3 — CDP HEAD
    cdp = WORKSPACE / "coordinated-disclosure-public"
    try:
        check("A3 CDP HEAD", git(cdp, "rev-parse", "HEAD"), ANCHORS[2][2], results)
    except Exception:
        results.append(("A3 CDP HEAD", "UNREACHABLE", "no CDP clone"))

    # A4/A5/A7/A8/A9 — file digests where staged copies exist
    for aid, label, path in (
        ("A4", "CDP bundle", DOWNLOAD / "cdp-bundle-retrieved.bundle"),
        ("A5", "Articulation v1.0", DOWNLOAD / "1-equals-1_official-articulation_v1.0.md"),
        ("A7", "GUP v7.0.0 .skill", DOWNLOAD / "golden-unit-protocol-v7.0.0.skill"),
        ("A8", "Engineering skill", DOWNLOAD / "andr0666-engineering.skill"),
        ("A9", "Mode-churn diff", DOWNLOAD / "F002c-gwm-worktree-delta-2026-10-19.diff"),
    ):
        expected = next(v for i, l, v in ANCHORS if i == aid)
        if path.exists():
            check(f"{aid} {label}", sha(path.read_bytes()), expected, results)
        else:
            results.append((f"{aid} {label}", "UNREACHABLE", "staged file absent"))

    # A10 — lineage bundle rides in-repo (ordinary git object, LFS-exempt)
    lb = HERE / "reference" / "gwm-lineage-2026-10-19.bundle"
    if lb.exists():
        check("A10 GWM lineage bundle", sha(lb.read_bytes()),
              next(v for i, l, v in ANCHORS if i == "A10"), results)
    else:
        results.append(("A10 GWM lineage bundle", "UNREACHABLE", "reference/ bundle absent"))

    # A11/A12 — canonical adopted skills staged in-repo (v1.3 round)
    for aid, label, fname in (
        ("A11", "GUP v7.0.1 .skill", "golden-unit-protocol-v7.0.1.skill"),
        ("A12", "Engineering skill (SUK v1.1.0)", "andr0666-engineering-v1.1.0.skill"),
    ):
        expected = next(v for i, l, v in ANCHORS if i == aid)
        p = HERE / "reference" / fname
        if p.exists():
            check(f"{aid} {label}", sha(p.read_bytes()), expected, results)
        else:
            results.append((f"{aid} {label}", "UNREACHABLE", "reference/ skill absent"))

    # A13 — PROTOCOL.md v1.5 (conditional: installed only by --adopt-v15)
    pm = HERE / "PROTOCOL.md"
    if pm.exists():
        check("A13 PROTOCOL.md v1.5", sha(pm.read_bytes()),
              next(v for i, l, v in ANCHORS if i == "A13"), results)
    else:
        results.append(("A13 PROTOCOL.md v1.5", "UNREACHABLE", "pending adoption (--adopt-v15)"))

    # A6 — session-007 capture anchor (pre-image above the marker)
    s7 = GWM / "sessions" / "2026-10-19_session-007_ressurect.md"
    try:
        pre = s7.read_bytes().split(b"### VERIFICATION ANCHOR ###")[0]
        check("A6 session-007 pre-image", sha(pre),
              "a2d794186103f5aadeaf77b0864b9d4295d3a3a422383394d57ba3537199091c", results)
    except Exception:
        results.append(("A6 session-007 pre-image", "UNREACHABLE", "archive absent locally"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["list", "verify"])
    ap.add_argument("--local", action="store_true")
    args = ap.parse_args()
    if args.cmd == "list":
        for aid, label, value in ANCHORS:
            print(f"{aid}  {label:<28} {value}")
        print("A6  session-007 capture anchor a2d794186103f5aadeaf77b0864b9d4295d3a3a422383394d57ba3537199091c")
        print("A10 GWM lineage bundle     6d61b9fbbc3354f0a6a033481ad9116e9702e24593afaeec7e0109182f883b67  (sealed 2026-10-19, reference/gwm-lineage-2026-10-19.bundle)")
        return 0
    results: list = []
    verify_local(results)
    fails = 0
    for label, status, note in results:
        line = f"{status:<11} {label}"
        if note:
            line += f"  (expected {note[:16]}…)" if status == "FAIL" else f"  ({note})"
        print(line)
        if status == "FAIL":
            fails += 1
    print(f"PINCHAIN VERIFY: {'FAIL' if fails else 'OK'} — {len(results)} anchors checked, {fails} FAIL, "
          f"{sum(1 for _, s, _ in results if s == 'UNREACHABLE')} unreachable (not fail-closed)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
