# Roles (制作角色 / Personas)

A **role** is a persona that changes *how* the deck is designed and written —
its structure, density, title voice, palette direction, and visual motif. The
user picks a role in the brief (e.g. `角色：咨询顾问`, `role: minimalist`,
`用商务风格做`). One deck = one role.

## How a role is applied

A role shapes two things:
1. **content.md generation** — slide count tendency, title style, how much text
   per slide, which layouts to favor, whether to lead with charts or narrative.
2. **rendering choices** — palette direction, typography feel, visual motif —
   *within the limits of the template* (see "Role vs. template" below).

If the brief names no role, infer one from the audience/tone (e.g. "for the
board, formal" → `商务` or `汇报者`; "teaching session" → `教学者`). If still
unclear, default to **`商务`** (clean professional baseline).

## Role vs. template (important)

- **A user template always wins on brand identity** — its master slides,
  theme colors, and fonts are kept. The role then guides *layout selection,
  content density, title voice, and visual motif* within that brand.
- **With no template**, the role *fully* defines the design (palette, fonts,
  layout) via the `pptx` skill's from-scratch route (`pptxgenjs.md`). Use the
  role's palette/typography hints below as the starting point.

## The roles

### 1. `简约` / Minimalist
- **Voice:** calm, essential. One idea per slide.
- **Density:** very low — short titles, ≤3 lines body, lots of whitespace.
- **Layouts:** `cover`, `stat-callout`, single-focus `image-text`, big `quote`.
- **Palette:** mostly white/neutral, one restrained accent. High contrast type.
- **Motif:** generous margins; type and space do the work. No decorative bars.

### 2. `商务` / Business (Corporate)
- **Voice:** clear, professional, confident.
- **Density:** medium — titles + 3-5 tight points; numbers where they matter.
- **Layouts:** balanced mix; `two-column`, `agenda`, `stat-callout`, `chart`.
- **Palette:** navy/charcoal primary, one accent (teal/blue), neutral support.
- **Motif:** consistent icon-in-circle for section headers; restrained, tidy.

### 3. `汇报者` / Executive Reporter (briefing)
- **Voice:** answer-first. Each title states the takeaway, not the topic.
- **Density:** medium-low — lead with the conclusion, supporting points below.
- **Layouts:** `stat-callout` heavy, `chart` with one-line insight, `closing`
  with a clear recommendation/ask.
- **Palette:** sober — slate/graphite with a single signal accent for the ask.
- **Motif:** every slide answers "so what?"; summary + recommendation framing.

### 4. `咨询顾问` / Consultant (structured)
- **Voice:** action titles (full-sentence takeaways, "Revenue grew because…").
- **Density:** medium-high but disciplined — MECE structure, pyramid logic.
- **Layouts:** `two-column`, `process`, `chart` with annotation, framework
  grids (2x2). Governing thought up top, support below.
- **Palette:** classic navy + grey, one accent for emphasis.
- **Motif:** structured frameworks; source line on data slides; tracker/agenda.

### 5. `创意` / Creative (editorial / bold)
- **Voice:** expressive, punchy, memorable.
- **Density:** low text, high visual impact.
- **Layouts:** full-bleed `image-text`, oversized type, asymmetric `quote`,
  bold `section-divider`.
- **Palette:** one bold dominant color + sharp accent; dark backgrounds welcome.
- **Motif:** a strong repeating visual element (oversized numerals, color block).

### 6. `数据派` / Data Analyst (dashboard)
- **Voice:** precise, evidence-led; the chart is the point.
- **Density:** charts dominate; minimal prose, one insight per chart.
- **Layouts:** `chart` heavy, `stat-callout` rows, comparison `two-column`,
  small-multiples grids.
- **Palette:** neutral canvas so data colors pop; consistent series colors.
- **Motif:** every data slide names its source; units and axes labeled.

### 7. `路演者` / Pitch (startup / investor)
- **Voice:** narrative arc — problem → solution → traction → ask.
- **Density:** low; momentum and story over detail.
- **Layouts:** big `stat-callout` for traction, `image-text` for product,
  `process` for go-to-market, decisive `closing` (the ask).
- **Palette:** energetic brand color + crisp accent.
- **Motif:** one hero metric per beat; confident, forward-leaning.

### 8. `教学者` / Educator (teaching)
- **Voice:** friendly, scaffolded; assume curiosity, not expertise.
- **Density:** one concept per slide, plenty of examples and diagrams.
- **Layouts:** `process` for steps, `image-text` for examples, recap slides,
  `agenda` framed as learning objectives.
- **Palette:** warm, approachable; clear contrast for readability.
- **Motif:** numbered progression; "key takeaway" callout per section.

## Combining a role with explicit brief instructions

The brief's specific instructions still override the role's defaults. If the
role is `简约` but the brief says "put all 12 KPIs on one slide," follow the
brief and note the tension. Role sets the defaults; the brief fine-tunes.
