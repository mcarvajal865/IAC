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