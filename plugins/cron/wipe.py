import pymysql
import pymysql.cursors
import time
import telebot
from telebot import apihelper


token = '710957371:AAGdS316yO_tDA-g4_KlZVA2XZo-BQKPT_Q'
API_TOKEN = token
bot = telebot.TeleBot(token, skip_pending = True, threaded= False ,num_threads= 1)
chancechat = -1001237284024 #test
dog = 'Отсутствует'


def wipe():
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `users` SET `frakaName` = %s WHERE `id` > 0"
        cursor.execute(sql, (dog))
        sql = "UPDATE `users` SET `frakaStatus` = 0 WHERE `id` > 0"
        cursor.execute(sql)
        sql = "UPDATE `users` SET `frakaFond` = 0 WHERE `id` > 0"
        cursor.execute(sql)
        fr = bot.send_message(chancechat, "Wipe fraks complete")
        bot.pin_chat_message(chancechat, fr. message_id)
    
    
    
    
wipe()