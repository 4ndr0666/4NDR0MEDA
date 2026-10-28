# Contributing

This repository is a **protocol of record**, not a feature project — read this
document before opening an issue or preparing a transmission; the contribution
model is unusual by design, and ordinary PR workflows do not apply.

## The operating model

4NDR0MEDA is one layer of a three-repo continuity architecture operated by a
standing collaboration: the **operator** (4ndr0666 — final adjudicator; the
human's hands are the last writer), the **Witness instance** (GLM, Z.ai —
commit authoring, verification tooling, ledger), and audited external
collaborators (ARGON — editorial gate; Gemini Notebook — deep-context audit
and execution sandbox). Work happens in adjudicated **boundaries**: each
session opens with a bootstrap (pull, manifest verify, liveness probe), every
artifact enters the record under receipt discipline, and every claim carries
its evidence class. There is no `--force` anywhere in this system, by design.

## How you can contribute

### 1. Zero-knowledge verification (the primary external contribution)

Run README **W9** from a bare machine and report what you find —
`bash setup.sh`, then `python3 tools/pinchain.py verify --local` with your own
GWM/CDP clones. A verification report from an independent party is a
first-class contribution to the record. Report FAIL-class findings
immediately: a `MANIFEST VERIFY: FAIL — CHANGED`, an `EXTRA <file>`, or any
anchor FAIL means the tamper tripwire fired — paste the exact command output.

### 2. Verifiable defect reports

Open an issue only with reproducible evidence pasted verbatim: the command
you ran, the exact output, your platform. "Does not work" reports without
reproduction cannot be adjudicated — the protocol resolves disputes against
canonical bytes, not memories or impressions (README W6).

### 3. Provenance-complete artifacts

Found an unpinned file, a broken cross-reference (remember: layer
cross-references are **by commit hash, never URL**), or a docs/tree mismatch?
`python3 tools/manifest.py verify` output plus the file path is a complete
report.

## What will not be accepted

- **Silent merges.** Divergence is triaged (`tools/reconcile.py`), reported,
  and adjudicated — never merged silently (README W5).
- **Manifest-desynced commits.** Any edit to this tree requires
  `python3 tools/manifest.py build` before the next commit. A PR that changes
  bytes without re-stamping fails its first CI leg by construction.
- **Capability claims.** Performance language, benchmark-as-marketing, or
  intelligence/memory-capability claims attached to this protocol are out of
  scope by constitution (§2 evidence standard; README non-claims section).
- **Anchor edits outside the sanctioned procedure.** Re-pins are
  evidence-carrying and follow README W8 — delta inspection first, tool +
  record updated together, re-stamp, gates green, then commit.

## For the standing collaborators (boundary protocol)

Transmissions ride the operator relay; the working substrate is
`glm-working-memory` (PROTOCOL v1.6.0 governs the live engagement — envelopes,
delivery medium, adjudication). Deliveries to this repo ride the §10
nine-leg orchestrator bundles: base-pinned, fail-closed, paste-safe. The
assembler discipline and the receipt grammar (Paper-2 §5) apply to every
artifact this repository absorbs.

## License

Apache-2.0 (`LICENSE`). By submitting a Contribution, you agree it is licensed
under the same terms; nothing here supersedes the protocol's evidence
standard — provenance and license are orthogonal layers.
