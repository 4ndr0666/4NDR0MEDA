# PLACEHOLDER — LINEAGE BUNDLE (slot A10, RESERVED)

**Status:** reserved, not yet sealed. Pending operator visibility
adjudication.

## What this slot is for

PIN-CHAIN A2 records that the public record's L1 (pre-rename whole-file
pins) recomputes 10/10 from commit `a207175` — but only where a GWM clone
exists, because the squash-bundle (A4) carries no pre-port lineage. This
slot holds the artifact that fixes that everywhere:

- **Artifact:** a git bundle of glm-working-memory's full history
  (complete history, single ref), which by construction carries
  `a207175474b850a8d001c19ddb2325f7e49f4084`.
- **Build (operator-side):**
  `git -C glm-working-memory bundle create gwm-lineage.bundle main`
- **Verify on receipt:**
  `sha256sum gwm-lineage.bundle` → record here and in PIN-CHAIN A10;
  `git bundle verify gwm-lineage.bundle`;
  `git bundle list-heads` → exactly one ref.
- **Effect when sealed:** A2 becomes executable anywhere:
  clone-from-bundle, run the L1 loop, expect 10/10.

## Visibility note (the adjudication)

GWM history may contain material beyond the public record's scope. Sealing
A10 into THIS repo publishes that lineage to whoever can read this repo.
Options for the operator:

1. **Seal here** — maximum verifiability; publish the lineage.
2. **Seal in a separate access-controlled repo** — keep this slot pointing
   to it by digest only.
3. **Never seal** — annotate instead (CDP PIN-CHAIN-RECOMPUTATION already
   documents the a207175 dependency); A2 stays substrate-local.

All three are protocol-consistent; the anchor stays RESERVED until the
operator picks one.
