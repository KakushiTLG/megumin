# -*- coding: utf-8 -*-
# coding: utf-8
import telebot
import json
import time
from os.path import exists
from telebot.apihelper import ApiException
import logging
import os
import math
from threading import Timer
from telebot import apihelper
import pymysql.cursors
import pymysql

__version__ = '2.1 open beta'
owner = ['702528084', '282054055', '439637823']
otorhinid = 702528084
otorhinchat = -1001237284024
chancechat = -1001237284024
donators = ['727760103', '784093524', '503247028', '702528084', '282054055', '847058378', '604923616', '965075012', '858978473']
token = '710957371:AAGdS316yO_tDA-g4_KlZVA2XZo-BQKPT_Q'
API_TOKEN = token


_print = print
log = open('log.txt', 'a')
def myprint(*args, **kwargs):
    _print(*args, **kwargs)
    try:
        log.write('\t'.join(str(v) for v in args))
        log.write('\n')
        log.flush()
    except:
        pass
print = myprint


bot = telebot.TeleBot(token, skip_pending = True, threaded= False ,num_threads= 1)
bot_id = int(token.split(':')[0])
print('Bot ID [%s]' % bot_id)

enabled_plugins = [ f[:-3] for f in os.listdir('plugins') if f.endswith('.py') ]

if exists('config.json'):
    with open('config.json') as f:
        bot_config = json.load(f)
    print('Подобие конфига загружено.')
else:
    with open('config.json', 'w') as f:
        json.dump({}, f)

for plugin in enabled_plugins:
    try:
        exec(open("./plugins/" + plugin + ".py", encoding="utf-8").read())
        print ("Подключен " + plugin)
     #   exec(compile(open("./plugins/" + plugin + ".py", "rb").read(), "./plugins/" + plugin + ".py" , 'exec'), globals, locals)
    except Exception as e:
        print("Ошибка подключения " + plugin) 
      #  bot.send_message(owner, 'Ошибка подключения ' + plugin)
       # bot.send_message(owner, e)
    #	 print("Unexpected error:", sys.exc_info()[0])
        print (e)
        exit(1)
        
try :
	exec(open("./texthand.py", encoding="utf-8").read())
except Exception as e:
	print(e)
	
def listener3(messages):
    for m in messages:
        print('%s[%s]:%s' % (m.from_user.first_name, m.chat.id, m.text if m.text else m.content_type))
bot.set_update_listener(listener3)


if(__name__ == '__main__'):
    f=open('digp.txt',encoding='utf-8')
    digp=f.read().splitlines()
    f.close()
    f=open('digt.txt',encoding='utf-8')
    digt=f.read().splitlines()
    f.close()
    f=open('dige.txt',encoding='utf-8')
    dige=f.read().splitlines()
    f.close()
    
    print('Bot started.')
    # Подключиться к базе данных.
    bot.send_message(chancechat, 'Restarted Megumin')
# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        print('\n\nRestart\n\n')
        time.sleep(20)
        