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

    def list_companies(self) -> List[Dict[str, Any]]:
        """Retorna lista de todas las empresas registradas"""
        data = self._get_all_data()
        return data.get("companies", [])

    def create_company(self, company: Company) -> None:
        """Registra una nueva empresa si no existe"""

        if not company.name or not company.nit:
            raise InvalidCompanyDataError("Nombre y NIT son requeridos")

        if company.id <= 0:
            raise InvalidCompanyDataError("El ID debe ser un número positivo")

        data = self._get_all_data()
        companies = data.get("companies", [])

        for c in companies:
            """Verificar si hay duplicados"""
            if c["id"] == company.id or c["nit"] == company.nit:
                raise DuplicateCompanyError(f"La empresa con ID {company.id} o NIT {company.nit} ya está registrada")

        """Agregar nueva empresa"""
        new_company = {
            "id": company.id,
            "name": company.name,
            "nit": company.nit,
            "services": [],
            "products": []
        }

        companies.append(new_company)
        data["companies"] = companies
        self._storage.save(data)

    def delete_company(self, company_id: int) -> None:
        """Elimina una empresa por su ID"""
        data = self._get_all_data()
        company = self._get_company(data, company_id)

        data["companies"].remove(company)
        self._storage.save(data)

    def add_product_to_company(self, company_id: int, product_data: Dict) -> None:
        """Agregar un producto """

        data = self._get_all_data()
        company = self._get_company(data, company_id)

        company["products"].append(product_data)
        self._storage.save(data)