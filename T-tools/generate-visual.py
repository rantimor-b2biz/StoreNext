#!/usr/bin/env python3
"""
StoreNext Visual Generator
Reads visual-data.json → outputs PNG per post
Usage: python3 T-tools/generate-visual.py O-output/W26/process/visual-data.json
"""

import json
import sys
import os
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

LOGO_SVG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "C-core", "storenext-logo.svg")

def load_logo(dark_bg=True, width=220):
    """Render SVG logo to PIL Image. On dark bg: wordmark becomes white."""
    try:
        import cairosvg
        from lxml import etree
        with open(LOGO_SVG_PATH) as f:
            svg_content = f.read()
        parser = etree.XMLParser(recover=True)
        tree = etree.fromstring(svg_content.encode(), parser)
        svg_str = etree.tostring(tree).decode()
        if dark_bg:
            svg_str = svg_str.replace("fill: #432f45", "fill: #FFFFFF")
        png_data = cairosvg.svg2png(bytestring=svg_str.encode(), output_width=width)
        return Image.open(io.BytesIO(png_data)).convert("RGBA")
    except Exception:
        return None

W, H = 1080, 1350  # LinkedIn optimal
MARGIN = 80          # safe zone — text never closer than this to edges

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def load_font(size, bold=False):
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


def fit_font(draw, text, max_width, max_size, bold=False, min_size=40):
    """Reduce font size until text fits within max_width."""
    size = max_size
    while size >= min_size:
        font = load_font(size, bold=bold)
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

