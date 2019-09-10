@bot.message_handler(commands=['wrestling'])
def wrest(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `users` WHERE `user_id` = '" + str(m.from_user.id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        username = result['username']
        db.close()
    if lvl == 10:
        pass
    else:
        bot.reply_to(m, "...")
        return
    bot.reply_to(m, "Надев БДСМ-костюм, отправились с Даркхолмом и братанами искать жертвы... Подождите немного...")
    bot.send_video(m.chat.id, open('./media/animation.mp4', 'rb'))
    time.sleep(13)
    wrResult(m)
   
def wrResult(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE users SET lvl = 11 WHERE `user_id` = '" + str(m.from_user.id) + "'"
        cursor.execute(sql)
        db.commit()
        db.close()
    bot.reply_to(m, "В походе с братанами вы нашли невинную жертву, которая через 15 минут оказалась раздетой, со скрученными сосками, на базе Зоны-51. Поздравляю, уровень повышен!")