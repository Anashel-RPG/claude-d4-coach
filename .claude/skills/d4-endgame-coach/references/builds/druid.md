# Druid — Pulverize (flagship endgame build)

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## What this build is
The defining Season 13 Druid: a Werebear **Pulverize** Overpower bruiser. You shapeshift into a bear and slam the ground, converting huge Willpower-scaled Overpower hits into screen-clearing shockwaves. **Grizzly Rage** is the Werebear ramp ultimate, **Earthen Bulwark** and **Cyclone Armor** keep you alive, and **Wolves** add a passive companion-damage layer. Extremely tanky front-line melee with massive burst windows. Scales off Willpower.

## Skill bar
| Skill | Role |
|---|---|
| Pulverize | Core — Werebear Overpower slam (primary damage) |
| Earthen Bulwark | Defensive — barrier / Unstoppable |
| Debilitating Roar | Utility — DR debuff + Fortify on packs |
| Cyclone Armor | Defensive — non-physical DR / resist buffer |
| Wolves | Companion — passive DPS layer |
| Grizzly Rage | Ultimate — Werebear damage ramp + Unstoppable |

## Key passive / class mechanic
- **Class mechanic:** Spirit Boons — bond with one spirit for two Boons, then one each from the others. Eagle's Boons (Crit) and Wolf/Snake support an Overpower bruiser; confirm the exact four with `graph_build`.
- **Key passive:** **Ursine Strength** — any-skill damage + Werebear DR; the backbone of Pulverize. See `references/classes/druid.md`.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("pulverize")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Stat priority (prose)
Willpower is the primary offensive attribute — it scales both skill damage and Overpower damage, making it doubly valuable for a build whose damage peaks come from Overpower slams. Beyond Willpower, prioritize damage-to-close/crowd-controlled enemies for the typical Pulverize melee range, then survivability stats (armor, resistances, max Life) to sustain the front-line positioning this build demands.

## How to play
Keep Cyclone Armor and a Spirit Boon defensive layer up, Debilitating Roar a pack to soften it, then Pulverize into the group for Overpower shockwaves. Pop Grizzly Rage for the Werebear damage ramp + Unstoppable burst window on Elites/bosses. Wolves run on their own. Manage Earthen Bulwark for barrier and Unstoppable uptime — Unstoppable windows are the primary damage multiplier trigger for this build's gear layer, so maintaining them is the core rhythm.

## Verify live
This is a curated snapshot. For the full current loadout (including paragon nodes, glyphs, and Spirit Boons) call `graph_build("pulverize")`; diff against the player's actual gear (ask them to paste or describe it).
