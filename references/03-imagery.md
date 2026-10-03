# Stage 3: Imagery

Purpose: source every icon, photo, logo, and piece of art so it sits on the locked palette instead of pasted on top of it.

Reach for `01-system.md` instead when the palette is not locked yet. Nothing here runs without `style-lock.md` holding an accent hue and a ground color.

## 1. Decision table

| Need | Source | Never |
|---|---|---|
| UI icon | React + shadcn: `lucide-react` or the lucide-animated registry. Any other stack: `fetch_icons.py --mood <lock mood>`. One set per project | Generate a PNG icon. Mix two icon sets |
| Photo (avatar, headshot, hero background) | `fetch_photos.py` (Openverse, CC0, keyless). Manual pick: Unsplash or aura.build/assets page URL, user downloads and crops | Unsplash API (requires visible credit). Hotlinked search results |
| Brand or social logo | `fetch_icons.py --set simple-icons` (mono) or `--set logos` (color). Check slug and license | A text chip in place of a mark. A redrawn likeness |
| Project's own logo | Existing asset in repo, byte for byte. None: construct 2 to 5 primitives in the palette | Letter in a rounded box |
| Hero, card, empty state, OG, mascot | `generate_image.py` with the recipe below | Stock that could belong to any product |
| Concept illustration (optional path) | A local unDraw SVG recolored with `recolor_svg.py`. Only if the user already has the files; unDraw bars scripted download | Hand-drawn SVG paths |

## 2. Reference-driven generation

When the user drops a reference image:

1. `uv run --with pillow scripts/extract_palette.py ref.png` prints JSON: dominant hexes, lightness and saturation stats, `likely_background`, `mood_notes`.
2. Merge with the lock: ground comes from the lock, hue from the lock's accent, register words from the reference's stats (low saturation reads "matte, muted", high lightness reads "airy, paper").
3. Write the style clause from that. Save the reference path under `## Imagery` in `style-lock.md`.

Originality boundary:
- Take lighting, texture, saturation, and register from the reference.
- Never copy its subject, layout, or a named brand's character.
- If the user asks for "the same thing", say what you are taking and what you are not, once.

## 3. The prompt recipe

Every generated prompt has four clauses, in this order. Only the subject and the hue word change across a set.

Subject rule, first: name a concrete subject. An animal, an object, a scene, a material, a place. "Abstract glowing lines", "layered planes", "particles", "gradient blobs" are the generated-art reflex and read as AI slop even when on-palette. Award-winning pages carry photographed or rendered things. Prefer editorial studio photography of the subject on a plain paper ground, then `remove_background.py` so it floats on the page. Reject any abstract-only prompt at the review step.

| Clause | Job | Example |
|---|---|---|
| Ground | Names the page background | "on a near-black ground" |
| Hue | The one accent from the lock, by name | "thin glowing violet lines" |
| Register | 3 to 5 style words from the lock | "minimal, geometric, editorial, soft volumetric light" |
| Exclusions | Always the same | "no text, no watermark, no logo, no UI chrome" |

Dark ground:

```
Abstract minimal illustration of layered request routing, thin glowing violet
lines over a near-black ground, soft volumetric light, geometric, editorial,
generous negative space, no text, no watermark, no logo, no UI chrome
```

Light paper ground:

```
Abstract minimal illustration of a calendar filling with tasks, matte terracotta
shapes on a warm off-white paper ground, flat risograph grain, soft daylight,
generous negative space, no text, no watermark, no logo, no UI chrome
```

Set rule: for a multi-hue product, change the color word only. Every other token stays byte identical. That is what makes five images read as one set.

## 4. Set consistency and mascots

1. Generate the first image with `generate_image.py`. Show it. Get a yes.
2. Every other image in the set: `edit_image.py -i first.png` with "SAME style, lighting, and palette, now depicting <subject>". Do not re-roll the text prompt.
3. Mascot: same loop. Describe what to keep ("the SAME character: identical body, colors, face") and what changes ("front-facing, waving"). Save the winning prompt to the lock.
4. Floating cutout: ask for "centered on a solid white background, generous margin" in the prompt, then `remove_background.py`. The flood fill seeds from the borders, so a subject touching an edge fails. Regenerate with more margin, do not fight `--thresh`.
5. `--thresh`: 30 default. 40 to 50 strips the baked contact shadow (risks light edges). 20 keeps light edges and leaves a faint shadow.

## 5. Commands

Run from the skill root. Generation scripts need `GEMINI_API_KEY` in `.env` at the skill root or the environment.

