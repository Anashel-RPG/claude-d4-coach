# d4-mcp — the coaching data service

`d4-mcp` is the live data backend for this coach. It exposes Diablo IV game data, a community knowledge graph, and deterministic calculators over a single MCP endpoint.

**Live URL:** `https://mcp-d4.anashel.com/mcp`

## Free public service

This MCP is **free to use** — no account, no signup, nothing to pay for. It's hosted by the project maintainer and costs almost nothing to run, so it's offered openly to anyone using this coach.

- **Zero setup.** This repo ships an `.mcp.json` that already includes a public access key, so a fresh clone connects automatically — no OAuth click, no browser step, no key to request.
- The public key is **read-only** and reaches only public game data plus the pure-math calculators. Requests are rate-limited per client (60/min) for fair use.
- You do **not** need to self-host or configure anything. Clone the repo, open the coach, and the tools are live.

## Already wired in this repo (Claude Code)

If you're using the coach from this repository, **you don't need to do anything**. The project `.mcp.json` points at the service with the public key, so Claude Code picks it up on launch and the `d4-mcp` tools resolve immediately.

To use the same service from a *different* project, copy the `d4-mcp` block from this repo's `.mcp.json` (the URL **and** the public `X-D4-Public-Key` header) into that project's `.mcp.json`.

## Add to Claude.ai (web or desktop)

Settings → Connectors → Add custom connector → URL: `https://mcp-d4.anashel.com/mcp` → follow the auto-approve prompt and click **Allow**. (Claude.ai connectors authenticate by OAuth rather than a header; the consent is auto-approved.)

## What it serves (22 tools, three layers)

| Layer | Tools | What you get |
|---|---|---|
| **Knowledge graph** | `graph_build`, `graph_entity`, `graph_search`, `graph_stats` | Build dependencies, gear/skill/aspect relationships, and synergies across all 8 classes for the current season |
| **Corpus (game data)** | `lookup_item`, `lookup_aspect`, `lookup_power`, `lookup_affix`, `lookup_item_type`, `lookup_recipe`, `search_corpus`, `class_roster`, `affix_pool`, `d4_list_types`, `d4_schema`, `d4_sample`, `d4_query` | Exact item stats, affix roll ranges, skill/aspect effect text, value ranges |
| **Calculators** | `compute_dps`, `armor_breakpoint`, `glyph_xp_time`, `recipe_cost`, `bucket_compare` | Deterministic math: bucket-model DPS, armor breakpoints, glyph XP, recipe material totals, upgrade comparison |

## When the coach calls it

Full per-tool routing lives in `SKILL.md` ("MCP — mandatory tool usage"). The discipline in short:

- **Graph before opinion.** Before asserting "this build uses X" or "equip Y", call `graph_build`/`graph_entity` to verify against the data — never recite a loadout from memory.
- **Corpus before classification.** Before calling an aspect offensive/defensive, look up its real effect with `lookup_aspect`/`lookup_item`. Slot does not imply function.
- **Calculators for any non-trivial math.** More than 2-3 multiplier sources → `compute_dps`. Comparing two upgrades → `bucket_compare`. Don't multiply by hand.
- **Extraction trumps graph.** The gear the player shows you (pasted or described) is their ACTUAL gear; the graph is the build template. When they differ, address the difference.
- **Never fabricate.** If a lookup returns no effect text and the player hasn't shown you the item, ask to see it rather than guessing from the name.

## Presenting results

- Cite the data layer when presenting results: "the game data shows…", "the build graph lists…", "I ran the numbers and got X." Game entity data comes from d4data (open-source D4 game files); build relations come from the d4-mcp knowledge graph (publicly available Season 13 build data). Do not invent citations to specific guides, tier lists, or creators — if you don't know the source, don't name one.
- Remind the user that some season constants behind the calculators (recipe costs, armor K-values) are approximations worth verifying in-game.

## Cost

*This coach uses the free public `d4-mcp` service above — there is nothing to install, configure, or pay for beyond connecting to it.*
