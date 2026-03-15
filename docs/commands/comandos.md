# 💻 Uso del Sistema (CLI)

El sistema se ejecuta desde la terminal utilizando una interfaz de línea de comandos (CLI).

## Gestión de Empresas

Crear una empresa:

```bash
uv run python main.py create-company 1 "IAC SAS" "900123456" 
```
Listar empresas registradas:

```bash
uv run python main.py list-companies
```

Actualizar una empresa:
```bash
uv run python main.py update-company 1 "New IAC" "900999999"
```

Eliminar una empresa:
```bash
uv run python main.py delete-company 1
```

## Gestión de Productos

Agregar un producto a una empresa:
```bash
uv run python main.py add-product 1 101 "Laptop" 2500 10
```

Listar productos de una empresa:
```bash
uv run python main.py list-products 1
```

Actualizar un producto:
```bash
uv run python main.py update-product 1 101 "Laptop Pro" 3200
```

Eliminar un producto:
```bash
uv run python main.py delete-product 1 101
```
## Gestión de Servicios

Agregar un servicio:
```bash
uv run python main.py add-service 1 201 "Consultoria" 500
```
Listar servicios de una empresa:
```bash
uv run python main.py list-services 1
```

Actualizar un servicio:
```bash
uv run python main.py update-service 1 201 "Consultoria Premium" 800
```

Eliminar un servicio:
```bash
uv run python main.py delete-service 1 201
```