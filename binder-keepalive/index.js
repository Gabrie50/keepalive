const puppeteer = require('puppeteer');

const BINDER_URL = "https://hub.gesis.mybinder.org/user/gabrie50-jupyter-desktop-server-mvlfebx3/desktop/";

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox'
    ]
  });

  const page = await browser.newPage();
  await page.goto(BINDER_URL, { waitUntil: 'networkidle2' });

  console.log("Binder link aberto com sucesso. Mantendo ativo...");

  // Mantém o navegador rodando
  setInterval(async () => {
    console.log("Pingando Binder...");
    await page.reload({ waitUntil: 'networkidle2' });
  }, 5 * 60 * 1000); // a cada 5 minutos
})();
