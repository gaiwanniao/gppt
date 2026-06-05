# Web Research

The skill can pull in current, external information when the brief asks for it
or when the folder's materials are insufficient. Primary scenario: **Claude
Code (CLI)**.

## When to research

Search the web when:
- The brief explicitly asks for it ("补充最新行业数据", "include 2026 market
  size", "research competitors").
- The brief requires facts the folder's documents don't contain.
- A claim, statistic, or trend needs a current source to be credible.

Do **not** search when the folder already contains everything needed — don't
pad the deck with web filler the user didn't ask for.

## How to research (Claude Code)

**Primary — built-in tools (no setup beyond permissions):**
- `WebSearch` finds relevant pages (returns titles + URLs).
- `WebFetch` reads a specific page's content.
Typical loop: `WebSearch` for the topic → pick credible sources → `WebFetch`
each to extract facts → use them in `content.md`.

These are first-party tools. If prompted for permission, allow them, or add to
`~/.claude/settings.json`:
```json
{ "permissions": { "allow": ["WebSearch", "WebFetch"] } }
```

**Fallback — search MCP (for Bedrock/Vertex/gateway setups):** the built-in
`WebSearch` is unavailable when Claude Code routes through Bedrock or Vertex.
In that case, connect a search MCP server (e.g. Brave Search or Exa), and add
`"WebSearch"` to `disabledBuiltinTools` so the model uses the MCP tool. The
research loop above is otherwise identical — the MCP tool replaces `WebSearch`.

If neither is available, tell the user research is off and proceed with the
folder's materials only (don't fabricate facts).

## Using results responsibly

- **Attribute sources.** Put the source (publication + date) in the slide's
  `Notes:` field in `content.md`, so the deck stays clean but traceable.
- **Prefer primary/credible sources** — official reports, filings, reputable
  outlets, peer-reviewed work — over forums and SEO content.
- **Note freshness.** Lead with the most recent data; flag if a figure is
  older than the brief implies.
- **Never invent.** If a needed figure can't be found, mark the slide as
  needing data and tell the user — don't guess.
- **Respect copyright.** Paraphrase; don't paste long verbatim passages into
  slides.
