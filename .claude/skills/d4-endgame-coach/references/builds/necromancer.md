# Necromancer — Full Minion Army (flagship endgame build)

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## What this build is
The defining Season 13 Necromancer: a maximized **minion army** that floods the screen with Skeletal Warriors, Skeletal Mages, and the Golem, then amplifies them through Book of the Dead choices and minion-damage gear. **Corpse Explosion** detonates the bodies your army leaves behind, **Decrepify** curses packs, and **Blood Wave** is the ultimate. You direct traffic while the army does the killing — very tanky, very hands-off. Scales off Intelligence.

## Skill bar
| Skill | Role |
|---|---|
| Raise Skeleton (Skeletal Warriors) | Summon — frontline melee army |
| Skeletal Mage | Summon — ranged damage layer |
| Golem | Summon — tank / AoE bruiser |
| Corpse Explosion | Corpse spender — detonates army's kills for AoE |
| Decrepify | Curse — DR + slow on packs (also a resource/CDR engine) |
| Blood Wave | Ultimate — burst AoE + boss damage |

## Key passive / class mechanic
- **Class mechanic:** Book of the Dead — pick the Warrior / Mage / Golem variants that maximize army output (DPS-leaning, not sacrifice). Minions inherit a share of your stats, so your gear directly scales the army's damage.
- **Key passive:** confirm the exact key passive this build runs with `graph_build("full-minion-army")`. See `references/classes/necromancer.md` for the full key-passive breakdown.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("full-minion-army")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## How to play
Keep the full army summoned (Warriors + Mages + Golem) at all times — if any die, resummon immediately. Curse packs with Decrepify before engaging so the DR and slow are active when minions arrive. Let the army kill; chain Corpse Explosion off the resulting corpses for AoE cleanup. Blood Wave on Elites and bosses for burst.

Your role is **traffic controller**: position the army into melee range, keep Decrepify cycling, and drop Corpse Explosion on dense corpse clusters. The minions carry the damage — your gear investment should prioritize what scales them (minion damage, the summoner amulet slot, and Intelligence as the primary stat).

**Hellbent Commander** is the amulet-slot payoff that most changes the feel of this build — once it's in place and the full army is alive, the damage spike is substantial. Always check that all three summon types are active before evaluating damage output; even one missing minion type drops DPS measurably.

## Priority sequencing
1. Get all three summon types on the bar and summoned before worrying about gear.
2. Finish the class quest (~L25) to unlock the Golem — the army is incomplete without it.
3. Fill the amulet slot (summoner payoff) as the first priority upgrade.
4. Gear Intelligence as the primary offensive stat; minions scale from your sheet.
5. Paragon boards and glyphs after gear slots are stable — confirm exact board order with `graph_build("full-minion-army")`.

## Verify live
This is curated coaching context. For the full current loadout (including paragon nodes, glyphs, charms/seal, and Book of the Dead picks) call `graph_build("full-minion-army")`; diff against the player's actual gear (ask them to paste or describe it).
