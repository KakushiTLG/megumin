import pymysql
import pymysql.cursors
import time
import telebot
from telebot import apihelper



token = '710957371:AAGdS316yO_tDA-g4_KlZVA2XZo-BQKPT_Q'
API_TOKEN = token
bot = telebot.TeleBot(token, skip_pending = True, threaded= False ,num_threads= 1)
chancechat = -1001237284024 #release


def weeklyFraka(chancechat):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `fraks` ORDER BY `fond` DESC"
        cursor.execute(sql)
        result = cursor.fetchall()
        count = 0
        fraka_everyweek = ""
        for dict in result:
            count += 1
            frakaName = str(dict['name'])
            frakaFond = int(dict['fond'])
            if count == 1:
                frakaBonus = frakaFond * 0.3
                fraka_everyweek += "Лучшая фракция по поинтам на этой неделе - " 
            else:
                frakaBonus = frakaFond * 0.07
            sql = "UPDATE `fraks` SET `fond` = fond + %s WHERE `name` = %s"
            cursor.execute(sql, (int(frakaBonus), str(frakaName)))
            db.commit()
            fraka_everyweek += str(frakaName) + "、в фонд было начислено " + str(int(frakaBonus)) + " pts \n"
        db.close()
        fr = bot.send_message(chancechat, "Начисление еженедельного фракционного бонуса было выполнено! " + str(fraka_everyweek))
        bot.pin_chat_message(chancechat, fr.message_id)



weeklyFraka(chancechat)