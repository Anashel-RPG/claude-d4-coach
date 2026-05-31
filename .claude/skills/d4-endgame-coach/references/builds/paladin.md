# Paladin — Arbiter Hammerdin (flagship endgame build)

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## What this build is
The defining Season 13 Paladin: a Holy melee/aura bruiser that spams **Blessed Hammer** while standing in **Consecration**, runs two auras for permanent buffs, and transforms with **Arbiter of Justice** for burst windows. Tanky front line, high sustained Holy damage. Scales off Strength → Armor → its key passive.

## Skill bar
| Skill | Role |
|---|---|
| Blessed Hammer | Core spender — primary damage (enhancements: cast speed, damage bonus, Disciple's Halo) |
| Consecration | Ground DoT + Fortify + Weaken (Hallowed Ground enhancement) |
| Defiance Aura | Toggle aura — max life / healing (Rite of Prayer) |
| Fanaticism Aura | Toggle aura — resource generation / max resource (Rite of Vengeance) |
| Falling Star | Mobility + burst (extra charge, cooldown, Starfall) |
| Rally | Buff/utility — crit chance, cost reduction (Words of Rejuvenation) |
| Arbiter of Justice | Ultimate / transformation — burst window (Seraph's Wings, Wing Strike recast) |

## Key passive / class mechanic
- **Key passive:** Coat of Arms (Armor + Block → damage) for the Hammerdin/aura bruiser. Only one key passive can be equipped.
- **Class mechanic:** Auras (Defiance + Fanaticism run together here, each toggled with its Rite upgrade) + the Arbiter transformation ultimate.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("arbiter-hammerdin")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Stat priority (prose)
Strength is the primary offensive attribute — it feeds both skill damage and Armor, which means it doubles as a defensive stat under Coat of Arms. Stack it first. After Strength, prioritize Armor and Block Chance to maximize the Coat of Arms multiplier, then fill in resistances and Max Life to meet survivability thresholds. For exact capping targets, see `references/stat-priorities.md`.

## How to play
Keep both auras on, drop Consecration and stand in it, spam Blessed Hammer, use Falling Star to reposition and burst, pop Arbiter of Justice on Elites/bosses and maintain its uptime through transitions. Rally for the crit/utility window.

## Verify live
This is a curated snapshot. For the full current loadout (including paragon nodes and glyphs) call `graph_build("arbiter-hammerdin")`; diff against the player's actual gear (ask them to paste or describe it).
