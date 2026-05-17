# Gems Runes

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-17 · Source: https://maxroll.gg/d4/resources/runewords-overview

## What it is

Runes and Runewords are a socketing system introduced in the **Vessel of Hatred** expansion (Season 13, Patch 2.4.1). Two runes — one **Rune of Ritual** and one **Rune of Invocation** — are socketed into the same item to form a **Runeword**. The Ritual rune generates a resource called **Offering**; when enough Offering accumulates, the Invocation rune fires automatically. Runes of Invocation can grant skills from *other classes*, making this system class-agnostic.

---

## Mechanics

1. **Two rune types exist:** Ritual (condition/generator) and Invocation (effect/consumer). As of Patch 2.4.1 there are **15 Runes of Ritual** and **26 Runes of Invocation**.
2. **Offering** is the internal currency. Each Ritual rune generates Offering when its condition is met; the paired Invocation rune fires once its Offering threshold is reached.
3. **Overflow:** Any Offering generated beyond the Invocation rune's requirement is Overflow. The bonus from the Overflow effect scales proportionally to the amount of Overflow accumulated.
4. **Each Invocation rune has a cooldown** that prevents repeated back-to-back triggers.
5. **Rarity matters:** Runes drop as Magic, Rare, or Legendary. Higher rarity grants stronger effects.
6. **Demanding Ritual runes pay more:** Harder-to-trigger conditions yield higher Offering per trigger.
7. **No duplicate runes:** You cannot use two copies of the same rune across all Runewords on a character.
8. **Gems and Runes are mutually exclusive per item:** An item can have Gems *or* Runes socketed, not both.

---

## Costs / requirements

| Requirement | Detail |
|---|---|
| Expansion | Vessel of Hatred required |
| Valid item slots | Helm, Chest, Legs, Two-Handed Weapon |
| Sockets needed | 2 sockets in the same item (one Ritual + one Invocation) |
| Storage | Socketables tab in the inventory |
| Tradeable | Yes |
| Duplicate rule | Cannot equip the same rune name twice across all runewords |
| Gems conflict | Cannot socket Gems and Runes in the same item |

---

## Recipes / breakpoints / interactions

### Runes of Ritual — Offering generated

| Rune | Trigger Condition | Offering Generated |
|---|---|---|
| Poc | Spend 5% of max Resource | 5 |
| Noc | Inflict Crowd Control (double if not Slow/Chill) | 5 / 10 |
| Igni | Stores every 0.3s; releases on non-Basic Skill cast | 25 per release |
| Tam | Cast a non-Channeled Core Skill | 25 |
| Yul | Cast a Skill with a Cooldown | 50 |
| Bac | Travel 5 meters | 50 |
| Cem | Cast Evade | 75 |
| Nagu | Maintain ≥1 active summon for 5s (100 per summon, up to 5) | 100–500 |
| Moni | Cast 2 Mobility or Macabre skills | 100 |
| Yax | Drink a Healing Potion | 200 |
| Neo | Deal damage after 2s without taking damage | 200 |
| Zan | Cast an Ultimate Skill | 200 |
| Cir | Cast 5 skills → exhausted for 3s | 300 |

### Runes of Invocation — Offering required & effect

| Rune | Offering Cost | Cooldown | Effect | Overflow Bonus |
|---|---|---|---|---|
| Gar | 25 | — | +2% Crit Chance for 5s (up to 10%) | (not covered in source) |
| Qua | 50 | 1s | +10% Movement Speed for 5s (up to 50%) | Increases duration |
| Wat | 100 | 1s | Necromancer's Horrid Decrepify — weakens & slows enemies | Increases duration |
| Vex | 100 | — | +1 to all Skills for 10s (up to +3) | (not covered in source) |
| Ceh | 100 | — | Summons Spirit Wolf for 8s | (not covered in source) |
| Teb | 100 | 1s | Necromancer's Abhorrent Iron Maiden — DoT & counterattack | +1% damage per Offering |
| Eom | 100 | 1s | Reduces active cooldowns by 0.1s | Further reduces cooldowns |
| Mot | 150 | 1s | Rogue's Dark Shroud — grants 1 shadow (reduces damage taken) | Grants multiple shadows |
| Tzic | 200 | 1s | Spiritborn's Concussive Stomp — damage & Knock Down | +1% damage per Offering |
| Thul | 250 | 2s | Sorcerer's Frost Nova — freezes nearby enemies | Increases size |
| Prid | 250 | 3s | Warlock's Dark Prison — tethers enemies for 3s | Increases duration |
| Que | 300 | 1s | Druid's Earthen Bulwark — 3s Barrier | Increases duration |
| Kry | 300 | — | Spiritborn's Vortex — damage & Pulls In enemies | (not covered in source) |
| Jah | 350–400* | — | Replaces next Evade with Sorcerer's Teleport | (not covered in source) |
| Lac | 400 | — | Barbarian's Challenging Shout — taunt & reduce damage taken 3s | (not covered in source) |
| Yom | 500 | 5s | Druid's Petrify — stuns enemies & restores 100 Resource | Increases Stun duration |
| Kel | 500 | — | Rally — grants Resource & Movement Speed for 8s | (not covered in source) |
| Ner | 600 | 6s | Rogue's Concealment — Unstoppable + Stealth for 5s | Increases duration |
| Ohm | 600 | — | Barbarian's War Cry — +7.5% damage for 6s | (not covered in source) |

