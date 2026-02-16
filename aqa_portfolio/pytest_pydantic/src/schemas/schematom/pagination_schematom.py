"""Атомарные схемы для валидации pagination"""
from typing import Optional

from pydantic import BaseModel, HttpUrl


class PaginationLinks(BaseModel):
    """Объект links в пагинации"""

    previous: Optional[HttpUrl] = None
    current: HttpUrl
    next: Optional[HttpUrl] = None

class PaginationInfo(BaseModel):
    """Объект pagination в meta"""
    total: int
    pages: int
    page: int
    limit: int
    links: PaginationLinks

