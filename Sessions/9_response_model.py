from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:int

class UserResponse(BaseModel):
    name:str
    age:int

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "name":"rahul singh",
        "age": 31,
        "password": 7890787
    }
