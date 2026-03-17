# Arquitectura del proyecto

El proyecto está organizado en diferentes módulos para separar responsabilidades y mantener el código más claro, ordenado y fácil de mantener.

La aplicación sigue una estructura modular donde cada archivo cumple una función específica dentro del sistema.

---

## main.py

El archivo `main.py` es el punto de entrada del programa.

Aquí se define la **interfaz de línea de comandos (CLI)** usando la librería **Typer**.  
Desde este archivo el usuario puede ejecutar comandos para interactuar con el sistema.

Las principales funciones de `main.py` son:

- recibir comandos desde la terminal
- llamar a los métodos del servicio `IACService`
- mostrar la información en consola con **Rich**
- manejar errores mediante excepciones

`main.py` no contiene la lógica del negocio directamente. Su trabajo es conectar al usuario con las funciones principales del sistema.

---

## src/iac

La carpeta `src/iac` contiene la lógica principal de la aplicación.

Dentro de esta carpeta se encuentran los módulos que manejan:

- los modelos de datos
- la lógica del negocio
- el almacenamiento
- las excepciones personalizadas

Esta organización ayuda a que el proyecto sea más limpio y más fácil de entender.

---

## services.py

El archivo `services.py` contiene la lógica principal del sistema.

Aquí está la clase `IACService`, que se encarga de realizar las operaciones del CRUD, por ejemplo:

- crear empresas
- listar empresas
- actualizar empresas
- eliminar empresas
- agregar productos a una empresa
- listar productos
- actualizar productos
- eliminar productos
- agregar servicios a una empresa
- listar servicios
- actualizar servicios
- eliminar servicios

Este archivo funciona como la capa intermedia entre la interfaz del usuario y el almacenamiento de los datos.

---

## models.py

El archivo `models.py` define las estructuras de datos que usa el sistema.

En este módulo se encuentran las clases:

- `Company`
- `Product`
- `Service`

Estas clases representan las entidades principales del proyecto y permiten trabajar la información de forma organizada.

---

## storage.py

El archivo `storage.py` se encarga de guardar y cargar la información.

Aquí se define:

- `StorageInterface`, que representa el contrato de almacenamiento
- `JSONStorage`, que implementa ese contrato usando un archivo JSON

Gracias a esto, el sistema puede persistir los datos sin depender directamente de una base de datos más compleja.

---

## Flujo general del sistema

El funcionamiento general del proyecto sigue este proceso:

```mermaid
flowchart LR
    A[Usuario en la terminal] --> B[CLI en main.py]
    B --> C[IACService en services.py]
    C --> D[JSONStorage en storage.py]
    D --> E[Archivo database.json]