from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time
import requests

BINDER_URL = "https://hub.gesis.mybinder.org/user/gabrie50-jupyter-desktop-server-825j7vvg/desktop/"

# Função para manter o Binder ativo
def ping_loop():
    while True:
        try:
            response = requests.get(BINDER_URL)
            print(f"Status: {response.status_code} - Mantendo ativo...")
        except Exception as e:
            print(f"Erro ao acessar: {e}")
        time.sleep(300)  # 5 minutos

# Página web servida pelo Render
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Binder Keepalive</title>
            <style>
                html, body {{
                    margin: 0;
                    height: 100%;
                    overflow: hidden;
                }}
                iframe {{
                    border: none;
                    width: 100%;
                    height: 100%;
                }}
            </style>
        </head>
        <body>
            <iframe src="{BINDER_URL}" allowfullscreen></iframe>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    threading.Thread(target=ping_loop, daemon=True).start()
    server = HTTPServer(("0.0.0.0", 10000), Handler)
    print("Servidor iniciado na porta 10000.")
    server.serve_forever()
        
