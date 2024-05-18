from typing import Optional
import uvicorn

from fastapi import Body, Depends, FastAPI, HTTPException, Header, status
from typing import Optional

app = FastAPI()

async def verify_token(x_token: str = Header(...)):
    if x_token != "fake_secret_token":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X_token header invalid") 

async def verify_key(x_key: str = Header(...)):
    if x_key != "fake_secret_key":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X_key header invalid") 


@app.post("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return {"Item_1": "PC"}

if __name__ == "__main__":
    uvicorn.run("Video_25:app", host="127.0.0.1", port=8000, reload=True)