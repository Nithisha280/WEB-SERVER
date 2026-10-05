from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
    <title>My Webserver</title>
</head>
<body>
    <h1>Welcome to My Webserver</h1>
    <h2>Laptop Device Specifications</h2>

    <p><b>Processor:</b> Intel Core i5</p>
    <p><b>RAM:</b> 8 GB</p>
    <p><b>Storage:</b> 512 GB SSD</p>
    <p><b>Operating System:</b> Windows 11</p>
</body>
</html>
"""


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Request received")

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(content.encode())


server_address = ("127.0.0.1", 8000)

httpd = HTTPServer(server_address, MyHandler)

print("My webserver is running...")

httpd.serve_forever()