from typing import Protocol, Dict, Any
from pathlib import Path
import json

class StorageInterface(Protocol):
    """Define el contrato de la capa Storage"""
    def load(self) -> Dict[str, Any]: ...

    def save(self, data: Dict[str, Any]) -> None: ...

class JSONStorage:
    """Implementación del almacenamiento en formato JSON, responsable de leer y escribir el archivo"""

    def __init__(self, filepath: Path):
        """Inicializa la ruta donde se almacenará el archivo JSON"""
        self.filepath = filepath