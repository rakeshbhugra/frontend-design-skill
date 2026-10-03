# Verb: comps

Directions before code. Hero options, key section layouts, or a brand-kit board, grounded in the same palette and structure a coded build would use.

Two outputs, user picks:

- Brief (default): structured prompts the user pastes into their own image tool.
- Rendered: the same briefs sent through `scripts/generate_image.py` (Gemini) when the user wants images now.

Either way, write `.frontend-design/comps-brief.md`.

Triggers: "just give me some comps", "show me directions before we build", "mock up a few hero options", "brand-kit board". A mockup of a screen that already has code is a normal Design pass, not this verb.

## 1. Reuse, do not reinvent

1. Palette: `uv run scripts/generate_palette.py --mood <mood> [--mode light|dark] [--seed N]`. Hand the hex values and roles (bg, surface, primary, accent, text) plus contrast results straight into the brief.
2. Structure: pick the macrostructure and archetype file per `02-structure.md`. "Hero: split, left-bias, real product mockup right" produces a specific image. "Nice hero" does not.
3. Logo or mark: a constructed geometric mark. Never a letter in a colored box. State it in the brief, image generators default to exactly that tell.

Skip Stage 3 (assets) and Stage 4 (build). There is no code yet.

## 2. Variants

- 2-3 comps by default. 4 only when the design space is wide.
- Each differs on a named axis: layout, density, hierarchy, interaction model, or motion. A color swap is not a variant.
- All comps share the one generated palette and, where relevant, the one macrostructure, so the set reads as one direction.

Write the direction set before any brief:

| Variant | Axis | Bet | Cost |
|---|---|---|---|
| Quiet | Lower density, minimal motion | Daily-use tool | Less memorable |
| Editorial | Larger type, stronger rhythm | Launch page | More vertical space |
| Operational | Dense controls, faster motion | Repeated work | Less emotionally polished |

Two rows that differ only by accent: merge them, make a real alternative.

## 3. The brief, one per comp

```
Comp: [Hero, split-demo direction]
Palette: bg #0C1414 (page) · surface #171F1F (panels) · primary #008286 (actions, links) ·
  accent #BE85CE (emphasis only) · text #E5F6F6 on bg (contrast X.XX:1, verified)
Composition: [macrostructure] · [archetype file] · [hero variant, e.g. "headline + subhead + CTA
  left, one real product screenshot right, left side dominant"]
Type register: [role, e.g. "geometric sans display, confident weight"; name faces if locked]
Mood: [premium | warm | technical | playful | elegant]
Constraints: no indigo-to-purple gradient · no letter-in-a-box mark · no invented metrics or logos ·
  [comp-specific anti-slop constraints]
```

## 4. Render path (optional)

Only when the user asked for images.

```bash
uv run scripts/generate_image.py "<brief text>" --style <preset> -o .frontend-design/comps/<comp-name>.png
```

- One call per comp. Same brief text that goes in the file, so image and record match.
- Requires `GEMINI_API_KEY` in the skill `.env` or the environment. Missing key: fall back to the brief and say so.
- Look at every result before treating it as locked. Rendered comps are directions, never assets to ship.
- Under Stage 3, a kept comp is treated like any reference image: grounding, not a source to pixel-clone.

## 5. Coded picker (optional, when the user must feel it)

For a hero, pricing card, onboarding step, empty state, command palette, or motion-heavy explainer where guessing is expensive, build 2-3 shippable variants behind a picker instead of images:

- Each variant uses locked tokens and real content. No dead controls, no lorem ipsum.
- Picker: floating pill bottom center, number keys switch, arrows cycle, `R` replays motion, `?v=2` in the URL, exactly one `aria-current="true"`.
- Picker chrome is neutral dark glass, not product tokens. Switching gets no animation.
- Verify before showing: flip every variant by mouse and keyboard, replay motion, check console, 390px and desktop, reduced motion keeps state changes.
- Promote only the chosen variant. Delete the picker unless asked to keep it. Log kept and rejected in `.frontend-design/decisions.log`.

## 6. State the picks out loud

Before handing anything back: "Palette: seed 7, technical dark, contrast verified. Structure: Feature Stack, product-proof-saas, split hero. 3 comps: hero, pricing section, brand-kit board, all from this palette."

## 7. Handoff file

`.frontend-design/comps-brief.md`:

```markdown
# Comps brief
Date: <date> · Palette: mood <m>, seed <n>, mode <light|dark> · Contrast: <pass|fail, matrix>
Roles: bg #… · surface #… · primary #… · accent #… · text #…
Macrostructure: <name> · Archetype: <file> · Hero variant: <knobs>
Rendered: <yes, paths | no, briefs only>

## Direction set
<table from step 2>

## Comp 1: <name>
<brief text exactly as used>
```

When the user returns with "now build this", Stage 1 and Stage 2 read this file first, write the picks into `style-lock.md`, and go straight to Stage 3.

## Limits to state every time

- The comp is only as good as the tool executing the brief. Palette and composition are verified, the render is not.
- Comps are not assets. Real screenshots, product UI, and photography come from Stage 3.
- `comps` generates new directions from this system. `study` extracts DNA from something that exists. Different direction of travel.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/verbs/comps.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/prototype-variants.md
