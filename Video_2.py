import uvicorn

from enum import Enum
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def list_items():
    return {"message": "You are in the list items endpoint."}


# if you have two endpoints with same name, one is static and the other is dynamic
# make sure to put the static first then the dynamic to not facing errors or logical errors.
# like this example if try to hit items/all ---> it will go to the first endpoint 
# and you send string and it accept int so it will raise error.
# so you have to swap them.
@app.get("/items/all")
async def get_item():
    return {"detail": f"You choose item: all"}

# trying the path parameter 
# you can also tell fastapi (pydantic) the datatype of the comming variable
# and it will raise error if you send different datatype.
@app.get("/items/{item_name}")
async def get_item(item_name: int):
    return {
        "detail": f"You choose item: {item_name}", 
        "message": "You are in the get item endpoint."
        }

class AnimalEnum(Enum):
    Cat = "cat"
    Dog = "Dog"
    Duck = "Duck"

@app.get("/chooseAnimal/{animal}")
async def get_animal(animal: AnimalEnum):
    if animal == AnimalEnum.Cat:
        return {"details": f"You choose {animal.value}, You are nice."}
    
    elif animal.value == AnimalEnum.Dog.value:
        return {"details": f"You choose {animal.value}, You are not nice."}
    
    elif animal.value == AnimalEnum.Duck.value:
        return {"details": f"You choose {animal.value}, You are farmer."}
    

if __name__ == "__main__":
    uvicorn.run("Video_2:app", host="127.0.0.1", port=8000, reload=True)