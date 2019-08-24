import datetime
import math
import time

timecheck = 0
def roulleteBeta(m):
    if m.reply_to_message:
        print('yes')
    else:
        bot.reply_to(m, "Отправь команду ответом тому игроку, с которым хочешь сыграть.")
        return
    bot_whoami = m.from_user.id
    bot_whoare = m.reply_to_message.from_user.id
    bot_whoami1 = m.from_user.username
    bot_whoare1 = m.reply_to_message.from_user.username
    shoot = random.randint(1, 8)
    shoot2 = random.randint(1, 8)
    print(bot_whoami)
    print(bot_whoare)
 #   print(timecheck1)
    global timecheck
    print(timecheck)
    if(m.chat.id != m.from_user.id):
        if str(bot_whoare) == str('710957371'):
            bot.reply_to(m, "Зря ты, дружок, быкануть решил...")
            time.sleep(5)
            bot.reply_to(m, "Итак, игра началась! Взято 50 поинтов у инициатора. В револьвере семь патронов из семи. Вы берете револьвер в руку, крутите барабан... *БА-А-А-АХ!*")
            db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "UPDATE `users` SET `points` = points - %s WHERE user_id = %s"
                cursor.execute(sql, (int('50'), str(bot_whoami)))
                db.commit()
                db.close()
                return
        if int(timecheck) < math.ceil(time.time()):
            timecheck = math.ceil(time.time()) + 600
            db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "UPDATE `users` SET `points` = points - %s WHERE user_id = %s"
                cursor.execute(sql, (int('10'), str(bot_whoami)))
                db.commit()
                sql = "UPDATE `users` SET `points` = points - %s WHERE user_id = %s"
                cursor.execute(sql, (int('10'), str(bot_whoare)))
                db.commit()
                db.close()
            text = "Итак, игра началась! Взято по 10 поинтов у каждого игрока. В револьвере один патрон из семи."
            if shoot == 1:
                text += "Вы взяли револьвер в руку, покрутили барабан. Нажали на курок... *БА-А-А-АХ!* \n'Приходи еще!', - рассмеявшись, сказал ваш соперник и забрал свои 17 поинтов"
                bot.reply_to(m, text)
                db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                with db.cursor() as cursor:
                    sql = "UPDATE `users` SET `points` = points + %s WHERE user_id = %s"
                    cursor.execute(sql, (int('17'),str(bot_whoare)))
                    db.commit()
                    db.close()
            else:
                text += "Вы взяли револьвер в руку, покрутили барабан. Нажали на курок... *клац* \n Вздохнув с облегчением, протягиваете револьвер своему сопернику."
                if shoot2 == 1:
                    text += "\nВаш соперник берет в руки револьвер, прокручивает барабан. нажимает на курок... *БА-А-А-АХ!* Ухмыльнувшись, берете свои 20 поинтов и уходите"
                    bot.reply_to(m, text)
                    db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                    with db.cursor() as cursor:
                        sql = "UPDATE `users` SET `points` = points + %s WHERE user_id = %s"
                        cursor.execute(sql, (int('20'), str(bot_whoami)))
                        db.commit()
                        db.close()
                else:
                    text += "\nВаш соперник берет в руки револьвер, прокручивает барабан. нажимает на курок... *клац*. Однозначно, это ничья! Каждый забирает свои поинты."
                    bot.reply_to(m, text)
                    db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                    with db.cursor() as cursor:
                        sql = "UPDATE `users` SET `points` = points + %s WHERE user_id = %s"
                        cursor.execute(sql, (int('10'),str(bot_whoami)))
                        db.commit()
                        sql = "UPDATE `users` SET `points` = points + %s WHERE user_id = %s"
                        cursor.execute(sql, (int('10'), str(bot_whoare)))
                        db.commit()
                        db.close()
        else:
            bot.reply_to(m, 'Играть в рулетку можно не чаще одного раза в 10 минут.')