# Gems Runes

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-20 · Source: https://maxroll.gg/d4/resources/runewords-overview

## What it is

Runewords are a socketing system introduced in the **Vessel of Hatred** expansion (Season 13, Patch 2.4.1). Each Runeword pairs two runes in the same item — one **Rune of Ritual** (condition/trigger) and one **Rune of Invocation** (effect). The Ritual rune generates a resource called **Offering**; once enough Offering accumulates, the Invocation rune fires. Runes are exclusive to the expansion and cannot coexist with Gems in the same item.

---

## Mechanics

1. **Two rune types:** 15 Runes of Ritual + 26 Runes of Invocation (as of Season 13 Patch 2.4.1; Kel and Zid added in the Season 11 update).
2. **Offering loop:** Ritual rune triggers on a condition → generates Offering → once the Invocation threshold is met → Invocation fires → Offering resets.
3. **Overflow:** If Offering generated exceeds the Invocation cost, the surplus is Overflow. The Invocation's bonus effect scales proportionally to Overflow amount (e.g., extended duration, increased damage).
4. **Cross-class skills:** Invocation runes grant skills from any class regardless of the character's own class.
5. **Three rarities:** Runes drop as Magic, Rare, or Legendary — higher rarity = stronger effect.
6. **Unique constraint:** You cannot use two copies of the same rune across all Runewords on a character.
7. **Gems vs. Runes:** A single item slot cannot hold both Gems and Runes simultaneously.

---

## Costs / requirements

- **Expansion required:** Vessel of Hatred (runes do not exist in base game).
- **Valid item slots:** Helm, Chest, Legs, Two-Handed Weapon (item must have 2 sockets).
- **Storage:** Socketables tab in inventory; runes are tradeable.
- **Crafting (upgrade):** Combine 3 runes of the same name at the Jeweler → receive 1 random rune.
- **Mythic Unique crafting cost (general formula):** 6 Legendary Runes + 6 Rare Runes + 6 Magic Runes (specific names) + 2 Resplendent Spark.

---

## Recipes / breakpoints / interactions

### Runes of Ritual — Offering generation

| Rune | Trigger condition | Offering generated |
|------|------------------|--------------------|
| Bac | Travel 25 meters | 400 Offering |
| Igni | Non-Basic Skill cast (stores every 0.3 s) | 25 Offering |
| Zan | Ultimate Skill cast | 200 Offering |
| Cem | Evade cast | 75 Offering |
| Cir | Cast 5 skills (then exhausted 3 s) | 300 Offering |
| Moni | Cast 2 Mobility or Macabre skills | 100 Offering |
| Nagu | Maintain ≥1 active summon for 5 s (up to 5 summons) | 100 Offering per summon |
| Noc | Inflict Crowd Control (double if not Slow/Chill) | 5 Offering (10 for hard CC) |
| Poc | Spend 5% of max Resource | 5 Offering |
| Tam | Cast non-Channeled Core Skill | 25 Offering |

> More demanding Ritual conditions generally yield higher Offering per trigger.

### Runes of Invocation — Offering cost & effect

| Rune | Offering cost | Invoked skill / effect | Source class | Cooldown | Overflow bonus |
|------|--------------|----------------------|-------------|---------|---------------|
| Eom | 100 | Reduce active cooldowns by 0.1 s | — | 1 s | Further cooldown reduction |
| Gar | 25 | +2% Crit Strike Chance for 5 s (stacks to 10%) | — | — | (not covered in source) |
| Qua | 50 | +10% Movement Speed for 5 s (stacks to 50%) | — | 1 s | Increased duration |
| Vex | 100 | +1 to all Skills for 10 s | — | — | Up to +3 Skill ranks |
| Wat | 100 | Horrid Decrepify — weakens & slows enemies | Necromancer | 1 s | Increased duration |
| Teb | 100 | Abhorrent Iron Maiden — DoT + counterattack | Necromancer | 1 s | +1% damage per Offering |
| Tzic | 200 | Concussive Stomp — damage + Knock Down | Spiritborn | 1 s | +1% damage per Offering |
| Thul | 250 | Frost Nova — freeze nearby enemies | Sorcerer | 2 s | Increased AoE size |
| Prid | 250 | Dark Prison — tether enemies for 3 s | Warlock | 3 s | Increased duration |
| Que | 300 | Earthen Bulwark — Barrier for 3 s | Druid | 1 s | Increased duration |
| Kry | 300 | Vortex — damage + Pull In enemies | Spiritborn | — | (not covered in source) |
| Lac | 400 | Challenging Shout — taunt + reduce damage taken 3 s | Barbarian | — | (not covered in source) |
| Jah | 400* | Replace next Evade with Teleport (Unstoppable, deals damage) | Sorcerer | — | (not covered in source) |
| Yom | 500 | Petrify — stun enemies + restore 100 Resource | Druid | 5 s | Increased Stun duration |
| Kel | 500 | Rally — grant Resource + Movement Speed for 8 s | Paladin | — | (not covered in source) |
| Ner | 600 | Concealment — Unstoppable + Stealth for 5 s + Movement Speed | Rogue | 6 s | Increased duration |
| Ohm | 600 | War Cry — +7.5% damage for 6 s | Barbarian | — | (not covered in source) |

