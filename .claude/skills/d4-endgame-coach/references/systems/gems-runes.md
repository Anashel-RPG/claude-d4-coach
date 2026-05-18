# Gems Runes

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-18 · Source: https://maxroll.gg/d4/resources/runewords-overview

## What it is

Runewords are a socketing system introduced in the **Vessel of Hatred** expansion (Season 13, Patch 2.4.1). Each Runeword is formed by pairing one **Rune of Ritual** (condition/trigger) with one **Rune of Invocation** (effect) in the same item. The Ritual rune accumulates a currency called **Offering**; once the threshold is met, the Invocation rune fires.

Runes are separate from Gems — you cannot have both in the same item.

---

## Mechanics

1. **Two rune types** exist: Ritual (generates Offering) and Invocation (consumes Offering to trigger an effect).
2. **Offering** is an internal resource tracked per item. When the Ritual rune's condition is met, it adds Offering toward the Invocation rune's cost.
3. When accumulated Offering meets or exceeds the Invocation rune's threshold, the Invocation effect fires automatically.
4. **Overflow** — surplus Offering beyond the threshold — grants a proportional bonus on top of the base Invocation effect (e.g., extended duration, increased damage).
5. **Rune rarity** (Magic / Rare / Legendary) affects potency; higher rarity = stronger effect.
6. Runes of Invocation can grant skills from **other classes** (e.g., a Barbarian using Frost Nova via Thul).
7. More demanding Ritual runes (harder conditions) generate higher Offering per trigger.
8. A character **cannot use the same rune twice** across all equipped Runewords.

---

## Costs / requirements

- **Expansion required:** Vessel of Hatred
- **Valid item slots:** Helm, Chest, Legs, Two-Handed Weapon (item must have 2 sockets)
- **Gems vs. Runes:** mutually exclusive per item — cannot socket both in the same item
- **Pool size (Patch 2.4.1):** 15 Runes of Ritual, 26 Runes of Invocation
- **Storage:** Socketables tab (stash)
- **Tradeable:** Yes

**Jeweler crafting (rune upgrading):**
- Combine **3 runes of the same name** → 1 random rune (higher tier implied)

**Mythic Unique crafting via Runecrafting:**
- Requires: **2 Resplendent Spark + 6 Legendary Runes + 6 Rare Runes + 6 Magic Runes** (specific names per item)

---

## Recipes / breakpoints / interactions

### Runes of Ritual — Offering generated

| Rune | Trigger Condition | Offering Generated |
|------|------------------|--------------------|
| Bac | Travel 25 meters | 400 |
| Cem | Cast Evade | 75 |
| Cir | Cast 5 skills (then exhausted 3 s) | 300 |
| Igni | Non-Basic Skill cast (stores 25 every 0.3 s, grants on cast) | 25 |
| Moni | Cast 2 Mobility or Macabre skills | 100 |
| Nagu | Maintain ≥1 active summon for 5 s (×1 per summon, up to 5) | 100 |
| Noc | Inflict Crowd Control (double if not Slow/Chill) | 5 (×2) |
| Poc | Spend 5% of max Resource | 5 |
| Zan | Cast an Ultimate Skill | 200 |
| Yax | Use a Healing Potion | 200 |
| Yul | Cast a Cooldown Skill | 50 |
| Tam | Cast a non-Channeled Core Skill | 25 |
| Neo | Avoid damage for 2 seconds | 200 |

### Runes of Invocation — Offering cost & effect

