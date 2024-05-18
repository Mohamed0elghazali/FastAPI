import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from fastapi.encoders import jsonable_encoder

app = FastAPI()

fake_db = {}

class Item(BaseModel):
    title: str 
    timestamp: datetime = datetime.now()
    description: str = Field(None)
    price: float

@app.put("/items/{id}")
async def update_item(id: str, item: Item):
    fake_db[id] = item
    print(fake_db)
    return item

@app.put("/items/{id}/json")
async def update_item_json(id: str, item: Item):
    item_encoder = jsonable_encoder(item)
    fake_db[id] = item_encoder
    print(fake_db)
    return item_encoder    
# note that the return of the previos two endpoints are same 
# as FastAPI by default encode data to json before send it.  

items = {
    "item_1": {"title": "PC", "price": 1500},
    "item_2": {"title": "Playstation5", "price": 2000, "description": "This PS 5"}
}

@app.put("/items_DB/{id}")
async def update_item_db(id: str, item: Item):
    item_encoded = jsonable_encoder(item)
    items[id] = item_encoded
    return items

@app.patch("/items_DB_part/{id}")
async def update_part_of_item_db(id: str, item: Item):
    stored_item_data = items.get(id)
    if stored_item_data == None:
        stored_item_model = Item(title="", price=0)
    else:
        stored_item_model = Item(**stored_item_data)
    
    update_date = item.model_dump(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_date)
    
    item_encoded = jsonable_encoder(updated_item)
    items[id] = item_encoded
    return items
# it has a small problem as you have to update required fields in model

if __name__ == "__main__":
    uvicorn.run("Video_21:app", host="127.0.0.1", port=8000, reload=True)