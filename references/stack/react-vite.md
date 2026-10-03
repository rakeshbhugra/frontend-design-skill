# Stack: React + Vite (house style)

Purpose: build app screens by copying the `frontend-app` template and wiring the lock from `01-system.md` into its `@theme` block.
Reach for `nextjs.md` instead when the surface needs SSR, metadata or OG images. Reach for `single-html.md` for a one-page static demo.

**Override rule:** the template ships OLED-black monochrome. That look applies only when the user asks for it. Otherwise the lock's palette, type, radius and mode replace the template values, one line each, before the first screen is built.

## Scaffold

```bash
cp -R ~/.claude-personal/skills/frontend-app/template/. frontend/   # or ./ when the repo is the frontend
cd frontend && npm install && npm run dev
```

Existing `frontend/`? Copy in only what is missing (`src/index.css`, `src/components/ui/`). Standalone app? Delete the `/api` proxy in `vite.config.ts`. Closed stack: React 19, Vite, TypeScript, Tailwind v4 (`@tailwindcss/vite`), React Router, TanStack Query 5, Zustand 5, `motion` 13 (`motion/react`), `lucide-react`, Vitest. Don't shop.

## Directory shape

```
src/
  main.tsx  app.tsx  index.css            providers, route table, @theme tokens
  lib/      api.ts (the only fetch)  cn.ts  <util>.ts
  components/ layout.tsx  ui/ (button card badge input skeleton empty-state page-header)  motion/fade-in.tsx
  features/<feature>/ types.ts  api.ts  hooks.ts  store.ts?  <feature>-page.tsx  <part>.tsx  <feature>-page.test.tsx
  test/     setup.ts  utils.tsx
public/     images/<feature>/<name>.png   og.png (1200 x 630)
```

Files `kebab-case.tsx`, components `PascalCase`, hooks `useThing`. 150 code lines guideline, 250 hard stop; past it, extract `<part>.tsx` (row, toolbar, drawer body, states with copy). `components/ui/` never imports `features/`; nothing imports another feature. Promote to `components/` on the second use.

## Tokens from the lock

Tailwind v4 turns each `@theme` line into utilities (`--color-surface` gives `bg-surface`). Replace the template values with the lock:

| Lock role | `@theme` token | Utility |
|---|---|---|
| bg | `--color-bg` | `bg-bg` |
| surface | `--color-surface`, `--color-surface-2` (one step raised) | `bg-surface` |
| border | `--color-border`, `--color-border-bright` (hover, focus) | `border-border` |
| text, text-muted | `--color-text`, `--color-text-dim`, `--color-text-faint` | `text-text-dim` |
| primary, on-primary | `--color-accent`, `--color-accent-ink` | `bg-accent text-accent-ink` |
| secondary, accent | add `--color-secondary`, `--color-highlight`; never inline | |
| display, body fonts | `--font-sans`, `--font-mono` (mono for labels, code, data) | `font-mono` |
| radius sm/md/lg | `--radius-control`, `--radius-card` | `rounded-control` |
| motion ease | `--ease-soft: cubic-bezier(0.16, 1, 0.3, 1)` | |

Fonts load via `<link rel="preconnect">` plus one stylesheet in `index.html`. `html { color-scheme }` and `<meta name="theme-color">` match the lock's mode. Toggle mode: light values in `@theme`, dark overrides under `:root[data-theme="dark"]` in `@layer base`, and the pre-paint `data-theme` script from `single-html.md` in `index.html`. Every pairing re-run through `scripts/check_contrast.py --matrix`. No color literal in any component; a missing shade is a new `@theme` line.

## Data rules

- Server data in TanStack Query, tab-local UI state in Zustand, everything derivable computed at render. Never `useEffect(() => setLocal(data))`; store the id, look the object up.
- `lib/api.ts` is the only file calling `fetch`, paths relative, `ApiError` carries `status`.
- Query keys as a factory in the feature's `api.ts` (`blockKeys.all / lists() / list(filters) / detail(id)`). Never inline in a component.
- Mutations invalidate (`qc.invalidateQueries({ queryKey: blockKeys.lists() })`); `setQueryData` only for optimistic toggles, reorders, likes.
- `retry: (n, e) => e instanceof ApiError && e.status < 500 ? false : n < 2`. Set `staleTime` per query; the default `0` refetches on every mount and reads as flicker.
- Linkable state (tab, open detail, search) lives in the URL via `useSearchParams`, not Zustand. One store per feature, selector reads.
- Tests stub `fetch`, not hooks. Query by role and label.

