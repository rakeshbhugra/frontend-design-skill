# Style lock: <project name>

<!-- Copy to <project>/.frontend-design/style-lock.md. Schema: references/style-lock-format.md. -->
<!-- Fill only what you derived. Leave a field blank rather than inventing a value. -->

Established: <YYYY-MM-DD>. Source: <"reference images: paths" | "generated from mood" | "user-specified">
Stack: <single-html | react-vite | nextjs>
Mood: <premium | warm | technical | playful | elegant>. Seed: <N | unseeded>
Descriptors: <2-4 words>

## Palette
<!-- From scripts/generate_palette.py or extract_palette.py + check_contrast.py. Ratios are measured, never guessed. -->
- Background: #
- Surface: #
- Border: #
- Text: #, contrast vs bg
- Text muted: #, contrast vs bg
- Primary: #
- On-primary: #, contrast vs primary
- Secondary: #
- Accent: #, contrast vs bg
- Dark mode: <single mode only | author-time companion, no switch | runtime toggle>
  <!-- If companion or toggle: list companion roles here, each re-verified with --matrix. Same --seed for both modes. -->

## Color contract
<!-- Paste the "Legal pairings" summary from: scripts/check_contrast.py --matrix text= bg= surface= primary= accent= border= on-primary= -->
- Text-safe (>=4.5):
- UI-safe (3.0-4.5):
- Decorative (<3.0):
- Nudges: <"none" | "Role #old -> #new to clear <class> vs <role>">

## Typography
- Display: <family>, <why>
- Body: <family>
- Mono: <family | none>
- Scale: <ratio>, base <px>, sizes in use <list>
- Line-height: heading <n>, body <n>
- Letter-spacing: heading <em>, label <em>
- Non-Latin: <n/a | family + heading/body/UI weights, letter-spacing 0, word-break keep-all>

## Shape
- Radius scale: sm <px>, md <px>, lg <px>
- Border: <width> <token>, <decorative | state-carrying>
- Shadow: <none | values>

## Spacing
- Base: 4px. Tokens in use: <space-1 ... space-48 subset>
- Section tiers (marketing only): connective <px>, standard <px>, pivotal <px>
- Card padding: content <px>, compact <px>, showcase <px>
- Density: <generous | dense>
- Section separation: <whitespace only | surface tint | hairline>

## Structure
- Archetype chosen: <name>, differs from last build by <...>
- Narrative arc: <hook -> problem -> solution -> how -> proof -> close>
- Shared chrome: nav <pick>, footer <pick>
- Per-page archetypes: <page: hero / feature / proof / CTA>
- Build log: .frontend-design/log.json

## Effects
- Active effects: <list | none>
- Motion feel: <...>
- Curves: <--ease-out: cubic-bezier(...)>
- Durations: press <ms>, popover <ms>, panel <ms>, page <ms>
- Entrance: <ms>, <px> rise
- Reduced motion: <how it degrades>
- Verified: <scripts/audit_motion.py <paths>, <date> | pending>

## Imagery
- Prompt recipe: ground <light | dark | colour>, hue <accent hue>, register <photo | illustration | 3D | abstract>, exclusions <...>
- Approved reference images: <paths | none>
- Anchor asset: <path>
- Photo vs illustration split: <per section type>
- Icon set: <name>, stroke <px>, tinted #
- Logo: <path>, <preserved | constructed>

## Taste memory
- Profile priors used: <list | none>
- Last resolved decisions: <ids or dates>
- Pending review: <list | none>
- Promoted: <none | "<pref> to ~/.frontend-design/profile.md because <evidence>">

## Navigation chrome (app shells only, delete otherwise)
- Sidebar bg: <role>. Content bg: <role>
- Active item: <treatment>. Hover: <treatment>
- Row height: <px>. Body type: <px>

## Do not
- <concrete reject>, decision <id or date>
