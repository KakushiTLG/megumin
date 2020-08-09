
@bot.message_handler(commands=['giveaway'])
def giveaway(m):
    randomg = random.randint(1,5)
    if randomg == 1:
        randompoints = random.randint(50, 100)
    else:
        randompoints = random.randint(25, 50)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `sleepg` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        if result:
            giveawaytime = int(result['sleepg'])
            db.close()
            pass
        else:
            bot.reply_to (m, "Ошибка. Возможно, вы не зарегистрированы в системе.")
            db.close()
            return
    last_time = time.time()
    last_time2 = math.ceil(last_time)
    last_time3 = giveawaytime - last_time2
    last_time_result = int(last_time3 / 60)
    if int(giveawaytime) < math.ceil(time.time()):
        giveawaytime = math.ceil(time.time()) + 3600
        bot.reply_to(m, "Поздравляю, ты захватил себе " + str(randompoints) + " поинтов. Возвращайся через час... ")
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `points` = points + %s WHERE `user_id` = %s"
            cursor.execute(sql, (int(randompoints), str(m.from_user.id)))
            db.commit()
            sql = "UPDATE `users` SET `sleepg` = %s WHERE `user_id` = %s"
            cursor.execute(sql, (int(giveawaytime), str(m.from_user.id)))
            db.commit()
            db.close()
    else:
        bot.reply_to(m, "Бесплатные поинты станут доступны через " + str(last_time_result) + " минут.")
    
    
