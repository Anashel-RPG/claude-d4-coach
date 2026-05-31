# Warlock

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Core identity
Season 13 demonic caster-summoner — channels Shadow and Fire (Hellfire) through clawed shadow swarms, fallen minions, demonic Sigils, and transformation. Core skills spend the Warlock's resource; the class layers its signature **Soul Shards** mechanic on top. Plays as a pet/DoT bruiser (Dread Claws + Command Fallen) or a Fire-AoE nuker (Apocalypse / Hell Fracture). The runaway top build is the Dread Claws summoner; Apocalypse is the #2 Fire-AoE push build, with Eviscerate and Hell Fracture as distinct endgame archetypes.

## Damage scaling buckets
- **Multiplicative sources:** legendary Aspects (crit-ramp, Shadow/demonic payoffs, resource-spend multipliers); the Soul Shards payoff; Mythic unique effects. Critical, Vulnerable, and Overpower are their own separate buckets.
- **Additive sources:** Intelligence (Warlock's main offensive attribute — skill damage); Core, Shadow, and Fire skill-damage tempers; additive damage paragon rares; minion/summon damage bonuses.
- **Critical / Vulnerable / Overpower hooks:** Dexterity feeds Crit Chance; CC skills apply Weaken/slow; Sigils layer demonic debuffs and Hellfire; Shadow builds stack DoT, Fire builds stack burn/Hellfire detonations. Overpower is generally skipped — Intelligence, not Willpower, is the priority.

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|
| Dread Claws | Core — summon | Top endgame core; summons clawed shadow swarms; carries the #1 build |
| Command Fallen | Minion / Core | Summons fallen minions; the pet-army layer |
| Apocalypse | Core / Fire AoE | Big Fire AoE; the #2 build's engine |
| Eviscerate / Hell Fracture | Core — archetype | Distinct endgame push builds |
| Umbral Chains | CC / utility | Captures + damages; the setup button |
| Dark Prison | CC / defense | Crowd control + Weaken / Fortify / Chain Aura |
| Nether Step | Mobility / evade | The Warlock dash |
| Rampage | Buff / killstreak | Killstreak damage ramp |
| Profane Sentinel | Sentry / turret | Stationary DPS |
| Sigil of Summons / Chaos / Subversion | Sigil category | Demonic sigils — persistent demonic damage conditions |
| Metamorphosis | Ultimate — transformation | Transform into a Terror Demon |
| Apocalypse (Annihilation) | Ultimate — Fire AoE | Screen-wide Fire detonation; the alternative ultimate pick |

## Key passives / class mechanic
**Soul Shards (class mechanic):** the Warlock's signature mechanic — a stacking resource/State the class generates and consumes to empower its demonic skills and transformation. Exact generation/spend rules are build-specific; confirm the active interaction with `graph_build` or a live lookup.

**Sigils (signature skill category):** a family of demonic sigil skills. Treat them like Necromancer Curses or Sorcerer Conjurations — persistent demonic effects that buff the build's damage condition.

**Key passive / archetype:** the Warlock's endgame builds organize around four archetypes — **Dread Claws** (summon/DoT bruiser), **Apocalypse** (Fire-AoE nuker), **Eviscerate**, and **Hell Fracture** (Fire) — and each selects the key passive that matches its damage condition. Pull the exact key passive for a given build with `graph_build("<build-name>")` rather than guessing.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("dread-claws")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Stat and scaling priority (prose)
Intelligence is the primary offensive attribute for nearly every Warlock build — prioritize it on gear upgrades across the board. Skill-damage tempers (Core or Shadow/Fire depending on archetype) are the dominant additive layer. Cooldown Reduction matters for Metamorphosis and Sigil uptime. Defensively, Max Life and total armor are the main levers, with resist capping as a floor requirement. Willpower and Overpower are generally wasted on this class — skip both unless a specific build variant explicitly calls for them.

For tempering: match the damage tag to your archetype. Summon/minion bonuses matter for Dread Claws and Command Fallen builds; Fire damage matters for Apocalypse and Hell Fracture. Consult `lookup_aspect` for exact roll ranges before committing to a tempering line.

## Masterworking priority (prose)
Prioritize your primary skill-damage type first (Core, Shadow, or Fire), then Critical Strike Damage or Vulnerable Damage as a second pick, then Intelligence or Cooldown Reduction. The exact item to masterwork first should be determined by which slot provides the largest per-tier damage gain — use `compute_dps` or `bucket_compare` to quantify before spending materials.

## Mercenary pairing
- **Hire:** Raheir — taunt + Fortify + armor; smooths the Warlock's frame while the pets/Sigils ramp up.
- **Reinforce:** Subo — pull + Vulnerable groups packs for Dread Claws / Apocalypse AoE and feeds the Vulnerable damage bucket.

## Season 13 Charms + Seal
Warlock fills 6 Charm slots and 1 Seal slot with seasonal items. The Charm and Seal assignments are the season's defining multiplier layer for this class — missing or unoptimized charm slots is a common reason endgame damage plateaus. For the exact charm names and seal for each build, call `graph_build("dread-claws")` (or the relevant build slug). See `references/systems/seasonal-charms.md` for the charm system mechanics.

## Common mistakes
- Running a Dread Claws / Command Fallen pet build without the summons on the bar — the pets are the damage and won't carry passively.
- Stacking the wrong attribute — Intelligence is the offensive attribute for nearly every Warlock build; Overpower/Willpower is wasted.
- Ignoring the Soul Shards mechanic — it's the class's signature multiplier layer; build around generating and spending it.
- Forgetting only one Ultimate (Metamorphosis or Apocalypse) and one key passive can be equipped at a time.
- Wasting Nether Step charges for damage instead of holding one as a CC-escape.
- Mismatching the build's key passive/damage type (Dread Claws = Shadow/summon, Apocalypse & Hell Fracture = Fire) — pull the exact key passive with `graph_build` rather than guessing.
- Leaving the Season 13 Charm/Seal slots empty or unoptimized.
