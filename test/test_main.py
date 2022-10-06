
from pythonserver import Response, Router, Application

app = Application("localhost", 8000)

router = Router()


@router.get("/")
def index(request):
    return Response(body="Hello World!", status_code=200, headers={"Header": "Value"})


def test_index():
    pass
