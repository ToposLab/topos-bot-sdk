import socketio

from sdk.config import MESSAGING_API_URL
from sdk.core import auth, get_chat, send_image, send_text
from sdk.model import Chat, Message

sio = socketio.Client()


@sio.on('connect')
def on_connect():
    print("- connected to messaging service")


@sio.on('message')
def on_message(data):
    request_handler(Context(Message(data)))


def set_request_handler(handler):
    global request_handler
    request_handler = handler


def connect():
    sio_url = MESSAGING_API_URL + ("?token=%s" % auth.token)
    sio.connect(sio_url, transports="websocket")


class Context:
    message: Message
    chat: Chat

    def __init__(self, message: Message) -> None:
        self.message = message
        self.chat = get_chat(message.to_chat_id)

    def send_text(self, content: str):
        return send_text(self.chat.id, content)

    def send_image(self, url: str, width: int, height: int):
        return send_image(self.chat.id, url, width, height)
