# Image Post-Processing Skill
# StoreNext Edition

**Used by:** Artist Agent
**Tools:** Python + Pillow (PIL)
**Purpose:** Add text overlays, branding, and resize FLUX-generated images for publication

---

## Platform Dimensions

```python
DIMENSIONS = {
    "linkedin_square":   (1080, 1080),
    "linkedin_portrait": (1080, 1350),
    "article_hero":      (1200, 630),
    "email_header":      (800,  200),
}
```

---

## StoreNext Branding Function

```python
from PIL import Image, ImageDraw, ImageFont
import os

def add_branding_storenext(img: Image.Image) -> Image.Image:
    """
    StoreNext brand: clean corporate white text, precise positioning.
    """
    draw = ImageDraw.Draw(img)
    W, H = img.size

    try:
        font_brand = ImageFont.truetype("arial.ttf", size=int(H * 0.025))
    except:
        font_brand = ImageFont.load_default()

    brand_text = "STORENEXT  |  storenext.com"
    padding = int(W * 0.04)
    bbox = draw.textbbox((0, 0), brand_text, font=font_brand)
    text_w = bbox[2] - bbox[0]
    x = W - text_w - padding
    y = H - padding - (bbox[3] - bbox[1])

    draw.text((x + 2, y + 2), brand_text, font=font_brand, fill=(0, 0, 0, 120))
    draw.text((x, y), brand_text, font=font_brand, fill=(255, 255, 255, 200))
    return img
```

---

## Full Pipeline

```python
def process_for_linkedin(raw_image_path: str, title: str, output_path: str, format: str = "linkedin_portrait") -> str:
    from PIL import Image, ImageDraw, ImageFont
    img = Image.open(raw_image_path).convert("RGB").resize(DIMENSIONS[format], Image.LANCZOS)

    # Overlay
    from PIL import Image as PILImage
    overlay = PILImage.new("RGBA", img.size, (0, 0, 0, 0))
    draw_o = ImageDraw.Draw(overlay)
    H = img.size[1]
    draw_o.rectangle([(0, int(H*0.6)), (img.size[0], H)], fill=(0, 0, 0, 80))
    img = PILImage.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

    # Title
    draw = ImageDraw.Draw(img)
    W, H = img.size
    try:
        font = ImageFont.truetype("arial.ttf", size=int(H * 0.065))
    except:
        font = ImageFont.load_default()
    pad = int(W * 0.05)
    draw.text((pad+2, H - int(H*0.16)+2), title, font=font, fill=(0,0,0,180))
    draw.text((pad, H - int(H*0.16)), title, font=font, fill=(255,255,255,255))

    # Branding
    img = add_branding_storenext(img)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")
    return output_path
```

---

## Output Naming Convention

```
StoreNext/O-output/[WEEK]/[FOLDER]/visual/
├── [name]-flux-raw.png
├── [name]-linkedin-final.png
└── [name]-article-hero.png
```

---

*Image Post-Processing Skill — StoreNext Edition*
*Last updated: 2026-03-16*
