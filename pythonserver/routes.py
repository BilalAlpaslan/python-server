
from re import S


class Route:
    def __init__(self, path, methods, handler):
        self.path = path
        self.methods = methods
        self.handler = handler

    def match(self, path, method):
        return self.path == path and method in self.methods


class Router:
    def __init__(self, routes: list = []):
        self.routes = routes

    def find_route(self, path, method):
        for route in self.routes:
            if route.match(path, method):
                return route.handler
        return None

    def add_route(self, path, methods, handler):
        self.routes.append(Route(path, methods, handler))

    def add_router(self, router):
        self.routes.extend(router.routes)

    def get(self, path):
        def wrapper(handler):
            def wrapper2(request, *args, **kwargs):
                return handler(request, *args, **kwargs)
            self.add_route(path, ["GET"], wrapper2)
        return wrapper

    def post(self, path, handler):
        def wrapper(request, *args, **kwargs):
            return handler(request, *args, **kwargs)
        self.add_route(path, ["POST"], wrapper)

    def put(self, path, handler):
        def wrapper(request, *args, **kwargs):
            return handler(request, *args, **kwargs)
        self.add_route(path, ["PUT"], wrapper)

    def delete(self, path, handler):
        def wrapper(request, *args, **kwargs):
            return handler(request, *args, **kwargs)
        self.add_route(path, ["DELETE"], wrapper)

    def patch(self, path, handler):
        def wrapper(request, *args, **kwargs):
            return handler(request, *args, **kwargs)
        self.add_route(path, ["PATCH"], wrapper)

    def options(self, path, handler):
        def wrapper(request, *args, **kwargs):
            return handler(request, *args, **kwargs)
        self.add_route(path, ["OPTIONS"], wrapper)

    def head(self, path, handler):
        def wrapper(request, *args, **kwargs):
            return handler(request, *args, **kwargs)
        self.add_route(path, ["HEAD"], wrapper)

    def connect(self, path, handler):
        def wrapper(request, *args, **kwargs):
            return handler(request, *args, **kwargs)
        self.add_route(path, ["CONNECT"], wrapper)

    def trace(self, path, handler):
        def wrapper(request, *args, **kwargs):
            return handler(request, *args, **kwargs)
        self.add_route(path, ["TRACE"], wrapper)

    def any(self, path, handler):
        def wrapper(request, *args, **kwargs):
            return handler(request, *args, **kwargs)
        self.add_route(path,
                       ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD", "CONNECT", "TRACE"], wrapper)
