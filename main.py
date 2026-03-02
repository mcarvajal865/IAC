from pathlib import Path #Maneja rutas de archivos de forma segura
import typer #Crear CLI facilmente
from rich.console import Console #Imprime bonito
from rich.table import Table #Imprime tablas

from src.iac.models import Company
from src.iac.services import IACService
from src.iac.storage import JSONStorage

app = typer.Typer() #Crea aplicaion CLI
console = Console() #Muestra tablas bonitas

"""Inicializar variables de almacenamiento y servicios"""
storage = JSONStorage(Path("data/database.json"))
service = IACService(storage)

@app.command()
def create_company(id: int, name: str, nit: str) -> str:
    """Crea nueva empresa"""
    company = Company(id = id, name = name, nit = nit)
    service.create_company(company)
    typer.echo("Empresa creada exitosamente")

@app.command()
def list_companies():
    """Lista todas las empresas registradas, usando tablas"""

    companies = service.list_companies()
    if not companies:
        console.print("No hay empresas registradas", style="bold red")
        return

    table = Table(tittle = "Empresas Registradas")
    table.add_column("ID", justify="righ", style="pink")
    table.add_column("Nombre", style="magenta")
    table.add_column("NIT", style="green")

    for company in companies:
        table.add_row(str(company["id"]), company["name"], company["nit"])
    console.print(table)

