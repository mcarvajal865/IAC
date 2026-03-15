from pathlib import Path# Path: permite trabajar con rutas de archivos de forma segura entre sistemas operativos
import typer # Typer: librería para crear interfaces de línea de comandos (CLI)
from rich.console import Console
from rich.table import Table # Rich: librería para mostrar texto y tablas bonitas
from mi_app.models import Company
from mi_app.services import IACService
from mi_app.storage import JSONStorage
from mi_app.exceptions import CompanyAlreadyExistsError

app = typer.Typer() # Crea la aplicación CLI donde se registrarán los comandos
console = Console() # Crea un objeto consola de Rich para mostrar mensajes con formato en la terminal
storage = JSONStorage(Path("data/database.json")) # Crea el sistema de almacenamiento usando el archivo JSON como base de datos
service = IACService(storage) # Crea el servicio de negocio que usará el almacenamiento para manejar las empresas

@app.command("crear-empresa")
def crear_empresa(id: int, nombre: str, nit: str) -> None:
    """
    Comando de la CLI que permite crear una nueva empresa.

    Recibe:
    id: identificador único de la empresa
    nombre: nombre de la empresa
    nit: número de identificación tributaria
    """
    try:
        empresa = Company(id=id, name=nombre, nit=nit)
        # Crea un objeto Company con los datos ingresados

        service.create_company(empresa)
        # Llama al servicio de negocio para guardar la empresa

        console.print("Empresa creada correctamente", style="bold green")
        # Muestra un mensaje de éxito en la terminal

    except CompanyAlreadyExistsError as e:
        # Si ocurre un error porque ya existe una empresa con ese ID

        console.print(f"Error: {e}", style="bold red")
        # Muestra el mensaje de error en la terminal


@app.command("listar-empresas")
def listar_empresas() -> None:
    """
    Comando de la CLI que muestra todas las empresas registradas.
    """

    empresas = service.list_companies()
    # Obtiene la lista de empresas almacenadas en el sistema

    if not empresas:
        # Si no hay empresas registradas

        console.print("No hay empresas registradas", style="yellow")
        # Muestra un mensaje indicando que la lista está vacía
        return

    table = Table(title="Empresas Registradas")
    # Crea una tabla para mostrar las empresas de forma organizada

    table.add_column("ID", justify="right")
    table.add_column("Nombre")
    table.add_column("NIT")
    # Define las columnas de la tabla

    for e in empresas:
        # Recorre cada empresa de la lista

        table.add_row(str(e["id"]), e["name"], e["nit"])
        # Agrega una fila a la tabla con los datos de la empresa

    console.print(table)
    # Muestra la tabla en la terminal


if __name__ == "__main__":
    # Punto de entrada del programa cuando se ejecuta el archivo directamente

    app()
    # Ejecuta la aplicación CLI de Typer



