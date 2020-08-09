import pymysql
import pymysql.cursors
import time
import telebot
from telebot import apihelper



token = '710957371:AAGdS316yO_tDA-g4_KlZVA2XZo-BQKPT_Q'
API_TOKEN = token
bot = telebot.TeleBot(token, skip_pending = True, threaded= False ,num_threads= 1)
chancechat = -1001237284024 #test


def frakaZP(chancechat):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaBonus`, `frakaName` FROM `users` WHERE `frakaBonus` > 0"
        cursor.execute(sql)
        result = cursor.fetchall()
        frakaZP = ""
        for dict in result:
            frakaBonus = int(dict['frakaBonus'])
            frakaName = str(dict['frakaName'])
            sql = "SELECT `fond` FROM `fraks` WHERE `name` = %s"
            cursor.execute(sql, (frakaName))
            fond = cursor.fetchone()
            fondNow = fond['fond']
            if frakaBonus < fondNow:
                pass
            else:
                print('Nope')
                return
            sql = "UPDATE `users` SET `points` = points + %s WHERE `frakaName` = %s"
            cursor.execute(sql, (int(frakaBonus), str(frakaName)))
            db.commit()
            sql = "UPDATE `fraks` SET `fond` = fond - %s WHERE `name` = %s"
            cursor.execute(sql, (int(frakaBonus), str(frakaName)))
            db.commit()
            print('done')
        db.close()
        fr = bot.send_message(chancechat, "Начисление фракционного бонуса было выполнено! " + str(fraka_everyday))
        bot.pin_chat_message(chancechat, fr.message_id)


   
frakaZP(chancechat) 
        
        
