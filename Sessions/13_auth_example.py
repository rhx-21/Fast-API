from fastapi import FastAPI,Depends,Header,HTTPException

app = FastAPI()

def verify_token(token:str = Header(None)):
    if token != "mytoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return {
        "User":"Authorized User"
    }
    
@app.get("/security")
def secure(user=Depends(verify_token)):
    return {
        "Message":"Secure Data Accessed",
        "user":user
    }
