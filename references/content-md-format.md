# `content.md` Format Specification

`content.md` is the intermediate slide plan the skill generates from the source
documents. It is the single source of truth for the deck. Each `## Slide`
block maps to exactly one output slide. Keep it concrete: the rendering step
copies these values into the template, so vague notes produce vague slides.

## Top-of-file metadata

Always start with a metadata block so the renderer knows global intent. When a
brief is present, fill this block from the brief (audience, goal, tone, slide
count, language all usually come straight from it):

```markdown
# Deck: <deck title>

- Audience: <who will read it>
- Goal: <the one thing the deck should achieve>
- Tone: <e.g. executive / technical / sales / academic>
- Language: <e.g. 中文 / English — match the source documents>
- Target slides: <number>
- Template: <filename of the .pptx template to build on>
```

## Per-slide blocks

Use this exact shape for every slide. The `[layout: ...]` tag tells the
renderer which template layout to reuse — **vary it**; a deck of identical
bullet slides is the most common failure.

```markdown
## Slide N — [layout: <layout-tag>]
Title: <short, specific>
Subtitle: <optional>
Body:
- <point — one idea per line, keep tight>
- <point>
Visual: <chart spec | image filename from the folder | icon idea | "none">
Notes: <speaker notes — optional>
```

### Allowed `layout` tags

Pick the tag that fits the content, not whatever is convenient:

| Tag | Use for |
|-----|---------|
| `cover` | Title slide (deck open) |
| `agenda` | Table of contents / what's ahead |
| `section-divider` | Chapter break between topics |
| `bullets` | A few key points (max ~5 lines) |
| `two-column` | Compare two things, or text + supporting list |
| `image-text` | One strong image beside explanatory text |
| `stat-callout` | One or more big numbers with short labels |
| `quote` | A testimonial, principle, or pull-quote |
| `chart` | Data visualization (specify chart type + the data file) |
| `process` | Numbered steps / timeline / flow |
| `closing` | Summary, call to action, thank-you / contact |

### Chart / data slides

When a slide draws on a `.csv`/`.xlsx` from the folder, the `Visual:` line must
name the file, the chart type, and which columns:

```markdown
Visual: chart — bar chart from sales_q4.csv, x=region, y=revenue
```

### Image slides

Name the image file exactly as it appears in the folder:

```markdown
Visual: image — product_hero.png, full-bleed left half
```

## Mapping rules the renderer follows

- One source document section ≠ one slide automatically. **Synthesize**:
  merge thin sections, split dense ones, cut filler. Aim for the target slide
  count, not a 1:1 transcription.
- Lead with the conclusion on content slides; don't bury the point.
- If the source has a number worth emphasizing, give it a `stat-callout`.
- Every slide should have a visual element (`Visual:` rarely `none`).
- Keep body lines to single ideas; long paragraphs overflow template shapes.

## Worked example

```markdown
# Deck: 2026 上半年增长复盘

- Audience: 管理层
- Goal: 让管理层批准下半年的渠道预算
- Tone: executive
- Language: 中文
- Target slides: 8
- Template: brand-template.pptx

## Slide 1 — [layout: cover]
Title: 2026 上半年增长复盘
Subtitle: 渠道、留存与下半年规划
Visual: none

## Slide 2 — [layout: agenda]
Title: 今天的内容
Body:
- 上半年关键结果
- 增长来自哪里
- 留存的隐患
- 下半年预算建议
Visual: icon — 四个编号圆圈

## Slide 3 — [layout: stat-callout]
Title: 上半年关键结果
Body:
- 营收同比 +38%
- 新客获取成本下降 22%
- 月活跃突破 120 万
Visual: stat — 三个大数字横排

## Slide 4 — [layout: chart]
Title: 增长来自哪里
Body:
- 自然流量仍是主力，但增速放缓
- 付费渠道贡献的增量翻倍
Visual: chart — stacked bar from channel_growth.csv, x=month, y=new_users by channel
Notes: 强调付费渠道的边际效率拐点

## Slide 8 — [layout: closing]
Title: 下半年建议
Body:
- 把付费渠道预算上调 40%
- 成立留存专项小组
Visual: none
```
