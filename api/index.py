from fastapi import APIRouter, Request
from api.movies_DB import movies
from starlette.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/",
            name="main:index")
def get_root(
        request: Request
):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"titles": [movie["title"] for movie in movies]}
    )
