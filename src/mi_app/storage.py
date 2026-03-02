from typing import Protocol, Dict, Any
from pathlib import Path
import json

class StorageInterface(Protocol):
    """Define el contrato de la capa Storage"""
    def load(self) -> Dict[str, Any]: ...

    def save(self, data: Dict[str, Any]) -> None: ...