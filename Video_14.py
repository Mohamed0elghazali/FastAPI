from typing import Literal, Union
import uvicorn

from pydantic import BaseModel, EmailStr
from fastapi import FastAPI

app = FastAPI()

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    
class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str
    
def fake_password_hasher(raw_password: str):
    return f"FakePasswordHasher{raw_password}"

def save_fake_password(user_in: UserIn):
    fake_password = fake_password_hasher(user_in.password)
    userdb = UserInDB(**user_in.model_dump(), hashed_password=fake_password)
    print("User Saved!")
    return userdb

@app.post("/user", response_model=UserOut)
async def create_user(user: UserIn):
    user_saved = save_fake_password(user)
    return user_saved

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type: str = "car"
    wheels: int = 4
    
class PlaneItem(BaseItem):
    type: str = "plane"
    size: int    
    
items = {
    "item_1": {"description": "This is a Car"},
    "item_2": {"description": "This is a Plane", "type": "plane", "size": 1000}
}

# make sure to put the class from the last defined to the first defined.
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: Literal["item_1", "item_2"]):
    return items[item_id]

class ListItem(BaseModel):
    name: str
    description: str
    
list_items = [
    {"name": "foo", "description": "hello"},
    {"name": "boo", "description": "world"}
]

@app.get("/list_items/", response_model=list[ListItem])
async def read_items():
    return list_items


if __name__ == "__main__":
    uvicorn.run("Video_14:app", host="127.0.0.1", port=8000, reload=True)