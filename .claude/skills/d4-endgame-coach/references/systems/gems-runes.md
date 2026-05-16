# Gems Runes

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-16 · Source: https://maxroll.gg/d4/resources/runewords-overview

## What it is

Gems and Runes are socketable items placed into gear to provide bonuses. **Runes** (introduced in the Vessel of Hatred expansion, Season 13 / Patch 2.4.1) are the primary focus here. They come in two functional types:

- **Rune of Ritual** — generates a resource called **Offering** when a specific condition is met
- **Rune of Invocation** — consumes a set amount of Offering to trigger a cross-class skill effect

A paired Ritual + Invocation rune slotted into the same item forms a **Runeword**.

Gems and Runes **cannot occupy the same item** — a socket holds one or the other.

---

## Mechanics

1. **Socket requirement:** Runewords require an item with exactly **two sockets** — one for the Ritual rune, one for the Invocation rune.
2. **Eligible slots:** Helm, Chest, Legs, and two-handed Weapons only.
3. **Equip cap:** A character can have at most **two Runewords** active at one time.
4. **No duplicate runes:** You cannot use the same rune in more than one Runeword on a single character.
5. **Rune rarities:** Runes drop as Magic, Rare, or Legendary. Higher rarity = stronger effect.
6. **Offering flow:** The Ritual rune fills an Offering counter; when the counter meets the Invocation rune's threshold, the cross-class skill fires automatically.
7. **Overflow:** If Offering generated exceeds the Invocation threshold, the surplus is called **Overflow**. Each Invocation rune has a distinct Overflow bonus proportional to the surplus amount.
8. **Storage & trade:** Runes are tradeable and stored in the **Socketables** tab.

---

## Costs / requirements

- Requires the **Vessel of Hatred** expansion.
- Items must have **two sockets** to form a Runeword.
- Crafting via Jeweler: combine **3 runes of the same name** → 1 random rune (same or higher rarity).
- Crafting non-Legendary runes has a chance to produce a rune of the next higher rarity.
- Crafting **Mythic Uniques** via Runecrafting costs: **2 Resplendent Spark + 6 Legendary Runes + 6 Rare Runes + 6 Magic Runes** of specific names.

**Invocation rune Offering costs:**

| Rune | Offering Required | Cooldown | Triggered Effect | Overflow Bonus |
|------|------------------|----------|-----------------|----------------|
| Wat | 100 | 1s | Necromancer's Horrid Decrepify (weakens/slows) | Increases duration |
| Vex | 100 | 5s | +1 to all Skills for 10s (up to +3 via Overflow) | Additional Skill ranks (max 3) |
| Mot | 150 | 1s | Rogue's Dark Shroud (1 shadow, reduces damage taken) | Grants multiple shadows |
| Tzic | 200 | 1s | Spiritborn's Concussive Stomp (damage + knockdown) | +1% damage per Offering |
| Prid | 250 | 3s | Warlock's Dark Prison (tethers enemies for 3s) | Increases duration |
| Thul | 250 | 2s | Sorcerer's Frost Nova (freeze enemies) | Increases effect size |
| Kry | 300 | 3s | Spiritborn's Vortex (damage + pull) | Increases vortex size |
| Jah | 350 | 3.5s | Sorcerer's Teleport (replaces next Evade) | Stores excess Offering |
| Lac | 400 | 1s | Barbarian's Challenging Shout (taunt + 3s damage reduction) | Increases duration |
| Kel | 500 | 3s | Paladin's Rally (Resource + Movement Speed for 8s) | Increases resource |
| Yom | 500 | 5s | Druid's Petrify (stun enemies + restore 100 Resource) | Increases Stun duration |
| Ner | 600 | 6s | Rogue's Concealment (5s: Movement Speed + Unstoppable + Stealth) | Increases duration |

---

## Recipes / breakpoints / interactions

**Ritual rune Offering generation:**

| Rune | Offering Generated | Condition |
|------|--------------------|-----------|
| Poc | 5 | 5% of max Resource spent |
| Noc | 5 (×2 if non-Slow/Chill CC) | Inflicting a Crowd Control |
| Igni | 25 (stored every 0.3s) | Granted when a non-Basic Skill is cast |
| Tam | 25 | Non-Channeled Core Skill cast |
| Cem | 75 | Evade cast |
| Bac | 50 | Player travels 5 meters |
| Moni | 100 | Two Mobility or Macabre skills cast |
| Nagu | 100 | 1 active summon maintained for 5s (×per summon, max 5) |
| Yax | 200 | Healing Potion consumed |
| Neo | 200 | Dealing damage after 2s without taking damage (resets if Invulnerable) |
| Zan | 200 | Ultimate Skill cast |
| Cir | 300 | After casting 5 skills (then exhausted for 3s) |

**Notable Runeword examples:**

| Runeword | Recipe | Effect |
|----------|--------|--------|
| BacJah | Bac + Jah | Accumulate 400 Offering by traveling 25m → replace next Evade with Teleport |
| Andariel's Visage (Mythic) | 6× Tam + 6× Qax + 6× Zan + 2 Resplendent Spark | Crafts the Mythic Unique Andariel's Visage |

**Drop sources:** World Bosses · Kurast Undercity (with Tribute of Harmony) · Helltide Chests · Tree of Whispers rewards

---

## Strategy

1. **Match generation rate to cost.** Pair high-yield Ritual runes (Zan: 200, Cir: 300) with high-cost Invocations (Ner: 600, Yom: 500); pair low-yield runes (Poc, Noc) with cheap Invocations (Wat: 100, Tzic: 200).
2. **Leverage Overflow deliberately.** If your Ritual rune can over-generate (e.g., Cir 300 into Tzic 200), the surplus Overflow amplifies the triggered effect — build around consistent over-generation.
3. **Cir requires skill density.** Cir fires after 5 skill casts then exhausts for 3 seconds; fast-hitting builds gain more cycles per minute.
4. **Noc doubles on hard CC.** Any crowd control that isn't Slow or Chill gives 10 Offering instead of 5 — favor builds that apply Stuns, Freezes, or Knockdowns.
5. **Bac pairs naturally with mobile builds.** At 50 Offering per 5m, a movement-heavy build (Evade-spam, dash skills) passively accumulates Offering for the BacJah combo.
6. **Plan rune uniqueness constraint early.** With only two Runewords allowed and no duplicate runes permitted, plan both Runewords together to avoid conflicts — especially for Legendary runes that are hard to farm.
7. **Craft up from low-rarity surplus.** Hoard 3× duplicate low-rarity runes and craft at the Jeweler for a chance at higher rarity; farm Kurast Undercity with Tribute of Harmony for targeted drops.

---

## Pitfalls

- **Gems and Runes are mutually exclusive per item** — socketing a Rune removes the ability to use a Gem in that same item.
- **Only 2-socket items can hold Runewords** — single-socket items cannot form a Runeword.
- **Duplicate rune restriction is character-wide** — using Zan in one Runeword locks it out of your second Runeword entirely.
- **Max two Runewords per character** — extra socketed gear beyond two active Runewords does not stack.
- **Neo Offering resets on Invulnerability** — builds using Invulnerability frames (e.g., Evade-based effects) will lose Neo's Offering counter.
- **Cir's 3-second exhaustion punishes burst windows** — if your damage window aligns with Cir's downtime, the Runeword adds nothing during that window.
- **Rune crafting output is random** — combining 3× of the same rune yields a *random* rune, not the same name; do not craft when you need a specific rune.
- **Vessel of Hatred required** — Runes and Runewords are inaccessible without the expansion.
