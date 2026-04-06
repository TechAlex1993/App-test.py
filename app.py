from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Hello, World!</h1></body></html>')
    
    def log_message(self, format, *args):
        # Optional: suppress default logging for cleaner output
        print(f"{self.address_string()} - {format % args}")

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, HelloWorldHandler)
    print(f"Server running on port {port}")
    print(f"Visit http://localhost:{port} to see 'Hello, World!'")
    httpd.serve_forever()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run_server(port)
    