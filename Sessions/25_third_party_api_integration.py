# pip install requests
# Third Party API Website - Jsonplaceholder

from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Get all data

@app.get("/photos")
def get_photos():
    url = "https://jsonplaceholder.typicode.com/photos"
    response = requests.get(url)
    data = response.json()
    return {
        "Total": len(data),
        "Data": data
        }

# Get specific data

@app.get("/photos/{photo_id}")
def get_photo(photo_id):
    url = f"https://jsonplaceholder.typicode.com/photos/{photo_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404,detail="Page not found")
    return response.json()

