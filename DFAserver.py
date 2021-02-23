# HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

leg_length = 0
leg_width = 0
height_backplate = 0
seat_length = 0
seat_width = 0
apron_heigth = 0
chair_colour = 0
seat_colour = 0

HOST_NAME = '127.0.0.1'  # locathost - http://127.0.0.1
#complete address would be: http://127.0.0.1:1234
PORT_NUMBER = 1234

dfaPath = "C:\\Users\\Amalie\\Documents\\GitHub\\TMM4275-KBE-project\\DFAs\\" #The location of your DFA files

f = open(dfaPath + "templates\\My_Chair_template.dfa", "r") 
fileContent = f.read()
f.close() #Opens and reads the DFA template to so that a new DFA file of the order can be made later

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

        path = s.path
        if path.find("/") != -1 and len(path) == 1:
            s.wfile.write(
                bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(
                bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))
        elif path.find("/info") != -1:
            s.wfile.write(
                bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(
                bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes("<body><p>Let's order a chair</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))
        elif path.find("/orderChair") != -1: #The webpage path to order a chair
            s.wfile.write(bytes('<html><body><h2>Set chair specifications (mm):</h2>', "utf-8"))
            s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8')) #Create a form to take in values
            s.wfile.write(bytes('<br>Legs length:<br><input type="text" name="leg_length" value="0">', "utf-8"))
            s.wfile.write(bytes('<br>Legs width:<br><input type="text" name="leg_width" value="0">', "utf-8"))
            s.wfile.write(bytes('<br>Backplate height:<br><input type="text" name="height_backplate" value="0">', "utf-8"))
            s.wfile.write(bytes('<br>Seat length:<br><input type="text" name="seat_length" value="0">', "utf-8"))
            s.wfile.write(bytes('<br>Seat width:<br><input type="text" name="seat_width" value="0">', "utf-8"))
            s.wfile.write(bytes('<br>Apron height:<br><input type="text" name="apron_height" value="0">', "utf-8"))
            s.wfile.write(bytes('<br>Chair colour:<br><select name="chair_colour" id="chair_colour"><option value="LIGHT_HARD_GREEN">Landscape Green</option><option value="CYAN">Icy Blue</option><option value="LIGHT_RED_ORANGE">Flaming Red</option><option value="LIGHT_FADED_YELLOW">Lightning Yellow</option></select>', "utf-8"))
            s.wfile.write(bytes('<br><br><input type="submit" value="Submit"></form><p> Click "Submit" to send order.</p></body></html>', "utf-8"))
        else:
            s.wfile.write(
                bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(
                bytes("<body><p>The path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))

    def do_POST(s):

        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        within_constraints = False #Boolean to see check if the customers order is within the manufactor constraints

        # Check what is the path
        path = s.path
        print("Path: ", path)
        
        if path.find("/orderChair") != -1:
            content_len = int(s.headers.get('Content-Length')) #Gets the string with the chair values
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)

            splitString = param_line.split("&") #Splits string so that the values can be set for each variable
            newSplit = []
            for i in splitString:
                newSplit.append(i.split("="))

            leg_length = int(newSplit[0][1])
            leg_width = int(newSplit[1][1])
            height_backplate = int(newSplit[2][1])
            seat_length = int(newSplit[3][1])
            seat_width = int(newSplit[4][1])
            apron_heigth = int(newSplit[5][1])
            chair_colour = newSplit[6][1] #Every variable has been given their value from the string

            manuf_constraints = ["legLengthMax","legLengthMin", "legWidthMax", "legWidthMin", #List of all the constraints from the manufactor
                "backMax", "backMin", "seatDepthMax", "seatDepthMin",
                "seatWidthMax", "seatWidthMin", "apronMax", "apronMin"]
            manuf_results = [] #Empty list for placing the value of the manufactor constraints
            URL = "http://127.0.0.1:3030/kbe/query" #URL of the server

            for c in manuf_constraints: #A for-loop that sends a query for every constraint
                PARAMS = {'query':'PREFIX kbe:<http://www.kbe_chair.com/.owl#> SELECT ?data WHERE {?inst kbe:' + c + ' ?data.}'} 
                # sending get request and saving the response as response object 
                r = requests.get(url = URL, params = PARAMS) 
                data = r.json()
                manuf_results.append(int(data['results']['bindings'][0]['data']['value']))
                print(c, data['results']['bindings'][0]['data']['value'])
            if leg_length <= manuf_results[0] and leg_length >= manuf_results[1]:
                if leg_width <= manuf_results[2] and leg_width >= manuf_results[3]:
                    if height_backplate <= manuf_results[4] and height_backplate >= manuf_results[5]:
                        if seat_length <= manuf_results[6] and seat_length >= manuf_results[7]:
                            if seat_width <= manuf_results[8] and seat_width >= manuf_results[9]:
                                if apron_heigth <= manuf_results[10] and apron_heigth >= manuf_results[11]: #Checks if every value the costumer has set is within the constraints
                                    print("Params OK")
                                    within_constraints = True

            if within_constraints: #If the chair is possible to make then the customer will be sent to this webpage and be able to order more
                s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
                s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8'))
                s.wfile.write(bytes('<label for="Thanks">Thank you for your order!</label><br>', 'utf-8'))

                s.wfile.write(bytes('<p>The following parameters have arrived. Leg length: ' + str(leg_length)
                    + ', leg width: '+ str(leg_width) + ', backplate length: '+ str(height_backplate)
                    + ', seat depth: '+ str(seat_length) + ', seat width: '+ str(seat_width) 
                    + ', apron height: '+ str(apron_heigth) + '</p>', 'utf-8'))
                s.wfile.write(bytes('<label for="More">Submit again if you wish to order more.</label><br>', 'utf-8')) #A confirmation that the different parameters have been set for the chair

                s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8')) #Form if the customer wish to order more chairs, with the previous values as suggestions in the form
                s.wfile.write(bytes('<br>Legs length:<br><input type="text" name="leg_length" value="' + str(leg_length) + '">', "utf-8"))
                s.wfile.write(bytes('<br>Legs width:<br><input type="text" name="leg_width" value="' + str(leg_width) + '">', "utf-8"))
                s.wfile.write(bytes('<br>Backplate height:<br><input type="text" name="height_backplate" value="' + str(height_backplate) + '">', "utf-8"))
                s.wfile.write(bytes('<br>Seat length:<br><input type="text" name="seat_length" value="' + str(seat_length) + '">', "utf-8"))
                s.wfile.write(bytes('<br>Seat width:<br><input type="text" name="seat_width" value="' + str(seat_width) + '">', "utf-8"))
                s.wfile.write(bytes('<br>Apron height:<br><input type="text" name="apron_height" value="' + str(apron_heigth) + '">', "utf-8"))
                s.wfile.write(bytes('<br>Chair colour:<br><select name="chair_colour" id="chair_colour"><option value="LIGHT_HARD_GREEN">Landscape Green</option><option value="CYAN">Icy Blue</option><option value="LIGHT_RED_ORANGE">Flaming Red</option><option value="LIGHT_FADED_YELLOW">Lightning Yellow</option></select>', "utf-8"))
                s.wfile.write(bytes('<br><br><input type="submit" value="Submit"></form><p> Click "Submit" to send order.</p></body></html>', "utf-8"))
                s.wfile.write(bytes('<img src="https://raw.githubusercontent.com/amaliebholm/TMM4275-KBE-project/amalie_test/chair.jpg" width="252" height="400">', "utf-8"))


                fileContentOut = fileContent
                fileContentOut = fileContentOut.replace("My_Chair_template (ug_base_part)", "My_Chair_Order (ug_base_part)") #Replaces the template with the customers chair values
                fileContentOut = fileContentOut.replace("<PARAM_LEGLENGTH>", str(leg_length))
                fileContentOut = fileContentOut.replace("<PARAM_LEGWIDTH>", str(leg_width))
                fileContentOut = fileContentOut.replace("<PARAM_BACK>", str(height_backplate))
                fileContentOut = fileContentOut.replace("<PARAM_APRON>", str(apron_heigth))
                fileContentOut = fileContentOut.replace("<PARAM_SEATWIDTH>", str(seat_width))
                fileContentOut = fileContentOut.replace("<PARAM_SEATDEPTH>", str(seat_length))
                fileContentOut = fileContentOut.replace("<PARAM_COLOR>", str(chair_colour)) 
                

                f = open(dfaPath + "My_Chair_Order.dfa", "w") #Saves the customers chair as a new DFA file with the name My_Chair_Order.dfa
                f.write(fileContentOut)
                f.close()

                return leg_length, leg_width, height_backplate, seat_length, seat_width, apron_heigth, chair_colour, seat_colour
            else: #If the chair is NOT possible to make then the customer will be sent to this webpage and must try again to set values within the constraints to order
                s.wfile.write(bytes('<html><body><h2>Set chair specifications (mm):</h2>', "utf-8"))
                s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8'))
                s.wfile.write(bytes('<p>The parameters where outside the constraints, please enter valid parameters to order a chair</p>', 'utf-8'))
                s.wfile.write(bytes('<br>Legs length:<br><input type="text" name="leg_length" value="0">', "utf-8"))
                s.wfile.write(bytes('<br>Legs width:<br><input type="text" name="leg_width" value="0">', "utf-8"))
                s.wfile.write(bytes('<br>Backplate height:<br><input type="text" name="height_backplate" value="0">', "utf-8"))
                s.wfile.write(bytes('<br>Seat length:<br><input type="text" name="seat_length" value="0">', "utf-8"))
                s.wfile.write(bytes('<br>Seat width:<br><input type="text" name="seat_width" value="0">', "utf-8"))
                s.wfile.write(bytes('<br>Apron height:<br><input type="text" name="apron_height" value="0">', "utf-8"))
                s.wfile.write(bytes('<br>Chair colour:<br><select name="chair_colour" id="chair_colour"><option value="LIGHT_HARD_GREEN">Landscape Green</option><option value="CYAN">Icy Blue</option><option value="LIGHT_RED_ORANGE">Flaming Red</option><option value="LIGHT_FADED_YELLOW">Lightning Yellow</option></select>', "utf-8"))
                s.wfile.write(bytes('<br><br><input type="submit" value="Submit"></form><p> Click "Submit" to send order.</p></body></html>', "utf-8"))
                s.wfile.write(bytes('<img src="https://raw.githubusercontent.com/amaliebholm/TMM4275-KBE-project/amalie_test/chair.jpg" width="252" height="400">', "utf-8"))
                print("Params not OK")

                


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
