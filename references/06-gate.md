# Stage 6: Gate

Purpose: prove the build on real screenshots. Scripts first, then two viewports, then the numbered eye checklist. Fix the top findings, re-shoot, hand back with a table.

Reach for `verbs/audit.md` instead when the UI is someone else's and no build happened this session. The checklist below is the same; only the fix loop is skipped.

## Sequence

1. Render. The page loads with zero console errors and a complete static first frame (nothing stuck at `opacity: 0`).
2. Mechanical scans. All four commands below. Fix every HIGH before taking a screenshot; a screenshot of a page with HIGH source tells is wasted.
3. Screenshots, three passes. Top of page: `node scripts/screenshot.mjs <url-or-file> .frontend-design/shots/` writes desktop 1280x720, wide 1536x1000, mobile 390x844. Full page: add `--full`. Section entries: add `--sections`, one viewport shot per section with its top edge at the viewport top, motion on. The entry frame is where sticky, pinned, and scrubbed sections fail: a block centered inside 100vh opens on an empty screen. Run `check_blank_bands.py` on the section shots (hard fail) and on the full-page shots (review). Open every shot. Read each as a stranger would for 5 seconds before reading the checklist.
4. Eye checklist. Walk the numbered list top to bottom against both images. Log each failure with its number and severity.
5. Fix loop. Fix the top 3 by severity, re-shoot, re-walk only the categories touched. Maximum 2 loops. Anything still open after loop 2 goes to `decisions.log` as `pending-review`, never silently dropped.
6. Log and hand back.

## Commands

```bash
uv run scripts/anti_slop_scan.py <changed-ui-paths> --fail-on high      # exit 1 on HIGH; --fail-on medium to tighten
uv run scripts/audit_motion.py <changed-ui-paths> --max-findings 50     # exit 1 on HIGH
uv run scripts/check_contrast.py --matrix text=<hex> bg=<hex> surface=<hex> primary=<hex> accent=<hex> border=<hex> on-primary=<hex>
uv run scripts/check_copy_diversity.py --headline "<hero headline>" --cta "<primary CTA>" --subhead "<subhead>"
node scripts/screenshot.mjs <url-or-file> .frontend-design/shots/
node scripts/screenshot.mjs <url-or-file> .frontend-design/shots/full --full
node scripts/screenshot.mjs <url-or-file> .frontend-design/shots/sections --sections
uv run scripts/check_blank_bands.py .frontend-design/shots/sections/desktop-*.png .frontend-design/shots/sections/wide-*.png --viewport 720
uv run scripts/check_blank_bands.py .frontend-design/shots/sections/mobile-*.png --viewport 844 --scale 2
```

`check_blank_bands.py` flags any vertical run of uniform pixels longer than 260 CSS px (gate 26) at the top or middle of a shot, or longer than 70 percent of the viewport at the bottom. Exit 1 on a finding. A sticky reading section's runway below its text is the one accepted reason to log a finding as `kept`.

`anti_slop_scan.py` rules: `ai-gradient`, `gradient-text`, `viewport-height`, `dead-link`, `missing-alt`, `transition-all`, `placeholder-content`, `em-dash` (all HIGH), `ai-copy`, `emoji-icon`, `eyebrow-spam` (MEDIUM). `check_contrast.py --matrix` is a report, exit 0; the single-pair and `--palette` forms exit 1 on a failed floor (4.5:1 text, 3.0:1 UI). `check_copy_diversity.py` flags the generic word bank (elevate, seamless, unlock, empower, streamline, all-in-one, next-gen) and the CTAs "get started", "learn more", "sign up", "click here", "submit", plus near-duplicates against `~/.tastemaker/copy-history.json` at Jaccard 0.6 over the last 10 entries.

## Eye checklist

Severity: H fails the gate, M needs a fix or a logged reason, L is a note. Mood notes loosen a gate only where stated.

### Slop clichés
1. H Structure is not the reflex template: hero, 3 feature cards, testimonial, CTA, footer, or the full hero, logo wall, metrics, bento, testimonials, FAQ, CTA sequence regardless of journey. No two sections share an archetype.
2. H No indigo-to-purple or blue-to-cyan gradient on hero, buttons, or backgrounds. No `background-clip: text` gradient headline, any mood.
3. H Logo is a real mark, not a letter in a rounded tile. Existing brand assets preserved unchanged.
4. H No emoji as icons. One icon set per page.
5. M No pill eyebrow with dot or hairline repeated above most headings; at most one per three sections. No hero pill restating the headline.
6. M No rounded-square icon tile above every feature heading; no run of identical icon, heading, description cards.
7. M No card apocalypse: every block boxed, cards nested in cards, hairline border plus diffuse shadow on the same edge, blob radii on small cards, accent stripe glued to one side.
8. M No fake chrome: hand-drawn browser, phone, or IDE frames; decorative dashboards or code windows showing nothing real.
9. M No decorative grid or stripes, sourceless radial lights, glow on every state, glass with no layering model, blur plus glow plus border plus noise stacked on one surface.
10. M No fake liveness: blinking cursor on static copy, pulsing dot on static data, random status pill.
11. M No italic emphasis word inside a heading, no all-italic display face. Emphasis by weight, accent, or drawn underline.
12. M One intentional rule-break exists (bleed, oversized number, asymmetry). Everything on-grid and evenly spaced reads as generated.
13. L Semi-brutalist hairline look was chosen for this product, not reached for by reflex.

