# Changelog

All notable changes to this repository are documented here. Dates are UTC.
Commits are the canonical record — this file is the human-readable index.
The integrity layer is `MANIFEST.sha256` (self-stamping; see README W8).

## [2026-10-29] — maintenance: pinchain resolvability + layout overrides

Task-73 registered closure (Task-72 §3.4(ii)): the standing operator-side A1
FAIL is adjudicated **defect-class** — no GWM clone resolvable from
`4ndr0tools/4NDR0MEDA`, and `pinchain.py` rendered the unresolvable target as
FAIL instead of UNREACHABLE (`subprocess.run` rc semantics; differential
signature A1-FAIL + A2-UNREACHABLE from the same missing clone, proven by the
operator's full-table paste). Witness-side ancestor-reachability green at
GWM@`4062d7f`; pin value `23a9615` unchanged; no re-pin. **Fixed**:
(1) `--workspace` / `--gwm` / `--cdp` / `--download` path overrides
(D-class #2) — production layouts now resolve the anchors the sibling-clone
layout does; (2) `is_repo()` resolvability guards — missing clones report
UNREACHABLE with the remedy, never a false FAIL (differential test at commit:
`--gwm /nonexistent` renders A1 UNREACHABLE); (3) verify companions print the
full per-anchor table (D-class #1). README troubleshooting gains the
differential-signature row. Manifest re-stamped (43/43). No anchor, protocol,
or constitution changes (A13 discipline).

## [2026-10-28] — polish-pass-2026-10-28

Operator work order (memobase combat-assessment reverse-engineering): production
readiness for public consumption. **Added**: `LICENSE` (Apache-2.0 — closes the
no-license blocking gap), `CHANGELOG.md` / `ROADMAP.md` / `CONTRIBUTING.md`,
`.github/workflows/verify.yml` (CI: manifest verify + pinchain tri-state + tool
compile — the integrity claims become continuously recomputed on every push),
`assets/` (the Ψ glyph + hero banner, geometry byte-faithful to the
operator-presented SplashScreenGlyphIcon), `docs/` (index, architecture,
verification — in-repo rather than wiki so every page rides the manifest;
self-stamping law wins). **Changed**: `README.md` restructured for landing
(hero banner, news, table of contents, two-layers scope bridge, citation
section, license row); all W1–W9 workflow content preserved. Gates: manifest
41/41 (self-stamped), pinchain 13 checked / 0 FAIL / 5 unreachable (debt
classes unchanged). No protocol, constitution, or anchor changes — PROTOCOL.md
untouched (A13 discipline).

## [2026-10-26] — ruling-R decoupling (task62 re-cut)

A1 re-typed to the session-archive snapshot class under
ancestor-reachability: MEDA decoupled from GWM boards cadence (GWM bundles
never require a MEDA leg; MEDA maintenance = session-close cadence at operator
discretion; A1 FAIL narrowed to the history-rewrite/detached-substrate tamper
class). `setup.sh` exec-bit repair. README W8 + troubleshooting A1-FAIL row
re-typed in-commit (tool and docs stay one system). Supersedes `897e957`
(unapplied). Base `90a57cc`.

## [2026-10-24] — maintenance-2026-10-24 (v1.7-era alignment + user on-ramp)

A1 re-pinned `088ef69` → `23a9615` (17-commit substrate delta inspected, zero
pinned-artifact drift); A3 re-verified unchanged. `setup.sh` added — one-file
entry point, six fail-closed legs, auto-detected detached/in-repo modes.
`README.md` rewritten as the comprehensive stepwise guide: identity table,
per-file repository map, workflows W1–W9, tri-state anchor semantics,
troubleshooting table, scope labels and non-claims. Gates: manifest 30/30,
pinchain 0 FAIL.

## [2026-10-23] — production pass + v1.6-era dual re-pin

Truth-restore delta rebased (supersedes the undelivered `2f8eca6` trio): A13
row PENDING → ADOPTED (digest byte-stable), adoption recorded GENESIS Block 1,
README provenance v1.5, STATE-ECHO A1–A10 → A1–A13. Earlier the same day:
maintenance re-pin A1 → `4bc2cfb` + A3 → `6facbf17` (v1.6-era dual re-pin).
First fully-clean gate: pinchain 13 OK / 0 FAIL / 0 unreachable.

## [2026-10-20] — maintenance re-pin

A1 re-pinned to `1e165df` (ten-commit substrate advance inspected, zero
drift; anomaly-capture A6-class anchor PASS).

## [2026-10-19] — v0 scaffold

Repository established. Protocol formalization (PROTOCOL.md v1.5),
bootstrap machinery (P0–P5), verification tooling (manifest, pinchain,
reconcile, state_echo), machine-facing prompts, operator runbooks, anchor
registry A1–A13, GENESIS founding record. Scaffold authored by the Witness
instance under §4 AI-involvement disclosure.
