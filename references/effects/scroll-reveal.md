# Effect: scroll reveal (keyframe + IntersectionObserver)

Purpose: a dependency-free blur-rise reveal driven by a CSS keyframe that stays paused until the element enters the viewport. Tailwind-friendly.

Reach for `assets/reveal.css` + `reveal.js` instead when the project already uses `data-reveal` markup, or `assets/gsap-starter.js` when GSAP is loaded. Never run two reveal engines on one page.

## Use when

- Tailwind project, no GSAP, marketing or portfolio page.
- Sections and cards should enter once as they scroll into view.

## Snippet

```html
<style>
  @keyframes animationIn {
    0%   { opacity: 0; transform: translateY(30px); filter: blur(8px); }
    100% { opacity: 1; transform: translateY(0);    filter: blur(0); }
  }
  .animate-on-scroll { animation-play-state: paused !important; }
  .animate-on-scroll.animate { animation-play-state: running !important; }
  @media (prefers-reduced-motion: reduce) {
    .animate-on-scroll { animation: none !important; opacity: 1; transform: none; filter: none; }
  }
</style>
<script>
  (function () {
    const once = true;
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("animate");
        if (once) io.unobserve(entry.target);
      });
    }, { threshold: 0.2, rootMargin: "0px 0px -10% 0px" });
    document.addEventListener("DOMContentLoaded", () =>
      document.querySelectorAll(".animate-on-scroll").forEach((el) => io.observe(el)));
  })();
</script>

<div class="animate-on-scroll [animation:animationIn_0.8s_ease-out_0.1s_both]">...</div>
```

Stagger siblings by raising the delay in the Tailwind value: `0.1s`, `0.16s`, `0.22s` (60ms steps per `05-motion.md`).

## Numbers

| Knob | Default | Range |
|---|---:|---|
| Duration | 0.8s | 0.22s (restrained) to 0.8s (editorial) |
| Rise | 30px | 12 to 30px |
| Blur | 8px | 0 to 8px, never above 20px |
| Delay | 0.1s | 0 to 0.3s, 60ms per sibling |
| `threshold` | 0.2 | 0.15 to 0.3 |
| `rootMargin` | `0px 0px -10% 0px` | -40px to -10% bottom |
| Replay | `once = true` | keep true; replays on tiny scrolls read as noise |

## Pitfalls

1. Keyframes must be in the `<head>` before the observer script, and the keyframe name must match the Tailwind `[animation:...]` value exactly.
2. Elements already in view before the observer initialises still fire on `observe()`; if you init late, call the init again after layout.
3. Content stays invisible if JS fails: gate `.animate-on-scroll` under a `.js` class set by an inline script when JS is not guaranteed.
4. `filter: blur` on large images is paint-heavy; drop the blur channel on hero media and keep it for text.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/animation-on-scroll/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/animation-on-scroll/demo/index.html
