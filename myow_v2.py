
from http.server import HTTPServer, BaseHTTPRequestHandler
import random
import logging

logging.basicConfig(level=logging.INFO)

cats = [
    " /\_/\\\\\n( o.o )\n > ^ <",
    " /ᐠ｡ꞈ｡ᐟ\\\\",
    " (=^･ω･^=)"
]

messages = [
    "Hello from Meow World!",
    "Everything is purr-fect!",
    "Docker says MEOW!",
    "Have a pawsome day!"
]

class CatApp(BaseHTTPRequestHandler):
    def do_GET(self):
        cat = random.choice(cats)
        message = random.choice(messages)

        html = f"""
        <html>
        <head>
            <title>Meow World</title>
            <style>
                body {{
                    background: #ffe4ec;
                    text-align: center;
                    font-family: Arial;
                    padding: 60px;
                }}
                h1 {{ color: #d65a8a; }}
                pre {{ font-size: 35px; }}
            </style>
        </head>
        <body>
            <h1>🐱 Meow World!</h1>
            <pre>{cat}</pre>
            <h2>{message}</h2>
            <p>Docker app is working! ✅</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())

        logging.info("🐾 Cat page visited: %s", message)

server = HTTPServer(("0.0.0.0", 8080), CatApp)

logging.info("🐱 Meow World started!")
logging.info("Listening on port 8080")

server.serve_forever()
