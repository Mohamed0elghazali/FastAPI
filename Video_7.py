import uvicorn

from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, Query, Path, Body

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float

## using the body parameter
# you can use str or int or any other datatype or model using body to
# tell fastapi that this parameter is a body pareameter.
# but if you define the parameter as dict or any other pydantic model
# it will understand that it`s a body parameter without body keyword.


@app.post("/items/{item_id}")
async def items(*,
                item_id: int = Path(...),
                q: str = Query(...),
                item: Item,
                details: str = Body(..., embed=True),
                nums: int = Body(...)):
    
    results = {"item_id": item_id, "item": item, "detail": details, "nums": nums}
    if q:
        results.update({"q": q})
    return results

# when you only have a single item body parameter from a Pydantic model Item.
# By default, FastAPI will then expect its body directly.
# But if you want it to expect a JSON with a key item and inside of it the model contents.
# as it does when you declare extra body parameters.
# you can use the special Body parameter embed=True

@app.post("/items_create")
async def create_items(item: Item = Body(..., embed=True)):
    return item.model_dump()

if __name__ == "__main__":
    uvicorn.run("Video_7:app", host="127.0.0.1", port=8000, reload=True)