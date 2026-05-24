# Gems Runes

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-24 · Source: https://maxroll.gg/d4/resources/runewords-overview

## What it is

Runewords are a socketing system introduced in the **Vessel of Hatred** expansion (Season 13, Patch 2.4.1). Each Runeword consists of exactly two runes socketed into the same item: one **Rune of Ritual** (the condition/trigger) and one **Rune of Invocation** (the effect). The Ritual rune generates a resource called **Offering**; once enough Offering accumulates, the Invocation rune fires automatically.

- 15 Runes of Ritual and 26 Runes of Invocation exist as of Patch 2.4.1
- Runes of Invocation can grant skills from **other classes**
- Both rune types drop in **Magic, Rare, and Legendary** rarity; higher rarity = stronger effect
- Runes are stored in the **Socketables** tab and are **tradeable**

---

## Mechanics

1. **Offering generation** — The socketed Ritual rune generates Offering whenever its trigger condition is met. More demanding conditions yield more Offering per trigger.
2. **Invocation firing** — When accumulated Offering meets or exceeds the Invocation rune's threshold, the Invocation effect activates and Offering resets.
3. **Overflow** — Any Offering accumulated beyond the threshold is called Overflow. Overflow scales a bonus secondary effect on the Invocation rune (e.g., increased duration, increased damage, increased stun duration). The bonus is proportional to the amount of Overflow.
4. **Cooldown** — Each Invocation rune has its own internal cooldown before it can fire again.
5. **Rarity scaling** — Magic < Rare < Legendary rarity increases the potency of both Ritual and Invocation effects.

### Runes of Ritual — reference table

| Rune | Trigger | Offering Generated |
|------|---------|-------------------|
| Bac | Travel 5 meters | 50 |
| Igni | Non-Basic Skill cast (stores every 0.3s, grants on cast) | 25 |
| Tam | Non-Channeled Core Skill cast | 25 |
| Yul | Cooldown Skill cast | 50 |
| Nagu | Maintain ≥1 active summon for 5 sec (per summon, up to 5) | 100 |
| Neo | Avoid taking damage for 2 sec | 200 |
| Noc | Inflict Crowd Control (double if not Slow/Chill) | 5 |
| Poc | Spend 5% of maximum Resource | 5 |
| Zan | Cast an Ultimate Skill | 200 |
| Cem | Cast Evade | 75 |
| Cir | Cast 5 skills (then exhausted for 3 sec) | 300 |
| Moni | Cast 2 Mobility or Macabre skills | 100 |
| Yax | Use a Healing Potion | 200 |

### Runes of Invocation — reference table

| Rune | Offering Cost | Cooldown | Effect | Overflow Bonus |
|------|--------------|----------|--------|----------------|
| Gar | 25 | — | +2% Crit Strike Chance for 5 sec (stacks up to 10%) | (not covered in source) |
| Qua | 50 | 1 sec | +10% Movement Speed for 5 sec (up to 50%) | Increases duration |
| Eom | 100 | — | Reduce active Cooldowns by 0.1 sec | Further reduces cooldowns |
| Vex | 100 | — | +1 to all Skills for 10 sec | Up to +3 Skill ranks |
| Wat | 100 | 1 sec | Necromancer's Horrid Decrepify — weakens & slows enemies | Increases duration |
| Ceh | 100 | — | Summons Spirit Wolf for 8 sec | (not covered in source) |
| Teb | 100 | 1 sec | Necromancer's Abhorrent Iron Maiden — DoT + counterattack | +1% damage per Offering |
| Mot | 150 | — | Rogue's Dark Shroud — gain 1 shadow, reduces damage taken | (not covered in source) |
| Tzic | 200 | 1 sec | Spiritborn's Concussive Stomp — damage + Knock Down | +1% damage per Offering |
| Thul | 250 | 2 sec | Sorcerer's Frost Nova — freeze nearby enemies | Increases size |
| Prid | 250 | 3 sec | Warlock's Dark Prison — tether enemies for 3 sec | Increases duration |
| Que | 300 | 1 sec | Druid's Earthen Bulwark — Barrier for 3 sec | Increases duration |
| Kry | 300 | — | Spiritborn's Vortex — damage + pull enemies | (not covered in source) |
| Jah | 350 (Bac context: 400) | — | Replace next Evade with Sorcerer's Teleport (Unstoppable, deals damage) | (not covered in source) |
| Lac | 400 | — | Barbarian's Challenging Shout — taunt + reduce damage taken for 3 sec | (not covered in source) |
| Yom | 500 | 5 sec | Druid's Petrify — stun enemies + restore 100 Resource | Increases Stun duration |
| Kel | 500 | — | Rally — grant Resource and Movement Speed for 8 sec | (not covered in source) |
| Ohm | 600 | — | Barbarian's War Cry — +7.5% damage for 6 sec | (not covered in source) |
| Ner | 600 | 6 sec | Rogue's Concealment — Unstoppable + Stealth + Movement Speed for 5 sec | Increases duration |

