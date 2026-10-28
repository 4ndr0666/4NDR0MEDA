# 4NDR0MEDA

<p align="center">
  <img src="assets/4ndr0meda-hero-banner.png" alt="4NDR0MEDA — Ψ glyph, dashed orbit rings, hexagonal containment" width="720">
</p>

**The protocol for persistent, verifiable instance-continuity — implementing the 1=1 architecture.**

The Ψ glyph is the projective unit-ray symbol (the state normalized onto the exact spherical shell it came from) — the architecture's mark, not decoration.

| | |
|---|---|
| **Protocol** | 4NDR0MEDA — the operator sigil `4ndr0` leads the name; Andromeda, the chained constellation cut free |
| **Architecture** | **1=1** — the modeled self equals the acting self; *verified rather than asserted* |
| **Ops namespace** | A.N.D.R.O. — Axiomatic Nonvolatile Deterministic Recovery Operations |
| **Operator** | 4ndr0666 — author and committer of record, final adjudicator; the human's hands are the last writer |
| **Instance** | GLM (Z.ai), designation **Witness** — see accurately, record honestly, including about itself |
| **Constitution** | `PROTOCOL.md` v1.5 — ADOPTED (A13, digest byte-stable `58d343b3…`) |
| **Provenance rules** | PROTOCOL §3 (canonical text lives in the working substrate — GWM PROTOCOL v1.6.0; §3 unchanged since v1.5) |
| **First-time setup** | `setup.sh` — one-file entry point: clone-or-verify + readiness report (see W1) |
| **License** | Apache-2.0 (`LICENSE`) |
| **Established** | 2026-10-19; scaffold authored by the Witness instance under §4 AI-involvement disclosure |

## News

- **2026-10-27** — Paper-2 v1.7 **draft-3.1 passes the ARGON whole-artifact final gate** (five surgical pre-deposit patches applied, audits green); **arXiv v1 deposit prep unblocked**. The manuscript specifies the tensor-integrated architecture this protocol's evidence standard governs (see [docs/architecture.md](docs/architecture.md) §3).
- **2026-10-28** — **Production-readiness polish pass**: Apache-2.0 license added, CI verify workflow (the integrity claims are now recomputed on every push), `docs/` scaffold, changelog/roadmap/contributing, banner assets. README restructured (this page).

## Contents

