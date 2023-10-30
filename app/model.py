# for annotation
from typing import Annotated
# for pydantic model
from pydantic import BaseModel, Field
# for date time
from datetime import date


class todo(BaseModel):
    id: Annotated[str,Field(min_length=1)]
    title: Annotated[str, Field(min_length=1)]
    description: Annotated[str, Field(min_length=1)]
    duedate: date




