// Converte um HTML local em PDF A4 com o Chromium do Playwright.
// Uso: node pdf.js entrada.html saida.pdf "Título do rodapé"
const path = require("path");
const { chromium } = require("playwright");

(async () => {
  const [src, out, title] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto("file://" + path.resolve(src), { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  const esc = (s) => (s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;");
  await page.pdf({
    path: out,
    format: "A4",
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: "<div></div>",
    footerTemplate:
      '<div style="width:100%;font-family:Inter,DejaVu Sans,sans-serif;font-size:7.5px;color:#8a8f98;' +
      'padding:0 14mm;display:flex;justify-content:space-between">' +
      `<span>LIMAC · ${esc(title)}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    margin: { top: "13mm", bottom: "15mm", left: "14mm", right: "14mm" },
  });
  await browser.close();
})();
