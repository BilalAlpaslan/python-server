import threading
from pythonserver.server import Server
from pythonserver.routes import Router
from pythonserver.response import Response


class Application:
    def __init__(self, name="bilal", version="0.0.1"):
        self.name = name
        self.version = version
        self.router = Router()

    def get(self, *args, **kwargs):
        return self.router.get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.router.post(*args, **kwargs)

    def put(self, *args, **kwargs):
        return self.router.put(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.router.delete(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.router.patch(*args, **kwargs)

    def options(self, *args, **kwargs):
        return self.router.options(*args, **kwargs)

    def head(self, *args, **kwargs):
        return self.router.head(*args, **kwargs)

    def connect(self, *args, **kwargs):
        return self.router.connect(*args, **kwargs)

    def trace(self, *args, **kwargs):
        return self.router.trace(*args, **kwargs)

    def any(self, *args, **kwargs):
        return self.router.any(*args, **kwargs)

    def add_router(self, router):
        self.router.add_router(router)

    def run(self, host="localhost", port=8000, debug=True):
        self.host = host
        self.port = port
        self.debug = debug
        self.server = Server(self.host, self.port)

        thread = threading.Thread(target=self._run)
        thread.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("Server stopped")
            self.server.close()
            # kill the thread
            exit(0)

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
