# Stage 4: Build

Purpose: turn the locked system (`01-system.md`), structure picks and sourced assets (`03-imagery.md`) into shipped screens where every component carries every state.
Reach for `verbs/audit.md` instead when the screen already exists and the ask is a critique. Reach for `06-gate.md` once the build is done, not during.

## Build order

| # | Step | Done when |
|---|---|---|
| 1 | Shell | nav, page frame, footer render with lock tokens; one route inside |
| 2 | Hero | one promise, one lede, one primary CTA, one visual; fits 1280x800 |
| 3 | Sections | each section is a stated archetype pick, mostly something to look at, text as caption |
| 4 | States | every list, query, form and control has the matrix below reachable |
| 5 | Responsive | single column below 60rem, display type steps down below 40rem, no horizontal scroll at 320px |
| 6 | Dark mode | only what the lock's Dark mode line says; every pair re-run through `scripts/check_contrast.py --matrix` |
| 7 | Motion | wired now, not deferred. Track per screen type, see `05-motion.md` |
| 8 | PROMPT.md | written next to the output, see the last section |

App screens go slice by slice: `types → api → hooks → page → four states`. Do not start slice 2 until slice 1 has all four states. Motion lands after a slice is stable, never mid-restructure.

Non-negotiables while building: show, don't tell (a chart, mockup, before/after or stat tile beats a paragraph); no section asset-empty; every new color pairing is in the lock's text-safe or UI-safe list or gets `--matrix` re-run; spacing comes from the lock scale, never improvised per card.

## Component craft

| Rule | Value |
|---|---|
| Concentric radius | outer radius = inner radius + padding. Never equal radii on nested boxes |
| Optical alignment | icons in buttons, play triangles, asymmetric glyphs get a manual nudge. Geometric centre is the start, not the answer |
| Hit area | 24x24px minimum (WCAG 2.5.8 AA). 44x44px touch, 40x40px desktop. Extend with a pseudo-element, keep the visual small |
| Hit area spacing | 12px between adjacent bordered controls, 24px around borderless icon-only ones. Extended areas never overlap |
| Decorative layers | `pointer-events: none` on glows, gradients, overlays |
| Depth | shadows for elevation, borders for structure (dividers, selected, focus). Layered transparent `box-shadow`, never a border that only fakes depth |
| Dark ground | borders replace shadows. A shadow on `#000` is invisible. Card with no border disappears |
| Image outline | 1px, `oklch(0 0 0 / 0.1)` light, `oklch(1 0 0 / 0.1)` dark. Never a tinted or slate neutral |
| Icon stroke | 1.5px beside 400 weight text, 2px beside 600. One stroke weight per set, one icon family per page |
| Icon color | `currentColor`; hover, selected, disabled come from CSS, not separate assets. Outline default, fill for active |
| Icon swap | animate `scale 0.25 → 1`, `opacity 0 → 1`, `blur 4px → 0`. Both icons stay in the DOM |
| Press | `scale(0.96)`. Below 0.95 reads exaggerated |
| Hover | gated with `@media (hover: hover)`. Contrast must go up on hover, never down |
| Transitions | name the properties. `transition: all` is a gate failure |
| Fake chrome | never hand-draw a browser bar, phone frame or IDE window. Real capture in a `<figure>` or nothing |
| Emoji | never as a feature, step or value icon |

## Layout

- Group with space first, background shape second, line last. Gap between groups is at least 2x the gap inside one: 8px intra, 16px+ inter.
- One spacing step per level of subordination, 16px default. Align to shared edges; each stray edge is noise.
- Reading order: top to bottom, leading to trailing. Use `padding-inline-start`, `margin-inline-end`, not left/right.
- Controls look like controls: background shape, border, or a fixed placement zone. Never styled like the static text beside them.
- Hidden content gets a cue: next item peeks 16 to 32px past the scroll edge, or a visible disclosure control.
- Full-width buttons stay inside layout margins, 16px inline on mobile. Content bleeds to the viewport, controls and text stay inside `env(safe-area-inset-*)`.
- Max measure 60 to 75ch. No fixed width or height on any text container; rows wrap. Flex children get `min-w-0` or truncation never fires. Overflow handled with truncate, line-clamp or `break-words`.
- Breakpoints come from content, not 768/1024 presets. Container queries for component-level adaptation. Test smallest and largest first.
- Card padding floor 24px. Internal padding <= external gap, always.
- Two columns of unequal height: centre the shorter, fill it with a real element, or cap the taller. Never leave the gap to chance.
- One section separator mechanism per project: alternating surface tint, hairline, or padding tiers alone. Record it in the lock.
- Section headline caps at 50 to 65% of the hero display size and reads in 1 to 2 lines.
- Lists over ~50 items virtualize. Never read layout during render.
- Critical action never sits where scroll or resize clips it.

