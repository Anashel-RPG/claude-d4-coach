# Gems Runes

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-25 · Source: https://maxroll.gg/d4/resources/runewords-overview

## What it is

Runewords are a socketing system introduced in the **Vessel of Hatred** expansion (Season 13, Patch 2.4.1). Each Runeword pairs one **Rune of Ritual** (condition/trigger) with one **Rune of Invocation** (effect). The Ritual rune accumulates a currency called **Offering**; once the required threshold is met, the Invocation rune fires automatically. Runes drop at Magic, Rare, and Legendary rarity — higher rarity grants stronger effects. There are **15 Runes of Ritual** and **26 Runes of Invocation** in the pool.

---

## Mechanics

1. **Two rune types per Runeword:** one Rune of Ritual + one Rune of Invocation, socketed into the same item.
2. **Offering:** Ritual runes generate Offering when their trigger condition is met. Harder triggers generate more Offering per proc.
3. **Invocation threshold:** when accumulated Offering ≥ the Invocation rune's cost, the Invocation effect fires and Offering resets.
4. **Overflow:** surplus Offering beyond the required threshold scales a bonus effect on the Invocation rune (e.g., increased duration, extra damage).
5. **Rarity scales power:** Magic < Rare < Legendary; all three rarities exist for both rune types.
6. **Cross-class skills:** Runes of Invocation can grant skills from other classes (e.g., Frost Nova, Teleport, Concealment) regardless of your class.
7. **Gems vs. Runes are mutually exclusive:** a single item cannot hold both Gems and Runes.
8. **Storage & trading:** Runes are tradeable and stored in the **Socketables** tab of the stash.

---

## Costs / requirements

- **Expansion required:** Vessel of Hatred (Runewords unavailable without it).
- **Valid item slots:** Helm, Chest, Legs, Two-Handed Weapon (items must have 2 sockets).
- **One Runeword per item** — two sockets consumed (one Ritual, one Invocation).
- **Gems and Runes cannot share an item.**

### Rune of Ritual — Offering generated

| Rune | Trigger | Offering |
|------|---------|----------|
| Bac | Travel 5 meters | 50 |
| Igni | Non-Basic Skill cast (stores every 0.3s, grants on cast) | 25 |
| Tam | Non-Channeled Core Skill cast | 25 |
| Yul | Cooldown Skill cast | 50 |
| Nagu | Maintain ≥1 active summon for 5s (per summon, up to 5) | 100 |
| Neo | Avoid damage for 2 seconds | 200 |
| Noc | Inflict Crowd Control (double if not Slow/Chill) | 5 |
| Poc | Spend 5% of max Resource | 5 |
| Zan | Cast an Ultimate Skill | 200 |
| Cem | Cast Evade | 75 |
| Cir | Cast 5 skills (then exhausted 3s) | 300 |
| Moni | Cast 2 Mobility or Macabre skills | 100 |
| Yax | Use Healing Potion | 200 |

### Rune of Invocation — Offering required & effect

| Rune | Cost | Effect | Cooldown | Overflow bonus |
|------|------|--------|----------|----------------|
| Gar | 25 | +2% Crit Strike Chance for 5s (stacks to 10%) | — | — |
| Qua | 50 | +10% Movement Speed for 5s (stacks to 50%) | 1s | Increased duration |
| Eom | 100 | Reduce active Cooldowns by 0.1s | — | Further CD reduction |
| Vex | 100 | +1 to all Skills for 10s | — | Up to +3 Skill ranks |
| Ceh | 100 | Summon Spirit Wolf for 8s | — | — |
| Wat | 100 | Necromancer's Horrid Decrepify (Weaken + Slow) | 1s | Increased duration |
| Teb | 100 | Necromancer's Abhorrent Iron Maiden (DoT + counterattack) | 1s | +1% dmg per Offering |
| Mot | 150 | Gain 1 shadow from Rogue's Dark Shroud | — | — |
| Tzic | 200 | Spiritborn's Concussive Stomp (damage + Knock Down) | 1s | +1% dmg per Offering |
| Thul | 250 | Sorcerer's Frost Nova (freeze nearby enemies) | 2s | Increased size |
| Prid | 250 | Warlock's Dark Prison (tether enemies 3s) | 3s | Increased duration |
| Que | 300 | Druid's Earthen Bulwark (Barrier 3s) | 1s | Increased duration |
| Kry | 300 | Spiritborn's Vortex (damage + pull) | — | — |
| Jah | 350 | Replace next Evade with Sorcerer's Teleport (Unstoppable + dmg) | — | — |
| Lac | 400 | Barbarian's Challenging Shout (taunt + reduce damage taken 3s) | — | — |
| Kel | 500 | Rally (grant Resource + Movement Speed 8s) | — | — |
| Yom | 500 | Druid's Petrify (stun enemies + restore 100 Resource) | 5s | Increased Stun duration |
| Ner | 600 | Rogue's Concealment (5s: Movement Speed, Unstoppable, Stealth) | 6s | Increased duration |
| Ohm | 600 | Barbarian's War Cry (+7.5% damage 6s) | — | — |
| Zid | — | (not covered in source) | — | — |

