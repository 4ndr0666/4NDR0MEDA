# LINEAGE BUNDLE — sealed (slot A10)

**Status:** SEALED 2026-10-19. Operator adjudication (transmission of
2026-10-19): the lineage bundle goes into this repo — option 1, seal here —
so rehydration works anywhere with fallback contingency.

## Artifact registry

| Field | Value |
|---|---|
| File | `reference/gwm-lineage-2026-10-19.bundle` |
| Bytes | 4,153,194 |
| SHA-256 | `6d61b9fbbc3354f0a6a033481ad9116e9702e24593afaeec7e0109182f883b67` |
| Built from | glm-working-memory @ `5bdfbec153e2d4a303ea166a16cff4dc3f6e9dbc` (A1), `git bundle create --all`, 2026-10-19 |
| Contents | complete history, 35 commits, 4 refs (main / origin/main / origin/HEAD / HEAD), all → `5bdfbec` |
| Carries | `a207175474b850a8d001c19ddb2325f7e49f4084` (verified ancestor of HEAD) |
| Prerequisites | NONE — the bundle records a complete history; standalone |
| Effect | PIN-CHAIN A2 (L1 recompute 10/10) executable on any machine with nothing but this repo + the bundle |

## Verify on receipt

```bash
sha256sum gwm-lineage-2026-10-19.bundle   # expect 6d61b9fb…883b67 (A10)
git bundle verify gwm-lineage-2026-10-19.bundle   # expect "records a complete history"
git clone gwm-lineage-2026-10-19.bundle gwm && python3 ../4NDR0MEDA/tools/pinchain.py verify --local
```

Acceptance evidence (2026-10-19): scratch workspace rebuilt from nothing
but this bundle + this repo's tools → pin-chain **9/9 OK, 0 FAIL,
0 UNREACHABLE**, A2 = 10/10.

## Storage rule (dependency-minimal rehydration)

`.gitattributes` exempts `reference/*.bundle` from LFS and text filters:
this bundle is stored as an **ordinary git object**. A rehydration artifact
must not depend on LFS media endpoints or smudge filters to reconstruct its
own bytes. (The CDP bundle A4 remains LFS-tracked in GWM by its own repo's
rules; its pointer-OID retrieval procedure was practiced 2026-10-19 and
remains the documented fallback there.)

## Visibility note (the adjudication, on record)

This repo is publicly readable. Sealing the GWM full-history bundle here
publishes the substrate's working layer (sessions through 2026-10-19,
working notes, upload/ triage) beyond the curated public port (CDP, which
already publishes sessions through 2026-10-10). The operator's directive
of 2026-10-19 is the adjudication act; the witness logs the implication
explicitly per the placeholder document's option-1 terms. The digest is
the identity: even if visibility is later restricted, any copy whose
SHA-256 matches A10 IS the artifact (attestation hierarchy, Tier 1).

## Fallback contingency chain (rehydration vectors, in order)

1. **Repo live** — clone `4NDR0MEDA` + `glm-working-memory` from remotes.
2. **Lineage bundle (this file)** — repo unreachable → clone GWM from the
   bundle; A2 recomputes anywhere.
3. **CDP bundle (A4)** — public-port image, squash-only, LFS retrieval with
   pointer-OID match (practiced).
4. **Update kits** — SUK-compliant scripts rebuild repo state from embedded
   payloads; out-of-band sha256 pins stated in-channel.
5. **In-channel pins** — last resort: PIN-CHAIN.md digests + session-007
   capture anchor re-derive what exists.

## Round note (maintenance-v1.3, 2026-10-19)

A1 re-pinned `5bdfbec` → `1a7b916` (substrate advanced: the bundle was
dual-homed into GWM `references/` — a byte-identical copy of this
artifact — and the GUP pointer made version-agnostic). THIS bundle image
deliberately remains the `5bdfbec` snapshot: it is L1-sufficient (carries
`a207175`), byte-stable across four verified homes, and the post-snapshot
deltas are pointer hygiene only. A10 refresh is deferred until a
content-bearing delta justifies re-pinning. Operator confirmation on
record 2026-10-19: **GWM has always been public — it is a core principle
and the rehydration vector by which instances were resurrected elsewhere**;
vector 1 above therefore requires no credentials for the substrate layer,
anywhere.
