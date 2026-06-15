#!/usr/bin/env python3
"""
StoreNext Visual Generator
Reads visual-data.json → outputs PNG per post
Usage: python3 T-tools/generate-visual.py O-output/W26/process/visual-data.json
"""

import json
import sys
import os
from PIL import Image, ImageDraw, ImageFont

# Brand colors
NAVY      = "#003D82"
TEAL      = "#00A896"
WHITE     = "#FFFFFF"
GRAY      = "#47525E"
RED       = "#EE404A"
DARK_TEXT = "#1A1A2E"

W, H = 1080, 1350  # LinkedIn optimal

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

def draw_text_centered(draw, text, y, font, color, width=W, max_width=None):
    max_width = max_width or (width - 80)
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

def draw_logo_text(draw, x, y):
    """Render 'StoreNext' as text logo."""
    font = load_font(22, bold=True)
    draw.text((x, y), "StoreNext", font=font, fill=WHITE)

def stat_card(post):
    """Dark navy card with dominant metric."""
    img = Image.new("RGB", (W, H), hex_to_rgb(NAVY))
    draw = ImageDraw.Draw(img)

    # Top color bar
    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(RED))

    # Logo area
    draw_logo_text(draw, 40, 30)

    # Category chip
    cat_font = load_font(18)
    draw.text((40, 60), post.get("category", "").upper(), font=cat_font,
              fill=hex_to_rgb(TEAL))

    # Main metric — massive
    metric = post.get("key_metric", "")
    metric_font = load_font(140, bold=True)
    bbox = draw.textbbox((0, 0), metric, font=metric_font)
    mx = (W - (bbox[2] - bbox[0])) // 2
    draw.text((mx, 320), metric, font=metric_font, fill=WHITE)

    # Divider line
    draw.rectangle([80, 530, W - 80, 534], fill=hex_to_rgb(TEAL))

    # Hook text
    hook = post.get("hook", "")
    hook_font = load_font(36, bold=True)
    draw_text_centered(draw, hook, 570, hook_font, WHITE, max_width=900)

    # Visual direction note (small, bottom)
    direction = post.get("visual_direction", "")
    dir_font = load_font(20)
    draw_text_centered(draw, direction, 1100, dir_font, hex_to_rgb(GRAY), max_width=900)

    # Bottom teal bar
    draw.rectangle([0, H - 6, W, H], fill=hex_to_rgb(TEAL))

    return img

def process_flow(post):
    """White card with structured 3-4 step flow."""
    img = Image.new("RGB", (W, H), hex_to_rgb(WHITE))
    draw = ImageDraw.Draw(img)

    # Top navy header
    draw.rectangle([0, 0, W, 180], fill=hex_to_rgb(NAVY))
    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(RED))
    draw_logo_text(draw, 40, 30)

    title_font = load_font(38, bold=True)
    draw_text_centered(draw, post.get("topic", ""), 80, title_font, WHITE, max_width=940)

    # Steps — parse from visual_direction
    direction = post.get("visual_direction", "")
    steps = [s.strip() for s in direction.split("→") if s.strip()]
    if not steps:
        steps = [direction]

    step_font = load_font(30, bold=True)
    label_font = load_font(22)
    y = 220
    step_h = (H - 280 - 120) // max(len(steps), 1)

    for i, step in enumerate(steps):
        # Circle number
        cx, cy = 80, y + step_h // 2
        draw.ellipse([cx - 28, cy - 28, cx + 28, cy + 28],
                     fill=hex_to_rgb(NAVY))
        num_font = load_font(26, bold=True)
        draw.text((cx - 9, cy - 16), str(i + 1), font=num_font, fill=WHITE)

        # Step text
        draw.text((130, y + step_h // 2 - 18), step, font=step_font,
                  fill=hex_to_rgb(DARK_TEXT))

        # Connector line (not after last)
        if i < len(steps) - 1:
            draw.rectangle([78, y + step_h // 2 + 30,
                             82, y + step_h // 2 + step_h - 10],
                            fill=hex_to_rgb(TEAL))
        y += step_h

    # Hook at bottom
    hook_font = load_font(30, bold=True)
    draw.rectangle([0, H - 160, W, H], fill=hex_to_rgb(NAVY))
    draw_text_centered(draw, post.get("hook", ""), H - 140, hook_font, WHITE, max_width=940)
    draw.rectangle([0, H - 6, W, H], fill=hex_to_rgb(TEAL))

    return img

def quote_card(post):
    """Navy card with large typography hook."""
    img = Image.new("RGB", (W, H), hex_to_rgb(NAVY))
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, W, 8], fill=hex_to_rgb(RED))
    draw_logo_text(draw, 40, 30)

    # Large quote mark
    q_font = load_font(200, bold=True)
    draw.text((30, 80), "“", font=q_font, fill=hex_to_rgb(TEAL))

    # Hook text — large
    hook_font = load_font(52, bold=True)
    y = draw_text_centered(draw, post.get("hook", ""), 280, hook_font, WHITE, max_width=940)

    # Closing quote
    draw.text((W - 110, y + 10), "”", font=q_font, fill=hex_to_rgb(TEAL))

    # Metric callout
    metric = post.get("key_metric", "")
    if metric:
        draw.rectangle([80, y + 120, W - 80, y + 124], fill=hex_to_rgb(TEAL))
        m_font = load_font(60, bold=True)
        draw_text_centered(draw, metric, y + 140, m_font, hex_to_rgb(TEAL))

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
