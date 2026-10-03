# Vendored unchanged from ~/.claude-personal/skills/image-gen-skill @ local (scripts/remove_background.py). Do not edit here; upstream fixes go to the source repo.
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pillow>=10.0.0",
# ]
# ///
"""
Remove the (near-white) background from an image and save a transparent PNG.

Designed for the images this skill generates: a centered 3D object / icon on a
solid ~white background with a baked soft-grey contact shadow. It flood-fills
the connected near-white background inward from the image borders, so the
centered subject (including light-colored parts of its body) stays intact.

The subject must NOT touch the image borders, because the flood-fill seeds from
the edges. Raise --thresh to also strip the baked contact shadow (risks nibbling
very light subject edges); lower it to preserve the subject at the cost of
leaving a faint shadow.

Usage:
    uv run scripts/remove_background.py <input.png> [-o out.png] [--thresh 30]

Example:
    uv run scripts/remove_background.py output/foo.png -o output/foo-cut.png --thresh 40
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

# Sentinel color painted into the flood-filled background. Chosen as an
# unlikely-in-photos magenta so we can reliably detect "this pixel was
# background" when building the alpha channel.
SENTINEL = (255, 0, 255)


def remove_background(
    input_path: str,
    output_path: str | None,
    thresh: int,
    feather: float,
    pad: int,
) -> str:
    # 1. Open and normalize to RGB.
    img = Image.open(input_path).convert("RGB")
    w, h = img.size

    # 2. Flood-fill the background from the borders with the sentinel color.
    #    Seed from the 4 corners, the 4 edge midpoints, and quarter points
    #    along the top/bottom edges so disconnected background regions all get
    #    filled. Each seed is wrapped in try/except in case a seed happens to
    #    land on the subject (or off the tolerance).
    draw = ImageDraw.Draw(img)
    seeds = [
        (0, 0),                       # top-left corner
        (w - 1, 0),                   # top-right corner
        (0, h - 1),                   # bottom-left corner
        (w - 1, h - 1),               # bottom-right corner
        (w // 2, 0),                  # top edge midpoint
        (w // 2, h - 1),              # bottom edge midpoint
        (0, h // 2),                  # left edge midpoint
        (w - 1, h // 2),              # right edge midpoint
        (w // 4, 0),                  # top edge quarter point
        (3 * w // 4, 0),              # top edge three-quarter point
        (w // 4, h - 1),              # bottom edge quarter point
        (3 * w // 4, h - 1),          # bottom edge three-quarter point
    ]
    for seed in seeds:
        try:
            ImageDraw.floodfill(img, seed, SENTINEL, thresh=thresh)
        except Exception:
            # A bad seed (e.g. on the subject) shouldn't abort the whole run.
            pass

    # 3. Build an RGBA image: sentinel pixels -> fully transparent, everything
    #    else -> original RGB with full opacity.
    rgba = Image.new("RGBA", (w, h))
    src_px = img.load()
    dst_px = rgba.load()
    for y in range(h):
        for x in range(w):
            r, g, b = src_px[x, y]
            if (r, g, b) == SENTINEL:
                dst_px[x, y] = (0, 0, 0, 0)
            else:
                dst_px[x, y] = (r, g, b, 255)

    # 4. Feather the alpha edge with a gaussian blur to soften the cutout.
    alpha = rgba.getchannel("A").filter(ImageFilter.GaussianBlur(feather))
    rgba.putalpha(alpha)

    # 5. Optionally crop to the content bbox, expanded by `pad` (clamped to the
    #    image bounds). A negative pad disables cropping entirely.
    if pad >= 0:
        bbox = rgba.getbbox()
        if bbox:
            left, top, right, bottom = bbox
            left = max(0, left - pad)
            top = max(0, top - pad)
            right = min(w, right + pad)
            bottom = min(h, bottom + pad)
            rgba = rgba.crop((left, top, right, bottom))

    # 6. Resolve the output path (default: alongside input as <name>-cut.png).
    if not output_path:
        p = Path(input_path)
        output_path = str(p.with_name(f"{p.stem}-cut.png"))
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    # 7. Save as RGBA PNG and report.
    rgba.save(out, "PNG")
    print(f"Saved: {out}")
    print(f"Size: {rgba.size[0]}x{rgba.size[1]} (mode {rgba.mode})")
    return str(out)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove a near-white background and save a transparent PNG."
    )
    parser.add_argument("input", help="Input PNG path.")
    parser.add_argument(
        "--output", "-o",
        help="Output PNG path (default: <input>-cut.png alongside the input).",
    )
    parser.add_argument(
        "--thresh", type=int, default=30,
        help="Flood-fill color tolerance from the border color (default: 30).",
    )
    parser.add_argument(
        "--feather", type=float, default=0.6,
        help="Gaussian blur radius applied to the alpha edge (default: 0.6).",
    )
    parser.add_argument(
        "--pad", type=int, default=10,
        help="Transparent padding kept around the content bbox; 0 crops tight, "
             "negative disables cropping (default: 10).",
    )
    args = parser.parse_args()
    remove_background(
        args.input, args.output, args.thresh, args.feather, args.pad
    )


if __name__ == "__main__":
    main()
