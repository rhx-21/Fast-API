from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):     # Nested Model
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    address: Address

@app.post("/create-user")
def create_user(user:User):
    return {
        "message": "User Created",
        "Data": user
    }
