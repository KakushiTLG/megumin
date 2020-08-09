import pymysql
import pymysql.cursors
import time
import telebot
from telebot import apihelper



token = '710957371:AAGdS316yO_tDA-g4_KlZVA2XZo-BQKPT_Q'
API_TOKEN = token
bot = telebot.TeleBot(token, skip_pending = True, threaded= False ,num_threads= 1)
chancechat = -1001237284024 #test


def everydayFrak(chancechat):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `fraks`"
        cursor.execute(sql)
        result = cursor.fetchall()
        fraka_everyday = ""
        for dict in result:
            frakaName = str(dict['name'])
            frakaFond = int(dict['fond'])
            frakaBonus = frakaFond * 0.05
            sql = "UPDATE `users` SET `points` = points + %s WHERE `frakaName` = %s AND `frakaStatus` = 1 OR `frakaName` = %s AND `frakaStatus` = 2 "
            cursor.execute(sql, (int(frakaBonus), str(frakaName), str(frakaName)))
            db.commit()
            fraka_everyday += "\nНачислено по " + str(int(frakaBonus)) + " pts участникам фракции " + str(frakaName) + "\n"
        db.close()
        fr = bot.send_message(chancechat, "Начисление фракционного бонуса было выполнено! " + str(fraka_everyday))
        bot.pin_chat_message(chancechat, fr.message_id)


   
everydayFrak(chancechat) 
        
        
