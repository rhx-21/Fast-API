# JWT - Json web token
# pip install python-jose     (jose-javascript object signature and encription)

from fastapi import FastAPI,HTTPException,Depends,Header
from datetime import timedelta,timezone,datetime
from jose import jwt

app = FastAPI()

SECRET_KEY = "mysecret"
ALGORITHM =  "HS256"          # HS512,RS256,ES256

# Create Token 

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token


@app.post("/login")
def login(username:str, password:int):
    if username != "rahul_21" or password != 7890:
        raise HTTPException(
            status_code = 401,
            detail="Invalid Username or Password"
        )
    token = create_token({
        "User":username
    })
    
    return {
        "Access Token": token
    }
    
# Token Verify

def verify_token(token:str=Header(None)):
    try: 
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired Token"
        )
        
@app.get("/dashboard")
def dashboard(user=Depends(verify_token)):
    return{
        "message":"Dashboard Access",
        "User":user
    }
