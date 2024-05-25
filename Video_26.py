from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import uvicorn

from fastapi import Body, Depends, FastAPI, HTTPException, Header, status
from typing import Optional

app = FastAPI()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_user_db = {
    "moh": dict(
        username="moh",
        full_name="moh yoh",
        email="mohyoh@example.com",
        hashed_password="fakehashedsecretpass",
        disabled=False
    ),
    "sand": dict(
        username="sand",
        full_name="sand mark",
        email="sandmark@example.com",
        hashed_password="fakehashedsecretsuperpass",
        disabled=False
    )
}

def fake_hash_password(password: str):
    return f"fakehashed{password}"

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

class UserInDB(User):
    hashed_password: str

@app.post("/token/")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_user_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid Username or Password.")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Invalid Username or Password.')
    return {"access_token": user.username, "token_type": "bearer"}

def get_user(db, username:str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
 
def fake_decode_token(token):
    return get_user(fake_user_db, token)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid authentication credentials",
                            headers={"www-Authenticate": "Bearer"})
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400,
                            detail="Inactive user.")
    return current_user

## operation procedures
# first, you authenticate using the route token or swagger form.
# second, you authenticate using username (token) and password.
# third, we check the username exist in fake db or not.
# fourth, if not exist raise error, if exist get user data.
# fifth, check the user hashed password with password he entered after being hashed.
# sixth, if similar login successed, if not raise error.

# function chain:
# get_me --> get_current_active_user --> get_current_user --> oauth_scheme
# --> fake_decode_token --> get_user

@app.get("/users/me")
async def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user


if __name__ == "__main__":
    uvicorn.run("Video_26:app", host="127.0.0.1", port=8000, reload=True)