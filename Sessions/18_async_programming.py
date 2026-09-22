# async programming m ek sath multiple request handle hoti hai

from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

# Sync programming 

def task():
   time.sleep(4)
   return "Done"

# async programming

async def task():
    await asyncio.sleep(4)
    return 'Done'

@app.get('/')
async def home():
    await asyncio.sleep(3)
    return {
        'Message':'Async API'
        }
