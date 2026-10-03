# `.frontend-design/style-lock.md` format

Purpose: the single source of truth for a project's visual system. Every stage after `01-system.md` reads tokens from here instead of re-deriving them.
Reach for `taste-memory.md` instead when the question is what to log or promote, not what the lock holds. Reach for `templates/style-lock.md` for a blank copy.

## Rules
- Fill only fields you actually derived. Blank beats invented.
- Every line should be something another project could plausibly do differently. "Clean typography" is not a lock entry.
- Update the lock when a choice becomes a project rule. Log the why in `.frontend-design/decisions.log`.
- Re-run `scripts/check_contrast.py --matrix` whenever the palette grows, then update the Color contract.

## Schema

```markdown
# Style lock: <project name>

Established: <date>. Source: <"reference images: paths" | "generated from mood" | "user-specified">
Stack: <single-html | react-vite | nextjs>
Mood: <premium | warm | technical | playful | elegant>. Seed: <N or "unseeded">
Descriptors: <2-4 words, e.g. "quiet, confident, technical">

## Palette
- Background: #hex
- Surface: #hex
- Border: #hex
- Text: #hex, contrast vs bg X.XX
- Text muted: #hex, contrast vs bg X.XX
- Primary: #hex
- On-primary: <#hex, "white" | "text">, contrast vs primary X.XX
- Secondary: #hex
- Accent: #hex, contrast vs bg X.XX
- Dark mode: <"single mode only" | "author-time companion, no switch" | "runtime toggle"> + companion roles if any, each re-verified

## Color contract
Floors: text on bg/surface 4.5, label on fill 4.5, accent as text 4.5, fill vs page 3.0, state border 3.0, decorative hairline exempt.
- Text-safe (>=4.5): <pairs from --matrix>
- UI-safe (3.0-4.5): <pairs>
- Decorative (<3.0): <pairs, never carry text or state>
- Nudges: <"Accent #aaa -> #bbb to clear UI-safe vs Surface" or "none">

## Typography
- Display: <family>, why
- Body: <family>
- Mono: <family or "none">, code/data/labels only
- Scale: <ratio, base px, sizes in use>
- Line-height: <heading / body>
- Letter-spacing: <heading / label>
- Non-Latin: <"n/a" | one family + heading/body/UI weights, letter-spacing 0, word-break keep-all>

## Shape
- Radius scale: <sm/md/lg px and where each applies>
- Border: <width, token, decorative vs state>
- Shadow: <"none" | values>

## Spacing
- Base: 4px. Tokens in use: <list>
- Section tiers (marketing only): connective <px>, standard <px>, pivotal <px>
- Card padding: content <px>, compact <px>, showcase <px>
- Density: <"generous" | "dense">
- Section separation: <"whitespace only" | "surface tint" | "hairline">

## Structure
- Archetype chosen: <name from `02-structure.md`>, differs from last build by <...>
- Narrative arc: <hook -> problem -> solution -> how -> proof -> close, with skips noted>
- Shared chrome: <nav + footer picks>
- Per-page archetypes: <page: hero/feature/proof/CTA picks>
- Build log: `.frontend-design/log.json`

## Effects
- Active effects: <list from `references/effects/`, or "none">
- Motion feel: <e.g. "quick, restrained">
- Curves: <e.g. --ease-out: cubic-bezier(0.23, 1, 0.32, 1)>
- Durations: <press / popover / panel / page>
- Entrance: <ms, px rise>
- Reduced motion: <how it degrades>
- Verified: <scripts/audit_motion.py paths + date, or "pending">

## Imagery
- Prompt recipe: ground <light|dark|colour>, hue <locked accent hue>, register <photo|illustration|3D|abstract>, exclusions <text, logos, faces, gradients...>
- Approved reference images: <paths under design/references/, or "none">
- Anchor asset: <path>
- Photo vs illustration split: <per section type>
- Icon set: <one set name>, stroke <px>, tinted <#hex>
- Logo: <path>, <"preserved" | "constructed">

## Taste memory
- Profile priors used: <1-3 from ~/.frontend-design/profile.md, or "none">
- Last resolved decisions: <ids or dates>
- Pending review: <list or "none">
- Promoted: <"none" | "<pref> to ~/.frontend-design/profile.md because <evidence>">

## Navigation chrome (app shells only)
- Sidebar bg: <role>. Content bg: <role>
- Active item: <treatment>. Hover: <treatment>
- Row height: <px>. Body type: <px>

## Do not
- <concrete rejects for this project, with the decision id>
```

## Field notes
| Field | Where it comes from |
|---|---|
| Palette, Color contract | `01-system.md` steps 2-4, pasted from `generate_palette.py` or `check_contrast.py --matrix` |
| Typography, Shape, Spacing | `01-system.md` steps 5-8 |
| Structure | `02-structure.md` plus `.frontend-design/log.json` rotation |
| Effects | `references/effects/` picks, verified by `scripts/audit_motion.py` |
| Imagery | `03-imagery.md`; recipe feeds `scripts/generate_image.py` |
| Stack | detected in Scope, gates which registries and effects apply |
| Taste memory, Do not | `taste-memory.md`, `.frontend-design/decisions.log` |

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/style-lock-format.md
