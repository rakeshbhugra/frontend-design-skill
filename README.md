# frontend-design

One Claude Code skill for functional, on-brand frontend UI. It merges the working parts of five sources into a single pipeline and vendors their scripts unchanged.

```txt
scope → system → structure → imagery → build → motion → gate
```

Plus four verbs: `study` a reference, `audit` a screen, `comps` for options, `break` a component into every state.

## Install

```bash
# personal
ln -s "$(pwd)" ~/.claude/skills/frontend-design
# or per project
ln -s "$(pwd)" <project>/.claude/skills/frontend-design
```

Requirements:

- Python 3.12 and `uv` (scripts declare their own deps inline)
- Node 18, then in the skill root: `npm install && npx playwright install chromium`
- `GEMINI_API_KEY` in `.env` (copy `.env.example`), only for image generation

Then ask for a UI. The skill triggers itself.

## Layout

```txt
SKILL.md                 entry, ~150 lines, one reference per stage
references/
  00-scope.md … 06-gate.md   the seven stages
  style-lock-format.md   schema for per-project memory
  taste-memory.md        precedence and keep/reject rules
  verbs/                 study, audit, comps, break
  archetypes/            six page shapes with real numbers
  effects/               optional signature effects, INDEX.md picks
  stack/                 single-html, react-vite, nextjs
scripts/                 vendored, see below
assets/                  reveal.css, reveal.js, gsap-starter.js, tokens.template.css
templates/               style-lock.md, decisions.log, PROMPT.md
examples/ai-dev-agency/  a full run of the pipeline: page, images, lock, log, shots
```

Open the example with `python3 -m http.server 4173 -d examples/ai-dev-agency` and visit `http://localhost:4173`.

Per-project state goes to `<project>/.frontend-design/`. Cross-project taste goes to `~/.frontend-design/profile.md`.

## Sources and credit

| Source | Taken | License |
|---|---|---|
| [codeswithroh/tastemaker](https://github.com/codeswithroh/tastemaker) @ 20c438e | palette generator, contrast matrix, anti-slop scan, motion audit, icon and photo fetchers, style-lock and memory model, reveal assets | MIT |
| [MengTo/Skills](https://github.com/MengTo/Skills) @ 321c769 | page archetypes, effects, animation systems, no-design-slop gates, demo and PROMPT.md contract | see repo |
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills) @ 267330e | better-ui, better-layout, better-typography, better-colors, better-accessibility, better-writing, interface-review, break, variant | see repo |
| [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) @ 9a6930c | scope and brief, visual-critique rubric, interaction laws, state mapping, loading and error UX | see repo |
| `~/.claude-personal/skills/image-gen-skill` and `frontend-app` | Gemini image generation, image-to-image, background removal, house prompt recipe, React/Vite house style | local |

## Scripts

Every file in `scripts/` except `screenshot.mjs` is a byte-for-byte copy with a one-line source header. Do not patch them here. Fix upstream, then re-vendor:

```bash
T=../frontend-skills/tastemaker/skills/tastemaker/scripts
for s in generate_palette check_contrast extract_palette anti_slop_scan audit_motion fetch_icons fetch_photos _netguard check_copy_diversity recolor_svg; do
  { echo "# Vendored unchanged from codeswithroh/tastemaker @ $(git -C ../frontend-skills/tastemaker rev-parse --short HEAD) (skills/tastemaker/scripts/$s.py)"; cat $T/$s.py; } > scripts/$s.py
done
```

Known quirk: `check_copy_diversity.py` keeps its history at `~/.tastemaker/copy-history.json`. Left as is.

## Deliberately not included

Game development, Codex browser workflows, research and design-ops plugins, and the eighty single-effect skills. `references/effects/INDEX.md` points at the effect skills by path when a build needs one.
