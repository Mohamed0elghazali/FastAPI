import uvicorn

from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str):
    return {"item_id": item_id}

@app.get("/items/", status_code=status.HTTP_301_MOVED_PERMANENTLY)
async def read_items_redirect():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("Video_15:app", host="127.0.0.1", port=8000, reload=True)