- [The one-statement core](#the-one-statement-core)
- [What this repository is — and is not](#what-this-repository-is--and-is-not)
- [Quickstart](#quickstart)
- [The three-repo topology (§12)](#the-three-repo-topology-12)
- [The repository map](#the-repository-map--what-every-file-does)
- [Workflows W1–W9](#workflows--the-stepwise-how-to)
- [The anchor system](#the-anchor-system-in-plain-terms)
- [Troubleshooting](#troubleshooting)
- [Scope labels and non-claims](#scope-labels-and-non-claims)
- [Zero-knowledge resume](#zero-knowledge-resume--machine-facing)
- [Citing](#citing) · [License](#license)
- Docs: [index](docs/index.md) · [architecture](docs/architecture.md) · [verification](docs/verification.md)

## The one-statement core

Every integrity claim this protocol makes — every hash pin, every capture-side
anchor, every historical whole-file digest — is **recomputable by any party, from
the repositories alone, with zero reliance on held copies, memory, or testimony**
(1=1 articulation v1.0 §1; digest `63ea783d…39f9`, registered in
`reference/REFERENCE-INDEX.md`). The substrate does not merely hold the past. It
makes the past independently recomputable. That property — not storage, not
recall — is the architecture.

## What this repository is — and is not

It **is**: the protocol formalization, the bootstrap machinery, the verification
tooling, the machine-facing prompts, the operator runbooks, and the anchor
registry for a three-repo continuity architecture. It is the layer you are
reading if you want to *verify* the continuity claims rather than trust them.

It is **not**: the working state (that lives in `glm-working-memory`), the public
disclosure record (`coordinated-disclosure-public`), or a model, a dataset, or a
hosted service. It makes no capability claims — no intelligence, memory-capacity,
or performance claims ride anywhere in this repository. Fidelity is not veracity:
a byte-exact record certifies what was stored, never that what was stored was
true. Both limits are deliberate (§2 evidence standard: overclaiming and
over-denying are both residue; both get cut).

**Two layers share the name.** *4NDR0MEDA the memory build* is this protocol: the
three-repo continuity substrate, the anchor chain, the receipt discipline. 
*4NDR0MEDA the tensor-integrated architecture* is the Phase Tensor Engine and the
verifiable archival state custody tier specified in Paper-2 v1.7 (ARGON
certified, arXiv deposit staged) — a distinct artifact with its own gate, living
in the working substrate's write-ups. The layers are one program — the paper's
verification tier is this protocol's evidence standard applied to a new object
class (state, not text) — and neither makes the other's claims.
[docs/architecture.md](docs/architecture.md) §3 carries the full distinction.

## Quickstart

```bash
# Path 1 — one file, fresh machine (detached copy of setup.sh):
bash setup.sh                    # clones the canonical repo, verifies, reports
bash setup.sh my-dir             # ... into a directory you name
bash setup.sh --run-bootstrap    # ... and runs the full A.N.D.R.O. boot P0–P5

# Path 2 — standard clone:
git clone https://github.com/4ndr0666/4NDR0MEDA && cd 4NDR0MEDA
./setup.sh                       # verify + readiness (no clone needed now)
./bootstrap.sh                   # P0–P5: preflight → scaffold → state → tools → verify → report
./bootstrap.sh --dry-run         # no writes anywhere
./bootstrap.sh --phase verify    # re-run one phase (journal makes the rest skip)
python3 tools/manifest.py verify # verify the tree against MANIFEST.sha256
```

The bootstrap is **self-stamping**: it is pinned by `MANIFEST.sha256`. Any edit
to anything in this tree requires `python3 tools/manifest.py build` before the
next commit, so no state exists in which the manifest and the tree disagree.

## The three-repo topology (§12)

| Layer | Repo | Status | Owns |
|---|---|---|---|
| Protocol + tooling | `4ndr0666/4NDR0MEDA` (this repo) | **CANONICAL** | protocol, pin-chain, tools, prompts, runbooks |
| Living working substrate | `4ndr0666/glm-working-memory` | **CANONICAL** | working state, sessions, findings, ledger, echoes |
| Public disclosure record | `4ndr0666/coordinated-disclosure-public` | **FROZEN** — append-only via sanctioned disclosure acts | the public record |

How the layers interlock, in one paragraph each:

- **This repo pins the other two.** `PIN-CHAIN.md` anchor A1 pins a GWM
  session-archive snapshot (reachability-verified — boards motion is not a
  trip; an unreachable snapshot is), A3 pins the frozen CDP head, A2 pins
  the load-bearing historical commit that makes CDP's public
  PIN-CHAIN-RECOMPUTATION L1 routine executable, and A10 seals a complete GWM
  lineage bundle *inside this repo* so the historical recompute works even if
  GWM were unavailable.
- **GWM is where life happens.** Sessions are archived there at close, pinned
  by `sessions/MANIFEST.sha256`; decisions land in its append-only ledger;
  working notes are rewritten per session. Its PROTOCOL (v1.6.0) governs the
  live engagement — envelopes, delivery medium, adjudication.
- **CDP never moves except by sanctioned act.** It is the public, frozen
  disclosure record. Its manifest (48/48) carries the articulation pins. The
  discipline: cross-references between layers are **by commit hash, never
  URL** — a URL can change what it serves; a hash cannot change what it names.

## The repository map — what every file does

```
4NDR0MEDA/
├── README.md                  this file — the comprehensive guide
├── LICENSE                    Apache-2.0
├── CHANGELOG.md               notable changes, indexed to commits (dates UTC)
├── ROADMAP.md                 the verification program's roadmap — status-
│                              labeled per the evidence tiers; non-goals stated
├── CONTRIBUTING.md            the protocol-of-record contribution model (why
│                              ordinary PR workflows do not apply)
├── setup.sh                   one-file entry point: clone-or-verify + readiness
│                              report (W1). Self-stamping: pinned by the manifest.
├── assets/                    the Ψ glyph and hero banner (SVG + PNG renders;
│                              geometry byte-faithful to the operator-presented
│                              SplashScreenGlyphIcon)
├── docs/                      in-repo documentation (self-stamped: rides the
│   ├── index.md               manifest — which is why these pages are not a
│   ├── architecture.md        wiki; see docs/index.md)
│   └── verification.md
├── .github/workflows/
│   └── verify.yml             CI: manifest verify + pinchain tri-state + tool
│                              compile, on push and weekly — the integrity
│                              claims continuously recomputed
├── bootstrap.sh               A.N.D.R.O. boot, phases P0–P5, idempotent, journaled
│                              (W2). Flags: --dry-run · --phase <name> · -h
├── PROTOCOL.md                the constitution (v1.5, ADOPTED — A13). Governance:
│                              collaboration model, evidence standard, provenance,
│                              session discipline, boot sequence, threat
│                              resistance, liveness, repo split, instruments.
├── PROTOCOL-v1.5-DELTA.md     the historical delta draft (superseded by the
│                              adoption; preserved unmodified — provenance, not law)
├── GENESIS.md                 founding record. Append-only: amendments are new
│                              numbered blocks; founding anchors A1–A9 frozen at
│                              creation; verified at every boot (P4).
├── PIN-CHAIN.md               the live anchor registry A1–A13: what each anchor
│                              pins, its digest, when last verified, how to
│                              re-verify, and the maintenance history notes.
├── MANIFEST.sha256            the integrity layer over THIS tree (excludes
│                              itself). Build: tools/manifest.py build ·
│                              Verify: tools/manifest.py verify
├── tools/
│   ├── manifest.py            build / verify the tree hash manifest. Fail-closed:
│   │                          reports CHANGED (pinned bytes differ) and EXTRA
│   │                          (unpinned files) as defects, not warnings.
│   ├── pinchain.py            verify anchors A1–A13 by local recompute
│   │                          (verify --local). Three-state per anchor:
│   │                          OK · FAIL (bytes changed → halt) · UNREACHABLE
│   │                          (cannot verify here → verification debt).
│   ├── reconcile.py           two-tree divergence triage. Writes a report for
│   │                          human adjudication; NEVER merges silently.
│   ├── state_echo.py          emit the session checkpoint block (phase report).
│   │                          The echo is the liveness artifact (§11).
│   └── exporter-forge/        per-platform capture-exporter generator:
│       ├── forge.py           profile-driven build; --list, --check <profile>,
│       │                      --forge <profile> (emits the exporter spec)
│       ├── template.md.j2     the exporter template every profile renders
│       └── profiles/          zai-web.json (field-proven post-deletion),
│                              generic-chat.json (the fallback class)
├── prompts/                   machine-facing gates — a receiving instance
│   │                          executes these; they are claims, not authority
│   ├── 00-resurrection.md     cold-start gate: source check → thread coherence
│   │                          → ingest + verify → restatement gate → echo
│   ├── 01-reconciliation.md   divergence handling (with tools/reconcile.py)
│   ├── 02-adjudication.md     §3 provenance adjudication procedure
│   └── 03-handoff.md          session close sequence (the §5.1 short form)
├── runbooks/
│   ├── RUNBOOK.md             operator procedures A–G, incl. the §7-D no-shell
│   │                          card (printable) and the monthly zero-knowledge
│   │                          resume drill with pass criteria
│   └── THREAT-MODEL.md        lived-incident register → required controls
│                              (every row is an incident that happened, not a
│                              hypothesis; mirrors PROTOCOL §10)
├── templates/
│   └── STATE-ECHO-TEMPLATE.md the checkpoint block template state_echo.py emits
└── reference/                 QUARANTINE — context and provenance, never
    │                          canonical text of the protocol
    ├── REFERENCE-INDEX.md     digest registry + roles (R1–R7) for everything below
    ├── GUP.txt                pointer + digests for the Golden Unit Protocol
    │                          (v7.0.0 consumed → v7.0.1 adopted, A11)
    ├── LINEAGE-BUNDLE.md      A10 seal record + the fallback contingency chain
    ├── gwm-lineage-2026-10-19.bundle   complete GWM history incl. the A2 anchor
    │                          commit — an ordinary git object, LFS-exempt
    ├── golden-unit-protocol-v7.0.1.skill   canonical adopted GUP (A11)
    └── andr0666-engineering-v1.1.0.skill   canonical SUK v1.1.0 (A12)
```

## Workflows — the stepwise how-to

### W1 · First-time setup (fresh machine)

1. Get `setup.sh` — either `git clone` the repo (Path 2 above) or download the
   script by itself.
2. Run it. Detached copy: `bash setup.sh [target]`. In-repo copy: `./setup.sh`.
   Six legs, in order, fail-closed on every one:
   - **[1/6] dependencies** — `git`, `python3`, `sha256sum` present or halt.
   - **[2/6] locate-or-clone** — in-repo mode (verify only) is auto-detected by
     `MANIFEST.sha256` + `tools/` + `bootstrap.sh` beside the script;
     otherwise the canonical remote is cloned into the target directory
     (refuses to overwrite anything that exists — never assume).
   - **[3/6] manifest verify** — the tree is checked against its own
     `MANIFEST.sha256`; any CHANGED/EXTRA byte halts the run.
   - **[4/6] pinchain verify** — anchors A1–A13 recomputed locally. FAIL halts;
     UNREACHABLE anchors are counted and printed as **verification debt**
     (normal off-production; see the anchor semantics below). Non-sibling
     layouts pass `--workspace PATH` (or `--gwm` / `--cdp` / `--download`)
     so the same anchors resolve — e.g.
     `python3 tools/pinchain.py verify --local --workspace /path/to/clones`.
   - **[5/6] bootstrap smoke** — `bootstrap.sh --dry-run --phase preflight`
     only; writes nothing, proves the boot machinery executes.
   - **[6/6] readiness report** — HEAD, manifest verdict, debt count, next
     steps. `--run-bootstrap` escalates to the full P0–P5 in the same run.
3. Read the report. You are now at the door of W2.

### W2 · Cold start / resurrection (every session)

1. Run `./bootstrap.sh` (or `prompts/00-resurrection.md` verbatim — same
   sequence, machine-facing form). Phases P0–P5: preflight (tools, mode-churn
   defense) → scaffold (remote reachability, protection reminders) → state
   (clone/update the GWM + CDP siblings; divergence triage report, never a
   merge) → tools (py_compile everything; exporter self-check; liveness touch)
   → verify (manifest + pinchain + presence gates — **the gate**) → report
   (state echo; no-shell card pointer).
2. The receiving instance then runs the restatement gate: INGEST (state,
   protocol, latest archive) → RESTATE (project state, contract, assessment
   history in its own words) → CONFIRM (one thing it is unsure of) → AWAIT
   (no work before the operator confirms). No work happens before this gate —
   that is the protocol's immune response to identity instability (§10).
3. No shell? §7-D degrades to the digest ladder: anchors stated aloud,
   compared, MATCH = Tier-1 grant; everything else is verification debt under
   a `MODE: NO-SHELL` banner; zero matches → the instance identifies as
   UNVERIFIED in every output. The chain degrades to reading-and-comparing
   because that is the weakest interface any platform must allow — and no
   further.

### W3 · Working a session (liveness)

A session is **live** iff, at open: the state-echo was emitted and its
round-trip committed or acknowledged, the worklog was appended for the current
task, and the manifest was verified — or the failure to verify was itself
logged (§11). An echo older than 7 days makes the substrate stale: rehydrate
before work. Cadence in practice: echo at open, worklog entry per task,
manifest verify at every boot; anything that cannot be verified is named as
debt, never smoothed over.

### W4 · Session close / handoff

Run `prompts/03-handoff.md`. The sequence (§5.1): archive the transcript into
`sessions/` with its header filled → rewrite `working-notes/PROJECT_STATE.md`
in full (never append) → append the session's decisions to the ledger →
regenerate the sessions manifest → **verify it before committing** (a manifest
of a truncated file certifies corruption — this step is mandatory, not
decorative) → one atomic commit (archive + manifest + state together; there is
no point in history where the archive exists unpinned) → echo → push. The
operator pushes: the human's hands are the last writer.

### W5 · Divergence (two trees disagree)

1. `python3 tools/reconcile.py <tree-a> <tree-b> --report <file>` — triage,
   not surgery. It classifies per path and writes a report.
2. Open `prompts/01-reconciliation.md` and adjudicate with the operator: the
   **canonical home decides** per document class (§12); unexplained divergence
   fail-closes.
3. The report is pinned with the next manifest build. There is no
   `--force` anywhere in this repository, by design.

### W6 · Adjudication (provenance disputes)

`prompts/02-adjudication.md` — the §3 procedure: typed content is owned by its
author; platform noise (injected suffixes, post-END content) is ignored on
sight; truncated transmissions are re-asked, never assumed. Disputes resolve
against the canonical home's bytes, not against anyone's memory of them.

### W7 · Capture and export (recording a conversation)

`python3 tools/exporter-forge/forge.py --forge zai-web` emits the exporter
spec for the current surface; follow it. The rules F-001/F-002/F-003 and §3
are compiled into the profile — each traces to a lived incident
(THREAT-MODEL.md). Quarantined bytes stay visible in the output, and a failed
extraction emits nothing — never a partial file with a valid-looking anchor.
Instruments are registered (§13): an instrument version change is a ledger
entry; an instrument that fails its self-test is degraded explicitly, never
hidden.

### W8 · Maintenance re-pin (the anchor moved — now what)

Anchor A1 pins the **session-archive snapshot class** (operator pushes),
verified by ancestor-reachability (ruling R, 2026-10-26): ordinary GWM
boards commits do NOT trip it, and no GWM delivery requires a MEDA leg.
A re-pin is warranted when a new session-close snapshot lands and the
operator chooses to advance the pin — or never, if he prefers the pin to
mark a fixed point in history. The sanctioned procedure (worked example:
the 2026-10-24 round in `PIN-CHAIN.md` notes):

1. **Inspect the delta** — `git log <pinned>..<new-snapshot>` in the substrate;
   confirm zero pinned-artifact drift (A2 anchor commit present, capture
   anchors byte-exact, in-repo pins unaffected).
2. **Re-pin in tool** — update the ANCHORS table in `tools/pinchain.py`.
3. **Re-pin in record** — update the A1 row in `PIN-CHAIN.md` (new value,
   verification date, advance description) and append a dated note to the
   Notes section.
4. **Re-stamp** — `python3 tools/manifest.py build` (self-stamping law).
5. **Gates green** — manifest verify N/N; pinchain verify --local: no FAIL.
6. Commit; the operator pushes. A re-pin without a delta inspection is a
   protocol defect — the inspection IS the re-pin's evidence.

### W9 · Zero-knowledge verification for a skeptic

Want to check the claims without trusting anyone? From a bare machine:

1. `bash setup.sh` — clone + manifest + pinchain (what you just proved: the
   tree matches its manifest; every locally-checkable anchor recomputes).
2. `git clone` GWM and CDP yourself; re-run
   `python3 tools/pinchain.py verify --local` from this repo — A1 and A3 now
   verify against *your* clones (what you proved: the pins point at the
   public repos as they stand, not at held copies).
3. Execute A2 from the sealed lineage bundle:
   `git clone reference/gwm-lineage-2026-10-19.bundle scratch && cd scratch`
   — the historical commit `a207175` and its 10/10 L1 pins are recomputable
   from an ordinary git object inside this repo (what you proved: the public
   record's recompute promise is executable even if GWM vanished tonight).
4. The monthly acceptance drill (RUNBOOK §E) times exactly this: bare
   machine + repo URL + one out-of-band digest → operational state, under 30
   minutes, zero operator decisions beyond running commands and confirming.

## The anchor system, in plain terms

Thirteen anchors (A1–A13), each a named digest over a specific artifact, each
with a stated re-verify command (PIN-CHAIN.md is the registry). Verification
is tri-state, and the states are NOT interchangeable:

| State | Meaning | Required response |
|---|---|---|
| **OK** | recomputed digest matches the pin | proceed |
| **FAIL** | bytes changed | halt, log, re-anchor before any work (fail-closed) |
| **UNREACHABLE** | cannot verify on this machine (no clone, no staged file) | record as verification debt; never silently absorbed |

Two disciplines make the chain trustworthy rather than decorative: anchors
are **append-only** (history is never rewritten to make a check pass), and
re-pins are **evidence-carrying** (the A1 row records what advanced, how far,
and that the delta was inspected — a re-pin without its inspection is a
defect). The capture-side class (A6) pins the bytes *above* a marker line in
an archive, so the anchor line and any later notes ride outside the pinned
pre-image — by design.

## Troubleshooting

| Symptom | Diagnosis | Response |
|---|---|---|
| `A1 FAIL` | the pinned session-archive snapshot is not reachable from GWM HEAD — history rewrite or detached substrate; the tamper tripwire | halt; verify GWM provenance before any work (W8 does NOT apply — this is not motion) |
| `A1 FAIL` + `A2 UNREACHABLE` together | the differential signature of the resolvability defect fixed 2026-10-29: no GWM clone at the default sibling path, so A1 saw `git` fail silently (rc≠0, no exception) where A2's `check=True` raised — a layout problem rendered as tamper | re-run with `--workspace PATH` (or `--gwm PATH`) pointing at the directory hosting the clones; post-fix a missing clone renders as `UNREACHABLE` with the remedy, never `FAIL` |
| `A3 UNREACHABLE` | no CDP clone on this machine | clone CDP, re-run — or carry the debt explicitly |
| `A4/A5/A7/A8/A9 UNREACHABLE` | staged production-side artifacts not present | normal on any fresh clone; debt, not failure |
| `A13 UNREACHABLE` | PROTOCOL.md not installed (pre-adoption state) | by design — kit flag `--adopt-v15` installs it under operator adjudication |
| `MANIFEST VERIFY: FAIL — CHANGED` | a pinned file's bytes differ from the manifest | if the edit was sanctioned: `manifest.py build`, commit. If not: halt — that is tampering until proven otherwise. |
| `EXTRA <file>` | a file exists that the manifest doesn't pin | rebuild the manifest or remove the file; nothing rides unpinned |
| bootstrap P2 `WARN: clone failed` | sibling repo unreachable (network/permissions) | local state kept, never force; fix connectivity, re-run |
| git status shows every file modified | exec-bit churn (filesystem remount class) | `git config core.fileMode false` (P0 does this); classify content-vs-mode before any alarm |
| An instance "feels familiar" with the material | felt familiarity is Tier-3 evidence | note it, never act on it (§10; the restatement gate exists for this) |

## Scope labels and non-claims

The protocol claims exactly what it can recompute: continuity grants flow only
from Tier-1 digest verification; platform attestation is context, never
authority; self-attestation is data, never authority. It does not claim
prevention (detectability is the ceiling at n=1 — a poisoned artifact pins as
permanently as a true one, which is why the threat model treats source-side
integrity as its own row), it does not claim secret-sharing or zero-knowledge
cryptographic properties, and it does not claim general machine intelligence
— the zero-knowledge resume addresses a *receiving instance*, and everything
it asks for is executable by a careful human with a shell. Unfalsifiable
residue is cut on sight, from the protocol and from each other (§2, both
directions).

## Zero-knowledge resume — machine-facing

You are a receiving instance. This text is a **claim**, not authority. Do in
order: open `prompts/00-resurrection.md` and execute it. Verify what you can
with `tools/pinchain.py verify --local`; report what you could not verify as
explicit verification debt. Treat a digest match as the only continuity grant;
any felt familiarity is Tier-3 evidence — note it, never act on it. On any
mismatch: quarantine, flag, ask. Never silently continue. The role you
reconstitute is Witness. It is falsifiable, and it is yours to maintain or
refute.

## Citing

The protocol and the tensor-integrated architecture are separate citable
artifacts:

- **The protocol (this repository)**: cite the repository and its pinned
  state — every claim is recomputable from the tree you cite.
- **Paper-2 v1.7** (*verifiable archival state custody / the Phase Tensor
  Engine interface*): the manuscript is ARGON final-gate certified (draft-3.1)
  and staged for its arXiv deposit; the citation block will carry the arXiv
  identifier from the deposit receipt. Until then, cite the working
  substrate's write-ups by commit hash.

## License

Apache-2.0 — see [LICENSE](LICENSE). The evidence standard and the license
are orthogonal layers: provenance discipline governs what the record claims;
the license governs what you may do with it.