### Hierarchy
14. H One entry point in 2 seconds. A single dominant element that matches the screen's primary goal, not scattered attention.
15. H Exactly one primary emphasis zone per view. Several primary actions at equal weight fails; a primary weaker than a decoration fails.
16. M Size differential at least 1.5x between hierarchy levels. Bold used sparingly enough to keep signal.
17. M Eye flow leads to the primary CTA with no dead ends or loops. No buried CTA.
18. H Hero passes the 5-second test (product, value, action) and the subtraction test. Budget: 1 optional eyebrow, 1 headline, 1 subhead, 1 primary CTA, at most 1 secondary, 1 visual. Rails, badges, orbits, and second mockups go below the fold.
19. H At 1280x720 the headline, lede, and primary CTA are visible without scrolling. Headline sized to word count, never one word per line. Mood note: elegant and premium may run a taller fold if the first screen is still a complete composition.
20. M No section headline outside the hero exceeds 50 to 65 percent of the hero display size. One stated statement moment is the only exception.
21. L Hero is not all-centered: at most 2 elements on the center axis, eyebrow or CTA off-axis.

### Composition
22. M Balance: no top-heavy, bottom-heavy, or tipped layout; a clear center of gravity at both viewports.
23. M Two-column sections are balanced: the shorter column is centered, filled with a real element, or capped. No column trailing into dead space.
24. M Every gap, margin, and padding sits on the spacing scale. Card padding floor 24px, and padding never exceeds the gap to the neighbour.
25. M One section-separation mechanism (tint, hairline, or padding) used at every boundary.
26. M Landing sections breathe: pivotal sections 128 to 192px per side, 120 to 250px between adjacent sections on desktop. Does not apply to app shells.
26b. H No empty entry frame. At every section's top edge, the first content starts within 260px. A sticky, pinned, or scrubbed block aligns its content to the top of its runway with section padding; centering inside 100vh fails. Checked by `check_blank_bands.py` on the section shots at 720 and 1000 tall.
27. M Proximity: related items closer than unrelated; a heading sits closer to what it introduces than to the previous section.
28. H No horizontal scroll 320 to 1920px. `overflow-x: clip` on html and body, image grid tracks `minmax(0, 1fr)`, display headers `overflow-wrap: anywhere; min-width: 0`.
29. H Nothing overlaps by accident at either viewport. Popovers not clipped by ancestor overflow. Sticky layers cover no control.
30. M Mobile is re-prioritised, not the desktop stack collapsed into one long column.

### Color
31. H Every pairing the build introduced is in the matrix's text-safe (4.5:1) or UI-safe (3.0:1) list: badge fills, disabled, hover, state borders. Decorative hairlines exempt.
32. H None of the three usual misses: button text within 5 percent OKLCH lightness of its fill; a dark panel (L under 50) whose text stayed dark; an accent fill with no verified on-accent color.
33. M Accent covers 5 percent or less of any viewport. Mood note: playful may run higher.
34. M Every color and `font-family` references a token. No inline hex, `oklch()`, or `rgb()`.
35. H State colors are semantic and color is never the only channel for state.
36. L Neutrals tinted toward the anchor hue. Mood note: technical and monochrome builds may use zero-chroma greys.
37. H Nothing contradicts the Do-not list in `style-lock.md`.

### Type
38. M At most 3 families. Body copy never monospace; mono for code, data, timestamps, short labels.
39. M Display line-height tightened but never under 1.0; descenders clear the next line at the real size and weight.
40. M Heading, subheading, and body sizes are clearly distinct. Functional text is readable; no tiny body because the layout came first.
41. H No button, nav link, tab, breadcrumb, or CTA wraps to 2 lines at 320 to 1920px. Hit targets at least 44x44px under 40rem.
42. L No collapsed display tracking, widened body tracking, long all-caps body, or justified text. No widows in focal copy.

### Affordance
43. H Hover, `:focus-visible`, `:active`, disabled, and loading states are specified, not browser defaults. Disabled uses opacity plus `cursor: not-allowed` plus the native attribute. Input border-width constant across states; input height equals adjacent button height.
44. H Focus ring at 3:1 or better, appears instantly, never transitioned in.
45. M Active nav, tab, filter, and selection states are unmistakable, not an uneven border.
46. M Destructive actions look different from routine ones.
47. M Hover is never the only route to essential information. Hover motion never moves the target away from the pointer or shifts neighbours.

