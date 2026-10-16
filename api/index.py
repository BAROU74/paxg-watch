from http.server import BaseHTTPRequestHandler
import requests, json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=10).json()
            prix = float(r['price'])
            msg = f"🚨 GOLD {prix}$ touche 4150$ - LONG!" if prix <= 4150 else f"GOLD {prix}$ - j'attends 4150$"
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"prix": prix, "message": msg}).encode())
        except Exception as e:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({"erreur": str(e)}).encode())
