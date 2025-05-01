import time
import requests

URL = "hub.gesis.mybinder.org/user/gabrie50-jupyter-desktop-server-d9m79il6/desktop/"

while True:
    try:
        response = requests.get(URL)
        print(f"Status: {response.status_code} - Mantendo ativo...")
    except Exception as e:
        print(f"Erro ao acessar: {e}")
    time.sleep(300)  # espera 5 minutos