```bash
# Generate. --style photo|illustration|icon|diagram|none (default none, use none with a full recipe prompt)
uv run scripts/generate_image.py "<recipe prompt>" -o <project>/public/images/hero.png --style none

# Consistent follow-ups. -i is repeatable, -o is required
uv run scripts/edit_image.py "SAME style and lighting, now depicting <subject>" -i hero.png -o card-2.png

# Transparent cutout. Defaults: --thresh 30 --feather 0.6 --pad 10 (0 crops tight, negative disables crop)
uv run scripts/remove_background.py mascot.png -o mascot-cut.png --thresh 40

# Reference pixels to JSON (Pillow, not inline-declared, so pass it)
uv run --with pillow scripts/extract_palette.py ref.png

# Icons. Discover names, then fetch tinted. --mood premium|warm|technical|playful|elegant, --seed for a repeatable set pick
uv run scripts/fetch_icons.py --search "chart growth shield" --mood technical
uv run scripts/fetch_icons.py --icons rocket shield mail --mood technical --color "#7C3AED" --width 48 --out <project>/public/icons

# Brand marks. Confirm the slug first: curl -s -o /dev/null -w "%{http_code}" https://api.iconify.design/simple-icons:<slug>.svg
uv run scripts/fetch_icons.py --icons vercel github openai --set simple-icons --color "#8A8A8A" --out <project>/public/logos

# Photos. --count 3, --source openverse|pixabay (pixabay needs PIXABAY_API_KEY), --credits-format html|plain|css
uv run scripts/fetch_photos.py "modern office workspace" --count 3 --out <project>/public/photos

# Recolor local SVGs to the accent. --preserve-dark keeps near-black strokes, --dry-run reports only
uv run scripts/recolor_svg.py <project>/public/illustrations --accent "#7C3AED" --preserve-dark

# Contrast of overlaid text against the image's sampled ground
uv run scripts/check_contrast.py "#F5F5F7" "#0B0B0F"
```

`fetch_photos.py` writes `CREDITS.html.txt` next to the photos. Paste it into a code comment, never onto the page. Brand slugs surprise: ChatGPT is `openai`, Gemini is `googlegemini`. A slug that 404s in both `simple-icons` and `logos` is dropped from the row, not replaced with text.

## 6. Image QA gate

Run per image before Build. Any failure means regenerate with a fixed prompt. Never retouch the PNG.

| Check | Pass condition |
|---|---|
| On hue | Sample 3 pixels of the art's accent. Same hue family as the lock's accent, within 15 degrees |
| Clean | No text, watermark, logo, or UI chrome anywhere in the frame |
| Aspect | Composition requested in the prompt, then cropped to target. Model output is roughly square, do not trust it |
| Dimensions | `width` and `height` set on every `<img>`, or an `aspect-[w/h]` box. No layout shift |
| Alt | `alt=""` for decorative art. Real alt only when the image carries information |
| Border | On a dark ground every image gets `border border-border` and the surface radius |
| Overlaid text | `check_contrast.py <text> <sampled ground>` passes 4.5:1. Add a vignette from the ground color if it fails |
| Set | Placed side by side, all images share one ground, one hue, one register |
| Loading | `loading="lazy"` below the fold, omitted on the hero. Path `public/images/<feature>/<name>.png`, referenced absolute, never imported |

## 7. Cost rule

Every generation call is paid. Never loop over a list, never batch before the hero is approved. The sequence:

1. Propose the image list: name, role, target size, ground. 4 to 6 roles max (hero anchor, proof, texture object, micro assets).
2. Generate the hero. Show it. Wait.
3. On approval, generate the rest via `edit_image.py -i hero.png`.
4. One retry per image on QA failure. A second failure goes back to the user with the prompt shown.

## 8. Write back to style-lock.md

Append under `## Imagery`, so later sessions reuse instead of drifting:

```
## Imagery
recipe:
  ground: <e.g. near-black #0A0A0A>
  hue: <e.g. violet #7C3AED>
  register: <e.g. minimal, geometric, editorial, soft volumetric light>
  exclusions: no text, no watermark, no logo, no UI chrome
references: <approved reference paths, or none>
seed image: <path to the approved hero, used as -i for the set>
icon set: <lucide-react | lucide-animated | iconify:<set>>
photo source: <openverse | unsplash manual | none>
mascot prompt: <the winning prompt, or none>
```

`06-gate.md` reads this block to verify the shipped images match. See `style-lock-format.md` for the full file layout.

Distilled from:
- /Users/rakeshbhugra/.claude-personal/skills/image-gen-skill/SKILL.md and scripts/generate_image.py, edit_image.py, remove_background.py
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/references/imagery.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/asset-curation.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/illustration-sources.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/logo-sourcing.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/component-sourcing.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/scripts/fetch_icons.py, fetch_photos.py, recolor_svg.py, extract_palette.py, check_contrast.py
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/ideagram/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/media/unsplash-asset-images/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/media/aura-asset-images/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/company-logos/SKILL.md
