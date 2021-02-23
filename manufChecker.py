from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 4321 #Manufactor server http://127.0.0.1:4321

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
        if path.find("/setParamsIntervals") != -1:#Form to set the manufactor constraints
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

        
        # Check what is the path
        path = s.path
        print("Path: ", path)
        if path.find("/setParamsIntervals") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)

            pairs = param_line.split("&")
            legLengthMax = pairs[0].split("=")[1]
            legLengthMin = pairs[1].split("=")[1]
            legWidthMax = pairs[2].split("=")[1]
            legWidthMin = pairs[3].split("=")[1]
            backMax = pairs[4].split("=")[1]
            backMin = pairs[5].split("=")[1]
            seatDepthMax = pairs[6].split("=")[1]
            seatDepthMin = pairs[7].split("=")[1]
            seatWidthMax = pairs[8].split("=")[1]
            seatWidthMin = pairs[9].split("=")[1]
            apronMax = pairs[10].split("=")[1]
            apronMin = pairs[11].split("=")[1] #Sets all the variables from the form, using split to get all values from the string
            print(pairs)
            print(legLengthMax)

            # Replaising old constrains with the new 
            manuf_constraints = ["legLengthMax","legLengthMin", "legWidthMax", "legWidthMin",
                "backMax", "backMin", "seatDepthMax", "seatDepthMin",
                "seatWidthMax", "seatWidthMin", "apronMax", "apronMin"] #Name of all manufactor caonstraints

            new_constaints = [legLengthMax, legLengthMin, legWidthMax, legWidthMin,
                backMax, backMin, seatDepthMax, seatDepthMin,
                seatWidthMax, seatWidthMin, apronMax, apronMin] #Value of all the new constraints

            URL = "http://127.0.0.1:3030/kbe/update"

            for i in range(11):
                 # Inserting to the right Class in the Class Hierarchy: Apron, Backplate, Leg or Seat
                if -1 < i < 4:
                    ch = "Leg"
                elif 3 < i < 6:
                    ch = "Backplate"
                elif 5 < i < 10:
                    ch = "Seat"
                elif 9 < i < 11:
                    ch = "Apron"

                # Deleting the current constraint
                PARAMS = {'update':'PREFIX kbe:<http://www.kbe_chair.com/.owl#> DELETE {?'+ ch +' kbe:'+ manuf_constraints[i] +' ?value.} WHERE {?'+ ch +' kbe:'+ manuf_constraints[i] +' ?value.}'} 

                # Sending get request and saving the response as response object 
                r = requests.post(url = URL, data = PARAMS) 

                # Checking the result
                print("Result for DELETE:", r.text)

                # Inserting the new constraint value
                PARAMS = {'update': 'PREFIX kbe:<http://www.kbe_chair.com/.owl#> INSERT {?'+ ch +' kbe:'+ manuf_constraints[i] +' " '+ str(new_constaints[i]) +' "^^<http://www.w3.org/2001/XMLSchema#string>.} WHERE {?'+ ch +' a kbe:'+ ch +' .}'} 
                
                # sending get request and saving the response as response object 
                r = requests.post(url = URL, data = PARAMS)  

                # Checking the result
                print("Result for INSERT:", r.text)
                

            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()

            s.wfile.write(bytes('<html><body><h2>Valid parameter intervals (mm): </h2>', 'utf-8'))
            s.wfile.write(bytes('<form action="http://127.0.0.1:4321/setParamsIntervals" method="post">', "utf-8"))
            
            s.wfile.write(bytes('<p>The following parameters intervals have arrived. Leg length: ' + str(legLengthMax) + '-' + str(legLengthMin) + 
                ', leg width: '+ str(legWidthMax) + '-' + str(legWidthMin)  + ', backplate length: '+ str(backMax) + '-' + str(backMin)
                + ', seat depth: '+ str(seatDepthMax) + '-' + str(seatDepthMin)  + ', seat width: '+ str(seatWidthMax) + '-' + str(seatWidtMin) 
                + ', apron height: '+ str(apronMax) + '-' + str(apronMin) + '</p>', 'utf-8')) #Confirmation that the constraints have been set and form with the previous values as suggestion if one would like to change again
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
            
 
if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()