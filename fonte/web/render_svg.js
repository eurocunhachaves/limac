// Renderiza SVGs em PNG (fundo branco) com o Chromium do Playwright.
// Uso: node render_svg.js jobs.json   onde jobs.json = {css, jobs: [{svg, png, scale}]}
const fs = require("fs");
const { chromium } = require("playwright");

(async () => {
  const { css, jobs } = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ deviceScaleFactor: jobs[0] ? jobs[0].scale : 2 });
  const page = await ctx.newPage();
  for (const j of jobs) {
    await page.setContent(
      `<html><head><style>${css} body{margin:0;background:#fff} svg{display:block}</style></head><body>${j.svg}</body></html>`
    );
    await page.evaluate(() => document.fonts.ready);
    const el = await page.$("svg");
    await el.screenshot({ path: j.png });
  }
  await browser.close();
})();
