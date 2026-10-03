# Effect: marquee loop

Purpose: a seamless infinite horizontal loop for logos, tags, and short chips, built from one duplicated track and a linear transform.

Reach for a static logo grid instead when the items must be read or compared, or when the page already has its signature effect.

## Use when

- Logo wall, integration row, tag cloud, or short feature chips that are recognised at a glance.
- Marketing page only. Never on app shells.

## Snippet

```html
<div class="marquee" aria-label="Customer logos">
  <div class="marqueeTrack">
    <span>Logo A</span><span>Logo B</span><span>Logo C</span><span>Logo D</span>
    <span aria-hidden="true">Logo A</span><span aria-hidden="true">Logo B</span>
    <span aria-hidden="true">Logo C</span><span aria-hidden="true">Logo D</span>
  </div>
</div>
<style>
  .marquee {
    overflow: hidden;
    -webkit-mask-image: linear-gradient(90deg, transparent, #000 15%, #000 85%, transparent);
    mask-image: linear-gradient(90deg, transparent, #000 15%, #000 85%, transparent);
  }
  .marqueeTrack { display: flex; width: max-content; animation: marquee 18s linear infinite; }
  .marqueeTrack span { min-width: 220px; padding: 34px; }
  .marquee:hover .marqueeTrack { animation-play-state: paused; }
  .marquee.is-offscreen .marqueeTrack { animation-play-state: paused; }
  @keyframes marquee { to { transform: translateX(-50%); } }
  @media (prefers-reduced-motion: reduce) {
    .marqueeTrack { animation: none; flex-wrap: wrap; width: auto; }
    .marquee { mask-image: none; -webkit-mask-image: none; }
  }
</style>
```

The second copy is `aria-hidden` so screen readers hear each item once. Toggle `is-offscreen` with the `IntersectionObserver` from `05-motion.md`.

## Numbers

| Knob | Default | Note |
|---|---:|---|
| Duration | 18s | Scale with track width; the duplicate makes `-50%` exactly one cycle |
| Easing | `linear` | The only correct easing for a loop |
| Travel | `translateX(-50%)` | Requires exactly two identical copies |
| Item width | 220px min | Stable widths prevent the seam jumping |
| Edge mask | 15% to 85% | Fade both ends; drop the mask under reduced motion |
| Hover | pause | Only when the items are links |

## Pitfalls

1. Any width difference between the two copies produces a visible jump at the seam. Fix image sizes explicitly.
2. Do not put testimonials or anything the user must read on a marquee. It hides content and demands attention.
3. No heavy shadows or filters on every moving item; the track repaints continuously.
4. Reduced motion means a static wrapped row, not a slower marquee.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/marquee-loop/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/animation-on-scroll/demo/index.html (marquee track and mask values)
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/codex/optimize-web-animations/SKILL.md
