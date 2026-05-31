# Rogue — Dance of Knives (flagship endgame build)

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## What this build is
The defining Season 13 Rogue: a **Dance of Knives** spin-to-win channeler. You orbit a storm of thrown knives that shreds everything around you while moving, layering Cold/Poison Imbuements for elemental conversion. Dark Shroud is the survival backbone, Dash keeps you mobile, Smoke Grenade controls packs, and Shadow Clone is the burst ultimate. High mobility, high uptime AoE — rewards setup and positioning. Scales off Dexterity.

## Skill bar
| Skill | Role |
|---|---|
| Dance of Knives | Core — channeled orbiting-knives damage (grenade-jumper / lucky-hit upgrades) |
| Dash | Mobility (extra charges + CDR) |
| Dark Shroud | Defensive — stacking DR + movement (the Rogue survival backbone) |
| Smoke Grenade | Utility / CC — Daze + Vulnerable setup |
| Cold Imbuement | Element layer — Chill/Freeze + Frigid Finesse multiplier (swap: Poison) |
| Shadow Clone | Ultimate — burst + extra damage source |

## Key passive / class mechanic
- **Class mechanic:** Specialization (Combo Points / Inner Sight / Preparation, swappable anytime) + Imbuements (Cold/Poison/Shadow). Running two active Imbuements raises overall Imbuement potency.
- **Key passive:** confirm the exact key passive this build runs with `graph_build("dance-of-knives")` — Dance of Knives builds typically lean on a Vulnerable/close-range multiplier. See `references/classes/rogue.md` for the key passive rationale by condition.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("dance-of-knives")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## How to play
Keep Dark Shroud stacked and an Imbuement active, Dash into a pack, then channel Dance of Knives and orbit the group while moving. Smoke Grenade to control and set up Vulnerable. Shadow Clone on Elites/bosses for the burst window. Manage Imbuement timing so the channel is always elementally converted, and never stand still without Dark Shroud stacks.

The key positioning principle: you deal damage while moving through the orbiting-knives pattern, so staying on the outside edge of packs while circling in keeps the knives on enemies longer. Standing still kills your output and your survivability simultaneously.

## Win condition
Sustained channeled AoE with elemental conversion active. The build wins by maintaining near-100% uptime on both Dance of Knives and at least one Imbuement, with Dark Shroud stacks always refreshed. If any of those three drop simultaneously, damage and survivability collapse together. Prioritize uptime over raw damage numbers when making gear decisions.

## Verify live
This is a curated coaching snapshot. For the full current loadout (including paragon nodes, glyphs, Specialization, exact Imbuement picks, charms, and seal) call `graph_build("dance-of-knives")`; diff against the player's actual gear (ask them to paste or describe it).
