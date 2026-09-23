# Use in Production
# pip install passlib[bcrypt]
# pip install python-multipart

from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError

app = FastAPI()

# JWT config

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password Hashing Setup

pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")

# OAuth Setup

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

# Dummy User DB

fake_user_db = {
    "admin":{
        "username": "admin",
        "hashed_password":pwd_context.hash("12345")
    }
}

# Hash Password

def hash_password(password:str):
    return pwd_context.hash(password)

# verify password

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password,hashed_password)

# create Token

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update( {
            "exp":expire
        })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

# Login API (OAuth2 Form)

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )
    access_token = create_token({"username":form_data.username})
    
    return{
        "access_token":access_token,
        "token_type": "bearer"
    }

# Verify Token
def verify_token(token:str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username:str = payload.get("username")
        if username is None:
            raise HTTPException(
                status_code= 401,
                detail='Invalid Token'
            )
        
        return username
    except JWTError:
        raise HTTPException(
            status_code= 401,
            detail='Invalid Token'
        )

# Protected route
@app.get("/protected")
def protected_route(username:str=Depends(verify_token)):
    return{
        "message":"You have access this route",
        "user": username
    }
