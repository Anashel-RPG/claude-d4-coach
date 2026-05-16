# claude-d4-coach

Diablo IV character coach for Claude Code. **v0.1.**

A Claude Code skill that helps you optimize a D4 character from level 60 through endgame — builds, paragon boards, glyphs, Horadric Cube recipes, masterworking, tempering, mercenary picks, Pit pushing, uber boss strategy.

## Install

```bash
git clone https://github.com/Anashel-RPG/claude-d4-coach.git
cd claude-d4-coach
claude
```

Claude Code picks up `.claude/skills/d4-endgame-coach/` automatically. On first session it will prompt you to approve the `d4-calc` MCP server (a public OAuth math calculator hosted at `https://mcp-d4.anashel.com/`). Click **Allow** in the browser tab.

## What it does

- Asks about your character once (class, level, paragon, gear, goals) and remembers
- Routes questions to the right reference doc — class file, paragon system, cube recipes, etc.
- Calls the `d4-calc` MCP for exact DPS math, armor breakpoints, glyph XP timing, recipe cost totals, multiplicative-bucket comparison
- Flags additive-vs-multiplicative mistakes before they cost you an aspect slot
- Logs your progress so future sessions resume with context

## What it doesn't do

- Play the game for you
- Predict the perfect build (community guides exist for that — link them and the coach reviews against your specifics)
- Replace patch notes (always verify season-specific numbers against current Blizzard sources)

## Disclaimer

v0.1, personal project. References are best-effort snapshots; D4's meta drifts every patch. If a number looks wrong, check the source URL in the reference file header and tell the coach.

Not affiliated with Blizzard.

## License

MIT. See `LICENSE`.
