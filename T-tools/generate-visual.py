#!/usr/bin/env python3
"""
StoreNext Visual Generator
Reads visual-data.json → outputs PNG per post
Usage: python3 T-tools/generate-visual.py O-output/W26/process/visual-data.json
"""

import json
import sys
import os
import math
import io
from PIL import Image, ImageDraw, ImageFont

# Brand colors — per C-core/brand-standards.md (updated 2026-06-08)
DEEP_PURPLE   = "#1E1030"   # dark card backgrounds
BRAND_PURPLE  = "#7C3AED"   # primary — logos, icons, headers
TEAL          = "#0D9488"   # financial data, secondary accent
CORAL_RED     = "#DC2626"   # CTA buttons, accent strips
LIGHT_PURPLE  = "#F5F0FF"   # light card backgrounds
DARK_TEXT     = "#1A1A2E"   # headlines on light bg
MUTED_TEXT    = "#6B7280"   # body / captions
WHITE         = "#FFFFFF"

CORE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "C-core")
LOGO_SVG_PATH   = os.path.join(CORE_DIR, "storenext-logo.svg")
METEOR_SVG_PATH = os.path.join(CORE_DIR, "meteor-logo.svg")

def _render_svg(path, dark_bg=True, width=220, recolor=("fill: #432f45", "fill: #FFFFFF")):
    """Render an SVG file to a PIL RGBA image. On dark bg, recolor dark wordmark to white."""
    try:
        import cairosvg
        from lxml import etree
        with open(path) as f:
            svg_content = f.read()
        parser = etree.XMLParser(recover=True)
        tree = etree.fromstring(svg_content.encode(), parser)
        svg_str = etree.tostring(tree).decode()
        if dark_bg and recolor:
            svg_str = svg_str.replace(recolor[0], recolor[1])
        png_data = cairosvg.svg2png(bytestring=svg_str.encode(), output_width=width)
        return Image.open(io.BytesIO(png_data)).convert("RGBA")
    except Exception:
        return None

def load_logo(dark_bg=True, width=220):
    """Render the StoreNext SVG logo. On dark bg: wordmark becomes white."""
    return _render_svg(LOGO_SVG_PATH, dark_bg=dark_bg, width=width)

def load_meteor_logo(dark_bg=True, width=240):
    """Render the official Meteor SVG logo if present in C-core; else None.
    On dark backgrounds, recolors the dark-purple wordmark shades to white while
    leaving the coral accent (reds) untouched."""
    if not os.path.exists(METEOR_SVG_PATH):
        return None
    try:
        import cairosvg
        from lxml import etree
        with open(METEOR_SVG_PATH) as f:
            svg = f.read()
        svg = etree.tostring(
            etree.fromstring(svg.encode(), etree.XMLParser(recover=True))).decode()
        if dark_bg:
            for dark in ("#3a2a3d", "#432f45", "#2b1e2e", "#3A2A3D", "#432F45",
                         "#2B1E2E", "#231018", "#1e1030", "#1E1030"):
                svg = svg.replace(dark, "#FFFFFF")
        png = cairosvg.svg2png(bytestring=svg.encode(), output_width=width)
        return Image.open(io.BytesIO(png)).convert("RGBA")
    except Exception:
        return None

W, H = 1080, 1350  # LinkedIn optimal
MARGIN = 80          # safe zone — text never closer than this to edges

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

INTER_VAR_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                              "C-core", "fonts", "Inter-var.ttf")

