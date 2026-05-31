# <Class Name>

> Season: <N> · Patch: <X.Y.Z> · Last refreshed: <YYYY-MM-DD> · Coaching synthesis over d4-mcp graph data

> **Loadout = live data.** Gear (with variants), aspects, paragon boards, charms/seal, glyphs, and effect text are NOT listed in this file — they come from the knowledge graph at runtime via `graph_build("<slug>")` + `lookup_*`. This file is coaching judgment only: identity, scaling logic, how-to-play, priorities. Never write a specific item/aspect/board/number here as authoritative — it will drift. If you're tempted to, put the logic instead ("match the multiplier bucket to the build's core skill") and let the graph supply the names.

## Core identity
<1-2 sentences: what this class is, its resource, its signature mechanic>

## Damage scaling buckets
- **Multiplicative sources:** <key passives + the *kinds* of aspects/uniques that multiply — by category, not by name>
- **Additive sources:** <attributes, skill-damage tempers, additive paragon>
- **Critical / Vulnerable / Overpower hooks:** <what feeds each>

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|
<!-- Skills are stable class identity (and the graph also serves them). Naming
     skills + their mechanical role is fine; do NOT add gear/aspect columns. -->

## Key passives / class mechanic
<the choices and when each wins — rationale, not a loadout>

## Aspect & unique selection logic
<HOW to choose, by bucket — not which ones. e.g. "a repeated-hit core wants
multi-hit amps; a transformation build wants on-transform amps." Defer the
actual names to `graph_build` / `lookup_aspect`.>

## Stat priority (prose)
<offensive attribute, defensive targets, in words — no exact-number tables;
point to references/stat-priorities.md for caps>

## Paragon & glyph logic
<the principle — rush the build's primary attribute, socket the dominant-bucket
glyph first, survival glyphs lag. Exact boards/nodes/glyph order come from the graph.>

## Mercenary pairing
- Hire: <role rationale>
- Reinforce: <role rationale>

## Common mistakes
- <class-specific traps>
