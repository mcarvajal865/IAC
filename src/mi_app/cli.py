import typer
from mi_app.models import Company
from mi_app.services import IACService
from mi_app.storage import JSONStorage
from mi_app.exceptions import CompanyAlreadyExistsError
from pathlib import Path

app = typer.Typer()

storage = JSONStorage(Path("data/database.json"))
service = IACService(storage)


@app.command()
def crear_empresa(id: int, nombre: str, nit: str):
    try:
        empresa = Company(id=id, name=nombre, nit=nit)
        service.create_company(empresa)
        print("Empresa creada correctamente")
    except CompanyAlreadyExistsError as e:
        print(f"Error: {e}")


@app.command()
def listar_empresas():
    empresas = service.list_companies()
    for e in empresas:
        print(e)


if __name__ == "__main__":
    app()