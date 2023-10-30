#pip install "fastapi[all]"

from fastapi import FastAPI
from .routers import router


discription = """
This is the Task Managment App Built By Manmeet Singh

This App help us to Perform CRUD operation on task
"""
app = FastAPI(title="Task Managment App",description= discription)
app.include_router(router)


@app.get("/root")
def root():
    return {"message":"Welcome to the todo task app"}