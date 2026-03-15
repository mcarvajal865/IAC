import pytest
from mi_app.services import IACService
from mi_app.models import Company
from mi_app.storage import JSONStorage
from mi_app.exceptions import (
    CompanyNotFoundError,
    DuplicateCompanyError,
    InvalidCompanyDataError,
    ProductNotFoundError,
    ServiceNotFoundError,
)


@pytest.fixture
def service(tmp_path):
    """Crea un servicio con base de datos temporal"""
    db_file = tmp_path / "test_db.json"
    storage = JSONStorage(db_file)
    return IACService(storage)



def test_create_company_success(service):
    """Crea una empresa"""
    company = Company(id=1, name="IAC", nit="123")
    service.create_company(company)

    companies = service.list_companies()
    assert len(companies) == 1
    assert companies[0]["name"] == "IAC"


def test_create_company_invalid_name(service):
    """Verifica que tenga nombre"""
    company = Company(id=1, name="", nit="123")

    with pytest.raises(InvalidCompanyDataError):
        service.create_company(company)


def test_create_company_invalid_id(service):
    """Verifica que el id >= 1"""
    company = Company(id=-1, name="IAC", nit="123")

    with pytest.raises(InvalidCompanyDataError):
        service.create_company(company)


def test_create_duplicate_company(service):
    """No permite que haya duplicados"""
    company = Company(id=1, name="IAC", nit="123")
    service.create_company(company)

    with pytest.raises(DuplicateCompanyError):
        service.create_company(company)


def test_delete_company_success(service):
    """Elimina empresas"""
    company = Company(id=1, name="IAC", nit="123")
    service.create_company(company)

    service.delete_company(1)
    assert service.list_companies() == []


def test_delete_company_not_found(service):
    """Capta error por si eliminas una empresa que no existe"""
    with pytest.raises(CompanyNotFoundError):
        service.delete_company(999)


def test_add_product_success(service):
    """Agrega productos"""
    company = Company(id=1, name="IAC", nit="123")
    service.create_company(company)

    product = {"id": 1, "name": "Laptop", "price": 1000, "stock": 5}
    service.add_product_to_company(1, product)

    products = service.list_products(1)
    assert len(products) == 1
    assert products[0]["name"] == "Laptop"


def test_delete_product_not_found(service):
    """Capta error por si eliminas un producto inexistente"""
    company = Company(id=1, name="IAC", nit="123")
    service.create_company(company)

    with pytest.raises(ProductNotFoundError):
        service.delete_product_from_company(1, 999)


def test_add_service_success(service):
    """Agrega servicios"""
    company = Company(id=1, name="IAC", nit="123")
    service.create_company(company)

    service_data = {"id": 1, "name": "Consultoría", "price": 500}
    service.add_service_to_company(1, service_data)

    services = service.list_services(1)
    assert len(services) == 1
    assert services[0]["name"] == "Consultoría"


def test_update_service_not_found(service):
    """Actualiza servicios inexistentes"""
    company = Company(id=1, name="IAC", nit="123")
    service.create_company(company)

    with pytest.raises(ServiceNotFoundError):
        service.update_service_in_company(1, 999, "Nuevo", 100)