def load_font(size, bold=False, weight=None):
    """Load Inter (variable) at the requested weight; fall back to DejaVu.

    weight overrides bold. Inter weight names: Thin, ExtraLight, Light,
    Regular, Medium, SemiBold, Bold, ExtraBold, Black.
    """
    target = weight or ("Bold" if bold else "Regular")
    if os.path.exists(INTER_VAR_PATH):
        try:
            font = ImageFont.truetype(INTER_VAR_PATH, size)
            try:
                font.set_variation_by_name(target)
            except Exception:
                pass
            return font
        except Exception:
            pass
    paths = [
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'Bold' if bold else ''}.ttf",
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans-{'Bold' if bold else 'Book'}.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def fit_font(draw, text, max_width, max_size, bold=False, min_size=40, weight=None):
    """Reduce font size until text fits within max_width."""
    size = max_size
    while size >= min_size:
        font = load_font(size, bold=bold, weight=weight)
        bbox = draw.textbbox((0, 0), text, font=font)
        if bbox[2] - bbox[0] <= max_width:
            return font, size
        size -= 4
    return load_font(min_size, bold=bold), min_size

def draw_text_centered(draw, text, y, font, color, width=W, max_width=None):
    max_width = max_width or (width - MARGIN * 2)
    words = text.split()
    lines = []
    line = []
    for word in words:
        test = " ".join(line + [word])
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_width and line:
            lines.append(" ".join(line))
            line = [word]
        else:
            line.append(word)
    if line:
        lines.append(" ".join(line))

    for ln in lines:
        bbox = draw.textbbox((0, 0), ln, font=font)
        x = (width - (bbox[2] - bbox[0])) // 2
        draw.text((x, y), ln, font=font, fill=color)
        y += (bbox[3] - bbox[1]) + 12
    return y

def draw_text_left(draw, text, x, y, font, color, max_width):
    """Draw left-aligned wrapped text, return final y."""
    words = text.split()
    lines, line = [], []
    for word in words:
        test = " ".join(line + [word])
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_width and line:
            lines.append(" ".join(line))
            line = [word]
        else:
            line.append(word)
    if line:
        lines.append(" ".join(line))
    for ln in lines:
        draw.text((x, y), ln, font=font, fill=color)
        bbox = draw.textbbox((0, 0), ln, font=font)
        y += (bbox[3] - bbox[1]) + 10
    return y

def paste_logo(img, dark_bg=True, x=40, y=36, width=200):
    """Paste actual SVG logo onto image."""
    logo = load_logo(dark_bg=dark_bg, width=width)
    if logo:
        img.paste(logo, (x, y), logo)
    else:
        draw = ImageDraw.Draw(img)
        font = load_font(22, bold=True)
        color = WHITE if dark_bg else hex_to_rgb(DEEP_PURPLE)
        draw.text((x, y), "StoreNext", font=font, fill=color)

def draw_rounded_rect(draw, xy, radius, fill):
    """Draw a filled rounded rectangle."""
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill)
    draw.ellipse([x0, y0, x0 + radius * 2, y0 + radius * 2], fill=fill)
    draw.ellipse([x1 - radius * 2, y0, x1, y0 + radius * 2], fill=fill)
    draw.ellipse([x0, y1 - radius * 2, x0 + radius * 2, y1], fill=fill)
    draw.ellipse([x1 - radius * 2, y1 - radius * 2, x1, y1], fill=fill)

def add_glow(img, cx, cy, radius, color_rgb, alpha_max=60):
    """Paint a soft radial glow blob onto the image."""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    for r in range(radius, 0, -radius // 20):
        a = int(alpha_max * (1 - r / radius) ** 2)
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color_rgb, a))
        overlay = Image.alpha_composite(overlay, layer)
    img_rgba = img.convert("RGBA")
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    return img_rgba.convert("RGB")

def _hexagon_points(cx, cy, r):
    """Flat-top hexagon vertices (matches the Meteor / StoreNext cube mark)."""
    return [(cx + r * math.cos(math.radians(60 * i)),
             cy + r * math.sin(math.radians(60 * i))) for i in range(6)]

