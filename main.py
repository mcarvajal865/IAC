from pathlib import Path
import typer
from rich.console import Console
from rich.table import Table

from src.iac.models import Company
from src.iac.services import IACService
from src.iac.storage import JSONStorage

app = typer.Typer()
console = Console()

"""Inicializar variables de almacenamiento y servicios"""
storage = JSONStorage(Path("data/database.json"))
service = IACService(storage)