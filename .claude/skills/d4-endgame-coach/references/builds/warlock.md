# Warlock — Dread Claws (flagship endgame build)

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## What this build is
The defining Season 13 Warlock: a Shadow summon/DoT bruiser built around **Dread Claws**. You send out persistent demonic claws that shred packs, layer Shadow damage-over-time, and feed the class resource while **Command Fallen** adds a second summon layer. **Dark Prison** locks targets down (CC + Weaken), **Metamorphosis** is the transformation burst window, and **Nether Step** handles mobility. Durable front line, high sustained Shadow damage. Scales off Intelligence.

## Skill bar
| Skill | Role |
|---|---|
| Dread Claws | Core — primary Shadow damage / summon engine |
| Command Fallen | Secondary summon layer + on-demand burst |
| Dark Prison | CC / setup — applies Fortify + Weaken (chain-aura enhancement) |
| Nether Step | Mobility (extra charge + movement-speed enhancements) |
| Metamorphosis | Transformation ultimate — burst + Terror Demon window |
| Rampage | Buff/steroid — elite hit-chance + killstreak damage |

## Key passive / class mechanic
- **Class mechanic:** Soul Shards — the Warlock's stacking resource/State, generated and consumed to empower demonic skills and the transformation. Sigils (demonic sigil skills) act like Necromancer Curses — persistent effects that buff the build's damage condition.
- **Key passive:** pull the exact key passive this build selects with `graph_build("dread-claws")` rather than guessing. See `references/classes/warlock.md`.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("dread-claws")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## How to play
Keep summons out (Dread Claws + Command Fallen), pull packs into Dark Prison to lock and Weaken them, then let the Shadow DoT and claws grind. Nether Step to reposition. Pop Metamorphosis on Elites/bosses for the transformation burst window and maintain Rampage's buff uptime.

The core loop is front-loaded on summon uptime — if the claws or fallen aren't active, the damage engine stalls. Prioritize keeping both summon skills cycling before worrying about burst windows.

## Stat and scaling priority (prose)
Intelligence is this build's primary offensive attribute and should be the first thing you look for on gear upgrades. Shadow skill damage and Core skill damage are the dominant additive tempering lines. Cooldown Reduction matters for Metamorphosis and Sigil uptime. Defensively, Max Life and total armor are the survivability levers; resist capping follows. Avoid investing in Willpower or Overpower — neither matches the build's damage condition.

## Verify live
This is curated coaching judgment, not a loadout table. For the full current loadout (gear, paragon nodes, charms/seal, glyphs) call `graph_build("dread-claws")`; diff against the player's actual gear (ask them to paste or describe it).
