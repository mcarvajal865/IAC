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
