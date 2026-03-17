from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

    def __post_init__(self):
        self._validate_id()
        self._validate_name()
        self._validate_price()
        self._validate_stock()

    def _validate_id(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("El id debe ser un entero positivo")

    def _validate_name(self):
        if not self.name or not self.name.strip():
            raise ValueError("El nombre del producto no puede estar vacío")

    def _validate_price(self):
        if self.price <= 0:
            raise ValueError("El precio debe ser mayor a 0")

    def _validate_stock(self):
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo")