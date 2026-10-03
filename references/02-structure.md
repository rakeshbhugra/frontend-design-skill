# Stage 2: Structure

Pick the page shape before any code. Shape is a separate axis from color (Stage 1) and imagery (Stage 3). Two builds with different palettes and the same hero, 3 cards, testimonial, CTA rhythm are the same template. Stage 1 prevents color monoculture. This stage prevents structural monoculture.
Inputs: the brief, `.frontend-design/style-lock.md`, `.frontend-design/log.json`. Outputs: one macrostructure, one archetype file, one arc, at most one signature effect, one log.json entry.

## Order of operations

1. Write the narrative arc (below). Shape carries the arc, never the reverse.
2. Read `.frontend-design/log.json`. Apply the rotation rule.
3. Pick one macrostructure from the catalog, by name, out loud.
4. Pick the archetype file from the picker table. It sets section order and numbers.
5. Pick at most one signature effect from `effects/INDEX.md`.
6. Set grid defaults.
7. Write the log.json entry, the CSS stamp, and the Structure section of style-lock.md.

## Macrostructure catalog

| # | Name | Shape | Reach for it when |
|---|---|---|---|
| 1 | Feature Stack | Hero, then one full-width band per feature, alternating text/visual, each band led by a real mockup | 3-6 capabilities that each deserve a visual |
| 2 | Bento Showcase | Asymmetric grid of 1x1, 2x1, 2x2 tiles, each a live-looking UI fragment | Many small features better shown than sequenced |
| 3 | Editorial Index | Masthead, numbered or categorized list, generous type, hairline rules | Portfolios, agencies, publications, "who we are" |
| 4 | Long-Scroll Narrative | The six arc beats top to bottom, one full section each, scroll-linked reveal between | Non-obvious product, manifesto, launch |
| 5 | Stat-Led | One dominant real number or a tight metric row is the hero and spine | Story is genuinely quantitative and numbers are real |
| 6 | Gallery Grid | Grid of real photography or case tiles, minimal chrome | Commerce, food, travel, physical product |
| 7 | Product Demo / Workbench | Hero is the product in use, page organized around doing | Dev tools, apps where seeing it work is the argument |
| 8 | Split Diptych | Persistent statement column beside a scrolling column, or a hard left/right fold | Studios, single-voice products, art-directed feel |
| 9 | Conversational FAQ | Built from real audience questions, proof and CTA folded into answers | Trust gap, regulated, high-consideration |
| 10 | Manifesto | Type-forward, few images, big statements, short lines | Brand-led launch, opinionated product |
| 11 | Catalogue | Structured near-tabular listing set with editorial care | Many SKUs, pricing-as-page, changelogs, specs |
| 12 | Poster Fold | One full-bleed art-directed fold, quieter page below | Event, fashion, a single image is the message |

- App shells (sidebar + topbar) are not in this table. The frame is their macrostructure.
- Vague brief: offer three from different groups (grid-led Bento, document-led Long-Scroll, poster-led Manifesto). Never all twelve.
- Honesty rule: Stat-Led, Catalogue and every proof band use real numbers, or a labelled "metric to confirm" placeholder. No invented "+47%".

## Archetype picker

| Product type | Archetype file | Default macrostructure |
|---|---|---|
| SaaS or AI product where the UI is the proof | `product-proof-saas.md` | Product Demo / Workbench, Feature Stack |
| Enterprise AI, automation, security, ops | `operational-enterprise.md` | Feature Stack (dark chapters), Stat-Led |
| One offer, one audience, one CTA (ads, search) | `landing-page.md` | Feature Stack, Long-Scroll Narrative |
| Plans and tiers | `pricing-page.md` | Catalogue |
| Salon, spa, clinic, hospitality, any booking | `editorial-service.md` | Editorial Index, Gallery Grid |
| Brand launch, studio, portfolio, "make it cinematic" | `awwwards-cinematic.md` | Poster Fold, Manifesto, Long-Scroll Narrative |

The archetype file sets section order and numbers. The macrostructure sets the skeleton. Name both.

## Narrative arc, per page

| Beat | Job | Typical section |
|---|---|---|
| 1 Hook | The promise, sized per hero rules | Hero |
| 2 Problem | What is broken, specific to this product | Short prose plus a broken-state visual, or the hero subhead |
| 3 Solution | Show the fix, never assert it | Alternating bands, bento tiles, annotated capture |
| 4 How it works | 3-5 steps | Numbered step sequence |
| 5 Proof | Real logos, quote, numbers | Logo wall, pull quote, stat strip |
| 6 Close | The ask, echoing the hook | Statement plus action, inline form |

