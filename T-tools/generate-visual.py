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

def stat_card(post):
    """Deep purple card with dominant metric — brand colors."""
    img = Image.new("RGB", (W, H), hex_to_rgb(DEEP_PURPLE))
    draw = ImageDraw.Draw(img)

    # Top coral accent strip
    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(CORAL_RED))

    # Logo
    paste_logo(img, dark_bg=True, x=MARGIN, y=30, width=200)

    # Category chip
    cat_font = load_font(18)
    draw.text((MARGIN, 80), post.get("category", "").upper(), font=cat_font,
              fill=hex_to_rgb(TEAL))

    # Main metric — massive, teal
    metric = post.get("key_metric", "")
    metric_font, _ = fit_font(draw, metric, W - MARGIN * 2, 130, bold=True)
    bbox = draw.textbbox((0, 0), metric, font=metric_font)
    mx = (W - (bbox[2] - bbox[0])) // 2
    draw.text((mx, 310), metric, font=metric_font, fill=hex_to_rgb(TEAL))

    # Divider
    draw.rectangle([MARGIN, 530, W - MARGIN, 534], fill=hex_to_rgb(BRAND_PURPLE))

    # Hook text
    hook_font = load_font(36, bold=True)
    draw_text_centered(draw, post.get("hook", ""), 565, hook_font, WHITE, max_width=W - MARGIN * 2)

    # Bottom brand purple bar
    draw.rectangle([0, H - 6, W, H], fill=hex_to_rgb(BRAND_PURPLE))

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
