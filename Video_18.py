import uvicorn

from fastapi import FastAPI, Form, Body, File, UploadFile

app = FastAPI()

@app.post("/file/")
async def create_file(
    fileA: bytes = File(..., description="File A"),
    fileB: UploadFile = File(..., description="File B"),
    token: str = Form(...),
    hello: str = Body(...)):
    
    return {
        "fileA": len(fileA),
        "fileB": fileB.content_type,
        "token": token,
        "hello": hello
    }



if __name__ == "__main__":
    uvicorn.run("Video_18:app", host="127.0.0.1", port=8000, reload=True)