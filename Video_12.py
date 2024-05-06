import uvicorn

from fastapi import FastAPI, Cookie, Header

app = FastAPI()


@app.get("/items")
async def items(
    cookie_id: str = Cookie(None),
    accept_encoding: str = Header(None),
    sec_ch_ua: str = Header(None),
    user_agent: str = Header(None),
    x_token: list[str] = Header(None),
    ):
    return {
        "cookie_id": cookie_id,
        "accept_encoding": accept_encoding,
        "sec_ch_ua": sec_ch_ua,
        "user_agent": user_agent,
        "x_token": x_token,
    }

if __name__ == "__main__":
    uvicorn.run("Video_12:app", host="127.0.0.1", port=8000, reload=True)