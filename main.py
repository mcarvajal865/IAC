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

#Company

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

@app.command()
def delete_company(id:int):
    """Elimina una empresa, por id"""
    service.delete_company(id)
    typer.echo("Empresa eliminada exitosamente")

@app.command()
def update_company(id: int, name: str, nit: str):
    """Actualiza nombre y NIT de una empresa existente"""
    service.update_company(id, name, nit)
    typer.echo("Empresa actualizada correctamente")

#Productos

@app.command()
def add_product(company_id: int, product_id: int, name: str, price: float):
    """Agregar producto"""
    product_data = {"id": product_id, "name": name, "price": price}
    service.add_product_to_company(company_id, product_data)
    typer.echo("Producto agregado")

@app.command()
def list_products(company_id: int):
    """Listar productos"""

    products = service.list_products(company_id)
    if not products:
        console.print("No hay productos registrados", style="bold red")
        return

    table = Table(title=f"Productos - Empresa {company_id}")
    table.add_column("ID", style="pink")
    table.add_column("Nombre", style="magenta")
    table.add_column("Precio", style="green")

    for product in products:
        table.add_row(str(product["id"]), product["name"], str(product["price"]))
    console.print(table)

@app.command()
def update_product(company_id: int, product_id: int, name: str, price: float):
    """Modificar producto"""
    service.update_product_in_company(company_id, product_id, name, price)
    typer.echo("Producto actualizado")

@app.command()
def delete_product(company_id: int, product_id: int):
    """Eliminar producto"""
    service.delete_product_from_company(company_id, product_id)
    typer.echo("Producto eliminado")

#Servicios

@app.command()
def add_service(company_id: int, service_id: int, name: str, price: float):
    """Agregar servicio"""
    service_data = {"id": service_id, "name": name, "price": price}
    service.add_service_to_company(company_id, service_data)
    typer.echo("Servicio agregado")

@app.command()
def list_services(company_id: int):
    """Listar servicios"""

    services = service.list_services(company_id)
    if not services:
        console.print("No hay servicios registrados", style="bold red")
        return

    table = Table(title=f"Servicios - Empresa {company_id}")
    table.add_column("ID", style="cyan")
    table.add_column("Nombre", style="magenta")
    table.add_column("Precio", style="green")

    for service_item in services:
        table.add_row(str(service_item["id"]), service_item["name"], str(service_item["price"]))
    console.print(table)

@app.command()
def update_service(company_id: int, service_id: int, name: str, price: float):
    """Modificar servicio"""
    service.update_service_in_company(company_id, service_id, name, price)
    typer.echo("Servicio actualizado")


if __name__ == "__main__":
    """Corre la aplicaion CLI"""
    app()
