# Style lock: Kestrel (fictional AI-native software studio)

Stack: single-html
Mode: dark only (no toggle)
Mood: cinematic technical. Palette studied from the user's reference (a basement studio Awwwards thumbnail: slate, moss, a photoreal object over terrain) via extract_palette.py, then verified. Third direction on 2026-09-16; the first two (generated teal/rose dark, then cream + terracotta with Instrument Serif + Geist) were rejected by the user.

## Scope
- Screens: one marketing page.
- Primary action: book a scoping call (mailto).
- Visual thesis: one kestrel over dark highland terrain at dusk. A real subject, cinematic light, nothing abstract.
- Out of scope: case studies, team page, pricing table, blog.

## Palette
| Role | Hex |
|---|---|
| bg | #151a1e |
| surface | #1f272c |
| border | #2c363c |
| text | #e6ebea |
| text-muted | #9aa5a3 |
| primary | #b7cf8f (lichen) |
| on-primary | #151a1e |
| accent | #b7cf8f (same hue as primary, one accent) |
| focus | #e6ebea |

Legal pairings (check_contrast.py --matrix): text-safe for text/bg, text/surface, muted/bg, muted/surface, primary/bg, primary/surface, primary/on-primary, muted/border. Decorative only: bg/border, surface/border, bg/surface, text/primary. Accent words sit on bg or surface only, never on text.

## Type
- Display: Bricolage Grotesque 700/800 at opsz 96, letter-spacing -0.035em, line-height 0.92. h3 at opsz 24.
- Body: Hanken Grotesk 400/500/600, 16px, line-height 1.55.
- Mono: Azeret Mono 400/500, labels 12px uppercase at 0.12em, artifacts 13px.
- Scale: 14 / 16 / 20 / 25 / 31, statement clamp(34px, 4.8vw, 68px), display clamp(48px, 7.4vw, 124px).

## Space, shape, depth
- 4px base: 4 8 12 16 24 32 48 64 96 128 176. Sections 128px top, 96px bottom (224 between), 96/96 mobile.
- Radius 4 / 8 / 14, pills for buttons. Borders 1px #2c363c. No shadows; hairlines carry elevation on dark.

## Structure
- Macrostructure: Poster Fold. Archetype: awwwards-cinematic.
- Arc: hook (photo fold) > problem (word reveal) > solution + how (system, build week) > proof (contract terms) > close (second photo fold).
- Nav: sticky over the fold, wordmark + mono "STUDIO" + 4 anchors + secondary CTA. Footer: single row.
- Rule-break: the two full-bleed photo folds; everything else contained.

## Effects
- Signature: scroll-scrubbed-word-reveal, manifesto passage only. Hidden opacity 0.18, blur 6px, rise 0.14em, span 200vh, content aligned to the top of the runway with 128px padding (gate 26b).

## Motion
- Engine: GSAP 3.12.5 + ScrollTrigger + gsap-starter.js. Reveals 0.22s / 16px / power3.out / stagger 0.06.
- Hero: 4 beats, photo settles 1.06 to 1 over 1.4s, masked lines 0.85s stagger 0.1, nav 0.5s, lede + actions 0.6s.
- Hover family: 1px lift + tint on buttons, color on links. Press 0.97.
- Reduced motion: word reveal final state, photo static, sticky released.
- Verified: audit_motion.py clean, 2026-09-16.

## Imagery
- Subject: a common kestrel over highland terrain. Style: cinematic aerial photograph, dusk light, muted moss and slate, subtle film grain.
- Prompt recipe: ground "dark highland terrain of moss, lichen, and wet rock"; hue "muted dark greens and charcoal slate"; register "cinematic aerial photograph, dusk light, subtle film grain, sharp subject"; exclusions "no text, no watermark, no logo, no people".
- Approved: assets/kestrel-terrain-2.png (hero, edit_image from kestrel-terrain.png), assets/kestrel-moss.png (system), assets/kestrel-rock.png (close), both derived from the hero with edit_image.py.
- Logo: wordmark "Kestrel" in Bricolage Grotesque 800 with a mono "STUDIO" suffix. No glyph.
- Icons: inline Lucide check only.

## Do not
- Instrument Serif, Geist, Inter, Playfair. Terracotta on cream. Teal, cyan, rose, or violet accents on black.
- Abstract generated art (glowing lines, planes, particles). Drawn SVG logo marks. Emoji icons.
- Fake logos, testimonials, metrics. A second signature effect. Marquee. Parallax on copy.
- A sticky or scrubbed block centered inside 100vh.
