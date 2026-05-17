# Masterworking

> Season: 13 · Patch: 2.4.1 · Last refreshed: 2026-05-17 · Source: https://maxroll.gg/d4/resources/masterworking-guide

## What it is

Masterworking is an endgame upgrade system accessed at the **Blacksmith** (found in any major Town) that improves base stats and all affix values — including Tempering Affixes — on Legendary, Unique, and Mythic Unique equipment.

*(Season 13, Patch 2.4.1)*

---

## Mechanics

1. Each upgrade attempt adds **1–5 Quality ranks** (random per attempt).
2. Each Quality rank grants **+1% to base Damage, Armor, Resistance, and all affix values**.
3. Maximum Quality rank is **25**, for a total of **+25%** to all stats.
4. At rank 25 the **Capstone Bonus** upgrade becomes available: grants **+50% to a random affix** (can target Tempering Affixes).
5. The Capstone Bonus can be **rerolled indefinitely** until the desired affix is hit.
6. Obducite cost per upgrade follows: `floor(3.75 × CurrentQuality + 10)`.

---

## Costs / requirements

**Materials consumed by Masterworking:**

| Material | Source |
|---|---|
| Obducite | Nightmare Dungeons, Infernal Hordes, Undercity (Tribute of Refinement), Mercenary bartering |
| Veiled Crystal | General drop / salvage |
| Abstruse Sigil | General drop / salvage |
| Forgotten Soul | High item power (800 IP) equipment upgrades |
| Gold | All upgrades |
| Neathiron | Capstone Bonus rerolls only; drops from endgame Bosses |

**Worst-case totals (0 → 25 + Capstone, 2 Quality per upgrade):**

| Item Power | Obducite | Secondary Mat | Abstruse Sigils | Gold |
|---|---|---|---|---|
| 750 (Legendary/Unique) | 862 | 64 Veiled Crystals | 16 | 2,000,000 |
| 800 (Legendary/Unique/Mythic Unique) | 862 | 16 Forgotten Souls | 32 | 2,000,000 |

**Best-case totals (0 → 25 + Capstone, 5 Quality per upgrade):**

| Item Power | Obducite | Secondary Mat | Abstruse Sigils | Gold |
|---|---|---|---|---|
| 750 (Legendary/Unique) | 386 | 36 Veiled Crystals | 9 | 1,125,000 |
| 800 (Legendary/Unique/Mythic Unique) | 386 | 9 Forgotten Souls | 18 | 1,125,000 |

**Capstone Bonus costs:**

| Action | Obducite | Neathiron | Gold |
|---|---|---|---|
| Initial unlock | 150 | — | — |
| Each reroll | 200 | 1 | 1,000,000 |

---

## Recipes / breakpoints / interactions

**Stat scaling formula:**

`Final Value = Base Value × (1 + MW% + Greater Affix bonus% + Capstone bonus%)`

| Scenario | Base | Multiplier | Result |
|---|---|---|---|
| Armor at rank 25 (no bonuses) | 1,509 Armor | ×1.25 | **1,886 Armor** |
| Max Resource (Greater Affix) at rank 25 | 18 | ×(1 + 25% + 50%) | **32** |
| CDR (no Greater Affix) + Capstone at rank 25 | 20% | ×(1 + 25% + 50%) | **35%** |
| CDR (Greater Affix) + Capstone at rank 25 | 20% | ×(1 + 25% + 50% + 50%) | **45%** |

**Key interactions:**
- **Greater Affix (+50%) + Capstone Bonus (+50%) stack multiplicatively** on the same affix — prioritize Capstone landing on a Greater Affix.
- Capstone Bonus **can target Tempering Affixes**.
- Masterworking applies to Legendary, Unique, and Mythic Unique slots only.

---

## Strategy

1. **Farm Obducite first.** Best source: Nightmare Dungeon sigils with the **Treasure Breach** (goblin) affix. Run four goblin NMD sigils in a group rotation for maximum efficiency.
2. **Use Infernal Hordes** as a secondary Obducite source alongside NMDs.
3. **Stockpile Neathiron** from endgame Boss kills before attempting Capstone rerolls — costs can spike if RNG is poor.
4. **Target the Capstone on a Greater Affix** — the combined +50% + +50% bonus (×2.25 total with MW) yields the largest stat swing.
5. **Fully Masterwork gear before pushing the Pit of Artificers** — the +25% baseline alone significantly raises effective power.
6. Accept RNG on upgrade speed (1–5 ranks per attempt); do not craft around hitting specific breakpoints on a schedule.

---

## Pitfalls

- **Rerolling the Capstone is expensive** — each reroll costs 200 Obducite + 1 Neathiron + 1,000,000 Gold. Don't reroll casually on items you may replace.
- **Worst-case upgrade RNG roughly doubles material cost** (386 vs. 862 Obducite) — maintain a buffer before starting.
- **800 IP items cost Forgotten Souls instead of Veiled Crystals** — track which secondary mat your target gear needs before farming.
- **Obducite from Mercenary bartering is the least efficient source** — use it only as a last resort.
- **Masterworking does not apply to non-Legendary/Unique/Mythic Unique items** — wasted materials if attempted on lower rarity gear.
- **Capstone Bonus is random** — there is no guarantee it will land on your best affix without potentially many rerolls.
