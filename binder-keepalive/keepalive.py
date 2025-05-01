from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

URL = "https://hub.gesis.mybinder.org/user/gabrie50-jupyter-desktop-server-r227cdea/desktop/"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

print("Abrindo o Binder...")
driver.get(URL)

# Mantém ativo com reload a cada 5 minutos
while True:
    print("Binder ativo... recarregando.")
    time.sleep(300)
    driver.refresh()
