from pymongo.mongo_client import MongoClient
from .model import todo
# json encoder
from fastapi.encoders import jsonable_encoder

uri = "mongodb+srv://manmeetsingh:manmeetsingh@taskcluster.bs3kzwv.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
dbs = client["Task_Database"]
collection = dbs["Task"]


def post_data(data: todo):
    jsondata = jsonable_encoder(data)
    result = collection.insert_one(jsondata)
    return result.inserted_id


def get_id(id:str):
    result = collection.find_one({"id":id})
    return result

def get_all():
    result = collection.find({})
    return result

def update_data(data:todo,id:str):
    response = collection.update_one({"id": id}, {"$set": {"title": data.title,"description":data.description}})
    return response


def delete(id: str):
    result = collection.delete_one({"id": id})
    return result




