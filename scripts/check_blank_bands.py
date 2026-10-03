#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["Pillow"]
# ///
"""Flag long vertical runs of empty page in a screenshot.

Usage:
    uv run scripts/check_blank_bands.py <png> [<png> ...] [--viewport 720] [--max-ratio 0.45] [--tolerance 6]

A row is "blank" when every sampled pixel is within --tolerance (0-255 per channel)
of the row's first pixel. A run of blank rows longer than --max-ratio * --viewport
is a finding. Exit 1 on any finding.

Run it on section-entry shots (hard fail) and on full-page shots (review; a sticky
or pinned section's runway shows as a band there and may be deliberate).
"""
import argparse
import sys
from pathlib import Path

from PIL import Image


def blank_rows(im, tolerance, samples=64):
    w, h = im.size
    px = im.load()
    xs = [int(w * (i + 0.5) / samples) for i in range(samples)]
    out = []
    for y in range(h):
        r0, g0, b0 = px[xs[0], y][:3]
        blank = True
        for x in xs[1:]:
            r, g, b = px[x, y][:3]
            if abs(r - r0) > tolerance or abs(g - g0) > tolerance or abs(b - b0) > tolerance:
                blank = False
                break
        out.append(blank)
    return out


def runs(flags):
    start = None
    for i, f in enumerate(flags + [False]):
        if f and start is None:
            start = i
        elif not f and start is not None:
            yield start, i
            start = None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("images", nargs="+", type=Path)
    ap.add_argument("--viewport", type=int, default=720, help="viewport height in CSS px the shot was taken at")
    ap.add_argument("--max-ratio", type=float, default=0.45, help="blank run longer than this fraction of the viewport is a finding")
    ap.add_argument("--max-px", type=int, default=260, help="blank run longer than this many CSS px is a finding (gate 26: 120 to 250px between sections)")
    ap.add_argument("--tolerance", type=int, default=6)
    ap.add_argument("--scale", type=float, default=None, help="device scale factor; inferred from width when omitted")
    a = ap.parse_args()

    findings = 0
    for path in a.images:
        im = Image.open(path).convert("RGB")
        w, h = im.size
        scale = a.scale or 1
        limit = int(min(a.max_ratio * a.viewport, a.max_px) * scale)
        flags = blank_rows(im, a.tolerance)
        # ponytail: a run touching the bottom edge is usually the next content arriving,
        # so it only counts past 70% of the viewport. Top and middle runs use the strict limit.
        bottom_limit = int(0.7 * a.viewport * scale)
        hits = [(s, e) for s, e in runs(flags)
                if (e - s > limit and e < h) or (e - s > bottom_limit)]
        if not hits:
            print(f"ok    {path}  (no blank run over {limit}px)")
            continue
        for s, e in hits:
            findings += 1
            pct = (e - s) / (a.viewport * scale) * 100
            print(f"BLANK {path}: rows {s}-{e} ({e - s}px, {pct:.0f}% of viewport)")
    if findings:
        print(f"{findings} blank band(s). Pull the next content up, or justify the runway in decisions.log.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
