# User Management CLI

Bienvenido a la documentación oficial de **User Management CLI**, una aplicación
de línea de comandos desarrollada en Python para gestionar usuarios utilizando
principios de **Clean Code**, **Testing** y **Arquitectura modular**.

Este proyecto fue diseñado como material educativo para aprender buenas prácticas
de desarrollo en Python.

---

## ✨ Características

- CLI moderna basada en **Typer**
- Persistencia de datos en archivo JSON
- Arquitectura modular (`src layout`)
- Pruebas unitarias con `pytest`
- Uso de **mocks** para aislar dependencias
- Excepciones personalizadas
- Principios de diseño **SOLID**
- Documentación generada automáticamente

---

## 🧠 Conceptos que aprenderás con este proyecto

!!! info "Conceptos clave"

    - Diseño limpio de funciones
    - Encapsulamiento
    - Testing con mocks
    - Excepciones de dominio
    - Separación de responsabilidades
    - Documentación profesional

---


## 📦 Arquitectura del sistema

El proyecto sigue una arquitectura simple por capas.

``` mermaid
flowchart LR
    CLI[CLI - Typer] --> Service[UserService]
    Service --> Storage[JSONStorage]
    Service --> Model[User Model]
    Storage --> Database[(database.json)]
```


## 📁 Estructura del proyecto

```bash
IAC/
│
├── data/
│   └── database.json
│
├── docs
│     └── commands
│     │    └── comandos.md
│     └── indes.md
│     └── readme.md
│
└── main.py
└──mkdocs.yml
└──poetry.lock
└── pyproject.toml
└── pyproject.toml.save
├── src/
│   ├──  iac/
│   │      ├── __init__.py
│   │      ├── __pycache__
│   │      ├── database.json
│   │      ├── exceptions.py
│   │      ├── implementacion.py
│   │      ├── models.py
│   │      ├── services.py
│   │      └── storage.py
│   │
│   └── mi app
├── tests/
│   ├── __pycache__
│   │   └── test_iac_service.cpython-312-pytest-9.0.2.pyc     
│   └── test_iac_service.py
│
└── UV.LOCK
```

## 🚀 Flujo general de ejecución

``` mermaid
sequenceDiagram

participant CLI
participant Service
participant Storage
participant Database

CLI->>Service: create_user()
Service->>Storage: load()
Storage->>Database: read JSON
Database-->>Storage: data
Storage-->>Service: users
Service->>Service: validate rules
Service->>Storage: save()
Storage->>Database: write JSON
```

## 📚 Documentación

Esta documentación está dividida en tres secciones principales:

| Sección         | Descripción               |
| --------------- | ------------------------- |
| Guía de Usuario | Cómo usar la aplicación   |
| Instalación     | Cómo instalar el proyecto |
| API             | Documentación del código  |

