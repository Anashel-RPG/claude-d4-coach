# Sorcerer — Ball Lightning (flagship endgame build)

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## What this build is
The defining Season 13 Sorcerer: a Lightning Conjuration caster built around **Ball Lightning**. Slow-moving orbital bolts pile up around you and melt anything they orbit, while **Familiar** adds a persistent pet-damage layer and **Unstable Currents** is the burst ultimate. **Charged Bolts** feeds the rotation through the Enchantment system. Glass-cannon by default — survival comes from **Ice Armor** barriers and **Teleport** positioning. Scales off Intelligence.

## Skill bar
| Skill | Role |
|---|---|
| Ball Lightning | Core spender — primary Lightning damage (orbital) |
| Charged Bolts | Generator / Enchantment fuel (movement-speed + Weaken upgrades) |
| Teleport | Mobility / defense (Enchanted = free repositioning) |
| Ice Armor | Defensive barrier (cooldown + Permafrost upgrades) |
| Familiar | Conjuration companion — persistent Lightning pet DPS |
| Unstable Currents | Ultimate — Lightning burst window (boundless / CDR upgrades) |

## Key passive / class mechanic
- **Class mechanic:** Enchantment Slots — slot a skill (e.g. Ball Lightning, Familiar) to gain its passive effect without using bar space. Two slots unlock through leveling; swap freely.
- **Key passive:** **Overflowing Energy** (the Lightning/Mana key passive) is the standard pick for this build. See `references/classes/sorcerer.md` for the full key-passive breakdown.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("ball-lightning")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## How to play
Keep Ice Armor up and Familiar active. Teleport into a pack, drop Ball Lightning, and let the orbiting bolts stack on the group. Charged Bolts and the Enchantment slots keep the rotation fed. Pop Unstable Currents on Elites and bosses for the burst window. Reposition constantly — without an active barrier you are fragile.

The build's survival is entirely positioning-dependent. The barrier from Ice Armor has a finite magnitude and refreshes (does not stack) on recast, so watch the timing. Teleport is both escape and setup — use it to center the pack inside your Ball Lightning orbits, not just to flee.

The Enchantment system is where this build's passive output lives. Upgrade and Enhancement choices on your Enchanted skills carry through into the passive proc — review them each time you swap a skill in or out of the slot.

## Progression priority
Season 13 Charm and Seal slots are the most common reason endgame damage stalls. Fill them before chasing incremental gear upgrades. After that, masterworking the highest-impact offensive slot (verify with `graph_build("ball-lightning")`) gives more return than farming a marginally better base.

## Verify live
This is curated coaching context. For the full current loadout — gear by slot, paragon boards, glyphs, charms, seal, and Enchantment picks — call `graph_build("ball-lightning")` and diff against the player's actual gear.