def draw_meteor_logo(draw, x, y, height=46):
    """Faithful Meteor wordmark: 'METE' + hexagon 'O' + 'R', with tagline.
    Wordmark white on dark bg; hexagon white outline with a coral accent segment.
    Recreated in vector form pending an official Meteor SVG in C-core."""
    font = load_font(int(height * 0.92), weight="ExtraBold")

    pre, post = "METE", "R"
    draw.text((x, y), pre, font=font, fill=WHITE)
    w_pre = draw.textbbox((x, y), pre, font=font)[2] - x

    # Hexagon as the 'O'
    r = int(height * 0.44)
    gap = int(height * 0.14)
    hx = x + w_pre + gap + r
    hy = y + int(height * 0.5)
    pts = _hexagon_points(hx, hy, r)
    stroke = max(4, int(height * 0.11))
    for i in range(6):
        a, b = pts[i], pts[(i + 1) % 6]
        # top-right two edges rendered in coral (the brand accent)
        col = CORAL_RED if i in (4, 5) else WHITE
        draw.line([a, b], fill=hex_to_rgb(col), width=stroke)

    # 'R' after the hexagon
    rx = hx + r + gap
    draw.text((rx, y), post, font=font, fill=WHITE)

    # Tagline
    tag_font = load_font(int(height * 0.30), weight="Medium")
    draw.text((x + 2, y + height + 4), "A StoreNext Company",
              font=tag_font, fill=hex_to_rgb(MUTED_TEXT))

def _draw_footer(img, draw, brand="storenext"):
    """Shared footer: brand logo left + domain right + coral bottom line.
    brand='meteor' switches to the Meteor wordmark and the /meteor domain."""
    footer_y = H - 110
    if brand == "meteor":
        logo = load_meteor_logo(dark_bg=True, width=230)
        if logo:
            img.paste(logo, (MARGIN, footer_y + 8), logo)
        else:
            draw_meteor_logo(draw, MARGIN, footer_y + 6, height=46)
        domain = "storenext.co.il/meteor"
    else:
        paste_logo(img, dark_bg=True, x=MARGIN, y=footer_y, width=180)
        domain = "storenext.co.il"
    domain_font = load_font(24)
    d_bbox = draw.textbbox((0, 0), domain, font=domain_font)
    draw.text((W - MARGIN - (d_bbox[2] - d_bbox[0]), footer_y + 22),
              domain, font=domain_font, fill=hex_to_rgb(MUTED_TEXT))
    draw.rectangle([0, H - 8, W, H], fill=hex_to_rgb(CORAL_RED))

# ── Generators ────────────────────────────────────────────────────────────────

def stat_card(post):
    """Glow bg, left-aligned metric, pill badge, body text, shared footer."""
    img = Image.new("RGB", (W, H), hex_to_rgb(DEEP_PURPLE))
    img = add_glow(img, cx=W - 100, cy=200, radius=600,
                   color_rgb=hex_to_rgb(BRAND_PURPLE), alpha_max=70)
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(CORAL_RED))

    # Metric
    metric = post.get("key_metric", "")
    metric_font, _ = fit_font(draw, metric, W - MARGIN * 2, 200, min_size=90, weight="ExtraBold")
    draw.text((MARGIN, 160), metric, font=metric_font, fill=hex_to_rgb(TEAL))
    metric_bbox = draw.textbbox((MARGIN, 160), metric, font=metric_font)
    metric_bottom = metric_bbox[3]

    # Topic label
    topic = post.get("topic", "")
    label_font = load_font(32, weight="Medium")
    draw.text((MARGIN, metric_bottom + 12), topic, font=label_font,
              fill=hex_to_rgb(MUTED_TEXT))
    label_bbox = draw.textbbox((MARGIN, metric_bottom + 12), topic, font=label_font)
    label_bottom = label_bbox[3]

    # Source
    source = post.get("source", "")
    if source:
        src_font = load_font(22)
        draw.text((MARGIN, label_bottom + 8), source, font=src_font,
                  fill=hex_to_rgb(MUTED_TEXT))
        label_bottom = draw.textbbox((MARGIN, label_bottom + 8), source, font=src_font)[3]

    # Teal divider
    div_y = label_bottom + 40
    draw.rectangle([MARGIN, div_y, W - MARGIN, div_y + 2], fill=hex_to_rgb(TEAL))

    # Badge pill
    badge = post.get("badge", "")
    pill_y = div_y + 28
    if badge:
        badge_font = load_font(26, weight="SemiBold")
        badge_bbox = draw.textbbox((0, 0), badge, font=badge_font)
        bw = badge_bbox[2] - badge_bbox[0] + 48
        bh = 54
        draw_rounded_rect(draw, [MARGIN, pill_y, MARGIN + bw, pill_y + bh],
                          radius=27, fill=hex_to_rgb(TEAL))
        draw.text((MARGIN + 24, pill_y + 10), badge, font=badge_font,
                  fill=hex_to_rgb(DEEP_PURPLE))
        pill_y += bh + 36
    else:
        pill_y += 20

    # Hook body
    hook = post.get("hook", "")
    body_font = load_font(34, weight="Regular")
    body_bold_font = load_font(34, weight="SemiBold")
    sentences = hook.split(". ")
    body_y = pill_y
    max_w = W - MARGIN * 2
    for i, sentence in enumerate(sentences):
        txt = sentence if sentence.endswith(".") else sentence + ("." if i < len(sentences) - 1 else "")
        if len(sentences) == 1:
            font, color = body_bold_font, WHITE
        else:
            font = body_bold_font if i == len(sentences) - 1 else body_font
            color = WHITE if i == len(sentences) - 1 else hex_to_rgb(MUTED_TEXT)
        body_y = draw_text_left(draw, txt, MARGIN, body_y, font, color, max_w)
        body_y += 6

    _draw_footer(img, draw, post.get("brand", "storenext"))
    return img


