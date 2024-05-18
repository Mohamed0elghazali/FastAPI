import uvicorn

from enum import Enum
from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(...)
    description: str = Field(None)
    price: float = Field(...)
    tax: float = Field(None)
    tags: list[str] = Field(None)

class Tags(Enum):
    items = "Items"
    users = "Users"
    
@app.post("/items/", 
          response_model=Item, 
          status_code=status.HTTP_201_CREATED, 
          tags=[Tags.items], 
          summary="Create Item Endpoint",
          response_description="The Created Item.")
async def create_item(item: Item):
    """
    Create an item of type Item:
    
    - **name** field is required and it`s a string.
    - **descriptiom** field is not required and it`s a string with default of None.
    - **price** field is required and it`s a float.
    - **tax** field is not required and it`s a float with default of 0.
    - **tags** field is not required and it`s list of string.
    """
    return item

@app.get("/items/", tags=[Tags.items], description="This Endpoint return all items in database.")
async def get_item():
    return {"Item": "PC"}
    
    
@app.get("/users/", tags=[Tags.users])
async def get_user():
    return {"username": "mohamed"}
    
     
if __name__ == "__main__":
    uvicorn.run("Video_20:app", host="127.0.0.1", port=8000, reload=True)