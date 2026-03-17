from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

@dataclass
class Company:
    id: int
    name: str
    nit: str
    products: List["Product"] = field(default_factory=list)
    services: List["Service"] = field(default_factory=list)

    def __post_init__(self):
        self._validate_id()
        self._validate_name()
        self._validate_nit()

    def _validate_id(self):
        if self.id <= 0:
            raise ValueError("El id debe ser mayor que 0")

    def _validate_name(self):
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío")

    def _validate_nit(self):
        if not self.nit.isdigit():
            raise ValueError("El NIT debe contener solo números")