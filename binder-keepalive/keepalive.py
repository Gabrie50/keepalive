import time
import requests
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

URL = "hub.gesis.mybinder.org/user/gabrie50-jupyter-desktop-server-825j7vvg/desktop/"

def ping_loop():
    while True:
        try:
            response = requests.get(URL)
            print(f"Status: {response.status_code} - Mantendo ativo...")
        except Exception as e:
            print(f"Erro ao acessar: {e}")
        time.sleep(300)  # espera 5 minutos

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Servico rodando.')

if __name__ == "__main__":
    # Inicia o loop de requisições em background
    threading.Thread(target=ping_loop, daemon=True).start()

    # Inicia um servidor HTTP fictício para manter a porta aberta
    server = HTTPServer(("0.0.0.0", 10000), DummyHandler)
    print("Servidor iniciado na porta 10000.")
    server.serve_forever()
    
