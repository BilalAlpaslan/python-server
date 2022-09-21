import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 8000))
print(f"Server started on port 8000")

server.listen(5)

while True:
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established!")
    print(f'path: {clientsocket.recv(1024).decode("utf-8")}')
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    print("Sent Hello World to", address)
    clientsocket.close()
