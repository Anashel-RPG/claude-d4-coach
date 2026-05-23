# Masterworking

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-23 · Source: https://maxroll.gg/d4/resources/masterworking-guide

## What it is

Masterworking is an endgame crafting system accessed at the **Blacksmith** (found in any major Town) that increases the quality of affixes — including Tempering Affixes — on **Legendary**, **Unique**, and **Mythic Unique** equipment. Maximum Quality rank is **25**, after which a Capstone Bonus upgrade becomes available.

---

## Mechanics

1. Each upgrade attempt adds a **random 2–5 Quality ranks** to the item (minimum 2, maximum 5).
2. Every Quality rank increases base **Damage**, **Armor**, **Resistance**, and **all affix values** (including Tempering Affixes) by **+1% per rank** — reaching **+25% total at rank 25**.
3. Obducite cost per upgrade follows the formula: **floor(3.75 × CurrentQuality + 10)**.
4. At rank 25, the **Capstone Bonus** upgrade unlocks — it applies a **+50% bonus** to one random affix (can target Tempering Affixes).
5. The Capstone Bonus can be **rerolled indefinitely** until it lands on the desired affix.
6. The Capstone **+50%** stacks with the **Greater Affix +50%** bonus on the same affix.

**Scaling example (rank 25, no Capstone):**  
A base 18 Max Resource Greater Affix scales to **32** — `18 × (1 + 25% + 50%)`.

---

## Costs / requirements

**Materials required by item power tier:**

| Item Power | Crystal Material | Soul Material |
|---|---|---|
| 750 (Legendary/Unique) | Veiled Crystals | Abstruse Sigils |
| 800 (Legendary/Unique/Mythic Unique) | Abstruse Sigils | Forgotten Souls |

All tiers also consume **Obducite** and **Gold**.

**Total 0→25 cost (including Capstone unlock):**

| Item Power | Case | Obducite | Crystal/Soul Mat | Sigil/Soul Mat | Gold |
|---|---|---|---|---|---|
| 750 | Best (5/upgrade) | 386 | 36 Veiled Crystals | 9 Abstruse Sigils | 1,125,000 |
| 750 | Worst (2/upgrade) | 862 | 64 Veiled Crystals | 16 Abstruse Sigils | 2,000,000 |
| 800 | Best (5/upgrade) | 386 | 9 Forgotten Souls | 18 Abstruse Sigils | 1,125,000 |
| 800 | Worst (2/upgrade) | 862 | 16 Forgotten Souls | 32 Abstruse Sigils | 2,000,000 |

**Capstone Bonus costs:**

| Action | Obducite | Neathiron | Gold |
|---|---|---|---|
| Unlock (rank 25) | 150 | — | — |
| Reroll | 200 | 1 | 1,000,000 |

**Neathiron** is gathered from endgame bosses throughout Sanctuary.

---

## Recipes / breakpoints / interactions

| Breakpoint / Interaction | Detail |
|---|---|
| Obducite cost formula | `floor(3.75 × CurrentQuality + 10)` per upgrade |
| Rank 25 total stat bonus | +25% to base Damage, Armor, Resistance, and all affixes |
| Capstone Bonus | +50% to one random affix (can target Tempering Affixes); rerollable |
| Capstone + Greater Affix stack | Capstone +50% stacks multiplicatively with Greater Affix +50% on the same affix |
| Greater Affix example | 18 Max Resource → **32** at rank 25 with Greater Affix (no Capstone) |
| Upgrade randomness | 2–5 Quality ranks granted per upgrade attempt |

**Obducite sources (priority order):**

| Priority | Source |
|---|---|
| 1 (Best) | Nightmare Dungeon with **Treasure Breach** affix (goblin NMD sigil) |
| 2 | Strongroom Chests via Nightmare Dungeon sigil affixes |
| 3 | Undercity with **Tribute of Refinement** |
| 4 | Infernal Hordes |
| 5 (Lowest) | Mercenary Bartering (Masterworking Cache) |

---

## Strategy

1. **Prioritize Greater Affixes** on the target slot before Masterworking — the Capstone stacks with them for maximum value.
2. **Farm NMD goblin sigils** (Treasure Breach affix) as your primary Obducite source; supplement with Undercity Tribute of Refinement runs.
3. **Socket your item before Masterworking** — complete all socketing and Tempering first, then Masterwork.
4. **Target Capstone on your highest-value affix** — reroll using Neathiron (from endgame bosses) until it lands on the desired stat.
5. **Budget for worst-case costs** — a bad-luck run (2 Quality/upgrade) costs over 2× the Obducite of a best-case run; stockpile before committing to a full 0→25 upgrade.
6. **Reserve Neathiron** — only endgame bosses drop it; don't waste Capstone rerolls on non-Greater Affix slots.

---

## Pitfalls

- **Randomness can double your Obducite cost** — worst-case (2/upgrade) requires 862 Obducite vs. 386 for best-case; never assume best-case when planning material farming.
- **Dismantling a Masterworked item returns only a small fraction of Obducite spent** — do not Masterwork items you aren't confident in keeping.
- **Capstone Bonus is random** — failing to budget Neathiron for rerolls leaves you with a wasted +50% on a low-value affix.
- **Item power tier changes the secondary material** — 800-power items require Forgotten Souls (not Veiled Crystals); confirm your item's power before farming materials.
- **Neathiron is gated behind endgame bosses** — it is not available from standard dungeon content; plan boss kill routes if heavy Capstone rerolling is expected.
- **Bartering for Obducite via Mercenaries is lowest priority** — treat it as a fallback only, not a primary farm.
