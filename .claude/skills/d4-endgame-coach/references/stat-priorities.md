# Stat Priorities

> Season: <pending> · Last refreshed: <pending> · Run enrichment to populate.

## Capping order (universal)
1. **Resistances to 70%** (cap). Sacrifice anything else for this first.
2. **Armor to current level cap** (≈9,230 at L60 — confirm season).
3. **Movement speed to 25%** if not provided by skills/aspects.

## Offensive priority by archetype
- **Crit-based:** Crit chance → Crit damage → Vulnerable damage → Multiplicative skill modifiers
- **DoT / damage-over-time:** Damage over time → All damage → Class-specific scalars
- **Overpower:** Overpower damage → Maximum life → Fortify generation
- **Minion:** Minion damage → Minion attack speed → Player damage (only if a Minion-damage-from-X aspect exists)

## Per-slot stat targets

See class file `references/classes/<class>.md` for slot-by-slot stat rolls — they vary by build.

## Pitfalls
- Pushing crit damage past ~700% with low crit chance is wasted budget. Crit chance is multiplicative on the expected value.
- Resistance gear bonuses do not carry through Paragon — check the Paragon defensive boards first.
- "All Damage" is not multiplicative with itself; stacking two All-Damage aspects is additive between them.
