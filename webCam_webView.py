import cv2
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from io import StringIO
import PIL
from PIL import Image
hostName = 'localhost'
hostPort = 5000
#run camera
cap = cv2.VideoCapture(0)
def updateCamFeed():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
    while True:
         ret, frame = cap.read()
class MyServer(BaseHTTPRequestHandler):
     def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>WebCam Display</title>  </head>", "utf-8"))
        self.wfile.write(bytes("<body><p><a href=\"output.avi\">Image</a>     </p>", "utf-8"))
        self.wfile.write(bytes("<p>It Worked!!!!! %s</p>" % self.path,     "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
def main():
# initialize server
    myServer = HTTPServer((hostName, hostPort), MyServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
    myServer.serve_forever()
    updateCamFeed()
if __name__ == '__main__':
    main()
