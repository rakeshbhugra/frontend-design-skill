# Stack: single HTML, no build

Purpose: ship one `index.html` that runs from a file server with no bundler, tokens on `:root`, motion from the vendored assets.
Reach for `react-vite.md` instead when the output has routing, server data or more than one screen. Reach for `nextjs.md` when SEO, SSR or OG images matter.

## File layout

```
<out>/
  index.html        all HTML, CSS (<style>) and JS (<script>) for the page
  PROMPT.md         recreate + remix prompts, see 04-build.md
  preview.jpg       1280 x 720 browser screenshot of the finished page
  assets/           images, fonts, models, textures, vendored reveal.css / reveal.js / gsap-starter.js
```

- Relative paths only. No build step. Fictional portable data.
- Copy the motion files from the skill root: `cp <skill>/assets/reveal.css <skill>/assets/reveal.js <out>/assets/` (add `gsap-starter.js` on the GSAP path).
- Run: `python3 -m http.server 4173 -d <out>`.

## Head

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="<bg hex from lock>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=<Display>:wght@600;700&family=<Body>:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/reveal.css">
```

Never `user-scalable=no` or `maximum-scale=1`. Korean type loads from Pretendard's own CDN, not Google Fonts (`01-system.md`).

## Tokens

Paste the `01-system.md` token sheet into `<style>` with the lock's hexes. First line of the `<style>` is the build stamp comment. Every rule reads `var(--token)`; a literal hex or magic px inside a component rule means a missing token, add it to `:root`.

```css
:root { --color-bg: …; --color-surface: …; --color-text: …; --color-primary: …; --space-4: 16px; --radius-md: 8px; }
html { color-scheme: light; background: var(--color-bg); color: var(--color-text); }
```

## Dark mode

One mechanism: `data-theme` on `<html>`. Default from `prefers-color-scheme`, `localStorage` override read before first paint. Skip the whole block when the lock says single mode.

```html
<script>
  var t = localStorage.getItem("theme") ||
    (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  document.documentElement.dataset.theme = t;
</script>
```

```css
:root[data-theme="dark"] { /* companion values from the same --seed, re-verified with check_contrast.py --matrix */ }
:root[data-theme="dark"] html, [data-theme="dark"] { color-scheme: dark; }
```

On toggle: inject `*,*::before,*::after{transition:none !important}`, force a reflow, remove it next frame, or the whole page smears.

## Motion: two paths, same markup

Mark elements `data-reveal`; mark a parent `data-reveal-group` to stagger its children. Both paths honour `prefers-reduced-motion` and observe at `threshold 0.15`, `rootMargin -40px`.

CSS path (default, zero dependencies), before `</body>`:

```html
<script src="assets/reveal.js"></script>
```

`reveal.css` variables: `--reveal-duration: 220ms`, `--reveal-distance: 12px`, `--reveal-easing: cubic-bezier(0.16, 1, 0.3, 1)`, `--reveal-stagger-step: 60ms`. Retune them to the lock's Motion line, never write new keyframes per project.

GSAP path (marketing pages with a hero timeline or scroll storytelling, per `05-motion.md`):

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="assets/gsap-starter.js"></script>
<script>TastemakerMotion.init({ duration: 0.22, distance: 16, ease: "power3.out", staggerStep: 0.06 });</script>
```

## CDN allowlist

| Library | Pinned URL | When |
|---|---|---|
| GSAP core | `cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js` | hero timeline, sequenced page moments |
| ScrollTrigger | `cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js` | scrubbed, pinned, parallax sections |
| Three.js | `cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js` | WebGL backgrounds and 3D objects only |
| Lenis | no pinned CDN in sources; the demos import `lenis` through a bundler | smooth scroll on cinematic marketing pages. Pin a version explicitly if added via CDN |

Load in this order: fonts, GSAP, ScrollTrigger, Three, then the starter, then page script. Nothing else from a CDN without stating why in `PROMPT.md`.

## Outputs and checks

1. `preview.jpg`: 1280 x 720 screenshot at the top of the page after fonts load.
2. `PROMPT.md`: recreate prompt and remix prompt per `04-build.md`.
3. `uv run scripts/anti_slop_scan.py <out>/index.html` and `uv run scripts/audit_motion.py <out>/index.html` come back with no HIGH before `06-gate.md`.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/DEMOS.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/tech-stack-guides.md
- /Users/rakeshbhugra/code/frontend-design-skill/assets/reveal.css
- /Users/rakeshbhugra/code/frontend-design-skill/assets/reveal.js
- /Users/rakeshbhugra/code/frontend-design-skill/assets/gsap-starter.js
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design (pinned CDN tags across demo/index.html files)
