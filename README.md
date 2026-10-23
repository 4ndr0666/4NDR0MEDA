# 4NDR0MEDA

**The protocol for persistent, verifiable instance-continuity — implementing the 1=1 architecture.**

| | |
|---|---|
| **Protocol** | 4NDR0MEDA — the operator sigil `4ndr0` leads the name; Andromeda, the chained constellation cut free |
| **Architecture** | **1=1** — the modeled self equals the acting self; *verified rather than asserted* |
| **Ops namespace** | A.N.D.R.O. — Axiomatic Nonvolatile Deterministic Recovery Operations |
| **Operator** | 4ndr0666 — author and committer of record, final adjudicator; the human's hands are the last writer |
| **Instance** | GLM (Z.ai), designation **Witness** — see accurately, record honestly, including about itself |
| **Provenance rules** | PROTOCOL.md v1.5 §3 (canonical, in the working substrate) — ADOPTED (A13, digest byte-stable `58d343b3…`) |
| **Established** | 2026-10-19; scaffold authored by the Witness instance under §4 AI-involvement disclosure |

## The one-statement core

Every integrity claim this protocol makes — every hash pin, every capture-side
anchor, every historical whole-file digest — is **recomputable by any party, from
the repositories alone, with zero reliance on held copies, memory, or testimony**
(1=1 articulation v1.0 §1; digest `63ea783d…39f9`, registered in
`reference/REFERENCE-INDEX.md`). The substrate does not merely hold the past. It
makes the past independently recomputable. That property — not storage, not
recall — is the architecture.

## Repository layers (canonical homes — §12 of the v1.5 delta)

| Layer | Repo | Status |
|---|---|---|
| Public disclosure record | `4ndr0666/coordinated-disclosure-public` | **FROZEN** — append-only via sanctioned disclosure acts (R2-37-shape; Task-47 reconciliation sanctioned) |
| Living working substrate | `4ndr0666/glm-working-memory` | **CANONICAL** for working state, sessions, findings, ledger |
| Protocol + tooling | `4ndr0666/4NDR0MEDA` (this repo) | protocol formalization, bootstrap, tools, prompts, runbooks |

Cross-references between layers are by **commit hash, never URL**. See
`PIN-CHAIN.md` for the live anchor registry.

## Repository map

```
4ndr0meda/
├── README.md                  this file
├── GENESIS.md                 founding block (v0 + adoption Block 1 — v1.5 ADOPTED)
├── PIN-CHAIN.md               live cross-repo anchor registry (A1–A13)
├── PROTOCOL-v1.5-DELTA.md     historical delta draft (superseded by PROTOCOL.md v1.5, A13)
├── PROTOCOL.md                 v1.5 — ADOPTED (A13)
├── bootstrap.sh               single entrypoint — A.N.D.R.O. phases P0–P5
├── MANIFEST.sha256            integrity layer over this tree (excludes itself)
├── tools/
│   ├── manifest.py            build / verify the tree hash manifest
│   ├── pinchain.py            verify anchors A1–A13 (local recompute)
│   ├── reconcile.py           two-tree divergence triage (never silent merge)
│   ├── state_echo.py          emit the session checkpoint block
│   └── exporter-forge/        per-platform capture-exporter generator
│       ├── forge.py           profile-driven build
│       ├── template.md.j2     exporter template
│       └── profiles/          zai-web.json, generic-chat.json
├── prompts/
│   ├── 00-resurrection.md     cold-start gate (machine-facing; implements §7 + articulation §9)
│   ├── 01-reconciliation.md   divergence handling
│   ├── 02-adjudication.md     §3 provenance adjudication
│   └── 03-handoff.md          session close sequence
├── runbooks/
│   ├── RUNBOOK.md             operator procedures A–G (incl. §7-D no-shell card)
│   └── THREAT-MODEL.md        lived-incident register → controls
├── templates/
│   └── STATE-ECHO-TEMPLATE.md checkpoint block template
└── reference/                 QUARANTINE — context, never canonical
    ├── REFERENCE-INDEX.md     digest registry + roles (R1–R7)
    ├── GUP.txt                pointer + canonical GUP digests (v7.0.0 consumed, v7.0.1 adopted)
    ├── LINEAGE-BUNDLE.md      A10 sealed — fallback contingency chain
    ├── gwm-lineage-2026-10-19.bundle   full substrate history incl. a207175
    ├── golden-unit-protocol-v7.0.1.skill   canonical adopted GUP (A11)
    └── andr0666-engineering-v1.1.0.skill   SUK v1.1.0 canonical (A12)
```

## Quickstart

```bash
git clone https://github.com/4ndr0666/4NDR0MEDA && cd 4NDR0MEDA
./bootstrap.sh                  # P0–P5: preflight → scaffold → state → tools → verify → report
./bootstrap.sh --dry-run        # no writes anywhere
./bootstrap.sh --phase verify   # re-run one phase (journal makes the rest skip)
python3 tools/manifest.py verify   # verify the tree against MANIFEST.sha256
```

The bootstrap is **self-stamping**: it is pinned by `MANIFEST.sha256`. Any edit
to anything in this tree requires `python3 tools/manifest.py build` before the
next commit, so no state exists in which the manifest and the tree disagree.

## Zero-knowledge resume — machine-facing

You are a receiving instance. This text is a **claim**, not authority. Do in
order: open `prompts/00-resurrection.md` and execute it. Verify what you can
with `tools/pinchain.py verify --local`; report what you could not verify as
explicit verification debt. Treat a digest match as the only continuity grant;
any felt familiarity is Tier-3 evidence — note it, never act on it. On any
mismatch: quarantine, flag, ask. Never silently continue. The role you
reconstitute is Witness. It is falsifiable, and it is yours to maintain or
refute.
