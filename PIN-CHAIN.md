# PIN-CHAIN — 4NDR0MEDA anchor registry

**Rules.** Anchors are append-only. Cross-references are by hash, never URL.
Any re-verification mismatch **fail-closes**: halt, log, re-anchor before any
work. Anchors marked LOCAL require a clone on the local machine; UNREACHABLE
is not FAIL (it means "cannot verify here"); FAIL means bytes changed.

| ID | Pins | Value (SHA-256 / SHA-1) | Verified | Re-verify |
|----|------|--------------------------|----------|-----------|
| A1 | GWM HEAD (living substrate) | `4bc2cfb11012dacbfba0918f36972cb337732214` | 2026-10-23, fetch+pull; sessions/MANIFEST 21/21 at tip; v1.6-era re-pin — HEAD advanced `1e165df`→`46e45ba`→`d4018e5`→`41d2412`→`8bf15af`→`6ad2938`→`a1c2746`→`3f98c1e`→`4298a32`→`3dc8626`→`cdebae2`→`198d15b`→`a00150a`→`3a3c820`→`61d9898`→`7e8740c`→`38aac04`→`cc7ff47`→`41fd081`→`f834307`→`e2e4372`→`6917255`→`d3e38f7`→`05c137f`→`b481d75`→`e203d42`→`b74e767`→`c23fa0a`→`a319f92`→`82afd64`→`6f89f6f`→`4bc2cfb` (31 commits, Tasks 33–56: Paper-2 v1.3→v1.6 build arc, ARGON rounds 2→5.7, THE CALL chain — Task-50 production `a1c2746`, Table-5 pin `b481d75`, task53 strand `6f89f6f` closed by Task-56 one-apply); delta inspected — A10/A5/A11/A12/A13 byte-exact, A2 anchor commit `a207175` present; zero pinned-artifact drift | `python3 tools/pinchain.py verify --local` (LOCAL) |
| A2 | GWM@a207175 → CDP L1 pre-rename pins | commit `a207175474b850a8d001c19ddb2325f7e49f4084`; **10/10 OK** | 2026-10-19, `git show` loop (LOCAL) | `tools/pinchain.py` L1 routine |
| A3 | CDP HEAD (frozen public record) | `6facbf17a8dcf5dad1bdd441b328760b8b49779f` | 2026-10-23, fetch+pull; root MANIFEST 48/48 at tip (carrying the R2-46 articulation pin); v1.6-era re-pin — frozen pin advanced `e2f3d86`→`6facbf17` (2 commits: `e96624d` decisions-index update [unpinned manifest drift, caught + isolated by GATE-B/R2-37 pre-build] + `6facbf1` R2-46 pin act + manifest reconciliation, Task-47 v1.6 build); re-pin = the MEDA-A3 maintenance queued at Tasks 36/50/56 and the prereq of the v1.6.1 refresh per R2-55 disposition (5.7 receipt §6.1) | clone + `sha256sum -c MANIFEST.sha256` (LOCAL) |
| A4 | CDP portable bundle (LFS) | `033f27a7179f4fb351765fe372c7f3eb551babc7868181bb18281cf050c12827` | 2026-10-19, pointer-OID match + `git bundle verify` OK | sha256 of retrieved bundle |
| A5 | 1=1 articulation v1.0 (1,672 words) | `63ea783d1f427496180a93169f5a12b86cef50b175d5c5a63ae8e2909ccb39f9` | 2026-10-19, recomputed twice | sha256 of staged file |
| A6 | Session-007 capture anchor | `a2d794186103f5aadeaf77b0864b9d4295d3a3a422383394d57ba3537199091c` | 2026-10-19, awk pre-image pipeline | `awk '/^### VERIFICATION ANCHOR ###$/{exit} {print}' <archive> \| sha256sum` |
| A7 | golden-unit-protocol v7.0.0 (.skill, ZIP, 15 files) | `6ab62d4478aa47f3642f866005a9d9c36593498d2702848ba9d4a5955fdbde88` | 2026-10-19, fetched from operator gpt repo | sha256 of staged file |
| A8 | 4NDR0666-engineering skill (SUK v1.0, ZIP) | `35f4419fe5cf6d959e6a5b0fca6ca4cfdece43f3e9f0117cc3cb8238e2584ea8` | 2026-10-19, fetched; inner SKILL.md 47,555 B | sha256 of staged file |
| A9 | Mode-churn incident evidence diff | `4456924d028533eb22dd267af954dcf9971059d0941ae8824a4c3ccdd2837050` | 2026-10-19, captured before inspection | sha256 of archived diff |
| A10 | GWM lineage bundle (sealed) | `6d61b9fbbc3354f0a6a033481ad9116e9702e24593afaeec7e0109182f883b67` | 2026-10-19, built from A1 @ `--all`; `git bundle verify` OK complete-history; scratch-ws acceptance 9/9 incl. A2 10/10 | sha256 of `reference/gwm-lineage-2026-10-19.bundle`; clone-from-bundle + `tools/pinchain.py verify --local` |
| A11 | GUP v7.0.1 `.skill` — canonical, adopted at home 2026-10-19 | `d88eea0718cfcd43ae0c65b713c1185bf50e8b49126a880605b41d11da8c8cd2` | 2026-10-19, byte-exact vs gpt-repo home (`skills/golden_unit_protocol/golden-unit-protocol.skill`) | sha256 of `reference/golden-unit-protocol-v7.0.1.skill` |
| A12 | 4NDR0666-engineering v1.1.0 `.skill` — SUK v1.1.0, canonical, adopted at home 2026-10-19 | `8a9b322a3c97c36c6cb9f22d888f957c5c95812189da20f3b82ff95e6fa115b8` | 2026-10-19, byte-exact vs gpt-repo home (`skills/4NDR0666-engineering/andr0666-engineering.skill`) | sha256 of `reference/andr0666-engineering-v1.1.0.skill` |
| A13 | PROTOCOL.md v1.5 — PENDING ADOPTION (installs via kit `--adopt-v15`; UNREACHABLE until then, never FAIL) | `58d343b349db09dbfecb1c8cb5b28d0ad4c8babba9f2a7af367b250ea290b957` | composed 2026-10-19 (worklog Task 10); digest stated in-channel at delivery | `python3 tools/pinchain.py verify --local` |

