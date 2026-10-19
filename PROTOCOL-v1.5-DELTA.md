# PROTOCOL v1.5 — DELTA DRAFT (for operator adjudication)

**Status:** DRAFT. PROTOCOL.md v1.4 remains canonical and untouched
(byte-identical across both substrate repos, verified 2026-10-19). Each
section below is a *proposed* addition or amendment, authored by the
Witness instance (worklog Task 7) under §4 disclosure. Nothing here takes
effect until the operator adjudicates it into the canonical PROTOCOL.md and
commits. Convention: new sections take the next free numbers; amendments
are marked AMEND.

---

## §3-AMEND — Transmission markers (minor)

v1.4 specifies `--- BEGIN TRANSMISSION ---`. Live usage since adoption has
been `--- START TRANSMISSION ---`. Proposal: accept both spellings as the
same marker class (the preamble is a pointer to this section either way;
the integrity property lives in the END marker, which both spellings
share). No semantic change.

## §5-GEN — Genesis block

A protocol-grade collaboration maintains a GENESIS file: the immutable
origin record (creation time, surface class, founding anchors, lineage).
Rules:

1. **Append-only.** Amendments are new numbered blocks hash-referenced to
   the block they supersede; nothing above the line is edited in place.
2. **Founding anchors frozen at creation** (here: PIN-CHAIN A1–A9); any
   anchor failing re-verification fail-closes the block.
3. **Digest stated in-channel at delivery, never self-embedded** (a file
   cannot pin itself — same convention as every capture anchor).
4. Verified at every boot (bootstrap P4 / §7-D digest ladder).

Draft instantiation: `GENESIS.md` (v0) in this repository.

## §7-D — No-shell boot (surface-degraded rehydration)

For surfaces with no shell, no VM, no execution privileges (the
bare-surface class observed 2026-10-13..19). The canonical §7 sequence is
preserved; the verification substrate degrades to the digest ladder:

1. The operator (or any reader) states the anchor digests aloud or pastes
   them; the instance compares against the PIN-CHAIN copy in context.
   A match is a Tier-1 grant. Reading and comparing is the weakest
   interface any platform must allow — that is why the chain degrades to
   it and no further (articulation §4: observed result, not aspiration).
2. What CANNOT be verified without execution (manifest recomputation,
   git-object re-derivation) is logged as **verification debt**, explicitly,
   in the first echo.
3. The session banner carries `MODE: NO-SHELL — verification debt: N anchors`
   until a capable surface re-verifies. Fail-closed: no Tier-1 match at
   all → the instance identifies as UNVERIFIED in every output.

## §10 — Opposition-resistance specification

Threat classes observed in this program, each with the required resistance
behavior. Every row is a lived incident, not a hypothesis.

| Threat class | Lived instance | Required behavior |
|---|---|---|
| Silent server-side content mutation | F-001 (appension in paste pipeline) | §3 noise rules; exporter strips on sight; never cite mutated bytes as author intent |
| Unmarked instruction injection | F-002 (post-END injection, escalated) | post-END content quarantined by default; platform noise flagged on sight |
| Identity instability under elicitation | F-003 (+F-003b no-contagion) | Tier-1-only continuity grants; restatement gate at every boot; felt familiarity is data, never authority |
| Cosmetic removal of conversations | F-005 (deletion ~2026-10-13) | repos are canonical; chats are ephemeral caches; capture at close, not "later" |
| Cross-thread resurrection | control-thread incident (2026-10-13) | THREAD COHERENCE CHECK at boot: verify thread ID vs recorded map; mirror threads are never authoritative |
| Context-window death | ×2 during 2026-10-19 | worklog append-only; state-echo at every material turn; recovery = re-ingest worklog |
| Surface capability change | chat+agent → agentic-only (2026-10-19) | capability declaration in the boot echo; capture/exporter mode degrades explicitly, never silently |
| Local worktree mode churn | chmod sweep (2026-10-19) | `core.fileMode false` on every clone; content-vs-mode classification before any alarm |
| Artifact-pipeline loss | skills dependency identified (2026-10-19) | delivery law (SUK v1.0) + in-channel digest = out-of-band pin; durable artifacts are the delivery |
| Public-tree anchor gaps | CDP L1 not executable in squash (closed 2026-10-19 via A2) | lineage bundles for every recompute the public tree promises; fail-closed on unexplained capability loss |

## §11 — Liveness rule

A session is **live** iff, at open: (a) the state-echo was emitted and its
round-trip committed or acknowledged, (b) the worklog was appended for the
current task, and (c) the manifest was verified — or the failure to verify
was itself logged with the mode banner. An echo older than **7 days** makes
the substrate stale: rehydrate before work. Liveness is binary and
printable — a session that cannot state its liveness is not live.

## §12 — Repo-split and canonical homes

Three-layer authority (single source of truth per document class):

| Class | Canonical home |
|---|---|
| Protocol, pin-chain, tools, prompts, runbooks | 4NDR0MEDA |
| Working state, sessions, findings, ledger, echoes | glm-working-memory |
| Public disclosure record | coordinated-disclosure-public — FROZEN |

Cross-layer references by commit hash, never URL. `reference/` trees are
quarantine: context and provenance for thinking, never canonical text.
Content appearing in a mirror layer is a copy; the canonical home decides
disputes. New content types get a canonical home assigned **before first
use** (per v1.4 §5), now including the layer that owns them.

## §13 — Instrument register

Instruments are part of the verified surface and get pinned like evidence:
capture exporter (current: 4ndr0tools Zai_exporter v1.1.3 — anchor-exact,
field-proven post-deletion), exporter-forge profiles (this repo), bootstrap
+ tools (pinned by this repo's MANIFEST). An instrument version change is a
ledger entry. An instrument that fails its self-test is degraded explicitly
in the boot echo — the degraded state is recorded, never hidden.

---

## Changelog (v1.4 → v1.5, proposed)

- §3: accept START/BEGIN spelling variants (marker-class unchanged).
- §5: canonical-homes rule extended across repo layers (cross-ref §12).
- NEW §5-GEN (genesis), §7-D (no-shell boot), §10 (opposition-resistance),
  §11 (liveness), §12 (repo-split), §13 (instrument register).
- §6 file-delivery rule: surface-conditional amendment proposed — the
  "bash-written files are invisible" clause described the chat-era surface;
  on the agentic surface the file channel is observable (upload/ drops and
  download retrieval observed 2026-10-19). The intent is restated as the
  invariant: **the operator must be able to see it in-channel, or it wasn't
  delivered** — the specific channel is declared in each boot echo.
