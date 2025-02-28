from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Junior Test",
    description="API para la prueba técnica de backend junior con FastAPI.",
    version="1.0.0"
)

# Simulación de base de datos en memoria
items = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Mouse", "price": 49.99},
    3: {"name": "Keyboard", "price": 79.99}
}

# Modelo de datos con Pydantic
class Item(BaseModel):
    name: str
    price: float

@app.get("/items/", tags=["Items"], summary="Obtener todos los productos")
def get_items():
    """
    Retorna una lista de todos los productos disponibles.
    """
    return items

@app.get("/items/{item_id}", tags=["Items"], summary="Obtener un producto por ID")
def get_item(item_id: int):
    """
    Retorna un producto específico basado en su ID.

    - **item_id**: ID del producto a buscar.
    - **Retorna**: Objeto con nombre y precio si el producto existe.
    """
    if item_id in items:
        return items[item_id]

# TODO: Agregar un endpoint para agregar productos
