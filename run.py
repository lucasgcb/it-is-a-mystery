import http.server
import socketserver
import os


PORT = int(os.environ["PORT"])
print(PORT)
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
