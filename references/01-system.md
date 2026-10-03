# 01 System: lock palette, type, and tokens before any layout

Purpose: produce one verified palette, one type pairing, one spacing/radius/shadow set, and write them to `.frontend-design/style-lock.md` so every later screen reuses them instead of re-deriving.
Reach for `verbs/study.md` instead when the user wants the DNA of a reference extracted, not a fresh system. Reach for `02-structure.md` once this stage is locked.

Runs only on a cold start (no `.frontend-design/style-lock.md`; read `~/.frontend-design/profile.md` first per `taste-memory.md`) or when the user asks to change direction. Otherwise read the lock and reuse it verbatim.

## 1. Classify the mood (no references given)

| Mood | Idea signals | Default mode | Base hue range (OKLCH) | Heading + body | Alt pairing |
|---|---|---|---|---|---|
| premium | fintech, B2B SaaS, analytics, enterprise, legal, insurance, admin/ops | light | 245-285 | Unbounded + Albert Sans | Inter + Inter, tight heading tracking |
| warm | wellness, health, coaching, community, nonprofit, education, food, hobby | light | 20-60 | Zain + Nunito | Epilogue + Baskervville |
| technical | dev tool, API, CLI, infra, devops, database, monitoring, open source | dark | 150-200 or 210-255 | Archivo + IBM Plex Sans, IBM Plex Mono for code/data only | IBM Plex Sans + IBM Plex Mono for data |
| playful | game, creator tools, teen audience, dating, music, social, "fun" | light | 0-360 | Urbanist + Open Sans | Fredoka + Nunito |
| elegant | publishing, portfolio, luxury, fashion, gallery, boutique, agency | light | 20-55 or 70-90 | Gloock + Inter | EB Garamond + DM Mono (accents) |

Reflex ban. These are the pairings a model reaches for on its own and they read as generated: Inter, Geist, Instrument Serif, Playfair Display, Space Grotesk, DM Sans, Manrope as a display face; terracotta or rust on cream paper; indigo or violet gradients; teal, cyan, or rose on near-black. Never ship them unless the user's own reference contains them. Pick from the mood table, or from a study of the user's reference, and say which.

Rules: if the request names the mood, use it. Ask only when the idea spans two moods with no lean. State in one line which mood was inferred and why. Non-Latin script (Korean, Japanese, Chinese): one family across a weight scale, not two families. Korean: Pretendard (9 weights, SIL OFL, own CDN, not Google Fonts). Heading SemiBold/Bold, body Regular, UI chrome Medium. `letter-spacing: 0`, `word-break: keep-all` on headings and UI text, line-height above 1.15 even on display.

## 2. Generate the palette (default path)

```bash
uv run scripts/generate_palette.py --mood <premium|warm|technical|playful|elegant> [--mode light|dark] [--seed N]
```
Prints 8 roles (text, bg, surface, primary, on-primary, secondary, accent, border), a realtimecolors preview URL, and the full contrast matrix. Omit `--seed` for a fresh palette; pass it only to reproduce a run. Never paste the five reference-anchor hexes from the source skill as a shipped palette.

## 3. Reference-image path (user supplied screenshots or images)

```bash
uv run --with pillow scripts/extract_palette.py <image_path> [image_path ...]
uv run scripts/check_contrast.py --palette text=<hex> bg=<hex> primary=<hex> accent=<hex>
uv run scripts/check_contrast.py --matrix text=<hex> bg=<hex> surface=<hex> primary=<hex> accent=<hex> border=<hex> on-primary=<hex>
```
`extract_palette.py` needs Pillow and prints JSON: 6 dominant colors (hex, share, hue, saturation, value), likely background, likely text, their contrast ratio, and mood notes. Assign roles yourself, then run `--palette` (exits 1 on a failing floor) and `--matrix`. Single pair: `uv run scripts/check_contrast.py <hex1> <hex2>`. Anchor every token to something visible in the image; if you cannot point to it, drop it.

## 4. Contrast contract (what the matrix means)

| Pairing | Floor | Matrix class |
|---|---|---|
| body or muted text on bg or surface | 4.5:1 | text-safe |
| button label on its fill (`on-primary`/`primary`) | 4.5:1 | text-safe |
| accent used as link text | 4.5:1 | text-safe |
| a fill vs the page (does the button show up) | 3:1 | UI-safe |
| accent as icon or highlight | 3:1 | UI-safe |
| border that carries state (focus, error, active) | 3:1 | UI-safe |
| decorative hairline | none | decorative, must never be the only state carrier |

Text goes only on text-safe pairs. Borders and icons that mean something go only on text-safe or UI-safe pairs. Decorative pairs carry neither text nor state.
`--palette` checks both white and the text color on primary; use whichever passes as `on-primary`. Do not assume white.
When a new pairing fails, in this order: 1) reuse a pair already legal for that purpose, 2) nudge lightness within the same hue, re-run `--matrix`, 3) fall back to `text` or `on-primary`, 4) surface the conflict to the user. Never change hue to fix contrast. Re-run `--matrix` every time the palette grows.

## 5. Type rules
- Max 3 families. Pair for contrast (serif display over sans body), never two near-identical sans. Mono for code, data, labels, never paragraphs.
- Weight 400 or heavier below 18px. Weights under 300 only at 28px and above.
- Line-height: headings 1.1-1.2, body 1.5-1.6, long-form 1.75, anything wrapping to 3+ lines at least 1.4. Unitless only.
- Letter-spacing: large headings -0.02em, body 0, uppercase labels 0.05em (mono eyebrow style: 0.18em).
- Measure 60-75ch. Body 16px minimum. UI text 14px, captions 13px, never below 12px. Inputs 16px on mobile.
- `text-wrap: balance` on headings, `text-wrap: pretty` on descriptions, `tabular-nums` on any changing number.

