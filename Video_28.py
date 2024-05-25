import time
import uvicorn

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# A "middleware" is a function that works with every request before it is processed by any specific path operation. 
# And also with every response before returning it.

class MyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

app.add_middleware(MyMiddleware)

@app.get("/items")
async def get_items():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("Video_28:app", host="127.0.0.1", port=8000, reload=True)