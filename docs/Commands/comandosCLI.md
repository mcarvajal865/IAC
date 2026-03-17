# 💻 Uso del Sistema (CLI)

El sistema se ejecuta desde la terminal utilizando una interfaz de línea de comandos (CLI).

Cada comando permite realizar una acción específica dentro del sistema, como crear empresas, gestionar productos o manejar servicios.

---

## 🏢 Gestión de Empresas
### Crear empresa
Crea una nueva empresa con ID, nombre y NIT:


```bash
uv run python main.py create-company 1 "IAC SAS" "900123456" 
```
### Listar empresas registradas

Muestra todas las empresas almacenadas en el sistema:

```bash
uv run python main.py list-companies
```

### Actualizar una empresa
Modifica el nombre y el NIT de una empresa existente:
```bash
uv run python main.py update-company 1 "New IAC" "900999999"
```

### Eliminar una empresa
Elimina una empresa según su ID:
```bash
uv run python main.py delete-company 1
```

## 📦Gestión de Productos

### Agregar un producto a una empresa
Agrega un producto a una empresa:
```bash
uv run python main.py add-product 1 101 "Laptop" 2500 10
```

### Listar productos de una empresa:
Muestra todos los productos de una empresa:
```bash
uv run python main.py list-products 1
```

### Actualizar un producto:
Modifica el nombre y precio de un producto:
```bash
uv run python main.py update-product 1 101 "Laptop Pro" 3200
```

### Eliminar un producto:
Elimina un producto de una empresa:
```bash
uv run python main.py delete-product 1 101
```
## 🛠️ Gestión de Servicios

### Agregar un servicio:
Agrega un servicio a una empresa:
```bash
uv run python main.py add-service 1 201 "Consultoria" 500
```
### Listar servicios de una empresa:
Muestra todos los servicios de una empresa:
```bash
uv run python main.py list-services 1
```

### Actualizar un servicio:
Modifica el nombre y precio de un servicio:
```bash
uv run python main.py update-service 1 201 "Consultoria Premium" 800
```

### Eliminar un servicio:
Elimina un servicio de una empresa:
```bash
uv run python main.py delete-service 1 201
```