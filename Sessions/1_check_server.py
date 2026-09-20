# Testing API

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the World"

@app.get("/user")
def user():
    return {        
        "name": "Rahul Singh",
        "age": 23
    }
