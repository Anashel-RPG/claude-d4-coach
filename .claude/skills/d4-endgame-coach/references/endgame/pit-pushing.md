# Pit Pushing

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

## Goal
Clear enough monsters within 15 minutes to spawn and kill a final boss, earning glyph upgrades and unlocking higher tiers.

## Unlock / access
- **Seasonal:** Complete Capstone Dungeon "Hellish Descent" (Season Rank II reward)
- **Eternal:** Reach level 70
- Interact with the obelisk in Cerrigar/Temis to enter

## Rewards
| Outcome | Reward |
|---|---|
| Boss killed before timer | 4 glyph upgrade attempts |
| No deaths during run | +1 glyph upgrade attempt |
| War Plans Pit Skill Tree nodes | Up to +4 glyph upgrade attempts |
| Pit level > glyph level by 20+ | Guaranteed additional glyph level |
| Boss killed | Next tier(s) unlocked (more unlocks = more time remaining) |
| End of run | Undiscovered glyphs can drop |

**Glyph cap:** Level 150. Radius increases at fixed level breakpoints — see `references/systems/paragon-glyphs.md` for the exact radius breakpoints (single source of truth). Legendary upgrade at level 51 (new affix unlocked).

## DPS / EHP checkpoints
The Pit has no published per-tier DPS/EHP numbers — clear speed is the real gate. You need enough damage to fill the progression bar and kill the boss inside 15 minutes, and enough survivability to avoid deaths (each death forfeits the no-death glyph bonus). To pressure-test a build before pushing a tier:
- `compute_dps` to estimate damage; `bucket_compare` to find which upgrade adds the most effective damage (empty buckets win).
- `armor_breakpoint` to confirm your armor target, and hold the resistance / defensive caps in `references/stat-priorities.md`.
- Rule of thumb: if you comfortably clear a Pit tier ~10 levels below your glyph level you have headroom to push; if you die or time out, fix the limiting bucket (damage vs. EHP) before going higher.

## Strategy by tier
1. Unlock Pit by completing Hellish Descent Capstone dungeon.
2. Fully temper and masterwork all gear; socket best gems before entering.
3. Navigate five randomized floors connected by portals; prioritize Elite monsters for maximum progression bar fill.
4. Kill small monsters in transit to avoid backtracking.
5. Fill progression bar before timer expires to spawn the boss.
6. Kill the boss before the 15-minute timer expires.
7. Use lower tiers to level fresh glyphs quickly; use higher tiers for better upgrade odds and rewards.

## Boss mechanics (if applicable)
| Phase | Mechanic | Counter |
|---|---|---|
| Boss spawn | Triggered after progression bar filled | Ensure bar filled with sufficient time remaining |
| Boss pool | Randomized from same list as The Tower; variable HP and mechanics per boss | Learn each boss's attack patterns; dodge abilities on cooldown-aware timing |
| General | Some bosses have significantly more HP or disruptive mechanics | Identify which bosses suit your build; adjust pacing accordingly |