def process_flow(post):
    """Glow bg, numbered steps, hook block, shared footer."""
    img = Image.new("RGB", (W, H), hex_to_rgb(DEEP_PURPLE))
    img = add_glow(img, cx=W - 100, cy=150, radius=500,
                   color_rgb=hex_to_rgb(BRAND_PURPLE), alpha_max=60)
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(CORAL_RED))

    # Topic title
    title_font = load_font(36, weight="Bold")
    title_y = draw_text_left(draw, post.get("topic", ""), MARGIN, 40,
                             title_font, WHITE, W - MARGIN * 2)

    # Teal divider
    div_y = title_y + 24
    draw.rectangle([MARGIN, div_y, W - MARGIN, div_y + 2], fill=hex_to_rgb(TEAL))

    # Steps from visual_direction
    direction = post.get("visual_direction", "")
    steps_raw = [s.strip() for s in direction.split("→") if s.strip()]
    steps = []
    for s in steps_raw:
        label = s.split(".")[0].strip()
        steps.append(label if label else s[:50])
    if not steps:
        steps = ["Identify", "Automate", "Measure"]

    step_font = load_font(30, weight="SemiBold")
    y = div_y + 40
    FOOTER_RESERVE = 220
    available = H - FOOTER_RESERVE - y
    step_h = available // max(len(steps), 1)

    for i, step in enumerate(steps):
        cy = y + step_h // 2
        draw.ellipse([MARGIN, cy - 28, MARGIN + 56, cy + 28],
                     fill=hex_to_rgb(BRAND_PURPLE))
        num_font = load_font(28, weight="Bold")
        nb = draw.textbbox((0, 0), str(i + 1), font=num_font)
        draw.text((MARGIN + 28 - (nb[2] - nb[0]) // 2,
                   cy - (nb[3] - nb[1]) // 2),
                  str(i + 1), font=num_font, fill=WHITE)
        draw.text((MARGIN + 72, cy - 18), step, font=step_font, fill=WHITE)
        if i < len(steps) - 1:
            draw.rectangle([MARGIN + 25, cy + 30, MARGIN + 31, cy + step_h - 10],
                           fill=hex_to_rgb(TEAL))
        y += step_h

    # Hook block above footer
    hook_y = H - FOOTER_RESERVE + 10
    draw.rectangle([MARGIN, hook_y - 10, W - MARGIN, hook_y - 8], fill=hex_to_rgb(TEAL))
    hook_font = load_font(32, weight="Bold")
    draw_text_left(draw, post.get("hook", ""), MARGIN, hook_y + 10,
                   hook_font, WHITE, W - MARGIN * 2)

    _draw_footer(img, draw, post.get("brand", "storenext"))
    return img


def quote_card(post):
    """Glow bg, large quote typography, metric + badge, shared footer."""
    img = Image.new("RGB", (W, H), hex_to_rgb(DEEP_PURPLE))
    img = add_glow(img, cx=200, cy=300, radius=600,
                   color_rgb=hex_to_rgb(BRAND_PURPLE), alpha_max=65)
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(CORAL_RED))

    q_font = load_font(180, weight="Black")
    draw.text((MARGIN - 10, 50), "“", font=q_font, fill=hex_to_rgb(BRAND_PURPLE))

    hook_font = load_font(52, weight="Bold")
    hook_y = draw_text_centered(draw, post.get("hook", ""), 260,
                                hook_font, WHITE, max_width=W - MARGIN * 2)

    draw.text((W - MARGIN - 80, hook_y + 10), "”", font=q_font,
              fill=hex_to_rgb(BRAND_PURPLE))

    metric = post.get("key_metric", "")
    if metric:
        div_y = hook_y + 120
        draw.rectangle([MARGIN, div_y, W - MARGIN, div_y + 2], fill=hex_to_rgb(TEAL))
        m_font, _ = fit_font(draw, metric, W - MARGIN * 2, 100, min_size=50, weight="ExtraBold")
        m_bbox = draw.textbbox((0, 0), metric, font=m_font)
        mx = (W - (m_bbox[2] - m_bbox[0])) // 2
        draw.text((mx, div_y + 24), metric, font=m_font, fill=hex_to_rgb(TEAL))

        badge = post.get("badge", "")
        if badge:
            b_font = load_font(26)
            b_bbox = draw.textbbox((0, 0), badge, font=b_font)
            bw = b_bbox[2] - b_bbox[0] + 48
            bx = (W - bw) // 2
            by = div_y + 24 + (m_bbox[3] - m_bbox[1]) + 20
            draw_rounded_rect(draw, [bx, by, bx + bw, by + 50],
                              radius=25, fill=hex_to_rgb(TEAL))
            draw.text((bx + 24, by + 10), badge, font=b_font,
                      fill=hex_to_rgb(DEEP_PURPLE))

    _draw_footer(img, draw, post.get("brand", "storenext"))
    return img


