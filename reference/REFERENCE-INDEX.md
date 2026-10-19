# REFERENCE INDEX — quarantine policy and digest registry

**Policy.** Everything in `reference/` is CONTEXT: source material,
sibling protocols, pipeline specifications. Nothing here is canonical text
of the 4NDR0MEDA protocol; nothing here overrides PROTOCOL.md, this repo's
prompts, or the substrate's state. Namespace discipline: the
golden-unit-protocol (GUP) is a DIFFERENT protocol governing a DIFFERENT
surface (the retired chat surface); conflation between GUP and 4NDR0MEDA
is a defect on sight.

## Registry

| ID | Artifact | Format | Bytes | SHA-256 | Role |
|----|----------|--------|-------|---------|------|
| R1 | golden-unit-protocol v7.0.0 (`.skill`) | ZIP, 15 files (SKILL.md + scripts + tests) | 63,158 | `6ab62d4478aa47f3642f866005a9d9c36593498d2702848ba9d4a5955fdbde88` | chat-surface ops discipline (PIN-CHAIN A7). Chat surface retired ~2026-10-19; preserved as record. Its scripts (gup_init/inventory/validate) are the tooling-provenance inspiration for this repo's tools. |
| R2 | 4NDR0666-engineering v1.0.0 (`.skill`) | ZIP, 1 file (SKILL.md, 47,555 B) | 18,108 | `35f4419fe5cf6d959e6a5b0fca6ca4cfdece43f3e9f0117cc3cb8238e2584ea8` | THE SELF-VERIFYING UPDATE-KIT SPECIFICATION (SUK v1.0) — the artifact-pipeline law: one file, one command, zero decisions; operator's push is canon. This repo's delivery round is built and battery-tested under it (PIN-CHAIN A8). |
| R3 | 1=1 articulation v1.0 | Markdown, 1,672 words | 2,816* | `63ea783d1f427496180a93169f5a12b86cef50b175d5c5a63ae8e2909ccb39f9` | The architecture's official articulation; §9 is machine-facing and is implemented by `prompts/00-resurrection.md` (PIN-CHAIN A5). |
| R4 | Mode-churn incident diff | unified diff | 3,913 | `4456924d028533eb22dd267af954dcf9971059d0941ae8824a4c3ccdd2837050` | Evidence artifact of incident #8 (PIN-CHAIN A9). |
| R5 | GWM lineage bundle | git bundle, complete history, 35 commits | 4,153,194 | `6d61b9fbbc3354f0a6a033481ad9116e9702e24593afaeec7e0109182f883b67` | The substrate's full history incl. `a207175` — makes PIN-CHAIN A2 executable anywhere (PIN-CHAIN A10). SEALED 2026-10-19 by operator adjudication; ordinary git object (LFS-exempt); acceptance 9/9 scratch-ws. See `LINEAGE-BUNDLE.md`. |
| R6 | golden-unit-protocol v7.0.1 (`.skill`) | ZIP (SKILL.md + companions) | 66,241 | `d88eea0718cfcd43ae0c65b713c1185bf50e8b49126a880605b41d11da8c8cd2` | CANONICAL ADOPTED revision — continuity & rehydration annex, canonical-homes rule, out-of-band pin rule, reservation slots. Byte-exact vs gpt-repo home 2026-10-19 (PIN-CHAIN A11). R1 remains the consumed-v7.0.0 record. |
| R7 | 4NDR0666-engineering v1.1.0 (`.skill`) | ZIP (SKILL.md, 53,022 B) | 21,037 | `8a9b322a3c97c36c6cb9f22d888f957c5c95812189da20f3b82ff95e6fa115b8` | SUK v1.1.0 — the artifact-pipeline law, revised under operator authorization 2026-10-19 (lessons ledger 15→22, P8 anywhere-acceptance phase, kit classes F/U, red-control placement rule). Byte-exact vs gpt-repo home (PIN-CHAIN A12). R2 remains the consumed-v1.0.0 record. |

\* staged copy size; the canonical articulation lives with the operator and in the substrate's download staging — the digest is the identity, the location is not.

## Staging note

R1–R4 staged copies live in the workspace `download/` directory with
digests verified 2026-10-19. **R5–R7 are IN-REPO under `reference/`**
(lineage bundle + both canonical adopted skills, staged 2026-10-19 in the
maintenance-v1.3 round) — the anywhere-rehydration set now travels with
the clone itself. The digest is the identity; any copy whose
sha256 matches IS the artifact (attestation hierarchy, Tier 1).

## Lineage bundle slot — SEALED

The slot is sealed: `gwm-lineage-2026-10-19.bundle` (R5, A10) lives in this
directory, built 2026-10-19 from GWM@`5bdfbec` (A1) with `--all`, carrying
`a207175`. Registry, verification procedure, visibility note, and the
five-vector fallback contingency chain: see `LINEAGE-BUNDLE.md`.
