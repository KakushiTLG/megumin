import datetime
import math
import time


@bot.message_handler(commands=['roulette'])
def roulette(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `krazhatime`, `points`, `azart` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        krazhatime = int(result['krazhatime'])
        pts = int(result['points'])
        azart = int(result['azart'])
        timenow = math.ceil(time.time())
        if azart == 0:
            cost = 100
        elif azart == 1:
            cost = 90
        elif azart == 2:
            cost = 80
        elif azart == 3:
            cost = 70
        elif azart == 4:
            cost = 60
        elif azart >= 5:
            cost = 50
        if (int(krazhatime) < math.ceil(time.time())):
            pass
        else:
            bot.reply_to(m, "Играть в рулетку можно не чаще, чем раз в минуту.")
            db.close()
            return
        if pts >= cost:
            pass
        else:
            bot.reply_to(m, "Для игры в рулетку необходимо иметь как минимум {} поинтов на балансе".format(str(cost)))
            db.close()
            return
        sql = "UPDATE users SET `points` = points - %s WHERE `user_id` = %s"
        cursor.execute(sql, (cost, m.from_user.id))
        db.commit()
        sql = "UPDATE users SET `krazhatime` = %s + 60 WHERE `user_id` = %s"
        cursor.execute(sql, (timenow, m.from_user.id))
        db.commit()
        chance = random.randint(1, 100)
        print(str(chance))
        if chance <= 40:
            bot.reply_to(m, "Ты проиграл в рулетку. Возможно, повезёт в следующий раз?")
            db.close()
            return
        elif (chance > 40) and (chance <= 60):
            sql = "UPDATE `users` SET `points` = points + 200 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            bot.reply_to(m, "Ты выиграл 200 pts. Поздравляю!")
            db.close()
            return
        elif (chance > 60) and (chance <= 70):
            sql = "UPDATE `users` SET `points` = points + 500 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            bot.reply_to(m, "Ты выиграл 500 pts. Поздравляю!")
            db.close()
            return
        elif (chance > 70) and (chance <= 75):
            sql = "UPDATE `users` SET `points` = points + 1000 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            bot.reply_to(m, "Тебе сегодня нереально везёт. Ты выиграл 1000 pts, молодец!")
            db.close()
            return
        elif (chance > 75) and (chance >= 94):
            randomEXP = random.randint(1, 100)
            sql = "UPDATE `users` SET `exp` = exp + %s WHERE `user_id` = %s"
            cursor.execute(sql, (randomEXP, m.from_user.id))
            db.commit()
            bot.reply_to(m, "Поздравляю, ты выиграл {} опыта.".format(str(randomEXP)))
            db.close()
            return
        elif (chance > 94) and (chance >= 97):
            sql = "UPDATE `users` SET `points` = points + 2500 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            bot_reply.to(m, "Мне аж завистно - тебе так повезло... Ты выиграл 2500 pts!")
            db.close()
            return
        elif (chance > 97):
            randomStat = random.randint(1, 10)
            if randomStat == 1:
                sql = "UPDATE `users` SET `atk` = atk + 5 WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                db.commit()
                bot_reply.to(m, "Поздравляю, ты выиграл +5 к атаке.")
                db.close()
                return
            elif randomStat == 2:
                sql = "UPDATE `users` SET `hp` = hp + 5 WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                db.commit()
                bot.reply_to(m, "Поздравляю, ты выиграл +5 к здоровью.")
                db.close()
                return
            elif randomStat == 3:
                sql = "UPDATE `users` SET `fatk` = fatk + 3 WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                db.commit()
                bot.reply_to(m, "Поздравляю, ты выиграл +3 к шансу первой атаки.")
                db.close()
                return
            elif randomStat == 4:
                sql = "UPDATE `users` SET `creet` = creet + 1 WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                db.commit()
                bot.reply_to(m, "Поздравляю, ты выиграл +1 к шансу критического урона.")
                db.close()
                return
            elif randomStat >= 5:
                sql = "UPDATE `users` SET `nowhp` = hp WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                db.commit()
                bot.reply_to(m, "Поздравляю, ты выиграл бутылочку лечебного зелья.")
                db.close()
                return