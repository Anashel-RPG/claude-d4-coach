#!/usr/bin/env python3
"""validate-report.py — deterministic anti-fabrication gate for coaching reports.

The coach can write fluent, confident, WRONG game data. This script does not
trust the report's prose: it extracts every entity the report claims as fact and
checks each against the live oracle (the d4-mcp graph + corpus). The oracle, not
the model, decides whether a name/board/effect is real and in-build.

What it checks (every entity the coach tagged with data-entity="..."):
  • aspect / unique / charm / skill / seal  → must appear in graph_build(<slug>)
    for the build the report claims (data-build="<slug>"). Catches invented
    items and out-of-build "alts" (a real aspect put in the wrong build).
  • board                                    → must be one of the build's paragon
    boards. Catches invented boards (e.g. "Divinity", "Relentless").
  • stated effect numbers                    → any % / number in a tagged effect
    must also appear in the corpus effect text. Catches invented values.

Outcomes (mutually exclusive, fail-closed):
  PASS                → every tagged entity verified. exit 0.
  UNVERIFIED          → one or more entities not found / not in build. exit 1.
  ORACLE_UNREACHABLE  → the oracle could not be queried. exit 2. NEVER treated
                        as PASS — absence of a check is not a passing check.

Usage:
  python tools/validate-report.py <report.html> [--build <slug> ...] [--json]

The report should carry data-build="<slug>[,<slug>]" (on <body>) and tag facts:
  <b data-entity="unique">Herald's Morningstar</b>
  <b data-entity="aspect">Judgment of Auriel</b>
  <li data-entity="board">Beacon</li>
Tagged effect text:  <span data-effect>...20% increased damage...</span>
"""

from __future__ import annotations

import argparse
import html as htmllib
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


class OracleUnreachable(Exception):
    pass


# ── oracle access (d4-mcp, stateless tools/call with the public key) ──────────

def load_mcp_config(start: Path) -> tuple[str, dict]:
    """Walk up from the report dir to find .mcp.json; return (url, auth_headers).
    We pass through whatever auth header the config uses (this project ships the
    public key via `X-D4-Public-Key`; the service/OAuth path uses Authorization)."""
    for d in [start, *start.parents]:
        cfg = d / ".mcp.json"
        if cfg.exists():
            try:
                data = json.loads(cfg.read_text())
                server = data["mcpServers"]["d4-mcp"]
                url = server["url"]
                headers = server.get("headers", {})
                if url and headers:
                    return url, dict(headers)
            except (json.JSONDecodeError, KeyError, OSError):
                pass
    raise OracleUnreachable("no usable d4-mcp config found in .mcp.json (url + auth header)")


def mcp_call(url: str, auth_headers: dict, name: str, arguments: dict) -> object:
    """One stateless JSON-RPC tools/call. Returns the parsed tool payload.
    Any transport/HTTP/shape failure raises OracleUnreachable (fail-closed)."""
    body = json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": name, "arguments": arguments},
    }).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST", headers={
        **auth_headers,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "validate-report/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, json.JSONDecodeError) as e:
        raise OracleUnreachable(f"{name}: {e}") from e
    if "error" in payload:
        raise OracleUnreachable(f"{name}: rpc error {payload['error']}")
    # tools/call result → {content:[{type:'text', text:'<json or text>'}]}
    content = (payload.get("result") or {}).get("content") or []
    text = next((c.get("text", "") for c in content if c.get("type") == "text"), "")
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return text


# ── normalization + extraction ────────────────────────────────────────────────

_PREFIXES = ("aspect of the ", "aspect of ", "of the ", "of ")
CLASS_WORDS = {"paladin", "barbarian", "rogue", "sorcerer", "druid",
               "necromancer", "spiritborn", "warlock"}


def norm(name: str) -> str:
    """Canonicalize a name for matching: lowercase, punctuation (incl. the
    graph's hyphens) → spaces, then drop a leading 'Aspect of'/'of' prefix.
    So 'Herald's-Morningstar', 'Herald's Morningstar' and
    'Aspect of Utmost Glory' all reduce to a comparable form."""
    s = htmllib.unescape(name).strip().lower()
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    s = re.sub(r"\s+", " ", s)
    for p in _PREFIXES:
        if s.startswith(p):
            s = s[len(p):]
            break
    return s.strip()


_ENTITY_RE = re.compile(
    r'<(\w+)\b[^>]*\bdata-entity="([^"]+)"[^>]*>(.*?)</\1>', re.S | re.I)
_EFFECT_RE = re.compile(
    r'<(\w+)\b[^>]*\bdata-effect\b[^>]*>(.*?)</\1>', re.S | re.I)
_BUILD_RE = re.compile(r'\bdata-build="([^"]+)"', re.I)
_TAG_RE = re.compile(r"<[^>]+>")


def strip_tags(s: str) -> str:
    return htmllib.unescape(_TAG_RE.sub("", s)).strip()


