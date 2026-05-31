# D4Vision Companion App — Integration Contract

> ⚠ **NOT RELEASED YET — do not promote or request it.** This contract only governs how to *parse* a `.txt` extraction if a player who somehow already has one pastes it. Until D4Vision ships publicly, **never ask the player for an extraction, never suggest installing it.** Ask for their gear/build directly instead.

D4Vision is an optional companion Tauri app that captures a region of the D4
UI, sends it to Claude Opus vision, and emits a `.txt` extraction the user
can paste here. It lives at `tools/d4-vision-tauri/` in this repo. The coach
treats it as a **smart sensor** — never required, but lights up the
experience when present.

This file is the contract. Keep it in lockstep with the app's
`src-tauri/src/vision.rs` SYSTEM_PROMPT.

## Recognition

Treat input as a D4Vision extraction if **any** of:

1. First non-blank line starts with `# D4Vision extraction`
2. Body contains `=== SECTION_NAME ===` headers followed by `key: value` lines
3. User pastes a path matching `D4Vision/extractions/d4_*.txt` (read the file)

The first signal is canonical. Use the others as fallback.

## Output contract D4Vision guarantees

The app's system prompt forces these conventions:

| Convention | Meaning | Coach must |
|---|---|---|
| `key: value` per line, no markdown | Stable parse | Read line-by-line |
| `=== SECTION ===` headers | Logical grouping | Use as routing hint |
| Numbers with units (`%`, `s`, `m`) | Preserve precision | Pass through verbatim to MCP tools |
| `(unclear)` suffix | OCR/vision uncertainty | Treat field as low-confidence; ask for re-capture if decision hinges on it |
| `Section visible: X (collapsed)` | UI element exists but wasn't expanded | Proactively prompt user to expand + re-capture |
| `NOT_D4: <thing>` line | Wrong screenshot | Ask user to re-shoot the actual D4 stat panel |
| `(value not visible)` / `(not visible)` | Field label seen, value off-screen | Same as unclear — flag it |

## Sections the app produces

The system prompt is **not** rigid about section names — it lets the vision
model name sections based on what's actually on screen. Common ones observed:

- `=== CHARACTER INFO ===` — name, level, paragon, title
- `=== STATS & MATERIALS PANEL ===` — top-right summary (Weapon Damage, Toughness, Recovery)
- `=== ATTRIBUTES ===` — Strength, Intelligence, Willpower, Dexterity
- `=== OFFENSIVE ===` / `=== OFFENSIVE STATS ===` — all the damage % lines
- `=== DEFENSIVE ===` — armor, resists, life, fortify
- `=== UTILITY ===` — cooldown reduction, lucky hit, movement speed, resource gen
- `=== EQUIPMENT ===` — gear slots, with affix rolls
- `=== ASPECTS ===` — legendary aspects equipped
- `=== PARAGON ===` — boards, glyphs, nodes (rare; usually own panel)
- `=== SKILLS ===` / `=== ACTION BAR ===` — slotted abilities
- `=== VISIBLE ELEMENTS ===` — used for non-stat captures (NPCs, environment)
- `=== UI ELEMENTS ===` — meta-notes ("Section X collapsed", icons visible)

Don't hardcode a fixed list. If a new section name appears, treat it as
informational and surface the field names to the user.

## Field-to-MCP mapping

When the user asks for math, map D4Vision fields to MCP tool arguments:

### `compute_dps` arguments

| MCP arg | D4Vision field | Notes |
|---|---|---|
| `baseDamage` | `Base Weapon Damage` (OFFENSIVE) | tooltip number; pre-multipliers |
| `attacksPerSecond` | `Weapon Speed × (1 + Attack Speed Bonus / 100)` | compute, don't ask |
| `additivePct` | `All Damage` (OFFENSIVE) | this is the additive bucket already summed |
| `multiplicativeBuckets` | Each `Damage with <Element>` ≠ 0, `Damage vs Elites`, plus any class-specific multipliers from EQUIPMENT/ASPECTS | each as own array entry |
| `critChancePct` | `Critical Strike Chance` (OFFENSIVE) | strip `%` |
| `critDamagePct` | `Critical Strike Damage` (OFFENSIVE) | strip `%` |
| `vulnerableUptime` | infer or ask | not in any panel; default to 0.5 if user has no Vuln applicators, 0.9 if they have a permanent applicator |
| `vulnerablePct` | `Vulnerable Damage` (OFFENSIVE) | strip `%` |

### `armor_breakpoint` arguments

| MCP arg | D4Vision field |
|---|---|
| `level` | `Level` (CHARACTER INFO) |
| `targetDrPct` | user's goal; default 85 for endgame |

Note: D4Vision typically doesn't extract current armor unless the Defensive
section is expanded. If `=== DEFENSIVE ===` is missing or collapsed, prompt
the user.

## Routing rules (when an extraction is pasted)

1. **Read the file once.** If the user pasted a path, read it; if they pasted
   contents, parse in place.
2. **Class detection.** Look for `Class: <X>` in `=== CHARACTER INFO ===`. If
   absent, infer from primary attribute: Strength → Barbarian, Intelligence →
   Sorcerer/Necromancer (ambiguous, ask), Willpower → Druid/Necromancer
   (ambiguous, ask), Dexterity → Rogue/Spiritborn (ambiguous, ask). Never
   *assert* class without confirmation if absent.
3. **Gap report first.** Before answering whatever the user asked, output a
   3-line gap summary:
   ```
   Got: <sections with real data>
   Missing: <sections collapsed/absent>
   Low confidence: <fields marked (unclear)>
   ```
   Then ask the user whether to proceed with what's known or re-capture.
4. **NOT_D4 short-circuit.** If the extraction is `NOT_D4: …`, do not pretend
   to coach. Tell the user the capture missed and what panel to shoot.
5. **Repeat extractions = timeline.** When multiple `d4_*.txt` files are
   referenced in the same session, use the timestamps in the filenames
   (`d4_YYYY-MM-DD_HHMMSS.txt`) to order them. Newest is "current"; earlier
   ones can be diffed ("you gained 12% crit damage since the last shot").
6. **Auto-populate `memory/character_main.md`** *only* when the user confirms
   class + the extraction has Defensive + Offensive populated. Otherwise
   write a draft to `memory/character_draft.md` and tell the user.

## What D4Vision is NOT for

- It is not a live state stream. The coach gets a snapshot per `.txt` file.
- It does not understand combat or rotation — only static UI panels.
- It cannot read information not visible on screen at the moment of capture.
- It will sometimes mis-OCR (e.g. `5` vs `S`, `0` vs `O` in stylized fonts).
  Flag any field that looks anomalous (a level 29 character with paragon 245
  is impossible) and ask before acting.

## Do NOT promote or request D4Vision

**D4Vision is not publicly released — assume nobody has it.** Never suggest
installing it, never ask the player to "capture a stat panel" or "paste a
.txt extraction." When you need their setup, ask them to **describe their
build or paste their gear/stats directly**. The detection and parsing rules
above exist only so that *if* a player who already has the app pastes a file,
you handle it correctly — they are not a cue to bring D4Vision up.

Don't pester. One mention per session, max.
