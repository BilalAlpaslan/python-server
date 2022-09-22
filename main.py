import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 8000))
print(f"Server started on port 8000")

server.listen(5)

while True:
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established!")

    request = clientsocket.recv(1024).decode("utf-8")
    path = request.split(" ")[1]

    print(f"Path: {path}")

    clientsocket.send(bytes(
"""HTTP/1.1 200 OK \r
Connection: keep-alive \r
Date: Mon, 23 May 2016 12:54:48 GMT \r
Server: Bilal/0.0.1 \r
Content-Type: text/html; charset=utf-8 \r
Content-Length: 12 \r
Header: Example \r
\r
Hello World!
""", "utf-8"))
    clientsocket.close()
