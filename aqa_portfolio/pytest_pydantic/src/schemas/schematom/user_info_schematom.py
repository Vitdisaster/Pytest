"""Атомарные схемы для валидации user_information"""
from enum import Enum


class UserGender(str, Enum):
    """Пол юзера"""

    male = "male"
    female = "female"

class UserStatus(str, Enum):
    """Статус юзера"""

    active = "active"
    inactive = "inactive"