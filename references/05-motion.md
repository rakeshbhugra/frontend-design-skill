# Stage 5: Motion

Purpose: give every screen a fixed motion vocabulary, a per-page budget, and a reduced-motion contract, then prove it with `audit_motion.py` before the gate.

Reach for `effects/INDEX.md` instead when the brief asks for one signature effect (marquee, progressive blur, word reveal). Reach for `04-build.md` when the four states do not work yet. Motion comes after states, never before.

## Decision gate, run before writing any animation

| Question | Ship when | Delete when |
|---|---|---|
| How often is it seen | First run, rare, explanatory, marketing scroll | Keyboard actions, command palette, core nav, dense lists, anything seen dozens of times a day |
| What does it answer | "What changed", "where did this come from", "did it hear me" | Only "it looks cool" |
| Within budget | UI under 300ms, pieces under 200ms | Needs slow showmanship to work |
| Helps the task | Clarifies state, hierarchy, progress | Moves data the user is reading or acting on |

Two tracks, chosen per screen. Marketing narrative: GSAP + ScrollTrigger via `assets/gsap-starter.js`. App shell: CSS transitions plus `gsap.to()` without ScrollTrigger, or the stack's own library (Motion for React). One engine per project. Record the pick in `style-lock.md` under Motion.

## Tokens, paste into `:root`

```css
:root {
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
  --ease-soft: cubic-bezier(0.16, 1, 0.3, 1);
}
```

## Durations

| Move | Duration | Travel | Easing |
|---|---:|---|---|
| Press | 80 to 120ms | `scale(0.97)` on pointer down | `--ease-out` |
| Hover | 100 to 150ms | `translateY(-1px)` to `-2px`, border or shadow shift | `--ease-out` |
| State change (toggle, tab, select) | 180 to 260ms | opacity, 8 to 12px slide in nav direction | `--ease-out` |
| Enter (card, row, panel) | 200ms app, 220ms marketing | `opacity 0→1`, `y 8→0` app, `y 12 to 16→0` marketing | `--ease-soft` |
| Exit | 120ms | opacity only, no movement | `--ease-out` |
| Popover, tooltip, dropdown | 125 to 200ms | `scale(0.95)` + opacity from the trigger origin | `--ease-out` |
| Modal, drawer, sheet | 200 to 500ms | sheets travel `translateY(100%)`, modals scale from center | `--ease-drawer` sheets, `--ease-out` modals |
| Page or view transition | under 400ms total | consistent direction for "forward" | `--ease-in-out` |
| Scroll reveal | 220ms | 12 to 16px rise | `--ease-soft` or `power3.out` |
| Hero sequence | 800 to 1600ms total, at most 4 beats | headline, subhead + actions, one proof visual | `power2.out` |

Ceilings: nothing in app chrome over 300ms. UI over 300ms needs a stated reason (modal, drawer, marketing beat). Total staggered sequence under 700ms. Button feedback within 100ms of press regardless of when the action completes. Never show a spinner for anything that resolves under 400ms.

## Easing rules

- Enter: ease-out. Exit: faster, opacity only. Move between positions: ease-in-out. Linear only for continuous motion (progress bars, marquee).
- Never `ease-in` on UI. Never browser default `ease`. Never overshoot (`cubic-bezier(0.34, 1.56, ...)`, `elastic`, `back`) on buttons, modals, tooltips, or state changes. Springs only for drag, swipe, and interruptible layout: `{ type: "spring", duration: 0.4, bounce: 0 }`, `bounce: 0.2` only on momentum release.
- Start from `scale(0.95)` never `scale(0)`; `transform-origin` at the trigger for popovers, center for modals; exit along the entry path.

## Stagger

| Context | Step | Cap |
|---|---:|---|
| App lists and grids on first paint | 40ms | 8 children, then the rest appear together |
| Marketing reveal groups, hero lines | 60ms (`--reveal-stagger-step`, `staggerStep: 0.06`), 40 to 90ms range | sequence under 700ms, hero 4 beats |

Smaller steps on mobile. Lead with the most important element. Entrance fires on mount, never on refetch. Key it.

## Motion budget per page

Count these: every entrance pattern, every scroll-reveal group, every hover family, every perpetual animation (marquee, pulse, ambient canvas), every scrubbed or pinned section, the signature effect.

| Surface | Budget |
|---|---|
| Marketing page | 1 hero sequence (4 beats max), 1 signature effect from `effects/INDEX.md`, at most 2 pinned or scrubbed sections, 1 reveal pattern reused everywhere, 1 hover family |
| App shell, forms | Five moves only: entrance, stagger, hover lift, press, exit. Zero perpetual animation, zero scroll effects, zero signature effects |

Delete motion where daily use makes it annoying. If a user meets it more than a handful of times per session, it is feedback, not choreography: 120ms or less, opacity or a 1 to 2px shift, never a slide. Never animate text content, font-size, page layout on data arrival (reserve space with a skeleton), or scroll position. No parallax on app screens.

## Scroll reveal defaults

Markup is shared by both engines: `<div data-reveal>` for one element, `<div data-reveal data-reveal-group>` to stagger its children.