| Rune | Cost | Invoked Skill / Effect | Cooldown | Overflow Bonus |
|------|------|----------------------|----------|----------------|
| Eom | 100 | Reduces active cooldowns by 0.1 s | 1 s | Further CDR |
| Gar | 25 | +2% Crit Strike Chance for 5 s (stacks to +10%) | — | — |
| Qua | 50 | +10% Movement Speed for 5 s (stacks to +50%) | 1 s | Increased duration |
| Vex | 100 | +1 to all Skills for 10 s | — | Up to +3 Skill ranks |
| Wat | 100 | Necromancer's Horrid Decrepify (Weaken + Slow) | 1 s | Increased duration |
| Ceh | 100 | Summon Spirit Wolf for 8 s | — | — |
| Teb | 100 | Necromancer's Abhorrent Iron Maiden (DoT + counterattack) | 1 s | +1% damage per Offering |
| Mot | 150 | Rogue's Dark Shroud (1 shadow, reduced damage taken) | — | — |
| Tzic | 200 | Spiritborn's Concussive Stomp (damage + Knockdown) | 1 s | +1% damage per Offering |
| Thul | 250 | Sorcerer's Frost Nova (Freeze nearby enemies) | 2 s | Increased AoE size |
| Prid | 250 | Warlock's Dark Prison (tether enemies 3 s) | 3 s | Increased duration |
| Que | 300 | Druid's Earthen Bulwark (Barrier 3 s) | 1 s | Increased duration |
| Kry | 300 | Spiritborn's Vortex (damage + Pull In) | — | — |
| Jah | ~400 | Replace next Evade with Sorcerer's Teleport (Unstoppable) | — | — |
| Lac | 400 | Barbarian's Challenging Shout (Taunt + damage reduction 3 s) | — | — |
| Yom | 500 | Druid's Petrify (Stun + restore 100 Resource) | 5 s | Increased Stun duration |
| Kel | 500 | Paladin's Rally (Resource + Movement Speed 8 s) | — | — |
| Ohm | 600 | Barbarian's War Cry (+7.5% damage for 6 s) | — | — |
| Ner | 600 | Rogue's Concealment (Unstoppable + Stealth 5 s + Move Speed) | 6 s | Increased duration |

### Named Runeword example

| Runeword | Components | How it works |
|----------|-----------|-------------|
| BacJah | Bac (Ritual) + Jah (Invocation) | Traveling 25 m builds 400 Offering → next Evade becomes Teleport |

### Mythic Unique crafting example

| Item | Rune ingredients | Other materials |
|------|-----------------|-----------------|
| Andariel's Visage | 6× Tam (Legendary), 6× Qax (Rare), 6× Zan (Magic) | 2× Resplendent Spark |

### Rune drop sources

| Source | Notes |
|--------|-------|
| World Bosses | Drop runes directly |
| Kurast Undercity | Requires Tribute of Harmony |
| Helltide Chests | Standard chest loot |
| Tree of Whispers | Reward cache |

---

## Strategy

1. **Match Offering generation rate to Invocation cost.** Low-cost Invocations (Eom 100, Qua 50, Gar 25) fire frequently with any Ritual rune; high-cost ones (Ner 600, Ohm 600, Yom 500) need high-throughput Rituals like Zan (Ultimate) or Bac (movement).
2. **Exploit Overflow for max value.** Pair a fast-generating Ritual rune with a low-cost Invocation to stack large Overflow bonuses (e.g., Tzic's "+1% damage per Offering" scales with surplus).
3. **Use BacJah on movement-heavy builds.** Bac accumulates 400 Offering from 25 m of travel, granting free Teleport on Evade — no Sorcerer required.
4. **Use Invocations for cross-class utility.** Classes without a freeze can equip Thul (Frost Nova); classes without a gap-closer can equip Jah (Teleport).
5. **Pair Nagu with summon-heavy builds.** Up to 5 active summons × 100 Offering every 5 s = 500 Offering per cycle; easily fuels 500-cost Invocations.
6. **Noc doubles on hard CC.** If your build applies Stun, Knockdown, or Freeze (not Slow/Chill), Noc generates 10 Offering per proc instead of 5.
7. **Plan the no-duplicate rule around your gear.** You can't run the same rune in two different Runewords simultaneously — budget unique runes across all socketed items.
8. **Upgrade via Jeweler when targeting a specific rune.** Combine 3× the same rune name to reroll into a (random) higher-value rune if your target is scarce.

---

## Pitfalls

- **Gems and Runes are mutually exclusive per item** — socketing a Runeword removes any existing Gem and vice versa; plan your item sockets before crafting.
- **No duplicate runes across the character** — using Zan in one Runeword locks it out of all others; unique high-value runes become bottlenecks.
- **Cir's exhaustion window wastes Offering generation** — after firing (300 Offering, 5 skills cast), it cannot generate for 3 s; pairing it with a very low-cost Invocation wastes the burst.
- **Igni's timing is easy to misread** — it stores Offering every 0.3 s but only grants it on a non-Basic Skill cast; not a passive drip.
- **Mythic Unique crafting requires specific rune names AND rarities** — substituting a different rarity of the same rune (e.g., Magic Tam instead of Legendary Tam) will not satisfy the recipe.
- **Runewords are Vessel of Hatred exclusive** — characters not on an expansion-enabled account cannot access this system at all.
- **Rune rarity matters for effect strength** — farming or trading for Legendary versions of key runes is required for optimal performance, not just any rarity.
