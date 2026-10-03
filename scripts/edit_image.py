# Vendored unchanged from ~/.claude-personal/skills/image-gen-skill @ local (scripts/edit_image.py). Do not edit here; upstream fixes go to the source repo.
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "google-genai>=1.0.0",
#     "pillow>=10.0.0",
#     "python-dotenv>=1.0.1",
# ]
# ///
"""
Image-to-image generation: riff on one or more reference images with a prompt,
using Google's Gemini image model (gemini-2.5-flash-image, "Nano Banana") via
the google-genai SDK. Use this (instead of generate_image.py) when you need the
output to stay consistent with an existing image — e.g. the same character in a
new pose, a restyle, or an edit.

Requires GEMINI_API_KEY (from a .env in the skill directory or the environment).

Usage:
    uv run scripts/edit_image.py "<prompt>" -i ref1.png [-i ref2.png] -o out.png
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from PIL import Image

_SKILL_DIR = Path(__file__).resolve().parent.parent
load_dotenv(_SKILL_DIR / ".env")
load_dotenv()

from google import genai  # noqa: E402  (after env load)


def edit_image(prompt: str, images: list[str], output_path: str, model: str) -> str:
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        sys.exit("ERROR: GEMINI_API_KEY is not set (skill .env or environment).")

    client = genai.Client(api_key=key)
    contents: list = [prompt]
    for p in images:
        if not Path(p).exists():
            sys.exit(f"ERROR: reference image not found: {p}")
        contents.append(Image.open(p))

    print(f"Editing with {len(images)} reference image(s), model={model}")
    resp = client.models.generate_content(model=model, contents=contents)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    for cand in resp.candidates or []:
        for part in cand.content.parts or []:
            data = getattr(getattr(part, "inline_data", None), "data", None)
            if data:
                out.write_bytes(data)
                print(f"Saved: {out}")
                return str(out)

    sys.exit(f"ERROR: model returned no image. Raw response: {resp}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Edit/riff reference images with a prompt.")
    ap.add_argument("prompt", help="What to make from the reference image(s).")
    ap.add_argument("--image", "-i", action="append", required=True,
                    help="Reference image path (repeatable).")
    ap.add_argument("--output", "-o", required=True, help="Output PNG path.")
    ap.add_argument("--model", default="gemini-2.5-flash-image",
                    help="Gemini image model id (default: gemini-2.5-flash-image).")
    args = ap.parse_args()
    edit_image(args.prompt, args.image, args.output, args.model)


if __name__ == "__main__":
    main()
