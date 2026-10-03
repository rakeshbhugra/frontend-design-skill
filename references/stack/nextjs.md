# Stack: Next.js App Router

Purpose: wire the lock into a Next.js App Router project so tokens, fonts, images and metadata live in one place each.
Reach for `react-vite.md` instead when there is no SSR, SEO or OG requirement. Reach for `single-html.md` for a static one-pager.

## Layout

```
app/
  layout.tsx          html, body, fonts, metadata, theme provider. Server component
  globals.css         tokens on :root and [data-theme="dark"], Tailwind import
  page.tsx            marketing home
  (marketing)/…       scroll-once pages: hero timeline + scroll beats
  (app)/…             shell screens: sidebar + topbar, app motion track
  opengraph-image.tsx optional generated OG, else public/og.png
lib/motion.ts         registers GSAP plugins once
components/ui/        primitives and pulled registry components, re-tokened
public/images/<feature>/<name>.png
```

Route groups split the two surface types so each gets its own motion track (`05-motion.md`) without leaking a hero timeline into the shell.

## Tokens in globals.css

- Paste the `01-system.md` token sheet on `:root`, companion values under `:root[data-theme="dark"]`. Every component reads `var()` or a Tailwind role utility, never a hex.
- Tailwind v4: `@theme { --color-surface: …; }` in `globals.css`. Tailwind v3: `theme.extend.colors` in `tailwind.config.js` with the lock's role names (`surface`, `accent`), not raw values in `className`.
- Card, button and badge variants are components, not repeated class strings.
- Theme toggle: `next-themes` with `attribute="data-theme"` and `suppressHydrationWarning` on `<html>`. Single locked mode: no provider, set `color-scheme` on `html`.
- New pairings go through `scripts/check_contrast.py --matrix` before they ship.

## Fonts via next/font

```tsx
import { Unbounded, Albert_Sans } from "next/font/google"
const display = Unbounded({ subsets: ["latin"], variable: "--font-display", weight: ["600", "700"] })
const body = Albert_Sans({ subsets: ["latin"], variable: "--font-body", weight: ["400", "500"] })
<html className={`${display.variable} ${body.variable}`}>
```

Self-hosted, no render-blocking request, no layout shift. Reference `var(--font-display)` in the Tailwind font family config. Non-Google families (Pretendard for Korean) go through `next/font/local`.

## Images via next/image

```tsx
<Image src="/images/hero/capture.png" alt="" width={1280} height={800} priority sizes="(max-width: 60rem) 100vw, 640px" />
```

- `width` and `height` always, so nothing shifts. `priority` on the one above-fold hero image, lazy (the default) below.
- `fill` only inside a box with an explicit aspect ratio; set `height: auto` when CSS `aspect-ratio` drives the box.
- Remote hosts need `images.remotePatterns` in `next.config`. Sourced assets from `03-imagery.md` land in `public/images/<feature>/`.

## Server vs client split for motion

- Pages, layouts, data fetching and static sections stay server components.
- Motion lives in small `"use client"` leaves: a `<Reveal>` wrapper, the hero timeline, a scroll-scrubbed section, an animated number. Pass server-rendered children through them; never mark a whole page client for one animation.
- GSAP: `npm i gsap @gsap/react`. In `lib/motion.ts`: `gsap.registerPlugin(ScrollTrigger)` once. Client components call `useGSAP(() => …, { scope })`, which cleans up ScrollTrigger on unmount; a bare `useEffect` leaks instances across route changes.
- Motion (`motion/react`) only in client components that need springs, layout or exit animation. Don't run it beside GSAP unless a pulled component brought it.
- Guard `Date`, `Intl` and random output against server/client mismatch; inputs with `value` need `onChange` or use `defaultValue`.

## Metadata and OG

```tsx
export const metadata: Metadata = {
  title: "…", description: "…",
  openGraph: { images: [{ url: "/og.png", width: 1200, height: 630 }] },
}
export const viewport: Viewport = { themeColor: "<bg hex from lock>" }
```

`public/og.png` is 1200 x 630 in the lock's palette. `app/opengraph-image.tsx` (ImageResponse) replaces it when the OG must carry dynamic text. Keep `<title>` and description free of em dashes and template phrases (`04-build.md`).

## Registries

`npx shadcn@latest init` when `components.json` is missing, then register `@kokonutui` and `@bklit` namespaces once and pull with `npx shadcn@latest add @bklit/<chart>`. KokonutUI targets Tailwind v4; check the major first. Every pulled file is re-tokened to the lock in the same pass.

## Finish

`next build` clean, then `uv run scripts/anti_slop_scan.py app/ components/` and `uv run scripts/audit_motion.py app/ components/`. `PROMPT.md` at the project root per `04-build.md`, then `06-gate.md`.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/tech-stack-guides.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/interface-quality-rules.md (Hydration, Images sections)
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/library-selection.md (next-themes, motion boundary)
- General Next.js App Router conventions (route groups, next/font, next/image, metadata and viewport exports, opengraph-image)
