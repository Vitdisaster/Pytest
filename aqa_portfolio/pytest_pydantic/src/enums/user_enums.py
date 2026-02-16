from aqa_portfolio.pytest_pydantic.src.base_classes.pyenum import PyEnum




class Statuses(PyEnum):
    """
    Статусы пользователя
    """
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    MERGED = "MERGED"