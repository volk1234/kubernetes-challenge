from http.server import BaseHTTPRequestHandler, HTTPServer 
 
class SimpleServer(BaseHTTPRequestHandler): 
   """HTTP request handler with GET method.""" 
 
   def do_GET(self):
       """Handle GET request.""" 
       self.send_response(200) 
       self.send_header('Content-Type', 'text/plain') 
       self.end_headers() 
       message = 'Kubernetes challenge' 
       self.wfile.write(bytes(message, 'utf-8')) 
 
def run_server(hostname: str, port: int): 
   """Run the HTTP server.""" 
   server = HTTPServer((hostname, port), SimpleServer) 
   print(f"HTTP server started at: http://{hostname}:{port}") 
 
   try: 
       server.serve_forever() 
   except KeyboardInterrupt: 
       pass 
   finally: 
       server.server_close() 
       print("HTTP server stopped") 
 
if __name__ == "__main__": 
   HOSTNAME = "0.0.0.0" 
   PORT = 8080 
   run_server(HOSTNAME, PORT)
