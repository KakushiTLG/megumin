import pymysql
import pymysql.cursors
import time
import telebot
from telebot import apihelper
token = '710957371:AAGdS316yO_tDA-g4_KlZVA2XZo-BQKPT_Q'
API_TOKEN = token
bot = telebot.TeleBot(token, skip_pending = True, threaded= False ,num_threads= 1)
chancechat = -1001237284024 #test



def bankboga4():
    text = "Было произведено взятие налога за использование ячейки в банке. Результаты:\n"
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT username, bankInv, id FROM users WHERE bankNo > 0"
        cursor.execute(sql)
        result = cursor.fetchall()
        for dict in result:
            bankInv = int(dict['bankInv'])
            pointsMinus = int(bankInv * 0.05)
            text += "\n У игрока {} было изъято {} pts из депозит-счёта".format(str(dict['username']), str(pointsMinus))
            sql = "UPDATE users SET bankInv = bankInv - %s WHERE id = %s"
            cursor.execute(sql, (pointsMinus, int(dict['id'])))
            db.commit()
        db.close()
    q = bot.send_message(chancechat, text)
    bot.pin_chat_message(chancechat, q.message_id)
    time.sleep(20)
    g = bot.send_message(chancechat, "ПОСЛЕДНИЕ НОЛОГИ НАХУЙ. ПОМЯНЕМ")
    bot.pin_chat_message(chancechat, q.message_id)
    return
    




bankboga4()