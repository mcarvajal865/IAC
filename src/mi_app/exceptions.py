class IACError(Exception):
    """Excepcion base: Para todos los errores del sistema IAC"""
    pass

class CompanyNotFoundError(IACError):
    """Cuando no se encuentra una empresa
    mensaje: La empresa solicitada no existe en el sistema"""
    pass

class ProductNotFoundError(IACError):
    """Cuando no se encuentra un producto
    mensaje: El producto solicitado no existe en el sistema"""
    pass

class ServiceNotFoundError(IACError):
    """Cuando no se encuentra un servicio
    mensaje: El servicio solicitado no existe en el sistema"""
    pass

class DuplicateCompanyError(IACError):
    """Al intentar registrar una empresa ya existente, por nit o id
    mensaje: La empresa ya está registrada"""
    pass

class InvalidCompanyDataError(IACError):
    """Cuando los datos de la empresa son inválidos,
    mensaje: Nombre y correo son requeridos"""
    pass

class DuplicateProductError(IACError):
    """Al intentar registrar un producto ya existente, por id
    mensaje: El producto ya está registrado"""
    pass

class DuplicateServiceError(IACError):
    """Al intentar registar un servicio ya existente, por id
    mensaje: El servicio ya está registrado"""
    pass

class CompanyAlreadyExistsError(Exception):
    """Se lanza cuando ya existe una empresa con el mismo ID."""
    pass