## Components

Seven primitives ship: `Button` (`primary ghost danger` x `sm md`), `Card` (`interactive?`), `Badge`, `Input` with `<Field>` label, `Skeleton`, `EmptyState`, `PageHeader`. Add an eighth on the third repeat. Write each as extractable: spread native props, `className` last through `cn()`, tokens only, a `variant` prop only once two variants exist. `primary` gets one job per screen region.

Every query renders four states, shaped so nothing shifts when data lands:

```tsx
if (isPending) return <BlockListSkeleton />
if (isError)   return <ErrorState error={error} onRetry={refetch} />
if (!data.length) return <EmptyState … />   // carries the action that fixes it
return <BlockList blocks={data} />
```

Pulling a component: copy the one shadcn/ui file into `components/ui/`, never `shadcn init`. Then `framer-motion` → `motion/react`, alias paths → relative, re-token (`background→bg`, `card/popover→surface`, `muted→surface-2`, `border/input→border`, `foreground→text`, `muted-foreground→text-faint`, `primary/ring→accent`), drop unused variants and any mode branch the lock does not have. Keep a Radix dep only for focus trap, dismissal, positioning. Full defaults table in `04-build.md`.

## Icons and images

- Icons are `lucide-react`: `<Inbox aria-hidden className="size-4 text-text-faint" />`. Size with `size-4`/`size-5`, color with a token, `aria-hidden` unless the icon is the label (then `aria-label` on the button). One family, never a generated PNG for an icon.
- Sourced or generated art (`03-imagery.md`) goes to `public/images/<feature>/<name>.png`, referenced as `/images/<feature>/<name>.png`. OG image at `public/og.png`, 1200 x 630, referenced from `index.html`. Never `import` static art.
- `<img src width={640} height={360} alt="" loading="lazy" className="rounded-card border border-border object-cover" />`. Drop `loading="lazy"` above the fold. Real `alt` only when the image carries information.

## Motion hook-ins

`motion` 13 from `motion/react`, `<MotionConfig reducedMotion="user">` already wraps the app, `index.css` neutralises CSS transitions under the media query. Vocabulary (`05-motion.md` owns the full rules):

| Move | Values | Where |
|---|---|---|
| Entrance | `opacity 0→1`, `y 8→0`, 200ms, `--ease-soft` | `<FadeIn>` |
| Stagger | 40ms per child, cap 8 | `<FadeIn.List>` + `<FadeIn.Item>` |
| Hover lift | `y -1px`, border → `border-bright`, 120ms | `Card interactive`, Tailwind transition |
| Press | template ships `scale 0.98`, 80ms; `04-build.md` allows down to `0.96` | `Button` |
| Exit | `opacity 1→0`, 120ms, no movement | `AnimatePresence` |

300ms ceiling in app chrome. `layout` and `AnimatePresence` only for list reorder and disclosure height. Entrances key on mount, not on refetch. Marketing route inside the same repo: `npm i gsap @gsap/react`, register ScrollTrigger once in `lib/motion.ts`, drive from `useGSAP`, and keep that route on the marketing track only.

## Finish

`npm run lint && npm test`, then `uv run scripts/anti_slop_scan.py src/` and `uv run scripts/audit_motion.py src/`. Write `PROMPT.md` at the frontend root per `04-build.md`, then `06-gate.md`.

Distilled from:
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/SKILL.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/references/structure.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/references/tokens.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/references/components.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/references/data.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/references/motion.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/references/imagery.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/template/ (package.json, src/index.css, vite.config.ts, src/components/ui/button.tsx, src/components/motion/fade-in.tsx, src/lib/api.ts)
