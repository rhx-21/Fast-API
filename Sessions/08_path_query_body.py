from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    
users = []

@app.get("/users")
def get_users():
    return{
        "User Data": users
    }
    
@app.post("/user")
def create_user(user:User):
    users.append(user)
    return {
        "message":"user created" ,
        "Data":user
        }
    
@app.put("/user/{user_id}")
def update_user(user_id:int, user:User, notify:bool = None):
    if user_id < len(users):
        users[user_id] = user
        return{
            "Message":"User Update",
            "notify": notify,
            "User": user
        }
    
    return "User Not Found"
