# Kestrel, AI-native software studio

## Recreate this build

Use $frontend-design. Build a single index.html marketing page for Kestrel, a fictional software studio where senior engineers paired with AI agents ship production software in five-day build weeks.

- Dark only, cinematic. Palette: bg #151a1e, surface #1f272c, border #2c363c, text #e6ebea, muted #9aa5a3, primary and accent #b7cf8f (lichen) with on-primary #151a1e. Verify with `check_contrast.py --matrix`.
- Type: Bricolage Grotesque 700/800 at opsz 96 for display (-0.035em, line-height 0.92), Hanken Grotesk 400/500/600 body, Azeret Mono for 12px uppercase labels at 0.12em.
- Logo: the wordmark "Kestrel" in Bricolage Grotesque 800 with a small mono "STUDIO" suffix. No glyph.
- Macrostructure Poster Fold, archetype awwwards-cinematic. Arc: a full-bleed photo fold (a kestrel banking over dark highland terrain at dusk, headline bottom-left "Software shipped in days, not quarters." with "days," in lichen, lede and two pill buttons bottom-right, a gradient scrim to the page background), a 200vh sticky manifesto with a scroll-scrubbed word reveal aligned to the top of its runway (hidden opacity 0.18, blur 6px, rise 0.14em, 128px top padding), a "system" section with three numbered surface cards beside a sticky terrain photo, a five-day build-week row (Friday outlined in lichen), four contract terms with a Lucide check, a second photo fold (the kestrel perched on lichen rock, positioned 92% right) carrying the closing statement and CTA, single-row footer.
- Imagery: three Gemini photographs of one kestrel. Hero prompt: "Cinematic aerial photograph looking almost straight down at a common kestrel, wings fully spread and banking, filling the center-right third, over dark highland terrain of moss, lichen, and wet rock, dusk light, muted dark greens and charcoal slate tones, subtle film grain, no text, no watermark, no logo, no people". Derive the terrain-only detail and the perched close-up with `edit_image.py -i hero.png`.
- Motion: GSAP 3.12.5 + ScrollTrigger + gsap-starter.js reveals (0.22s, 16px, power3.out, stagger 0.06). Hero in four beats: photo settles 1.06 to 1 over 1.4s, masked headline lines (yPercent 110, 0.85s, stagger 0.1), nav, lede and actions. Full prefers-reduced-motion branch. No marquee, no parallax, no second effect.
- Sections: 128px top, 96px bottom. No sticky block centered in 100vh. No invented metrics, logos, or testimonials. No em-dashes. Every image has width, height, and an alt decision.

## Remix

Same skeleton for a different studio: pick one animal or object as the subject and photograph it over one real environment from one prompt, swap lichen for another muted natural accent that stays text-safe on the dark ground, rewrite the three principle headings and five day outputs, and keep the manifesto passage under 30 words with one accent phrase at the end.
