from http.server import BaseHTTPRequestHandler, HTTPServer

# Manufacturability Checker Server, checking in the parameters set by the customer is within the contraints set by the process engeneer

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 4321 # Maybe set this to 1234
"""
sidePairUp = 2000
sidePairLow = 0 #500
depthPairUp = 2000
depthPairLow = 0
heightPairUp = 2000
heightPairLow = 0
widthPairUp = 2000
widthPairLow = 0
apronPairUp = 2000
apronPairLow = 0
"""
legLengthMax = 2000
legLengthMin = 0
legWidthMax = 1000
legWidthMin = 0
backMax = 2000
backMin = 0
seatDepthMax = 2000
seatDepthMin = 0
seatWidthMax = 2000
seatWidtMin = 0
apronMax = 1000
apronMin = 0


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
		if path.find("/setParamsIntervals") != -1:
			s.wfile.write(bytes('<html><body><h2>Valid parameter intervals (mm): </h2><form action="http://127.0.0.1:4321/setParamsIntervals" method="post">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum leg length:<br><input type="text" name="legLengthMax" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum leg length:<br><input type="text" name="legLengthMin" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum leg width:<br><input type="text" name="legWidthMax" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum leg width:<br><input type="text" name="legWidthMin" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum backplate length:<br><input type="text" name="backMax" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum backplate length:<br><input type="text" name="backMin" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum seat depth:<br><input type="text" name="seatDepthMax" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum seat depth:<br><input type="text" name="seatDepthMin" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum seat width:<br><input type="text" name="seatWidthMax" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum seat width:<br><input type="text" name="seatWidthMin" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum apron heigth:<br><input type="text" name="apronMax" value="0">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum apron height:<br><input type="text" name="apronMin" value="0">', "utf-8"))

			s.wfile.write(bytes('<br><br><input type="submit" value="Submit"></form><p>Click "Submit" to send.</p></body></html>', "utf-8"))
		else:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>The path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))



	def do_POST(s):
		global sidePairUp, sidePairLow, depthPairUp, depthPairLow, heightPairUp,  heightPairLow, widthPairUp, widthPairLow, apronPairUp, apronPairLow

		
		# Check what is the path
		path = s.path
		print("Path: ", path)
		if path.find("/setParamsIntervals") != -1:
			#TODO - set intervals for params
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			"""
			#Get the param value
			pairs = param_line.split("&")
			legLengthPair = pairs[0].split("=")
			depthPair = pairs[1].split("=")
			heightPair = pairs[2].split("=")
			widthPair = pairs[3].split("=")
			print(pairs)
			"""
			pairs = param_line.split("&")
			legLengthMax = pairs[0].split("=")[1]
			legLengthMin = pairs[1].split("=")[1]
			legWidthMax = pairs[2].split("=")[1]
			legWidthMin = pairs[3].split("=")[1]
			backMax = pairs[4].split("=")[1]
			backMin = pairs[5].split("=")[1]
			seatDepthMax = pairs[6].split("=")[1]
			seatDepthMin = pairs[7].split("=")[1]
			seatWidthMax = pairs[4].split("=")[1]
			seatWidtMin = pairs[5].split("=")[1]
			apronMax = pairs[6].split("=")[1]
			apronMin = pairs[7].split("=")[1]
			print(pairs)
			print(legLengthMax)

			s.send_response(200)
			s.send_header("Content-type", "text/html")
			s.end_headers()

			s.wfile.write(bytes('<html><body><h2>Valid parameter intervals (mm): </h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="http://127.0.0.1:4321/setParamsIntervals" method="post">', "utf-8"))
			
			s.wfile.write(bytes('<p>The following parameters intervals have arrived. Leg length: ' + str(legLengthMax) + '-' + str(legLengthMin) + 
				', leg width: '+ str(legWidthMax) + '-' + str(legWidthMin)  + ', backplate length: '+ str(backMax) + '-' + str(backMin)
				+ ', seat depth: '+ str(seatDepthMax) + '-' + str(seatDepthMin)  + ', seat width: '+ str(seatWidthMax) + '-' + str(seatWidtMin) 
				+ ', apron height: '+ str(apronMax) + '-' + str(apronMin) + '</p>', 'utf-8'))
			s.wfile.write(bytes('<br>Maximum leg length:<br><input type="text" name="legLengthMax" value="' + str(legLengthMax) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum leg length:<br><input type="text" name="legLengthMin" value="' + str(legLengthMin) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum leg width:<br><input type="text" name="legWidthMax" value="' + str(legWidthMax) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum leg width:<br><input type="text" name="legWidthMin" value="' + str(legWidthMin) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum backplate length:<br><input type="text" name="backMax" value="' + str(backMax) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum backplate length:<br><input type="text" name="backMin" value="' + str(backMin) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum seat depth:<br><input type="text" name="seatDepthMax" value="' + str(seatDepthMax) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum seat depth:<br><input type="text" name="seatDepthMin" value="' + str(seatDepthMin) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum seat width:<br><input type="text" name="seatWidthMax" value="' + str(seatWidthMax) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum seat width:<br><input type="text" name="seatWidthMin" value="' + str(seatDepthMin) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Maximum apron heigth:<br><input type="text" name="apronMax" value="' + str(apronMax) + '">', "utf-8"))
			s.wfile.write(bytes('<br>Minimum apron height:<br><input type="text" name="apronMin" value="' + str(apronMin) + '">', "utf-8"))

			s.wfile.write(bytes('<br><br><input type="submit" value="Submit"></form><p>Click "Submit" to set new parameters.</p></body></html>', "utf-8"))
			
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
			
			
			s.send_response(200)
			s.send_header("Content-type", "text/html")
			s.end_headers()
			
			flagOK = False 
			if (int(sidePair[1]) < sidePairUp) and (int(sidePair[1]) > sidePairLow):
				if (int(depthPair[1]) < depthPairUp) and (int(depthPair[1]) > depthPairLow):
					if (int(heightPair[1]) < heightPairUp) and (int(heightPair[1]) > heightPairLow):
						if (int(widthPair[1]) < widthPairUp) and (int(widthPair[1]) > widthPairLow):
							s.wfile.write(bytes('OK', 'utf-8'))
							print("Params OK")
							flagOK = True
			if not flagOK:		
				s.wfile.write(bytes('NOK', 'utf-8'))
				print("Params Not OK")
			
			
			
 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
