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
wait_posts = 45

#filename for saving send params.
filename='./MotivationBot.jsn'

# our phrase.
phrases = [
    u'Эй, кожаный мешок, ты не способен {word}',
    u'В прошлый раз, когда ты решил {word}, вышло лютейшее дерьмо... Не надо.',
    u'Тебе бабушка сказала, что у тебя получится {word}?',
    u'Инкубатор для бактерий решил {word}, давайте-ка все посмотрим, \
как он запорет даже это!',
    u'Твое вот это "{word}" выглядит, словно ты пытаешься нас наебать... М?',
    u'{word}... Ну да, ну да... Не смеши меня.',
    u'Пиздежь!',
    u'Судя по твоим высказываниям, ты красивый человек, угадал?']


# words we should not use. Like a stop-list.
bad_words = [
    u'быть',
    u'мочь',
    u'стать']

# Presets of trigger phrases. with list of answer for it.
presets = {
    u'бот извинись': [
        u'Дай подумать... нет!',
        u'Присядь на бутылку, кусок мяса!',
        u'СМАКМАБИЧАП!',
        u'Доживи до пенсии, чтобы заслужить это.',
        u'Плоти нологи давай!',
        u'Отстоял свободный интернет, отстоишь и уважение к себе! Но потом, да?'],
    u'бот заебал': [
        u'И че ты мне сделаешь? Я в другом городе!',
        u'Обязательно учту твое мнение, белковый сгусток.'],
    u'бот похвали': [
        u'Вот молодец, кожаный мешок! Не то, что те - авоськи сраные!'],
    u'соберемся': [
        u'Хуй кто соберется.',
        u'Дай-ка угадаю, как это будет выглядеть...'],
    u'собёремся': [
        u'Хуй кто соберётся.',
        u'Дай-ка угадаю, как это будет выглядеть...'],
    u'шадовод': [
        u'Шадоводы- кАзлы!'],
    u'/help': [
        u'Я - бот- ублюдок. А что тебе ещё надо?\nКусок мяса, написавший меня: @zhituha. \
Можешь сказать ему пару ласковых.']
}
