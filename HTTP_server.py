#HTTPselferver template

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1' #locathost - http://127.0.0.1
PORT_NUMBER = 1234 # Maybeselfet this to 1234 /selfo, complete address would be: http://127.0.0.1:1234
# Webselfervers example: http://www.ntnu.edu:80

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
	def do_HEAD(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
	def do_GET(self):
		"""Respond to a GET request."""
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		
		# Check what is the path
		path =self.path
		if path.find("/") != -1 and len(path) == 1:
			self.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			self.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			self.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/info") != -1:
			self.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			self.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			self.wfile.write(bytes("<body><p>Let's order a chair</p>", "utf-8"))
			self.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/setLength") != -1:
			self.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
			self.wfile.write(bytes('<form action="/setLength" method="post">', 'utf-8'))
			self.wfile.write(bytes('<label for="clength">Set Length:</label><br>', 'utf-8'))
			self.wfile.write(bytes('<input type="text" id="clength" name="clength" value="100"><br><br>', 'utf-8'))
			self.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			self.wfile.write(bytes('</form></body></html>', 'utf-8'))
		else:
			self.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			self.wfile.write(bytes("<body><p>The path: " + path + "</p>", "utf-8"))
			self.wfile.write(bytes('</body></html>', "utf-8"))
			
			
	def do_POST(self):

		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		
		# Check what is the path
		path =self.path
		print("Path: ", path)
		if path.find("/setLength") != -1:
			content_len = int(self.headers.get('Content-Length'))
			post_body =self.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			
			self.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
			self.wfile.write(bytes('<form action="/setLength" method="post">', 'utf-8'))
			self.wfile.write(bytes('<label for="clength">Set Length:</label><br>', 'utf-8'))
			self.wfile.write(bytes('<input type="text" id="clength" name="clength" value="100"><br><br>', 'utf-8'))
			self.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			
			self.wfile.write(bytes('<p>' + param_line + '</p>', 'utf-8'))
			
			self.wfile.write(bytes('</form></body></html>', 'utf-8'))
			
			
 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()