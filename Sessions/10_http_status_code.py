from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

@app.post("/user", status_code=status.HTTP_201_CREATED)
def user_created():
    return {
        "message":"user created"
        }
