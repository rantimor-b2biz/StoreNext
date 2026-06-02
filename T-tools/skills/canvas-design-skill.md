---
name: canvas-design
description: Create premium static enterprise visual assets (.png, .pdf) using a design-philosophy-first approach. Use when creating LinkedIn graphics, infographic covers, case study visuals, thought leadership posters, or any high-craft static piece for StoreNext content.
client: StoreNext
brand-ref: T-tools/skills/brand-guidelines-skill.md
---

# Canvas Design Skill — StoreNext Edition

## Overview

This skill produces enterprise-quality static visuals using a two-step process: **design philosophy first, then visual execution**. Output is always `.png` or `.pdf`.

**Keywords**: canvas, enterprise graphic, LinkedIn visual, infographic, data visualization, case study design, poster, brand asset, static visual

---

## When to Use This Skill

- Creating a LinkedIn graphic that communicates data-driven authority
- Designing a procurement/supply chain infographic cover
- Building case study visual templates
- Producing an executive-quality blog header image
- Creating any high-craft static visual where enterprise credibility is paramount

**Not for:** Realistic photography (→ use flux-prompt-engineering-skill), interactive dashboards (→ HTML/SVG), or generative animations (→ algorithmic-art-skill).

---

## The Two-Step Process

### Step 1 — Design Philosophy

Before touching canvas tools, write a visual philosophy (`.md` file). This is NOT a layout brief — it's a visual aesthetic worldview.

**Name the movement** (1–2 words): e.g., "Procurement Order", "Data Authority", "Systems Clarity"

**Write the philosophy** (4–6 paragraphs):
- How does it express through space, form, color, composition?
- What communicates enterprise scale and trust?
- What is the *visual mood* — not the content?

**Critical guidelines:**
- Emphasize craftsmanship repeatedly — the work must look like it came from a top-tier B2B design firm
- Data should feel authoritative — numbers are visual anchors, not decoration
- Minimal text in the philosophy — ideas live in design, not paragraphs
- The finished piece should look like it could appear in a Fortune 500 annual report

**Philosophy examples for StoreNext:**

> **"Procurement Order"**
> Philosophy: Complexity made legible through systematic visual architecture.
> Visual expression: Purple fields divided into precise zones — each representing a different operational domain. Turquoise lines connect nodes, showing flow without chaos. Typography is Inter Bold at commanding scale for primary metrics, Inter Regular at micro scale for supporting detail. The composition reads like a procurement org chart elevated to art — authoritative, structured, instantly scannable. No wasted space. Every element load-bearing. The work of a designer who spent weeks calibrating the weight of each visual element until the enterprise complexity became self-evident.

> **"Data Authority"**
> Philosophy: Numbers as the primary visual language of trust.
> Visual expression: Key metrics isolated in purple fields — large, commanding, unmistakable. Supporting context in turquoise accents. Data visualization elements (bars, lines, flows) built from first principles of honest information design. Grid barely perceptible in light grey beneath the composition. The visual hierarchy says: here is what matters, here is why, here is the proof. Meticulously calibrated by a designer who understands that CFOs make decisions from visual patterns before they read a single word.

---

### Step 2 — Canvas Execution

With the philosophy established, execute on canvas. Use Python (Pillow/Cairo), HTML Canvas, or SVG.

**Brand alignment (mandatory):**
- Pull colors from `T-tools/skills/brand-guidelines-skill.md`
- Default palette: Purple `#3C2C4C` + Turquoise `#7CCBC3` + White `#FFFFFF`
- Typography: Inter (bold headers, regular body); fallback Segoe UI
- 8px baseline grid; 16/24/32/48px spacing rhythm
- Data sources visible when charts or statistics are used

**Craftsmanship requirements:**
- No element overlaps unless intentional and designed
- All text within canvas boundaries with proper margins
- Spacing is deliberate — not arbitrary
- Limited palette (2–4 colors max) that feels intentional
- Typography serves the data hierarchy — not decoration
- Second-pass refinement is mandatory: review and make more enterprise-grade

**Canvas conventions:**
- **LinkedIn optimal:** 1080×1350px (portrait)
- **Blog/article header:** 1200×600px
- **Infographic:** 1080×1920px (tall) or 1200×800px (landscape)
- **Case study visual:** 1280×720px (16:9)
- **Email banner:** 600×200px
- **PDF one-pager:** A4 (2480×3508px at 300dpi)

---

## Conceptual Thread (Critical)

Before executing, identify the **quiet business concept** embedded in the visual:

For StoreNext, this often means:
- Supplier complexity → multiple nodes that resolve into a single organized hub
- DSO/cash flow pressure → time-series tension building toward resolution
- Procurement as infrastructure → foundational layers supporting operational activity above
- Enterprise scale → density of detail that rewards closer inspection

The concept should be felt by procurement professionals, not announced. Others simply experience a credible enterprise design.

---

## Data Visualization Principles

When including charts, metrics, or data:

- **Metric first** — display the number large, then contextualize
- **Comparison matters** — before/after, benchmark, industry average
- **No 3D charts** — they distort; flat only
- **Color meaning** — Purple for primary, Turquoise for secondary, Red for alerts/deviations
- **Source attribution** — "McKinsey, 2025" or "Internal data, 300+ clients" adds credibility
- **Visual hierarchy:** metric → context → proof → implication

---

## Refinement Protocol

After generating, ask: *"Would a CFO trust this data? Would a procurement leader save this?"*

To refine:
- ❌ Don't add decorative elements — add clarity
- ❌ Don't introduce new colors — deepen the existing data story
- ✅ Tighten spacing so visual hierarchy becomes self-evident
- ✅ Ensure key metrics are unmistakably prominent
- ✅ Remove anything that doesn't contribute to the enterprise message

---

## Output Format

1. **Philosophy file:** `[topic]-design-philosophy.md`
2. **Visual asset:** `[topic]-visual.png` or `[topic]-visual.pdf`
3. Save to: `O-output/[week-or-topic]/process/` (draft) → `final/` (approved)

---

## Fonts Available

Located in the original skill's `canvas-fonts/` directory. Key fonts for StoreNext:
- `BricolageGrotesque-Bold.ttf` — Strong enterprise headlines
- `IBMPlexMono-Regular.ttf` — Data/technical metrics display
- `GeistMono-Bold.ttf` — Precise, system-like labels
- `IBMPlexSerif-Bold.ttf` — Executive editorial headers

---

## Quality Bar

The finished piece should look like:
- It belongs in a Fortune 500 procurement team's strategy presentation
- A CFO would approve it without revision
- It took a professional B2B designer several hours to produce
- Data is legible, trustworthy, and clearly sourced

**For StoreNext, corporate credibility is design credibility.** Complexity is fine — if it's organized. Data is the hero — make it look like it.

---

*Canvas Design Skill — Enterprise Edition*
*StoreNext / Procurement, Finance, Data Intelligence visuals*
