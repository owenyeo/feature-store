from enum import Enum
from fastapi import FastAPI

class catEnum(str, Enum):
    dog = "dog"
    fish = "fish"
    hell_yeah = "hell yeah"

app = FastAPI()

@app.get("/")
async def root():
    return {'Message': 'wassup'}

@app.get("/models/{cat_name}")
async def get_cat(cat_name: catEnum):
    if cat_name is catEnum.fish:
        return {"model_name": cat_name, "message": "bloop bloop"}
    elif cat_name is catEnum.dog:
        return {'model_name': cat_name, "message": "ARF ARF"}
    else:
        return {'model_name': cat_name, "message": "hell yeah"}
    

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]