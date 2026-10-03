# Effects index

Purpose: the optional signature effects this skill knows, with cost and the exact context each one earns.

Reach for `05-motion.md` instead for baseline motion (reveal, press, hover, stagger). Those are not effects, they are the floor.

## Rules

1. One signature effect per page, maximum. The hero sequence and the reveal pattern do not count; everything in this table does.
2. Effects never appear on daily-use app screens (dashboards, settings, editors, forms). Marketing narrative and portfolio surfaces only.
3. Every effect ships with its `prefers-reduced-motion` branch and pauses offscreen (`05-motion.md`). Expensive rows also clamp DPR to 1 to 2 and stop their loop on `document.hidden`.
4. An effect must survive the removal test and gate 68 in `06-gate.md`: name its job, remove it mentally, keep it only if meaning, state, hierarchy, or brand character is lost.
5. Log the pick in `style-lock.md` under Effects and in `decisions.log` with `axis: "effects"`.

Cost: cheap = CSS only, no per-frame work. Medium = JS observers or GSAP tweens, transform and opacity only. Expensive = canvas, WebGL, shader, or per-frame pointer work.

## Table

| Effect | Where | Cost | Use when | Never with |
|---|---|---|---|---|
| Scroll reveal (keyframe + IO) | `scroll-reveal.md` | cheap | Tailwind projects that cannot load GSAP and want blur-rise reveals | `reveal.js` or `gsap-starter.js` on the same page (pick one engine) |
| Marquee loop | `marquee-loop.md` | cheap | Logo walls, tag rows, short chips that are recognised, not read | Testimonials or any copy the user must read; more than one per page |
| Progressive blur | `progressive-blur.md` | medium | Fixed nav or bottom bar over scrolling content on a dark or photographic page | `prefers-reduced-transparency`; large heights on low-end mobile; glass cards already on the page |
| CSS border gradient | `css-border-gradient.md` | cheap | One hierarchy level needs a premium edge: featured plan, active tab, hero panel | Rainbow or animated gradients; every card at once; an existing `border-color` |
| CSS alpha masking | `mengto:web-design/css-alpha-masking` | cheap | Edge fades on horizontal scrollers and marquees | Masks over text that must stay legible at the edge |
| Beautiful shadows | `mengto:web-design/beautiful-shadows` | cheap | Compact cards, popovers, hero media that need layered neutral elevation | Hairline border on the same edge; many animated shadows at once |
| Staggered word reveal | `mengto:web-design/staggered-word-reveal` | medium | Editorial hero copy, section intros under 12 words | Body copy; app screens; more than one headline per viewport |
| Masked reveal | `mengto:web-design/masked-reveal` | medium | GSAP projects where a headline should rise through an overflow mask | Staggered word reveal on the same page; pages without GSAP |
| Scroll progress timeline | `mengto:web-design/scroll-progress-timeline` | medium | Ordered process with 3 to 8 steps: onboarding, roadmap, how it works | Unordered feature lists; pinned sections elsewhere on the page |
| Liquid metal border | `mengto:web-design/liquid-metal-border` | expensive | React, one selected or premium control needs a metallic edge | Non-React stacks; more than a handful of instances; reduced motion without a static fallback |
| Mesh gradient dark blue | `mengto:web-design/mesh-gradient-dark-blue-clean` | expensive | Whole-page dark navy system with a procedural backdrop | Light mode; any second background effect; pages with photography |
| Dither background | `mengto:web-design/dither-background` | expensive | Monochrome, near-black atmospheric field behind a hero | Colour palettes; text-heavy sections; mesh or atmosphere backgrounds |
| Atmosphere background | `mengto:web-design/atmosphere-background` | expensive | Dark hero that needs a single luminous bloom and drifting light folds | Dither, mesh, or corner lasers on the same page |
| Corner lasers | `mengto:web-design/corner-lasers` | expensive | Dark tech hero with one emitter node and thin beams | Playful, warm, or paper moods; any other background effect |
| Container lines | `mengto:web-design/container-lines` | cheap | Editorial or technical layouts that show the container edges | Pages with a decorative grid already; app shells |
| Number details | `mengto:web-design/number-details` | cheap | 01, 02, 03 markers on a real sequence (steps, chapters) | Numbering that does not encode order; every section head |
| Scroll-scrubbed word reveal | `mengto:web-design/scroll-scrubbed-word-reveal` | medium | One manifesto or statement passage under 40 words, paced by scroll, 120 to 220vh span | Staggered word reveal on the same page; body copy; app screens |
| Shader cursor ripples | `mengto:web-design/shaders-cursor-ripples` | expensive | Pointer response is the art direction of a cinematic hero | Coarse pointers without a static fallback; any background effect |
| Reveal hover effect | `mengto:web-design/reveal-hover-effect` | expensive | Before and after, x-ray, material or product-detail hero with two aligned images | Touch-first audiences; hover as the only way to see the second image |

Path prefix `mengto:web-design/<name>` resolves to `/Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/<name>/SKILL.md`. Read that file and its `demo/index.html` for the real code before use; do not reconstruct the effect from memory.

## Background effects share one slot

Mesh gradient, dither, atmosphere, and corner lasers are all "the background". A page gets at most one, and that one is the page's signature effect. Pair it only with cheap rows (border gradient, container lines, number details) and only when gate 9 in `06-gate.md` still passes.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/animation-on-scroll/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/marquee-loop/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/progressive-blur/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/css-border-gradient/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/*/SKILL.md (frontmatter descriptions of the 13 path-only rows)
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/ui/no-ai-design-slop/ARTICLE.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/animation-guidelines.md
