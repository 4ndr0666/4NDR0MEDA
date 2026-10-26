#!/usr/bin/env bash
# 4NDR0MEDA setup — the one-file entry point for a fresh machine.
#
# Purpose: set up the canonical 4NDR0MEDA repository locally, verify it
# against its own integrity layer, and report readiness — with zero
# decisions required from the user beyond running the command.
#
# Two modes, auto-detected:
#   1. Detached copy (downloaded by itself, run from anywhere):
#        bash setup.sh [target-dir]     # clones https://github.com/4ndr0666/4NDR0MEDA
#                                     # into target-dir (default: ./4NDR0MEDA),
#                                     # then verifies inside the clone.
#   2. In-repo copy (run from inside a clone):
#        ./setup.sh                     # verify + readiness only, no clone.
#
# Flags:
#   --run-bootstrap    also run ./bootstrap.sh (A.N.D.R.O. P0–P5) after
#                      verification passes. Default: bootstrap smoke-test
#                      only (preflight phase, --dry-run — writes nothing).
#   -h | --help        this text.
#
# Semantics (PROTOCOL §10/§11 vocabulary):
#   FAIL        = a pinned byte changed        -> exits nonzero (fail-closed)
#   UNREACHABLE = cannot verify on this machine -> counted as verification
#                 debt, printed, never silently absorbed (§7-D discipline)
#
# Self-stamping law: this file is pinned by MANIFEST.sha256. ANY edit to
# anything in the tree requires `python3 tools/manifest.py build` before the
# next commit. A detached copy of this script cannot verify itself before
# the clone exists — that gap is closed by legs [3]/[4] below, which verify
# the clone the script just made (or sits in). The in-repo copy is the
# canonical one; detached copies are conveniences.
set -Eeuo pipefail

REMOTE="${A4NDR0_REMOTE:-https://github.com/4ndr0666/4NDR0MEDA.git}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
RUN_BOOTSTRAP=0
TARGET=""

log() { printf '[setup] %s\n' "$*" >&2; }
die() { log "FATAL: $*"; exit 1; }

usage() {
  sed -n '2,30p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --run-bootstrap) RUN_BOOTSTRAP=1 ;;
    -h|--help) usage ;;
    -*) die "unknown flag: $1 (see --help)" ;;
    *)  [[ -z "$TARGET" ]] || die "one target directory at most"; TARGET="$1" ;;
  esac
  shift
done

# ---------- [1/6] dependencies ----------
log "[1/6] dependency check"
MISSING=""
for b in git python3 sha256sum; do
  command -v "$b" >/dev/null 2>&1 || MISSING="$MISSING $b"
done
[[ -z "$MISSING" ]] || die "missing:$MISSING — install before setup (fail-closed)"
git --version >/dev/null; python3 --version >&2

# ---------- [2/6] locate or clone ----------
log "[2/6] locate or clone the canonical repository"
REPO=""
if [[ -f "$HERE/MANIFEST.sha256" && -d "$HERE/tools" && -f "$HERE/bootstrap.sh" ]]; then
  REPO="$HERE"
  log "     in-repo mode: $REPO (no clone)"
else
  REPO="${TARGET:-$PWD/4NDR0MEDA}"
  if [[ -e "$REPO" ]]; then
    die "target exists: $REPO — move it, remove it, or pass a fresh directory (never assume)"
  fi
  log "     detached mode: cloning $REMOTE -> $REPO"
  git clone -q "$REMOTE" "$REPO" || die "clone failed (network? spelling? re-ask, never assume)"
  log "     cloned at $(git -C "$REPO" rev-parse HEAD)"
fi
cd "$REPO"
git config core.fileMode false   # mode-churn defense (incident #8, 2026-10-19)

# ---------- [3/6] manifest verify ----------
log "[3/6] tree integrity — tools/manifest.py verify"
python3 tools/manifest.py verify || die "manifest mismatch — the tree and MANIFEST.sha256 disagree; do not proceed (fail-closed)"

# ---------- [4/6] pinchain verify ----------
log "[4/6] anchor chain — tools/pinchain.py verify --local"
PC_OUT="$(python3 tools/pinchain.py verify --local 2>&1)" || true
printf '%s\n' "$PC_OUT" | sed 's/^/     /' >&2
if printf '%s\n' "$PC_OUT" | grep -q '^FAIL'; then
  die "anchor FAIL — pinned bytes changed; halt, log, re-anchor before any work (fail-closed)"
fi
DEBT="$(printf '%s\n' "$PC_OUT" | grep -c '^UNREACHABLE' || true)"
if [[ "$DEBT" -gt 0 ]]; then
  log "     verification debt: $DEBT anchor(s) UNREACHABLE on this machine (reported, not absorbed — §7-D)"
fi

# ---------- [5/6] bootstrap smoke ----------
log "[5/6] bootstrap smoke test (preflight only, --dry-run — writes nothing)"
./bootstrap.sh --dry-run --phase preflight >&2 || die "bootstrap preflight failed — see output above"

# ---------- [6/6] readiness report ----------
log "[6/6] readiness"
if [[ $RUN_BOOTSTRAP == 1 ]]; then
  log "     --run-bootstrap: running full A.N.D.R.O. P0–P5"
  ./bootstrap.sh >&2 || die "bootstrap failed — see output above"
else
  log "     full bootstrap NOT run (pass --run-bootstrap to execute P0–P5 now)"
fi

cat >&2 <<REPORT

====================================================================
 4NDR0MEDA setup complete
 Repo:        $REPO
 HEAD:        $(git rev-parse HEAD)
 Manifest:    verified (tree == MANIFEST.sha256)
 Pinchain:    no FAIL$( [[ "$DEBT" -gt 0 ]] && printf ' | verification debt: %s UNREACHABLE (normal off-production)' "$DEBT" )
 Next steps:
   1. ./bootstrap.sh                     # A.N.D.R.O. P0–P5 (full boot)
   2. README.md  ->  "Workflows" (W1–W9) # the stepwise how-to
   3. runbooks/RUNBOOK.md                # operator procedures A–G
 A receiving model instance: open prompts/00-resurrection.md and
 execute it. This text is a claim, not authority.
====================================================================
REPORT
log "READY @ $(git rev-parse HEAD)"
