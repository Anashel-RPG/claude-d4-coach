# Gems Runes

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-23 · Source: https://maxroll.gg/d4/resources/runewords-overview

## What it is

Runewords are a crafting and socket system introduced in the **Vessel of Hatred** expansion (Season 13, Patch 2.4.1). Each Runeword pairs exactly one **Rune of Ritual** (condition/trigger) with one **Rune of Invocation** (effect). The Ritual rune accumulates a resource called **Offering**; once the Invocation rune's threshold is met, its effect fires automatically.

- 15 Runes of Ritual and 26 Runes of Invocation exist as of Patch 2.4.1
- Both rune types drop in **Magic, Rare, and Legendary** rarity — higher rarity = stronger effect
- Runes are stored in the **Socketables** tab and are **tradeable**
- Runes of Invocation can grant skills from **other classes**

---

## Mechanics

1. **Offering generation** — The socketed Rune of Ritual fires on a specific condition and adds Offering toward the paired Invocation rune's threshold.
2. **Invocation trigger** — When accumulated Offering ≥ the Invocation rune's required amount, the effect activates and Offering resets.
3. **Overflow** — Any Offering generated beyond the threshold counts as Overflow; bonus effects scale with Overflow amount (e.g., longer duration, higher damage %).
4. **Cooldown** — Each Invocation rune has its own internal cooldown that prevents back-to-back triggers regardless of Offering.
5. **Rarity scaling** — Higher-rarity runes generate or require more Offering and produce stronger Overflow bonuses.
6. **Demanding Ritual runes generate more Offering per trigger** — harder conditions yield higher Offering values.

---

## Costs / requirements

| Requirement | Detail |
|---|---|
| Expansion | Vessel of Hatred (exclusive) |
| Valid item slots | Helm, Chest, Legs, Two-Handed Weapon |
| Sockets needed | 2 per item (one per rune) |
| Gems vs. Runes | Mutually exclusive — cannot equip both in the same item |
| Crafting runes (Jeweler) | Combine 3 runes of the same name → 1 random rune |
| Crafting Mythic Uniques | 2 Resplendent Spark + 6 Legendary Runes + 6 Rare Runes + 6 Magic Runes (specific names) |

---

## Recipes / breakpoints / interactions

### Runes of Ritual — Offering generation

| Rune | Trigger condition | Offering generated |
|---|---|---|
| Bac | Travel 25 m (400 total, ~50 per 5 m) | 50 / 5 m |
| Igni | Non-Basic Skill cast (stores every 0.3 s) | 25 |
| Tam | Non-Channeled Core Skill cast | 25 |
| Yul | Cooldown Skill cast | 50 |
| Nagu | Maintain ≥1 active summon for 5 s (up to 5 summons) | 100 |
| Neo | Avoid damage for 2 s | 200 |
| Noc | Inflict Crowd Control (×2 if not Slow/Chill) | 5 (or 10) |
| Poc | Spend 5% max Resource | 5 |
| Zan | Cast an Ultimate Skill | 200 |
| Cem | Cast Evade | 75 |
| Cir | Cast 5 skills → exhausted for 3 s | 300 |
| Moni | Cast 2 Mobility or Macabre skills | 100 |
| Yax | Use Healing Potion | 200 |

### Runes of Invocation — Effects & thresholds

