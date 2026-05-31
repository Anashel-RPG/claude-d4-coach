# `d4-mcp` — full tool reference

The coach is backed by **`d4-mcp`** (`https://mcp-d4.anashel.com/mcp`), a free hosted service that ships **22 tools** across three layers. The repo's `.mcp.json` wires it in automatically — see the [README](../README.md) for setup and the public-key details.

Current data (Season 13 / Patch 2.4): **65,356** graph relations across **100+ endgame builds**, all 8 classes; a game-data corpus of **389 items**, **416 affixes**, **2,845 item-affix tooltips**, **234 skills**, **600+ aspect effects**, and **85 recipes**.

---

## Layer 1 · Calculators (5) — Diablo IV's real equations

Deterministic math on real game values, not rules of thumb. Season-tuned constants (armor K-value, recipe costs) are approximations each tool flags for you to confirm in-game.

| Tool | What it computes |
|---|---|
| `compute_dps` | Effective DPS in D4's actual damage model: base × (1 + additive %) × each independent multiplicative bucket × crit × Vulnerable. Surfaces which bucket is empty (your biggest gain). |
| `armor_breakpoint` | Armor needed to hit a target damage-reduction %, using the real curve `DR = armor / (armor + K(level))`. |
| `glyph_xp_time` | How many Nightmare Dungeon / Pit runs to take a glyph to a target level. |
| `recipe_cost` | Total materials for *N* crafts of a Horadric Cube recipe. |
| `bucket_compare` | Given two candidate upgrades, which adds more *effective* damage — accounts for which bucket each one lands in. |

## Layer 2 · Game-data corpus (13) — extracted from D4's own files

Exact item stats, effect text, and roll ranges — the factual backbone.

| Tool | Returns |
|---|---|
| `lookup_item` | Item by name/ID: type, class, rarity, item-power range, and (for uniques/legendaries) the legendary affix text with min/max value ranges. |
| `lookup_aspect` | Aspect by name/ID: class restriction, allowed slots, and resolved effect text with values. |
| `lookup_power` | Skill/power: damage type, resource cost, cooldown, channeled/ultimate/passive flags, tags. |
| `lookup_affix` | Affix: stat roll ranges and the item types it can appear on. |
| `lookup_item_type` | Item-type metadata: weapon class, body slots, enchantment cost. |
| `lookup_recipe` | Horadric Cube recipe details. |
| `search_corpus` | Fuzzy substring search across every entity — find the exact name first, then `lookup_*`. |
| `class_roster` | Summary roster for a class. |
| `affix_pool` | What stats can roll on a given slot (optionally filtered by class). |
| `d4_list_types` | List every data table with row counts. |
| `d4_schema` | Columns of a given table. |
| `d4_sample` | A few sample rows from a table. |
| `d4_query` | Filtered analytical query over the corpus (whitelisted operators only). |

## Layer 3 · Knowledge graph (4) — how it all fits together

Build → gear → aspect → skill → paragon → charm relationships, crawled from current-season endgame builds.

| Tool | Returns |
|---|---|
| `graph_build` | The full graph for a build: every gear slot (with variants), aspect, skill, paragon board, and charm it `REQUIRES`/`SLOTS_IN`. The authority for a build's actual loadout. |
| `graph_entity` | Every relation involving one entity, in `Type:Name` form (e.g. `Unique:Herald's Morningstar`), incoming and outgoing. |
| `graph_search` | Filtered search by predicate, entity type, keyword, or minimum confidence. |
| `graph_stats` | Overview: total relations, breakdown by predicate and entity type, and the most-connected entities. |

---

## How the coach uses them

The harness doesn't just *have* these tools — it's instructed when to reach for each (see the skill's `mcp.md` and `SKILL.md`):

- **Graph before opinion** — call `graph_build` / `graph_entity` before stating a build's loadout; never recite it from memory.
- **Corpus before classification** — `lookup_aspect` / `lookup_item` before calling an aspect offensive or defensive; slot doesn't imply function.
- **Calculators for any non-trivial math** — more than 2–3 multiplier sources → `compute_dps`; two upgrades head-to-head → `bucket_compare`. Don't multiply by hand.
- **Validate before shipping** — every named entity in a generated report is checked back against the graph by [`tools/validate-report.py`](../tools/validate-report.py).

> All data is presented as the coach's own synthesis over the `d4-mcp` graph. The service credits its data layer; it never fabricates a citation to a specific guide or creator.
