# Spiritborn — Rock Splitter (flagship endgame build)

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## What this build is
The defining Season 13 Spiritborn: the **Rock Splitter** "Gorillaborn" — a Gorilla-spirit Earth bruiser. Rock Splitter pounds the ground for escalating physical damage while the Gorilla Spirit Hall layers **Barrier, Thorns, and Resolve** so you tank everything. **Armored Hide** and **The Protector** stack defenses, **Concussive Stomp** controls packs, and **Rushing Claw** keeps the engine fed. The tankiest of the Spiritborn archetypes. Scales off Dexterity.

## Skill bar
| Skill | Role |
|---|---|
| Rock Splitter | Core — escalating Earth/physical slam (primary damage) |
| Rushing Claw | Basic / generator — Vigor + setup |
| Armored Hide | Defensive — Barrier / DR |
| Counterattack | Utility — retaliation + Thorns synergy |
| Concussive Stomp | CC — knockback / setup |
| The Protector | Ultimate — defensive burst window |

## Key passive / class mechanic
- **Class mechanic:** Spirit Hall — **Gorilla primary** (Thorns + Barrier on Gorilla-skill hits) is what makes this build tanky; the secondary raises max Resolve (DR) and turns high Resolve into Unstoppable. Confirm the secondary with `graph_build`.
- **Key passive:** confirm the exact key passive this build runs with `graph_build("rock-splitter")`. See `references/classes/spiritborn.md`.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("rock-splitter")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Stat priorities (prose)
Offensive attribute is **Dexterity** — it drives skill damage. Strength adds Crit Chance for Spiritborn and is a secondary offensive consideration. Prioritize Resolve generation and Barrier uptime as defensive targets; the Gorilla secondary translates high Resolve into Unstoppable, which is the build's core survivability mechanism. Vigor cost reduction helps sustain the rotation. For exact targets and capping order, see `references/stat-priorities.md`.

## How to play
Keep the Gorilla Barrier and Resolve up (Armored Hide + Gorilla-skill hits), Concussive Stomp to control a pack, then Rock Splitter into the group and let the escalating damage ramp. Rushing Claw keeps Vigor flowing. Pop The Protector on Elites/bosses. The build's identity is never dropping its defensive stacks — high Resolve = Unstoppable = you keep slamming through everything.

## Verify live
This is a curated snapshot. For the full current loadout (including paragon nodes, glyphs, and Spirit Hall picks) call `graph_build("rock-splitter")`; diff against the player's actual gear (ask them to paste or describe it).
