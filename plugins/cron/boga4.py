import pymysql
import pymysql.cursors
import time
import telebot
from telebot import apihelper
token = '710957371:AAGdS316yO_tDA-g4_KlZVA2XZo-BQKPT_Q'
API_TOKEN = token
bot = telebot.TeleBot(token, skip_pending = True, threaded= False ,num_threads= 1)
chancechat = -1001237284024 #test



def boga4():
    text = "Было произведено взятие налога на развитие локации. Результаты:\n"
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT username, points, id FROM users WHERE points >= 1000"
        cursor.execute(sql)
        result = cursor.fetchall()
        for dict in result:
            pointsNow = int(dict['points'])
            pointsMinus = int(pointsNow * 0.25)
            text += "\n У игрока {} было изъято {} pts".format(str(dict['username']), str(pointsMinus))
            sql = "UPDATE users SET points = points - %s WHERE id = %s"
            cursor.execute(sql, (pointsMinus, int(dict['id'])))
            db.commit()
        db.close()
    q = bot.send_message(chancechat, text)
    bot.pin_chat_message(chancechat, q.message_id)
    return
    




boga4()