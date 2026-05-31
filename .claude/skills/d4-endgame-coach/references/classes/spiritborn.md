# Spiritborn

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Core identity
Vessel-of-Hatred class that channels four Spirit Guardians — Jaguar, Eagle, Gorilla, Centipede — and freely mixes their skills around a chosen primary/secondary spirit (the **Spirit Hall**). Vigor is the resource, built by Basic skills. A durable bruiser by class fantasy: many builds layer Barrier, Resolve, and Thorns while a single Core skill carries the damage.

## Damage scaling buckets
- **Multiplicative sources:** Spirit Hall primary bonuses (Jaguar's Beat Strike stacking, Eagle's Storm Feathers, Gorilla's Barrier/Thorns, Centipede's Poison stacks); Key Passives (Vital Strikes, Noxious Resonance). Critical, Vulnerable, and Overpower are their own separate buckets.
- **Additive sources:** Dexterity (Spiritborn's main offensive attribute — skill damage), spirit-element skill-damage tempers, additive damage paragon rares, Spirit Hall secondary stacking (Ferocity attack speed, Resolve).
- **Critical / Vulnerable / Overpower hooks:** Eagle secondary makes every other cast a guaranteed Crit and grants a Vulnerable-damage window; Eagle skills can apply Vulnerable; Vital Strikes turns Vulnerable into bonus damage + sustain; Noxious Resonance makes Crits consume Poison for burst; Strength → Crit Chance. Willpower (Overpower) is low priority for most Spiritborn builds.

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|
| Thunderspike | Basic — Eagle gen | Applies Vulnerable; the standard generator for Eagle builds |
| Rock Splitter / Thrash / Withering Fist | Basic — alt | Gorilla (thorns/defense), Jaguar (Ferocity/dive), Centipede (poison spread) |
| Quill Volley | Core — Eagle | Strong endgame core; feather volley that overlaps at close range for large single-target |
| Crushing Hand / Rake / Stinger | Core — alt | Gorilla shockwaves, Jaguar Ferocity-spender, Centipede poison AoE |
| Ravager | Focus — Jaguar | Flurry/attack-speed buff; kills extend it (mind boss transitions) |
| Vortex / Soar | Focus — Eagle | Vortex groups packs for AoE; Soar is aerial mobility |
| Armored Hide | Defensive — Gorilla | Big Block + Resolve defensive layer; common even on Eagle builds |
| Counterattack | Defensive — Eagle | Passive dodge + an active full-dodge offensive window |
| Toxic Skin / Scourge | Defensive — Centipede | Passive poison + active sustain/phase utility |
| The Hunter / The Seeker / The Protector / The Devourer | Ultimate | One pick; Jaguar execute, Eagle knockdown+Vulnerable, Gorilla Barrier+AoE, Centipede long poison |

## Key passives / class mechanic
**Spirit Hall (class mechanic):** Unlock the **Primary** spirit ~L15 and the **Secondary** ~L30. The primary spirit makes ALL your skills count as that spirit's type in addition to their own — this is what lets you stack one spirit's bonuses while playing another's skills. Choose primary/secondary to match your damage condition.
- **Jaguar:** primary stacks **Beat Strike** (repeating direct hits build escalating bonus damage, decays if you stop attacking); secondary raises max **Ferocity** (attack speed) and grants it on kill/boss-hit.
- **Eagle:** primary fires **Storm Feathers** (Lightning, applies Vulnerable) from Eagle skills/Evade and boosts movement; secondary makes every other cast a guaranteed Crit plus a Vulnerable-damage window — the backbone of Eagle builds.
- **Gorilla:** primary grants Thorns + a Barrier on Gorilla-skill hits; secondary raises max **Resolve** (DR) and turns high Resolve into Unstoppable — the tanky enabler.
- **Centipede:** primary applies stacking Poison + enemy damage reduction/slow; secondary heals per nearby Poisoned enemy.

**Keywords:** Ferocity (attack speed, Jaguar), Resolve (DR stacks, Gorilla), Storm Feathers (movement → Eagle damage), Pestilent Swarms (Centipede poison).

**Key Passives (choose one):**
- **Vital Strikes** — Vulnerable synergy (bonus damage, healing, Vigor); pairs with the Eagle Vulnerable engine.
- **Noxious Resonance** — Crits consume Poison for burst; the Centipede payoff.
- **Adaptive Stances** — empowers based on the invoked spirit.
- **Prodigy's Tempo** — reward for casting the same skill repeatedly.

## Aspects and uniques — coaching guidance

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("rock-splitter")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

When evaluating which aspects to keep or replace, consider whether the aspect's effect condition is actually met in your rotation (a damage-while-Barrier-active aspect is wasted without reliable Barrier uptime), and whether you're in an additive or multiplicative bucket (multiplicative wins on a well-stacked character; additive is better when that bucket is thin). Use `lookup_aspect` to read exact effect text and confirm roll ranges before swapping.

For uniques: verify with `lookup_item` + `graph_build` before chasing any specific drop. The Spiritborn unique pool is relatively thin — build-confirmed items are the ones to prioritize; treat any other Spiritborn unique as unverified until checked via the graph.

Mythic uniques offer universal offensive and defensive options that benefit multiple Spiritborn archetypes. Confirm which fits the build's condition via `lookup_item` before farming.

## Tempering and masterworking priorities (prose)
Tempering: prioritize the damage tag that matches your spirit/skill type first, then Vulnerable damage, then attack speed or a key defensive stat depending on your survivability gap. Armor slots lean toward Max Life, total armor, and the resource or defensive generation your build depends on.

Masterworking: the highest-value crits land on your primary damage multiplier (the skill tag or spirit element driving your build), then Critical Strike Damage or Vulnerable Damage, then Dexterity or Cooldown Reduction for Ultimate/defensive uptime. The exact picks per slot come from the graph; the ranking above is the tiebreaker logic.

## Paragon approach (prose)
Rush toward Dexterity and skill-damage rare nodes on the starting board to reach the first meaningful legendary node quickly. Board order, glyph choices, and socket positions depend on which archetype you're playing — confirm via `graph_build`. Glyph priority follows the same rule as tempering: damage-amp matched to your spirit first, then Crit/Vulnerable amplification, then survival. Level damage glyphs before survival glyphs unless you're dying on content you should be clearing.

## Mercenary pairing
- Hire: Raheir — taunt + Fortify + armor; smooths Pit pushing even on tanky Spiritborn.
- Reinforce: Subo — pull + Vulnerable, groups packs for AoE Core skills and feeds the Vulnerable damage bucket.

## Season 13 Charms + Seal
Spiritborn fills 6 Charm slots (Charm 1–6) and 1 Seal slot with seasonal items. These are the season's defining multiplier layer — missing or unoptimized charms is a common reason endgame damage plateaus. Confirm exactly which charms and seal the build uses via `graph_build`. (See `references/systems/seasonal-charms.md` for the system.)

## Common mistakes
- Stacking Willpower/Overpower — Dexterity is the offensive attribute for nearly every Spiritborn build.
- Forgetting only one Ultimate and one Key Passive can be equipped at a time.
- Poor positioning on skills whose projectiles or shockwaves must overlap the target for single-target spike damage.
- Letting Beat Strike (Jaguar primary) decay by pausing during a DPS window, or losing the Ravager buff on a boss transition because trash wasn't cleared.
- Picking the primary/secondary spirit that doesn't match your damage condition (Eagle for the Vulnerable/Crit engine, Gorilla for the tanky Resolve layer, Centipede for poison/Noxious Resonance, Jaguar for Ferocity/Beat Strike).
- Leaving the Season 13 Charm/Seal slots empty or unoptimized.
