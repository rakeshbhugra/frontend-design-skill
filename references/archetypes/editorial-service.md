# Editorial Service

Appointment-based service site (salon, barber, spa, clinic, wellness, hospitality) that reads like a quiet lookbook, then carries that confidence into a resilient booking flow.

Reach for `awwwards-cinematic.md` instead when the brand is the pitch and nothing is booked. Reach for `landing-page.md` when it is one offer, one CTA, no schedule.

## Section order

1. Header: essential routes, current location, one booking action. Uppercase nav, sparse.
2. Hero: split between a large serif statement and one cropped documentary portrait or place image.
3. Confidence line: one slow text loop, only when it carries real positioning.
4. About: two or three layered photographs with captions and a clear reading order.
5. Treatments: tab list plus a reserved media stage showing name, description, duration, price, booking link.
6. Favorites (dark chapter): verified popular services or results.
7. Locations: address, hours, accessibility, contact, availability, before booking starts.
8. Booking: selected service, professional, location, and time stay visible through confirmation.
9. Footer: operational information ahead of marketing filler.

## Numbers

| Number | Default | Failure prevented |
|---|---|---|
| Treatment options in selector | 3 | Dense price table before desire exists |
| About photographs | 2-3 | Gallery dump |
| Accent colors | 1 muted, selection and status only | Beauty-template ornament |
| Radius | Minimal, hairline rules | Glossy card look |
| Control feedback | 160-220ms | Sluggish tabs |
| Section entrance | 500-760ms | Frantic reveals |
| Confidence loop cycle | Slower than 14s, paused offscreen | Marquee that reads as noise |
| Layered photo reveals | 1 | Motion on every image |
| Layout shift on treatment change | 0, stage height reserved | Jumping page |

## Signature moves

- Warm ivory paper with near-black chapters; black for decisive actions.
- High-contrast serif display paired with compact sans labels.
- Treatment selector is a real `tablist`: arrow keys, Enter, Space, polite announcement, expanded static list under reduced motion.
- Booking never claims a slot before server confirmation. Selections survive Back, errors, and retry; focus returns to the failing field.
- Trust from environment, process, and practitioner evidence, not badges.

## Do not

- Hover-only treatment previews. Touch must not depend on hover.
- Fake availability, reviews, results, or credentials.
- Auto-advancing carousels, glass, cosmetic gradients.
- Dense pricing before context.
- Lose booking state after an error or navigation.

## Effects it may use

- `masked-reveal` for the layered photo reveal.
- `marquee-loop` for the confidence line.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/editorial-service-booking/SKILL.md
- /Users/rakeshbhugra/code/frontend-skills/mengto-frontend-skills/agent-skills/web-design/editorial-service-booking/demo/PROMPT.md
