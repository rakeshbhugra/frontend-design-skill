# Awwwards Cinematic

Motion-led marketing, editorial, or portfolio site where hero, imagery, type, and motion tell one story. "Awwwards quality" is an acceptance bar, never a claim.

Reach for `landing-page.md` instead when the goal is conversion from paid traffic. Reach for `product-proof-saas.md` when the product UI is the proof.

Write the direction before code: visual thesis, hero focal asset, type hierarchy, color system, section sequence, motion narrative, smooth-scroll engine, Three.js decision, asset provenance.

## Section order

1. Hero: the strongest authored moment. Message plus CTA plus original imagery, video, pointer interaction, or a justified Three.js scene. GSAP intro; nav, message, and CTA usable before it ends.
2. Sections choreographed one by one: label, heading, media, then cards.
3. Optional pinned story scene, one idea per viewport.
4. Concrete conversion content.
5. Final CTA.
6. Footer.

## Numbers

| Number | Default | Failure prevented |
|---|---|---|
| Smooth-scroll engines | 1 (Lenis or Locomotive) | Two engines fighting ScrollTrigger |
| Lenis | lerp 0.08, wheelMultiplier 0.9 | Floaty or twitchy scroll |
| Eases | power3.out, power4.out, expo.out | Bounce, elastic, springy |
| Default duration | 0.85s | Abrupt transitions |
| Reveals | 0.75-1.1s, trigger `top 82%`, once | Elements that animate on every scroll tick |
| Text stagger | Words 0.035-0.07s, lines 0.08-0.14s | Word-by-word crawl |
| Card stagger | 0.06-0.1s | Slideshow feel |
| Hover | 0.35-0.6s, image zoom 1 to 1.06 over 0.7s | Large scale jumps |
| Magnetic | Scale under 1.03, card tilt under 4deg, movement under 16px | Gaming-style effects |
| Cursor lag | 0.25-0.45s, hidden on coarse pointer | Cursor on touch |
| Scroll scrub | 0.8-1.4, parallax speed 0.18 | Parallax that moves text |
| Pin | anticipatePin 1 | Pinned section overlapping the next |

## Signature moves

- Hero order: media first, headline lines second, copy third, CTA last.
- Masked word or line reveals with an unsplit `aria-label`, decorative spans `aria-hidden`.
- Clip-path image reveal (`inset(0 0 100% 0)` to `0%`, 1.1s) with the image settling from scale 1.08 to 1.
- Magnetic CTA via `gsap.quickTo`, x/y only.
- Three.js only with one responsibility: capped DPR, paused offscreen, static poster under reduced motion or WebGL failure.

## Do not

- Draw illustrations with model-authored SVG, CSS, or canvas. Use generated or licensed transparent PNG cutouts.
- Ship initials, illustrated heads, or generated people as customers. Photographs for every avatar.
- Fake a logo wall. Iconify Solar for icons, SVG Logos only for real companies, Logo Ipsum only as disclosed fiction.
- Gradient blobs, ornamental bento, glass everywhere, motion with no narrative role.
- Describe the result as award-winning.

## Effects it may use

- `scroll-scrubbed-word-reveal` for the hero statement.
- `shaders-cursor-ripples` when pointer response is the art direction.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/build-awwwards-quality-sites/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/cinematic-gsap-lenis-motion-system/SKILL.md
