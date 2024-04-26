import uvicorn

from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/Home")
async def Home():
    return "Welcome To My FastAPI API"

@myapp.get("/")
async def getEndpoint():
    return {"Message": "Welcome from inside get endpoint."}

@myapp.post("/")
async def postEndpoint():
    return {"Message": "Welcome from inside post endpoint."}



if __name__ == "__main__":
    uvicorn.run("1-Intro:myapp", host="127.0.0.1", port=8000, reload=True)
