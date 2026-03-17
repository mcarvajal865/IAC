from pathlib import Path
from iac.storage import JSONStorage
from iac.services import IACService
from iac.models import Company

storage = JSONStorage(Path("database.json"))
service = IACService(storage)

"""empresa = Company(id=1, name="IAC SAS", nit="900123456")

try:
    service.create_company(empresa)
    print("Empresa creada")
except Exception as e:
    print("Error detectado:", e)"""

"""producto = {
    "id": 101,
    "nombre": "Laptop",
    "price": 2500,
    "stock": 5
}

service.add_product_to_company(1, producto)
print(service.list_companies())"""

servicio = {
    "id": 201,
    "nombre": "Consultoría",
    "description": "Servicio empresarial",
    "price": 500
}

service.add_service_to_company(1, servicio)
print(service.list_companies())


