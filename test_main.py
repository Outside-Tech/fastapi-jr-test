from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Prueba para obtener todos los productos
def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# TODO: Agregar pruebas para el nuevo endpoint de agregar productos
