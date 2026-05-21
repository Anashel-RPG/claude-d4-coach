# Masterworking

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-21 · Source: https://maxroll.gg/d4/resources/masterworking-guide

## What it is

Masterworking is an endgame crafting system accessed at the **Blacksmith** (found in any major Town) that improves the quality of affixes — including Tempering Affixes — on **Legendary**, **Unique**, and **Mythic Unique** equipment. Max rank is **25**, after which a **Capstone Bonus** upgrade becomes available.

---

## Mechanics

1. Each upgrade attempt grants **1–5 Quality ranks** randomly (not 1 rank guaranteed).
2. Every Quality rank increases **base Damage, Armor, Resistance, and all affix values by +1% per rank**.
3. At rank 25 the cumulative bonus is **+25%** to all stats and affixes on the item.
4. Reaching rank 25 unlocks the **Capstone Bonus** upgrade: grants **+50% to a random affix** (can target Tempering Affixes).
5. Obducite cost per individual upgrade = **floor(3.75 × CurrentQuality + 10)**.
6. The Capstone Bonus can be **rerolled indefinitely** until it lands on the desired affix, at additional cost each attempt.

---

## Costs / requirements

**Per-rank material requirements by item power:**

| Item Power | Secondary Material | Notes |
|---|---|---|
| 750 (Legendary/Unique) | Veiled Crystals | — |
| 800 (Legendary/Unique/Mythic Unique) | Forgotten Souls | Higher tier material |

**All items also require:** Obducite + Gold for every rank upgrade.  
**Abstruse Sigils** are required at both item power tiers.

**Total 0 → 25 cost (including Capstone unlock):**

| Item Power | Scenario | Obducite | Secondary Mat | Abstruse Sigils | Gold |
|---|---|---|---|---|---|
| 750 | Best case (5 Quality/upgrade) | 386 | 36 Veiled Crystals | 9 | 1,125,000 |
| 750 | Worst case (2 Quality/upgrade) | 862 | 64 Veiled Crystals | 16 | 2,000,000 |
| 800 | Best case (5 Quality/upgrade) | 386 | 9 Forgotten Souls | 18 Abstruse Sigils | 1,125,000 |
| 800 | Worst case (2 Quality/upgrade) | 862 | 16 Forgotten Souls | 32 Abstruse Sigils | 2,000,000 |

**Capstone Bonus:**

| Action | Cost |
|---|---|
| Unlock (at rank 25) | 150 Obducite |
| Reroll | 200 Obducite + 1 Neathiron + 1,000,000 Gold |

---

## Recipes / breakpoints / interactions

**Obducite cost formula:** `floor(3.75 × CurrentQuality + 10)` per upgrade attempt.

**Key stat breakpoint — rank 25 with Greater Affix + Capstone on same affix:**

| Affix | Base | MW +25% | +50% Greater Affix | +50% Capstone | Final |
|---|---|---|---|---|---|
| Max Resource (example) | 18 | × 1.25 | stacked | stacked | 32 |

- **Greater Affix (+50%) and Capstone Bonus (+50%) stack multiplicatively** when both target the same affix.
- Formula for above example: `18 × (1 + 25% + 50%) = 32` (MW bonus + Capstone, no Greater Affix in that case).
- Capstone Bonus **can target Tempering Affixes**.
- Masterworking **also scales Tempering Affix values** by +1% per rank like any other affix.

**Obducite sources (priority order):**

| Priority | Source | Notes |
|---|---|---|
| 1 (Best) | Nightmare Dungeon with **Treasure Breach** affix sigil (goblin NMD) | Highest yield |
| 2 | Nightmare Dungeon Strongroom Chests | Via NMD sigil affixes |
| 3 | Infernal Hordes | Reliable secondary source |
| 4 | Undercity | Requires Tribute of Refinement |
| 5 (Lowest) | Mercenary Bartering (Masterworking Cache) | Least efficient |

**Neathiron source:** Endgame bosses throughout Sanctuary.

---

## Strategy

1. **Prioritize item power 800 gear** before investing heavy Masterworking resources — item power affects secondary material tier (Veiled Crystals vs. Forgotten Souls but total Obducite cost is the same).
2. **Farm Nightmare Dungeons with the Treasure Breach sigil affix** first for Obducite — it is the most efficient source by a significant margin.
3. **Temper your item before Masterworking** — confirmed crafting order is: socket → Masterwork → Temper (Tempering Affixes also benefit from +1% per MW rank, so MW before final Temper locks in scaling).
4. **Target the Capstone Bonus on your highest-value affix**, especially if it already has a Greater Affix roll — the +50% Capstone stacks with the +50% Greater Affix for maximum gain.
5. **Reroll the Capstone indefinitely** if needed; the cost per reroll (200 Obducite + 1 Neathiron + 1M Gold) is worth it to land on a priority affix or Tempering Affix.
6. **Budget for worst-case costs**: plan for up to 862 Obducite and 2,000,000 Gold per item — RNG can give as few as 2 Quality ranks per upgrade.

---

## Pitfalls

- **Upgrade Quality is random (1–5 per attempt)** — budget for worst case (2 Quality/upgrade = 2.2× more upgrades than best case).
- **Dismantling a Masterworked item returns only a small fraction of Obducite spent** — do not Masterwork items you plan to replace soon.
- **Capstone Bonus targets a random affix** — without rerolling, it may land on a low-value stat; rerolls cost Neathiron (endgame boss drops only).
- **Mercenary Bartering for Obducite is the lowest-priority source** — do not rely on it as a primary farm method.
- **Undercity requires Tribute of Refinement** to yield Obducite — not a free-to-run source.
- **Item power tier changes the secondary material required** (Veiled Crystals at 750 vs. Forgotten Souls at 800) — stockpiling the wrong material wastes resources if you upgrade gear tiers.
