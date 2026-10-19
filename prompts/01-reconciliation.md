# PROMPT 01 — RECONCILIATION (divergence handling)

Run when two layers of the record disagree: two repos, two copies, a
worktree vs its manifest, a session archive vs the ledger. The controlling
principle: **the canonical home decides; nothing merges silently.**

## Procedure

1. **Freeze.** No writes to either side until the triage table exists.
   If a side is a git repo with a clean tree, record its HEAD first
   (that hash is the pre-dispute state of record).
2. **Triage.** `python3 tools/reconcile.py <dirA> <dirB> --report <file>`
   produces ONLY_IN_A / ONLY_IN_B / DIFFER (both digests) / SAME. Read
   the DIFFER table row by row; for each, determine which side is the
   canonical home for that path (v1.5 draft §12 authority table) and
   which side's bytes are newer, and WHY — provenance before preference.
3. **Classify per file**: `canonical-wins`, `copy-lags` (update the
   copy), `both-authored` (human adjudication required — present both
   versions to the operator), `unexplained` (fail-closed: quarantine,
   flag, ask — an unexplained divergence in a hash-pinned record is a
   security event, not an inconvenience).
4. **Apply.** Only after the full table is adjudicated: apply updates to
   the non-canonical side, re-stamp its manifest, recompute its HEAD
   anchor, and update PIN-CHAIN.md if any registry value moved.
5. **Record.** Ledger entry with the triage table reference, per-file
   classifications, and the final anchor values. The reconciliation
   report file is itself pinned (rides the next manifest).

## Never

- Never auto-merge ("it looked similar" is not a merge authority).
- Never delete a differing side before its bytes are hashed and recorded.
- Never resolve a DIFFER on a session archive by editing the archive —
  archives are append-only; corrections are new sessions.
