from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom error Handler

class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name = name
        
# Global Error Handler

@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request:Request, exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"user {exc.name} not found"
        }
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name != 'rahul':
        raise UserNotFoundException(name)
    return {
        "name": name
        }

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return {
        "id":1,
        "name":"rahul singh"
    }
    
