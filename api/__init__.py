from fastapi import APIRouter
from .movies import router as movies_router
from .index import router as index_router
from .about import router as about_router


router = APIRouter(
    prefix="/api",
    tags=["api"]
)

router.include_router(movies_router)





