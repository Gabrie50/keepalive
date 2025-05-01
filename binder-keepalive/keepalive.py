import time
import undetected_chromedriver as uc

URL = "https://hub.gesis.mybinder.org/user/gabrie50-jupyter-desktop-server-jt7jvpj0/desktop/"

options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-fullscreen")

driver = uc.Chrome(options=options)

print("Abrindo o Binder em tela cheia...")
driver.get(URL)

while True:
    print("Mantendo o Binder ativo...")
    time.sleep(300)  # 5 minutos
    driver.refresh()
    
