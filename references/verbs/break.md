# Verb: break

Purpose: render one component in every state it can reach on a throwaway page, look once, report what visibly broke.

Reach for `verbs/audit.md` instead when the question is quality against rules. This verb observes, it does not judge. The variant sub-flow at the end covers "build me three options".

Triggers: "break this", "stress test the card", "show me every state", "map the states".

## 1. Scope one component

One component per run. "The settings page" is not a component; the profile form's text input is. If the request spans several, list candidates and ask which one.

Restate it in one sentence: what it accepts, what it renders, where it lives.

## 2. Pick scenarios from the matrix

Stress only what varies. Read the props, slots, states, and data first. Keep an axis when its cue matches, drop it and say so in one line.

| Axis | Cue | Scenarios |
|---|---|---|
| Interaction states | Component has the state as a prop | idle, disabled, loading, error, success. Hover, focus, active are the user's to try: invite them to tab through instances |
| Data states | Component fetches or receives data | empty (zero items, empty string), populated, error |
| Content length | Renders text it does not author | empty string, one word, typical, several sentences, one unbreakable 60-char string |
| Content shape | Text from users or locales the team does not write | emoji alone and mixed, RTL, mixed-direction, diacritics and tall scripts, numbers in aligned columns |
| Quantity | Repeats over items | 0, 1, realistic count, 10× realistic |
| Container | Always | 320px fixed, squeezed by a flex or grid sibling, very wide |
| Environment | Project supports the mode | dark mode, browser zoom, reduced motion. Not rendered on the page: named in the report for the user to toggle |

Loading gets its own floor. Under 100ms: no indicator. 100ms to 1s: skeleton or opacity. 1s to 10s: clear indicator, progress if measurable. Over 10s: progress, time estimate, background option. Skeleton shapes match real content. Lists stagger in at 30 to 50ms. No layout shift when content lands. Shimmer respects reduced motion.

Write the kept scenarios down before building, one line each.

## 3. Build the harness page

- One scratch route inside the app (`/_break/<component>`), so the component gets the app's layout, fonts, tokens, and globals for free. Static HTML file only when no app can host it.
- Import the real component. Never rebuild a lookalike.
- One column. Short text label above each instance. One instance per scenario.
- Widths are fixed-width containers on the page, side by side with the full-width one. Never resize the viewport.
- Page adds labels, containers, and fixture props. Nothing else: no fonts, no styles, no simulated dark tokens, no probes.
- In Next or any server/client split, the page is `"use client"`. Fixture props vanish across that boundary and every scenario renders empty.
- Harness never imports production state or live data. Production never imports from the harness.

## 4. Look once

One load, one pass, top to bottom. Note what visibly broke in the words of what you saw: "text escapes the field's right edge", never "spacing feels tight".

No browser at hand, or it needs launching or debugging: skip the look, hand over the URL. The user's eyes are the observation.

Then mark every break on the page as a one-line note under that scenario's label, in a single edit. The page must read as the report by itself.

## 5. Report and stop

| Scenario | Observed | Owner |
|---|---|---|
| One unbreakable 60-char string | Overflows the card, no wrap, no truncation | typography |
| Zero items | Blank region, no message | writing |
| 320px container | Buttons escape the box | layout |
| Disabled | Label drops below 3:1 | color |
| Loading | Content pops in and shifts the row 24px | motion |

Owner names the domain whose rules diagnose the fix: layout, typography, color, writing, accessibility, motion. The fix itself follows `06-gate.md`.

"Everything survived" is a complete report. List the scenarios on the page and the URL. Do not pad with preferences. Do not fix unasked. On "fix it": apply the owner's rules, re-render only the failing scenarios to confirm.

## 6. Cleanup

Leave the page up. It is half the report. Delete the route and its fixtures only when the user says they are done.

## Variant sub-flow

Trigger: "give me a few options", "three versions of the hero", uncertain direction on a hero, pricing card, onboarding step, dashboard card, command palette, toast, empty state, or motion-heavy component.

1. Scope one piece. Read the tokens, component library, motion library, density, voice, and where it renders.
2. Pick one axis. Each variant takes a different position on it. Secondary choices follow from that position.

| Axis | What varies |
|---|---|
| Structure | Grouping, order, column count, what collapses |
| Density | Spacing scale, hit areas, how much fits |
| Emphasis | Where filled color goes, what recedes |
| Type | Scale steps, weight contrast, measure |
| Voice | Labels, tone, how much copy |

Three variants by default, five only when asked. Names say the direction (`Quiet`, `Editorial`, `Dense`), never `Option A`. Color swaps are not variants.

3. Floor every variant clears before entering the picker: accessible name on every control, keyboard reaches everything, focus visible, nothing clips at 320px, no meaning on color alone. A direction that only works by breaking the floor is dropped.
4. Host on the real page with real neighbours and real content, the item count the page will carry. Select with `?variant=<name>` so every variant is a link. Render one at a time, full size.
5. Picker: fixed, bottom centre, `bottom: 24px`, `z-index: 2147483647`, dark neutral `rgb(20 20 20 / 0.9)`, system font 13px, pill buttons, no project tokens. Left and right arrows step, number keys jump, active item carries `aria-current="true"`, no transition on switch. Move to top centre if the piece sits at the bottom.
6. Flip through every variant yourself: each renders, each interaction responds, console clean. Then hand over a table: Variant | Axis position | Right when | Costs. State the width you judged at. Never mark a favourite.
7. On a choice: build the winner properly in place, delete the other variants and the harness. On another round: keep the harness, re-pick positions around the direction they leaned toward.

## Before you finish

| Mistake | Fix |
|---|---|
| Every axis run on every component | Keep the axes whose cue matches, name the drops |
| Predicted failure reported as observed | Render it or leave it out |
| Scenario rendered empty | Harness bug, not the component. Make the page client code |
| Harness restyles or re-themes the component | Labels and widths only |
| Screenshot per scenario, browser wrangling | One load, or hand over the URL |
| Break in the table but not on the page | Note it under the label |
| Variants differ only in tint or copy | Move one to a new axis position or cut it |
| Page deleted in the same turn as the report | Delete only on the user's word |

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/break/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/break/scenarios.md
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/variant/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/jakubkrehe-skills/skills/variant/picker.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/commands/map-states.md
- /Users/rakeshbhugra/code/frontend-skills/designer-skills/interaction-design/skills/loading-states/SKILL.md
