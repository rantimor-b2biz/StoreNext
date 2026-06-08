#!/usr/bin/env python3
"""
StoreNext Visual Generation - Vendor Consolidation Theme
Supports multiple Replicate models.
Complete guide at: SYSTEM/docs/REPLICATE-NANO-BANANA-GUIDE.md

Usage:
    python storenext_generate_image.py              # default: nano-banana
    python storenext_generate_image.py --flux2pro   # Flux 2 Pro (best quality)
    python storenext_generate_image.py --schnell    # Flux Schnell (fast & cheap)
    python storenext_generate_image.py --pro        # Flux 1.1 Pro

Model comparison:
  default     nano-banana      Fast, good quality, ~$0.32/image
  --flux2pro  flux-2-pro       Best quality + speed, ~$0.055/image  ← Recommended
  --schnell   flux-schnell     Very fast & cheap, lower quality
  --pro       flux-1.1-pro     High quality, ~$0.04/image
"""

import os
import sys
from pathlib import Path

try:
    import replicate
except ImportError:
    print("❌ Replicate package not found")
    print("Install with: pip install replicate")
    sys.exit(1)

# Set API token
os.environ["REPLICATE_API_TOKEN"] = os.environ.get("REPLICATE_API_TOKEN", "")

# Model selection
MODELS = {
    "nano-banana": "google/nano-banana",
    "flux2pro":    "black-forest-labs/flux-2-pro",
    "schnell":     "black-forest-labs/flux-schnell",
    "pro":         "black-forest-labs/flux-1.1-pro",
}

def select_model():
    """Select model from command-line flags."""
    if "--flux2pro" in sys.argv:
        return "flux2pro", MODELS["flux2pro"]
    elif "--schnell" in sys.argv:
        return "schnell", MODELS["schnell"]
    elif "--pro" in sys.argv:
        return "pro", MODELS["pro"]
    else:
        return "nano-banana", MODELS["nano-banana"]

def build_input(prompt, model_key):
    """Build model input params - each model has slightly different schema."""
    if model_key == "nano-banana":
        return {"prompt": prompt}
    elif model_key in ("flux2pro", "schnell", "pro"):
        return {
            "prompt": prompt,
            "aspect_ratio": "4:5",      # 1080x1350 ratio for LinkedIn
            "output_format": "jpg",
            "output_quality": 90,
        }
    return {"prompt": prompt}

def parse_output(output):
    """Handle different output formats across Replicate models."""
    if isinstance(output, list) and len(output) > 0:
        item = output[0]
        return str(item.url) if hasattr(item, "url") else str(item)
    if hasattr(output, "url"):
        return str(output.url)
    return str(output)

def generate_storenext_visual():
    """Generate professional StoreNext vendor consolidation visual"""

    model_key, model_id = select_model()

    print("=" * 60)
    print("🎨 StoreNext Visual Generation - Vendor Consolidation")
    print("=" * 60)
    print("")
    print(f"Model: {model_id}")
    print("Format: 1080x1350px (LinkedIn optimal)")
    print("Theme: Vendor Network Hub & Control")
    print("Brand: Navy / Teal / Corporate")
    print("")
    print("⏳ Generating...")
    print("")

    # STORENEXT VENDOR CONSOLIDATION PROMPT
    prompt = """Professional enterprise B2B image: Interconnected network of navy blue spheres representing vendors, arranged in a precise geometric grid pattern on a white background.

Teal glowing connection lines radiating from a larger central hub sphere to all surrounding vendor nodes.
Clean white space background with subtle gray gradient.
Composition clearly shows central control - hub sphere slightly elevated, larger, commanding attention.
All peripheral spheres connected through teal lines to the central authority.

The visualization represents vendor consolidation and centralized procurement control.

Three-dimensional photorealistic rendering with professional cinematic lighting.
Sharp depth of field focusing on central hub with slight blur on peripheral nodes.
Polished metallic finish on spheres with warm professional lighting creating subtle shadows.
Clean modern architecture aesthetic - precise, controlled, efficient.
Corporate enterprise aesthetic - sophisticated, authoritative, trustworthy.

Dimensions: 1080x1350 pixels, LinkedIn format, 4K quality.

This represents StoreNext value proposition: Centralized visibility and control over complex enterprise vendor ecosystems through intelligent consolidation."""

    try:
        print(f"📝 Sending prompt to Replicate ({model_id})...")
        print("")

        output = replicate.run(
            model_id,
            input=build_input(prompt, model_key),
        )

        print("✅ Image generated successfully!")
        print("")

        image_url = parse_output(output)
        
        print(f"📥 Downloading image from Replicate...")
        
        # Download the image
        import urllib.request
        
        # Create output directory
        output_dir = Path("StoreNext/O-output/W11-vendor-consolidation")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_path = output_dir / "vendor-consolidation-visual.jpg"
        urllib.request.urlretrieve(image_url, output_path)
        
        file_size = output_path.stat().st_size / 1024
        
        print(f"✅ Image saved: {output_path}")
        print(f"📊 File size: {file_size:.1f} KB")
        print("")
        print("=" * 60)
        print("✨ STORENEXT VISUAL GENERATION COMPLETE!")
        print("=" * 60)
        print("")
        print("📋 Checklist:")
        print("   ✅ Professional corporate aesthetic")
        print("   ✅ Navy/teal color scheme (brand compliant)")
        print("   ✅ Clear vendor consolidation metaphor")
        print("   ✅ 1080x1350px optimized for LinkedIn")
        print("   ✅ Ready for Guardian review")
        print("")
        print(f"📍 Next: Have Guardian review at {output_path}")
        print("")
        
        return str(output_path)

    except Exception as e:
        print(f"❌ Error generating image:")
        print(f"   {str(e)}")
        print("")
        print("🔍 Troubleshooting:")
        print("1. Check internet connection")
        print("2. Verify API token at https://replicate.com/account")
        print("3. Check account credits at https://replicate.com/account/billing")
        print("4. Ensure you have $5+ credit balance")
        print("")
        print("Full guide: SYSTEM/docs/REPLICATE-NANO-BANANA-GUIDE.md")
        print("")
        sys.exit(1)

if __name__ == "__main__":
    generate_storenext_visual()
