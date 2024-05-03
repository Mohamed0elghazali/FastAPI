import uvicorn
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

# difference between path parameter and query parameter
# path parameter: we add the parameter in the path url 
# eg. @app.get("items/{item_id}")
# eg. async def get_item(item_id):
# query parameter: we just define the parameter in the endpoint arguments
# eg. @app.get("items")
# eg. async def get_item(item_id):


# simulate a database
items_data = ["Monitor", "PC", "Mouse", "SmartPhone", "Keyboard", "TV"]

@app.get("/items/")
async def search_items(skip: int = 0, limit: int = 1):
    return items_data[skip: skip + limit]

@app.get("/items/{item_id}")
async def search_items(item_id: int, q: Optional[str] = None):
    # we can use q: str | None = None from python 3.10 and above
    # it means that q is string and can be None.

    # if you didn`t assign a default value for the query parameter
    # it will be required parameter then.
    if q:
        if items_data[item_id] == q:
            return {"details": f"You are search on {q}"}
        else:
            return {"details": f"This is not the right item id you search on. {items_data[item_id]} - {q}"}
    return items_data[item_id:item_id+1]

if __name__ == "__main__":
    uvicorn.run("Video_3:app", host="127.0.0.1", port=8000, reload=True)
