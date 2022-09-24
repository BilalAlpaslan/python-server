import socket

from response import Response
from server import Server

server = Server("localhost", 8000)


while True:
    request, clientsocket, address = server.accept()

    path = request.split(" ")[1]

    html = f"""<html><head><title>Test</title></head><body><h1>Path: {path}</h1></body></html>"""

    Response(body=html).send(clientsocket)

    clientsocket.close()
