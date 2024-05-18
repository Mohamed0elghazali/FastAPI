from typing import Optional
import uvicorn

from fastapi import Body, Depends, FastAPI
from typing import Optional

app = FastAPI()

def query_extractor(q: Optional[str] = None):
    return q

def query_or_body_extractor(q: str = Depends(query_extractor), body_data: str = Body(None)):
    if q:
        return q
    return body_data

@app.post("/items/")
async def read_items(query_or_body = Depends(query_or_body_extractor)):
    return {"query_or_body": query_or_body}

if __name__ == "__main__":
    uvicorn.run("Video_24:app", host="127.0.0.1", port=8000, reload=True)