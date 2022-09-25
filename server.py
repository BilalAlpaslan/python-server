
import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((self.host, self.port))
        self._server.listen(5)
        print(f"Server started on port {self.port}")

    def accept(self):
        clientsocket, address = self._server.accept()
        request = clientsocket.recv(1024).decode("utf-8")
        path = request.split(" ")[1]
        print(f"Connection from {address} has been established!, path: {path}")
        return request, clientsocket, address
