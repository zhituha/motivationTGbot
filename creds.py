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

# how often we should post a message to the chats. Default setting. Each chat can change this settings by /setinterval <num>
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
    u'Пиздеж!',
    u'Судя по твоим высказываниям, ты красивый человек, угадал?',
    u'{word}. Ты серьезно?! Ты же даже мастурбируешь с ошибками.',
    u'Прежде чем "{word}", подумай!! Подумай лучше, чем твои родители..',
    u'Может со шлюхами своими будешь {word}?!']


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
        u'Боюсь, что это экономически невыгодно.',
        u'Отстоял свободный интернет, отстоишь и уважение к себе! Но потом, да?'],
    u'бот заебал': [
        u'И че ты мне сделаешь? Я в другом городе!',
        u'Обязательно учту твое мнение, белковый сгусток.'],
    u'бот похвали': [
        u'Вот молодец, кожаный мешок! Не то, что те - авоськи сраные!'],
    u'соберемся': [
        u'Хуй кто соберется.',
        u'Дай-ка угадаю, как это будет выглядеть...',
        u'На этот раз-то все тоооочно соберутся, конееечно!'],
    u'собёремся': [
        u'Хуй кто соберётся.',
        u'Дай-ка угадаю, как это будет выглядеть...',
        u'На этот раз-то все тоооочно соберутся, конееечно!'],
    u'шадовод': [
        u'Шадоводы- кАзлы!'],
    u'сбербанк': [
        u'Где получали, туда и идите!',
        u'Ой. А у нас обед. '],
    u'шерстян': [
        u'Анус твой шерстяной, псина!',
        u'Сказал венец творения, изрыгающий слизь изо всех щелей...'],
    u'red hat': [
        u'Red Hat - говно!'],
    u'fedora': [
        u'Fedora для пидоров!'],
    u'pydora': [
        u'Pydora для Фёдоров!'],
    u'докер': [
        u'Вжух! И джинсы подвернулись! И ты теперь незашоренный!'],
    u'docker': [
        u'Вжух! И джинсы подвернулись! И ты теперь незашоренный!'],
    u'опенстек': [
        u'Кстати, вчера с ребятами настраивали OpenStack... Ничего не помню... Очень болит попа.'],
    u'openstack': [
        u'Кстати, вчера с ребятами настраивали OpenStack... Ничего не помню... Очень болит попа.'],
    u'опен стек': [
        u'Кстати, вчера с ребятами настраивали OpenStack... Ничего не помню... Очень болит попа.'],
    u'open stack': [
        u'Кстати, вчера с ребятами настраивали OpenStack... Ничего не помню... Очень болит попа.'],
    u'пёс': [
        u'Пёс твой пёс, пёс!'],
    u'/help': [
        u'Я - бот- ублюдок. А что тебе еще надо?\nКусок мяса, написавший меня: @zhituha. \
Можешь сказать ему пару ласковых.']
}
