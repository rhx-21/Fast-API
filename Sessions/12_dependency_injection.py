# Agar har API m token verification karna ho toh uska ek alag function bana dete hai aur jaha jarurat hoti hai waha use karte hai

from fastapi import FastAPI,Depends

app = FastAPI()

def current_user():
    return{
        "user":"rahul singh"
    }

@app.get("/profile")
def profile(user=Depends(current_user)):  # Yaha hamne dependency injection k through dusara  commonly run karaya hai
    return user

@app.get("/dashboard")
def dashboard(user=Depends(current_user)): 
    return user



