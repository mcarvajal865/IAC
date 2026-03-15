class IACError(Exception):
    """Excepcion base: Para todos los errores del sistema IAC"""
    pass

class CompanyNotFoundError(Exception):
    """Se lanza cuando no se encuentra una empresa."""
    pass


class DuplicateCompanyError(Exception):
    """Se lanza cuando ya existe una empresa con el mismo ID."""
    pass


class InvalidCompanyDataError(Exception):
    """Se lanza cuando los datos de la empresa no son válidos."""
    pass


class ProductNotFoundError(Exception):
    """Se lanza cuando no se encuentra un producto."""
    pass


class ServiceNotFoundError(Exception):
    """Se lanza cuando no se encuentra un servicio."""
    pass