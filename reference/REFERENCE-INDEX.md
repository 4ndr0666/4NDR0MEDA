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

\* staged copy size; the canonical articulation lives with the operator and in the substrate's download staging — the digest is the identity, the location is not.

## Staging note

R1–R4 staged copies live in the workspace `download/` directory with
digests verified 2026-10-19. The digest is the identity; any copy whose
sha256 matches IS the artifact (attestation hierarchy, Tier 1).

## Lineage bundle slot

`PLACEHOLDER-LINEAGE-BUNDLE.md` (this directory) reserves the slot for the
GWM full-history bundle — the artifact that makes PIN-CHAIN A2 executable
on any machine. Pending operator visibility adjudication.
