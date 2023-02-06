from fastapi import FastAPI, Path, Request, UploadFile, File
from typing import Optional


app = FastAPI()


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you'd like yo view", gt=0, lt=5)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(*, name: Optional[str] = None, test: int):
     for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"Data": "Not found"}