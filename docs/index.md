# Documentation index

Everything in `docs/` is part of the repository tree and therefore rides
`MANIFEST.sha256` — the docs are self-stamped with the code they describe.
(The same self-stamping law is why these pages live in-repo rather than in a
GitHub wiki: a wiki page cannot be pinned by the manifest. A wiki mirror may
be sanctioned later at the operator's discretion; the canonical text stays
here.)

| Page | What it covers |
|---|---|
| [architecture.md](architecture.md) | The three-repo topology, the two-layers distinction (protocol vs. tensor-integrated architecture), and how the layers interlock |
| [verification.md](verification.md) | The verification grammar in brief: evidence tiers, tri-state anchors, the receipt discipline, and what a continuity claim actually asserts |

## Where to start

- **New here?** The [README](../README.md) is the comprehensive guide —
  quickstart, the per-file repository map, and workflows W1–W9.
- **Skeptic?** README [W9](../README.md#w9--zero-knowledge-verification-for-a-skeptic)
  is the zero-knowledge path: verify every claim from a bare machine.
- **Auditor?** [PIN-CHAIN.md](../PIN-CHAIN.md) is the anchor registry (A1–A13,
  each with its re-verify command); [verification.md](verification.md) is the
  grammar those anchors speak.
- **Looking for the paper?** The Phase Tensor Engine / verifiable archival
  state custody manuscript (Paper-2 v1.7) lives in the working substrate's
  write-ups and is staged for its arXiv deposit; see [architecture.md](architecture.md)
  §3 for the two-layers distinction.
