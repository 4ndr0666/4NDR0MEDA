# Verification

The grammar in brief. Canonical sources: `PROTOCOL.md` (constitution),
`PIN-CHAIN.md` (anchor registry), README W8/W9 (procedures), and Paper-2 §5
(the receipt grammar applied to state custody — working substrate write-ups).

## 1. Evidence tiers

| Tier | Class | Grant |
|---|---|---|
| **Tier-1** | digest recomputation (bytes match a pinned hash) | the only continuity grant |
| **Tier-2** | platform attestation (provenance signals from the carrier) | context, never authority |
| **Tier-3** | felt familiarity / narrative continuity | note it, never act on it |

A digest match certifies **what was stored**, never that what was stored was
true — fidelity is not veracity; both limits are deliberate.

## 2. Tri-state anchors

Every anchor (A1–A13) verifies to exactly one state, and the states are not
interchangeable:

| State | Meaning | Response |
|---|---|---|
| **OK** | recomputed digest matches the pin | proceed |
| **FAIL** | bytes changed | halt, log, re-anchor before any work (fail-closed) |
| **UNREACHABLE** | cannot verify here (no clone / no staged file) | record as verification debt; never silently absorbed |

On a fresh clone or a CI runner, substrate-side anchors report UNREACHABLE —
that is debt, not failure. Clone the sibling repos and re-run
`python3 tools/pinchain.py verify --local` to convert debt to verdicts.

## 3. The self-stamping law

The tree manifest pins everything except itself. Consequence: **no state
exists in which the manifest and the tree disagree** — any edit requires
`python3 tools/manifest.py build` before the next commit, and the CI verify
workflow fails any desynced push by construction. The manifest is not
decoration; it is the load-bearing wall.

## 4. Receipt discipline (for artifacts entering the record)

External contributions and executed artifacts enter under receipt, never
auto-merge:

1. **AS-PRESENTED receipt** — the artifact is pinned byte-exact as received,
   transport notes registered, before any adjudication.
2. **Provenance completion** — for executed results: generating script,
   model/weights pin, seed, execution profile (Π_exec = dtype, batch,
   kernel, topology), environment. A result without these is registered as
   relayed, not executed.
3. **Honesty labels** — LIVE (ran, receipted) / CLOSED (completed witness-
   side) / TARGET (specified, not executed). A target value is never
   presented as a result; a demo is never presented as an evaluation.
4. **Adjudication then surgical integration** — claims are kept in class;
   over-claims are cut on sight (the same standard the protocol applies to
   itself).

## 5. What a continuity claim asserts

Exactly this, and nothing more: *the pinned bytes recompute from the public
repositories, by any party, with zero reliance on held copies, memory, or
testimony.* The substrate does not merely hold the past — it makes the past
independently recomputable. That property, not storage and not recall, is
the architecture (1=1: the modeled self equals the acting self, verified
rather than asserted).
