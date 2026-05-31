# Barbarian — Frenzy (flagship endgame build)

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## What this build is
The defining Season 13 Barbarian: a dual-wield **Frenzy** attack-speed bruiser. Frenzy stacks ramp your attack speed, and the build's unique weapon configuration turns the basic-attack engine into a damage spender. Three Shouts (Rallying Cry, Challenging Shout, War Cry) keep you buffed and tanky. Steel Grasp pulls and sets up, Call of the Ancients is the ultimate. Fast, sticky melee with shout-driven uptime. Scales off Strength.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("frenzy")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Skill bar
| Skill | Role |
|---|---|
| Frenzy | Core engine — attack-speed ramp + primary damage |
| Rallying Cry | Shout — resource / movement / cooldown |
| Challenging Shout | Shout — defensive (DR + taunt) |
| War Cry | Shout — damage buff |
| Steel Grasp | Utility — pull + Vulnerable/Bleed setup |
| Call of the Ancients | Ultimate — burst + sustained buff |

## Key passive / class mechanic
- **Class mechanic:** Arsenal System — four weapons (2H Bludgeoning + 2H Slashing + two 1H), auto-swapped by skill type; only the Arsenal-assigned weapon feeds a given skill. **Technique Slot** grants one Weapon Expertise permanently.
- **Key passive:** confirm the exact key passive this build runs with `graph_build("frenzy")`. See `references/classes/barbarian.md` for key passive trade-offs.

## How to play
Open with Steel Grasp to pull a pack, cycle your three Shouts to stay buffed and tanky, then Frenzy to ramp attack speed and let the basic-attack engine carry the damage. Call of the Ancients on Elites and bosses. Keep all three shouts on cooldown rotation — shout uptime is the build's damage and survivability backbone, and it feeds the cast-then-detonate multiplier on your gloves slot.

## Why shout uptime is non-negotiable
Each shout serves a distinct role: Rallying Cry extends Frenzy uptime via resource sustain and Unstoppable, Challenging Shout provides the Damage Reduction and taunt that let you stand in melee, and War Cry delivers the Berserking window that underpins the damage burst. Missing any shout for more than a second or two substantially drops both offense and defense simultaneously.

## Stat priority (prose guidance)
Offensive scaling is primarily Strength (skill damage per 100 Str, also converts to Armor). After capping resistances and hitting the armor Damage Reduction threshold, invest in Critical Strike Chance and Critical Strike Damage, then Vulnerable Damage. Avoid stacking additive +skill-damage affixes at the expense of the multiplicative weapon slots — the build's damage multipliers live on weapons, not on armor affixes. For exact cap targets use `armor_breakpoint` and `references/stat-priorities.md`.

## Progression and upgrade priorities
1. The dual-wield weapon pair is the build's first priority — without the core weapon pair the build is a different, weaker archetype.
2. Shout gear (helm and pants uniques that pay off shout uptime) come next.
3. Mythic rings are a strong mid-to-late upgrade, not a blocker.
4. Charms and Seal (Season 13) are endgame multipliers — if damage plateaus despite good gear, check whether the full charm set is filled. Pull exact assignments from `graph_build("frenzy")`.
5. Paragon and glyph investment follows gear — see class file for sequencing rationale.

## Verify live
This is curated coaching context. For the full current loadout (including the full four-weapon Arsenal, paragon nodes, glyphs, and charm/seal assignments) call `graph_build("frenzy")`; diff against the player's actual gear (ask them to paste or describe it).
