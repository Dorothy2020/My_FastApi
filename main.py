# initializing my fast api
import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello"}

#create an endpoint that gets a random number. limit should be 100

@app.get("/random")
async def get_number():
    rn:int=random.randint(0,100)
    return {"number":rn,"limit":100}

# set the limit of the random number
@app.get("/random/{limit}")
async def get_number(limit:int):
    rn:int=random.randint(0,limit)
    return {"number":rn,"limit":limit}

