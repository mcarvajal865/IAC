# 🚀 Primeros pasos

En esta sección se explica cómo instalar y ejecutar el proyecto paso a paso.

---

## 🧾 Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.11 o superior
- Git
- uv (gestor de dependencias)

---

## 📥 Clonar el repositorio

Clona el proyecto desde GitHub:

```bash
git clone https://github.com/TU_USUARIO/IAC.git
```
Luego entra a la carpeta del proyecto:
```bash
cd IAC
```
---
## 📦 Instalar dependencias con uv

El proyecto utiliza uv para manejar el entorno virtual y las dependencias.

Ejecuta:
```bash
uv sync
```
Esto hará:

- crear el entorno virtual automáticamente

- instalar todas las dependencias necesarias

---

## ▶️ Ejecutar comandos

La aplicación funciona mediante comandos en la terminal.

Por ejemplo, para listar empresas:

```bash
uv run python main.py list-companies
```
---


## 🧪 Primer uso del CLI

Para ver todos los comandos disponibles en la aplicación, ejecuta:

```bash
uv run python main.py --help
```

Esto mostrará todas las opciones disponibles en la CLI, como crear empresas, listar productos o gestionar servicios.

