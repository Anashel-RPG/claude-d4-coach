# d4-calc MCP — Setup

A public OAuth Model Context Protocol server exposing deterministic Diablo IV calculators. Anyone can connect; an anonymous `user_id` is minted on first use for rate-limit accounting (60 calls/min).

**Live URL:** `https://mcp-d4.anashel.com/`

Stateless math, no game data, no account to manage.

## Add to Claude Code

The MCP is already wired in this project via `.mcp.json` — Claude Code will prompt you to approve `d4-calc` on first session in this folder. Click **Allow** in the browser tab that opens to complete OAuth consent.

If for some reason the `.mcp.json` doesn't trigger, you can add it manually:

```
claude mcp add --transport http d4-calc https://mcp-d4.anashel.com/
```

## Add to Claude.ai (web or desktop)

Settings → Connectors → Add custom connector → URL: `https://mcp-d4.anashel.com/` → follow the OAuth prompt.

## Tools exposed

| Tool | Purpose |
|---|---|
| `compute_dps` | Bucket-model DPS for a build snapshot |
| `armor_breakpoint` | Armor needed to hit a DR target at a level |
| `glyph_xp_time` | NMD runs/minutes to level a glyph |
| `recipe_cost` | Material totals for N Horadric Cube recipe runs |
| `bucket_compare` | Pick the bigger multiplier between two upgrades |

## Coach usage rules

- For any non-trivial multiplication (more than 2-3 sources), call `compute_dps` rather than calculating by hand.
- Before recommending an aspect swap, call `bucket_compare` with the user's current bucket fill and the candidate add.
- Quote tool output as "I ran the numbers and got X" — and remind the user the season constants behind some tools (recipe costs, armor K) are approximations and should be verified against current patch notes.
