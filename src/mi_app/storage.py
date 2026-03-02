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

    def load(self) -> Dict[str, Any]:
        """Carga los datos desde el archivo JSON, si el archivo no existe, retorna una estructura base"""
        if not self.filepath.exists():
            return {"companies": []}

        with self.filepath.open("r", encoding = "utf-8") as file: #utf-8: permite usar caracteres especiales
            return json.load(file)