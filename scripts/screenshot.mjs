#!/usr/bin/env node
// Screenshot a page for the gate stage.
// Usage: node scripts/screenshot.mjs <url-or-file> <out-dir> [--full] [--sections]
//   default    desktop-1280x720.png and mobile-390x844.png at the top of the page
//   --full     full-page captures, after walking the page so scroll-triggered reveals fire
//   --sections one viewport shot per <main> section with its top edge at the viewport top:
//              section-<n>-<id>.png. This is what a sticky, pinned, or scrubbed section
//              looks like the moment it enters. Run check_blank_bands.py on these.
// Needs: npm install && npx playwright install chromium
import { chromium } from "playwright";
import { mkdirSync } from "node:fs";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";

const [target, outDir = ".frontend-design/shots", ...flags] = process.argv.slice(2);
if (!target) {
  console.error("usage: screenshot.mjs <url-or-file> <out-dir> [--full] [--sections]");
  process.exit(2);
}
const fullPage = flags.includes("--full");
const sections = flags.includes("--sections");
const url = /^https?:\/\//.test(target) ? target : pathToFileURL(resolve(target)).href;
mkdirSync(outDir, { recursive: true });

const viewports = [
  { name: "desktop", width: 1280, height: 720 },
  { name: "wide", width: 1536, height: 1000 }, // tall desktop windows expose centered-sticky gaps
  { name: "mobile", width: 390, height: 844, isMobile: true, deviceScaleFactor: 2 },
];

const browser = await chromium.launch();
for (const vp of viewports) {
  const ctx = await browser.newContext({
    viewport: { width: vp.width, height: vp.height },
    isMobile: vp.isMobile ?? false,
    deviceScaleFactor: vp.deviceScaleFactor ?? 1,
    // Top and full-page shots settle motion for determinism. Section-entry shots keep
    // motion on, because the entry frame of a sticky or scrubbed section is the defect.
    reducedMotion: sections ? "no-preference" : "reduce",
  });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts?.ready);

  if (sections) {
    const tops = await page.evaluate(() =>
      [...document.querySelectorAll("main > section, main > article")].map((el, i) => ({
        i, id: el.id || `s${i + 1}`, top: Math.round(el.getBoundingClientRect().top + scrollY),
      }))
    );
    for (const s of tops) {
      await page.evaluate((y) => scrollTo(0, y), s.top);
      await page.waitForTimeout(900); // let reveals finish; entry layout is what we want

      const path = `${outDir}/${vp.name}-section-${s.i + 1}-${s.id}.png`;
      await page.screenshot({ path });
      console.log(path);
    }
    await ctx.close();
    continue;
  }

  if (fullPage) {
    // Walk the page so scroll-triggered reveals fire, then return to the top.
    await page.evaluate(async () => {
      const step = Math.max(200, Math.floor(innerHeight * 0.6));
      for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
        scrollTo(0, y);
        await new Promise((r) => setTimeout(r, 60));
      }
      scrollTo(0, 0);
    });
  }
  await page.waitForTimeout(400);
  const path = `${outDir}/${vp.name}-${vp.width}x${vp.height}.png`;
  await page.screenshot({ path, fullPage });
  console.log(path);
  await ctx.close();
}
await browser.close();
