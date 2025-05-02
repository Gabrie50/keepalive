import time
import requests

# URL do seu Binder (coloque a URL correta que abre o Jupyter Desktop)
URL = "https://hub.gesis.mybinder.org/user/gabrie50-jupyter-desktop-server-825j7vvg/desktop/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

while True:
    try:
        response = requests.get(URL, headers=headers)
        print(f"[{time.ctime()}] Status: {response.status_code} - Mantendo ativo...")
    except Exception as e:
        print(f"[{time.ctime()}] Erro ao acessar: {e}")
    time.sleep(300)  # espera 5 minutos
