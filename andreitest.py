from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 # Maybe set this to 1234

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
			
			
 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
