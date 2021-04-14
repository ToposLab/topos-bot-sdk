from sdk.core import auth, login, get_user
from sdk.messaging import Context, connect, set_request_handler

countryCode: int = 86
mobile: str = ""
password: str = ""

def request_handler(ctx: Context):
    chat = ctx.chat
    message = ctx.message

    # if the message has no sender or the sender is self, do not proceed
    if message.from_user_id is None or message.from_user_id == auth.user.id:
        return

    # if the message is not a text, do not proceed
    if message.type != "text":
        return

    # if the message is not from a chat, do not proceed
    if not chat.is_direct:
        return

    user = get_user(message.from_user_id)
    ctx.send_text("Hi, %s" % user.nickname)


# set the request handler
set_request_handler(request_handler)

# login the user
login(countryCode, mobile, password)

# connect to messaging service
connect()
