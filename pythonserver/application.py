from pythonserver.server import Server
from pythonserver.routes import Router
from pythonserver.response import Response


class Application:
    def __init__(self, name="bilal", version="0.0.1"):
        self.name = name
        self.version = version
        self.router = Router()

    def run(self, host="localhost", port=8000, debug=True):
        self.host = host
        self.port = port
        self.debug = debug
        self.server = Server(self.host, self.port)

        # run _run method in a subprocess
        self._run()

    def _run(self):

        if self.debug:
            print(
                f"Running {self.name} on http://{self.host}:{self.port} (CTRL + C to quit)")

        while True:
            request, clientsocket, address = self.server.accept()

            method = request.split(" ")[0]
            path = request.split(" ")[1]

            handler = self.router.find_route(path, method)

            if handler:
                handler(request).send(clientsocket)
            else:
                Response(body="Not found", status_code=404).send(clientsocket)

            clientsocket.close()
