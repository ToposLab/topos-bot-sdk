# 介绍
## Topos App

Topos 是一个以「一起搞事情」为主题的社交 App。在这里，我们鼓励人们与未知的朋友们相识、交流甚至一起做一些事情。在 Topos，我们给予每个用户平等的展示机会，希望每一个用户都可以在这里找到属于自己的「拓扑学家」们。

官网链接：https://topos.world

## Topos Bot SDK

Topos Bot SDK (以下简称 BotSDK)，是 Topos 专为开发者打造的聊天机器人框架。你可以通过调用框架中的方法（函数）来操作机器人的各项功能，执行各种指令。

# 环境配置与部署
## 下载开发包

你可以 clone 或直接下载这个 Repository。目录下的 sdk 文件夹即为 BotSDK 的全部功能实现，example.py 为最基本的使用示例。

## 环境配置与运行

BotSDK 运行在 Python >=3.9 的环境下。如果你是第一次使用 BotSDK，需要先使用 pip 安装所需要的依赖包。

```
pip3 install -r requirements.txt
```

在确认依赖包都已经被安装后，你就可以通过 ```python3 example.py``` 调用。

注：请确保调用前已经正确填写了该文件中的账号信息

```
countryCode: int = <手机号国家编码>
mobile: str = "<账号手机号>"
password: str = "<账号密码>"
```

# API 函数列表
```python
from sdk.core import get_user, get_chat, get_joined_chats

# 通过 user_id 获得 user
user = get_user(user_id)

# 通过 chat_id 获得 chat
chat = get_chat(chat_id)

# 获得所有加入的 chats
joined_chats = get_joined_chats()
```

```python
from sdk.messaging import Context

# Request Handler 的使用方法
def request_handler(ctx: Context):
    # 获得当前消息
    message = ctx.message

    # 获得当前消息所属的 chat
    chat = ctx.chat

    # 发送消息
    ctx.send_text("Hello World")

    # 发送图片，并指定宽高为 60x60
    ctx.send_image("<URL>", width=60, height=60)
```