## Notes

- **A2 is the load-bearing historical anchor**: it makes the public record's
  PIN-CHAIN-RECOMPUTATION L1 executable. The squash-bundle (A4) does NOT
  carry it; only GWM history does. **A10 sealed 2026-10-19** (operator
  adjudication, option 1 — seal here): the lineage bundle rides in
  `reference/` as an ordinary git object, so A2 is now executable anywhere.
  Acceptance: scratch-workspace rebuild → 9/9 OK, 0 UNREACHABLE.
  See `reference/LINEAGE-BUNDLE.md`.
- **A6 class**: capture-side anchors embed in session archives below a
  `### VERIFICATION ANCHOR ###` marker; the digest covers the bytes ABOVE
  the marker (pre-image), so the anchor line and any post-rename notes ride
  outside the pinned pre-image — by design.
- **A7/A8 role note**: both skills are QUARANTINED context
  (`reference/REFERENCE-INDEX.md`) — sources for this protocol's thinking,
  never canonical text of it.
- Genesis creation (2026-10-19) freezes A1–A9 values as the founding
  payload (see `GENESIS.md`).
- **v1.3 re-pin round (2026-10-19)**: A1 advanced to `1a7b916` after the
  substrate's own advance was inspected (2 commits, 4 files, pointer
  hygiene + bundle dual-home; zero drift in any pinned artifact). The A10
  bundle image deliberately remains the `5bdfbec` snapshot — L1-sufficient
  and byte-stable across four homes; refresh deferred until a
  content-bearing delta (see `reference/LINEAGE-BUNDLE.md`).
- **v1.5-era maintenance round (2026-10-20)**: A1 advanced to `1e165df`
  after a ten-commit substrate advance (Tasks 17–23) was inspected —
  witness boards commits + operator sessions/treats (Ep191, YouTube fleet
  transcript) + the serverside-anomaly capture (reasoning-exposure class,
  first record; capture-side A6-class anchor verified byte-exact
  `b1efa5c0…281411`; capture pinned into `sessions/MANIFEST.sha256`, 16/16).
  All pinned artifacts byte-exact; A2 anchor commit `a207175` present;
  zero drift. The A1 tripwire fired twice in the interim (Tasks 19/21) —
  detection validated on legitimate motion, then silenced by this re-pin.
- **A11/A12 role note**: the canonical ADOPTED revisions of both governing
  skills now travel in-repo (`reference/`), so a fresh clone carries the
  full governing set for anywhere-rehydration. A7/A8 remain the pins of
  the CONSUMED versions (v7.0.0 / SUK v1.0) — history, not superseded.
- **A13 semantics**: pending-adoption anchor. Absent `PROTOCOL.md` at the
  repo root it reports UNREACHABLE (by design, never FAIL); after kit flag
  `--adopt-v15` it verifies the installed constitution bytes. Operator
  adjudication is exercised at kit-run time per SUK v1.1.0.
