from typing import List, Dict, Any
from mi_app.models import Company
from mi_app.storage import StorageInterface
from mi_app.exceptions import(
    CompanyNotFoundError,
    DuplicateCompanyError,
    InvalidCompanyDataError,
    ProductNotFoundError,
    ServiceNotFoundError
)

class IACService:
    def __init__(self, storage: StorageInterface) -> None:
        self._storage = storage

    def _get_all_data(self) -> Dict[str, Any]:
        """Para obtener todos los datos del JSON"""
        return self._storage.load()

    def _get_company(self, data: Dict[str, Any], company_id: int ) -> Dict[str, Any]:
        """Busca empresa por su ID,
        si no existe lanza error"""
        companies = data.get("companies", [])

        for company in companies:
            if company["id"] == company_id:
                return company

        raise CompanyNotFoundError(
            f"La empresa con ID {company_id} no existe en el sistema"
        )

    def list_companies(self) -> List[Dict[str, Any]]:
        """Retorna lista de todas
        las empresas registradas"""
        data = self._get_all_data()
        return data.get("companies", [])


    def create_company(self, company: Company) -> None:
        " ""Método para crear una nueva empresa"""

        data = self._get_all_data()

        if not company.name.strip():
            raise InvalidCompanyDataError("El nombre de la empresa no puede estar vacío")

        if company.id < 1:
            raise InvalidCompanyDataError("El ID de la empresa debe ser mayor o igual a 1")

        if any(c["id"] == company.id for c in data["companies"]):
            raise DuplicateCompanyError("Ya existe una empresa con ese ID")

        data["companies"].append({
            "id": company.id,
            "name": company.name,
            "nit": company.nit,
            "products": [],
            "services": [],
        })

        self._storage.save(data)

    def delete_company(self, company_id: int) -> None:
        """Elimina una empresa por su ID"""
        data = self._get_all_data()
        company = self._get_company(data, company_id)

        data["companies"].remove(company)
        self._storage.save(data)

    def update_company(
            self,
            company_id: int,
            new_name: str,
            new_nit: str
    ) -> None:
        """Acutualiza el nombre y
        NIT de una empresa existente"""
        data = self._get_all_data()
        company = self._get_company(data, company_id)

        company["name"] = new_name
        company["nit"] = new_nit

        self._storage.save(data)

    def list_products(self, company_id: int) -> List[Dict[str, Any]]:
        """Lista todos los productos de la empresa"""
        data = self._get_all_data()
        company = self._get_company(data, company_id)
        return company.get("products", [])

    def add_product_to_company(
            self,
            company_id: int,
            product_data: Dict[str, Any]
    ) -> None:
        """Agregar un producto """

        data = self._get_all_data()
        company = self._get_company(data, company_id)

        company["products"].append(product_data)
        self._storage.save(data)

    def delete_product_from_company(self, company_id: int, product_id: int) -> None:
        """Elimina producto de una empresa"""
        data = self._get_all_data()
        company = self._get_company(data, company_id)

        products = company.get("products", [])

        for product in products:
            if product["id"] == product_id:
                products.remove(product)
                self._storage.save(data)
                return

        raise ProductNotFoundError(
            f"El producto con ID {product_id} no existe"
        )

    def update_product_in_company(
            self,
            company_id: int,
            product_id: int,
            new_name: str,
            new_price: float
    ) -> None:
        data = self._get_all_data()
        company = self._get_company(data, company_id)

        for product in company.get("products", []):
            if product["id"] == product_id:
                product["name"] = new_name
                product["price"] = new_price
                self._storage.save(data)
                return

        raise ProductNotFoundError(
            f"Producto con ID {product_id} no existe"
        )

    def list_services(self, company_id: int) -> List[Dict[str, Any]]:
        data = self._get_all_data()
        company = self._get_company(data, company_id)
        return company.get("services", [])


    def add_service_to_company(
            self,
            company_id: int,
            service_data: Dict[str, Any]
    ) -> None:
        """Agregar un servicio """
        data = self._get_all_data()
        company = self._get_company(data, company_id)

        company["services"].append(service_data)
        self._storage.save(data)

    def delete_service_from_company(
            self,
            company_id: int,
            service_id: int
    ) -> None:
        data = self._get_all_data()
        company = self._get_company(data, company_id)

        services = company.get("services", [])

        for service in services:
            if service["id"] == service_id:
                services.remove(service)
                self._storage.save(data)
                return

        raise ServiceNotFoundError(
            f"Servicio con ID {service_id} no existe"
        )

    def update_service_in_company(
            self,
            company_id: int,
            service_id: int,
            new_name: str,
            new_price: float
    ) -> None:
        data = self._get_all_data()
        company = self._get_company(data, company_id)

        for service in company.get("services", []):
            if service["id"] == service_id:
                service["name"] = new_name
                service["price"] = new_price
                self._storage.save(data)
                return

        raise ServiceNotFoundError(
            f"Servicio con ID {service_id} no existe"
        )


