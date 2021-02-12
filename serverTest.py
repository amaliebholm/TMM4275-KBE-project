from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 1234
dfaPath = "C:\\<YOUR PATH HERE>\\"

f = open(dfaPath + "templates\\My_Chair_template.dfa", "r")
fileContent = f.read()
f.close()

