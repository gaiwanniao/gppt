---
name: gppt
description: "gwn's ppt, invoked with /gppt: generate a complete, fully-editable PowerPoint deck from a folder, in one shot. Use whenever the user wants slides built from a folder containing a brief (a short file describing the deck they want), content documents (.md/.txt/.docx/.pdf), data and images, and optionally their own .pptx template. Trigger on '/gppt', 'build a deck from this folder', 'turn these documents into a presentation using my template', '按我写的需求生成PPT', '用我的模板做PPT', or any request where the user has described their PPT requirements and gathered materials and expects Claude to PLAN the slides (auto-write the outline from the brief) AND render them. Supports user-specified maker ROLES (简约/商务/汇报者/咨询顾问/创意/数据派/路演者/教学者) for different styles, fully custom user templates, and live web research when the brief needs current facts. The user does NOT prepare content.md themselves. Do NOT use for editing a single existing slide."
---

# gwn's ppt (`/gppt`)

Turn a folder of raw materials into a finished, editable `.pptx` — handling
both halves the user usually does by hand: **(1) planning what goes on each
slide, and (2) rendering it onto a template.** On top of that, it supports
**maker roles** (different design styles), **fully custom templates**, and
**live web research** when the brief calls for current facts.

The user's promise: "I drop a short note describing what I want — including
which style/role and which template — plus my documents, data, and images into
a folder; I run `/gppt`; I get a deck." Honor that — don't make them hand-write
a slide outline.

## The brief steers everything

The **brief** is a short, plain-language file in the folder where the user
describes what they want — e.g. "8 slides for the board, focus on Q2 growth and
the budget ask, skip the methodology, formal tone." It is the steering input.
The relationship between inputs is a strict priority order:

1. **Brief** — decides structure, emphasis, slide count, tone, what to include
   and exclude, and ordering. Follow it closely.
2. **Source documents / data / images** — the raw material the brief draws on.
3. **Skill defaults** — used only where the brief is silent.

If the brief and a document disagree on what matters, the brief wins. If the
brief asks for something the materials don't contain, surface the gap to the
user rather than inventing facts.

The brief can also specify **a role** (the design style, e.g. `角色：咨询顾问`)
and **request web research** (e.g. "补充最新行业数据"). The brief is detected by
filename (`brief`, `requirements`, `需求`, `要求`, `outline`, `说明`, etc.). If
no file matches but one short document clearly describes the deck rather than
containing deck content, treat that as the brief. See `references/brief-guide.md`
for everything a brief can contain.

## Custom templates

The template is **fully user-supplied** — drop any `.pptx` into the folder and
the deck is built on it, keeping its master slides, theme colors, and fonts so
output stays on-brand. Notes:
- The scanner picks the `.pptx` whose name signals a template (`template`,
  `模板`, `brand`, `母版`); if names are ambiguous and several `.pptx` exist,
  ask which is the template.
- **No template provided** → build from scratch with the `pptx` skill's
  `pptxgenjs.md` route, using the chosen role's palette/typography as the design
  basis (see `references/roles.md`).
- **Template + role together**: the template wins on brand identity; the role
  guides layout selection, content density, title voice, and visual motif
  within that brand.

## When to ask vs. proceed

Proceed without questions if the folder contains a template `.pptx` and at
least one content document. Only ask the user when something essential is
genuinely missing or ambiguous:
- No `.pptx` template found → ask for one, or offer to build from scratch via
  the `pptx` skill's `pptxgenjs.md` route instead.
- Multiple `.pptx` files and none is clearly the template → ask which is the
  template (the rest may be content to merge).
- The goal/audience is unclear and the documents don't make it obvious → ask
  one short question (audience + goal), then proceed.

Don't over-interview. A reasonable deck the user can edit beats a perfect
interview.

## Workflow

### Step 1 — Scan the folder

Locate the folder (a path the user gave, or `/mnt/user-data/uploads`). Run:

```bash
python scripts/scan_folder.py /path/to/folder
```

This returns JSON categorizing files into `template`, `brief`, `documents`,
`data`, `images`, `other`. Note the chosen template and the detected brief, and
confirm they look right. If no brief was detected, check `documents` for a short
file that describes the deck (vs. containing its content), or ask the user for a
one-line description of what they want.

### Step 2 — Read the brief, then every source document

**Read the brief first** — it tells you what the deck is for and how to shape
it, which changes how you read everything else. Then read the full content of
each file in `documents`. For formats whose text isn't already in context, use
the right reader rather than `cat`-ing binaries — consult the **`file-reading`**
skill for routing (`.docx`, `.pdf`, `.xlsx`, etc.). For `data` files, read
enough to understand the columns and ranges you'll chart. Look at `images` so
you know what visual assets are available and what each shows.

Do not skim. The quality of the deck is capped by how well you understood the
brief and the inputs.

### Step 3 — Select the role (design style)

Determine the maker role from the brief. If the brief names one
(`角色：商务`, `role: minimalist`, "用汇报风格"), use it. If not, infer from the
audience/tone; if still unclear, default to `商务`.

