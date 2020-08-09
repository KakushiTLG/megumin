import pymysql
import pymysql.cursors
import time
import telebot
import random
from telebot import apihelper

token = '710957371:AAGdS316yO_tDA-g4_KlZVA2XZo-BQKPT_Q'
API_TOKEN = token
bot = telebot.TeleBot(token, skip_pending = True, threaded= False ,num_threads= 1)
chancechat = -1001237284024 #test


def randWar(chancechat):
    randWar = random.randint(1, 5)
    if randWar == 1:
        pass
    else:
        print(str(randWar))
        return
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `id` FROM `fraks`"
        cursor.execute(sql)
        result = cursor.fetchall()
        selectFrak = []
        for dict in result:
            print(str(dict['id']))
            selectFrak += str(dict['id'])
        db.close()
        print(str(selectFrak))
        oneFrak = random.choice(selectFrak)
        twoFrak = random.choice(selectFrak)
        print(str(oneFrak))
        print(str(twoFrak))
        if (oneFrak == twoFrak):
            return
        else:
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                print("yep")
                sql = "SELECT `name` FROM `fraks` WHERE `id` = %s"
                cursor.execute(sql, (oneFrak))
                firstFraka = cursor.fetchone()
                oneName = str(firstFraka['name'])
                sql = "SELECT `name` FROM `fraks` WHERE `id` = %s"
                cursor.execute(sql, (twoFrak))
                secondFraka = cursor.fetchone()
                twoName = str(secondFraka['name'])
                print(str(oneName))
                print(str(twoName))
                sql = "UPDATE `fraks` SET `warStatus` = 1 WHERE `name` = %s"
                cursor.execute(sql, (oneName))
                db.commit()
                sql = "UPDATE `fraks` SET `warStatus` = 1 WHERE `name` = %s"
                cursor.execute(sql, (twoName))
                db.commit()
                sql = "UPDATE `fraks` SET `warFraka` = %s WHERE `name` = %s"
                cursor.execute(sql, (oneName, twoName))
                db.commit()
                sql = "UPDATE `fraks` SET `warFraka` = %s WHERE `name` = %s"
                cursor.execute(sql, (twoName, oneName))
                db.commit()
                db.close()
            q = bot.send_message(chancechat, "Началась война между фракцией ''{}'' и ''{}''".format(oneName, twoName))
            bot.pin_chat_message(chancechat, q.message_id)
            
randWar(chancechat)