from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def user(user_id:int):
    return {
        "User_id": user_id
    }
