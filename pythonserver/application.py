from pythonserver.server import Server
from pythonserver.routes import Router
from pythonserver.response import Response


class Application:
    def __init__(self, name="bilal", version="0.0.1"):
        self.name = name
        self.version = version
        self.router = Router()

    def run(self, host="localhost", port=8000, debug=True):
        server = Server(host, port)
        
        if debug:
            print(f"Running {self.name} on http://{host}:{port}")

        while True:
            request, clientsocket, address = server.accept()

            method = request.split(" ")[0]
            path = request.split(" ")[1]

            handler = self.router.find_route(path, method)

            if handler:
                handler(request).send(clientsocket)
            else:
                Response(body="Not found", status_code=404).send(clientsocket)

            clientsocket.close()
