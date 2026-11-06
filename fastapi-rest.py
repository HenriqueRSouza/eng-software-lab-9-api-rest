from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ItemIn(BaseModel):
    name: str


# Sample data
items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]


def find_item(item_id: int) -> dict:
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# Get all items
@app.get("/items")
def get_items():
    return {"items": items}


# Get a specific item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item": find_item(item_id)}


# Create a new item
@app.post("/items", status_code=201)
def create_item(data: ItemIn):
    new_id = max((item["id"] for item in items), default=0) + 1
    item = {"id": new_id, "name": data.name}
    items.append(item)
    return {"item": item}


# Update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, data: ItemIn):
    item = find_item(item_id)
    item["name"] = data.name
    return {"item": item}


# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    items.remove(find_item(item_id))
    return {"message": "Item deleted"}
