from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer, urlparse, subprocess, os
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
from os import curdir, sep

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
	self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_POST(self):
        self._set_headers()
	if "string" in self.path:
        	string = self.rfile.read(int(self.headers['Content-Length']))
		print(" The data is  %s" % string)
                output = subprocess.check_output("sh ./voice.sh '%s'" %string, shell=True)
		self.wfile.write("%s " %output)
		print output
	elif "LoadBalancer_Healthcheck" in self.path:
		self.wfile.write("Im working properly bro!!")
	elif "favicon.ico" in self.path:
		f = open('./' + self.path, 'rb')
		self.send_response(200)
        	self.send_header('Content-type', 'image/x-icon')
		self.end_headers()
                self.wfile.write(f.read())
                f.close()
		
	else:
		self.wfile.write("None of my business")
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        if "home" in self.path:
                f = open(curdir + sep + 'home.html', 'rb')
                self.wfile.write(f.read())
                f.close()
                return
        elif "css" in self.path:
                f = open(curdir + self.path, 'rb')
                self.wfile.write(f.read())
                f.close()
                return
        elif "bower_components" in self.path:
                f = open(curdir + self.path, 'rb')
                self.wfile.write(f.read())
                f.close()
                return
        elif "img" in self.path:
                f = open(curdir + self.path, 'rb')
                self.wfile.write(f.read())
                f.close()
                return
        else:
            self.wfile.write("File not found")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd... at => ', port
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
	print 'Starting the server'
        run()
