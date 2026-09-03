"""Create clean SVG/PNG deliverables from the two supplied 7D logo rasters."""

from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
SOURCES = {
    "segmented": Path(r"C:\Users\rant\Downloads\7Da"),
    "solid": Path(r"C:\Users\rant\Downloads\7Db"),
}


def channel_paths(image: Image.Image, kind: str, levels: int = 12) -> list[tuple[str, str, float]]:
    """Convert raster color/coverage into compact horizontal vector runs."""
    pixels = image.load()
    width, height = image.size
    buckets: list[list[str]] = [[] for _ in range(levels)]

    for y in range(height):
        active_level = -1
        run_start = 0
        for x in range(width + 1):
            level = -1
            if x < width:
                red, green, blue = pixels[x, y][:3]
                if kind == "white":
                    coverage = min(red, green, blue)
                    if coverage >= 12 and not (red > green * 1.22 and red > blue * 1.16):
                        level = min(levels - 1, coverage * levels // 256)
                else:
                    coverage = max(0, red - max(green, blue) // 2)
                    if red >= 30 and red > green * 1.22 and red > blue * 1.16:
                        level = min(levels - 1, coverage * levels // 256)

            if level != active_level:
                if active_level >= 0:
                    buckets[active_level].append(f"M{run_start} {y}h{x-run_start}v1H{run_start}z")
                active_level = level
                run_start = x

    color = "#ffffff" if kind == "white" else "#ff3047"
    return [(color, "".join(parts), (i + 0.5) / levels) for i, parts in enumerate(buckets) if parts]


def write_svg(source: Path, target: Path) -> None:
    image = Image.open(source).convert("RGB")
    width, height = image.size
    layers = channel_paths(image, "white") + channel_paths(image, "red")
    body = "\n".join(
        f'  <path fill="{color}" fill-opacity="{opacity:.4f}" d="{path}"/>'
        for color, path, opacity in layers
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-label="7D, A Meteor company">\n'
        f'  <rect width="{width}" height="{height}" fill="#000000"/>\n{body}\n</svg>\n'
    )
    target.write_text(svg, encoding="utf-8")


def main() -> None:
    output = ROOT / "C-core"
    for name, source in SOURCES.items():
        image = Image.open(source).convert("RGB")
        png_target = output / f"7d-logo-{name}.png"
        svg_target = output / f"7d-logo-{name}.svg"
        image.save(png_target, format="PNG", optimize=True)
        write_svg(source, svg_target)


if __name__ == "__main__":
    main()
