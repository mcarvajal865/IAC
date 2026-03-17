from pathlib import Path
import typer
from rich.console import Console
from rich.table import Table
from iac.models import Company
from iac.services import IACService
from iac.storage import JSONStorage
from iac.exceptions import (
    CompanyNotFoundError,
    DuplicateCompanyError,
    InvalidCompanyDataError,
    ProductNotFoundError,
    ServiceNotFoundError,
)

app = typer.Typer()
console = Console()
storage = JSONStorage(Path("data/database.json"))
service = IACService(storage)


@app.command("create-company")
def create_company(company_id: int, name: str, nit: str) -> None:
    """Crea una nueva empresa en el sistema."""
    try:
        company = Company(id=company_id, name=name, nit=nit)
        service.create_company(company)
        console.print("Empresa creada correctamente", style="bold green")
    except (DuplicateCompanyError, InvalidCompanyDataError, ValueError) as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("list-companies")
def list_companies() -> None:
    """Muestra todas las empresas registradas."""
    companies = service.list_companies()

    if not companies:
        console.print("No hay empresas registradas", style="yellow")
        return

    table = Table(
        title="Empresas Registradas",
        header_style="bold cyan",
        border_style="cyan",
    )
    table.add_column("ID", justify="right", style="magenta")
    table.add_column("Name", style="green")
    table.add_column("NIT", style="yellow")

    for company in companies:
        table.add_row(
            str(company["id"]),
            company["name"],
            company["nit"],
        )

    console.print(table)


@app.command("update-company")
def update_company(company_id: int, new_name: str, new_nit: str) -> None:
    """Actualiza el nombre y el NIT de una empresa."""
    try:
        service.update_company(company_id, new_name, new_nit)
        console.print("Empresa actualizada correctamente", style="bold green")
    except (CompanyNotFoundError, ValueError) as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("delete-company")
def delete_company(company_id: int) -> None:
    """Elimina una empresa según su ID."""
    try:
        service.delete_company(company_id)
        console.print("Empresa eliminada correctamente", style="bold green")
    except CompanyNotFoundError as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("add-product")
def add_product(
    company_id: int,
    product_id: int,
    name: str,
    price: float,
    stock: int,
) -> None:
    """Agrega un producto a una empresa."""
    try:
        product_data = {
            "id": product_id,
            "name": name,
            "price": price,
            "stock": stock,
        }
        service.add_product_to_company(company_id, product_data)
        console.print("Producto agregado correctamente", style="bold green")
    except (CompanyNotFoundError, ValueError)  as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("list-products")
def list_products(company_id: int) -> None:
    """Muestra todos los productos de una empresa."""
    try:
        products = service.list_products(company_id)

        if not products:
            console.print("No hay productos registrados", style="yellow")
            return

        table = Table(
            title="Productos Registrados",
            header_style="bold cyan",
            border_style="cyan",
        )
        table.add_column("ID", justify="right", style="magenta")
        table.add_column("Name", style="green")
        table.add_column("Price", style="yellow")
        table.add_column("Stock", style="blue")

        for product in products:
            table.add_row(
                str(product["id"]),
                product["name"],
                str(product["price"]),
                str(product["stock"]),
            )

        console.print(table)
    except CompanyNotFoundError as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("update-product")
def update_product(
    company_id: int,
    product_id: int,
    new_name: str,
    new_price: float,
) -> None:
    """Actualiza el nombre y el precio de un producto."""
    try:
        service.update_product_in_company(
            company_id,
            product_id,
            new_name,
            new_price,
        )
        console.print("Producto actualizado correctamente", style="bold green")
    except (CompanyNotFoundError, ProductNotFoundError, ValueError) as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("delete-product")
def delete_product(company_id: int, product_id: int) -> None:
    """Elimina un producto de una empresa."""
    try:
        service.delete_product_from_company(company_id, product_id)
        console.print("Producto eliminado correctamente", style="bold green")
    except (CompanyNotFoundError, ProductNotFoundError) as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("add-service")
def add_service(
    company_id: int,
    service_id: int,
    name: str,
    price: float,
) -> None:
    """Agrega un servicio a una empresa."""
    try:
        service_data = {
            "id": service_id,
            "name": name,
            "price": price,
        }
        service.add_service_to_company(company_id, service_data)
        console.print("Servicio agregado correctamente", style="bold green")
    except (CompanyNotFoundError, ValueError) as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("list-services")
def list_services(company_id: int) -> None:
    """Muestra todos los servicios de una empresa."""
    try:
        services = service.list_services(company_id)

        if not services:
            console.print("No hay servicios registrados", style="yellow")
            return

        table = Table(
            title="Servicios Registrados",
            header_style="bold cyan",
            border_style="cyan",
        )
        table.add_column("ID", justify="right", style="magenta")
        table.add_column("Name", style="green")
        table.add_column("Price", style="yellow")

        for current_service in services:
            table.add_row(
                str(current_service["id"]),
                current_service["name"],
                str(current_service["price"]),
            )

        console.print(table)
    except CompanyNotFoundError as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("update-service")
def update_service(
    company_id: int,
    service_id: int,
    new_name: str,
    new_price: float,
) -> None:
    """Actualiza el nombre y el precio de un servicio."""
    try:
        service.update_service_in_company(
            company_id,
            service_id,
            new_name,
            new_price,
        )
        console.print("Servicio actualizado correctamente", style="bold green")
    except (CompanyNotFoundError, ServiceNotFoundError, ValueError) as error:
        console.print(f"Error: {error}", style="bold red")


@app.command("delete-service")
def delete_service(company_id: int, service_id: int) -> None:
    """Elimina un servicio de una empresa."""
    try:
        service.delete_service_from_company(company_id, service_id)
        console.print("Servicio eliminado correctamente", style="bold green")
    except (CompanyNotFoundError, ServiceNotFoundError) as error:
        console.print(f"Error: {error}", style="bold red")


if __name__ == "__main__":
    app()