| Rune | Offering required | Cooldown | Effect | Overflow bonus |
|---|---|---|---|---|
| Eom | 100 | — | Reduce active Cooldowns by 0.1 s | Further cooldown reduction |
| Vex | 100 | — | +1 to all Skills for 10 s | Up to +3 Skill ranks |
| Gar | 25 | — | +2% Crit Strike Chance for 5 s (stacks to 10%) | (not covered in source) |
| Qua | 50 | 1 s | +10% Movement Speed for 5 s (stacks to 50%) | Increases duration |
| Wat | 100 | 1 s | Necromancer's Horrid Decrepify — Weakens & Slows enemies | Increases duration |
| Ceh | 100 | — | Summon Spirit Wolf for 8 s (benefits from Summon bonuses) | (not covered in source) |
| Teb | 100 | 1 s | Necromancer's Abhorrent Iron Maiden — DoT & counterattack | +1% damage per Offering |
| Mot | 150 | — | Rogue's Dark Shroud — grant 1 shadow, reduces damage taken | (not covered in source) |
| Tzic | 200 | 1 s | Spiritborn's Concussive Stomp — damage + Knock Down | +1% damage per Offering |
| Thul | 250 | 2 s | Sorcerer's Frost Nova — Freeze nearby enemies | Increases size |
| Prid | 250 | 3 s | Warlock's Dark Prison — tether enemies for 3 s | Increases duration |
| Que | 300 | 1 s | Druid's Earthen Bulwark — Barrier for 3 s | Increases duration |
| Kry | 300 | — | Spiritborn's Vortex — damage + Pull In enemies | (not covered in source) |
| Jah | 350–400* | — | Replace next Evade with Sorcerer's Teleport (Unstoppable, deals damage) | (not covered in source) |
| Lac | 400 | — | Barbarian's Challenging Shout — taunt + reduce damage taken 3 s | (not covered in source) |
| Yom | 500 | 5 s | Druid's Petrify — Stun enemies + restore 100 Resource | Increases Stun duration |
| Kel | 500 | — | Rally — grant Resource + Movement Speed for 8 s | (not covered in source) |
| Ohm | 600 | — | Barbarian's War Cry — +7.5% damage for 6 s | (not covered in source) |
| Ner | 600 | 6 s | Rogue's Concealment — Unstoppable + Stealth for 5 s, Movement Speed | Increases duration |

*Jah requires 400 Offering via BacJah (traveling 25 m); structural relations list 350 as base.

### Notable Runeword recipes

| Runeword | Ritual rune | Invocation rune | Combined effect |
|---|---|---|---|
| BacJah | Bac | Jah | Travel 25 m (400 Offering) → replace next Evade with Teleport |

### Mythic Unique crafting example

| Item | Runes required | Additional cost |
|---|---|---|
| Andariel's Visage | 6× Tam, 6× Qax, 6× Zan | 2 Resplendent Spark |

---

## Strategy

1. **Match Ritual speed to Invocation threshold** — pair high-Offering-per-cast Ritual runes (Zan 200, Cir 300, Neo 200) with expensive Invocation runes (Ohm 600, Ner 600, Yom 500) to avoid wasting triggers.
2. **Low-threshold Invocations reward spammy Ritual runes** — Gar (25), Qua (50), and Eom (100) chain-fire when paired with Poc or Noc for near-constant uptime.
3. **Maximize Overflow for scaling effects** — pair a fast Ritual rune with a Tzic or Teb to stack the "+1% damage per Offering" Overflow bonus.
4. **BacJah for mobility builds** — any build that dashes or repositions frequently charges Bac quickly, granting free Teleports without spending a Sorcerer skill slot.
5. **Nagu synergy with summoner builds** — maintain 5 active summons for 5× the base Offering rate (100 per trigger × summon count).
6. **Slot choice matters** — reserve two-socket items for Runewords; don't slot Gems in the same item or you must choose one system.
7. **Craft unwanted runes at the Jeweler** — combine 3× identical runes into a random rune to convert surplus drops into desired ones.

---

## Pitfalls

- **Gems and Runes are mutually exclusive per item** — socketing a rune into a gem slot (or vice versa) is not possible; plan gear accordingly.
- **Runewords require the Vessel of Hatred expansion** — unavailable to base-game-only players.
- **Cir's 3-second exhaustion window** punishes builds that burst 5 skills rapidly but then can't cast to keep Offering flowing.
- **Invocation cooldowns are independent of Offering** — hitting Yom's 500 Offering before its 5 s cooldown expires wastes the surplus.
- **Higher-rarity runes are gated behind RNG** — Legendary runes needed for Mythic crafting (e.g., Andariel's Visage) require 6× specific Legendary runes plus 2 Resplendent Spark; plan for extended farming.
- **Three-rune Jeweler craft produces a *random* rune** — not a targeted upgrade; use this as a last resort rather than a reliable progression path.
- **Noc generates only 5 Offering per Crowd Control** (10 if not Slow/Chill) — extremely low; avoid pairing with high-threshold Invocations.
