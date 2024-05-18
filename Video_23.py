import uvicorn

from fastapi import Depends, FastAPI

app = FastAPI()

fake_items_db = [{"Item_Name": "PC"}, {"Item_Name": "PS5"}, {"Item_Name": "TV"}]

class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
async def read_items(common = Depends(CommonQueryParams)):
    response = {}
    if common.q:
        response.update({"q": common.q})
    items = fake_items_db[common.skip : common.skip + common.limit]
    response.update({"items": items}) 
    return response

if __name__ == "__main__":
    uvicorn.run("Video_23:app", host="127.0.0.1", port=8000, reload=True)