*Jah costs 350 Offering per structural data; BacJah runeword accumulates 400 Offering via 25m of travel.

### Named Runeword examples

| Runeword | Components | How it works |
|---|---|---|
| **BacJah** | Bac (Ritual) + Jah (Invocation) | Traveling 25m builds 400 Offering via Bac; Jah replaces the next Evade with Teleport |

### Mythic Unique crafting via Runecrafting

Crafting Mythic Uniques at the Jeweler requires: **6 Legendary Runes + 6 Rare Runes + 6 Magic Runes** (specific named runes) **+ 2 Resplendent Spark**.

| Mythic Unique | Runes Required |
|---|---|
| Andariel's Visage | 6× Tam, 6× Qax, 6× Zan, 2× Resplendent Spark |

### Rune crafting (Jeweler)

Combine **3 runes of the same name** → receive **1 random rune** (higher or same tier).

### Drop sources

| Source | Condition |
|---|---|
| World Bosses | Standard drop |
| Kurast Undercity | Requires Tribute of Harmony |
| Helltide Chests | Standard drop |
| Tree of Whispers | Reward selection |

---

## Strategy

1. **Match Ritual to playstyle:** Pick a Ritual rune whose trigger aligns with how you naturally play — e.g., Cir (cast 5 skills) for skill-spammers, Zan (Ultimate cast) for Ultimate-reliant builds, Bac (movement) for mobile builds.
2. **Scale Overflow deliberately:** Pair fast-generating Ritual runes with low-cost Invocations (Wat, Teb, Mot) to trigger frequently and accumulate Overflow bonuses; pair slow-generating Ritual runes with high-cost Invocations for burst effects.
3. **Use cross-class utility:** Invocations like Ner (Concealment/Unstoppable), Thul (Freeze), and Prid (tether) provide utility unavailable in your own class toolkit — prioritize them for survivability gaps.
4. **Plan rune uniqueness globally:** Since no duplicate rune can appear across your full set of Runewords, plan all four item slots together before crafting or trading.
5. **Upgrade via Jeweler crafting:** If you have excess copies of a rune, combine 3× same-name at the Jeweler to fish for higher-rarity or more useful runes.
6. **BacJah on mobile builds:** The BacJah Runeword is particularly strong on builds that dash or reposition constantly, as movement passively charges Offering.
7. **Prioritize Legendary rarity:** Higher rarity runes grant stronger effects — target Legendary drops from World Bosses and Kurast Undercity with Tribute of Harmony.

---

## Pitfalls

- **Gems vs. Runes conflict:** Socketing runes into an item removes the ability to use Gems in that item — plan item socket allocation ahead of time.
- **Duplicate rune lock-out:** Accidentally using the same rune name in two different Runewords wastes a slot and is not immediately obvious; audit all socketed items before finalizing a setup.
- **Overflow wasted on low-cooldown Invocations:** If your Ritual rune generates Offering far faster than the Invocation cooldown allows, surplus Offering is lost — match generation rate to cooldown.
- **Runewords only fit specific slots:** One-handed weapons, Rings, Amulets, Gloves, and Boots cannot hold Runewords; don't socket runes expecting any item to work.
- **Vessel of Hatred required:** Runes are completely unavailable without the expansion — they do not drop or function on base-game-only accounts.
- **Jah Offering cost discrepancy:** Structural data lists Jah at 350 Offering; BacJah context states 400 — verify in-game before finalizing pairings, as values may vary by rune rarity.
- **Kel and Zid are newer additions:** Added in the Season 11 update (December 21, 2025) — older guides may omit them.
