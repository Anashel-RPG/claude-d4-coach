# Rogue

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Core identity
Agile melee/ranged hybrid that spends Energy on Core skills and layers Imbuements (Cold/Poison/Shadow) for elemental conversion and chain effects. A swappable Specialization (Combo Points / Inner Sight / Preparation) is the class signature. Damage is highly conditional — Vulnerable, Crit, and positioning gate most multipliers — so Rogue rewards setup and decision-making over face-tanking.

## Damage scaling buckets
- **Multiplicative sources:** Key Passives (Momentum, Precision, Victimize, Close Quarters Combat), Combo-Point–empowered Core skills, Imbuement potency, resource-spend multipliers, basic-attack engines, cast-then-detonate effects, Frigid Finesse vs Chilled/Frozen targets. Critical and Vulnerable are their own separate buckets.
- **Additive sources:** Dexterity (skill damage), Intelligence (crit chance + resistance), Core/Marksman/Cutthroat skill-damage tempers, additive damage paragon rares, passive bonuses from the tree.
- **Critical / Vulnerable / Overpower hooks:** Vulnerable is the central gate — it enables the Victimize AoE proc and powers several key passives; confirm how your specific build applies it via `graph_build`. Overpower is generally ignored (Willpower scales it, but Rogue prioritizes Dex/Int).

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|
| Heartseeker | Core / Marksman | Auto-seeks, ramps attack speed + Crit, applies Vulnerable; carries the top endgame build |
| Dance of Knives | Core / channel | Spin-to-win clear engine; the other top S13 ladder build |
| Twisting Blades | Core / melee | High ceiling; reposition so returning blades route back through packs |
| Flurry | Core / melee AoE | Hits multiple times per cast; superb Imbuement and Lucky-Hit vehicle |
| Barrage / Rapid Fire / Penetrating Shot | Core / ranged | Barrage = Lucky-Hit AoE, Rapid Fire = single-target boss, Penetrating Shot = line clear |
| Puncture | Basic / utility | Vulnerable + slow + Energy refund; cheap Combo-Point generator |
| Dash / Shadow Step | Mobility | Near-universal; Shadow Step pairs with melee cores |
| Dark Shroud | Defense | Stacking damage reduction + movement; the Rogue survival backbone |
| Smoke Grenade | CC / debuff | On-demand Daze; amplifies damage dealt inside the cloud |
| Concealment | Utility | Movement + Energy + guaranteed ambush Crit; Unstoppable cleanse |
| Caltrops | Slow / trap | Slows + (Enhanced) Vulnerable; feeds Trap and Cold builds |
| Cold / Poison / Shadow Imbuement | Element layer | Cold = Chill/Freeze + Frigid Finesse multiplier, Poison = DoT (best on multi-hit skills), Shadow = chain AoE |
| Death Trap / Rain of Arrows / Shadow Clone | Ultimate | Death Trap pairs with Exposure/Preparation; Shadow Clone underwhelms at endgame |

## Key passives / class mechanic
**Key Passives (choose one):**
- **Momentum** — stacks from Cutthroat skills for a large additive/multiplier; strong early, scales poorly late.
- **Close Quarters Combat** — needs both Cutthroat + Marksman stacks held; attack-speed + damage steroid that scales with close-range damage.
- **Precision** — Marksman only; 3 stacks makes the next Core/Ultimate Marksman skill a guaranteed Crit with a big multiplier. Backbone of Heartseeker.
- **Victimize** — best AoE scaler; Vulnerable hits proc an area explosion.
- **Exposure** — Trapper enabler; spending/triggering rapidly cools down traps and caltrops.
- **Alchemical Admixture** — Imbuement enabler; running two active elements raises all Imbuement potency.

**Specialization (class mechanic, unlocked ~L15 via the "True Potential" quest, swappable anytime — even mid-fight):**
- **Combo Points** — Basic skills bank up to 3 points to empower the next Core skill (more damage + a per-skill bonus). Default for most spender builds.
- **Inner Sight** — filling the gauge on a marked enemy grants a window of free, unlimited-Energy casting; weak against tanky solo bosses that can't refill it fast.
- **Preparation** — spending Energy cuts the Ultimate cooldown; using the Ultimate resets other skills. Pairs with Death Trap / high-attack-speed loops.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("dance-of-knives")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Stat priorities (prose guidance — exact numbers from `graph_build`)
Dexterity is the primary offensive stat for virtually every Rogue build and should be maximized on every piece possible. Intelligence follows as the secondary offensive attribute (crit chance + resistances). After those two: stack the damage multiplier that matches your key passive and spender — Vulnerable damage if running Victimize, Critical Strike Damage if running Precision, close-range damage if running Close Quarters Combat. Survival stats (max life, armor, resistances) are secondary but required for higher Pit tiers; Dark Shroud uptime supplements them rather than replacing them.

Avoid stacking Willpower or Overpower investment — Rogue's Overpower scaling is poor relative to the Dexterity payoff, and those stats compete for the same gear budget.

## Tempering and masterworking guidance
Tempering priorities flow from your spender tag and key passive. Match the skill-damage temper to your Core skill's tag (Marksman, Cutthroat, or the skill-specific option). On weapons, lead with the damage multiplier that fills your biggest bucket; on armor, prioritize defensive stats that let you survive the tier before layering more offense. Confirm exact temper options for each slot with `lookup_item` or `lookup_aspect` at runtime — temper pools are slot-specific and can change between patches.

Masterworking: crit-upgrade the stat that multiplies your largest existing bucket first. For most Rogue builds that means the offensive skill-damage temper on your weapons, then Crit/Vulnerable damage on the gear pieces where those rolled. Confirm which stats are on your specific piece before committing masterworking materials — a well-rolled affix is worth more than a mediocre one at a higher upgrade tier.

## Mercenary pairing
- **Hire:** Raheir — taunt + Fortify + armor uptime is the standard pick to smooth Rogue's squishy frame.
- **Reinforce:** Subo — pull + Vulnerable utility feeds Victimize and the Vulnerable bucket.

## Common mistakes
- Running Inner Sight in high Pit tiers where bosses are too tanky to refill the gauge — Combo Points or Preparation usually win there.
- Forgetting to reposition after Twisting Blades — the returning blades must pass back through enemies to deal damage.
- Leaning on Shadow Clone at endgame — it ignores most of your damage modifiers.
- Neglecting the off-hand weapon slot (ranged on a melee build or vice versa) — all equipped weapon stats always apply.
- Stacking Willpower/Overpower on a Rogue — Dexterity and Intelligence are the offensive attributes for nearly every build.
- Leaving the Specialization on the wrong mode for the content — it's free to swap, even mid-fight.
