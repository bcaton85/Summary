from summarize import summarizeArticle
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import simplejson
import random

class S(BaseHTTPRequestHandler):

    #Set the headers
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    #GET endpoint for testing
    def do_GET(self):
        self._set_headers()
        self.wfile.write("test")

    #POST endpoint recieves article url and passes it to summarize.py for processing
    #Analyzed article is recieved and sent back
    def do_POST(self):
        self._set_headers()
  
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        data = simplejson.loads(self.data_string)

        summary = summarizeArticle(data['url'])

        responseData = {}
        responseData['summary'] = summary
        json_data = simplejson.dumps(responseData)

        self.wfile.write(json_data)
        return

#Run the server
def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting http...'
    httpd.serve_forever()


run()