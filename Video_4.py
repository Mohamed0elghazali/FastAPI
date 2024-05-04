import uvicorn

from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


# you can now accept data from the request body.
# using the item parameter but make sure to define it as dict or any model.
# a dict example.
@app.post("/items/")
async def create_item(item: dict):
    return item


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float

# a model example, and it has to be pydantic class
# because FastAPI expects a Pydantic model for automatic response serialization.
# if you don`t do so, you have to handle serialization manually. (response_model=None)
@app.post("/items/create")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# an endpoint with path, query and body parameter.
@app.put("/items/{item_id}")
async def edit_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


if __name__ == "__main__":
    uvicorn.run("Video_4:app", host="127.0.0.1", port=8000, reload=True)