def add_glow(img, cx, cy, radius, color_rgb, alpha_max=60):
    """Paint a soft radial glow blob onto the image."""
    import math
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    for r in range(radius, 0, -radius // 20):
        a = int(alpha_max * (1 - r / radius) ** 2)
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        d.ellipse([cx - r, cy - r, cx + r, cy + r],
                  fill=(*color_rgb, a))
        overlay = Image.alpha_composite(overlay, layer)
    img_rgba = img.convert("RGBA")
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    return img_rgba.convert("RGB")

def stat_card(post):
    """Redesigned stat card matching premium B2B style: glow bg, left-aligned metric, pill badge, body text, logo+domain footer."""
    bg = hex_to_rgb(DEEP_PURPLE)
    img = Image.new("RGB", (W, H), bg)

    # Soft purple glow — top-right
    img = add_glow(img, cx=W - 100, cy=200, radius=600,
                   color_rgb=hex_to_rgb(BRAND_PURPLE), alpha_max=70)

    # Rounded card inset (subtle — just darker border feel via draw)
    draw = ImageDraw.Draw(img)

    # ── Metric block (top-left) ──────────────────────────────────────────────
    metric = post.get("key_metric", "")
    metric_font, _ = fit_font(draw, metric, W - MARGIN * 2, 180, bold=True, min_size=80)
    draw.text((MARGIN, 160), metric, font=metric_font, fill=hex_to_rgb(TEAL))
    metric_bbox = draw.textbbox((MARGIN, 160), metric, font=metric_font)
    metric_bottom = metric_bbox[3]

    # Metric label (topic as subtitle under metric)
    topic = post.get("topic", "")
    label_font = load_font(32)
    draw.text((MARGIN, metric_bottom + 12), topic, font=label_font,
              fill=hex_to_rgb(MUTED_TEXT))
    label_bbox = draw.textbbox((MARGIN, metric_bottom + 12), topic, font=label_font)
    label_bottom = label_bbox[3]

    # Source line
    source = post.get("source", "")
    if source:
        src_font = load_font(22)
        draw.text((MARGIN, label_bottom + 8), source, font=src_font,
                  fill=hex_to_rgb(MUTED_TEXT))
        label_bottom = draw.textbbox((MARGIN, label_bottom + 8), source, font=src_font)[3]

    # ── Teal divider ─────────────────────────────────────────────────────────
    div_y = label_bottom + 40
    draw.rectangle([MARGIN, div_y, W - MARGIN, div_y + 2], fill=hex_to_rgb(TEAL))

    # ── Pill / badge ─────────────────────────────────────────────────────────
    badge = post.get("badge", "")
    pill_y = div_y + 28
    if badge:
        badge_font = load_font(26)
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

    # ── Hook / body text ─────────────────────────────────────────────────────
    hook = post.get("hook", "")
    body_font = load_font(34)
    body_bold_font = load_font(34, bold=True)

    # Split hook at last sentence to bold it (the punchy stat line)
    sentences = hook.split(". ")
    body_y = pill_y
    max_w = W - MARGIN * 2
    for i, sentence in enumerate(sentences):
        txt = sentence if sentence.endswith(".") else sentence + ("." if i < len(sentences) - 1 else "")
        font = body_bold_font if i == len(sentences) - 1 else body_font
        color = WHITE if i == len(sentences) - 1 else hex_to_rgb(MUTED_TEXT)
        # manually handle color: first sentences muted, last bold white
        if len(sentences) == 1:
            font, color = body_bold_font, WHITE
        body_y = draw_text_left(draw, txt, MARGIN, body_y, font, color, max_w)
        body_y += 6

    # ── Footer: logo left + domain right ────────────────────────────────────
    footer_y = H - 110
    paste_logo(img, dark_bg=True, x=MARGIN, y=footer_y, width=180)

    domain_font = load_font(24)
    domain = "storenext.co.il"
    d_bbox = draw.textbbox((0, 0), domain, font=domain_font)
    draw.text((W - MARGIN - (d_bbox[2] - d_bbox[0]), footer_y + 22),
              domain, font=domain_font, fill=hex_to_rgb(MUTED_TEXT))

    # Bottom teal line
    draw.rectangle([0, H - 8, W, H], fill=hex_to_rgb(CORAL_RED))

    return img

def process_flow(post):
    """Light purple card with 3-step flow."""
    img = Image.new("RGB", (W, H), hex_to_rgb(LIGHT_PURPLE))
    draw = ImageDraw.Draw(img)

    # Top deep purple header
    draw.rectangle([0, 0, W, 190], fill=hex_to_rgb(DEEP_PURPLE))
    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(CORAL_RED))
    paste_logo(img, dark_bg=True, x=MARGIN, y=32, width=200)

    title_font = load_font(36, bold=True)
    draw_text_centered(draw, post.get("topic", ""), 85, title_font, WHITE, max_width=W - MARGIN * 2)

    # Steps from visual_direction
    direction = post.get("visual_direction", "")
    steps_raw = [s.strip() for s in direction.split("→") if s.strip()]
    # Take only the step labels (first sentence fragment of each)
    steps = []
    for s in steps_raw:
        label = s.split(".")[0].strip()
        steps.append(label if label else s[:40])
    if not steps:
        steps = ["Start", "Process", "Result"]

    step_font = load_font(28, bold=True)
    y = 230
    step_h = (H - 310 - 160) // max(len(steps), 1)

    for i, step in enumerate(steps):
        cx, cy = 80, y + step_h // 2
        # Circle
        draw.ellipse([cx - 30, cy - 30, cx + 30, cy + 30],
                     fill=hex_to_rgb(BRAND_PURPLE))
        num_font = load_font(28, bold=True)
        nw = draw.textbbox((0,0), str(i+1), font=num_font)
        draw.text((cx - (nw[2]-nw[0])//2, cy - (nw[3]-nw[1])//2),
                  str(i+1), font=num_font, fill=WHITE)
        draw.text((MARGIN + 60, cy - 18), step, font=step_font, fill=hex_to_rgb(DARK_TEXT))

        if i < len(steps) - 1:
            draw.rectangle([77, cy + 32, 83, cy + step_h - 10],
                           fill=hex_to_rgb(TEAL))
        y += step_h

    # Hook footer
    hook_font = load_font(30, bold=True)
    draw.rectangle([0, H - 170, W, H], fill=hex_to_rgb(DEEP_PURPLE))
    draw_text_centered(draw, post.get("hook", ""), H - 150, hook_font, WHITE, max_width=W - MARGIN * 2)
    draw.rectangle([0, H - 6, W, H], fill=hex_to_rgb(TEAL))

    return img

def quote_card(post):
    """Deep purple card with large typography hook."""
    img = Image.new("RGB", (W, H), hex_to_rgb(DEEP_PURPLE))
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(CORAL_RED))
    paste_logo(img, dark_bg=True, x=MARGIN, y=30, width=200)

    # Large quote mark in brand purple
    q_font = load_font(200, bold=True)
    draw.text((30, 80), "\u201c", font=q_font, fill=hex_to_rgb(BRAND_PURPLE))

    # Hook text
    hook_font = load_font(50, bold=True)
    hook_y = draw_text_centered(draw, post.get("hook", ""), 290, hook_font, WHITE, max_width=W - MARGIN * 2)

    draw.text((W - 120, hook_y + 10), "\u201d", font=q_font, fill=hex_to_rgb(BRAND_PURPLE))

    # Metric callout in teal
    metric = post.get("key_metric", "")
    if metric:
        draw.rectangle([MARGIN, hook_y + 110, W - MARGIN, hook_y + 114], fill=hex_to_rgb(TEAL))
        m_font = load_font(60, bold=True)
        draw_text_centered(draw, metric, hook_y + 130, m_font, hex_to_rgb(TEAL))

    draw.rectangle([0, H - 6, W, H], fill=hex_to_rgb(TEAL))
    return img

GENERATORS = {
    "stat_card":    stat_card,
    "process_flow": process_flow,
    "quote_card":   quote_card,
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
