import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 # Maybe set this to 1234
dfaPath = "C:\\<YOUR PATH HERE>\\DFAs\\"

f = open(dfaPath + "templates\\chair.dfa", "r")
fileContent = f.read()
f.close()

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	def do_GET(s):
		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		if path.find("/") != -1 and len(path) == 1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/info") != -1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes("<body><p>Let's order a chair</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/setLength") != -1:
			s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/setLength" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="clength">Set Length:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="clength" name="clength" value="100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
		elif path.find("/orderChair") != -1:
			s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8'))
			
			s.wfile.write(bytes('<label for="cside">Set Side of the chair (outer):</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="cside" name="cside" value="1500"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="cdepth">Set Depth for the seat:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="cdepth" name="cdepth" value="1100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="cheight">Set Height for the seat:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="cheight" name="cheight" value="1100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="cwidth">Set Width of the seat:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="cwidth" name="cwidth" value="1100"><br><br>', 'utf-8'))
			
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
		else:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>The path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
			
			
	def do_POST(s):

		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		print("Path: ", path)
		if path.find("/setLength") != -1:
					
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			
			#Get the param value
			pair = param_line.split("=")
			
			s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/setLength" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="clength">Set Length:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="clength" name="clength" value="' + pair[1] +'"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			
			s.wfile.write(bytes('<p>The value of the length was set to ' + pair[1] + '</p>', 'utf-8'))
			
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
		elif path.find("/orderChair") != -1:
			global fileContent
			
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			
			#Get the param value
			pairs = param_line.split("&")
			sidePair = pairs[0].split("=")
			depthPair = pairs[1].split("=")
			heightPair = pairs[2].split("=")
			widthPair = pairs[3].split("=")
			
			#Check if the parameters are in the range - manufacturability check
			# Integrating http Post method
			url = 'http://127.0.0.1:4321/orderChair'
			x = requests.post(url, data = 'a=1111&b=1234&c=1500&d=1600')
			
			# Gettin and processing a reply
			replyByChecker = x.text
			
			if replyByChecker.find("NOK") != -1:
				#TODO - Tell customer not ok.
			else:
				#TODO - Normal reply.
			
			# Giving corresponding message to the customer.
			
			
			s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8'))
			
			s.wfile.write(bytes('<p>The following parameters have arrived: ' + str(sidePair[1]) + ', ' + str(depthPair[1]) + ', ' + str(heightPair[1]) + ', ' + str(widthPair[1]) + '</p>', 'utf-8'))
			
			s.wfile.write(bytes('<label for="cside">Set Side of the chair (outer):</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="cside" name="cside" value="' + str(sidePair[1]) + '"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="cdepth">Set Depth for the seat:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="cdepth" name="cdepth" value="' + str(depthPair[1]) + '"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="cheight">Set Height for the seat:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="cheight" name="cheight" value="' + str(heightPair[1]) + '"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="cwidth">Set Width of the seat:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="cwidth" name="cwidth" value="' + str(widthPair[1]) + '"><br><br>', 'utf-8'))
			
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
			
			#Updating / wiring DFA file
			#Set in parameters.
			fileContentOut = fileContent.replace("<PARAM_SIDE>", str(sidePair[1]))
			fileContentOut = fileContentOut.replace("<PARAM_DEPTH>", str(depthPair[1]))
			fileContentOut = fileContentOut.replace("<PARAM_WIDTH>", str(heightPair[1]))
			fileContentOut = fileContentOut.replace("<PARAM_HEIGHT>", str(widthPair[1]))


			#Let's write the file
			f = open(dfaPath + "My_Chair_210201.dfa", "w")
			f.write(fileContentOut)
			f.close()
			
 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
