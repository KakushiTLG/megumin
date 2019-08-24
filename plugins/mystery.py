mdir='mquotes'
def getpoints(m,p):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT points FROM `users` WHERE `user_id` = '" + str(p) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            print(result)
        else:
            sql = "INSERT INTO users (user_id, lvl, points, atk, hp) VALUES (%s, '1', '0', '0', '0')"
            cursor.execute(sql, (str(p)))
            db.commit()
            db.close()
            print('net')
            points=0
            result = points
    return (result)

def putpoints(m,w,p):
    print(w)
   # try: 
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `users` SET `points` = %s WHERE user_id = %s"
        cursor.execute(sql, (w, str(p)))
        db.commit()
        db.close()
@bot.message_handler(commands=['giveaway'])
def giveaway(m):
    randompoints = random.randint(5, 30)
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
    
    
@bot.message_handler(commands=['mystery'])
def megamystery(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT lvl FROM `users` WHERE `user_id` = '" + str(m.from_user.id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
        lvl = result['lvl']
        db.close()
    if int(lvl) >= 2 :
        pass
    else:
        bot.reply_to(m, "/mystery доступен со второго уровня.")
        return
    mystery_number = random.randrange(1, 11, 1)
    p = m.from_user.id
    result = getpoints(m,p)
   # q = int(record[0])
#    w = math.ceil(q) + 1
    bot_time_timeban = 10
    bot_timeban = int(bot_time_timeban) * 60
    bot2_timeban = time.time()
    bot3_timeban = math.ceil(bot2_timeban)
    timebanbot = bot3_timeban + bot_timeban
    if len(m.text.split(' ')) > 1:
        text = m.text.replace('/mystery ', '', 1)
        if(text) == str(mystery_number):
            bot.reply_to(m, 'Ты выиграл! Держи мемчик. Начислено 10 поинтов и 10 опыта!')
            filename = './media/memes/' + random.choice(['file1', 'file2', 'file3', 'file4', 'file5', 'file6', 'file7', 'file8', 'file9', 'file10', 'file11', 'file12', 'file13', 'file14', 'file15', 'file16', 'file17', 'file18', 'file19', 'file20', 'file21', 'file22', 'file23', 'file24', 'file25', 'file26', 'file27', 'file28', 'file29', 'file30', 'file31', 'file32', 'file33', 'file34', 'file35']) + '.jpg' 
            with open (filename, "rb") as file: # открывать как бинарник
                bot.send_photo(m.chat.id, file)
      #      q = record[0]
        #    print('q: ' + int(record[0]) )
        #    print('qw: ' + record[0] )
                e = 10
                if (m.chat.id == chancechat):
                    w = int(result['points']) + e
                    putpoints(m,w,p)
                    db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                    with db.cursor() as cursor:
                        sql = "UPDATE `users` SET `exp` = exp + 10 WHERE user_id = %s"
                        cursor.execute(sql, (str(m.from_user.id)))
                        db.commit()
                        db.close()
        else:
            try:
                bot.restrict_chat_member(m.chat.id, m.from_user.id, timebanbot, False)
                bot.reply_to(m, 'Не угадал. Прости, придется тебя наказать на 10 минут. А правильное число - ' +str(mystery_number))
            except:
                bot.reply_to(m, 'Ты, конечно, не угадал, но ты - администратор, поэтому трогать тебя не буду.')
    else:
        random_player = random.randrange(1, 11, 1)
        if str(random_player) == str(mystery_number):
            bot.reply_to(m, 'Силой двух рандомов обьявляю тебя победителем! Держи мемчик. Начислено 15 поинтов и 10 опыта.')
            filename = './media/memes/' + random.choice(['file1', 'file2', 'file3', 'file4', 'file5', 'file6', 'file7', 'file8', 'file9', 'file10', 'file11', 'file12', 'file13', 'file14', 'file15', 'file16', 'file17', 'file18', 'file19', 'file20', 'file21', 'file22', 'file23', 'file24', 'file25', 'file26', 'file27', 'file28', 'file29', 'file30', 'file31', 'file32', 'file33', 'file34', 'file35']) + '.jpg' 
            with open (filename, "rb") as file: # открывать как бинарник
                bot.send_photo(m.chat.id, file)
      #      q = record[0]
        #    print('q: ' + int(record[0]) )
        #    print('qw: ' + record[0] )
                e = 15
                w = int(result['points']) + e
          #  print( 'q:')
                if (m.chat.id == chancechat):
                    print(w, ' w')
                    putpoints(m,w,p)
                    db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                    with db.cursor() as cursor:
                        sql = "UPDATE `users` SET `exp` = exp + 10 WHERE user_id = %s"
                        cursor.execute(sql, (str(m.from_user.id)))
                        db.commit()
                        db.close()
        else:
            try:
                bot.restrict_chat_member(m.chat.id, m.from_user.id, timebanbot, False)
                bot.reply_to(m, 'Сила рандома тебе не помогла. Прости, придется тебя наказать на 10 минут. Рандомом тебе присвоилось число ' + str(random_player) + ', а правильное число - ' +str(mystery_number))
            except:
                bot.reply_to(m, 'Ты, конечно, не угадал, но ты - администратор, поэтому трогать тебя не буду.')




    