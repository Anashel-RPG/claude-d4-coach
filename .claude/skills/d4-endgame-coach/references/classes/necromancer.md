# Necromancer

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Core identity
Commands a minion army (Skeletal Warriors, Mages, Golem) or sacrifices it for self-buffs, dealing damage through Blood, Bone, Shadow, Corpses, and Curses. Corpse generation/consumption is the central loop alongside Essence. Builds split into Blood (Overpower/sustain), Bone (Crit/Essence), Shadow (DoT/Shadowblight), and Summoner (minion/sacrifice) archetypes.

## Damage scaling buckets
- **Multiplicative sources:** Legendary Aspects are the primary multipliers across all archetypes; Key Passives each define a separate multiplier layer; skill-type passives layer on top. Critical, Vulnerable, and Overpower are their own separate buckets.
- **Additive sources:** Intelligence (skill damage — minions inherit a share), +skill ranks (large base bump per rank), archetype-specific damage tempers, additive paragon rares.
- **Critical / Vulnerable / Overpower hooks:** Bone builds stack Crit (Ossified Essence + Compound Fracture); Blood builds stack Overpower (Tides of Blood + Rathma's Vigor); Shadow builds stack Shadowblight detonations. Vulnerable is applied by Decrepify, basic skills, and select Macabre skills.

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|
| Bone Splinters / Reap / Hemorrhage / Decompose | Basic — Essence + Corpse gen | Also apply Vulnerable; Decompose channels for Essence on Blood/Bone setups |
| Blood Surge | Core — Blood AoE | Overpower + healing engine, scales with Tides of Blood |
| Bone Spear | Core — Bone ST/AoE | Highest Crit-burst core; pairs with Ossified Essence |
| Blight / Sever / Blood Lance | Core — alt | DoT, projectile, and lance variants for Shadow/Blood hybrids |
| Corpse Explosion | Corpse — AoE nuke | Near-universal; Blighted or Plagued upgrade |
| Blood Mist | Corpse — survival | Defensive staple; immunity + cleanse |
| Corpse Tendrils | Macabre — CC | Best class CC; Blighted = Vulnerable |
| Bone Spirit | Macabre — ST nuke | Strongest single-target burst option |
| Decrepify / Iron Maiden | Corruption — Curses | Decrepify = DR + cooldown/Vulnerable support; damage amp |
| Blood Wave / Bone Storm / Army of the Dead / Soulrift | Ultimate | One pick; Soulrift is top Blood/Shadow; Bone Storm for Bone |

## Key passives / class mechanic
**Book of the Dead** — Necromancer-exclusive minion customization (unlocked ~L5):
- **Skeletal Warriors:** 3 variants (DPS / Tank / heavy-damage); can sacrifice for an offensive bonus.
- **Skeletal Mages:** 3 variants (Shadow / Cold-CC / heavy-damage); sacrifice for damage + resource bonuses.
- **Golem:** 3 variants (ultra-tank / AoE damage / AoE CC), unlocked via the ~L25 class quest; sacrifice for tankiness or DPS.
- Minions inherit a share of player stats. Raise Skeleton and Golem must be on the bar to summon. **Sacrifice builds** give up the army for a permanent multiplier — the aspect loadout changes significantly; confirm with `lookup_aspect` + `graph_build`.

**Key Passives (choose one per build):**
- **Rathma's Vigor** — Blood enabler; Overpower + Fortify ramp. Backbone of Blood Surge builds.
- **Shadowblight** — Shadow enabler; stacking shadow detonations.
- **Ossified Essence** — Bone enabler; Crit/Essence-scaled Bone damage.
- **Kalan's Edict** — minion/attack-speed enabler for summoner builds.
- **Affliction** — curse/minion hybrid scaling.

The coaching principle: always confirm which key passive a build runs before evaluating gear choices — the key passive defines which damage buckets are available, and aspects that don't feed that bucket are dead weight.

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("full-minion-army")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

## Aspect / unique coaching judgment
Exact slot assignments, effect text, and roll ranges come from the graph. The coaching judgment below is about *when* to prioritize each category — not about which slot it occupies.

- **Summoner builds** need aspects that either multiply minion damage or sustain the army's survivability. The amulet slot is the highest-value slot for summoner payoff aspects — prioritize filling it.
- **Sacrifice builds** need a completely different aspect set and should not mix summoner and sacrifice aspects; the multiplier is lost if any minion is alive when a sacrifice aspect expects none.
- **Blood builds** want aspects that feed the Overpower bucket and the Blood Orb sustain loop. Corpus Explosion stays relevant as a corpse spender even in Blood builds.
- **Bone builds** want Crit-scaling aspects and aspects that convert Bone Spear into a repeating or echoing tool. Essence management is tighter here than in other archetypes.
- **Shadow builds** stack Shadowblight detonation triggers and DoT overlap; area-coverage and grouping tools (Corpse Tendrils) are especially high value.

For mythic uniques: confirm applicability to the specific build archetype before farming — a mythic slot that doesn't feed the build's primary damage bucket is a wasted opportunity. Use `lookup_item` to check effect text before committing.

## Tempering and masterworking priorities (coaching frame)
Tempering: match the damage tag to your archetype (Blood / Bone / Darkness). Don't temper for a tag your key passive and aspects don't feed — it's additive in a bucket you're not multiplying. Overpower tempers serve Blood; Crit tempers serve Bone; DoT tempers serve Shadow.

Masterworking: prioritize the stat that sits at the intersection of your largest multiplicative bucket and the stat your key passive scales from. For summoner builds, minion damage stats critting on masterwork are the highest-ceiling rolls. Use `compute_dps` to validate before spending materials.

## Paragon priority (coaching frame)
Board order and glyph selection are build-specific and version-sensitive — confirm exact sequences with `graph_build`. The general frame:
- Rush the primary damage legendary node on whichever board feeds your archetype first.
- Level the glyph that amplifies your primary damage tag to 15 before branching.
- Survival glyphs after offense is online, not before.
- Summoner builds have a different board sequence than Blood/Bone/Shadow builds — do not cross-apply board advice between archetypes.

## Mercenary pairing
- **Hire:** Raheir — taunt + Fortify + armor uptime; smooths squishier setups, especially pre-endgame-gear.
- **Reinforce:** Subo — pull + Vulnerable utility that stacks with Corpse Tendrils for grouping.

## Common mistakes
- Neglecting Corpse generation — many skills and aspects need corpses on the ground to function. If Corpse Explosion isn't firing, the generation loop is broken.
- Skipping Blood Mist — near-universal defensive requirement across all archetypes.
- Running a minion build without Raise Skeleton and Golem on the bar (minions won't summon), or mixing sacrifice aspects with a living army (the multiplier requires no minions alive).
- Not finishing the ~L25 class quest before trying to slot the Golem.
- Mismatching the Key Passive to the skill type — Blood needs Rathma's Vigor, Bone needs Ossified Essence, Shadow needs Shadowblight. Running the wrong key passive is the single largest source of underperformance in this class.
- Stacking additive damage tempers in a bucket with no multipliers (tempers should amplify an existing multiply chain, not exist in isolation).
