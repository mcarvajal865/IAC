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

    def _get_company(self, data: Dict, company_id: int ) -> Dict[str, Any]:
        """Busca empresa por su ID, si no existe lanza error"""
        companies = data.get("companies", [])

        for company in companies:
            if company["id"] == company_id:
                return company

        raise CompanyNotFoundError(f"La empresa con ID {company_id} no existe en el sistema")