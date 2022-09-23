import socket
from time import sleep

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

server.bind(('localhost', 8000))
# server6.bind(('[0:0:0:0:0:0:0:1]', 8000))
print(f"Server started on port 8000")

server.listen(5)
# server6.listen(5)


while True:
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established!")

    request = clientsocket.recv(1024).decode("utf-8")
    path = request.split(" ")[1]

    print(f"Path: {path}")
    
    html = f"""<html>
<head><title>Test</title></head><body><h1>Test  Path: {path}"""

    raw = f"""HTTP/1.1 200 OK \r
Connection: keep-alive \r
Date: Mon, 23 May 2016 12:54:48 GMT \r
Server: Bilal/0.0.1 \r
Content-Type: text/html; charset=utf-8 \r
Content-Length: {len(html)+23+100} \r
Header: Example \r
\r
{html}
"""

    clientsocket.send(bytes(
f"""HTTP\r
\r
{html}
""", "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))
    sleep(5)
    clientsocket.send(bytes('-', "utf-8"))

    sleep(5)
    clientsocket.send(bytes('-</h1></body></html>', "utf-8"))

    sleep(5)
    clientsocket.close()