**Read `references/roles.md`** for the full role definitions and how each shapes
both the outline and the rendering. The available roles:
`简约` (Minimalist), `商务` (Business), `汇报者` (Executive reporter),
`咨询顾问` (Consultant), `创意` (Creative), `数据派` (Data analyst),
`路演者` (Pitch), `教学者` (Educator). The role governs slide density, title
voice, favored layouts, palette direction, and visual motif — applied within
the template's brand when a template is present.

### Step 4 — Research the web (only if the brief needs it)

If the brief asks for current/external information, or the materials lack facts
the brief requires, gather them now. **Read `references/research.md`** for the
approach. In short, for Claude Code: use the built-in `WebSearch` to find
sources and `WebFetch` to read them (fallback: a search MCP on Bedrock/Vertex
setups). Attribute every sourced fact in the slide's `Notes:` field, prefer
credible primary sources, and never fabricate a figure you can't find. Skip
this step entirely when the folder already has what's needed.

### Step 5 — Auto-generate `content.md` (the slide plan)

This is the step the user is delegating to you. Build the slide-by-slide plan
**by following the brief, in the voice and structure of the chosen role**,
drawing the actual content from the source material and any research, and write
it to `content.md` in the working directory.

Let the brief drive the decisions: if it names a slide count, hit it; if it
says what to emphasize or skip, obey; if it sets a tone, order, or specific
sections, follow that. The role sets the defaults (density, layouts, title
voice); the brief fine-tunes them. Fill remaining gaps with the source
documents and the principles below.

**Read `references/content-md-format.md` for the exact `content.md` format**,
the allowed layout tags, and a worked example. Key principles (apply where the
brief and role are silent):
- Synthesize, don't transcribe — merge thin sections, split dense ones, cut
  filler, hit a sensible slide count.
- Vary layouts deliberately (cover, agenda, stat-callout, chart, two-column,
  quote, process, closing). A deck of identical bullet slides is the failure
  mode to avoid.
- Map every `data` file that matters to a `chart` slide; map relevant `images`
  onto `image-text` slides.
- Match the language and tone of the brief and source documents.

Briefly show the user the `content.md` outline (or a short summary) before
rendering, so they can redirect early. If the brief or the user said "just make
it," skip straight to rendering.

### Step 6 — Render onto the template (editable .pptx)

Hand the plan and the template to the **`pptx`** skill's **template-based
workflow** — read `editing.md` in that skill and follow it. In short:

1. Analyze the template with `thumbnail.py` + `extract-text` to see its real
   layouts, fonts, and colors.
2. For each `## Slide` block in `content.md`, choose the template layout whose
   style matches the `[layout: ...]` tag.
3. Unpack the template, duplicate/delete/reorder slides to match the plan,
   then edit each slide's XML to insert the real content — preserving the
   template's master, layouts, theme colors, and fonts so the output stays
   on-brand.
4. Insert charts from the `data` files and place `images` where the plan calls
   for them.
5. Clean and pack to `output.pptx` **with `--original <template.pptx>`** so the
   theme and masters are retained.

The result must be native, editable PowerPoint objects (text, shapes, native
charts) — never flattened images of slides.

If no template was provided, build from scratch via the `pptx` skill's
`pptxgenjs.md` route, designing with the chosen role's palette and typography
(see `references/roles.md`).

### Step 7 — QA before delivering

Follow the `pptx` skill's QA section:
- `extract-text output.pptx` — check for missing content, wrong order, and
  leftover template placeholder text (grep for `xxx`, `lorem`, `[insert`,
  "this layout", etc.). Fix any hits.
- Render slides to images and visually inspect for overflow, overlap,
  misalignment, and low contrast. Fix real, user-visible defects in one
  focused pass; don't chase sub-pixel nitpicks.

### Step 8 — Deliver

Copy the final file to `/mnt/user-data/outputs/` and present it. Tell the user
in one line what they got and that it's fully editable in PowerPoint / WPS /
Keynote. If you generated `content.md`, mention they can tweak it and re-run to
regenerate.

## Re-running

If the user edits the brief, edits `content.md`, or swaps files in the folder
and re-invokes, re-run from the step that changed: Step 5 if the brief, role, or
content changed; Step 6 if only the template changed. Editing the brief and
re-running is the intended way to reshape the deck. Keep the same
template-retention rules.

## Reference files

- `references/brief-guide.md` — what the user's brief can contain (including
  role and research) and how to interpret it. Read in Step 2.
- `references/roles.md` — the maker roles and how each shapes the deck. Read in
  Step 3.
- `references/research.md` — web research approach for Claude Code (built-in
  WebSearch/WebFetch, MCP fallback). Read in Step 4 when research is needed.
- `references/content-md-format.md` — the `content.md` spec, layout tags,
  chart/image syntax, and a full worked example. Read before Step 5.
- The `pptx` skill (`editing.md` / `pptxgenjs.md`) — the rendering engine. Read
  before Step 6.
- The `file-reading` skill — how to read each source file type. Consult in
  Step 2 when a document's text isn't already in context.
