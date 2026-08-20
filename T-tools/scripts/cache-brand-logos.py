#!/usr/bin/env python3
"""
Cache the brand SVG logos as transparent PNGs for T-tools/generate-visual.py.

Why this exists
---------------
generate-visual.py rasterizes C-core/*.svg with cairosvg. cairosvg needs the
native libcairo library, which GitHub Actions has and a stock Windows box does
not. When it is missing, the visual generator silently falls back to drawing the
word "StoreNext" as plain text, losing the hexagon symbol. That shipped once, on
a locally regenerated W34 visual, on 2026-08-20.

Caching a PNG next to each SVG removes the native dependency entirely, so a
visual generated on Ran's laptop is byte-identical in branding to one generated
in CI.

Usage
-----
    python T-tools/scripts/cache-brand-logos.py

Re-run this whenever a logo SVG in C-core/ changes. The PNGs are committed.
Rendering uses headless Edge or Chrome, which every Windows 11 machine has.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "C-core"

# Recolor pairs applied for the dark-background ("-white") variant.
DARK_REPLACEMENTS = [
    "#432f45", "#432F45", "#3a2a3d", "#3A2A3D",
    "#2b1e2e", "#2B1E2E", "#231018", "#1e1030", "#1E1030",
]

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def find_browser():
    for path in BROWSERS:
        if os.path.exists(path):
            return path
    for name in ("msedge", "chrome", "chromium", "google-chrome"):
        from shutil import which
        found = which(name)
        if found:
            return found
    return None


def svg_viewbox(svg_text):
    """Return (width, height) from the viewBox, defaulting to a sane ratio."""
    import re
    match = re.search(r'viewBox\s*=\s*["\']([\d.\s-]+)["\']', svg_text)
    if match:
        parts = [float(p) for p in match.group(1).split()]
        if len(parts) == 4 and parts[2] > 0 and parts[3] > 0:
            return parts[2], parts[3]
    return 132.0, 24.0


def render(svg_path, out_path, white=False, target_width=880):
    browser = find_browser()
    if not browser:
        print("ERROR: no Edge or Chrome found to render with", file=sys.stderr)
        return False

    svg_text = svg_path.read_text(encoding="utf-8")
    if white:
        for dark in DARK_REPLACEMENTS:
            svg_text = svg_text.replace(dark, "#FFFFFF")

    vb_w, vb_h = svg_viewbox(svg_text)
    height = int(round(target_width * vb_h / vb_w))

    html = (
        "<!doctype html><html><head><meta charset='utf-8'><style>"
        "html,body{margin:0;padding:0;background:transparent;}"
        f"svg{{display:block;width:{target_width}px;height:{height}px;}}"
        "</style></head><body>" + svg_text + "</body></html>"
    )

    tmpdir = tempfile.mkdtemp()
    html_path = Path(tmpdir) / "logo.html"
    shot_path = Path(tmpdir) / "shot.png"
    html_path.write_text(html, encoding="utf-8")

    cmd = [
        browser, "--headless", "--disable-gpu", "--hide-scrollbars",
        "--default-background-color=00000000",
        f"--window-size={target_width},{height}",
        f"--screenshot={shot_path}",
        html_path.as_uri(),
    ]
    subprocess.run(cmd, capture_output=True, timeout=120)

    if not shot_path.exists():
        print(f"ERROR: browser produced no screenshot for {svg_path.name}", file=sys.stderr)
        return False

    from PIL import Image
    img = Image.open(shot_path).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    img.save(out_path)
    print(f"  {out_path.relative_to(ROOT)}  {img.size[0]}x{img.size[1]}")
    return True


def main():
    targets = [
        (CORE / "storenext-logo.svg", CORE / "storenext-logo-white.png", True),
        (CORE / "storenext-logo.svg", CORE / "storenext-logo.png", False),
    ]
    ok = True
    print("Caching brand logos:")
    for svg, png, white in targets:
        if not svg.exists():
            print(f"  skip, missing {svg.name}")
            continue
        if not render(svg, png, white=white):
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