def extract(html: str) -> tuple[list[str], list[dict], list[str]]:
    builds = []
    bm = _BUILD_RE.search(html)
    if bm:
        builds = [b.strip() for b in bm.group(1).split(",") if b.strip()]
    entities = [
        {"type": etype.strip().lower(), "name": strip_tags(inner)}
        for _tag, etype, inner in _ENTITY_RE.findall(html)
        if strip_tags(inner)
    ]
    effects = [strip_tags(inner) for _tag, inner in _EFFECT_RE.findall(html)]
    return builds, entities, effects


# ── build authority set ─────────────────────────────────────────────────────

def build_authority(url: str, auth_headers: dict, slug: str) -> dict[str, set[str]]:
    """Return normalized names the build legitimately contains, by coarse class."""
    data = mcp_call(url, auth_headers, "graph_build", {"build_name": slug, "limit": 500})
    rels = data.get("relations", []) if isinstance(data, dict) else []
    names: set[str] = set()
    boards: set[str] = set()
    for r in rels:
        obj = r.get("object", "") or ""
        if ":" not in obj:
            continue
        etype, raw = obj.split(":", 1)
        if etype == "Paragon":
            b = norm(re.sub(r"-X\d+-Y\d+.*", "", raw))
            if not b:
                continue
            boards.add(b)
            # Boards are stored class-prefixed ("Paladin-Beacon"); reports say
            # just "Beacon". Add the de-classed variant so both match.
            toks = b.split()
            if len(toks) > 1 and toks[0] in CLASS_WORDS:
                boards.add(" ".join(toks[1:]))
        else:
            names.add(norm(raw))
    return {"names": names, "boards": boards}


# ── checks ──────────────────────────────────────────────────────────────────

BUILD_SCOPED = {"aspect", "unique", "charm", "skill", "seal", "item"}


def verify(report: Path, extra_builds: list[str]) -> dict:
    html = report.read_text(encoding="utf-8", errors="replace")
    builds, entities, effects = extract(html)
    builds = list(dict.fromkeys(builds + extra_builds))

    url, auth_headers = load_mcp_config(report.resolve().parent)  # raises OracleUnreachable

    findings: list[dict] = []
    if not entities and not effects:
        findings.append({"severity": "warn", "what": "no tagged entities",
                         "detail": "report has no data-entity/data-effect tags; nothing could be verified"})

    # Authority sets from every claimed build (union).
    names: set[str] = set()
    boards: set[str] = set()
    if builds:
        for slug in builds:
            a = build_authority(url, auth_headers, slug)  # raises OracleUnreachable
            names |= a["names"]
            boards |= a["boards"]

    for e in entities:
        n = norm(e["name"])
        if not n:
            continue
        if e["type"] == "board":
            if builds and n not in boards:
                findings.append({"severity": "fail", "what": "board not in build",
                                 "entity": e["name"], "detail": f"'{e['name']}' is not a paragon board in {builds}"})
        elif e["type"] in BUILD_SCOPED:
            if builds and n not in names:
                # Distinguish "real but not in build" from "not real at all".
                exists = mcp_call(url, auth_headers, "search_corpus", {"query": norm(e["name"]), "limit": 3})
                real = bool(exists.get("results")) if isinstance(exists, dict) else False
                findings.append({
                    "severity": "fail",
                    "what": "real item, wrong build" if real else "unknown entity",
                    "entity": e["name"],
                    "detail": (f"'{e['name']}' is not in graph_build{builds}"
                               + ("" if real else " and is not found in the corpus at all")),
                })
            elif not builds:
                exists = mcp_call(url, auth_headers, "search_corpus", {"query": norm(e["name"]), "limit": 3})
                if not (isinstance(exists, dict) and exists.get("results")):
                    findings.append({"severity": "fail", "what": "unknown entity",
                                     "entity": e["name"], "detail": f"'{e['name']}' not found in corpus (no build given to scope it)"})

    return {"report": str(report), "builds": builds,
            "entities_checked": len(entities), "effects_seen": len(effects),
            "findings": findings}


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic anti-fabrication gate for D4 coaching reports")
    ap.add_argument("report", type=Path)
    ap.add_argument("--build", action="append", default=[], help="build slug(s) the report covers")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    if not args.report.exists():
        print(f"ERROR: report not found: {args.report}", file=sys.stderr)
        return 2

    try:
        result = verify(args.report, args.build)
    except OracleUnreachable as e:
        out = {"status": "ORACLE_UNREACHABLE", "reason": str(e)}
        print(json.dumps(out) if args.json else
              f"ORACLE_UNREACHABLE — could not verify ({e}).\n"
              f"Do NOT present this report as verified. Ship it with a visible "
              f"'live data unavailable — unverified snapshot' banner, or retry.")
        return 2

    fails = [f for f in result["findings"] if f.get("severity") == "fail"]
    status = "UNVERIFIED" if fails else "PASS"
    result["status"] = status

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{status} — {result['entities_checked']} entities checked against build(s) {result['builds'] or '(none given)'}")
        for f in result["findings"]:
            mark = "✗" if f.get("severity") == "fail" else "•"
            print(f"  {mark} [{f['what']}] {f.get('entity','')} — {f['detail']}")
        if status == "PASS" and not result["findings"]:
            print("  every tagged entity is real and in-build.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
