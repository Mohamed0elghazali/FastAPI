import uvicorn

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/file/")
async def create_file(file: bytes = File(...)):
    content = file.decode()
    size = file.__sizeof__()
    return {"content": content, "size": size}

@app.post("/uploadfile/")
async def create_file(file: UploadFile = File(...)):
    file_name = file.filename
    content = await file.read()
    size = file.__sizeof__() 
    return {"filename": file_name, "content": content, "size": size}

@app.post("/files/")
async def create_file(files: list[bytes] = File(...)):
    return {"file": [len(file) for file in files]}

@app.post("/uploadfiles/")
async def create_file(files: list[UploadFile] = File(...)):
    return {"file": [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
    <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
    </body>
    """
    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run("Video_17:app", host="127.0.0.1", port=8000, reload=True)