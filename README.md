# 🚀 FastAPI Junior Test

Este es un pequeño proyecto en FastAPI para evaluar habilidades básicas de desarrollo backend.


## 📂 Instrucciones

1. Clona este repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/fastapi-jr-test.git
   cd fastapi-jr-test

## 📌 Tareas para la prueba técnica

1. **Agregar un nuevo endpoint `POST /items/add`**  
   - Recibe un producto en JSON con `name` y `price`.
   - Asigna un ID único y lo almacena en `items`.
   - Si falta algún campo, devuelve un `400 Bad Request`.

2. **Mejorar `GET /items/{item_id}`**  
   - Si el producto no existe, debe devolver un mensaje detallado en JSON, y el respectivo codigo de error `404 Not Found`.

3. **Escribir pruebas unitarias para `POST /items/add`**  
   - Validar que el producto se agrega correctamente.
   - Validar que si falta un campo, devuelve `400 Bad Request`.

4. **(Bonus) Evitar productos duplicados**  
   - Si el nombre del producto ya existe en `items`, devolver `400 Bad Request`.

5. **Implementar `DELETE /items/{item_id}`**
   - Si el producto existe, debe eliminarlo de `items`.
   - Si el producto no existe, debe devolver `404 Not Found`.
   - **Bonus:** Agregar una prueba unitaria en `test_main.py`.

6. **Implementar `PUT /items/{item_id}`**
   - Si el producto existe, debe actualizar su `name` y `price`.
   - Si el producto no existe, debe devolver `404 Not Found`.
   - **Bonus:** Validar que el `price` no pueda ser negativo (`400 Bad Request`).