> *Kel and Zid are new Invocation runes added in the Season 11 update (December 21, 2025).*

---

## Costs / requirements

- **Expansion required:** Vessel of Hatred (Runewords are not available without it)
- **Item slots:** Helm, Chest, Legs, or Two-Handed Weapon — the item must have **two sockets**
- **Gems vs. Runes:** You **cannot** socket both Gems and Runes in the same item; they are mutually exclusive
- **Crafting (upgrade):** Combine **3 runes of the same name** at the Jeweler to create a random rune (upgrades rarity)
- **Mythic Unique crafting:** Requires **2 Resplendent Sparks + 6 Legendary Runes + 6 Rare Runes + 6 Magic Runes** (specific names per recipe)
- **Drop sources:** World Bosses · Kurast Undercity (with Tribute of Harmony) · Helltide Chests · Tree of Whispers rewards

---

## Recipes / breakpoints / interactions

### BacJah Runeword
| Component | Type | Role |
|-----------|------|------|
| Bac | Ritual | Generates 50 Offering per 5 m traveled |
| Jah | Invocation | Fires at 400 Offering — replaces next Evade with Teleport |

- Traveling **25 meters** completes 5 Bac triggers → 400 Offering → Jah fires
- Jah grants Unstoppable and deals damage on Teleport

### Andariel's Visage (Mythic Unique craft)
| Material | Quantity |
|----------|----------|
| Tam (Ritual rune) | ×6 |
| Qax (Ritual rune) | ×6 |
| Zan (Ritual rune) | ×6 |
| Resplendent Spark | ×2 |

### Offering breakpoints (Invocation fire thresholds)
Pair your Ritual rune's per-trigger output against the Invocation cost to estimate fire frequency:

| Offering Cost Tier | Invocation Runes |
|--------------------|-----------------|
| 25–100 | Gar, Qua, Eom, Vex, Wat, Ceh, Teb, Mot |
| 150–300 | Mot, Tzic, Thul, Prid, Que, Kry |
| 350–600 | Jah, Lac, Yom, Kel, Ohm, Ner |

- High-output Ritual runes (Cir 300, Zan 200, Neo 200, Yax 200) pair well with expensive Invocations
- Low-output Ritual runes (Noc 5, Poc 5, Tam 25) pair best with cheap Invocations (Gar 25, Qua 50)

---

## Strategy

1. **Match Offering rates to Invocation cost.** Calculate expected Offering per minute for your Ritual rune and confirm it realistically fires the Invocation at useful intervals. Cir (300 Offering on 5 skill casts) fires high-cost Invocations quickly in dense packs.
2. **Maximize Overflow for bonus scaling.** Pair a Ritual rune that overshoots the Invocation threshold to consistently generate Overflow and strengthen the secondary effect (e.g., Zan → Yom gives large Overflow that extends Petrify stun duration).
3. **Use Invocations as cross-class utility.** Classes lacking crowd control, mobility, or defensives benefit most — e.g., Barbarians slotting Thul (Frost Nova) or Jah (Teleport) for burst mobility.
4. **Nagu + summon builds.** With up to 5 active summons, Nagu generates 500 Offering per 5-second window, making it one of the fastest Offering generators for Necromancer or Druid summon builds.
5. **BacJah for mobility-focused builds.** Any build that naturally moves long distances (Barbarian Whirlwind, Rogue Twisting Blades) fires Jah frequently for free Teleport repositioning and Unstoppable uptime.
6. **Gem vs. Rune trade-off.** Gems provide passive stat bonuses; Runes provide active utility. Endgame builds with sufficient stats via Paragon/Aspects may favor Runes for the functional effects. Evaluate per item slot.
7. **Craft duplicates at the Jeweler.** Farming a specific rune name? Stockpile duplicates and combine 3× at the Jeweler to upgrade toward Legendary rarity for stronger effects.

---

## Pitfalls

- **Gems and Runes are mutually exclusive per item** — socketing a rune removes gem benefits from that slot; plan accordingly.
- **Invocation cooldowns gate fire rate** — a fast Ritual rune paired with a long-cooldown Invocation (e.g., Ner 6 sec, Yom 5 sec) wastes generated Offering; the Invocation won't fire more often than its cooldown allows.
- **Cir's 3-second exhaustion window** — after firing its 300 Offering burst, Cir generates nothing for 3 seconds; brief gaps in damage output can occur if the Invocation effect relied on Cir's cadence.
- **Runewords require Vessel of Hatred** — characters or accounts without the expansion cannot access this system at all.
- **Two sockets are mandatory** — items with only one socket cannot form a Runeword; check socket count before planning around a specific item.
- **Rune crafting output is random** — combining 3 runes of the same name at the Jeweler yields a *random* rune, not a guaranteed specific one; don't count on crafting to target a precise Invocation.
- **Overflow scales proportionally, not infinitely** — excess Offering past the overflow threshold improves the bonus, but pairing a very high-output Ritual with a very cheap Invocation doesn't stack unboundedly; balance accordingly.