| Engine | Trigger | Once | Distance | Duration |
|---|---|---|---|---|
| `assets/reveal.css` + `reveal.js` (no deps) | IntersectionObserver `threshold: 0.15`, `rootMargin: "0px 0px -40px 0px"` | yes | `--reveal-distance: 12px` | `--reveal-duration: 220ms` |
| `assets/gsap-starter.js` | ScrollTrigger `start: "top 85%"` | yes | `distance: 16` | `duration: 0.22` |

Rules: animate once, never replay on small scrolls. Elements already in view on load must reveal without a scroll (ScrollTrigger does this; the IO fallback fires on observe). Only `opacity` and `transform`; `filter: blur(8px)` max as an optional third channel on marketing headlines. Call `ScrollTrigger.refresh()` after images load. If JavaScript can fail, the page must still show content: gate the hidden state on a `.js` class set by an inline script.

## Reduced motion contract

`@media (prefers-reduced-motion: reduce)` is mandatory on every animation, bespoke or starter.

- Keep: opacity and color changes, the complete end state, all state feedback. Spatial motion collapses to an opacity crossfade of 150ms or less, not to nothing.
- Drop: slides, springs, parallax, scrub, pin, ambient loops, cursor follow, the marquee (static wrap).
- Drag follow is never gated (it is the user's own pointer). The release settle is: critically damped, no overshoot. Never gate information behind an animation; a state shown only by a pulse does not exist for this user.
- Hover motion only under `@media (hover: hover) and (pointer: fine)`. Translucent surfaces also handle `prefers-reduced-transparency` and `prefers-contrast: more`: raise opacity, drop blur, add a visible border.

`gsap-starter.js` branches with `gsap.matchMedia()`. `reveal.css` sets `transition-duration: 0.01ms` and `transform: none`. Motion (React): `<MotionConfig reducedMotion="user">`.

## Performance and cleanup

- Animate only `transform` and `opacity`. Never `width`, `height`, `top`, `left`, `margin`, `padding`, `border-radius`, `box-shadow`. Never `transition: all`. Blur under 20px. Clamp canvas DPR to 1 to 2.
- Offscreen pause: one `IntersectionObserver` at `threshold: 0.01` toggling `is-offscreen` on the section and its animated children, then `animation-play-state: paused !important` (include `::before` and `::after` glimmers). Canvas, WebGL, and physics loops cancel `requestAnimationFrame` when offscreen and on `document.hidden`, restart on re-entry, cap the frame delta on resume.
- Unmount cleanup (React, SPA routes): `gsap.context()` then `ctx.revert()`; `ScrollTrigger.getAll().forEach(t => t.kill())`; clear every timeout and interval; cancel RAF; disconnect Intersection, Resize, Mutation observers; remove window and document listeners with the same handler reference; dispose Three textures, materials, geometries, renderers; stop media streams; guard async loaders with an `isDisposed` flag.

## Recipe: GSAP marketing page

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="assets/gsap-starter.js"></script>
<script>
  TastemakerMotion.init({ duration: 0.22, distance: 16, ease: "power3.out", staggerStep: 0.06 });
  gsap.matchMedia().add("(prefers-reduced-motion: no-preference)", () => {
    gsap.timeline({ defaults: { ease: "power2.out", duration: 0.6 } })
      .from(".hero-title", { y: 24, autoAlpha: 0 })
      .from(".hero-lede, .hero-actions", { y: 16, autoAlpha: 0, stagger: 0.06 }, "-=0.3")
      .from(".hero-visual", { y: 16, autoAlpha: 0 }, "-=0.2");
  });
</script>
```

## Recipe: CSS-only app shell

```html
<link rel="stylesheet" href="assets/reveal.css">
<script src="assets/reveal.js" defer></script>
<style>
  .button, .card { transition: transform 120ms var(--ease-out), border-color 120ms var(--ease-out); }
  .button:active { transform: scale(0.97); }
  @media (hover: hover) and (pointer: fine) { .card:hover { transform: translateY(-1px); } }
  @media (prefers-reduced-motion: reduce) { .button, .card { transition-duration: 0.01ms; transform: none !important; } }
</style>
```

## Verify

```bash
uv run scripts/audit_motion.py <changed-ui-paths> --max-findings 50
```

Rules it fires: `transition-all`, `ease-in-ui`, `scale-zero`, `origin-center` (popover scaling from center), `layout-transition`, `long-duration`, `missing-reduced-motion`, `ungated-hover-motion`. Exit 1 on any HIGH. Fix every HIGH; a MEDIUM needs a fix or a one-line reason in `decisions.log`. Then the feel pass: slow key animations to 25% and check origins; spam tabs and toasts (motion retargets, never restarts); toggle reduced motion (movement drops, feedback stays); watch the page once at normal speed. If you noticed the animation, it is too slow or too big. Write feel, curves, durations, distance, and the audit date into `style-lock.md` under Motion.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/animation-guidelines.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/scripts/audit_motion.py
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/assets/reveal.css
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/assets/reveal.js
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/assets/gsap-starter.js
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/animation-systems/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/gsap/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/codex/optimize-web-animations/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/skills/animation-principles/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/skills/doherty-threshold/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/skills/micro-interaction-spec/SKILL.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/references/motion.md
