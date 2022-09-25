from server import Server
from routes import Router
from response import Response

class Application:
    def __init__(self, name="bilal", version="0.0.1"):
        self.name = name
        self.version = version
        self.router = Router()

    def run(self, host="localhost", port=8000):
        server = Server(host, port)
        
        while True:
            request, clientsocket, address = server.accept()

            method = request.split(" ")[0]
            path = request.split(" ")[1]
            
            handler = self.router.find_route(path, method)
            
            if handler:
                response = handler(request)
                response.send(clientsocket)
            else:
                response = Response(body="Not found", status_code=404)
                response.send(clientsocket)

            clientsocket.close()