## State matrix

Every list, query, form and primary control ships all of these. Populated-only is unfinished.

| State | Default |
|---|---|
| Loading | skeleton shaped like the content, same box sizes, same grid. No indicator under 100ms; subtle 100ms to 1s; visible with progress 1 to 10s; over 10s add estimate and background option. Content fades in, list items stagger 30 to 50ms. Label ends with `…` (`Loading…`). Shimmer honours reduced motion |
| Empty | what this place is, how to fill it, one action. Search/filter empty names the query and offers "Clear filters". Never persistent info here |
| Error | what happened, what to do, beside where it broke. Retry for transient failures. Keep the user's input. Never "Oops", never a stack, never blame |
| Success | toast 3 to 5s auto-dismiss via `role="status"`; toasts carrying an action or an error stay until dismissed. Undo beats "Are you sure?" |
| Disabled | native `disabled` when truly unavailable. `aria-disabled="true"` only when it must stay focusable, then block behaviour in code. Tooltip on a disabled control goes beside it, not on it |
| Hover | contrast up, `@media (hover: hover)` |
| Focus | `:focus-visible` ring, 2px solid, verified against every adjacent color |
| Pressed | `scale(0.96)` plus a static cue (color, icon or label). Motion is never the only feedback |

Destructive actions: confirmation or undo window, visually separated from safe actions. Never immediate.

## Forms and feedback

- Single column. Top-aligned labels. Field width matches expected input length. Mark optional, not required.
- Every input: visible `<label for>`, `name`, `autocomplete`, correct `type` and `inputmode`. `spellcheck="false"` on emails, codes, usernames. Never block paste.
- Placeholder is an example ending with `…` (`name@example.com…`), never the label. Helper text sits below the label, above the field.
- Input choice: 5 or fewer options radio, 6+ select, multiple checkboxes, dates a picker or segmented fields, password with show/hide, phone and card with masking.
- Validate on blur or submit, not per keystroke. Error directly below the field, `aria-invalid="true"`, `aria-describedby` pointing at it, focus the first invalid field. Hint phrased positively before the mistake ("Use only letters").
- Submit stays enabled until the request starts, then disable with a spinner and the original label.
- Warn before leaving unsaved changes. Character counts always visible when a limit exists.
- Multi-step: visible progress, back without data loss, save progress, review step before a high-stakes submit.
- Feedback hierarchy: inline first, then component, then page toast, then system. Acknowledge every action. Never color-only.
- Uncontrolled inputs by default. Dates and numbers through `Intl.DateTimeFormat` and `Intl.NumberFormat`.

## Copy voice

- No em dashes in any shipped copy: headlines, body, buttons, alt, meta, errors. `scripts/anti_slop_scan.py` fails HIGH on one. Rewrite with a full stop, comma or colon.
- Ground each headline in one fact that would be false with a competitor's name swapped in. Write three candidates (mechanism, outcome, tension), pick by elimination, run `scripts/check_copy_diversity.py --headline "<text>" --cta "<text>"`.
- Reject these shapes on sight: "The [adj] way to [verb]", "Built for [audience] who [verb]", "[Verb] your [noun] in [time]", "Where X meets Y", "[Adj], [adj] [noun]", "Everything you need to", "[Noun] made [adj]", "Say goodbye to", "Your [noun], reimagined", "One platform for all your".
- Banned filler: elevate, seamless, unleash, blazing fast, next-gen, exquisite, unparalleled, curated (as filler), stacked intensifiers.
- Buttons start with a verb naming the action: "Save draft", "Delete project". Never "OK!", "Let's go!", bare "Yes/No". A confirmation repeats the consequence: "Delete project" / "Cancel". "Get started" and "Learn more" only when nothing specific fits; suffix "Learn more about exports".
- One flow vocabulary: "Continue" or "Next", pick one. Sentence case by default, one policy per element type. Toggles describe the ON state.
- "You", not "the user". No "we" in errors: "Unable to save. Check your connection and try again."
- Numerals for quantities ("8 deployments"). Active voice. Ellipsis `…`, curly quotes, `&nbsp;` in `10&nbsp;MB` and `⌘&nbsp;K`.
- Full templated strings with pluralisation; never `"You have " + n + " messages"`.

