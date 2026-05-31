# Seasonal Charms + Seal (Season 13)

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## What it is
The Season 13 power system. Every endgame loadout fills **6 Charm slots (Charm 1-6)** plus **1 Seal slot** with seasonal Talisman items. Charms grant flat skill-rank bonuses to a skill *category* (e.g. +2 to all Aura skills) and carry slot-typed unique affixes, so a full set of optimized charms is a large, build-defining multiplier layer stacked on top of normal gear. This is the seasonal mechanic that replaced **Season 11's Incense** and **Season 10's Chaos Perk** systems — when a player's damage plateaus at endgame, missing or unoptimized charms is one of the first things to check.

## Slots
| Slot | Holds | Notes |
|---|---|---|
| Charm 1-6 | Talisman Charms | Six independent slots. Most builds run five generic family charms + one unique charm. |
| Seal | A Seal talisman | One slot. Generic Seal for most builds; a few classes have a build-specific unique Seal. |

## How charms are named
Generic family charms follow the pattern **`<Prefix> of <Family>`**:

- **Five recurring prefixes** appear across every class: **Berú, Fer, Linta, Mlor, Phoba**. The prefix determines which slot/affix shape the charm rolls; you collect one of each to fill five of the six slots.
- **The "of <Family>" suffix is class- and archetype-specific** — it ties the charm's skill-rank bonus to that build's skill category.

So a Hammerdin runs "Berú of Light's Epiphany," "Fer of Light's Epiphany," etc., while a Dread Claws Warlock runs the same five prefixes "of Harash's Shadow."

## Generic charm families by class
| Class | Archetype | Charm family |
|---|---|---|
| Paladin | Hammerdin / aura | of Light's Epiphany |
| Paladin | Thorns / Shield of Retribution | of Righteous Will |
| Paladin | Auradin (Holy Light) | of Radiant Fire |
| Warlock | Dread Claws (summon) | of Harash's Shadow |
| Warlock | Dread Claws (variants) | of Horazon's Chains |
| Warlock | Eviscerate / Apocalypse | of the Nameless |
| Sorcerer | Shock / Ball Lightning | of the Threefold |
| Barbarian | Frenzy | of Sescheron's Fury |
| Barbarian | Frenzy (variant) | of the Crucible |
| Druid | Pulverize | of the Old Mountain |
| Druid | Pulverize (variant) | of the Den Mother |
| Spiritborn | Gorillaborn / Rock Splitter | of Wumba's Embrace |
| Spiritborn | Rushing Claw | of Balazan's Bite |
| Rogue | Dance of Knives | of the Sightless |

A class can have more than one family because the family follows the *skill archetype*, not just the class. To get a specific build's exact five-charm set and slot assignments, call `graph_build(build_name)` and read its Charm 1-6 entries, or `graph_entity` on the family aspect.

## Unique charms (the 6th slot)
Most builds reserve one Charm slot (usually Charm 4) for a build-specific **unique charm** instead of a sixth family charm. Confirmed unique charms:

| Class | Unique charm | Notes |
|---|---|---|
| Paladin | Griswold's Opus | Craftable ("Craft Griswold's Opus Charm" recipe). The signature Hammerdin charm. |
| Warlock | Seed of Horazon | Dread Claws / summon builds. |
| Spiritborn | Protean Heart | Gorillaborn builds. |
| Spiritborn | Harmony of Ebewaka | Fireborn / Simianborn builds. |
| Druid | Might of the Ursine | Companion / Storm Pack builds. |
| Druid | Banished Lord's Talisman | Storm Shred. |
| Druid | Dirge of Airidah | Storm Shred. |
| Necromancer | Red Blessing | Minion builds. |

Some builds instead park a powerful **mythic/unique gear item in the Charm 4 slot** (e.g. Paingorger's Gauntlets, Godslayer Crown, Blood-Mad Idol, Rustbitten Dirk) when its affix outperforms a sixth family charm. Always read the player's actual loadout rather than assuming a fixed sixth charm.

## The Seal slot
| Class | Seal | Notes |
|---|---|---|
| Any | Seal (generic) | Default; equipped in the Seal slot by most builds. |
| Paladin | Seal of the Second Trumpet | Datamined; craftable. Can slot in a Ring or the Seal/Charm slot. |
| Druid | Seal of the Diamond Mind | Pulverize builds. |

## What charms grant
- **Category skill ranks** — the headline effect. A charm adds flat ranks to an entire skill category (e.g. a Paladin Aura-category charm grants +2 to all Aura skills; charms also exist for category-specific bonuses like Juggernaut). Stacking the right family across all slots pushes key skills well past their gear-only rank ceiling.
- **Slot-typed unique affixes** — charms carry affixes keyed to a gear slot/weapon type (1H Sword, 1H Shield, 2H Axe, Ring, Amulet, Helm, Chest, Pants), letting a charm reinforce the affixes that matter for that build's weapon and armor setup.

For the exact rolled values on a given charm, use `lookup_affix` / `lookup_item` on the specific talisman; exact numbers vary by item power and are not assumed here.

## Acquisition / crafting
- Charms drop and are upgraded through Season 13 seasonal activities.
- Several signature charms are **crafted**, not dropped — confirmed recipes include **Craft Griswold's Opus Charm** (Paladin) and **Craft Seal of the Second Trumpet Charm** (Paladin). Use `lookup_recipe` for material costs.

## How to coach with charms
1. Ask which build the player runs, then `graph_build(<build>)` and read the Charm 1-6 + Seal entries — that is the target charm set.
2. Compare against the player's actual charms. Empty slots, wrong family (mismatched skill category), or a missing unique charm are common, high-impact gaps.
3. Frame charms as a *multiplier layer*: a build can have perfect gear and still underperform if the charm/seal slots are empty or off-archetype. This is frequently the answer to "my gear looks right but my damage is low."

## Pitfalls
- Leaving Charm or Seal slots empty — the single most common endgame damage leak in Season 13.
- Running a charm family that doesn't match your build's skill category (the skill-rank bonus is wasted).
- Forgetting that one Charm slot is usually a build-specific *unique* charm, not a sixth family charm — slotting a fifth family charm there is a downgrade for most builds.
- Not crafting the signature charm/seal (e.g. Griswold's Opus, Seal of the Second Trumpet) when the build calls for it.
