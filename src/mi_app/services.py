from typing import List, Dict, Any
from .models import Company
from .storage import StorageInterface
from .exceptions import(
    CompanyNotFoundError,
    DuplicateCompanyError,
    InvalidCompanyDataError
)

class IACService:
    def __init__(self, storage: StorageInterface) -> None:
        self._storage = storage

    def _get_all_data(self) -> Dict[str, Any]:
        """Para obtener todos los datos del JSON"""
        return self._storage.load()