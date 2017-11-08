from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import simplejson as json

hostName = "0.0.0.0"
hostPort = 8000

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
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        data = json.loads(self.data_string)
        print ("Recieved: {} at {}".format(data, time.asctime()))
        self.wfile.write(bytes(json.dumps("{}".format(data)), "utf-8"))
        return

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
