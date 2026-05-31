# Builds — Season 13 flagship endgame builds

> Season: 13 · Patch: 2.4 · Last refreshed: 2026-05-29 · Coaching synthesis over d4-mcp graph data

One curated flagship build per class. **These files are strategy/curation prose only — they do NOT contain loadout data.** Gear-per-slot (with variants), paragon boards, Charms + Seal, glyphs, and effect text are all served live from the knowledge graph: call `graph_build(<slug>)` + `lookup_*` and present the variants. The files give you the coaching judgment the graph can't — win condition, how-to-play, priorities, why-this-build.

| Class | Flagship build | File | `graph_build` slug |
|---|---|---|---|
| Paladin | Arbiter Hammerdin | [paladin.md](paladin.md) | `arbiter-hammerdin` |
| Warlock | Dread Claws | [warlock.md](warlock.md) | `dread-claws` |
| Sorcerer | Ball Lightning | [sorcerer.md](sorcerer.md) | `ball-lightning` |
| Necromancer | Full Minion Army | [necromancer.md](necromancer.md) | `full-minion-army` |
| Druid | Pulverize | [druid.md](druid.md) | `pulverize` |
| Barbarian | Frenzy | [barbarian.md](barbarian.md) | `frenzy` |
| Rogue | Dance of Knives | [rogue.md](rogue.md) | `dance-of-knives` |
| Spiritborn | Rock Splitter | [spiritborn.md](spiritborn.md) | `rock-splitter` |

## How to use these
- **"Review my build"** → `graph_build(<slug>)` + `lookup_*` for the loadout (the authority), and the matching `<class>.md` for strategy/priorities. Diff the graph's loadout against the player's actual gear (ask them to paste or describe it). Flag missing Charms/Seal first — that's the most common Season 13 damage plateau.
- **Aspect classification** → never call an aspect offensive/defensive from its name or slot. Use `lookup_aspect` for the real effect (see the hard rule in SKILL.md and `references/damage-formula.md`).
- **Deeper class theory** (paragon, glyph order, tempering, masterworking, mercenary pairing) lives in `references/classes/<class>.md`, not here.
- **The Charm system** is documented in `references/systems/seasonal-charms.md`.
