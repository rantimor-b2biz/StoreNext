# Visual Design Language — StoreNext LinkedIn Post Graphics

**Purpose:** Define the visual language for LinkedIn post graphics (1080x1350px).
**How Artist uses this file:** Read before every visual generation task. This is the authoritative reference for all LinkedIn post visual decisions.

---

## Visual Formats for LinkedIn Posts

The Artist selects one of three formats per post based on content type:

### 1. Stat Card
- **Use when:** Post centers on a key metric (%, $, time savings, error rate)
- **Layout:** Single dominant metric in large typography, minimal supporting text
- **Background:** Navy `#003D82`
- **Accent:** Teal `#00A896` on the key number or percentage
- **Goal:** Stop scroll with a single undeniable data point

### 2. Process Flow
- **Use when:** Post explains a process, steps, or before/after scenario
- **Layout:** 3-4 step flow diagram with clean nodes and labeled connectors
- **Background:** White `#FFFFFF`
- **Connectors:** Teal `#00A896`
- **Nodes:** Navy `#003D82` outlines, white fill, navy text
- **Goal:** Make complexity legible in 5 seconds

### 3. Quote / Insight Card
- **Use when:** Post is insight-driven or thought leadership without a dominant numeric stat
- **Layout:** Key sentence from the post in large typography, supporting data context below
- **Background:** Navy `#003D82`
- **Quote text:** White `#FFFFFF` (large)
- **Supporting stat:** Teal `#00A896`
- **Goal:** Amplify the post's most quotable moment

---

## Composition Rules

- **Canvas:** Always 1080x1350px (portrait, LinkedIn optimal)
- **Top 20%** (0–270px): StoreNext logo (left-aligned) + category label (right-aligned, Gray `#47525E`, small caps)
- **Middle 60%** (270–810px): Main visual element — stat / flow / quote
- **Bottom 20%** (810–1350px): One-line supporting fact + brand color bar (Navy or Teal, full width, 8px)
- **Max 2 fonts** (Inter Bold for headlines/metrics, Inter Regular for supporting text)
- **Max 3 colors** — always from brand palette below

---

## Color Usage (Authoritative Source)

Use THESE values for all LinkedIn post visuals. Do NOT reference artist-agent.md for colors — that file contains outdated values.

| Role | Name | Hex |
|------|------|-----|
| Primary | Navy | `#003D82` |
| Accent | Teal | `#00A896` |
| Neutral | Gray | `#47525E` |
| Text on dark | White | `#FFFFFF` |
| Background | White or Navy | `#FFFFFF` / `#003D82` |

> **Note:** artist-agent.md references purple `#3C2C4C` — that is OUTDATED. The current brand standard is navy `#003D82`. Source of truth: this file + `C-core/brand-standards.md`.

---

## Visual Selection Logic

| Post Content Signal | Select This Format |
|---------------------|--------------------|
| Has a key metric (%, $, time) | Stat Card |
| Explains a process or sequential steps | Process Flow |
| Insight / thought leadership, no dominant stat | Quote Card |

When in doubt, default to Stat Card — data-forward visuals perform best with CFO and Procurement audiences.

---

## Prohibited in LinkedIn Visuals

- Stock photography (brand decision — no faces, no people, no generic shutterstock imagery)
- More than 40 words total on the visual
- Gradients (flat color only — no linear or radial gradients)
- More than 3 colors on a single visual
- Faces or people (brand decision)
- Decorative elements unrelated to data or message
- Drop shadows (flat design only)

---

## Logo Usage

**File:** `C-core/storenext-logo.svg`
**Embed in every visual — no exceptions.**

| Background | Wordmark (cls-1) | Icon (cls-2) |
|---|---|---|
| Light (white) | `#432f45` (as-is) | `#ee404a` (as-is) |
| Dark (navy `#003D82`) | Override to `#FFFFFF` | `#ee404a` unchanged |

- Position: top-left, 16px clear space minimum
- Width: 100px minimum on 1080px canvas
- Never stretch, rotate, or recolor beyond the above rules

---

*Visual Design Language — StoreNext*
*Authority: C-core/brand-standards.md | Updated: 2026-06-08*
