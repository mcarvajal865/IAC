from dataclasses import dataclass, field
from typing import List

@dataclass
class Service:   #Clase Servicio, guarda su información
    id:int
    name: str
    description: str
    price: float

@dataclass
class Product: #Clase Producto, se guarda su información
    id:int
    name: str
    price: float
    stock: int

@dataclass
class Company: #clase Empresa, guarda su información
    id: int
    name: str
    nit: str
    services: List[Service] = field(default_factory=list)
    products: List[Product] = field(default_factory=list)