# Paladin

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Core identity
Season 13 holy warrior — a melee/aura bruiser who channels Holy (Divine) damage through Auras, shields, and the Arbiter transformation. Core skills (Blessed Hammer, Blessed Shield, Zeal, Spear of the Heavens, Condemn) spend the Paladin's resource, replenished by Basic skills and aura/passive sustain. The class signature is **Auras** — toggled persistent buffs (Fanaticism, Defiance, Holy Light), each with a "Rite" upgrade — layered over a transformation ultimate (Arbiter of Justice). Tanky by fantasy: builds stack Armor, Block, and Resolve, then convert that defense into damage via Coat of Arms.

## Damage scaling buckets
- **Multiplicative sources:** Key Passives (Coat of Arms turns Armor + Block Chance into damage; Path of the Penitent ramps Zealot skills; Exaltation buffs while transformed into Arbiter; Judgement Day chains Judgement detonations); build-specific legendary Aspects and Uniques (verify with `graph_build` / `lookup_*`). Critical, Vulnerable, and Overpower are their own separate buckets.
- **Additive sources:** Strength (Paladin's main offensive attribute — skill damage, and it feeds Armor, so it pulls double duty under Coat of Arms); +Core / +Holy skill-damage tempers; additive damage paragon rares; aura-bonus passives.
- **Critical / Vulnerable / Overpower hooks:** Block Chance and Armor feed Coat of Arms (defense → offense); Condemn and certain passives apply Vulnerable; mobility skills supply burst and CC; Dexterity → Crit Chance. Overpower is build-dependent — shield/Block variants lean on it more than aura-zoom builds.

## Skill tree priorities
| Skill | Role | Notes |
|---|---|---|
| Blessed Hammer | Core — Holy | Top endgame core; rotating hammers; the Hammerdin engine (signature weapon confirmed via `graph_build`) |
| Blessed Shield | Core — Holy | Ricocheting shield throw; the Shield-build core (Shield of Justice upgrade) |
| Zeal | Core — melee flurry | Multi-hit melee spender (Zealot's Legacy); pairs with Path of the Penitent |
| Spear of the Heavens | Core — ranged Holy | Thrown spear with a Vulnerable/CC payoff (Pronouncement of Heaven) |
| Condemn | Core — AoE | Gathers and detonates enemies (Gather the Guilty); feeds Judgement Day |
| En Guarde / Riposte / Holy Bolt | Basic — resource gen | Build resource and apply early procs; pick to match your spender |
| Defiance / Fanaticism / Holy Light Aura | Aura — class mechanic | Toggled buff + a Rite upgrade; Fanaticism (Rite of Vengeance) = offense, Defiance = DR, Holy Light (Rite of Judgement) = sustain/holy |
| Shield Charge | Mobility / engage | Auradin "zoom" mobility (Relentless Charge); also a damage hit |
| Falling Star | Mobility / burst | Freefall gap-closer with an impact nuke |
| Aegis | Defensive | Block/shield wall (Stay Resolute); the survival button |
| Rally / Longevity / Renewal | Utility / sustain | Group buff and healing/uptime passives |
| Consecration | Ground / sustain | Holy ground that heals and damages |
| Arbiter of Justice | Ultimate — transformation | Transform into the Arbiter; the flagship ultimate Exaltation keys off |

## Key passives / class mechanic
**Auras (class mechanic):** The Paladin runs persistent toggled Auras that continuously buff the Paladin (and allies). Each aura has a **Rite** upgrade that changes or amplifies its effect — e.g. Fanaticism Aura → Rite of Vengeance (offense), Holy Light Aura → Rite of Judgement. Builds keep one aura active at all times; "Auradin" zoom builds revolve around movement + aura uptime. The flagship ultimate, **Arbiter of Justice**, transforms the Paladin and is the payoff the Exaltation key passive scales.

**Key Passives (choose one):**
- **Coat of Arms** — converts Armor + Block Chance into damage; the defensive-bruiser backbone (Strength and shields pull double duty).
- **Path of the Penitent** — Zealot skills (Zeal) ramp into a frenzy of attack speed/damage.
- **Exaltation** — empowers the Paladin while transformed into the Arbiter; the transformation-build payoff.
- **Judgement Day** — Judgement/Holy detonations chain-react; the AoE-nuke enabler.

## Aspects and uniques

> **Loadout = live data.** This build's exact gear (with variants), paragon boards, charms/seal, glyphs, and effect text come from the knowledge graph — the coach pulls them with `graph_build("arbiter-hammerdin")` + `lookup_*` at runtime and presents the variants. The notes here are coaching judgment, not a loadout list.

**Aspect selection logic:** Paladin aspects generally fall into three buckets — multiplicative damage amps tied to the build's core skill condition, defensive stacking (Armor, Resolve, Block), and mobility/attack-speed. When choosing between aspects, match the multiplier bucket to what the build actually does: a repeated-hit core (like Blessed Hammer) benefits from multi-hit amps; an aura or transformation build benefits from condition-on-transform amps. Use `lookup_aspect` + `graph_build` to see which aspects are graph-confirmed for a specific build before swapping anything.

**Unique priority logic:** The Paladin has meaningful uniques in most weapon and armor slots. Treat any Paladin unique as unverified until confirmed with `lookup_item` / `graph_build`. Prioritize uniques that directly multiply the build's core skill or enable the transformation window; replace only when a higher-roll or better-suited unique drops.

## Mythic uniques
Mythic uniques are universal chase items available to any class. Which mythic is best-in-slot for a specific Paladin build depends on the build's scaling buckets — verify with `graph_build` and `lookup_item`. General coaching: prioritize mythics that plug the build's weakest bucket (survivability, resource sustain, or a missing damage multiplier) rather than defaulting to the most famous name.

## Tempering manuals
- Weapon: Core or Holy skill damage (match your spender), Vulnerable damage, attack speed, aura / Block bonuses.
- Armor: Max Life, total armor, Block Chance, Resolve / aura bonuses, resource cost reduction, resistances.

## Masterworking crit picks
1. Core skill damage (or the Holy / aura tag your build uses)
2. Critical Strike Damage / Vulnerable Damage (or Overpower for shield/Block variants)
3. Strength, or Cooldown Reduction for Arbiter / aura uptime

## Paragon priority
Exact board sequence, node picks, and glyph leveling order are build-specific and live in the graph — use `graph_build("arbiter-hammerdin")` (or the relevant slug) to retrieve them. General coaching principle: prioritize the rare nodes that feed the build's primary scaling attribute first, then socket glyphs in the order that maximizes the build's dominant damage bucket, then fill survival. Glyph leveling: level the most impactful damage-amp glyph first; survival glyphs can lag behind until Pit difficulty demands them.

## Mercenary pairing
- Hire: Raheir — taunt + Fortify + armor; layers onto the Paladin's already-tanky frame for Pit pushing.
- Reinforce: Subo — pull + Vulnerable groups packs for Blessed Hammer / Condemn AoE and feeds the Vulnerable bucket.

## Season 13 Charms + Seal
Paladin fills 6 Charm slots and 1 Seal slot with seasonal items — the season's defining multiplier layer. Which specific charms and seal a given build uses is live data; retrieve with `graph_build` and verify with `lookup_item`. Coaching priority: missing or unoptimized charms is the most common reason endgame damage plateaus — always check these slots early in a build review. (See `references/systems/seasonal-charms.md` for how the charm system works.)

## Common mistakes
- Running with no Aura active — the toggled aura is free, persistent power; forgetting it leaves a multiplier on the table.
- Stacking the wrong attribute — Strength is the offensive attribute, and it feeds Armor → Coat of Arms, so it pulls double duty for nearly every Paladin build.
- Ignoring Armor/Block while running Coat of Arms — the key passive scales off defense, so under-capping Armor or Block directly cuts damage.
- Forgetting only one Ultimate and one Key Passive can be equipped at a time.
- Losing Arbiter (transformation) uptime on boss transitions, or letting Path of the Penitent's Zeal ramp decay by pausing during a DPS window.
- Mismatching the Key Passive to the build (Blessed Hammer / aura-bruiser wants Coat of Arms, Zeal wants Path of the Penitent, transformation wants Exaltation, Condemn/Judgement wants Judgement Day).
- Leaving the Season 13 Charm/Seal slots empty or unoptimized.
