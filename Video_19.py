from pydantic import BaseModel
import uvicorn

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.encoders import jsonable_encoder

from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

items = {"Item_1": "PC"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found", headers={"X-Error": "Some thing went wrong"})
    return {"item": items[item_id]}

class ItemNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name
        
@app.exception_handler(ItemNotFoundException)
async def item_not_found_exception_handler(request: Request, exce: ItemNotFoundException):
    return JSONResponse(status_code=status.HTTP_418_IM_A_TEAPOT, content={"message": f"[{exce.name}] input, caused an error !"})

@app.get("/items/ownexcept/")
async def get_item(keyword: str):
    if keyword != "PC":
        raise ItemNotFoundException(name=keyword)
    return {"Keyword": keyword}

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exce: RequestValidationError):
#     return PlainTextResponse(str(exce), status_code=status.HTTP_400_BAD_REQUEST)

# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exce):
#     return PlainTextResponse(str(exce.detail), status_code=exce.status_code)

@app.get("/validation_items/{item_id}")
async def read_validaiton_items(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="Try again...")
    return {"item_id": item_id}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler2(request: Request, exce: RequestValidationError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"detail": exce.errors(), "body": exce.body}))

class Item(BaseModel):
    title: str
    size: int
    
@app.post("/items/")
async def create_item(item: Item):
    return item

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exce: StarletteHTTPException):
    print(f"An HTTP error: {repr(exce)}")
    return await http_exception_handler(request, exce)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exce: RequestValidationError):
    print(f"The client sent invalid data: {repr(exce)}")
    return await request_validation_exception_handler(request, exce)

@app.get("/qwi_items/{item_id}")
async def read_qwi_items(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="No, It`s not the right answer...")
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run("Video_19:app", host="127.0.0.1", port=8000, reload=True)