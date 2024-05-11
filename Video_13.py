import uvicorn

from typing import Literal
from pydantic import BaseModel, EmailStr, Field
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str = Field(None)
    description: str = Field(None)
    price: float = Field(None)
    tax: float = Field(None)
    tags: list[str] = []

items = {
    "foo": {"name": "foo", "price": 50.2},
    "bar": {"name": "bar", "description": "TV", "price": 100, "tax": 20},
    "baz": {"name": "baz", "description": "PC", "price": 200, "tax": 10, "tags": []}
}

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

# using response_models helps in change the information we want to return 
# desipte of the input class.
@app.post("/Signin", response_model=UserOut)
async def signin(user: UserIn):
    return user

# it return string as we didn`t define the return model.
@app.post("/items")
async def create_item(item: Item):
    return item

@app.get("/items/{choose_item}", 
         response_model=Item, 
         response_model_exclude_unset=True)
def choose_item(choose_item: Literal["foo", "bar", "baz"]):
    return items[choose_item]

# you can use exclude_unset to return the same fields sent from the body only.
# response_model_exclude_unset = False
@app.post("/items/", 
         response_model=Item, 
         response_model_exclude_unset=False)
def choose_item(item: Item):
    return item


# you can now use the same model 
# and choose which fields to include or exclude.
# response_model_include={"name", "description"}
# response_model_exclude={"tax"}
@app.post("/items/include", 
         response_model=Item, 
         response_model_include={"name", "description"})
def choose_item_include(item: Item):
    return item

@app.post("/items/exclude", 
         response_model=Item, 
         response_model_exclude={"tax"})
def choose_item_include(item: Item):
    return item

if __name__ == "__main__":
    uvicorn.run("Video_13:app", host="127.0.0.1", port=8000, reload=True)