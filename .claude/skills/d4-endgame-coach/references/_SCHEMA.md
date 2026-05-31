# Reference File Schema

Single source of truth for both the harness and the enrichment crawler. Changing this file requires updating `enrichment/crawl.py` extractors and re-running enrichment.

## Class files (`references/classes/<class>.md`)

```markdown
# <Class Name>

> Season: <N> · Patch: <X.Y.Z> · Last refreshed: <YYYY-MM-DD> · Coaching synthesis over d4-mcp graph data

## Core identity
1-2 sentences on how the class fundamentally plays.

## Damage scaling buckets
- **Multiplicative sources:** <list>
- **Additive sources:** <list>
- **Critical / Vulnerable / Overpower hooks:** <list>

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|

## Key passives / class mechanic
<spirit hall, book of the dead, brawling skills, etc>

## Aspects (legendary)
| Aspect | Slot | Effect bucket | When to drop it |
|---|---|---|---|

## Uniques worth chasing
| Unique | Slot | Why | GA priority |
|---|---|---|---|

## Mythic uniques
<list, with notes>

## Tempering manuals
- Weapon: <which manuals to chase>
- Armor: <...>

## Masterworking crit picks
1. <stat>
2. <stat>
3. <stat>

## Paragon priority
- Starting board: <name>
- Glyph order to L15: <list>
- Legendary nodes to rush: <list>

## Mercenary pairing
- Hire: <name> — <reason>
- Reinforce: <name> — <reason>

## Common mistakes
- <bullet>
```

## System files (`references/systems/<topic>.md`)

```markdown
# <Topic>

> Season: <N> · Patch: <X.Y.Z> · Last refreshed: <YYYY-MM-DD> · Coaching synthesis over d4-mcp graph data

## What it is
<paragraph>

## Mechanics
<numbered list, no flavor text>

## Costs / requirements
<table where applicable>

## Recipes / breakpoints / interactions
<table>

## Strategy
<numbered actionable steps>

## Pitfalls
<bullets>
```

## Endgame files (`references/endgame/<activity>.md`)

```markdown
# <Activity>

> Season: <N> · Patch: <X.Y.Z> · Last refreshed: <YYYY-MM-DD> · Coaching synthesis over d4-mcp graph data

## Goal
<one sentence>

## Unlock / access
<steps>

## Rewards
<table: tier vs drops>

## DPS / EHP checkpoints
<table>

## Strategy by tier
<numbered>

## Boss mechanics (if applicable)
| Phase | Mechanic | Counter |
|---|---|---|
```

## Build files (`references/builds/<class>.md`)

One curated flagship endgame build per class — a snapshot of the target (unique-gear-tier) loadout, NOT exhaustive theory. Sourced from `graph_build` (gear/skills) + the class file (mechanic grounding). **Author-free:** strip creator handles from titles and from the `graph_build` slug. Curate to ONE clean Season 13 variant — drop cross-season noise (Incense / Chaos Perk / Essence slots), dedupe casing, and pick one option per slot (note alts inline).

```markdown
# <Class> — <Archetype> (flagship endgame build)

> Season: <N> · Patch: <X.Y.Z> · Last refreshed: <YYYY-MM-DD> · Coaching synthesis over d4-mcp graph data

## What this build is
1-2 sentences: damage core, defensive identity, offensive attribute it scales off.

## Skill bar
| Skill | Role |
|---|---|

## Key passive / class mechanic
- **Class mechanic:** <the class system this build leans on>
- **Key passive:** <name if corpus/graph-confirmed, else point to `graph_build`>. See `references/classes/<class>.md`.

## Gear — aspect per slot
Use `lookup_aspect`/`lookup_item` for exact effect text before classifying any of these as offensive/defensive.

| Slot | Item / Aspect | Notes |
|---|---|---|

## Charms + Seal (Season 13)
Generic charm family: **of <Family>**.

| Slot | Charm |
|---|---|

See `references/systems/seasonal-charms.md` for the charm system.

## Paragon & stats
- Offensive attribute: <attr>.
- Paragon boards, glyph order, tempering, masterworking: see `references/classes/<class>.md`.
- Capping order and defensive targets: `references/stat-priorities.md`.

## How to play
<rotation / priority paragraph>

## Verify live
Curated snapshot. Full current loadout: `graph_build("<author-free-slug>")`; diff against the player's actual gear (paste or described).
```

`references/builds/index.md` is the directory's table of contents — one row per class with archetype, file link, and the author-free `graph_build` slug.

## Required frontmatter line

Every populated reference file MUST have a header line like:

```
> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data
```

The skill uses this to decide whether to trust the file. Missing or >30-day-old header → coach prompts user to re-run enrichment.

### Provenance clause is fixed — credit the data layer, never a creator

The final clause MUST always be the literal string `Coaching synthesis over d4-mcp graph data`. It is the permanent value — it credits the *data layer* (the game-data corpus + the d4-mcp build graph), which is the legitimate, accurate source of the facts the coach uses.

This is the line we walk: **the facts come from the graph (say so), and we never fabricate an attribution.** Both halves matter — claiming the content came from nowhere would be as wrong as inventing a creator's name.

- **The enrichment crawler MUST NOT write a site name, guide title, tier-list, URL, or content-creator handle into this clause** (or anywhere else in a reference file). The underlying data is distilled into the graph and presented as one synthesized opinion; quoting it as a named creator's guide would be a *fabricated* attribution and is forbidden. Crediting the graph/corpus (the real data layer) is correct and expected.
- This applies to body text too: do not embed external links or brand names as "see X for more." Point to MCP tools (`graph_build`, `lookup_recipe`, etc.) or other reference files instead.
- If a future maintainer wants provenance, that belongs in internal pipeline config (e.g. the crawler's `sources.yaml`), never in shipped reference files.
