from typing import Annotated
from fastapi import APIRouter, Query, Form, HTTPException
from .schemas import NewMovie
from .movies_DB import movies
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED


router = APIRouter(
    prefix="/movies",
    tags=["Фильмы"],
)


@router.get(
    "",
    summary="Получить все фильмы",
    status_code=HTTP_200_OK

)
def read_movies(
        filter_name: Annotated[str, Query(alias="filter")] = None,
):
    if filter_name:
        filtered_movies = [
            movie
            for movie in movies
            if filter_name.lower() in movie["title"].lower()
        ]
        return {"movies": filtered_movies}
    return {"movies": movies}


@router.post(
    "",
    summary="Добавление нового фильма",
    status_code=HTTP_201_CREATED

)
def create_movie(new_movie: Annotated[NewMovie, Form()]):
    if any(new_movie.title.lower() == movie["title"].lower() for movie in movies):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f'Movie {new_movie.title} already exists!',
        )
    new_m = {
        "id": len(movies) + 1,
        "title": new_movie.title.title(),
        "director": new_movie.director.title()
        }
    movies.append(new_m)
    return {"new_movie": new_m}


@router.get(
    "/{movie_id}",
    summary="Получить конкретный фильм по ID",
    status_code=HTTP_200_OK,
)
def get_book(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Фильм не найден")

