# SImpleWEBSever
# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
from http.server import HTTPServer, BaseHTTPRequestHandler
import platform

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Laptop Device Specifications</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f2f2f2;
                        text-align: center;
                    }}

                    h1 {{
                        color: #333333;
                    }}

                    table {{
                        margin: 30px auto;
                        border-collapse: collapse;
                        background-color: white;
                    }}

                    th, td {{
                        border: 1px solid black;
                        padding: 12px 20px;
                    }}

                    th {{
                        background-color: #dddddd;
                    }}
                </style>
            </head>

            <body>
                <h1>Laptop Device Specifications</h1>

                <table>
                    <tr>
                        <th>Specification</th>
                        <th>Details</th>
                    </tr>

                    <tr>
                        <td>Operating System</td>
                        <td>{platform.system()} {platform.release()}</td>
                    </tr>

                    <tr>
                        <td>Machine</td>
                        <td>{platform.machine()}</td>
                    </tr>

                    <tr>
                        <td>Processor</td>
                        <td>{platform.processor()}</td>
                    </tr>

                    <tr>
                        <td>Python Version</td>
                        <td>{platform.python_version()}</td>
                    </tr>
                </table>
            </body>
            </html>
            """

            self.wfile.write(html.encode("utf-8"))

        else:
            self.send_error(404, "Page Not Found")


HOST = "127.0.0.1"
PORT = 8000

server = HTTPServer((HOST, PORT), MyRequestHandler)

print(f"Server running at http://{HOST}:{PORT}")
print("Press Ctrl+C to stop the server.")

server.serve_forever()

## OUTPUT:
After running the program:

Server running at http://127.0.0.1:8000
Press Ctrl+C to stop the server.

Open a web browser and enter:

http://127.0.0.1:8000

The browser displays a web page titled Laptop Device Specifications, containing details such as:

Operating System
Machine architecture
Processor
Python version

The actual values depend on the laptop on which the program is executed.

## RESULT:
The program for implementing simple webserver is executed successfully.The program for implementing a simple web server using Python was executed successfully, and the laptop device specifications were displayed on an HTML web page.
