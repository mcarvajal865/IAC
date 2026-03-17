# Persistencia de datos

En este proyecto, la información no se guarda en una base de datos tradicional, sino en un archivo **JSON**.

Esto permite manejar los datos de forma sencilla y fácil de entender.

---

## ¿Dónde se guardan los datos?

Todos los datos del sistema se almacenan en el archivo:

## data/database.json

# Persistencia de datos

En este proyecto, la información no se guarda en una base de datos tradicional, sino en un archivo **JSON**.

Esto permite manejar los datos de forma sencilla y fácil de entender.

---

## ¿Dónde se guardan los datos?

Todos los datos del sistema se almacenan en el archivo:


Este archivo funciona como una pequeña base de datos donde se guarda toda la información de las empresas, productos y servicios.

---

## ¿Qué tipo de información se guarda?

El archivo JSON contiene una lista de empresas, y cada empresa tiene:

- ID
- nombre
- NIT
- lista de productos
- lista de servicios

Un ejemplo de cómo se ve la información:

```json
{
  "companies": [
    {
      "id": 1,
      "name": "Empresa Ejemplo",
      "nit": "123456",
      "products": [
        {
          "id": 1,
          "name": "Producto A",
          "price": 100.0,
          "stock": 10
        }
      ],
      "services": [
        {
          "id": 1,
          "name": "Servicio A",
          "price": 50.0
        }
      ]
    }
  ]
}
```
## ¿Cómo lee los datos la aplicación?

Cuando se ejecuta un comando, la aplicación usa la clase JSONStorage para cargar la información.

El proceso es:

- Se abre el archivo *database.json*.

- Se leen los datos.

- Se convierten en estructuras que el programa puede usa.

Esto se hace a través del método:

```json
load()
```

## ¿Cómo se escriben los datos?

Cuando el usuario crea, actualiza o elimina información, el sistema:

- modifica los datos en memoria

- usa la clase JSONStorage

- guarda los cambios en el archivo JSON

Esto se hace con el método:

```json
save(data)
```

## ¿Por qué usar JSON?

Se usa JSON porque:

- es fácil de leer.

- es simple de modificar.

- no requiere instalación de bases de datos.

- es ideal para proyectos pequeños o educativos.

Esto permite que la aplicación mantenga la información incluso después de cerrarse


