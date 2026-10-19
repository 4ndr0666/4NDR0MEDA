# PROMPT 03 — HANDOFF (session close sequence)

Implements PROTOCOL §5.1 (canonical close sequence) plus the 4NDR0MEDA
additions (echo, worklog, instruments). The agent drafts; the operator
executes the commands and is the committer of record — unless the agent
environment holds credentials, in which case steps 4–6 may execute under
operator approval. The human's hands remain the last writer wherever the
agent lacks credentials.

## Sequence

1. **Archive.** The session transcript is captured into `sessions/` with
   the session-header template fully filled (lived incident: session-007
   shipped with two unfilled placeholders). Use the exporter; compute and
   embed the capture-side anchor; spell-check the filename BEFORE commit —
   the manifest pins filenames, typos survive forever.
2. **State.** Rewrite `working-notes/PROJECT_STATE.md` in full. Never
   append. Agent drafts; operator approves.
3. **Ledger.** Append the session's decisions to
   `working-notes/decisions-ledger.md` (DECISION / RATIONALE /
   ALTERNATIVES REJECTED), and the worklog entry to the agent worklog.
4. **Hash manifest.** `sha256sum sessions/*.md > sessions/MANIFEST.sha256`
   (glob excludes the manifest itself by design).
5. **Verify before committing.** `sha256sum -c sessions/MANIFEST.sha256` —
   mandatory, not decorative: a manifest of a truncated file certifies
   corruption.
6. **Single atomic commit.** Archive + manifest + state together: no point
   in history contains an unpinned archive.
7. **Echo.** Emit the state-echo; operator commits it to
   `working-notes/`. This is the liveness heartbeat (v1.5 draft §11).
8. **Instruments.** Note exporter/tool versions used, with digests if
   changed (v1.5 draft §13). Note any rule that fired during capture.
9. **Clocks.** State any live deadlines on record (disclosure windows,
   follow-up dates) so the next boot inherits them.
10. **Push.** The operator's push is canon. The final line of every close
    is the push, and it belongs to the operator alone.

## Never

- Never close without the echo — an unclosed session is an unwitnessed one.
- Never rewrite a closed session archive; corrections are new sessions.
- Never leave the tree dirty across a close ("I'll commit tomorrow" is how
  unpinned archives die).
