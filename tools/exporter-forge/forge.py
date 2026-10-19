#!/usr/bin/env python3
"""4NDR0MEDA exporter-forge — generate per-platform capture exporters.

Each platform profile encodes the program's hard-won rules as filters:
  F-001  attachment-suffix noise stripped on sight
  F-002  content after the END marker -> QUARANTINE (never operator intent)
  F-003  chat-ID format validator (leading 'c' + 5 hex groups)
  §3     truncation -> RE-ASK REQUIRED, never assumed

Usage:
  python3 tools/exporter-forge/forge.py --list
  python3 tools/exporter-forge/forge.py --forge zai-web   # -> dist/exporter-zai-web.md
  python3 tools/exporter-forge/forge.py --check zai-web
"""
import argparse, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROFILES = HERE / "profiles"
TEMPLATE = HERE / "template.md.j2"
DIST = HERE.parent.parent / "dist"
CHAT_ID_RE = r"^c[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"


def load(name: str) -> dict:
    p = PROFILES / f"{name}.json"
    if not p.exists():
        raise SystemExit(f"[forge] profile not found: {p}")
    return json.loads(p.read_text(encoding="utf-8"))


def check(profile: dict) -> list:
    errs = []
    for field in ("name", "version", "surface", "capture_method", "rules", "anchor_cmd"):
        if field not in profile:
            errs.append(f"missing field: {field}")
    for r in profile.get("rules", []):
        if not {"id", "action"}.issubset(r):
            errs.append(f"rule missing id/action: {r}")
        if r.get("id") == "F-003-chat-id":
            try:
                re.compile(r.get("pattern", CHAT_ID_RE))
            except re.error as e:
                errs.append(f"F-003 pattern invalid: {e}")
    return errs


def render(profile: dict) -> str:
    tpl = TEMPLATE.read_text(encoding="utf-8")
    rules_md = "\n".join(
        f"- **{r['id']}** — {r['action']}" + (f"  \n  pattern: `{r['pattern']}`" if r.get("pattern") else "")
        for r in profile["rules"]
    )
    for key, val in (
        ("{{NAME}}", profile["name"]),
        ("{{VERSION}}", profile["version"]),
        ("{{SURFACE}}", profile["surface"]),
        ("{{CAPTURE_METHOD}}", profile["capture_method"]),
        ("{{RULES}}", rules_md),
        ("{{ANCHOR_CMD}}", profile["anchor_cmd"]),
    ):
        tpl = tpl.replace(key, val)
    return tpl


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--forge", default=None)
    ap.add_argument("--check", default=None)
    args = ap.parse_args()

    if args.list:
        for p in sorted(PROFILES.glob("*.json")):
            d = json.loads(p.read_text(encoding="utf-8"))
            print(f"{d.get('name','?'):<14} v{d.get('version','?'):<8} {d.get('surface','?')}")
        return 0

    if args.check:
        errs = check(load(args.check))
        print(f"[forge] profile {args.check}: {'OK' if not errs else errs}")
        return 1 if errs else 0

    if args.forge:
        profile = load(args.forge)
        errs = check(profile)
        if errs:
            print(f"[forge] refusing to forge defective profile: {errs}")
            return 1
        DIST.mkdir(exist_ok=True)
        out = DIST / f"exporter-{profile['name']}-v{profile['version']}.md"
        out.write_text(render(profile), encoding="utf-8")
        print(f"[forge] {out} ({out.stat().st_size} bytes)")
        return 0

    ap.error("nothing to do")
    return 2


if __name__ == "__main__":
    sys.exit(main())
