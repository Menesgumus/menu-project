import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Sunucu başlatıldı - http://localhost:{PORT}")
    print("Sunucuyu durdurmak için CTRL+C tuşlarına basın")
    httpd.serve_forever() 