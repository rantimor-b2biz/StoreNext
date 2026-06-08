# StoreNext — LinkedIn Visual Design Language

**Purpose:** Consistent visual template system for all LinkedIn post graphics.
**Format:** 1080 × 1080px (square), 72dpi, RGB
**Updated:** 2026-06-08

---

## 1. Color Palette (from live website)

> Note: brand-standards.md listed #003D82 (navy). The actual website uses violet-purple as primary. Use the values below for all visuals.

### Core Colors

| Name | HEX | Use |
|------|-----|-----|
| **Brand Purple** | `#7C3AED` | Primary accent, stat highlights, hexagon icons |
| **Deep Purple** | `#1E1030` | Dark card backgrounds, overlay blocks |
| **Light Purple Gradient** | `#F5F0FF` → `#FFFFFF` | Light card backgrounds, hero wash |
| **Teal** | `#0D9488` | Financial data, secondary stat color, borders |
| **Coral Red** | `#DC2626` | CTA highlights, accent strip at top of dark cards |
| **White** | `#FFFFFF` | Text on dark, backgrounds |
| **Text Dark** | `#1A1A2E` | Headlines on light backgrounds |
| **Text Muted** | `#6B7280` | Supporting text, source citations |

### Color Combinations Per Post Type

| Post Type | Background | Stat Color | Text | Accent Strip |
|-----------|------------|------------|------|--------------|
| Data / Stat | `#1E1030` dark | `#0D9488` teal | White | `#DC2626` coral |
| Insight / Quote | `#F5F0FF` gradient | `#7C3AED` purple | `#1A1A2E` dark | `#0D9488` teal |
| Comparison | Split: dark left / light right | Both accent colors | Contrast per side | None |

---

## 2. Typography

Use **Inter** (Google Fonts, free) as the primary typeface. Fallback: Segoe UI, Helvetica Neue.

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| **Primary Stat** | 96–120px | 800 ExtraBold | Teal `#0D9488` or White |
| **Stat Label** | 28–32px | 600 SemiBold | White or Dark |
| **Headline** | 42–52px | 700 Bold | White or `#1A1A2E` |
| **Body / Supporting** | 22–26px | 400 Regular | White 80% or `#6B7280` |
| **Source Citation** | 16px | 400 Italic | White 50% or `#9CA3AF` |
| **Logo Lockup** | Fixed SVG | — | White (on dark) or Purple (on light) |

---

## 3. Layout Templates

### Template A — STAT CARD (default for data-led posts)

```
┌─────────────────────────────────────┐
│ ▓▓▓ CORAL ACCENT STRIP (8px top) ▓▓▓│
│                                     │
│   [HEXAGON ICON - small, top left]  │
│                                     │
│                                     │
│         $53                         │  ← 120px ExtraBold, Teal
│    per invoice exception            │  ← 28px, White 80%
│                                     │
│   ─────────────────────────────     │  ← thin teal divider
│                                     │
│   Supporting insight line here.     │  ← 24px, White
│   One or two sentences max.         │
│                                     │
│   (Ardent Partners, 2024)           │  ← 16px, White 50%, italic
│                                     │
│                                     │
│  [StoreNext logo]   storenext.com   │  ← bottom strip, dark #150C2A
└─────────────────────────────────────┘
```

**Background:** `#1E1030` solid or subtle radial gradient toward `#2D1B4E`
**Hexagon icon:** 64×64px, purple fill `#7C3AED`, white icon stroke inside

---

### Template B — INSIGHT CARD (for principle / insight posts)

```
┌─────────────────────────────────────┐
│                                     │
│  [StoreNext logo — top left]        │
│                                     │
│  ┌─────────────────────────────┐    │
│  │  ❝                         │    │  ← quote block, Purple bg
│  │  The insight headline       │    │  ← 42px Bold, White
│  │  goes here in bold.         │    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  Supporting sentence with data.     │  ← 22px, Dark text
│  Second sentence here.              │
│                                     │
│  Source or context line.            │  ← 16px, Muted
│                                     │
│  ─────────────────────────────────  │  ← teal divider
│  storenext.com          #SupplierPortal │
└─────────────────────────────────────┘
```

**Background:** `#F5F0FF` → `#FFFFFF` gradient (top-left to bottom-right)
**Quote block:** `#7C3AED` purple, rounded corners 12px

---

### Template C — COMPARISON / BEFORE-AFTER (for contrast posts)

