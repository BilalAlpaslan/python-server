

from datetime import datetime


class Response:
    SERVER_NAME = "Bilal/0.0.1"

    def __init__(self, body=None, status_code=200, headers=None, content_type="text/html", charset="utf-8"):
        self.body = body
        self.status_code = status_code
        self.headers = headers
        self.content_type = content_type
        self.charset = charset
        self.date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")

    def send(self, clientsocket):
        clientsocket.send(bytes(
            f"""HTTP/1.1 {self.status_code} OK\r
Connection: keep-alive\r
Date: {self.date}\r
Server: {self.SERVER_NAME}\r
Content-Type: {self.content_type}; charset={self.charset}\r
Content-Length: {len(self.body)}\r
Header: {self.headers}\r
\r
{self.body}
""", "utf-8"))
