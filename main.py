from pathlib import Path
import typer
from rich.console import Console
from rich.table import Table

from src.iac.models import Company
from src.iac.services import IACService
from src.iac.storage import JSONStorage
