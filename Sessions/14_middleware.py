# use for performance tracking, debugging, api-monitoring  | authentication check, logging, request validate,rate limiter, 

from fastapi import FastAPI,Request
import time

app = FastAPI()

@app.middleware("http")
async def my_middleware(request:Request, call_next):
    print("Request Received")

    response = await call_next(request) 
    print("Response Sent")
    return response


#  Logging Middleware

@app.middleware("http")
async def log_middleware(request:Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f'path:{request.url.path} | Time: {process_time}')
    return response




#  difference between dependency-injection and middleware

#       Dependency                            Middleware
    
#       per route                               global hota hai 
#       specific api par bhi chal               har request par chalega
#       sakti hai
