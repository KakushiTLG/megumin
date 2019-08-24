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