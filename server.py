from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import simplejson as json
from sentenceParsing import *

hostName = "0.0.0.0"
hostPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(401)

    def do_POST(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.data_string = self.rfile.read(int(self.headers["Content-Length"]))

        data = json.loads(self.data_string)
        print ("Recieved: {} at {}".format(data, time.asctime()))
        identifyOutput(data["message"])
        data["message"] = getKeyWord("Strength") + getKeyWord("Cardio") 
        JSONstr = str(data).replace("'", '"').replace('\\"', "'").replace("\\'", "'").replace(': None', ': ""')
        self.wfile.write(bytes(json.dumps(JSONstr), "utf-8"))
        return

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
