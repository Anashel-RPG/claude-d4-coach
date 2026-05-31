# Sorcerer

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Core identity
Ranged elemental caster channeling Cold, Lightning, and Fire for AoE and crowd control. Resource is Mana; Enchantment Slots passively extend skill effects without using bar space. Squishy by default — survival comes from Barriers (Ice Armor / Flame Shield), Teleport, and damage-reduction passives, so uptime and positioning gate the high ceiling.

## Damage scaling buckets
- **Multiplicative sources:** Key Passives (element-matched); legendary aspects that multiply a specific skill or mechanic; resource-spend ring effects; stacking elemental-rotation bonuses. Critical and Vulnerable are their own separate buckets.
- **Additive sources:** Intelligence (skill damage), skill-damage tempers matched to your element, additive paragon rares, passive bonuses tied to your element or trigger condition.
- **Critical / Vulnerable / Overpower hooks:** Dexterity → Crit Chance; certain skill upgrades (e.g. Weaken) apply Vulnerable; Cold builds chain Frozen into Shatter; Lightning builds stack Crackling Energy with crit; Overpower is niche and generally skipped.

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|
| Charged Bolts | Core — Lightning | Top S13 engine with pierce/seek aspects; pairs with Ball Lightning |
| Frozen Orb | Core — Cold | Iconic clear; auto-casts from Frost Nova via a key amulet unique |
| Chain Lightning | Core — Lightning | Bouncing AoE, high Lucky Hit; amplified by split/Crackling aspects |
| Ice Shards | Core — Cold | Enchantment fires at Frozen enemies; single-target heavy |
| Fireball / Incinerate | Core — Fire | Fireball = burst AoE, Incinerate = channeled DoT (Conflagration variant) |
| Ball Lightning | Mastery — Lightning | Orbital DPS; the damage core of the top Lightning build |
| Blizzard | Mastery — Cold | Static Field / damage-bonus upgrades; great pack control |
| Firewall / Meteor | Mastery — Fire | Firewall DoT (snapshot-aware), Meteor for Overpower variants |
| Teleport | Mobility / Defense | Universal; Enchantment grants free repositioning |
| Frost Nova | CC / Vulnerable | Mystical = Vulnerable; the Cold-build setup button |
| Flame Shield / Ice Armor | Defense / Barrier | Mid-action survival; Barriers refresh (do not stack) |
| Hydra / Lightning Spear / Familiar | Conjuration | Summon DPS layer; Familiar is a strong S13 Lightning pet |
| Unstable Currents / Deep Freeze / Inferno | Ultimate | One pick; Unstable Currents for Lightning, Deep Freeze for Cold |

## Key passives / class mechanic
**Key Passives (choose one):** Avalanche (Cold), Shatter (Frozen explode on death), Combustion (Fire), Esu's Ferocity (Fire/Cold), Overflowing Energy (Lightning/Mana), Vyr's Mastery (Lightning melee), Enlightenment (attack speed + additive).

The most important coaching call here is element-matching: Lightning builds want Overflowing Energy or Vyr's Mastery; Cold builds want Avalanche or Shatter; Fire builds want Combustion or Esu's Ferocity. Mismatching the Key Passive to your element is a common reason a build underperforms — verify this first when a player reports low damage.

**Enchantment Slots (class mechanic):**
- Slot 1 unlocks around mid-teens leveling, slot 2 shortly after.
- Any skill with at least one point can be enchanted; a skill can be on the bar AND in an Enchantment Slot simultaneously. Enhancement and Upgrade choices carry into the slot's passive proc — review them whenever you swap a skill in or out. Ultimates cannot be enchanted. Swap freely anytime outside combat.

**Season 13 Charms + Seal:** Sorcerer fills 6 Charm slots and 1 Seal slot with seasonal items. These are the season's defining multiplier layer; missing or unoptimized charms is the most common reason endgame damage stalls. For exact charm/seal assignments for a specific build, the coach pulls them from the knowledge graph at runtime. (See `references/systems/seasonal-charms.md` for the system.)

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("ball-lightning")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Tempering and masterworking guidance (prose)
Tempering on weapons prioritizes skill damage matched to your element (Lightning, Cold, or Fire) plus Mana-cost reduction or Lucky Hit depending on your build's trigger economy. Armor tempering focuses on survivability — Max Life, Barrier generation, total armor — before offensive secondaries.

Masterworking crit picks follow a consistent priority: first, the stat that most directly multiplies your primary damage type (usually a skill-damage or element-specific mod); second, Critical Strike Damage or Vulnerable Damage; third, a utility stat like Cooldown Reduction if Ultimate uptime is a bottleneck. Verify the exact slots against `graph_build` output for the specific build.

## Mercenary pairing
- Hire: **Raheir** — taunt, Fortify, and armor smooths the Sorcerer's thin effective HP.
- Reinforce: **Subo** — pull and Vulnerable procs group packs for AoE and feed the Vulnerable bucket.

## Common mistakes
- Spamming Core skills with no Mana plan (Basic skill, aspect support, or Enchantment sustain) and bottoming out.
- Ignoring Enchantment Enhancement/Upgrade choices — they carry through and change the passive effect significantly.
- Taking a Staff for stats while losing the Offhand's extra Aspect slot and cooldown-reduction bonus.
- Assuming Barriers stack — extra casts only refresh duration, not magnitude.
- Leaving Season 13 Charm/Seal slots empty or unoptimized — the missing multiplier when damage stalls.
- Mismatching Key Passive to element.
