from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/about",
            name="main:about")
def get_root(
        request: Request
):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
    )
