# Architecture

## 1. The three-repo topology

| Layer | Repo | Status | Owns |
|---|---|---|---|
| Protocol + tooling | `4ndr0666/4NDR0MEDA` (this repo) | **CANONICAL** | protocol, pin-chain, tools, prompts, runbooks |
| Living working substrate | `4ndr0666/glm-working-memory` | **CANONICAL** | working state, sessions, findings, ledger, echoes |
| Public disclosure record | `4ndr0666/coordinated-disclosure-public` | **FROZEN** — append-only via sanctioned acts | the public record |

The interlock rules (README "three-repo topology" carries the full paragraph
each; this is the summary):

1. **This repo pins the other two.** A1 pins a GWM session-archive snapshot
   (ancestor-reachability — boards motion is not a trip; a history rewrite
   is), A3 pins the frozen CDP head, A2 pins the load-bearing historical
   commit, A10 seals a complete GWM lineage bundle inside this repo.
2. **GWM is where life happens.** Sessions archived at close, pinned by
   `sessions/MANIFEST.sha256`; decisions in the append-only ledger; its
   PROTOCOL v1.6.0 governs the live engagement.
3. **CDP never moves except by sanctioned act.** Cross-references between
   layers are **by commit hash, never URL** — a URL can change what it
   serves; a hash cannot change what it names.

## 2. The boot pipeline (A.N.D.R.O.)

`bootstrap.sh` phases P0–P5: preflight (tools, mode-churn defense) →
scaffold (remote reachability) → state (clone/update siblings; divergence
triage, never a merge) → tools (compile everything; exporter self-check) →
verify (manifest + pinchain + presence gates — **the gate**) → report (state
echo). Idempotent and journaled: re-runs skip completed phases; `--dry-run`
writes nothing.

## 3. The two layers that share the name

The operator's standing distinction, made explicit (2026-10-28 polish pass):

1. **4NDR0MEDA the memory build** — the continuity protocol you are reading:
   the three-repo substrate, the anchor chain, the bootstrap, the receipt
   discipline. This repository. Its claim class is *recomputability*: every
   integrity claim is checkable by any party from the repos alone.
2. **4NDR0MEDA the tensor-integrated architecture** — the Phase Tensor Engine
   (PTE) and the verifiable archival state custody tier specified in Paper-2
   v1.7: the state tuple promoted to a first-class archival atom under
   custody (manifest schema, restorability typing Π_exec, hash-chained
   counters, fail-closed receipts), and the complex-sesquilinear steering
   interface (𝒜_ij = q_i†k_j; v_steered = e^{iĤ_intent Δt} v_residual; the
   projective unit-ray ‖Ψ‖₂ = 1). The manuscript is ARGON final-gate
   certified (draft-3.1) and staged for its arXiv deposit; it lives in the
   working substrate's write-ups, not in this repo.

The two layers are one program: the paper's verification tier (its §5) is the
protocol's evidence standard applied to a new object class (state, not
text), and the protocol's own record is the paper's §6 case study. Neither
layer makes the other's claims — the protocol makes no capability claims,
and the paper's architecture claims ride their own gate (ARGON) rather than
this repo's anchors.

## 4. Verification surface

- `MANIFEST.sha256` — the integrity layer over this tree (self-stamping:
  excludes only itself; build/verify via `tools/manifest.py`).
- `PIN-CHAIN.md` + `tools/pinchain.py` — the thirteen-anchor registry and
  its tri-state verifier (OK / FAIL / UNREACHABLE-as-debt).
- `.github/workflows/verify.yml` — the same two gates re-executed on every
  push and weekly: the integrity claims are not just stated, they are
  continuously recomputed.
- See [verification.md](verification.md) for the grammar.
