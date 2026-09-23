# import os
# from dotenv import load_dotenv

from config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# load_dotenv()      # yaha ham .env file ko load kar rahe hai


# ye saara code ham config file m likhte hai

origins = settings.ORIGINS
# ORIGINS = os.getenv("ORIGINS") 
# DB_URL = os.getenv("DATABASE_URL")
# SECRET_KEY = os.getenv("SECRET_KEY")

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],     # Saare methods k liye apply hoga
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
        "message":"CORS ENABLE"
    }
