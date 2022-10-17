
from pythonserver import Response, Router, Application

app = Application("localhost", 8000)
router = Router()

@app.get("/")
def index(request):
    return Response(body="Hello World!", status_code=200, headers={"Header": "Value"})


@app.get("/about")
def about(request):
    return Response(body="About page", status_code=200, headers={"Header": "Value"})


@app.get("/contact")
def contact(request):
    return Response(body="Contact page", status_code=200, headers={"Header": "Value"})


@router.get("/test")
def test(request):
    return Response(body="Test page", status_code=200, headers={"Header": "Value"})

app.add_router(router)
app.run()
