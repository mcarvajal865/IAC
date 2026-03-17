from dataclasses import dataclass

@dataclass
class Service:
    id: int
    name: str
    description: str
    price: float

    def __post_init__(self):
        self._validate_id()
        self._validate_name()
        self._validate_description()
        self._validate_price()

    def _validate_id(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("El id debe ser un entero positivo")

    def _validate_name(self):
        if not self.name or not self.name.strip():
            raise ValueError("El nombre del servicio no puede estar vacío")

    def _validate_description(self):
        if not self.description or not self.description.strip():
            raise ValueError("La descripción no puede estar vacía")

    def _validate_price(self):
        if self.price <= 0:
            raise ValueError("El precio debe ser mayor a 0")