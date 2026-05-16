# Damage Formula — Bucket Model

> Stable across seasons. Bucket *contents* change; the bucket model does not.

## The model

Final damage = Base × (1 + Σ additives) × Π(multiplicative_buckets)

Each multiplicative source is its own bucket and multiplies the running total. Each additive source goes into the additive sum and contributes diminishing returns.

## Default buckets (most classes)

Multiplicative (each its own bucket — chase these):
- Critical strike damage (only when crit lands)
- Vulnerable damage (only when target Vulnerable)
- Overpower damage (only on Overpower hits)
- Damage to <enemy state> (Crowd Controlled, Stunned, Burning, Bleeding, Poisoned…)
- Damage to <enemy type> (Elites, Bosses, Close, Distant)
- <Skill name> damage (single-skill multipliers, often on Unique items)
- Class mechanic multipliers (Berserking, Inner Sight, etc.)
- Most legendary Aspects that say "X% increased damage"

Additive (one shared bucket — diminishing returns):
- "+X% damage" with no qualifier (rare; most Aspects are multiplicative)
- Most Paragon rare nodes
- Skill tree "increases damage" passives (verify per skill — some are multiplicative)

## How to evaluate an upgrade

1. Identify which bucket the new source lives in.
2. If it lives in a bucket the build already has filled → multiply your current bucket's value.
3. If it lives in a bucket the build has nothing in → it's a new multiplier (huge).
4. Always prefer filling an empty bucket over over-stacking a filled one.

## Example

Current loadout has 200% Crit Damage and 80% Vulnerable damage. Two aspect choices:
- Aspect A: +30% Crit Damage → 200 → 230 in same bucket. Ratio: 3.3/3.0 = 1.10× damage.
- Aspect B: +20% Damage to Elites (new bucket, no current source) → adds whole 1.20× multiplier. **Better.**

## Pitfalls

- Some "increases damage" on the skill tree is additive, some is multiplicative. The tooltip wording is unreliable — check community-tested guides.
- Stacking two Aspects with the same "damage to X" type is usually additive within that bucket, not multiplicative across buckets.
- Skill-specific multipliers from Uniques are typically their own bucket and stack with the generic bucket of the same skill.
