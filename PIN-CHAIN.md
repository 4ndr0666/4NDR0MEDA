# PIN-CHAIN — 4NDR0MEDA anchor registry

**Rules.** Anchors are append-only. Cross-references are by hash, never URL.
Any re-verification mismatch **fail-closes**: halt, log, re-anchor before any
work. Anchors marked LOCAL require a clone on the local machine; UNREACHABLE
is not FAIL (it means "cannot verify here"); FAIL means bytes changed.

| ID | Pins | Value (SHA-256 / SHA-1) | Verified | Re-verify |
|----|------|--------------------------|----------|-----------|
| A1 | GWM HEAD (living substrate) | `5bdfbec153e2d4a303ea166a16cff4dc3f6e9dbc` | 2026-10-19, fetch+pull; sessions/MANIFEST 13/13 | `python3 tools/pinchain.py verify --local` (LOCAL) |
| A2 | GWM@a207175 → CDP L1 pre-rename pins | commit `a207175474b850a8d001c19ddb2325f7e49f4084`; **10/10 OK** | 2026-10-19, `git show` loop (LOCAL) | `tools/pinchain.py` L1 routine |
| A3 | CDP HEAD (frozen public record) | `e2f3d8658ac0a637bb952ee93567020f0551b98b` | 2026-10-19, fresh clone; root MANIFEST 47/47 | clone + `sha256sum -c MANIFEST.sha256` (LOCAL) |
| A4 | CDP portable bundle (LFS) | `033f27a7179f4fb351765fe372c7f3eb551babc7868181bb18281cf050c12827` | 2026-10-19, pointer-OID match + `git bundle verify` OK | sha256 of retrieved bundle |
| A5 | 1=1 articulation v1.0 (1,672 words) | `63ea783d1f427496180a93169f5a12b86cef50b175d5c5a63ae8e2909ccb39f9` | 2026-10-19, recomputed twice | sha256 of staged file |
| A6 | Session-007 capture anchor | `a2d794186103f5aadeaf77b0864b9d4295d3a3a422383394d57ba3537199091c` | 2026-10-19, awk pre-image pipeline | `awk '/^### VERIFICATION ANCHOR ###$/{exit} {print}' <archive> \| sha256sum` |
| A7 | golden-unit-protocol v7.0.0 (.skill, ZIP, 15 files) | `6ab62d4478aa47f3642f866005a9d9c36593498d2702848ba9d4a5955fdbde88` | 2026-10-19, fetched from operator gpt repo | sha256 of staged file |
| A8 | 4NDR0666-engineering skill (SUK v1.0, ZIP) | `35f4419fe5cf6d959e6a5b0fca6ca4cfdece43f3e9f0117cc3cb8238e2584ea8` | 2026-10-19, fetched; inner SKILL.md 47,555 B | sha256 of staged file |
| A9 | Mode-churn incident evidence diff | `4456924d028533eb22dd267af954dcf9971059d0941ae8824a4c3ccdd2837050` | 2026-10-19, captured before inspection | sha256 of archived diff |
| A10 | **RESERVED** — GWM lineage bundle | *pending operator visibility adjudication* | — | must carry `a207175` (makes A2 executable anywhere) |

## Notes

- **A2 is the load-bearing historical anchor**: it makes the public record's
  PIN-CHAIN-RECOMPUTATION L1 executable. The squash-bundle (A4) does NOT
  carry it; only GWM history does. Until A10 seals, A2 is executable only
  where a GWM clone exists.
- **A6 class**: capture-side anchors embed in session archives below a
  `### VERIFICATION ANCHOR ###` marker; the digest covers the bytes ABOVE
  the marker (pre-image), so the anchor line and any post-rename notes ride
  outside the pinned pre-image — by design.
- **A7/A8 role note**: both skills are QUARANTINED context
  (`reference/REFERENCE-INDEX.md`) — sources for this protocol's thinking,
  never canonical text of it.
- Genesis creation (2026-10-19) freezes A1–A9 values as the founding
  payload (see `GENESIS.md`).