```
┌──────────────┬──────────────────────┐
│              │                      │
│  WITHOUT     │  WITH                │
│  portal      │  StoreNext           │
│              │                      │
│  100         │  27                  │  ← big numbers
│  exceptions  │  exceptions          │
│  /month      │  /month              │
│              │                      │
│  $5,300      │  $1,431              │
│  direct cost │  direct cost         │
│              │                      │
└──────────────┴──────────────────────┘
│  [StoreNext logo]  73% fewer exceptions  │
└─────────────────────────────────────────┘
```

**Left panel:** `#1E1030` dark, white text, muted/red numbers
**Right panel:** `#0D9488` teal or `#7C3AED` purple, white text, bold teal/white numbers
**Bottom strip:** Dark `#1A1A2E`, logo + summary stat

---

## 4. Recurring Brand Elements

### Hexagon Icon Container
- Shape: Regular hexagon, flat-top orientation
- Sizes: 48px (small), 64px (medium), 96px (large — hero)
- Fill: `#7C3AED` purple OR `#0D9488` teal (alternate by post type)
- Icon inside: White, 60% of hex size, 2px stroke
- Use for: category icon top-left on every card

### Top Accent Strip
- Height: 8px
- Color: `#DC2626` coral red (dark cards) or `#0D9488` teal (light cards)
- Full width across top edge
- Creates visual anchor, consistent across all posts

### Bottom Logo Strip
- Height: 60px
- Background: `#150C2A` (very dark purple, one shade deeper than card bg)
- Left: StoreNext logo, white, 120px wide
- Right: `storenext.com` in muted white, 16px

### Trust Markers (optional, for credibility posts)
- "Since 2002 · 400+ Enterprise Clients" — 14px, White 50%
- SOC 2 · ISO 27001 badge row (use sparingly)

---

## 5. Per-Post visual-data.json Format

Every week's process folder should include a `visual-data.json` with instructions for the Artist agent or image generator:

```json
{
  "week": "W25",
  "template": "A",
  "primary_stat": "$53",
  "stat_label": "per invoice exception",
  "supporting_line": "Organizations with a supplier portal report 73% fewer exceptions.",
  "source": "Ardent Partners, 2024",
  "hex_icon": "invoice",
  "color_scheme": "dark",
  "accent_color": "#DC2626",
  "stat_color": "#0D9488",
  "background": "#1E1030",
  "publish_date": "2026-06-15"
}
```

**Template options:** `"A"` (stat), `"B"` (insight), `"C"` (comparison)
**Color scheme options:** `"dark"` (Template A), `"light"` (Template B), `"split"` (Template C)
**hex_icon options:** `"invoice"`, `"supplier"`, `"bank"`, `"chart"`, `"shield"`, `"globe"`, `"erp"`

---

## 6. What to Avoid (Visual)

| Avoid | Use Instead |
|-------|-------------|
| Navy blue `#003D82` (old brand) | Purple `#7C3AED` or Teal `#0D9488` |
| Stock photography | Pure typography + data cards |
| More than 3 colors per card | 2 colors max + white |
| Centered body text | Left-aligned (right-align stats) |
| Emojis in visuals | Hexagon icon system |
| Cluttered layouts | One stat. One idea. White space. |
| Gradient text effects | Solid color on contrast background |
| Watermarks or copyright banners | Bottom strip with logo only |

---

## 7. Application by Post Category

| Category | Template | Stat Color | Background |
|----------|----------|------------|------------|
| דיוק וחיסכון / Cost & Accuracy | A (Stat) | Teal | Dark |
| רגולציה / Compliance | A (Stat) | Coral | Dark |
| כנסים / Thought Leadership | B (Insight) | Purple | Light |
| תשתית / Infrastructure | B (Insight) | Teal | Light |
| Comparison / ROI proof | C (Split) | Both | Split |

---

## 8. W25 Visual Spec (First Implementation)

```json
{
  "week": "W25",
  "template": "A",
  "primary_stat": "$53",
  "stat_label": "per invoice exception (direct handling only)",
  "supporting_line": "73% fewer exceptions with a centralized supplier portal.",
  "source": "Ardent Partners, 2024",
  "hex_icon": "invoice",
  "color_scheme": "dark",
  "accent_color": "#DC2626",
  "stat_color": "#0D9488",
  "background": "#1E1030",
  "secondary_stat": "$5,300 / month at 100 exceptions",
  "publish_date": "2026-06-15"
}
```

---

*This document is the authoritative visual spec for all StoreNext LinkedIn post graphics.*
*Update Section 8 each week with the current post's visual-data.json.*
