from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import simplejson as json
from sentenceParsing import *
from Replying import *

# Accept all connections on port 8000
#
hostName = "0.0.0.0"
hostPort = 8000

class MyServer(BaseHTTPRequestHandler):
    
    exercisesToDict()

    # Method is called when GET request is made
    def do_GET(self):
        # Deny GET method and return 401 unauthorised
        self.send_response(401)

    # Method is called when POST request is made
    def do_POST(self):
        # Tell client connection is accepted and
        # Allow connections over different ports
        #
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
<<<<<<< HEAD
=======
        # Read the input from client as a string
        # 
>>>>>>> 83ac258d85b5c1117ab7435865ce4f201dcdedcd
        self.data_string = self.rfile.read(int(self.headers["Content-Length"]))

        # Turns the JSON string into a dictionary
        data = json.loads(self.data_string)
<<<<<<< HEAD
        JSONstr = str(data).replace("'", '"').replace('\\"', "'").replace("\\'", "'").replace(': None', ': ""')
        print ("Recieved: {} at {}".format(data, time.asctime()))
=======

        print ("Recieved: {} at {}".format(data, time.asctime()))
        # Take keywords from message recieved and
        # put them into a dict keyWords
        identifyOutput(data["message"])
        #print(exercise_Muscle)
        data["message"] = handleReply(returnOutput())
        #print(data["message"])

        # Format dictionary into acceptable JSON
        # format
        JSONstr = str(data).replace("'", '"').replace('\\"', "'").replace("\\'", "'").replace(': None', ': ""')
        # Send the file back to the client in bytes
        # in utf-8
>>>>>>> 83ac258d85b5c1117ab7435865ce4f201dcdedcd
        self.wfile.write(bytes(json.dumps(JSONstr), "utf-8"))
        return

# initialise server
myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
