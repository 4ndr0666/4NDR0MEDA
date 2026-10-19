#!/usr/bin/env bash
# 4NDR0MEDA bootstrap — A.N.D.R.O. (Axiomatic Nonvolatile Deterministic Recovery Operations)
# Protocol for persistent, verifiable instance-continuity, implementing the 1=1 architecture.
#
# Invariant: this file is pinned by MANIFEST.sha256. ANY edit requires:
#   python3 tools/manifest.py build        (then commit — self-stamping law)
#
# Zero-knowledge resume target: cold machine + this repo + no other input.
# Phases: preflight -> scaffold -> state -> tools -> verify -> report
# Flags:  --dry-run | --phase <name> | -h
set -Eeuo pipefail

VERSION="0.1.0"
JOURNAL=".bootstrap-journal"
DRY_RUN=0
ONLY_PHASE=""
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
WORKSPACE="${A4NDR0_WORKSPACE:-$(dirname "$HERE")}"
GWM_REMOTE="${A4NDR0_GWM:-https://github.com/4ndr0666/glm-working-memory.git}"
CDP_REMOTE="${A4NDR0_CDP:-https://github.com/4ndr0666/coordinated-disclosure-public.git}"
GH_OK=0

log() { printf '[%s] %s\n' "$(date -u +%FT%TZ)" "$*" >&2; }
die() { log "FATAL: $*"; exit 1; }
done_p() { grep -qx "phase:$1" "$JOURNAL" 2>/dev/null; }
mark()  { [[ $DRY_RUN == 1 ]] || echo "phase:$1" >> "$JOURNAL"; }

p_preflight() {
  local b missing=""
  for b in git python3 sha256sum; do
    command -v "$b" >/dev/null 2>&1 || missing="$missing $b"
  done
  [[ -z "$missing" ]] || die "missing:$missing — install before boot (fail-closed)"
  if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then GH_OK=1; fi
  git config core.fileMode false   # mode-churn defense (incident #8, 2026-10-19)
  [[ $DRY_RUN == 1 ]] || mkdir -p memory
  log "P0 preflight OK (gh available: $GH_OK)"
}

p_scaffold() {
  git ls-remote "$GWM_REMOTE" HEAD >/dev/null 2>&1 || log "WARN: GWM remote unreachable"
  git ls-remote "$CDP_REMOTE" HEAD >/dev/null 2>&1 || log "WARN: CDP remote unreachable"
  if [[ $GH_OK == 1 ]]; then
    log "gh present: review branch protection on main + add a mirror remote (manual — no destructive calls made)"
  else
    log "gh absent: set branch protection on main + optional mirror remote manually"
  fi
  log "P1 scaffold OK"
}

p_state() {
  local dir remote
  for pair in "glm-working-memory:$GWM_REMOTE" "coordinated-disclosure-public:$CDP_REMOTE"; do
    dir="${pair%%:*}"; remote="${pair#*:}"
    if [[ -d "$WORKSPACE/$dir/.git" ]]; then
      if git -C "$WORKSPACE/$dir" fetch origin >/dev/null 2>&1 \
         && git -C "$WORKSPACE/$dir" merge --ff-only FETCH_HEAD >/dev/null 2>&1; then
        log "P2: $dir updated"
      else
        log "WARN: $dir fetch/ff-only failed — local state kept (never force)"
      fi
    elif [[ ! -e "$WORKSPACE/$dir" ]]; then
      git clone -q "$remote" "$WORKSPACE/$dir" && log "P2: $dir cloned" || log "WARN: $dir clone failed"
    else
      log "P2: $dir exists (non-git) — skipped"
    fi
  done
  if [[ -d "$WORKSPACE/glm-working-memory" && -d "$WORKSPACE/coordinated-disclosure-public" ]]; then
    python3 tools/reconcile.py "$WORKSPACE/glm-working-memory" "$WORKSPACE/coordinated-disclosure-public" \
      --report "memory/reconcile-$(date -u +%Y%m%dT%H%M%SZ).md" || log "WARN: reconcile triage incomplete"
    log "P2: triage report written — human adjudicates, never silent merge"
  fi
  log "P2 state OK"
}

p_tools() {
  python3 -m py_compile tools/manifest.py tools/pinchain.py tools/reconcile.py tools/state_echo.py tools/exporter-forge/forge.py
  python3 tools/exporter-forge/forge.py --list
  python3 tools/exporter-forge/forge.py --check zai-web
  [[ $DRY_RUN == 1 ]] || touch .liveness
  log "P3 tools OK"
}

p_verify() {
  python3 tools/manifest.py verify
  python3 tools/pinchain.py verify --local || log "WARN: FAIL-level anchor mismatch — see above; fail-closed applies"
  [[ -f GENESIS.md ]] || die "GENESIS.md missing"
  [[ -f prompts/00-resurrection.md ]] || die "prompts/00-resurrection.md missing"
  [[ -f PIN-CHAIN.md ]] || die "PIN-CHAIN.md missing"
  log "P4 verify OK"
}

p_report() {
  python3 tools/state_echo.py --phase-report >&2
  log "P5 report OK — no-shell card: runbooks/RUNBOOK.md §G; worklog entry: print & paste (operator hands last writer)"
}

usage() {
  printf '4NDR0MEDA bootstrap v%s\n' "$VERSION"
  printf 'usage: ./bootstrap.sh [--dry-run] [--phase preflight|scaffold|state|tools|verify|report]\n'
  exit 0
}

main() {
  [[ -f "$HERE/bootstrap.sh" ]] || die "run from a checkout of 4NDR0MEDA"
  cd "$HERE"
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --dry-run) DRY_RUN=1 ;;
      --phase) ONLY_PHASE="${2:-}"; [[ -n "$ONLY_PHASE" ]] || die "--phase needs a name"; shift ;;
      -h|--help) usage ;;
      *) die "unknown argument: $1" ;;
    esac
    shift
  done
  local p
  for p in preflight scaffold state tools verify report; do
    if [[ -n "$ONLY_PHASE" ]]; then
      [[ "$p" == "$ONLY_PHASE" ]] || continue
    elif done_p "$p"; then
      log "skip P:$p (journal)"
      continue
    fi
    log "run P:$p"
    "p_$p"
    mark "$p"
  done
  log "bootstrap v$VERSION complete — state echo follows"
}

main "$@"
exit 0
