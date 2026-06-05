# gwn's ppt (`/gppt`)

*[中文说明](./README.md) · English*

A Claude Skill that turns a single folder — your **brief + materials + your own
template** — into a **fully-editable** PowerPoint deck in one shot. You just drop
in the files and write a one-line brief; it handles the rest: planning the
outline, applying your template, researching the web when asked, and producing
the slides.

---

## 1. What it does

- **Builds on your template.** Uses your own `.pptx` as the base, preserving its
  master slides, theme colors, and fonts. Output is **native, editable**
  PowerPoint objects — not images.
- **Brief-driven.** You write a short brief in the folder; it auto-generates the
  slide outline (`content.md`). You never hand-write the outline.
- **8 maker roles (styles).** Specify a role in the brief to change the output
  style: `简约` (Minimalist), `商务` (Business), `汇报者` (Executive reporter),
  `咨询顾问` (Consultant), `创意` (Creative), `数据派` (Data analyst),
  `路演者` (Pitch), `教学者` (Educator).
- **Web research.** When the brief asks for current data, it uses Claude Code's
  built-in WebSearch / WebFetch to gather and cite sources (with a search-MCP
  fallback on Bedrock/Vertex gateways), attributing facts in the speaker notes.
- **One-shot invocation.** Type `/gppt` in Claude Code, or just describe what you
  want and it triggers automatically.
- **Iterate freely.** Edit the brief or `content.md` and re-run to reshape the
  whole deck.

---

## 2. Repository layout

```
gppt/
├── SKILL.md                       # Skill entry point (how Claude works)
├── README.md                      # Chinese docs
├── README.en.md                   # This file
├── LICENSE                        # MIT
├── references/
│   ├── brief-guide.md             # What a brief can contain
│   ├── roles.md                   # The 8 maker roles
│   ├── research.md                # Web research approach
│   └── content-md-format.md       # content.md outline spec
└── scripts/
    └── scan_folder.py             # Scans & categorizes folder inputs
```

---

## 3. Installation

### Option A — Claude Code (CLI, recommended)

Claude Code discovers skills at `~/.claude/skills/<name>/SKILL.md`. **The
important part: install the extracted folder, not the `.skill` archive.**

**Via git (simplest):**

```bash
git clone https://github.com/<your-username>/gppt.git ~/.claude/skills/gppt
```

**Or manually:** copy the repo contents into `~/.claude/skills/gppt/`, making
sure `~/.claude/skills/gppt/SKILL.md` exists.

**If you only have the `gppt.skill` archive** (it is a zip):

```bash
cd ~/.claude/skills
unzip -o gppt.skill -d .     # produces gppt/SKILL.md
```

**Verify:**

```bash
ls ~/.claude/skills/gppt/SKILL.md
```

Back in Claude Code, type `/gp` and `/gppt` should appear. If not, restart
`claude` and try again.

> To share with a team, place it under a project's `<project>/.claude/skills/gppt/`
> and commit it.

### Option B — claude.ai / desktop (upload)

The web apps install by **uploading the `.skill` archive**:

1. Download `gppt.skill` from this repo (or build it from a clone — see below).
2. Open Claude → Settings → Capabilities / Skills → upload `gppt.skill`.

> To build it yourself: zip the `gppt` folder and rename the archive to
> `gppt.skill`.

---

## 4. How to use

### 1) Prepare a folder with these inside

| Put in | Role | Notes |
|--------|------|-------|
| A brief file (e.g. `brief.md`) | **The driver** | Auto-detected if the filename contains `brief / requirements / 需求 / 要求 / 说明 / 大纲` |
| One `.pptx` template | Brand base | A name with `template / 模板 / brand / 母版` is preferred; omit it to design from scratch by role |
| `.docx / .pdf / .md / .txt` | Source content | Where the actual content comes from |
| `.csv / .xlsx` | Chart data | Rendered as editable charts |
| Images (png/jpg…) | Figures, logos | Placed per the brief |

### 2) Write the brief (free-form, no rigid format)

A brief can state: audience, goal, slide count, emphasis, what to skip, order,
tone, **role**, **whether to research the web**, and **which template**. Example:

```
Quarterly review for the leadership team, 8 slides, role: 汇报者,
use brand.pptx as the template. Focus on growth drivers and the H2 budget ask,
skip the methodology, add the latest industry growth figures from the web,
and end with one slide stating the budget request.
```

### 3) Invoke it in Claude

- Claude Code: type `/gppt` and point it at the folder ("build a deck from
  ~/Desktop/testppt").
- Or describe it naturally: "turn this folder into a deck using my template."

Flow: scan the folder → read brief + materials → pick the role → research if
asked → generate `content.md` (shown to you for confirmation) → render onto your
template → QA → deliver an editable `.pptx`.

---

## 5. The roles at a glance

| Role | Style |
|------|-------|
| `简约` Minimalist | Lots of whitespace, one idea per slide, restrained palette |
| `商务` Business | Clean and professional (default) |
| `汇报者` Reporter | Answer-first; every title states the takeaway |
| `咨询顾问` Consultant | Action titles, MECE / pyramid structure |
| `创意` Creative | Bold, editorial, high visual impact |
| `数据派` Data analyst | Chart-led; sources and units labeled |
| `路演者` Pitch | Problem → solution → traction → ask narrative |
| `教学者` Educator | Step-by-step, friendly, example-rich |

When a template and a role are both present: **the template governs brand
(colors / fonts / masters); the role governs layout, density, title voice, and
visual motif.**

---

## 6. Web research

- **Primary:** Claude Code's built-in `WebSearch` + `WebFetch`, no setup needed.
  If prompted, allow them, or add to `~/.claude/settings.json`:
  ```json
  { "permissions": { "allow": ["WebSearch", "WebFetch"] } }
  ```
- **Fallback:** when routing through a Bedrock / Vertex gateway, the built-in
  WebSearch is unavailable — connect a search MCP (e.g. Brave Search, Exa) and
  add `WebSearch` to `disabledBuiltinTools`.
- Sourced facts are attributed in the outline; nothing is fabricated.

---

## 7. FAQ

**`/gppt` doesn't show up?**
Most likely you dropped the `gppt.skill` archive straight into
`~/.claude/skills/gppt/`. Claude Code needs the extracted `SKILL.md`. Re-extract
per Option A so `~/.claude/skills/gppt/SKILL.md` exists, then restart `claude`.

**Can I run it without a template?**
Yes. Without a template it designs from scratch using the chosen role's palette
and typography.

**Are the generated slides editable?**
Yes — native PowerPoint objects (text, shapes, charts), editable in
PowerPoint / WPS / Keynote.

---

## 8. License

MIT — see [LICENSE](./LICENSE). Rendering relies on Claude's built-in `pptx` and
`file-reading` capabilities.