*BacJah pairing specifically notes 400 Offering from 25 m travel via Bac triggering Jah.

### Notable Runeword pairings

| Runeword | Ritual rune | Invocation rune | Combined effect |
|----------|------------|----------------|----------------|
| BacJah | Bac (travel 25 m → 400 Offering) | Jah | Next Evade replaced with Sorcerer Teleport |

### Mythic Unique recipe example

| Item | Components |
|------|-----------|
| Andariel's Visage | 6× Tam (Legendary) + 6× Qax + 6× Zan + 2× Resplendent Spark |

---

## Strategy

1. **Match Offering rate to Invocation cost.** Pair fast-generating Ritual runes (Poc, Noc) with low-cost Invocations (Gar, Qua, Eom) for near-constant uptime; pair burst generators (Zan, Cir) with expensive Invocations (Yom, Ner, Ohm).
2. **Exploit Overflow for bonus scaling.** Choose Ritual runes that regularly overshoot the Invocation threshold — e.g., Zan (200 Offering) into Teb or Wat (100 cost) guarantees Overflow and the damage/duration bonus every Ultimate cast.
3. **Target cross-class utility you otherwise lack.** Use Invocations to fill defensive gaps (Que for Barrier, Mot for damage mitigation via Dark Shroud, Ner for Unstoppable) regardless of your class.
4. **Summon builds: stack Nagu.** Nagu generates 100 Offering per active summon (up to 5 summons) every 5 s, making it extremely high throughput for Necromancer or Druid; pair with Ceh or other moderate-cost Invocations.
5. **Mobility builds: BacJah.** Moving 25 m charges 400 Offering, replacing Evade with Teleport — strong on any build that moves constantly through dense maps.
6. **Plan rune uniqueness.** You cannot duplicate runes across all equipped Runewords; build your full socket loadout before farming to avoid wasted effort.
7. **Prioritize higher-rarity runes for key slots.** Legendary runes provide the strongest effects; target Legendary versions of your core Ritual/Invocation pair for your main item slot.

---

## Pitfalls

- **Gems and Runes are mutually exclusive per item** — socketing Runes in an item removes the option to use Gems in that same slot; plan your item setup deliberately.
- **Duplicate rune restriction** — equipping the same rune name in two different Runewords is not allowed; verify your full loadout before crafting or trading.
- **Invocation Cooldown gates re-trigger** — several Invocations have independent cooldowns (e.g., Yom 5 s, Ner 6 s); excess Offering generated during cooldown does not queue another trigger, potentially wasting fast-generating Ritual runes.
- **Cir exhaustion window** — Cir becomes exhausted for 3 s after awarding its 300 Offering; builds relying on rapid skill spam may find the downtime punishing.
- **Crafting is non-deterministic** — combining 3 identical runes at the Jeweler gives a *random* rune, not a guaranteed upgrade of that name; don't burn rare runes expecting a specific result.
- **Expansion-locked** — Runes only drop and function if Vessel of Hatred is owned; they do not appear for base-game-only accounts.
- **Item socket requirement** — valid slots (Helm, Chest, Legs, 2H Weapon) must already have 2 sockets; not all items of those types roll with 2 sockets by default.
