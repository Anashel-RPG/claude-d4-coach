# Masterworking

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-16 · Source: https://maxroll.gg/d4/resources/masterworking-guide

## What it is

Masterworking is an endgame upgrade system at the **Blacksmith** (found in any major Town) that improves affix values — including Tempering Affixes — on eligible equipment. Available in Season 13 / Patch 2.4.1.

**Eligible items:** Legendary, Unique, Mythic Unique

---

## Mechanics

1. Each Masterworking upgrade grants **1–5 Quality ranks** at once (random).
2. Every Quality rank increases base Damage, Armor, Resistance, and **all affix values by +1% per rank**.
3. Maximum Quality rank is **25**, giving a total **+25%** to all affix values.
4. At rank 25, the **Capstone Bonus** unlocks — a **+50% bonus** applied to one random affix (can target Tempering Affixes).
5. The Capstone Bonus is separate from and stacks with the **+50% Greater Affix bonus**.
6. The Capstone Bonus can be **rerolled indefinitely** (each reroll costs resources, see Costs).

**Scaling examples:**

| Scenario | Base | Formula | Result |
|---|---|---|---|
| Armor at rank 25 | 1509 | 1509 × 1.25 | **1886** |
| Max Resource (Greater Affix) + rank 25 + Capstone | 18 | 18 × (1 + 25% + 50% + 50%) | **32** |
| CDR (Greater Affix) + rank 25 + Capstone | 20% | 20% × (1 + 25% + 50% + 50%) | **45%** |
| CDR (standard affix) + rank 25 + Capstone | 20% | 20% × (1 + 25% + 50%) | **35%** |

---

## Costs / requirements

**Per upgrade — Obducite cost formula:** `floor(3.75 × CurrentQuality + 10)`

| Quality → | 0 | ... | 24 |
|---|---|---|---|
| Obducite | 10 | scales linearly | 100 |

**Additional materials per upgrade** also include: Gold, Veiled Crystals, Abstruse Sigils, Forgotten Souls (amount varies by item power tier — see breakpoints below).

**Capstone Bonus unlock (rank 25):** 150 Obducite

**Capstone Bonus reroll (per attempt):** 200 Obducite + 1 Neathiron + 1,000,000 Gold

> Neathiron drops from endgame bosses throughout Sanctuary.

---

## Recipes / breakpoints / interactions

**Full 0→25 + Capstone cost summary (750 item power Legendary/Unique):**

| Scenario | Obducite | Veiled Crystals | Abstruse Sigils | Gold |
|---|---|---|---|---|
| Best case (5 Quality/upgrade) | 386 | 36 | 9 | 1,125,000 |
| Worst case (2 Quality/upgrade) | 862 | 64 | 16 | 2,000,000 |

**Full 0→25 + Capstone cost summary (800 item power Legendary/Unique/Mythic Unique):**

| Scenario | Obducite | Forgotten Souls | Abstruse Sigils | Gold |
|---|---|---|---|---|
| Best case (5 Quality/upgrade) | 386 | 9 | 18 | 1,125,000 |
| Worst case (2 Quality/upgrade) | 862 | 16 | 32 | 2,000,000 |

**Key interactions:**
- Capstone Bonus (+50%) stacks **additively** with Greater Affix bonus (+50%) and rank 25 bonus (+25%).
- Capstone can land on any affix slot including Tempering Affixes.
- Rerolling Capstone is unlimited — keep rerolling until the desired affix is targeted.

---

## Strategy

1. **Farm Obducite efficiently** — best source is a Nightmare Dungeon sigil with the **Treasure Breach** affix (goblin NMD). Second-best is an NMD sigil with the **Strongroom Chest** affix.
2. **Run goblin NMDs in a group rotation** with four goblin sigils for maximum Obducite throughput.
3. **Supplement Obducite** via Undercity runs with Tribute of Refinement, Infernal Hordes, and mercenary bartering.
4. **Prioritize the Capstone Bonus target** — decide which affix you want the +50% on before spending Neathiron on rerolls; Greater Affixes benefit most (double +50% stack).
5. **Upgrade order** — fully Masterwork your best-in-slot pieces rather than spreading resources across many items; rank 25 + Capstone is a massive breakpoint.
6. **Material check before starting** — worst-case runs cost nearly 2.25× the Obducite of best-case; stockpile before committing to a piece.

---

## Pitfalls

- **Rank gain is random (1–5 per upgrade)** — budget for worst-case (2/upgrade ≈ 12 upgrades to reach rank 25) to avoid running out of materials mid-progression.
- **Capstone Bonus targets a random affix** — if it lands on a low-value affix, rerolls cost 200 Obducite + 1 Neathiron + 1,000,000 Gold each; these costs add up quickly.
- **Neathiron is a bottleneck** — only obtainable from endgame bosses; running out blocks Capstone rerolls entirely.
- **Item power tier changes the material type** — 750 IP uses Veiled Crystals; 800 IP uses Forgotten Souls. Using the wrong tier item wastes the wrong material pool.
- **Do not Masterwork a piece you plan to replace** — all ranks and the Capstone are lost when swapping items; upgrade only gear you intend to keep.
- **Gold drain is significant** — worst-case 800 IP runs to 2,000,000 Gold before any Capstone rerolls; Gold management matters late game.
