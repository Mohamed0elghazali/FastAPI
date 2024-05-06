import time
import uvicorn

from datetime import datetime, timedelta
from uuid import UUID
from fastapi import FastAPI, Body

app = FastAPI()


@app.post("/items/{item_id}")
async def create_items(
    item_id: UUID,
    start_date: datetime = Body(None),
    end_date: datetime = Body(None),
    process_after: timedelta = Body(None)
    ):
    start_process = start_date + process_after
    duration = end_date - start_process
    return {
        "item_id": item_id,
        "start_date": start_date,
        "end_date": end_date,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration
    }

if __name__ == "__main__":
    uvicorn.run("Video_11:app", host="127.0.0.1", port=8000, reload=True)