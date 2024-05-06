import uvicorn

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from fastapi import FastAPI, Query, Path, Body

app = FastAPI()


## method 1 (define config class in Item class)
class Item(BaseModel):
    name: str = Field(None)
    description: str = Field(None)
    price: float = Field(None)
    tax: float = Field(None)

    class Config:
        schema_extra = {
            "example": {
                "name": "foo",
                "description": "A simple description",
                "price": 100,
                "tax": 10
            }
        }

## method 2 (define example in Field function)
class Item(BaseModel): 
    name: str = Field(None, example="foo")
    description: str = Field(None, example="A simple description")
    price: float = Field(None, example=100)
    tax: float = Field(None, example=10)

class Item2(BaseModel):
    name: str = Field(None)
    description: str = Field(None)
    price: float = Field(None)
    tax: float = Field(None)

@app.post("/items_create")
async def create_items(item: Item = Body(..., embed=True)):
    return item.model_dump()


# method 3 (define example in body, make sure that embed = False)
@app.post("/items_create_2")
async def create_items_2(item: Item2 = Body( ...,
                                            embed=False, 
                                            example={"name": "foo",
                                                    "description": "A simple description",
                                                    "price": 100,
                                                    "tax": 10,})):
    
    return item.model_dump()


if __name__ == "__main__":
    uvicorn.run("Video_10:app", host="127.0.0.1", port=8000, reload=True)