## Accessibility basics

- Native first: `<button>` for actions, `<a href>` for navigation, never `<div onClick>`. Cmd/middle-click must work. Remove ARIA before adding it.
- Focus: style `:focus-visible`, never `outline: none` without a verified 2px replacement. `:focus-within` on compound controls. Keep system colors in forced-colors mode.
- Contrast: 4.5:1 text, 3:1 UI and state borders (`01-system.md`). Status never by color alone.
- Keyboard: Escape closes overlays, arrows move inside composites (roving tabindex 0/-1), Tab between widgets, Enter and Space activate. Only `tabindex="0"` or `"-1"`.
- Modals: `inert` on background, focus moves in on open and returns to the trigger on close, `overscroll-behavior: contain`.
- Names: icon-only buttons get `aria-label`; decorative icons `aria-hidden="true"`, never on a focusable element. Alt by purpose: decorative `alt=""`, functional describes the action.
- Announce: `aria-describedby` for field errors, `role="status"` for toasts and counts, `role="alert"` for urgent untied errors only. Stable empty region before the text updates.
- Reduced motion: wrap motion in `@media (prefers-reduced-motion: no-preference)`. Under reduce, crossfade replaces slide and scale; parallax and autoplay die. Autoplay always has a visible pause.
- Structure: one `<h1>`, no skipped levels, one `<main>`, skip link first, `scroll-margin-top` on anchors. Works at 200% zoom and reflows at 320px. Never `user-scalable=no`.
- Touch: `touch-action: manipulation`, deliberate `-webkit-tap-highlight-color`, `autofocus` only on desktop and only one input.
- Theming: `color-scheme` on `<html>`, `<meta name="theme-color">` matches the page, native `<select>` gets explicit `background-color` and `color`.
- URL reflects state: filters, tabs, pagination, expanded panels in query params.

## Library selection

Order: 1) name the task, not the library; 2) read `package.json` and existing imports; 3) reuse the healthy library already there; 4) else pick one default below; 5) hand-roll only when the behaviour is static, simple, or dependencies are forbidden. Never swap a working library because the table names another one.

| Task | Default |
|---|---|
| Dialog, popover, menu, select | Base UI |
| Command palette | cmdk |
| Toasts | Sonner |
| OTP input | input-otp |
| React springs, layout, exit, gesture | Motion (`motion/react`) |
| Hover, press, reveal | CSS transitions, or GSAP for scroll storytelling |
| Changing numbers | NumberFlow |
| Charts | Recharts, or a bklit registry chart on shadcn. Never hand-roll a chart |
| Drag and drop | dnd kit |
| Long lists | Virtuoso |
| Shared client state | Zustand |
| Class names, variants | clsx, cva |
| Theme switch (Next) | next-themes |

Coherence rule when mixing: every pulled component is re-tokened to the lock in the same pass it arrives, keeps one icon family, one motion library (Motion and GSAP together only when a pulled component brought the second), and clears the craft rules above. No installing a library for a button press; no hand-rolled spring, dialog focus trap, or chart. Prefer the cheaper fix: delete, use the platform, reuse a project token, correct the value, then add.

## Write PROMPT.md next to the output

Before handing off, write `PROMPT.md` beside `index.html` (or at the app root) with two sections:

1. **Recreate**: the exact prompt that rebuilds this output. Name the archetype picks, mood, palette seed, type pairing, motion track, and each asset by path.
2. **Remix**: a shorter prompt that keeps layout logic, visual treatment, interaction choreography and responsive behaviour but swaps brand, copy, palette and content.

Same pass: stamp the first line of the shipped CSS with the picks and contrast result, then run `scripts/anti_slop_scan.py`, `scripts/audit_motion.py` on the changed paths and fix HIGH before `06-gate.md`.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/better-ui/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/better-layout/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/better-accessibility/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/better-writing/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/better-interface/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/interface-quality-rules.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/component-patterns.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/component-catalog.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/copy-voice.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/library-selection.md
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/skills/loading-states/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/skills/error-handling-ux/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/skills/form-design/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/skills/feedback-patterns/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/skills/fitts-law/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/DEMOS.md
- /Users/rakeshbhugra/.claude-personal/skills/frontend-app/SKILL.md