## 6. Type scale (ratio 1.25, base 16px)

| Token | px | Weight | Line-height |
|---|---|---|---|
| caption | 12 | 400-500 | 1.5 |
| body-sm | 14 | 400 | 1.5 |
| body | 16 | 400 | 1.5-1.6 |
| subheading | 20 | 500-600 | 1.3 |
| h3 | 24 | 600 | 1.2 |
| h2 | 32 | 600 | 1.2 |
| h1 | 40 | 600-700 | 1.1 |
| display | 48-64 | 600-700 | 1.0-1.15 |

Keep 4-5 sizes in regular use. Headings descend with level; step display sizes down one tier on mobile, keep body at 16px.

## 7. Spacing scale (4px base)

| Token | px | Use |
|---|---|---|
| space-1 | 4 | icon to label, badge padding |
| space-2 | 8 | label to value, stacked related lines |
| space-3 | 12 | dense table cell, app-shell nav row (floor) |
| space-4 | 16 | button padding, compact stat tile |
| space-6 | 24 | content card padding floor (pricing, feature, testimonial) |
| space-8 | 32 | showcase/hero card padding, gap between groups |
| space-12 | 48 | small section, connective bands |
| space-16 | 64 | default section padding |
| space-24 | 96 | standard landing section |
| space-32 | 128 | pivotal section (hero, primary proof) |
| space-40 | 160 | strongest beat |
| space-48 | 192 | ceiling, one section per page |

Governing rule: internal padding <= external gap. Section tiers on landing pages: connective 48-64px, standard 64-96px, pivotal 128-192px. Adjacent-section boundary gap lands 120-250px on desktop. Drop 1-2 tiers at <=40rem. App shells stay on space-3 to space-6 and never import section tiers. Density modes: compact = one step down, spacious = one step up.

## 8. Radius, border, shadow by mood

| Mood | Radius | Border | Shadow |
|---|---|---|---|
| premium | 4-8px | 1px hairline | none or minimal |
| warm | 12-20px | soft | soft, 2-4px blur allowed |
| technical | 0-4px | visible 1px grid lines | none |
| playful | 16-24px | optional | layered depth allowed |
| elegant | 0-4px | thin hairline rules between sections, no cards | none |

Pick one radius scale (e.g. 4/8/16px sm/md/lg) and never mix arbitrary values. On a black ground borders replace shadows; a shadow on #000 is invisible.

## 9. Semantic token naming
- Primitives by hue and step (`--blue-500`), never used in a component. Semantics by role (`--color-text-secondary`, `--color-bg-surface`, `--color-accent-solid`), the only tier components touch.
- `accent` = brand; `primary` = most prominent of its group. Never name by appearance or first use. Never borrow a token for its value; a missing role means add a token.
- One neutral ramp, one accent ramp, status ramps only for states actually rendered. Every ramp step needs a consuming role.
- One color, one meaning: hues within 15 degrees are the same color. The interactive hue never sits on static text.
- Fill one primary action per view; peers stay neutral. Colour on the background, not the label.

## 10. Dark mode
- Not a mechanical invert. Start reversed, then lower chroma, widen the dark end, re-run `--matrix` on every pair.
- Companion pair: same `--seed`, `--mode light` then `--mode dark`. Different seeds give two palettes that merely share a mood.
- Primary must clear 3:1 against the dark bg (visibility), not just 4.5:1 with its label. Source example: `#2F27CE` hits 2.16:1 on `#0A0A12`, `#5850E0` clears 3.42:1 in the same family.
- One switching mechanism: `data-theme="light|dark"` on `<html>`, default from `prefers-color-scheme`, `localStorage` override read before first paint. Decide single mode, author-time companion, or runtime toggle, and record it in the lock.

## 11. Token sheet (paste, then replace hexes with generated values)

```css
:root {
  --color-bg: #FBFBFE; --color-surface: #F3F3F8; --color-border: #E1E1EA;
  --color-text: #050315; --color-text-muted: #5C5A72;
  --color-primary: #2F27CE; --color-on-primary: #FFFFFF; --color-secondary: #DEDCFF; --color-accent: #433BFF;
  --font-display: "Unbounded", sans-serif; --font-body: "Albert Sans", sans-serif;
  --text-sm: 14px; --text-base: 16px; --text-lg: 20px; --text-xl: 24px; --text-2xl: 32px; --text-3xl: 40px;
  --leading-tight: 1.1; --leading-body: 1.5;
  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px; --space-6: 24px; --space-8: 32px;
  --space-12: 48px; --space-16: 64px; --space-24: 96px; --space-32: 128px;
  --radius-sm: 4px; --radius-md: 8px; --radius-lg: 16px; --border: 1px solid var(--color-border); --shadow-soft: 0 2px 4px rgb(0 0 0 / 0.06);
}
:root[data-theme="dark"] { /* companion values from the same --seed, re-verified with --matrix */ }
```

## 12. Write it down
Write palette, matrix summary (text-safe / UI-safe / decorative lists), type pairing, scale, spacing tiers, radius, border, shadow, and dark-mode decision to `.frontend-design/style-lock.md` per `style-lock-format.md`. Say in one line: mood inferred, seed used, and whether any token was nudged to clear a floor.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/style-tokens.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/scripts/generate_palette.py
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/scripts/check_contrast.py
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/scripts/extract_palette.py
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/better-colors/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/better-typography/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/ui-design/skills/color-system/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/ui-design/skills/typography-scale/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/ui-design/skills/spacing-system/SKILL.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/references/tokens.md
