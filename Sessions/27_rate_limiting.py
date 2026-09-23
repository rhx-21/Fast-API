# Unnecessary api hit se protect karna e.g. agar koi api ko 1000 baar hit kar raha hai toh woh spam kar raha hai jisse apka server crash ho sakta hai

# rate limit se aap per minute api hit set kar sakte ho

# pip install slowapi


from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI()

# Limiter Setup

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Error Handle

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "Detail":"Too Many Request"
        }
    )

# API

@app.get("/home")
@limiter.limit("5/minute")
def get_data(request: Request):
    return {
        "Message":"Success"
    }
