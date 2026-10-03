# Product Proof SaaS

SaaS or AI product page where a real, deterministic workflow in the hero is the proof. The interface is the evidence, not decoration.

Reach for `landing-page.md` instead when a screenshot explains the product and there is no state machine to show. Reach for `operational-enterprise.md` when the buyer needs permissions, audit, and rollback before the pitch.

## Section order

1. Header: compact product routes, one obvious trial or demo action.
2. Hero: friction-led headline left, dense product stage right. Stage shows editable input, sample output, selected direction, version, progress, and a `Sample · not published` label.
3. Friction proof: before/after, time breakdown, or a concrete workflow constraint.
4. Feature modules: small icon, focused copy, each tied to the central workflow.
5. Workflow: input, processing, draft, edit, approval, publish as explicit states. Human control, not one-click magic.
6. Audience tabs: content stays in the DOM, deep-linkable.
7. Proof: verified customer evidence or clearly labeled samples.
8. Pricing: aligned limits, usage units, footnotes.
9. FAQ: ambiguous plan terms deep-link here from the comparison table.
10. Footer: trust, docs, legal on a pale-blue fade.

## Numbers

| Number | Default | Failure prevented |
|---|---|---|
| Grid columns | 12 | Product panels that drift off the marketing grid |
| Radius | 12-16px | Pill-soft cards that read as consumer app |
| Signal colors | 1 cool hue, active/progress/selection/focus only | Accent sprayed on everything |
| Primary action color | Black | Signal color losing its meaning |
| Workflow states | 6 | Mockup that cannot explain its own transitions |
| Control feedback | 160-220ms | Laggy or instant-jump controls |
| Interface state change | 420-700ms | Handoffs too fast to read |
| Card stagger | 45-70ms | Reveal that feels like a slideshow |
| Handoffs animated at once | 1 | Competing motion |
| Hero proof visuals | 1 | Second mockup fighting the stage |

## Signature moves

- Product panel denser than the marketing copy around it.
- High-x-height grotesk paired with compact mono labels.
- Surfaces run white to pale blue with soft gray grid lines and thin borders.
- Run action visibly moves through processing and ready without pretending to call a model. Deterministic replay plus a text transcript.
- Browser Back restores the prior comparison view; pricing terms deep-link to FAQ answers.

## Do not

- Fake typing speed, generation speed, or output quality.
- Ship unlabeled sample output or invented customers, metrics, security claims.
- Build a feature grid unrelated to the central workflow.
- Add AI particles, glowing orbs, floating glass cards, or perpetual motion.
- Hide pricing limits or disconnect FAQ from the table.

## Effects it may use

- `container-lines` for the soft grid behind the product stage.
- `atmosphere-background` for slow cloud drift, optional, paused offscreen.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/product-proof-saas/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/product-proof-saas/demo/PROMPT.md
