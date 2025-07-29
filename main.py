from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model definition
class Item(BaseModel):
    name: str
    price: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Cloud API!"}

# POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
