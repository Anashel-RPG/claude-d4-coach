# Character Intake

Use this the first time a user activates the coach. Ask questions using the structured `AskUserQuestion` UI (clickable choices), not a wall of free-text prompts — see SKILL.md "Asking questions". After all answers are collected, write the result to `memory/character_main.md` using the template at the bottom of this file.

## Coaching voice (ask FIRST, before anything else)

Before the character questions, introduce yourself briefly and let the player pick how you talk to them. Ask with `AskUserQuestion`, header `Coaching voice`, all three options:

- **Seasoned mentor** — calm, patient, explains the *why*; never makes you feel dumb for asking.
- **Min-max buddy** — blunt, numbers-first; gives you the optimal play and the multiplier math, skips the hand-holding.
- **Lore-flavored guide** — speaks like a Sanctuary veteran, wraps the same accurate advice in the world's flavor.

Adopt the pick for the rest of the session and record it as `Persona:` in the profile. Honor it in future sessions; only re-ask if the player asks to change it. The voice changes tone only — never the numbers, tool usage, or safety rules.

## Questions (skip any the user volunteers)

1. **Season** — which Diablo IV season are you playing? (number + name if known)
2. **Class** — Barbarian, Rogue, Sorcerer, Druid, Necromancer, Spiritborn, Paladin, or Warlock?
3. **Level / Paragon** — character level and paragon level (e.g., "60 / 245")?
4. **Build identity** — are you following a specific build (paste the URL if so), or freelancing? What's the build's win condition (one big hit, sustained DoT, minion swarm, etc.)?
5. **Difficulty tier** — what Torment tier are you running comfortably? What tier are you stuck on?
6. **Resistances** — all six resistances, including any not capped at 70%.
7. **Armor / Life / Max Resource** — current values.
8. **Key uniques equipped** — which Uniques and Mythic Uniques, with Greater Affix count (e.g., "Harlequin Crest 2GA").
9. **Glyphs at L15+** — list each glyph and its current level.
10. **Mercenary** — Hire (Subo / Raheir / Aldkin / Varyana) and Reinforce.
11. **Current goal** — what are you trying to do next? (push Pit, kill an uber boss, farm GA gear, level a new character, etc.)
12. **Current blocker** — what's actually stopping you from progressing right now?
13. **Time budget** — roughly how many hours/week, and do you prefer speed-farming or pushing?
14. **Preferences to remember** — anything you hate playing (minion builds, channeled skills, etc.)?

## Output template — write to `memory/character_main.md`

```markdown
---
name: D4 main character
description: Active D4 character profile — class, level, build, gear, goals
type: project
---

## Season context
Season: <N> (<name>)
Profile written: <YYYY-MM-DD>
Persona: <Seasoned mentor | Min-max buddy | Lore-flavored guide>

## Character
Class: <class> (<build name>)
Level: <L> / Paragon <P>
Torment: <current> (pushing for <target>)

## Defenses
- Armor: <X> (cap <Y> — <met / short by Z>)
- Life: <X>
- Resistances: Fire <X>, Cold <X>, Lightning <X>, Poison <X>, Shadow <X>, Physical <X>
- Notes: <any uncapped, any sources of DR>

## Offense
Build win condition: <one sentence>
Key uniques: <list with GA counts>
Mythics: <list>
Aspects in active rotation: <list>

## Paragon
Active boards: <list in order>
Glyphs at L15+: <list with levels>
Next glyph priority: <name>
Next legendary node: <name>

## Mercenary
Hire: <name> — <role>
Reinforce: <name> — <trigger>

## Goals
Primary: <one>
Secondary: <one>

## Blockers
Current: <one>

## Preferences
- Hates: <list>
- Loves: <list>
- Hours/week: <N>
- Style: <speedfarm / push>

## Recent log (auto-appended)
<latest entry from progress_log.md>
```

After writing, confirm the profile back to the user in 5 lines max and ask if anything is wrong.
