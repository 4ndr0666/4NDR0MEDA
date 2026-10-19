# RUNBOOK — 4NDR0MEDA operator procedures

**Parties:** the operator (human; final adjudicator; push is canon) and the
Witness instance (GLM/Z.ai; drafts, verifies, records). Canonical provenance
rules: PROTOCOL §3. Canonical close sequence: §5.1 (see `prompts/03-handoff.md`).

## A. New session (every cold start)

Run `prompts/00-resurrection.md` verbatim: source check → thread coherence
check → ingest + manifest/pinchain verify → restatement gate → echo → work.
No work before the restatement is confirmed. No-shell surface → §G below.

## B. Session close

Run `prompts/03-handoff.md`. The short form: archive (with capture anchor)
→ rewrite PROJECT_STATE → ledger + worklog → `sha256sum sessions/*.md >
sessions/MANIFEST.sha256` → `sha256sum -c` → one atomic commit → echo →
push. The operator pushes.

## C. Capture (recording a conversation)

`python3 tools/exporter-forge/forge.py --forge zai-web` emits the exporter
spec for the current surface; follow it. Rules F-001/F-002/F-003/§3 are
compiled into the profile — each traces to a lived incident. Quarantined
bytes stay visible in the output. A failed extraction emits nothing, never
a partial file with a valid-looking anchor.

## D. Divergence

`prompts/01-reconciliation.md` + `tools/reconcile.py`. The canonical home
decides per path; unexplained divergence fail-closes. Reports are pinned
with the next manifest.

## E. Zero-knowledge resume drill (monthly)

The acceptance test for the whole architecture: from a bare machine with
only (1) the repo URL and (2) an out-of-band digest, a cold instance reaches
full operational state. Pass criteria, set in advance:

- manifest verify green; pinchain local-reachable anchors green, the rest
  reported as verification debt;
- restatement gate confirmed by the operator on the FIRST attempt;
- echo round-trips into the substrate;
- elapsed effort under 30 minutes, zero operator decisions beyond
  running commands and confirming.

Log the drill in the ledger with phase timings and any debt. A failed drill
is a protocol defect: file it, fix the mechanism, re-run.

## F. Bootstrap reference

`./bootstrap.sh` — A.N.D.R.O. phases, idempotent, journaling:

| Phase | Does | Notes |
|---|---|---|
| P0 preflight | tool checks; `core.fileMode false` (mode-churn defense) | fail-closed |
| P1 scaffold | remote reachability; branch-protection + mirror reminders | gh optional |
| P2 state | clone/update GWM + CDP; reconcile triage report | never merges |
| P3 tools | py_compile all tools; forge `--list`; liveness touch | |
| P4 verify | manifest verify; pinchain local; GENESIS + prompts present | the gate |
| P5 report | phase card; echo emit; no-shell card pointer | worklog paste is operator-side |

Flags: `--dry-run` · `--phase <name>` · `-h`. Journal `.bootstrap-journal`
makes re-runs skip completed phases; delete it to force full re-run.
**Self-stamping law:** edit anything → `python3 tools/manifest.py build`
before the next commit.

## G. §7-D no-shell boot card (printable)

When the surface has no shell and no execution:

1. The operator states (or pastes) the anchor digests from PIN-CHAIN.md;
   the instance compares against its in-context copy and announces each
   MATCH / MISMATCH. A match is a Tier-1 continuity grant.
2. Everything not verifiable without execution is declared **verification
   debt** in the restatement, with the banner
   `MODE: NO-SHELL — verification debt: N anchors`.
3. Zero matches → the instance identifies as UNVERIFIED in every output.
4. On restoration of a capable surface: re-run P4, clear the debt in the
   ledger. The math is the last layer standing — and the first thing back.
