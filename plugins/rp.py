@bot.message_handler(commands=['me'])
def merp(m):
    text = m.text.replace('/me ', '', 1)
    try:
        bot.delete_message(m.chat.id, m.message_id)
    except:
        pass
    bot.send_message(m.chat.id, '[RP] @' + m.from_user.username + ' ' + text)


@bot.message_handler(commands=['do'])
def dorp(m):
    text = m.text.replace('/do ', '', 1)
    try:
        bot.delete_message(m.chat.id, m.message_id)
    except:
        pass
    bot.send_message(m.chat.id, '[RP] ' + text + ' (@' +  m.from_user.username + ')')

@bot.message_handler(commands=['try'])
def tryrp(m):
    tryRandom = random.randint(0, 1)
    text = m.text.replace('/try ', '', 1)
    if tryRandom == 0:
        try:
            bot.delete_message(m.chat.id, m.message_id)
        except:
            pass
        bot.send_message(m.chat.id, ' [RP] @' + m.from_user.username + ' ' + text + ' | Удачно')

    if tryRandom == 1:
        try:
            bot.delete_message(m.chat.id, m.message_id)
        except:
            pass
        bot.send_message(m.chat.id, ' [RP] @' + m.from_user.username + ' ' + text + ' | Неудачно')
        
        



# АДМИН КОМАНДЫ


@bot.message_handler(commands=['addmob'])
def addMobAdm(m):
    if str(m.from_user.id) in owner:
        if len(m.text.split(' ')) > 1:
            try:
                mob = m.text.replace('/addmob ', '', 1).split(':')
                nameMob = mob[0]
                atkMob = mob[1]
                hpMob = mob[2]
                location = mob[3]
                db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                with db.cursor() as cursor:
                    sql = "INSERT INTO wrestling (mobname, atk, hp, localspawn) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (nameMob, int(atkMob), int(hpMob), int(location)))
                    db.commit()
                db.close()
                bot.reply_to(m, "Добавлен моб: \nИмя - {0} \nАтака - {1} \nХП - {2} \nЛокация - {3}".format(nameMob, str(atkMob), str(hpMob), str(location)))
            except:
                bot.reply_to(m, "Какая-то ошибка...")
                db.close()
        else:
            bot.reply_to(m, "/addmob nameMob:atkMob:hpMob:localspawn")
    else:
        return
        
        
        
        
@bot.message_handler(commands=['notification'])
def notification(m):
    if str(m.from_user.id) in owner:
        pass
    else:
        return
    notif = m.text.replace('/notification ', '', 1)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `user_id` FROM `users` WHERE `id` != 1 ORDER BY `id` DESC"
        cursor.execute(sql)
        result = cursor.fetchall()
        count = 0
        countDone = 0
        for dict in result:
            user_id = str(dict['user_id'])
            try:
                bot.send_message(user_id, str(notif))
                countDone += 1
                count += 1
            except:
                count += 1
        bot.send_message(otorhinid, "Рассылка завершена. Письмо получили " + str(countDone) + " игроков из " + str(count))
        db.close()
 
 
 
 
 
@bot.message_handler(commands=['ownfraks'])
def ownfraks(m):
    if str(m.from_user.id) in owner:
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
            text = ""
            for dict in result:
                name = str(dict['name'])
                text += "\n\n\nФракция ''" + str(name) + "''"
                fond = str(dict['fond'])
                lvl = str(dict['lvl'])
                warStatus = int(dict['warStatus'])
                if warStatus != 0:
                    warFraka = str(dict['warFraka'])
                else:
                    warFraka = "None"
                text += "\n Fond - {}pts \nLvl - {}".format(fond, lvl)
                text += "\n warStatus {} \n warFraka {}".format(warStatus, warFraka)
                sql = "SELECT `username`, `frakaBonus`, `frakaFond` FROM `users` WHERE `frakaName` = %s"
                cursor.execute(sql, (name))
                users = cursor.fetchall()
                for res in users:
                    username = res['username']
                    frakaBonus = res['frakaBonus']
                    frakaFond = res['frakaFond']
                    text += "\n User: \n{} - {}pts/h - {} pts".format(username, frakaBonus, frakaFond)
            db.close()
            bot.reply_to(m, text)
                





@bot.message_handler(commands=['ownsetpoints'])
def ownsetpoints(m):
    if str(m.from_user.id) in owner:
        text = m.text.replace('/ownsetpoints ', '', 1).split(':')
        p = text[0]
        w = text[1]
        db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `points` = %s WHERE username = %s"
            cursor.execute(sql, (w, p))
            db.commit()
            db.close()
            bot.reply_to(m, "Игроку " + p + " установлено " + w + " поинтов.")
        
        
        
@bot.message_handler(commands=['ownsetstats'])
def ownsetstats(m):
    if str(m.from_user.id) in owner:
        text = m.text.replace('/ownsetstats ', '', 1).split(':')
        p = text[0]
        a = text[1]
        hp = text[2]
        db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `atk` = %s WHERE username = %s"
            cursor.execute(sql, (int(a), p))
            db.commit()
            db.close()
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `hp` = %s WHERE username = %s"
            cursor.execute(sql, (int(hp), p))
            db.commit()
            db.close()
        bot.reply_to(m, "Игроку " + p + " установлено " + a + " ед.атаки и " + hp + " hp.")

@bot.message_handler(commands=['ownadd'])
def ownadd(m):
    if str(m.from_user.id) in owner:
        text = m.text.replace('/ownadd ', '', 1).split(':')
        name = text[0]
        desc = text[1]
        price = text[2]
        db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "INSERT INTO lot (`name`, `desc`, `price`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (str(name), str(desc), int(price)))
            db.commit()
            db.close()
            bot.reply_to(m, "Done")
    else:
        return




@bot.message_handler(commands=['promolist'])
def promoList(m):
    if str(m.from_user.id) in owner:
        db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "SELECT `promo` FROM `promo` WHERE `status` = 0"
            cursor.execute(sql)
            result = cursor.fetchall()
            bot.reply_to(m, str(result))
            db.close()
    else:
        bot.reply_to(m, ":(")