- Minimum 4 distinct beats. How it works may fold into Solution. Say so when it does.
- Self-check top to bottom: who is this for, what is wrong, how it fixes it, why believe it, what now. A section that serves none of these is a gap.

## Hero rules

Complete before markup: "This product helps [user] achieve [outcome] by [mechanism]." Outcome is the headline. Mechanism is the subhead.

| Element | Budget |
|---|---|
| Eyebrow | 0-1 |
| Headline | 1, 6-12 words. 3-8 words at full display size. 9-12 words one clamp tier down, 15-20% smaller |
| Headline lines | 2-3 at full size, 3-5 at 390px, never one word per line |
| Subhead | 1 sentence, 16-28 words, 2 lines max on desktop |
| CTA | 1 primary, 1 optional secondary for a lower-commitment path |
| Proof visual | Exactly 1, at most 1 outer frame |
| Metric chip | 0-2, sitting on the visual, real numbers only |
| Rule-break | 1 max: a bleed, an off-grid edge, or an accent bar |
| Intro motion | 4 beats max: nav, headline, subhead + CTAs, visual as one composition |

- Trust rows, feature chips, badges, orbits, second mockups go below the fold.
- One side dominates. Equal-weight columns read as template.
- Hero palette stays quieter than the sections below it.
- Comparison proof: animate a wipe between two real captures, range 15%-85%, frozen at 50% under reduced motion.
- Subtraction pass: every hero group answers one of what is this, why care, what next, what does good look like. Otherwise move it down.
- 390px: no horizontal overflow. Short desktop viewport: promise and CTA visible without scrolling.

## Grid defaults

| Breakpoint | Columns | Gutter | Margin |
|---|---|---|---|
| 375 | 4 | 16 | 16 |
| 768 | 8 | 24 | 24 |
| 1024 | 12 | 24 | 32 |
| 1440 | 12 | 32 | 48 |

- Baseline grid 4px or 8px. Contained max-width by default, full-bleed only for the fold or one band.
- Hierarchy: size steps of at least 1.5x between levels, one primary action per view, squint test passes.
- Break the grid once, on purpose. Not twice.

## One signature effect, max

- Pick at most one from `effects/INDEX.md`. Each archetype file lists the two it tolerates. Everything else is CSS hover, focus, and one reveal preset.
- The effect must sit in the Hook or Solution beat and serve it. Decorative means cut.
- Static first frame is complete without JS. `prefers-reduced-motion` renders the final state.
- Sticky, pinned, or scrubbed sections align content to the top of the runway (`align-content: start`, section padding 96 to 128px). Never center inside 100vh: the section enters on an empty screen and the gap to the previous section doubles on tall windows. Gate 26b measures it.
- Two signature effects on one page fail the Gate.

## Rotation rule

Read the last 3-5 entries of `.frontend-design/log.json`.

1. Macrostructure differs from the last build, ideally from the last three.
2. Nav, hero, and footer variants each differ from the last build.
3. Signature effect differs from the last build.
4. Forced to reuse? Change at least one knob and name the delta.

Palette is exempt, it is regenerated per project. Marketing pages only, app shells do not rotate.

Say it before code: "Last 3: Feature Stack, Editorial Index, Bento. Picking Long-Scroll Narrative, the brief needs explaining. Hero: was split, now statement. Effect: was masked-reveal, now none."
- First build: no rotation block, just the pick.
- User asks for the same shape again: honor it, change knobs, state them.
- Within one project, nav, footer, and type stay shared. Rotate the body, not the frame.

## What the stage writes

`.frontend-design/log.json`, JSON array, newest first, trimmed to 20. Infer one entry from the CSS stamp if the file is missing.
```json
{ "date": "2026-09-16", "page": "landing", "macrostructure": "Long-Scroll Narrative",
  "archetype": "product-proof-saas", "arc": "hook > problem > solution > how > proof > close",
  "nav": "compact", "hero": "split/left-bias/mockup", "footer": "statement",
  "effect": "masked-reveal", "knobs": "features=bands", "brief": "Tracejam, SaaS observability" }
```

First line of the built CSS:

```css
/* frontend-design · macrostructure: Long-Scroll Narrative · archetype: product-proof-saas
 * arc: hook > problem > solution > how > proof > close · hero: split/left-bias/mockup
 * effect: masked-reveal · palette: seed 4 (warm/light) · contrast: pass */
```

`style-lock.md` Structure section: macrostructure, archetype, shared nav/footer, signature effect.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/macrostructures.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/diversification.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/narrative-arc.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/hero-guidelines.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/ui-design/skills/layout-grid/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/ui-design/skills/visual-hierarchy/SKILL.md
