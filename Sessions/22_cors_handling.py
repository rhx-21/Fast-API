# CORS - Cross origin resource sharing
# use for connect frontend and backend

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]

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
