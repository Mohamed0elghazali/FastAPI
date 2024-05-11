import uvicorn

from fastapi import FastAPI, Form, Body

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}

@app.post("/login_json/")
async def login_json(username: str = Body(...), password: str = Body(...)):
    return {"username": username, "password": password}

@app.post("/login_both/")
async def login_both(username: str = Form(...), password: str = Body(...)):
    return {"username": username, "password": password}

if __name__ == "__main__":
    uvicorn.run("Video_16:app", host="127.0.0.1", port=8000, reload=True)