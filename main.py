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
    
    clientsocket.send(bytes("HTTP/1.1 200 OK", "utf-8"))
    clientsocket.close()
