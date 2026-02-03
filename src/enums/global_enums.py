from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Полученный статус код не совпадает с ожидаемым"