from fastapi import FastAPI
import time
import requests

app = FastAPI()

cache_data = []
last_fetch = 0 

# Get all data

@app.get("/photos")
def get_photos():
    
    global cache_data, last_fetch
    
    start = time.time()
    if time.time() - last_fetch > 60:
        print ("Fetching Fresh Data")
        url = "https://jsonplaceholder.typicode.com/photos"
        response = requests.get(url,timeout=10)
        response.raise_for_status()
        data = response.json()
        
        cache_data = data
        
        last_fetch= time.time()
        end = time.time()
        time_taken = round(end - start, 4)
        
        return {
          "Time Taken":time_taken,
          "Total": len(data),
          "Data": data
        }
    else:
        print("Using Cache Data")

        end = time.time()
        time_taken = round(end - start, 4)
   
    
        return {
        "Time Taken":time_taken,
        "Data": cache_data
            }
