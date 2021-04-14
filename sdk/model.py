class Message:
    id: str
    type: str
    content: str
    element: dict
    from_user_id: str
    to_chat_id: str

    def __init__(self, json: dict) -> None:
        self.id = json.get("_id")
        self.type = json.get("type")
        self.content = json.get("content")
        self.element = json.get("element")
        self.from_user_id = json.get("fromUser")
        self.to_chat_id = json.get("toChat")


class User:
    id: str
    nickname: str
    avatar_url: str

    def __init__(self, json: dict) -> None:
        self.id = json.get("_id")
        self.nickname = json.get("nickname")
        self.avatar_url = json.get("avatarUrl")


class Chat:
    id: str
    is_direct: str
    title: str
    metadata: dict
    users: list[User]

    def __init__(self, json: dict) -> None:
        self.id = json.get("_id")
        self.is_direct = json.get("isDirect")
        self.title = json.get("title")
        self.metadata = json.get("metadata")
        self.users = list(map(lambda x: User(x), json.get("users")))
