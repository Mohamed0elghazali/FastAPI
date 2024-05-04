import uvicorn

from typing import Optional
from fastapi import FastAPI, Query, Path

app = FastAPI()

# in python you can`t define a non-default argument after default argument.
# only if you add * first.
# which means that all the parameters after it are keyword arguments (kwargs)

@app.get("/items/{item_id}")
async def get_item(
    *,
    item_id: int = Path(..., title="The Id of the item to get.", ge=10, lt=15),
    q: str = Query(None, title="The query parameter.", alias="query_search"),
    qq: str):
    results = {"item_id": item_id, "qq": qq}
    if q:
        results.update({"q": q})
    return results

if __name__ == "__main__":
    uvicorn.run("Video_6:app", host="127.0.0.1", port=8000, reload=True)