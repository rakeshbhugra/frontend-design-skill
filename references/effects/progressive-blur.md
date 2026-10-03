# Effect: progressive blur

Purpose: a stepped `backdrop-filter` stack that fades from sharp to blurred at the top or bottom edge, so fixed chrome floats over scrolling content without a hard line.

Reach for a solid or tinted bar instead when the page is light and text-heavy, or when `prefers-reduced-transparency` must be honoured with no design change.

## Use when

- Fixed nav over a dark or photographic page; a bottom action bar over a feed.
- The background behind the layer is real content (backdrop-filter blurs what is behind it, nothing else).

## Snippet (top edge)

```html
<div class="gradient-blur" aria-hidden="true">
  <div></div><div></div><div></div><div></div><div></div><div></div>
</div>
<style>
  .gradient-blur { position: fixed; z-index: 5; inset: 0 0 auto 0; height: 12%; pointer-events: none; }
  .gradient-blur > div, .gradient-blur::before, .gradient-blur::after { position: absolute; inset: 0; }
  .gradient-blur::before { content: ""; z-index: 1; backdrop-filter: blur(0.5px);
    mask: linear-gradient(to top, rgba(0,0,0,0) 0%, #000 12.5%, #000 25%, rgba(0,0,0,0) 37.5%); }
  .gradient-blur > div:nth-of-type(1) { z-index: 2; backdrop-filter: blur(1px);
    mask: linear-gradient(to top, rgba(0,0,0,0) 12.5%, #000 25%, #000 37.5%, rgba(0,0,0,0) 50%); }
  .gradient-blur > div:nth-of-type(2) { z-index: 3; backdrop-filter: blur(2px);
    mask: linear-gradient(to top, rgba(0,0,0,0) 25%, #000 37.5%, #000 50%, rgba(0,0,0,0) 62.5%); }
  .gradient-blur > div:nth-of-type(3) { z-index: 4; backdrop-filter: blur(4px);
    mask: linear-gradient(to top, rgba(0,0,0,0) 37.5%, #000 50%, #000 62.5%, rgba(0,0,0,0) 75%); }
  .gradient-blur > div:nth-of-type(4) { z-index: 5; backdrop-filter: blur(8px);
    mask: linear-gradient(to top, rgba(0,0,0,0) 50%, #000 62.5%, #000 75%, rgba(0,0,0,0) 87.5%); }
  .gradient-blur > div:nth-of-type(5) { z-index: 6; backdrop-filter: blur(16px);
    mask: linear-gradient(to top, rgba(0,0,0,0) 62.5%, #000 75%, #000 87.5%, rgba(0,0,0,0) 100%); }
  .gradient-blur > div:nth-of-type(6) { z-index: 7; backdrop-filter: blur(32px);
    mask: linear-gradient(to top, rgba(0,0,0,0) 75%, #000 87.5%, #000 100%); }
  .gradient-blur::after { content: ""; z-index: 8; backdrop-filter: blur(64px);
    mask: linear-gradient(to top, rgba(0,0,0,0) 87.5%, #000 100%); }
  @media (prefers-reduced-transparency: reduce) { .gradient-blur { display: none; } }
</style>
```

Bottom edge: `inset: auto 0 0 0`, `height: 65%` in the source, and every mask becomes `to bottom`. Add `-webkit-mask` for Safari.

## Numbers

| Knob | Default | Note |
|---|---:|---|
| Layers | 8 (before, 6 divs, after) | Each layer doubles blur: 0.5, 1, 2, 4, 8, 16, 32, 64px |
| Mask step | 12.5% | Each band overlaps its neighbours by one step |
| Height, top | 12% | Nav height plus one band |
| Height, bottom | 65% | Source default; 20 to 30% reads cleaner on mobile |
| `z-index` | 5 | Above content, below modals and the nav itself |

## Pitfalls

1. Keep `.gradient-blur` near the top of the DOM and `pointer-events: none`, or it blocks clicks on the nav.
2. Eight `backdrop-filter` layers cost paint on low-end mobile. Test `mobile-390x844.png` at scroll, and cut to 4 layers (1, 4, 16, 64px) if it stutters.
3. Nothing behind it means nothing to blur. On a flat solid background use a plain gradient instead.
4. Never stack it with glass cards or a second glow in the same viewport (gate 9 in `06-gate.md`).

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/progressive-blur/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/animation-guidelines.md (reduced-transparency rule)
