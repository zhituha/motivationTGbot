# -*- coding: utf-8 -*-

"""

Rename this file to settings.py or fix the "import" block in the main file.

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

# our phrase.
phrase = u'Эй, кожаный мешок, ты не способен '


# words we should not use. Like a stop-list.

bad_words = [
    u'быть'
]

# Presets of trigger phrases. with list of answer for it.
presets = {
    u'бот извинись': [
        u'Ребята, простите, ради Бога!',
        u'Присядь на бутылку, кусок мяса!',
        u'СМАКМАБИЧАП!'],
    u'бот заебал': [
        u'И че ты мне сделаешь? Я в другом городе!',
        u'В следующий раз святой рандом будет на твоей стороне... Возможно.',
        u'Обязательно учту твое мнение, инкубатор для бактерий.'],
    u'соберемся': [
        u'Хуй кто соберется.',
        u'Дай-ка угадаю, как это будет выглядеть...']
}
