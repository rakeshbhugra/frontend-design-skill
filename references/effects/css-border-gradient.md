# Effect: CSS border gradient

Purpose: a 1px gradient edge on one surface level, drawn with two stacked backgrounds or a masked pseudo-element, so a featured card reads premium without a glow.

Reach for a plain hairline from the lock's border token instead when more than one hierarchy level would get it, or when the mood is paper, warm, or brutalist.

## Use when

- One surface needs to outrank its siblings: featured pricing tier, active tab, selected plan, hero panel, nav bar, modal.
- Dark glass or dark card UI reads flat with a solid border.

## Snippet (solid or translucent fill)

```css
.gradient-border {
  --surface: rgba(10, 14, 24, 0.72);
  --border-a: rgba(255, 255, 255, 0.34);
  --border-b: rgba(125, 92, 255, 0.36);   /* swap for the locked accent */
  --border-c: rgba(255, 255, 255, 0.08);
  border: 1px solid transparent;
  border-radius: 20px;
  background:
    linear-gradient(var(--surface), var(--surface)) padding-box,
    linear-gradient(135deg, var(--border-a), var(--border-b), var(--border-c)) border-box;
}
```

## Snippet (surface already has a complex background)

```css
.gradient-border-mask { position: relative; border-radius: 20px; }
.gradient-border-mask::before {
  content: ""; position: absolute; inset: 0; border-radius: inherit; padding: 1px;
  background: linear-gradient(145deg, rgba(255,255,255,.34), rgba(125,92,255,.36) 45%, rgba(255,255,255,.08));
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}
```

Tailwind one-off: `border border-transparent [background:linear-gradient(<surface>,<surface>)_padding-box,linear-gradient(135deg,<a>,<b>,<c>)_border-box]`.

## Numbers

| Knob | Default | Note |
|---|---:|---|
| Width | 1px | 2px only on large hero cards or active states |
| Angle | 135deg or 160deg | Light from top-left reads natural |
| Stops | 3: highlight, accent, fade | Neutral, one brand accent, neutral |
| Stop alpha | 0.34, 0.36, 0.08 | Keep most stops under 0.4 |
| Radius | inherit the surface | Any mismatch shows as a double edge |
| Animation | none | Animated or rainbow gradients are a slop tell |

## Pitfalls

1. Remove any existing `border-color`; two borders on one edge is gate 7 in `06-gate.md`.
2. Radius must match the surface exactly, including on the `::before` (`border-radius: inherit`).
3. Same alpha rarely works in light and dark. Check both themes, and check the accent stop against the lock's UI-safe list.
4. Focus states cannot rely on the gradient. Keep the `:focus-visible` ring from `05-motion.md` and gate 44.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/css-border-gradient/SKILL.md
