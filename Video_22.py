import uvicorn

from fastapi import Depends, FastAPI

app = FastAPI()

async def hello():
    return "world"

async def common_parameters(q: str = None, 
                            skip: int = 0, 
                            limit: int = 100,
                            others: str = Depends(hello)):
    return {"q": q, "skip": skip, "limit": limit, "hello": others}

@app.get("/items/")
async def read_items(common: dict = Depends(common_parameters)):
    return common

if __name__ == "__main__":
    uvicorn.run("Video_22:app", host="127.0.0.1", port=8000, reload=True)