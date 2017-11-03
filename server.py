from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import simplejson

hostName = "localhost"
hostPort = 9000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Gym-Chat-Bot</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><form method=\"post\"><input type=\"submit\"> </form>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.wfile.write(bytes("{'Cake': '5'}", "utf-8"))

        data = simplejson.loads(self.data_string)
        print ("{}".format(data))
        self.wfile.write(bytes("{'wow': 'okay'}", "utf-8"))
        return

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
