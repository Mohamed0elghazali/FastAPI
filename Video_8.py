import uvicorn

from pydantic import BaseModel, Field
from typing import Optional
from fastapi import FastAPI, Query, Path, Body

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = Field(None, title="The description of item", max_length=300)
    price: float = Field(1, gt=0, description="the price should be greater than zero.")
    tax: float = Field(None)


@app.post("/items_create")
async def create_items(item: Item = Body(..., embed=True)):
    return item.model_dump()

if __name__ == "__main__":
    uvicorn.run("Video_8:app", host="127.0.0.1", port=8000, reload=True)