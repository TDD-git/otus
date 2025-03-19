from annotated_types import Len
from pydantic import BaseModel
from typing import Annotated

class NewMovie(BaseModel):
    title: Annotated[str, Len(min_length=3, max_length=24)]
    director: Annotated[str, Len(min_length=3, max_length=24)]