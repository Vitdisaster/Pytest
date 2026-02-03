# {'userId': 1, 'id': 1,
# 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
# 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita
# et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
POST_SCHEMA = {
    "type": "object", # Пока один объект, потом сделать array
    "properties": {  # Когда список объектов, добавить items: { type: "object" ...} - для каждого item обработка
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},

    },
    "required": ["userId", "id", "title", "body"],
}
