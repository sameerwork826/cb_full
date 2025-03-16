from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

# Sample menu data
menu_items = {
    "italian": [
        {"name": "Pizza Margherita", "price": 12.99},
        {"name": "Pasta Carbonara", "price": 14.99},
        {"name": "Tiramisu", "price": 6.99}
    ],
    "mexican": [
        {"name": "Tacos", "price": 8.99},
        {"name": "Burrito", "price": 10.99},
        {"name": "Quesadilla", "price": 9.99}
    ],
    "indian": [
        {"name": "Butter Chicken", "price": 15.99},
        {"name": "Naan", "price": 3.99},
        {"name": "Biryani", "price": 16.99}
    ]
}

@app.get("/")
def read_root():
    return {"message": "Welcome to our restaurant API"}

@app.get("/cuisines")
def get_cuisines() -> List[str]:
    return list(menu_items.keys())

@app.get("/menu/{cuisine}")
def get_menu_items(cuisine: str) -> Dict:
    cuisine = cuisine.lower()
    if cuisine not in menu_items:
        return {"error": "Cuisine not found"}
    return {"cuisine": cuisine, "items": menu_items[cuisine]}

@app.get("/item/{cuisine}/{item_name}")
def get_item_details(cuisine: str, item_name: str) -> Dict:
    cuisine = cuisine.lower()
    if cuisine not in menu_items:
        return {"error": "Cuisine not found"}
    
    for item in menu_items[cuisine]:
        if item["name"].lower() == item_name.lower():
            return item
    return {"error": "Item not found"}

# Example URLs to try:
# GET http://localhost:8000/                          - Welcome message
# GET http://localhost:8000/cuisines                  - List all cuisines
# GET http://localhost:8000/menu/italian              - Get Italian menu items
# GET http://localhost:8000/menu/mexican              - Get Mexican menu items
# GET http://localhost:8000/menu/indian               - Get Indian menu items
# GET http://localhost:8000/item/italian/pizza%20margherita    - Get specific item details
# GET http://localhost:8000/item/mexican/tacos        - Get specific item details
# GET http://localhost:8000/item/indian/naan          - Get specific item details




