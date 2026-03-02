from dataclasses import dataclass, field
from typing import List

@dataclass
class Service:   #Clase Servicio, guarda su información
    id:int
    name: str
    description: str
    price: float
