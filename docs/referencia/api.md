# Referencia de la API

En esta sección se explica la parte técnica del proyecto.  
Aquí se muestran las clases principales del sistema y qué hace cada una.

El objetivo es entender cómo está organizado el código y cómo interactúan los diferentes componentes del sistema.

---

# Servicio principal

El módulo `services` contiene la lógica principal del programa.

La clase **IACService** se encarga de manejar todas las operaciones del sistema, como crear empresas, eliminarlas o modificar su información.  
También permite gestionar los productos y servicios que pertenecen a cada empresa.

::: iac.services.IACService

---

# Modelos

El módulo `models` contiene las clases que representan la información que maneja el sistema.

Estas clases sirven para organizar los datos de forma clara dentro del programa.

## Company

La clase **Company** representa una empresa dentro del sistema.  
Cada empresa tiene un identificador, un nombre y un NIT.

Además, cada empresa puede tener una lista de productos y una lista de servicios.

::: iac.models.Company

## Product

La clase **Product** representa un producto que pertenece a una empresa.

Un producto tiene información como su identificador, nombre, precio y la cantidad disponible en inventario.

::: iac.models.Product

## Service

La clase **Service** representa un servicio que ofrece una empresa.

Incluye datos como el identificador, el nombre del servicio, una descripción y su precio.

::: iac.models.Service

---

# Almacenamiento de datos

El módulo `storage` se encarga de guardar y cargar la información del sistema.

Para este proyecto se usa un archivo **JSON** como base de datos simple.

## StorageInterface

Define las funciones básicas que cualquier sistema de almacenamiento debería tener, como cargar y guardar datos.

::: iac.storage.StorageInterface

## JSONStorage

Es la implementación que realmente se usa en el proyecto.  
Esta clase lee los datos desde un archivo JSON y guarda los cambios que se hacen en el sistema.

::: iac.storage.JSONStorage

---

# Excepciones

El módulo `exceptions` contiene los errores personalizados del sistema.

Estas excepciones ayudan a manejar situaciones en las que algo no sale como se espera.

## IACError

Es la excepción base del sistema.  
Las demás excepciones heredan de esta.

::: iac.exceptions.IACError

## CompanyNotFoundError

Se usa cuando se intenta buscar una empresa que no existe.

::: iac.exceptions.CompanyNotFoundError

## ProductNotFoundError

Se lanza cuando un producto no se encuentra dentro de una empresa.

::: iac.exceptions.ProductNotFoundError

## ServiceNotFoundError

Se usa cuando un servicio no existe dentro de una empresa.

::: iac.exceptions.ServiceNotFoundError

## DuplicateCompanyError

Ocurre cuando se intenta registrar una empresa que ya existe en el sistema.

::: iac.exceptions.DuplicateCompanyError

## InvalidCompanyDataError

Se lanza cuando los datos de la empresa no son válidos o están incompletos.

::: iac.exceptions.InvalidCompanyDataError

## DuplicateProductError

Se usa cuando se intenta registrar un producto que ya existe.

::: iac.exceptions.DuplicateProductError

## DuplicateServiceError

Se usa cuando se intenta registrar un servicio que ya existe.

::: iac.exceptions.DuplicateServiceError