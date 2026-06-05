# Brief Guide

The **brief** is the user's plain-language description of the deck they want.
It is deliberately free-form — the user writes a short note, not a rigid form.
The skill reads it and lets it steer `content.md` generation.

## How to interpret a brief

A brief is the highest-priority input. Treat anything it states as a
requirement, and fill silence with the source material and skill defaults.
Watch for these dimensions (any subset may appear, in any phrasing):

| Dimension | What to look for | How it affects content.md |
|-----------|------------------|---------------------------|
| Audience | "for the board", "给客户", "internal team" | Sets tone, depth, and what to assume known |
| Goal | "get budget approved", "教学用" | The deck's spine — lead every slide toward it |
| Slide count | "8 slides", "控制在10页内" | Hit the number; merge/split content to fit |
| Emphasis | "focus on Q2 growth", "重点讲留存" | Give these more slides / a stat or chart slide |
| Exclusions | "skip methodology", "不要财务细节" | Leave these out even if the documents cover them |
| Structure | "problem → solution → ask", a numbered list | Follow the given order and sections |
| Tone | "formal", "活泼一点", "data-driven" | Match wording and visual choices |
| Specific slides | "make slide 1 a big quote" | Honor exact requests verbatim |
| Length per slide | "keep it skimmable", "每页不超过3点" | Constrain body density |
| **Role / style** | "角色：咨询顾问", "用商务风格", "minimalist" | Picks the maker persona — see `roles.md` |
| **Web research** | "补充最新行业数据", "research competitors", "加上2026市场规模" | Triggers web search — see `research.md` |
| Template | "用 brand.pptx 这个模板", "套用模板X" | Names which `.pptx` to build on |

## Precedence

1. **Brief** wins on structure, emphasis, count, tone, inclusion/exclusion.
2. **Source documents / data / images** supply the facts and visuals.
3. **Skill defaults** (varied layouts, every slide gets a visual, lead with the
   conclusion) apply only where the brief is silent.

If the brief asks for content the materials don't support, don't fabricate —
note the gap to the user and either ask for the missing input or mark the slide
as needing data.

## What the user might name the file

Detected automatically when the filename contains: `brief`, `requirements`,
`spec`, `instructions`, `outline`, `需求`, `要求`, `说明`, `大纲`. If the user
named it something else, the shortest document that *describes* the deck (rather
than containing its content) is the brief.

## Example briefs (free-form is fine)

**Example 1 — terse (with role + research):**
```
给管理层的季度复盘，8页，重点讲增长来源和下半年预算建议，
方法论那部分跳过。角色：汇报者。补充一下行业最新增速数据。
结尾要一页明确的预算请求。模板用 brand.pptx。
```

**Example 2 — structured:**
```
Audience: prospective enterprise customers
Goal: book a pilot
Length: ~10 slides
Must include: the problem, our approach, 2 case studies, pricing, next steps
Skip: company history
Tone: confident, data-led — use the numbers in metrics.xlsx
Slide 1: bold one-line value prop, no bullets
```

**Example 3 — narrative:**
```
This is a teaching deck for a 30-minute intro session on our API.
Assume the audience codes but hasn't used us before. Walk from "what
problem this solves" through a live-ish example to "how to get started".
Keep each slide light — one idea per slide. Friendly tone.
```

In all three cases, generate `content.md` by turning the brief's intent into a
slide-by-slide plan and pulling the actual content from the folder's documents,
data, and images.
