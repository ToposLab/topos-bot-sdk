import urllib.parse
import requests

from sdk.config import RESTFUL_API_URL, SDK_VERSION
from sdk.model import User, Chat, Message

print("Topos Messaging Service SDK (v%s)" % SDK_VERSION)


class AuthStore:
    token: str
    user: User

    def __init__(self) -> None:
        self.token = None
        self.user = None


auth = AuthStore()

chat_cache: dict[str, Chat] = {}
user_cache: dict[str, User] = {}


def base_url(path: str) -> str:
    return urllib.parse.urljoin(RESTFUL_API_URL, path)


def auth_headers() -> dict:
    return {"authorization": "Bearer %s" % auth.token}


def make_request(method: str, path: str, json: dict = {}, useAuth: bool = True):
    res = requests.request(method, base_url(
        path), json=json, headers=auth_headers() if useAuth else {})

    if res.status_code == 401 and auth.token is not None:
        renew()
        return make_request(method, path, json, useAuth)

    if res.status_code != 200 and res.status_code != 201:
        raise Exception(res.json())

    return res.json()


def renew(token: str):
    data = make_request("POST", "/auth/login",
                       json={"token": token}, useAuth=False)

    auth.token = data["token"]
    auth.user = get_user(data["user"]["_id"])

    print("- renewed token")


def login(countryCode: int, mobile: str, password: str):
    data = make_request("POST", "/auth/login", json={
        "countryCode": countryCode,
        "mobile": mobile,
        "password": password
    }, useAuth=False)

    auth.token = data["token"]
    auth.user = get_user(data["user"]["_id"])

    print("- logined as %s" % auth.user.id)


def get_joined_chats():
    data = make_request("GET", "/chats")
    return list(map(lambda x: Chat(x), data))


def get_chat(chat_id: str, ignore_cache: bool = False):
    if (not ignore_cache) and chat_id in chat_cache:
        return chat_cache[chat_id]

    data = make_request("GET", "/chats/%s" % chat_id)

    chat = Chat(data)
    chat_cache[chat_id] = chat

    return chat


def get_user(user_id: str, ignore_cache: bool = False):
    if (not ignore_cache) and user_id in user_cache:
        return user_cache[user_id]

    data = make_request("GET", "/users/%s" % user_id)

    user = User(data)
    user_cache[user_id] = user

    return user


def send_text(to_chat_id: str, content: str):
    data = make_request("POST", "/chats/%s/messages" % to_chat_id, json={
        "type": "text",
        "content": content
    })

    return Message(data)


def send_image(to_chat_id: str, url: str, width: int, height: int):
    data = make_request("POST", "/chats/%s/messages" % to_chat_id, json={
        "type": "image",
        "content": "[Image]",
        "element": {
            "type": "image",
            "url": url,
            "width": width,
            "height": height
        }
    })

    return Message(data)
