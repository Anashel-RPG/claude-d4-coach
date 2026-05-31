# Barbarian

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Core identity
Fury-based melee bruiser that equips four weapons at once and swaps between them per skill via the Arsenal System. Physical by default; excels at close-range burst and sustained DPS through Berserking uptime. Stacks more legendary Aspects than any class (four weapon slots), and either spams a Core spender or runs a basic/weapon-throw engine.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("frenzy")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Damage scaling buckets
- **Multiplicative sources:** Berserking (raised cap + larger bonus via Unconstrained, further amplified by Supreme Wrath of the Berserker), Weapon Expertise Rank-10 multipliers for the relevant weapon type, Walking Arsenal, resource-spend multipliers, cast-then-detonate multipliers on gloves, attack-speed ramp via Frenzy stacks, and distance multipliers. Critical and Vulnerable are their own separate buckets.
- **Additive sources:** Strength (skill damage per 100), +Core/+Basic skill damage tempers, additive damage paragon rares, shout damage bonuses, passive skills in the heavy-hitting and critical strike trees.
- **Critical / Vulnerable / Overpower hooks:** Gushing Wounds pairs Crit with Bleed and wants a Crit-Damage mythic 2H; 2H Axe Expertise pays off Vulnerable damage; Vulnerable can be applied by War Cry (Power upgrade), Challenging Shout, and Steel Grasp. Overpower hooks well with Hammer of the Ancients and certain paragon legendaries.

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|
| Lunging Strike | Basic / Fury gen | Mobility, Combat heal, Berserking/Bleed trigger; scales well with basic-attack weapons |
| Flay / Frenzy / Bash | Basic / Fury gen | Flay = Bleed + DR; Frenzy = attack speed via Battle Trance; Bash = Fortify + Overpower guarantee |
| Hammer of the Ancients | Core / primary | Top Overpower-burst core; Violent/Overpower upgrades scale best |
| Whirlwind / Warpath | Core / primary | Fury-efficient sustained channel; great clear, weaker single-target |
| Rallying Cry | Shout | Movement speed, Fury gen, Unstoppable; near-mandatory |
| Challenging Shout | Shout | Extra Life + Damage Reduction; Weaken/Vulnerable support |
| War Cry | Shout | Berserking grant + (Power) Vulnerable; Booming Voice extends all shouts |
| Steel Grasp / Ground Stomp | Utility | Pull + Vulnerable / stun + Fury + Overpower setup |
| Wrath of the Berserker | Ultimate | Most popular endgame ult; Berserking doubling, Unstoppable; Prime/Supreme keys |
| Call of the Ancients | Ultimate (summon) | Brobarian summon variant — Ancients carry the damage |

## Key passives / class mechanic

**Arsenal System:** equips 4 weapons (2H Bludgeoning + 2H Slashing + two 1H), auto-swapped by skill type. Each weapon type has a Weapon Expertise bonus that activates when that weapon attacks; Expertise ranks 1–10 via on-hit XP, Rank 10 unlocks an extra bonus. Only the Arsenal-assigned weapon's DPS feeds a given skill — the others are stat sticks.

**Technique Slot** (unlocked via Dry Steppes quest around level 15): grants one chosen Weapon Expertise bonus permanently regardless of active weapon. Common pick rationale: 2H Sword adds Bleed across all attacks; 2H Axe adds a Vulnerable damage multiplier. Choose based on whether your build's primary damage source is Bleed or Vulnerable.

**Weapon Expertise trade-offs:** 1H weapons tend to provide attack speed and Berserking synergies; 2H weapons provide Crit or Vulnerable payoff. Confirm Rank-10 bonuses for your specific Arsenal via `lookup_item_type` or `d4_query`.

**Key Passives — when to pick each:**
- **Unconstrained** — best when Berserking uptime is very high (triple-shout builds, Frenzy). The raised Berserking damage cap and duration extension reward builds that sustain Berserking near-permanently.
- **Unbridled Rage** — best when you have strong Fury generation and spam a Core skill. The extra Fury cost punishes low-resource setups severely; do not pick this without solving Fury generation first.
- **Walking Arsenal** — best for builds rotating through all weapon types naturally. Rewards diverse Arsenal use; punishes builds that lock onto one weapon type.
- **Gushing Wounds** — best for dedicated Bleed/Crit builds with a Crit-Damage mythic 2H. Without full Crit investment it underperforms every other key passive.
- **Resolve** via Glynn's Anvil aspect — supplements any key passive as a pure DR floor; not a primary damage passive, and treating it as one is a common mistake.

