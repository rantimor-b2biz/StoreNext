---
name: algorithmic-art
description: Create interactive generative art and animated data visualizations using p5.js with seeded randomness. Use when StoreNext content calls for animated supply chain flow visualizations, interactive data stories, generative brand patterns, or visually distinctive enterprise content that demonstrates technical sophistication.
client: StoreNext
brand-ref: T-tools/skills/brand-guidelines-skill.md
---

# Algorithmic Art Skill — StoreNext Edition

## Overview

This skill produces **living, interactive generative visualizations** using p5.js. Output is a self-contained `.html` file (interactive) and/or `.png` captures. Use when a business concept benefits from motion, emergence, or parametric exploration.

**Keywords**: generative art, algorithmic, p5.js, animation, interactive, supply chain visualization, data flow, procurement network, brand pattern

---

## When to Use This Skill

- Visualizing supplier network dynamics (nodes, connections, flow)
- Creating an animated supply chain disruption scenario for a thought leadership piece
- Building an interactive procurement efficiency visualization for a demo or landing page
- Generating a distinctive animated brand pattern (website background, video intro)
- Demonstrating data behavior through animation — not static charts

**Not for:** Static infographics (→ canvas-design-skill), standard data charts (→ HTML/SVG), or photography (→ flux-prompt-engineering-skill).

---

## The Two-Step Process

### Step 1 — Algorithmic Philosophy

Write a computational aesthetic philosophy (`.md` file) before writing a single line of code.

**Name the movement** (1–2 words): e.g., "Supplier Gravity", "Procurement Flow", "Disruption Cascade"

**Write the philosophy** (4–6 paragraphs):
- What computational processes express the enterprise concept?
- What behaviors, forces, and dynamics mirror the business reality?
- How does emergence tell the procurement/finance story?
- What makes each seed variation feel coherent yet unique?

**Critical guidelines:**
- The philosophy must stress that the algorithm looks like it was refined through countless iterations by someone with both enterprise expertise and computational mastery
- Beauty emerges from the *process*, not just the final frame
- Parameters should emerge naturally from the business concept

**Philosophy examples for StoreNext:**

> **"Supplier Gravity"**
> Philosophy: Procurement complexity as orbital mechanics.
> Algorithmic expression: Hundreds of supplier-nodes initialized across the canvas, each with a mass proportional to transaction volume. A central hub — the procurement platform — exerts gravitational pull. Nodes orbit with slight Perlin noise perturbation, creating organic-feeling orbits rather than perfect circles. High-value suppliers cluster tightly. Long-tail suppliers drift further out but remain in the system. Occasionally a node breaks orbit (disruption event) — others briefly shift before restabilizing. The visualization makes visible what enterprise procurement teams feel but cannot see: hundreds of relationships in constant motion, held together by the gravity of process. Every physics parameter calibrated through painstaking iteration by a designer who understands both orbital mechanics and enterprise supply chains at the highest level.

> **"Procurement Flow"**
> Philosophy: Data moving through organizational structure as water through channels.
> Algorithmic expression: Flow fields constructed from organizational topology — invoices, POs, approvals each represented as particle streams following channels of different widths. Bottlenecks render as particle density. Clear paths render as smooth acceleration. Color maps to process stage: purple for in-progress, turquoise for complete, red for exception states. The visual reads like an honest system diagnostic — showing both the beauty of well-functioning procurement and the friction points that cost organizations millions. Meticulously tuned to feel both technically credible and visually compelling.

---

### Step 2 — p5.js Implementation

**Brand alignment (mandatory):**
```javascript
// StoreNext color palette
const BRAND = {
  purple: '#3C2C4C',
  turquoise: '#7CCBC3',
  red: '#E85252',
  darkGrey: '#333333',
  lightGrey: '#F5F5F5',
  white: '#FFFFFF',
  // Meteor satellite
  meteorTeal: '#2B8D85',
  meteorBlue: '#B8D4E8',
  // Data satellite
  chartBlue: '#4A7BA7'
};
```

**Seeded randomness (always):**
```javascript
let seed = 12345;
randomSeed(seed);
noiseSeed(seed);
// Same seed = identical output (reproducibility for demos)
```

**Parameter structure:**
```javascript
let params = {
  seed: 12345,
  // Quantities (supplier count, flow rate, disruption frequency)
  // Scales (network density, connection radius, particle speed)
  // Thresholds (when does an alert trigger? when does disruption cascade?)
  // Must emerge naturally from the enterprise concept
};
```

---

## Interactive HTML Artifact

The output is a **single self-contained `.html` file** that runs immediately in any browser or demo environment.

### Required Structure

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js"></script>
  <style>/* All styling inline — enterprise-clean aesthetic */</style>
</head>
<body>
  <!-- Canvas area + Controls sidebar -->
  <script>
    // ALL p5.js inline: params, classes, setup(), draw(), UI handlers
  </script>
</body>
</html>
```

### Sidebar Controls (Standard)

**Fixed sections (always include):**
- **Seed:** Display + Prev/Next/Random/Jump buttons
- **Actions:** Regenerate, Reset, Download PNG

**Variable sections (per artwork):**
- **Parameters:** Sliders for each tunable business parameter
  - Example: "Supplier Count", "Disruption Frequency", "Flow Speed"
- **Colors:** Optional — include if product personas matter (Core vs Meteor vs Data)

---

## StoreNext Application Context

Generative art for StoreNext should feel:
- **System-level credible** — feels like a real enterprise visualization, not art for art's sake
- **Data-honest** — shows both smooth states and friction/disruption states
- **Enterprise-dense** — complexity is not hidden, it's organized and legible
- **Purple gravity, turquoise flow** — purple anchors the structure, turquoise shows movement

It should NOT feel:
- ❌ Abstract / decorative / "screensaver"
- ❌ Overly colorful / playful / startup-y
- ❌ So simplified it loses enterprise credibility
- ❌ Technically impressive but disconnected from business reality

---

## Demo Use Case

For sales demos and conference presentations:
- The visualization should run as a background for live presentations
- Parameter controls allow showing: "normal state" → "disruption event" → "platform response"
- Seed navigation allows showing consistent, rehearsed scenarios
- Download PNG for use in static materials after demo

---

## Output Format

1. **Philosophy file:** `[topic]-algo-philosophy.md`
2. **Interactive artifact:** `[topic]-generative.html`
3. **PNG captures** (optional): `[topic]-seed-[N].png`
4. Save to: `O-output/[week-or-topic]/process/` → `final/` when approved

---

## Quality Bar

The finished artifact should:
- Run smoothly (60fps target)
- Produce meaningfully different results per seed while maintaining brand coherence
- Have controls that mirror real enterprise parameters (not abstract sliders)
- Feel like it was built by a developer who deeply understands both procurement systems and computational aesthetics
- Work as a demo asset — reliable, reproducible, impressive

---

*Algorithmic Art Skill — Enterprise Edition*
*StoreNext / Supply Chain, Procurement, Finance visualization*
