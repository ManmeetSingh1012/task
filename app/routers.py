# annoted
from typing import Annotated
# api router
from fastapi import APIRouter, Query
from . import database

from .model import todo

router = APIRouter()


# create a new task
@router.post("/create_data",tags=["This end point is use to create the new task"])
def create_todo(data: todo):
    message = database.post_data(data)
    return {"Result":str(message)}


# get list of task
@router.get("/get_task_list",tags=["This end point is use to get the all the task"])
def get_list_data():

    data = []
    result = database.get_all()
    for i in result:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data


# get the specific task
@router.get("/get_task/{id}",tags=["This end point is use to update the task"])
def get_task_id(id: str):
    result = database.get_id(id)
    result["_id"] = str(result["_id"])
    return result


# update the data
@router.put("/update_task/{id}",tags=["This end point is use to upadate the task"])
def update_task(id: str, data: todo):
    result = database.update_data(data,id)
    return {"result": str(result)}


# delete the data
@router.delete("/delete_data",tags=["This end point is used to delete the task"])
def delete(id: Annotated[str, Query(min_length=1)]):
    message = database.delete(id)
    return {"result": str(message)}
