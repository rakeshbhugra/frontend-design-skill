# Vendored unchanged from ~/.claude-personal/skills/image-gen-skill @ local (scripts/generate_image.py). Do not edit here; upstream fixes go to the source repo.
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "litellm>=1.82.1",
#     "python-dotenv>=1.0.1",
# ]
# ///
"""
Generate an image from a text prompt and save it as a PNG.

Backed by Google's Gemini image model (gemini-2.5-flash-image, "Nano Banana")
through LiteLLM. Requires GEMINI_API_KEY (from a .env in the skill directory,
or the surrounding environment).

Usage:
    uv run scripts/generate_image.py "<prompt>" [--output path.png] [--style photo]

Examples:
    uv run scripts/generate_image.py "a fox reading a book" --style illustration -o fox.png
    uv run scripts/generate_image.py "dark editorial blog cover, glowing async tasks" \
        --output ../../public/blog-images/cover.png
"""

from __future__ import annotations

import argparse
import base64
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

# Load .env from the skill directory (scripts/..) and from the current dir.
_SKILL_DIR = Path(__file__).resolve().parent.parent
load_dotenv(_SKILL_DIR / ".env")
load_dotenv()  # also pick up a .env in the cwd, if any

import litellm  # noqa: E402  (imported after env is loaded)


STYLE_PRESETS: dict[str, str] = {
    "none": "{prompt}",
    "photo": (
        "A professional photograph of {prompt}. "
        "Soft natural lighting, shallow depth of field, realistic detail, "
        "high resolution. No text, no watermark, no logo."
    ),
    "illustration": (
        "A clean modern illustration of {prompt}. "
        "Bold shapes, balanced composition, tasteful color palette, "
        "editorial style. No text, no watermark, no logo."
    ),
    "icon": (
        "A minimal flat icon representing {prompt}. "
        "Simple geometric shapes, centered, solid background, crisp edges. "
        "No text, no watermark."
    ),
    "diagram": (
        "A clean technical diagram illustrating {prompt}. "
        "Clear labels, simple boxes and arrows, generous whitespace, "
        "muted palette. Legible and uncluttered."
    ),
}


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (slug[:60] or "image")


def build_prompt(prompt: str, style: str) -> str:
    return STYLE_PRESETS[style].format(prompt=prompt)


def generate_image(
    prompt: str,
    output_path: str | None,
    style: str,
    model: str,
) -> str:
    if not os.getenv("GEMINI_API_KEY"):
        sys.exit(
            "ERROR: GEMINI_API_KEY is not set. Copy .env.example to .env in the "
            "skill directory and add your key, or export GEMINI_API_KEY."
        )

    full_prompt = build_prompt(prompt, style)
    print(f"Generating image  (style={style}, model={model})")
    print(f"Prompt: {full_prompt}")

    response = litellm.image_generation(prompt=full_prompt, model=model, n=1)

    datum = response.data[0]
    b64_data = getattr(datum, "b64_json", None) or (
        datum.get("b64_json") if isinstance(datum, dict) else None
    )
    if not b64_data:
        sys.exit(f"ERROR: model returned no image data. Raw response: {response}")

    if not output_path:
        output_path = str(_SKILL_DIR / "output" / f"{slugify(prompt)}.png")

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(base64.b64decode(b64_data))

    print(f"Saved: {out}")
    return str(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an image from a text prompt.")
    parser.add_argument("prompt", help="Text description of the image to generate.")
    parser.add_argument("--output", "-o", help="Output PNG path.")
    parser.add_argument(
        "--style",
        choices=sorted(STYLE_PRESETS),
        default="none",
        help="Style scaffold to wrap the prompt in (default: none).",
    )
    parser.add_argument(
        "--model",
        default="gemini/gemini-2.5-flash-image",
        help="LiteLLM model id (default: gemini/gemini-2.5-flash-image).",
    )
    args = parser.parse_args()
    generate_image(args.prompt, args.output, args.style, args.model)


if __name__ == "__main__":
    main()
