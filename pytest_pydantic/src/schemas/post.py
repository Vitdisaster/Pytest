from pydantic import BaseModel, Field, EmailStr

from pytest_pydantic.src.schemas.schematom.pagination_schematom import PaginationInfo
from pytest_pydantic.src.schemas.schematom.user_info_schematom import UserGender, UserStatus

class MetaInfo(BaseModel):
    """Мета-информация ответа запроса"""

    pagination: PaginationInfo = Field(...,description="Информация о пагинации")


class User(BaseModel):
    """Данные о пользователе в ответе"""

    id: int = Field(..., le=9508022)
    name: str
    email: str
    gender: UserGender = Field(..., description="Пол пользователя")
    status: UserStatus = Field(..., description="Статус пользователя")


class UsersListResponse(BaseModel):
    """Данные обо всех юзерах"""
    meta: MetaInfo
    data: list[User]