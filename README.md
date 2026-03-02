# IAC – Sistema de Gestión Empresarial

# 📖 1. Explicación del Proyecto

IAC es un sistema de gestión empresarial desarrollado en Python con arquitectura modular y principios de código limpio.

# 🎯 Propósito

Modernizar la administración interna de la empresa IAC, reemplazando el uso de herramientas como Microsoft Office por un sistema más estructurado, mantenible y escalable.

# 📦 Alcance

El sistema permite:

- Registrar empresas

- Agregar productos y servicios

- Listar información almacenada

- Persistir datos en archivos JSON

- Manejar errores mediante excepciones personalizadas

- Ejecutar operaciones desde una CLI (Interfaz de Línea de Comandos)

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

# ⚙️ 2. Guía de Instalación (usando uv)

### 1. Clonar el repositorio

git clone https://github.com/mcarvajal865/IAC.git
cd IAC

### 2. Crear entorno virtual e instalar dependencias con uv

uv sync

# 💻 Manual de la CLI

La aplicación se ejecuta mediante:

#### uv run python -m mi_app.cli

# 📌 Ejemplos de comandos

## ➤ Crear empresa
#### uv run python -m mi_app.cli crear-empresa --id 1 --nombre "IAC SAS" --nit "900123456"

## ➤ Listar empresas
#### uv run python -m mi_app.cli listar-empresas

## ➤ Agregar producto
#### uv run python -m mi_app.cli agregar-producto --empresa 1 --id 101 --nombre "Laptop" --precio 2500 --stock 10

## ➤ Agregar servicio
#### uv run python -m mi_app.cli agregar-servicio --empresa 1 --id 201 --nombre "Consultoria" --precio 500

# 🧪 4. Instrucciones de Testing
El proyecto incluye 10 pruebas unitarias desarrolladas con pytest.

Para ejecutarlas:

#### uv run pytest

Si todo funciona correctamente, deberías ver:

#### 10 passed