def threshold_drop(post):
    """Two date-anchored thresholds with a dramatic downward arrow between them.

    Reads `visual_direction` as two milestone strings separated by '→':
      "JAN 1, 2026 | NIS 10,000 → JUN 1, 2026 | NIS 5,000"
    Each milestone is 'DATE LABEL | BIG VALUE'. Emphasis on the second (the drop).
    """
    img = Image.new("RGB", (W, H), hex_to_rgb(DEEP_PURPLE))
    img = add_glow(img, cx=W // 2, cy=H // 2, radius=650,
                   color_rgb=hex_to_rgb(BRAND_PURPLE), alpha_max=55)
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(CORAL_RED))

    # Kicker + title
    kicker_font = load_font(24, weight="SemiBold")
    draw.text((MARGIN, 46), post.get("category", "").upper(), font=kicker_font,
              fill=hex_to_rgb(TEAL))
    title_font = load_font(40, weight="Bold")
    title_y = draw_text_left(draw, post.get("topic", ""), MARGIN, 84,
                             title_font, WHITE, W - MARGIN * 2)

    # Parse milestones
    direction = post.get("visual_direction", "")
    parts = [p.strip() for p in direction.split("→") if p.strip()]
    milestones = []
    for p in parts:
        if "|" in p:
            label, value = p.split("|", 1)
            milestones.append((label.strip(), value.strip()))
    if len(milestones) < 2:
        milestones = [("JAN 1, 2026", "NIS 10,000"), ("JUN 1, 2026", "NIS 5,000")]

    ARROW_ZONE = 200   # reserved column on the right for the arrow
    val_max_w = W - MARGIN * 2 - ARROW_ZONE

    def draw_milestone(cy, date_label, value, emphasis):
        chip_font = load_font(26, weight="Bold")
        cb = draw.textbbox((0, 0), date_label, font=chip_font)
        cw = cb[2] - cb[0] + 44
        chip_col = CORAL_RED if emphasis else BRAND_PURPLE
        draw_rounded_rect(draw, [MARGIN, cy, MARGIN + cw, cy + 48],
                          radius=24, fill=hex_to_rgb(chip_col))
        draw.text((MARGIN + 22, cy + 8), date_label, font=chip_font, fill=WHITE)
        # Big value (kept clear of the arrow column)
        val_color = WHITE if emphasis else TEAL
        val_font, _ = fit_font(draw, value, val_max_w, 150,
                               min_size=72, weight="ExtraBold")
        draw.text((MARGIN, cy + 58), value, font=val_font, fill=hex_to_rgb(val_color))
        vb = draw.textbbox((MARGIN, cy + 58), value, font=val_font)
        return vb[3]

    y1 = title_y + 50
    y1_bottom = draw_milestone(y1, milestones[0][0], milestones[0][1], emphasis=False)

    y2 = y1_bottom + 190
    y2_bottom = draw_milestone(y2, milestones[1][0], milestones[1][1], emphasis=True)

    # Downward arrow spanning the two milestones, in the reserved right column
    arrow_cx = W - MARGIN - 70
    arrow_top = y1 + 30
    arrow_bottom = y2 + 40
    draw.line([(arrow_cx, arrow_top), (arrow_cx, arrow_bottom)],
              fill=hex_to_rgb(CORAL_RED), width=10)
    draw.polygon([(arrow_cx - 34, arrow_bottom - 6),
                  (arrow_cx + 34, arrow_bottom - 6),
                  (arrow_cx, arrow_bottom + 46)], fill=hex_to_rgb(CORAL_RED))
    # Drop label in the gap between the two milestones, left of the arrow
    drop_font = load_font(40, weight="ExtraBold")
    dl = "-50%"
    db = draw.textbbox((0, 0), dl, font=drop_font)
    draw.text((arrow_cx - 40 - (db[2] - db[0]), (y1_bottom + y2) // 2 - 20),
              dl, font=drop_font, fill=hex_to_rgb(CORAL_RED))

    # Divider + consequence hook
    div_y = y2_bottom + 50
    draw.rectangle([MARGIN, div_y, W - MARGIN, div_y + 2], fill=hex_to_rgb(TEAL))
    hook_font = load_font(32, weight="SemiBold")
    draw_text_left(draw, post.get("hook", ""), MARGIN, div_y + 26,
                   hook_font, WHITE, W - MARGIN * 2)

    _draw_footer(img, draw, post.get("brand", "storenext"))
    return img


GENERATORS = {
    "stat_card":      stat_card,
    "process_flow":   process_flow,
    "quote_card":     quote_card,
    "threshold_drop": threshold_drop,
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate-visual.py <path/to/visual-data.json>")
        sys.exit(1)

    json_path = sys.argv[1]
    out_dir = os.path.join(os.path.dirname(os.path.dirname(json_path)), "final")
    os.makedirs(out_dir, exist_ok=True)

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    posts = data.get("posts", data) if isinstance(data, dict) else data

    for post in posts:
        vtype = post.get("visual_type", "stat_card")
        gen = GENERATORS.get(vtype, stat_card)
        img = gen(post)

        post_id = post.get("post_id", "post")
        out_file = os.path.join(out_dir, f"{post_id}-visual.png")
        img.save(out_file, "PNG", optimize=True)
        print(f"Saved: {out_file}  ({vtype})")

if __name__ == "__main__":
    main()
