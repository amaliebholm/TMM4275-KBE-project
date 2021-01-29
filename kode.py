# HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1'  # locathost - http://127.0.0.1
# Maybe set this to 1234 / So, complete address would be: http://127.0.0.1:1234
PORT_NUMBER = 1234
# Web servers example: http://www.ntnu.edu:80

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
        elif path.find("/setSize") != -1:
            s.wfile.write(
                bytes('<html><body><h2>Set chair specifications (cm):</h2>', "utf-8"))
            s.wfile.write(
                bytes('<form action="/setSize" method="post">', 'utf-8'))
            s.wfile.write(bytes(
                '<br>Legs length:<br><input type="text" name="leg_length" value="0">', "utf-8"))
            s.wfile.write(bytes(
                '<br>Legs width:<br><input type="text" name="leg_width" value="0">', "utf-8"))
            s.wfile.write(bytes(
                '<br>Backplate height:<br><input type="text" name="height_backplate" value="0">', "utf-8"))
            s.wfile.write(bytes(
                '<br>Seat length:<br><input type="text" name="seat_length" value="0">', "utf-8"))
            s.wfile.write(bytes(
                '<br>Seat width:<br><input type="text" name="seat_width" value="0">', "utf-8"))
            s.wfile.write(bytes(
                '<br>Apron height:<br><input type="text" name="apron_height" value="0">', "utf-8"))
            s.wfile.write(bytes('<br>Chair colour:<br><select name="chair_colour" id="chair_colour"><option value="1">Forrest Brown</option><option value="2">Icy Blue</option><option value="3">Flaming Red</option><option value="4">Lightning Yellow</option></select>', "utf-8"))
            s.wfile.write(bytes('<br>Seat colour:<br><select name="seat_colour" id="seat_colour"><option value="3">Flaming Red</option><option value="2">Icy Blue</option><option value="5">Landscape Green</option><option value="4">Lightning Yellow</option></select>', "utf-8"))
            s.wfile.write(bytes('<br><br><input type="submit" value="Submit"></form><p> Click "Submit" to send order.</p></body></html>', "utf-8"))
            s.wfile.write(bytes('<img src="https://raw.githubusercontent.com/amaliebholm/TMM4275-KBE-project/amalie_test/chair.jpg" width="252" height="400">', "utf-8"))

        elif path.find("/setLength") != -1:
            s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
            s.wfile.write(
                bytes('<form action="/setLength" method="post">', 'utf-8'))
            s.wfile.write(
                bytes('<label for="clength">Set Length:</label><br>', 'utf-8'))
            s.wfile.write(bytes(
                '<input type="text" id="clength" name="clength" value="100"><br><br>', 'utf-8'))
            s.wfile.write(
                bytes('<label for="cwidth">Set Length:</label><br>', 'utf-8'))
            s.wfile.write(bytes(
                '<input type="text" id="cwidth" name="cwidth" value="100"><br><br>', 'utf-8'))
            s.wfile.write(
                bytes('<input type="submit" value="Submit">', 'utf-8'))
            s.wfile.write(bytes('</form></body></html>', 'utf-8'))
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

        # Check what is the path
        path = s.path
        print("Path: ", path)
        if path.find("/setLength") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)

            s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
            s.wfile.write(
                bytes('<form action="/setLength" method="post">', 'utf-8'))
            s.wfile.write(
                bytes('<label for="clength">Set Length:</label><br>', 'utf-8'))
            s.wfile.write(bytes(
                '<input type="text" id="clength" name="clength" value="100"><br><br>', 'utf-8'))
            s.wfile.write(
                bytes('<input type="submit" value="Submit">', 'utf-8'))

            s.wfile.write(bytes('<p>' + param_line + '</p>', 'utf-8'))

            s.wfile.write(bytes('</form></body></html>', 'utf-8'))

        if path.find("/setSize") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)

            splitString = param_line.split("&")
            newSplit = []
            for i in splitString:
                newSplit.append(i.split("="))

            print(newSplit)

            leg_length = int(newSplit[0][1])
            leg_width = int(newSplit[1][1])
            height_backplate = int(newSplit[2][1])
            seat_length = int(newSplit[3][1])
            seat_width = int(newSplit[4][1])
            apron_heigth = int(newSplit[5][1])
            chair_colour = int(newSplit[6][1])
            seat_colour = int(newSplit[7][1])

            print(leg_length, leg_width, height_backplate,
                  seat_length, seat_width, apron_heigth, chair_colour, seat_colour)

            s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
            s.wfile.write(
                bytes('<form action="/setSize" method="post">', 'utf-8'))
            s.wfile.write(
                bytes('<label for="Thanks">Thank you for your order!</label><br>', 'utf-8'))

            s.wfile.write(bytes('<p>' + param_line + '</p>', 'utf-8'))

            s.wfile.write(bytes('</form></body></html>', 'utf-8'))


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
