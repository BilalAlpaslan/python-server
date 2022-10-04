
from pythonserver import  Response, Router, Application

app = Application("localhost", 8000)

router = Router()


@router.get("/")
def index(request):
    return Response(body="Hello World!", status_code=200, headers={"Header": "Value"})

@router.get("/about")
def about(request):
    return Response(body="About page", status_code=200, headers={"Header": "Value"})

@router.get("/contact")
def contact(request):
    return Response(body="Contact page", status_code=200, headers={"Header": "Value"})


app.router.add_router(router)
app.run()
