from typing import Protocol, Dict, Any
from pathlib import Path
import json

class StorageInterface(Protocol):
    """Define el contrato de la capa Storage"""
    def load(self) -> Dict[str, Any]: ...

    def save(self, data: Dict[str, Any]) -> None: ...

class JSONStorage:
    """Implementación del almacenamiento en formato JSON,
    responsable de leer y escribir el archivo"""

    def __init__(self, filepath: Path) -> None:
        """Inicializa la ruta donde se
        almacenará el archivo JSON"""
        self.filepath = filepath

    def load(self) -> Dict[str, Any]:
        """Carga los datos desde el archivo JSON.
        Si no existe o está vacío, retorna una estructura base.
        """
        if not self.filepath.exists():
            return {"companies": []}

        contenido = self.filepath.read_text(encoding="utf-8").strip()

        if not contenido:
            return {"companies": []}

        return json.loads(contenido)

    def save(self, data: Dict[str, Any]) -> None:
        """Guarda los datos en el archivo JSON,
        sobrescribe el contenido si ya existe"""
        with self.filepath.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)