---

## Recipes / breakpoints / interactions

### Crafting runes at the Jeweler
- Combine **3 runes of the same name** → receive **1 random rune** (any name/type).

### Crafting Mythic Uniques (Runecrafting)
Requires: **2 Resplendent Spark + 6 Legendary Runes + 6 Rare Runes + 6 Magic Runes** of specific names.

| Mythic Unique | Runes required |
|---------------|----------------|
| Andariel's Visage | 6× Tam (Legendary), 6× Qax, 6× Zan + 2 Resplendent Spark |

### Notable Runeword combos

| Runeword | Ritual rune | Invocation rune | How it works |
|----------|-------------|-----------------|--------------|
| BacJah | Bac | Jah | Travel 25m total (5× Bac at 50 Offering each = 400) → next Evade replaced with Sorcerer's Teleport |

### Overflow breakpoints
- Overflow is proportional: the more surplus Offering beyond the threshold, the stronger the bonus.
- High-Offering Invocations (Yom 500, Ner/Ohm 600) benefit most from fast Ritual runes like Cir (300/burst) or Zan (200/Ultimate).

---

## Strategy

1. **Match Ritual pace to Invocation cost.** Low-cost Invocations (Gar 25, Qua 50, Eom/Vex/Ceh/Wat/Teb 100) pair well with low-volume Ritual runes (Noc, Poc). High-cost Invocations (Yom, Ner, Ohm 500–600) need burst generators like Zan, Cir, or Yax.
2. **Chase Overflow for scaling.** Tzic and Teb scale damage by +1% per Offering in Overflow — pair with high-yield Ritual runes to maximize surplus.
3. **Use cross-class utility offensively or defensively.** Thul (Frost Nova) freezes for set-up; Jah (Teleport) adds mobility to non-Sorcerer classes; Prid (Dark Prison) groups enemies for burst.
4. **Slot in survivability slots.** Helm/Chest/Legs all accept Runewords — put defensive Invocations (Que, Mot, Lac) in armor slots and offensive ones (Ohm, Tzic, Teb) in the two-handed weapon slot.
5. **Summon-heavy builds:** Nagu generates 100 Offering per 5s per active summon (cap 5) — with 5 summons that is 500 Offering per cycle, capable of firing high-cost Invocations repeatedly.
6. **Upgrade runes at the Jeweler** when stuck on a specific rune. 3× any named rune → 1 random rune is the primary upgrade/re-roll path.
7. **Farm targeted drop sources.** Kurast Undercity (Tribute of Harmony), World Bosses, Helltide Chests, and Tree of Whispers rewards all drop runes; rotate these for volume.

---

## Pitfalls

- **Gems are locked out.** Socketing a Runeword in an item permanently bars Gems from that item — plan item slots before committing.
- **Runewords are Vessel of Hatred exclusive.** Base-game accounts cannot equip or benefit from them.
- **Rune crafting at the Jeweler is random.** 3× same rune gives a *random* output — not a specific upgrade; don't burn rare runes expecting a targeted result.
- **Cir's 3-second exhaustion.** Generates 300 Offering then locks out for 3s — do not pair with Invocations that need constant rapid firing.
- **Item socket requirements.** Items need exactly 2 sockets to hold a Runeword; a 1-socket item cannot form a Runeword.
- **Noc double-Offering only for non-Slow/Chill CC.** Do not assume all crowd control doubles the Offering; Slow and Chill only generate the base 5.
- **Mythic crafting is resource-intensive.** 6 Legendary + 6 Rare + 6 Magic named runes + 2 Resplendent Sparks per Mythic Unique — farm all three rarities, not just Legendaries.
