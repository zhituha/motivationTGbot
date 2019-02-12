# -*- coding: utf-8 -*-

"""

Rename this file to seetings.py or fix the "import" block in the main file.

"""


# Just add your settings here.
# You can create new bot via @BotFather bot in TG client.

token = 'botID:And_token_you_have_got_from_BotFather'
api = 'https://api.telegram.org'

# If you want use socks5 proxy, add credentials
# and uncomment strings below.

# import socks
# import socket

# proxy_user = ''
# proxy_pass = ''
# proxy_server = ''
# proxy_port = 1080

# socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, addr=proxy_server, port=proxy_port,
#                         username=proxy_user, password=proxy_pass)
# socket.socket = socks.socksocket

# settings for code.

# timeout for connection to the API.
api_timeout = 30

# how often we should post a message to the chats.
wait_posts = 35

# our pharase.
phrase = u'Эй, кожаный мешок, ты не способен '


# words we should not use. Like a stop-list.

bad_words = [
    u'быть'
]
