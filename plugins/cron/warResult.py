import pymysql
import pymysql.cursors
import time
import telebot
from telebot import apihelper



token = '710957371:AAGdS316yO_tDA-g4_KlZVA2XZo-BQKPT_Q'
API_TOKEN = token
bot = telebot.TeleBot(token, skip_pending = True, threaded= False ,num_threads= 1)
chancechat = -1001237284024 #test


def warResult(chancechat):
    text = ""
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `name`, `warPts` FROM `fraks` WHERE `warStatus` = 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        for dict in result:
            sql = "SELECT `name`, `warPts` FROM `fraks` WHERE `warFraka` = %s"
            cursor.execute(sql, (str(dict['name'])))
            resultNow = cursor.fetchone()
            if resultNow:
                print(str(dict['warPts']))
                print(str(resultNow['warPts']))
                if (int(resultNow['warPts']) > int(dict['warPts'])):
                    winPts = int(resultNow['warPts']) * 7
                    text += "\nПобедителем в войне вышла фракция ''{}''".format(str(resultNow['name']))
                    sql = "UPDATE `fraks` SET `fond` = fond + %s WHERE `name` = %s"
                    cursor.execute(sql, (winPts, str(resultNow['name'])))
                    db.commit()
                else:
                    winPts = int(dict['warPts']) * 7
                    text += "\nПобедителем в войне вышла фракция ''{}''".format(str(dict['name']))
                    sql = "UPDATE `fraks` SET `fond` = fond + %s WHERE `name` = %s"
                    cursor.execute(sql, (winPts, str(dict['name'])))
                    db.commit()
                cancel = ""
                sql = "UPDATE `fraks` SET `warStatus` = 0 WHERE `name` = %s"
                cursor.execute(sql, (str(dict['name'])))
                db.commit()
                sql = "UPDATE `fraks` SET `warStatus` = 0 WHERE `name` = %s"
                cursor.execute(sql, (str(resultNow['name'])))
                db.commit()
                sql = "UPDATE `fraks` SET `warPts` = 0 WHERE `name` = %s"
                cursor.execute(sql, (str(dict['name'])))
                db.commit()
                sql = "UPDATE `fraks` SET `warPts` = 0 WHERE `name` = %s"
                cursor.execute(sql, (str(resultNow['name'])))
                db.commit()
                sql = "UPDATE `fraks` SET `warFraka` = %s WHERE `name` = %s"
                cursor.execute(sql, (str(cancel), str(dict['name'])))
                db.commit()
                sql = "UPDATE `fraks` SET `warFraka` = %s WHERE `name` = %s"
                cursor.execute(sql, (str(cancel), str(resultNow['name'])))
                db.commit()
            else:
                pass
        wResult = bot.send_message(chancechat, text)
        bot.pin_chat_message(chancechat, wResult.message_id)
        db.close()
        return
                
                
warResult(chancechat)