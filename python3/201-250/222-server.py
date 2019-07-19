#creating a simple web server that
#serves the contents of the directory
# and display files

import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(
    ('', 5000), handler) as httpd:
    #ip / port
    httpd.serve_forever()
