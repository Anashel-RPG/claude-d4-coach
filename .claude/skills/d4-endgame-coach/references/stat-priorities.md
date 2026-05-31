# Stat Priorities

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Capping order (universal)
1. **Resistances to 70%** (cap). Sacrifice anything else for this first.
2. **Armor to the damage-reduction cap for your level** — use `armor_breakpoint` for the exact value (verify against the current patch).
3. **Movement speed to 25%** if not provided by skills/aspects.

## Offensive priority by archetype
- **Crit-based:** Crit chance → Crit damage → Vulnerable damage → Multiplicative skill modifiers
- **DoT / damage-over-time:** Damage over time → All damage → Class-specific scalars
- **Overpower:** Overpower damage → Maximum life → Fortify generation
- **Minion:** Minion damage → Minion attack speed → Player damage (only if a Minion-damage-from-X aspect exists)

## Per-class offensive attribute
Your class's main attribute is your primary offensive stat — stack it on every slot that can roll it.

| Class | Main attribute |
|---|---|
| Barbarian | Strength |
| Paladin | Strength |
| Rogue | Dexterity |
| Spiritborn | Dexterity |
| Sorcerer | Intelligence |
| Necromancer | Intelligence |
| Warlock | Intelligence |
| Druid | Willpower |

Paladin's Strength also feeds Armor → its Coat of Arms key passive, so it pulls double duty. See `references/classes/<class>.md` for class-specific attribute interactions.

## Season 13 multiplier layer — Charms + Seal
The 6 Charm slots + Seal are a large, build-defining multiplier stacked on top of normal gear stats. After capping defenses and stacking your offensive bucket, an underperforming build is very often missing optimized charms rather than missing gear rolls. See `references/systems/seasonal-charms.md`.

## Per-slot stat targets

See class file `references/classes/<class>.md` for slot-by-slot stat rolls — they vary by build.

## Pitfalls
- Pushing crit damage past ~700% with low crit chance is wasted budget. Crit chance is multiplicative on the expected value.
- Resistance gear bonuses do not carry through Paragon — check the Paragon defensive boards first.
- "All Damage" is not multiplicative with itself; stacking two All-Damage aspects is additive between them.
