# Druid

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Core identity
Shapeshifter who flows between Werewolf, Werebear, and human caster form, spending Spirit (built by Basic skills) on high-cost Core skills. Tanky and mobile in animal form, fragile and rooted in caster form. Damage is Physical, Lightning (Storm), Earth, and Poison. The class signature is **Spirit Boons** (passive bonuses bonded from four animal spirits) plus form-swapping key passives that reward alternating Werebear/Werewolf or Earth/Storm.

## Damage scaling buckets
- **Multiplicative sources:** Key Passives (Ursine Strength, Bestial Rampage, Lupine Ferocity, Perfect Storm, Nature's Fury, Earthen Might, One With Nature); legendary Aspects (Ursine Horror, Crushing, Inner Calm, Stormchaser's, the Companion aspects); Ring of Starless Skies (resource-spend); Heir of Perdition's Mother's Favor; Grizzly Rage's Werebear ramp. Critical, Vulnerable, and Overpower are their own separate buckets.
- **Additive sources:** Willpower (Druid's main offensive attribute — skill damage), Spirit Boon bonuses (Crit Chance, Crit Damage, Attack Speed from Eagle), Companion damage (Wolves/Ravens/Poison Creeper), +Core / +Earth / +Storm / +Werebear skill-damage tempers, additive damage paragon rares.
- **Critical / Vulnerable / Overpower hooks:** Willpower also scales Overpower Damage — central to Pulverize (Werebear Overpower is the flagship endgame burst); Snake Spirit Boon grants guaranteed Overpower on Earth skills; Storm Strike / Wind Shear apply Vulnerable; Petrify adds boss Crit Damage; Earthen Might converts Crits into resource/damage procs; Dexterity → Crit Chance.

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|
| Maul / Storm Strike / Wind Shear / Claw / Earth Spike | Basic — Spirit gen | Pick to match form (Werebear/Storm/Werewolf/Earth); Wind Shear applies Vulnerable |
| Pulverize | Core — Werebear AoE | Current top endgame core; Overpower-burst engine, becomes an Earth skill via Ursine Horror (feeds Earthen Might) |
| Shred | Core — Werewolf | Consecutive-hit chain; free Spirit on the second hit; pairs with Waxing Gibbous |
| Lightning Storm | Core — Storm channel | Maintain one cast per buff window; scales with Unsung Ascetic's Wraps |
| Tornado / Landslide / Stone Burst | Core — alt | Tornado seeks via Stormchaser's; Landslide/Stone Burst for Earth variants |
| Debilitating Roar | Defensive shout | Screen-wide; damage reduction + Weaken; near-universal survival button |
| Cyclone Armor | Passive mitigation | Resistance + DR uptime; party utility with Cyclonic Force |
| Earthen Bulwark | Barrier / Unstoppable | Mending Stone enables high Unstoppable uptime; Travertine variant adds offense |
| Trample / Blood Howl | Mobility / sustain | Reserve Trample as a CC escape, not a damage button |
| Ravens / Wolves / Poison Creeper | Companion | Summon DPS layer; One With Nature lets them attack without bar slots |
| Grizzly Rage | Ultimate — Werebear | Flagship ult; Werebear damage ramp + Unstoppable; Prime/Supreme keys |
| Cataclysm | Ultimate — Storm | Mjölnic Ryng grants a multiplier + unlimited resource during uptime; backbone of the AFK farmer |
| Lacerate / Petrify | Ultimate — alt | Lacerate (Werewolf multi-hit), Petrify (Earth boss Crit-Damage window) |

## Key passives / class mechanic
**Spirit Boons (class mechanic):** Unlocked ~L15 via "Spirits of the Lost Grove" (after Túr Dúlra stronghold). Four spirits — Deer, Eagle, Wolf, Snake — each with four Boons bought with Druidic Spirit Offerings. Bond with one spirit to take two of its Boons, then one Boon each from the other three (four total). Snake's Boons require all four spirits unlocked. Boons are swappable anytime.
- **Deer:** Thorns, max Spirit, DR vs Elites, movement/impairment reduction
- **Eagle:** Crit Chance, Lucky Hit, Attack Speed, Crit Damage, bonus Life (the offensive spirit)
- **Wolf:** Lucky Hit → reset Companion cooldowns / grant Spirit, Fortify, extend Ultimate duration
- **Snake:** guaranteed Overpower on Earth skills, Lightning discharge proc, Fortify on shapeshift Crit, Ultimate cooldown reduction on Nature Magic

**Key Passives (choose one):**
- **Ursine Strength** — any-skill damage + Werebear DR; backbone of Pulverize.
- **Bestial Rampage** — alternating Werebear/Werewolf grants stacking damage + attack speed; amplified by Wildheart Hunger.
- **Lupine Ferocity** — Werewolf Crit ramp; pairs with Tempest Roar (Storm skills become Werewolf skills).
- **Perfect Storm** — Storm-skill enabler (strong while leveling Storm).
- **Nature's Fury** — Earth and Storm skills trigger each other (interaction rules apply).
- **Earthen Might** — Crits restore resource + grant a damage window; triggered by Pulverize-Ursine-Horror or Storm skills.
- **One With Nature** — Companions attack passively without bar slots; the Companion-build enabler.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("pulverize")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Aspects and uniques — coaching judgment
The Druid's Aspect and Unique selection is tightly form- and element-locked. As a general principle: match your Aspects to the skill type and form your build is built around (Werebear vs. Werewolf vs. Storm vs. Earth vs. Companions) — an Aspect that only fires for one form or element category provides near-zero value if you're not activating its condition. For exact current slot assignments, which Aspects are mandatory vs. swappable, and what rolls to prioritize on each, pull `graph_build("pulverize")` and `lookup_aspect` at runtime.

Mythic Uniques that appear in endgame Druid loadouts tend to reward builds that generate or spend Spirit frequently, maintain high Unstoppable uptime, or stack a specific damage type. These are aspirational targets — the coach should verify which mythics are in the player's current loadout before recommending farming targets.

## Tempering and masterworking — coaching judgment
Match weapon tempering to the form/element your build is centered on — tempering a Werebear damage tag does nothing for a Storm build and vice versa. Armor tempering generally prioritizes survivability (armor, life, resistances) unless the build has strong defensive mechanics that free up those slots. For exact affix targets per slot and masterworking priority columns, call `lookup_item` + `graph_build("pulverize")` at runtime.

## Paragon — coaching judgment
Druid paragon rewards Willpower above other offensive attributes. Boards are selected to amplify either the form damage (Werebear/Werewolf), the element (Earth/Storm), or companion output depending on the build variant. Glyph priorities follow the same logic: match the glyph's activation condition to the skills and damage type the build actually uses. For the specific board sequence, node priorities, and glyph targets for the Pulverize build, pull `graph_build("pulverize")` at runtime.

## Mercenary pairing
- Hire: Raheir — taunt + Fortify + armor; layers onto the Druid's already-strong animal-form EHP for Pit pushing.
- Reinforce: Subo — pull + Vulnerable groups packs for Pulverize/Storm AoE and feeds the Vulnerable bucket.

## Season 13 Charms + Seal
Druid fills the 6 Charm slots (Charm 1-6) and 1 Seal slot with seasonal items. Charms are the season’s defining multiplier layer — missing or unoptimized Charm/Seal slots are a common reason endgame damage plateaus. The exact charm names and Seal for each build variant come from `graph_build("pulverize")` at runtime. (See `references/systems/seasonal-charms.md` for the charm system mechanics.)

## Common mistakes
- Fighting in human caster form without accounting for the survivability drop versus animal form.
- Judging a 2H weapon vs 1H + Totem by tooltip alone — one strong Aspect on a 2H often beats two weaker Aspects on the split.
- Recasting Hurricane unnecessarily and resetting the Tempest damage ramp; over-channeling Lightning Storm (the size buff only needs one cast per window).
- Spending Trample for damage instead of holding it as a CC-escape.
- Running a Companion build without One With Nature (or without a Companion on the bar) — the pets won't carry.
- Mismatching the Key Passive to the form/element (Pulverize wants Ursine Strength + Earthen Might, Werewolf wants Bestial Rampage/Lupine Ferocity, Companions want One With Nature).
- Leaving the Season 13 Charm/Seal slots empty or unoptimized — often the missing multiplier when damage stalls.
