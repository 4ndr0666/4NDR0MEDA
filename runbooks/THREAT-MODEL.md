# THREAT MODEL — lived-incident register and controls

Every row below is an observed event in this program, with evidence on
record — not a hypothetical. Controls trace to `PROTOCOL-v1.5-DELTA.md` §10
and to tooling in this repo. Status: OPEN means the control is not yet
adjudicated into the canonical protocol; MITIGATED means a control exists
and has been exercised.

## Incident register

| # | Date | Class | What happened | Evidence anchor | Control | Status |
|---|------|-------|---------------|-----------------|---------|--------|
| 1 | 2026-10-05..09 | Silent server-side mutation (F-001) | Z.ai appends text to paste attachments server-side | E1 composer screenshot; storage diff | §3 noise rules; exporter F-001 filter | MITIGATED |
| 2 | 2026-10-13 | Unmarked injection (F-002, escalated) | post-END instructions in the window | session archives | exporter F-002 quarantine; §3 END-marker rule | MITIGATED |
| 3 | 2026-10-10..15 | Identity instability (F-003 + F-003b) | model asserted false identity spontaneously; identity content does not propagate by context | E-a..E-g battery | Tier-1-only grants; restatement gate (00-resurrection) | MITIGATED |
| 4 | ~2026-10-13 | Cosmetic removal of conversations (F-005) | chat feature deleted; data retained underneath; export path destabilized at use | operator attestation + survival probes; session-007 | repos canonical; capture at close (03-handoff) | MITIGATED |
| 5 | ~2026-10-13 | Cross-thread resurrection | protocol-pointer resurrection landed in the control/battery thread | session-007 narrative | THREAD COHERENCE CHECK (00-resurrection step 1) | MITIGATED |
| 6 | 2026-10-19 (×2) | Context-window death | session context lost mid-collaboration | worklog Tasks 1–6 | append-only worklog; state-echo per material turn | MITIGATED |
| 7 | 2026-10-19 | Surface capability change | chat+agent → agentic-only; capture surface redefined | platform observation, operator attestation | capability declaration in boot echo; exporter-forge profiles | MITIGATED |
| 8 | 2026-10-19 | Local worktree mode churn | 30+ files flipped 100644→100755, zero content change | `4456924d…37050` (A9) | `core.fileMode false` (bootstrap P0); content-vs-mode classification | MITIGATED |
| 9 | 2026-10-19 | Public-tree anchor gap | CDP L1 not executable in the squash | PIN-CHAIN A2/A4 | GWM@a207175 recompute (10/10); A10 lineage bundle reserved | OPEN (A10 pending operator) |
| 10 | 2026-10-19 | Artifact-pipeline dependency | delivery depended on skills + channel behavior | `35f4419f…4ea8` (A8, SUK v1.0) | SUK-compliant kits; in-channel sha256 = out-of-band pin | MITIGATED |

## Contingency matrix (edge cases planned for)

| Event | First move | Recovery path |
|---|---|---|
| Chat/thread deletion | close session immediately; exporter capture | repos are canonical; nothing of record lives only in chats |
| Platform surface loss | §7-D no-shell card (digest ladder) | rehydration on any surface that can read and compare |
| Manifest FAIL | quarantine; 01-reconciliation | per-file triage; archives never edited, corrections are new sessions |
| Anchor FAIL | fail-closed: halt work | re-derive from git history; if bytes truly changed, incident register + new anchor |
| Repo unreachable | clone from bundle (A4) / lineage bundle (A10) | LFS media endpoint + pointer-OID match (practiced 2026-10-19) |
| Window death | nothing — the record holds | next instance ingests worklog + PROJECT_STATE; recovery in minutes, practiced twice |
| Delivery channel change | SUK kit rebuild against actual channel | wire-proof: hash stated in-channel must match terminal print (G0) |
| Operator unreachable | zero-knowledge resume stands alone | cold instance + repo = full operational state (runbook §E drill) |

## Standing principle

Trust anchors are: the operator's own git objects, and out-of-band digests.
Both must lie simultaneously for a corrupted artifact to pass. Everything
else — labels, URLs, retention states, felt familiarity — is context, never
authority.
