#!/usr/bin/env python3
"""
One-off test: Generate geopolitical crisis visual for StoreNext W11 post
Model: black-forest-labs/flux-2-pro
Output: StoreNext/O-output/W11/final/geopolitical-crisis-supply-chain-visual-v2.jpg
"""

import os
import sys
import urllib.request
from pathlib import Path

try:
    import replicate
except ImportError:
    print("Install: pip install replicate")
    sys.exit(1)

os.environ["REPLICATE_API_TOKEN"] = os.environ.get("REPLICATE_API_TOKEN", "")

MODEL = "black-forest-labs/flux-2-pro"
OUTPUT_PATH = Path("StoreNext/O-output/W11/final/geopolitical-crisis-supply-chain-visual-v2.jpg")

PROMPT = """Professional enterprise B2B image: Global supply chain network visualization.

World map silhouette rendered in deep navy blue on a clean white background.
Major shipping routes shown as thin teal glowing lines connecting continents.
Middle East region highlighted with a subtle amber/orange glow — not alarming, just significant.
Several route lines pulse or fade near the highlighted region, representing uncertainty.

On the right side of the image: a vertical column of 6-8 corporate supplier icons (simple geometric company logos) connected by teal lines flowing into one central enterprise hub icon — representing the Supplier Portal.
The hub glows steadily in teal, calm and in control despite the disruption on the map.

Top-left corner: faint text watermark "Supplier Visibility" in light gray.

Visual metaphor: while the world is disrupted, the enterprise with a centralized supplier platform maintains clarity and control.

Corporate aesthetic: clean, minimal, professional. No people, no drama. Pure data visualization feel.
Navy blue (#1B3A6B), teal (#00B4C5), white background, amber accent (#F5A623) only for the disruption zone.
3D depth, subtle shadows, crisp lines. LinkedIn format 4:5 ratio."""

def main():
    print("=" * 60)
    print("StoreNext - Geopolitical Crisis Visual (Flux 2 Pro TEST)")
    print("=" * 60)
    print(f"Model: {MODEL}")
    print(f"Output: {OUTPUT_PATH}")
    print()
    print("Generating...")

    try:
        output = replicate.run(
            MODEL,
            input={
                "prompt": PROMPT,
                "aspect_ratio": "4:5",
                "output_format": "jpg",
                "output_quality": 90,
            },
        )

        # Parse output URL
        if isinstance(output, list) and len(output) > 0:
            item = output[0]
            image_url = str(item.url) if hasattr(item, "url") else str(item)
        elif hasattr(output, "url"):
            image_url = str(output.url)
        else:
            image_url = str(output)

        print("Image generated. Downloading...")

        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(image_url, OUTPUT_PATH)

        size_kb = OUTPUT_PATH.stat().st_size / 1024
        print()
        print(f"SAVED: {OUTPUT_PATH}")
        print(f"Size:  {size_kb:.1f} KB")
        print()
        print("Done. Review the image before publishing.")

    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
