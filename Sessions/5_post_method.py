from fastapi import FastAPI

app = FastAPI()

@app.post("/create-user")
def create_user(name:str, age:int):   # isme url query param ki tarah aata hai
    return {                          
        "Name": name,
        "Age": age
    }

@app.post("/create-user")            # isme url normal aata hai
def create_user(user:dict):          # request body m json data bhejna    
    return {
        "message": "User Created",
        "Data": user
    }
