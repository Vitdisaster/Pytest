"""Схема для проверки ответа POST в формате json"""

POST_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "userId": {
                "type": "integer",
                "minimum": 1
            },
            "id": {
                "type": "integer",
                "minimum": 1
            },
            "title": {
                "type": "string",
                "minlength": 1
            },
            "body": {
                "type": "string",
                "minlength": 1
            },
        }
    },
    "required": ["userId", "id", "title", "body"],
    "additionalProperties": False
}