## Aspects (legendary) — coaching notes
Use `lookup_aspect` for exact effect text and roll ranges; do not rely on memory for numbers. General selection logic:

- Weapon slots hold the build's most impactful aspects because those aspects roll with the highest item power and receive the highest aspect multipliers. Fill weapon slots with multiplicative (not additive) aspects first.
- Additive +skill-damage aspects provide diminishing returns when stacked — one or two is fine, but stacking them while leaving a weapon slot with a weak aspect is a net loss.
- Cooldown-reduction aspects on armor are valuable primarily for shout-heavy builds where shout downtime is a real DPS loss; if shouts already have near-full uptime the CDR return is low.
- Defensive aspects (Resolve/DR) on armor are valuable when the build is dying but not when survival is already comfortable.

For specific aspect choices per slot for the Frenzy build, call `graph_build("frenzy")`.

## Uniques and Mythics — coaching notes
The Barbarian's four-weapon Arsenal creates four potential unique/mythic slots, making the class unusually gated on specific weapon drops. Key coaching points:

- The dual-wield weapon pair is build-enabling for the Frenzy archetype — without it the build functions as a weaker generic melee build. Prioritize this pair over armor uniques.
- Pants and helm uniques that pay off shout uptime or Unstoppable windows are strong mid-priority items; they amplify an already-present mechanic rather than enabling a new one.
- Mythic rings (resource-spend multipliers) are strong but not blocking — the build functions without them; they are a damage ceiling upgrade.
- A Crit-Damage mythic 2H only belongs in a Gushing Wounds build; in other builds it is a stat stick with wasted budget on Crit Damage.

For exact unique recommendations per slot and GA priority, call `graph_build("frenzy")` and `lookup_item` for the candidate items.

## Tempering — coaching guidance
- Weapon tempering: match the damage-type affix to your skill (basic vs core), then add Overpower damage for Overpower-centric builds or attack speed for Frenzy builds.
- Armor tempering: Max Life and total armor are survivability fundamentals. Shout cooldown reduction on at least one armor piece sustains the shout rotation.
- Resist tempering: fill the lowest resistance first; balanced resistances are more efficient than over-capping one element.

## Masterworking — coaching guidance
Masterworking crit-picks should follow the same priority as tempering: damage multiplier on the weapon first, then Critical Strike Damage or Vulnerable Damage, then Cooldown Reduction for shout builds. Overpower Damage is a valid third pick for Overpower-centric builds. Do not waste masterworking crits on additive +skill-damage affixes when a multiplicative affix is available.

## Paragon — coaching guidance
Paragon boards and glyph choices are build-specific and version-sensitive. For exact board sequence, node targets, and glyph slot assignments call `graph_build("frenzy")`.

General sequencing rationale: the first glyph slot should amplify the primary damage type (basic or core skill, depending on the build). A Vulnerable or Crit glyph fills the second slot. Survival glyphs come after the damage floor is established. Board legendaries that extend Berserking uptime or amplify the primary damage type have priority over flat stat legendaries.

## Mercenary pairing
- **Hire: Raheir** — taunt, Fortify, and armor uptime smooths melee survivability. The taunt buys the Barbarian standing-time in dense packs.
- **Reinforce: Subo** — pull and Vulnerable utility feeds the Barbarian's Vulnerable bucket without needing a skill slot dedicated to it.

## Common mistakes
- Leaving all skills on weapon Auto-Select instead of assigning the Arsenal weapon per skill — causes suboptimal Expertise procs and mismatched DPS attribution.
- Skipping the Technique quest early and forfeiting a permanent free Expertise bonus.
- Equipping Gushing Wounds without a Crit-Damage mythic 2H and maxed Crit — it underperforms every other key passive without full investment.
- Judging stat-stick weapons by their tooltip DPS — only the Arsenal-assigned weapon's DPS matters for a given skill.
- Over-stacking additive +skill damage while the multiplicative weapon slot sits empty or holds a weak aspect.
- Treating Glynn's Anvil as a damage aspect — it provides Resolve/DR and nothing else.
- Neglecting Fury generation on gear — Unbridled Rage and Core skills punish low resource severely.
- Filling charm slots with generic charms before acquiring the build-specific unique charm — the unique charm carries a disproportionate share of the seasonal power budget. Confirm charm priorities via `graph_build("frenzy")`.
