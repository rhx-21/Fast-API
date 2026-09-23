from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "THIS IS HOME OF MY WEB"

@app.get("/about")
def about():
    return{
        "message":"This is About"
    }
@app.get("/users")
def user():
    return {
        "name":"Rahul Singh",
        "age": 21
    }
