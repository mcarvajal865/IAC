from pathlib import Path# Path: permite trabajar con rutas de archivos de forma segura entre sistemas operativos
import typer # Typer: librería para crear interfaces de línea de comandos (CLI)
from rich.console import Console
from rich.table import Table # Rich: librería para mostrar texto y tablas bonitas
from mi_app.models import Company
from mi_app.services import IACService
from mi_app.storage import JSONStorage
from mi_app.exceptions import DuplicateCompanyError

app = typer.Typer() # Crea la aplicación CLI donde se registrarán los comandos
console = Console() # Crea un objeto consola de Rich para mostrar mensajes con formato en la terminal
storage = JSONStorage(Path("data/database.json")) # Crea el sistema de almacenamiento usando el archivo JSON como base de datos
service = IACService(storage) # Crea el servicio de negocio que usará el almacenamiento para manejar las empresas

@app.command("crear-empresa")
def crear_empresa(id: int, nombre: str, nit: str) -> None:
    """
    Comando de la CLI que permite crear una nueva empresa.
    Recibe:
    id, nombre, nit
    """
    try:
        empresa = Company(id=id, name=nombre, nit=nit)
        service.create_company(empresa)
        console.print("Empresa creada correctamente", style="bold green")
        # Muestra un mensaje de éxito en la terminal

    except DuplicateCompanyError as e:
        console.print(f"Error: {e}", style="bold red")


@app.command("listar-empresas")
def listar_empresas() -> None:
    """
    Comando de la CLI que muestra todas las empresas registradas.
    """
    empresas = service.list_companies()
    # Obtiene la lista de empresas almacenadas en el sistema

    if not empresas:
        console.print("No hay empresas registradas", style="yellow")
        return

    table = Table(title="Empresas Registradas", style="cyan")

    table.add_column("ID", justify="right", style="magenta")

    table.add_column("Nombre", style="green")

    table.add_column("NIT", style="yellow")

    for e in empresas:
        table.add_row(
            str(e["id"]),
            e["name"],
            e["nit"],
        )

    console.print(table)

if __name__ == "__main__":
    # Punto de entrada del programa cuando se ejecuta el archivo directamente

    app()
    # Ejecuta la aplicación CLI de Typer



