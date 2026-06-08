---
name: brand-guidelines
description: Applies StoreNext's official brand colors, typography, and visual identity to any artifact — presentations, graphics, HTML, SVG, email, or documents. Use when brand consistency, visual formatting, or enterprise design standards apply.
client: StoreNext
source: C-core/brand-guidelines.md, C-core/brand-standards.md
---

# StoreNext Brand Styling

## Overview

Use this skill to apply StoreNext's official brand identity to any visual or design artifact.

**Keywords**: branding, brand colors, visual identity, post-processing, styling, typography, StoreNext, enterprise design, B2B visuals, procurement, CFO

---

## Brand Colors

### Primary Palette

| Name | Hex | RGB | Use For |
|------|-----|-----|---------|
| **Purple** | `#3C2C4C` | rgb(60, 44, 76) | Headers, primary CTAs, key UI elements, authority |
| **Turquoise** | `#7CCBC3` | rgb(124, 203, 195) | Accents, secondary CTAs, data highlights, trust |

### Secondary Palette

| Name | Hex | RGB | Use For |
|------|-----|-----|---------|
| **Red** | `#E85252` | rgb(232, 82, 82) | Alerts, important callouts, error states, urgency |
| **Dark Grey** | `#333333` | rgb(51, 51, 51) | Body text, primary typography |
| **Light Grey** | `#F5F5F5` | rgb(245, 245, 245) | Card backgrounds, dividers, subtle sections |
| **White** | `#FFFFFF` | rgb(255, 255, 255) | Main backgrounds, clean space |

### Satellite Colors — Meteor (Finance Automation)

| Name | Hex | Use For |
|------|-----|---------|
| Finance Teal | `#2B8D85` | Meteor-specific accents |
| Baby Blue | `#B8D4E8` | Soft accent for finance content |
| Dark Electric Blue | `#1F4A5C` | Deep headers for Meteor |
| Finance Orange | `#FF8C42` | Highlights in financial context |

### Satellite Colors — Data & Analytics

| Name | Hex | Use For |
|------|-----|---------|
| Data Teal | `#2B8D85` | Data visualization primary |
| Chart Blue | `#4A7BA7` | Secondary data series |

---

## Typography

| Role | Font | Weight | Size | Notes |
|------|------|--------|------|-------|
| **H1 Page Title** | Inter / Segoe UI | Bold (700) | 48–54pt | Main page headlines |
| **H2 Section Header** | Inter / Segoe UI | Bold (700) | 36–42pt | Major sections |
| **H3 Subsection** | Inter / Segoe UI | Semi-Bold (600) | 28–32pt | Feature groups |
| **H4 Heading** | Inter / Segoe UI | Semi-Bold (600) | 20–24pt | Component headers |
| **Body Text** | Inter / Segoe UI | Regular (400) | 16–18pt | Main content |
| **Small Text** | Inter / Segoe UI | Regular (400) | 14pt | Captions, metadata |
| **Micro Text** | Inter / Segoe UI | Regular (400) | 12pt | Footnotes, timestamps |

**Typography rules:**
- Headers: always bold/semi-bold, sentence case, max 50 characters
- Body: 16–18pt minimum, line-height 1.5, 60–80 char line length
- Use **bold** for key terms — never italics for emphasis
- Use color for data highlights — not size changes

---

## Color Combinations (Ready to Use)

### LinkedIn Posts — Primary
```
Background: #3C2C4C (Purple)
Accent: #7CCBC3 (Turquoise)
Alert/Highlight: #E85252 (Red)
Body Text: #FFFFFF (White)
```

### Web / Document — Clean
```
Background: #FFFFFF or #F5F5F5
Headers: #3C2C4C (Purple)
Accents: #7CCBC3 (Turquoise)
Body Text: #333333 (Dark Grey)
```

### Data Visualization
```
Primary Series: #3C2C4C (Purple)
Secondary Series: #7CCBC3 (Turquoise)
Alert / Deviation: #E85252 (Red)
Grid Lines: #F5F5F5 (Light Grey)
```

### Email
```
Background: #FFFFFF
CTA Button: #3C2C4C (Purple) with #7CCBC3 hover
Body Text: #333333
Link Color: #3C2C4C
```

---

## CSS Variables (for HTML/SVG artifacts)

```css
:root {
  --brand-purple: #3C2C4C;
  --brand-turquoise: #7CCBC3;
  --brand-red: #E85252;
  --text-primary: #333333;
  --text-inverse: #FFFFFF;
  --bg-primary: #FFFFFF;
  --bg-subtle: #F5F5F5;

  /* Meteor satellite */
  --meteor-teal: #2B8D85;
  --meteor-blue: #B8D4E8;
  --meteor-electric: #1F4A5C;
  --meteor-orange: #FF8C42;

  /* Data satellite */
  --data-teal: #2B8D85;
  --data-chart: #4A7BA7;
}
```

---

## Application Rules

### DO
✅ Use Purple (`#3C2C4C`) for authority, headers, primary actions
✅ Use Turquoise (`#7CCBC3`) as the trust and accessibility accent
✅ Use Red (`#E85252`) sparingly — alerts and critical callouts only
✅ Maintain 8px baseline grid; 16/24/32/48px spacing rhythm
✅ Include data sources for credibility (sources visible when relevant)
✅ High resolution: minimum 1200px width web, 300 DPI print
✅ Respect WCAG AA color contrast standards

### DON'T
❌ Use hype colors (rainbow, neon, playful gradients)
❌ Use stock photo clichés (handshakes, high-fives, servers)
❌ Distort data with 3D charts or overlapping visual elements
❌ Use fonts other than Inter/Segoe UI without explicit reason
❌ Overuse Red — it signals urgency, use strategically only

---

## Visual Quality Checklist

Before finalizing any StoreNext visual:

- [ ] Colors match brand palette (purple `#3C2C4C`, turquoise `#7CCBC3`)
- [ ] Typography: Inter Bold headers, Inter Regular body
- [ ] Minimum font size: 16px body, 24px headers
- [ ] High-resolution imagery (1200px+ width for web)
- [ ] Adequate white space (16px minimum padding)
- [ ] Color contrast accessible (WCAG AA minimum)
- [ ] No stock photo clichés
- [ ] Data sources visible if charts/stats used
- [ ] Logo placement: bottom right or top left

---

## Brand Personality Through Color

- **Purple** → Strength, authority, enterprise gravitas — we are infrastructure
- **Turquoise** → Trust, accessibility, human partnership — we work with people
- **Red** → Urgency, action, honest alerts — we don't hide problems
- **Dark Grey** → Clarity, directness, professionalism — we say what we mean

**Overall feel:** Authoritative, clear, data-driven, trustworthy, enterprise-grade.
**Not:** playful, trendy, vague, hype-heavy, or decorative.

---

*Source: `StoreNext/C-core/brand-guidelines.md` + `StoreNext/C-core/brand-standards.md`*
*For use in all StoreNext content, visuals, presentations, and artifacts.*