### Density
48. M Density matches the surface: dashboards stay dense and scannable, landing pages breathe. No marketing spacing on an app shell, no cramped landing.
49. M Whitespace shapes hierarchy, not spectacle. No single sentence enlarged to consume the first viewport.
50. H App screens ship every core state: loading (skeleton mirroring the layout), empty (points to the next action), error (names the recovery), success (says what happened next), populated.

### Copy
51. H Shows, doesn't tell: each section is mostly something to look at with text as caption. Heading plus two sentences plus icon is the failure. Proof sections carry real visuals, not sparse label cards.
52. H Headline states one specific, checkable fact. `check_copy_diversity.py` passes. Buzzwords are not a value proposition.
53. H No em-dash anywhere in shipped copy: headlines, body, buttons, alt text, meta.
54. H No invented metrics, testimonials, customer logos, ratings, awards, or activity. Use a real number, an honest "metric to confirm" placeholder, or drop the slot.
55. H No lorem ipsum, "Sample text", or placeholder names when the brief gives real content.
56. M CTA verbs are specific. Not "Get started", "Learn more", "Submit".
57. L No caption that narrates what the visual already shows, no defensive captions, no labels restating the heading.

### Accessibility
58. H Every image has `alt` (empty for decorative) and explicit dimensions. No dead links, no non-functional controls.
59. H Controls have accessible names and roles and are keyboard reachable. Reading order matches visual order.
60. M Heading levels do not skip.
61. M Touch is handled: hover-only reveals have a touch path, pointer-only motion is gated.
62. M No layout shift after fonts, images, or client state load. Long names and other locales do not break the layout.

### Motion
63. M Not static. Marketing pages have reveal, stagger, and press feedback wired through `assets/gsap-starter.js` or `reveal.css`. App shells use the app track from `05-motion.md`.
64. H `audit_motion.py` is clean: no `transition: all`, `ease-in`, `scale(0)`, layout-property animation, ungated hover motion, or missing reduced-motion branch. UI over 300ms has a stated reason.
65. H Reduced motion leaves a complete end state with at most a 150ms opacity crossfade. Shortening the animation is not a fallback.
66. M No uniform `hover:scale`, no translate plus scale plus shadow plus color on one element, no bounce easing on UI state.
67. M Hero enters in at most 4 beats. Not every element gets the same entrance; internal labels do not animate independently.
68. M At most one signature effect from `effects/INDEX.md`. Perpetual animations pause offscreen. No marquee of content that must be read.
69. L Motion carries information: silent success over a celebratory toast, optimistic update plus Undo over a confirm dialog, hover tooltips at 800ms, focus tooltips at 0ms.

### Imagery
70. H Not asset-empty: real photos where the section calls for photos, illustrations for concepts, real fetched icons. Nothing deferred.
71. M One visual DNA: consistent lighting, crop, grade, stroke width, and color treatment across the batch.
72. M Imagery is subject-specific, not pleasant stock. Product screenshots match the current UI and copy.
73. M Generated imagery checked for anatomy, embedded text, logos, lighting, and context before use.
74. M Every chart has a one-line caption and its geometry was looked at: bars match labels, lines span the plotted range, segments sum sensibly.
75. M No visible attribution line on the page; credits live in a code comment. SVGs parse.

## Pass criteria

- All four scripts exit 0, or every MEDIUM finding has a logged reason.
- Zero H items open on both screenshots. Every M is fixed or logged with a reason from the brief.
- The final screenshots were taken after the last fix, not before.

## What goes to decisions.log

One JSONL line per item that changed the build, format per `taste-memory.md`:

- A fixed H or M: `status: "rejected"`, `axis` set to the checklist category, `decision` names the pattern removed, `why` starts with the gate number (`"gate 7: nested cards"`).
- A MEDIUM kept on purpose: `status: "kept"`, `why` cites the brief; `source: "user"` if the user said so, else `"agent-pending"` with `status: "pending-review"`.
- Anything open after loop 2: `status: "pending-review"`.
- Update `style-lock.md`: the Motion `Verified` line with the audit date, and the Do-not list with any newly rejected pattern.

## Hand back

The code, both screenshot paths, the gate table (number, severity, fixed or logged), and the scope block. Reasoning stays in `decisions.log`. Never claim a pass from source alone; the rendered surface decides.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/anti-slop-checklist.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/scripts/anti_slop_scan.py
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/scripts/check_copy_diversity.py
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/scripts/check_contrast.py
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/ui/no-ai-design-slop/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/ui/no-ai-design-slop/ARTICLE.md
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/interface-review/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/visual-critique/skills/critique-visual-hierarchy/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/visual-critique/skills/critique-composition/SKILL.md
