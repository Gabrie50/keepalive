from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time

URL = "https://hub.gesis.mybinder.org/user/gabrie50-jupyter-desktop-server-jt7jvpj0/desktop/"

chromedriver_autoinstaller.install()

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

print("Abrindo o Binder...")
driver.get(URL)

while True:
    print("Binder ativo... recarregando.")
    time.sleep(300)
    driver.refresh()
    
