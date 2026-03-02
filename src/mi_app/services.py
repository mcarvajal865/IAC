from typing import List, Dict, Any
from .models import Company
from .storage import StorageInterface
from .exceptions import(
    CompanyNotFoundError,
    DuplicateCompanyError,
    InvalidCompanyDataError
)