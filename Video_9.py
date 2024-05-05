import uvicorn

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from fastapi import FastAPI, Query, Path, Body

app = FastAPI()

class Image(BaseModel):
    name: str
    url: HttpUrl

class Item(BaseModel):
    name: str
    description: str = Field(None, title="The description of item", max_length=300)
    price: float = Field(1, gt=0, description="the price should be greater than zero.")
    tax: float = Field(None)
    keywords: set[str] = () # to remove duplicates
    keywords2: set[str] = Field((), max_length=30) # to remove duplicates
    image: Image


class Offer(BaseModel):
    name: str
    description: str
    price: float
    item: list[Item]

@app.post("/items_create")
async def create_items(item: Item = Body(..., embed=True)):
    return item.model_dump()

@app.post("/offers")
async def create_offer(offer: Offer = Body(..., embed=True)):
    return offer.model_dump()


# this a simple list of Image objects.
@app.post("/images")
async def send_images(image: list[Image] = Body(..., embed=True)):
    return image


# this a simple dictionanry of keys as int and values as Image object.
@app.post("/simpledicts")
async def simple_dicts(dummy_dict: dict[int, Image] = Body(..., embed=True)):
    return dummy_dict

if __name__ == "__main__":
    uvicorn.run("Video_9:app", host="127.0.0.1", port=8000, reload=True)