# IAC
Proyecto para Codigo Limpio

Con este proyecto se busca desarrollar un sistema que optimice la gestión de la empresa IAC, ya que actualmente su base de datos se administra mediante Microsoft Office. Aunque es una herramienta sólida y funcional, su interfaz puede resultar poco intuitiva para usuarios no expertos, lo que dificulta la eficiencia en los procesos diarios.

Esta propuesta tiene como objetivo modernizar y mejorar la gestión interna de la empresa, implementando un sistema más ágil, intuitivo y eficiente, que facilite el trabajo de los usuarios y optimice los procesos administrativos.

# 🚀 Características

- ### *Arquitectura Modular:*
División clara entre modelos de datos, lógica de negocio, almacenamiento y excepciones.
- ### *Persistencia JSON:*
Implementaremos un sistema de guardadp y carga de datos local mediante archivos tipo *.json.*

- ### *Manejo de Errores:*
Usaremos jerarquia de excepciones para hayar errores especificos como *ids duplicados,stock insuficiente, empresa no encontrada, entre otros...*
- ### *Tipado Estático:*
Usamos *dataclasses* y *typing* para hacer el código más legible y menos propenso a errores.

# 🚀 Funcionalidades Principales
El sistema permite realizar las siguientes operaciones a través de una interfaz de línea de comandos (CLI):

- ### Gestión de Empresas: 
Agregar nuevas empresas al sistema.

- ### Gestión de Catálogo: 
Registrar, modificar y eliminar servicios y productos asociados a cada empresa.


- ### Visualización: 
Listar todas las empresas registradas junto con sus respectivos servicios, productos o ventas realizadas.


- ### Persistencia Local: 
Almacenamiento de información en archivos de formato JSON, sin depender de sistemas de bases de datos externos.

# 📁 Estructura de Capas del Código

| Capa | Archivo | Responsabilidad Principal |
| :--- | :--- | :--- |
| **Models** | `models.py` | [cite_start]Define las entidades `Company`, `Product` y `Service` con tipado estático[cite: 1, 12]. |
| **Storage** | `storage.py` | [cite_start]Gestiona la persistencia de datos y la interfaz de lectura/escritura de archivos **JSON**[cite: 9, 12]. |
| **Services** | `services.py` | [cite_start]Contiene la lógica de negocio, validaciones y reglas de gestión empresarial[cite: 11, 12]. |
| **Exceptions** | `exceptions.py` | [cite_start]Define errores personalizados para un manejo adecuado de excepciones[cite: 16]. |
| **CLI** | `main.py` | [cite_start]Interfaz de línea de comandos para la interacción con el usuario desde la terminal[cite: 12, 14]. |

# 🛠️ Detalles Técnicos y Alcance
Orientamos el proyecto a fines académicos, para demuestrar la implementación de buenas prácticas de desarrollo en Python:


- ### Tipado Estático: 
Usamos *typing* y *dataclasses* para mayor solidez.


- ### Manejo de Excepciones: 
Sistema personalizado de errores (ej. CompanyNotFoundError, DuplicateCompanyError).


- ### Interfaz:
Interacción exclusiva mediante la terminal (CLI), sin interfaz gráfica.


- ### Pruebas: 
Estructura preparada para la implementación de pruebas unitarias

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