#1 - создатель
#2 - юзер
#0 - никто
#3 приглашенный
@bot.message_handler(commands=['fraka_help'])
def frakaHelp(m):
    frakaInfo = "Фракция - место где игроки могут сплотиться и зарабатывать поинты вместе."
    frakaInfo += "Чтобы попасть во фракцию, нужно получить приглашение от создателя фракции."
    frakaInfo += "Во фракциях запрещен ТимКилл (нельзя вызывать друг друга на битвы), зато инвестируя в фонд фракции, вы можете получать пассивный заработок. \nСоздание своей фракцит платное и стоит 5000pts. Для создания фракции используйте /fcreate"
    bot.reply_to(m, frakaInfo)


@bot.message_handler(commands=['fcreate'])
def frakaCreate(m):
    if len(m.text.split(' ')) > 1:
        pass
    else:
        bot.reply_to(m, "Введите /fcreate [имя желаемой фракции]]")
        return
    fname = m.text.replace('/fcreate ', '', 1)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `points` , `lvl` , `frakaName` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        points = int(result['points'])
        lvl = int(result['lvl'])
        frakaName = result['frakaName']
        if frakaName:
            bot.reply_to(m, "Вы состоите во фракции!")
            return
        else:
            pass
        if points < 5000:
            bot.reply_to(m, "У вас недостаточно поинтов для создания фракции!")
            return
        else:
            pass
        if lvl < 5:
            bot.reply_to(m, "Для создания саоей фракции необходимо иметь минимум 10 уровень.")
            return
        else:
            pass
        sql = "UPDATE `users` SET `points` = points - 5000 WHERE `user_id` = %s"
        cursor.execute(sql, (str(m.from_user.id)))
        db.commit()
        sql = "UPDATE `users` SET `frakaName` = %s WHERE `user_id` = %s"
        cursor.execute(sql, (str(fname), str(m.from_user.id)))
        db.commit()
        sql = "UPDATE `users` SET `frakaStatus` = 1 WHERE `user_id` = %s"
        cursor.execute(sql, (str(m.from_user.id)))
        db.commit()
        sql = "INSERT INTO `fraks` (`name`, `desc`) VALUES (%s, '/fedit_desc')"
        cursor.execute(sql, (str(fname)))
        db.commit()
        bot.reply_to(m, "Фракция успешно создана! Осталось придумать описание фракции и пригласить туда игроков! /finfo - справка")
        db.close()
        
        
        
        
@bot.message_handler(commands=['finfo'])
def fHelp(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaStatus` , `frakaName` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        frakaStatus = result['frakaStatus']
        frakaName = result['frakaName']
        if frakaName:
            pass
        else:
            bot.reply_to(m, "Вы не состоите во фракции.")
            db.close()
            return
        if frakaStatus == 1:
            bot.reply_to(m, "Команды для создателя фракции: \n/fedit_name - изменить название фракции \n/fedit_desc - изменить описание фракции\n/f_invite - пригласить игрока во фракцию. \n/f_players - список игроков в вашей фракции \n/f_uninvite - выгнать игрока из фракции\n ВНИМАНИЕ! Смена названия фракции платная и стоит 10000 pts , сумма снимается с фонда фракции!\n/f_profile - узнать информацию о вашей фракции; \n/fpay - взнос в фонд фракции")
            return
        elif frakaStatus == 2:
            bot.reply_to(m, "nКоманды для участников фракции: \n/f_profile - узнать информацию о вашей фракции; \n/fpay - взнос в фонд фракции")
        elif fkaraStatus == 0:
            bot.reply_to(m, "Вы не состоите во фракции.")



finfo_msg = []

@bot.message_handler(commands=['f_profile'])
def fInfo(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus`, `frakaFond` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = result['frakaStatus']
        frakaFond = result['frakaFond']
        if int(frakaStatus) >= 1:
            pass
        elif int(frakaStatus) == 3:
            bot.reply_to(m, "Вы приглашены во фракцию. Воспользуйтесь профилем.")
            db.close()
            return
        else:
            bot.reply_to(m, "Вы не состоите во фракции.")
            db.close()
            return
        if result:
            pass
        else:
            bot.reply_to(m, "Вы не состоите во фракции.")
            db.close()
            return
        sql = "SELECT * FROM `fraks` WHERE `name` = %s"
        cursor.execute(sql, (frakaName))
        frakainfo = cursor.fetchone()
        db.close()
        name = frakaName
        desc = frakainfo['desc']
        players = frakainfo['players']
        fond = frakainfo['fond']
        lvl = frakainfo['lvl']
        warStatus = int(frakainfo['warStatus'])
        warFraka = frakainfo['warFraka']
        warPts = int(frakainfo['warPts'])
        playersmax = int(lvl) * 2
        fondmax = int(lvl) * 1500
        needptsLvlup = int(lvl) * 750
        notif = ""
        if warStatus == 1:
            notif += "⚠️Идёт война с фракцией\n ''{}''⚠️\nℹ️Фракционные очки: {}ℹ️".format(warFraka, str(warPts))
        elif warStatus == 2:
            notif += "⚠️Ожидается ответ от создателя фракции\n ''{}'' по поводу войны".format(warFraka)
        elif warStatus == 3:
            notif += "⚠️Фракция ''{}'' вызывает вас на бой. \n     /fw_accept - принять;          /fw_cancel - отказаться".format(warFraka)
        else:
            pass
        if int(fond) >= int(needptsLvlup):
            notif += "\n⚠️Доступно повышение уровня фракции за " + str(needptsLvlup) + " pts. Повышение уровня увеличит лимит на игроков во фракции, а так же максимально возможный фонд. /f_lvlup для повышения уровня.⚠️"
        else:
            notif += ""
        if (frakaStatus == 2):
            markup = InlineKeyboardMarkup()
            markup.row_width = 2
            markup.add(InlineKeyboardButton('Список игроков во фракции', callback_data="f_players"))
            finfo = "ℹ️Название: " + str(name) + "ℹ️"
            finfo += "\n▶️Описание: " + str(desc) + "◀️\n \n"
            finfo += "\n📌Уровень: " + str(lvl) + "📌"
            finfo += "\n♻️Игроков: " + str(players) + "/" + str(playersmax) + "♻️"
            finfo += "\n💰Фонд фракции: " + str(fond) + "/" + str(fondmax) + "pts💰"
            finfo += "\n💵Ваш вклад: " +str(frakaFond) + " pts💵 \n" + str(notif)
            bot.reply_to(m, finfo, reply_markup=markup)
        elif (warStatus == 0) and (frakaStatus == 1):
            markup = InlineKeyboardMarkup()
            markup.row_width = 2
            markup.add(InlineKeyboardButton('Панель основателя', callback_data="leader_panel"))
            markup.add(InlineKeyboardButton('Список игроков во фракции', callback_data="f_players"))
            finfo = "\nℹ️Название: " + str(name) + "ℹ️"
            finfo += "\n▶️Описание: " + str(desc) + "◀️\n \n"
            finfo += "\n📌Уровень: " + str(lvl) + "📌"
            finfo += "\n♻️Игроков: " + str(players) + "/" + str(playersmax) + "♻️"
            finfo += "\n💰Фонд фракции: " + str(fond) + "/" + str(fondmax) + "pts💰"
            finfo += "\n💵Ваш вклад: " +str(frakaFond) + " pts💵 \n" + str(notif)
            finfo_m = bot.reply_to(m, finfo, reply_markup=markup)
        elif (frakaStatus == 1):
            markup = InlineKeyboardMarkup()
            markup.row_width = 2
            markup.add(InlineKeyboardButton('Панель основателя', callback_data="leader_panel"))
            markup.add(InlineKeyboardButton('Список игроков во фракции', callback_data="f_players"))
            finfo = "ℹ️Название: " + str(name) + "ℹ️"
            finfo += "\n▶️Описание: " + str(desc) + "◀️\n \n"
            finfo += "\n📌Уровень: " + str(lvl) + "📌"
            finfo += "\n♻️Игроков: " + str(players) + "/" + str(playersmax) + "♻️"
            finfo += "\n💰Фонд фракции: " + str(fond) + "/" + str(fondmax) + "pts💰"
            finfo += "\n💵Ваш вклад: " +str(frakaFond) + " pts💵 \n" + str(notif)
            bot.reply_to(m, finfo)
            
            
@bot.callback_query_handler(func=lambda call: call.data.startswith('leader_panel'))
def leadPanel(call): 
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('Войны', callback_data="WAR"))
    markup.add(InlineKeyboardButton('Отчисления', callback_data="payPlayers"))
    markup.add(InlineKeyboardButton('Пригласить', callback_data="invite"))
    markup.add(InlineKeyboardButton('Выгнать', callback_data="funinvite"))
   # markup.add(InlineKeyboardButton('Продать фракцию', callback_data="sellfraka"))
    text = "\n       🔰Панель основателя🔰\n"
    text += "Краткая информация по панели:\n"
    text += "Войны - панель нападения на другую фракцию\n"
    text += "Отчисления - начисление из фонда участникам фракции\n"
    text += "Пригласить - панель, в которой можно пригласить игрока в свою фракцию\n"
    text += "Выгнать - панель, в которой можно выгнать участника фракции\n"
    text += "(Недоступно)Продать фракцию - вы можете продать свою фракцию игроку, который не состоит ни в одной из фракций"
    gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('WAR'))
def WAR_fraka(call): 
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = int(result['frakaStatus'])
        if frakaStatus == 1:
            pass
        else:
            bot.reply_to(m, "Вы не являетесь создателем фракции.")
            db.close()
            return
        sql = "SELECT `warStatus` FROM `fraks` WHERE `name` = %s"
        cursor.execute(sql, (frakaName))
        result = cursor.fetchone()
        warStatus = int(result['warStatus'])
        if warStatus != 0:
            bot.send_message(call.message.chat.id, "Недоступно")
            return
        else:
            pass
        sql = "SELECT `id` FROM `fraks` WHERE `name` = %s"
        cursor.execute(sql, (frakaName))
        result = cursor.fetchone()
        myfrak = int(result['id'])
        sql = "SELECT `name`, `lvl`, `id` FROM `fraks` WHERE `id` != %s"
        cursor.execute(sql, (myfrak))
        result = cursor.fetchall()
        db.close()
        spisok = ""
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        for dict in result:
            spisok += str(dict['name']) + " - " + str(dict['lvl']) + "pts \n"
            markup.add(InlineKeyboardButton(str(dict['name']), callback_data="clanwar_{}".format(dict['id'])))
        text = "Выберите фракцию, на которую хотите напасть: \n" + str(spisok)
        gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
        
        
    

@bot.callback_query_handler(func=lambda call: call.data.startswith('clanwar_'))
def clanwar(call):
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    clanwar_id = call.data.split('_')
    clanwarid = clanwar_id[1]
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (str(call.from_user.id)))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        sql = "SELECT `name` FROM `fraks` WHERE `id` = %s"
        cursor.execute(sql, (clanwarid))
        result = cursor.fetchone()
        frakaEnemy = result['name']
        sql = "UPDATE `fraks` SET `warStatus` = 2 WHERE `name` = %s"
        cursor.execute(sql, (frakaName))
        db.commit()
        sql = "UPDATE `fraks` SET `warFraka` = %s WHERE `name` = %s"
        cursor.execute(sql, (frakaEnemy, frakaName))
        db.commit()
        sql = "UPDATE `fraks` SET `warStatus` = 3 WHERE `name` = %s"
        cursor.execute(sql, (frakaEnemy))
        db.commit()
        sql = "UPDATE `fraks` SET `warFraka` = %s WHERE `name` = %s"
        cursor.execute(sql, (frakaName, frakaEnemy))
        db.commit()
        sql = "SELECT `user_id` FROM `users` WHERE `frakaStatus` = 1 AND `frakaName` = %s"
        cursor.execute(sql, (frakaEnemy))
        result = cursor.fetchone()
        ownerFrakaEnemy = result['user_id']
        db.close()
    text = "Вы бросили вызов фракции ''{}''! За результатом ответа наблюдайте за профилем фракции.".format(frakaEnemy)
    gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    bot.send_message(ownerFrakaEnemy, "Вашу фракцию вызвали на войну. Запрос от фракции ''{}''".format(frakaName))

    
    
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('payPlayers'))
def payPlayers(call): 
    if (call.message.reply_to_message.from_user.id == call.from_user.id):
        pass
    else:
        bot.reply_to(call.message.chat.id, "Вот поэтому разработчики и просят такие действия делать в лс... Вот @" + str(call.from_user.username) + " попытаося клацнуть.")
        return
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (call.message.reply_to_message.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        sql = "SELECT `id`, `username`, `frakaBonus` FROM `users` WHERE `frakaName` = %s AND `frakaStatus` != 3"
        cursor.execute(sql, (frakaName))
        result = cursor.fetchall()
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        spisok = "Чтобы изменить отчисления текущего игрока, нажмите на кнопку с его именем\nФормат: юзернейм - текущие отчисления\n"
        for dict in result:
            spisok += str(dict['username']) + " - " + str(dict['frakaBonus']) + "pts \n"
            markup.add(InlineKeyboardButton(str(dict['username']), callback_data="paysTo_{}".format(dict['id'])))
        db.close()
        gg = bot.edit_message_text(spisok, call.message.chat.id, call.message.message_id, reply_markup=markup)
    
    
    
    
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('paysTo_'))
def pay_to_player(call):
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    pays = call.data.split('_')
    pay_to = pays[1]
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `username`, `frakaBonus` FROM `users` WHERE `id` = %s"
        cursor.execute(sql, (pay_to))
        result = cursor.fetchone()
        username = result['username']
        frakaBonus = result['frakaBonus']
        markup = InlineKeyboardMarkup()
        markup.row_width = 5
        db.close()
        text = "Игрок " + str(username) + " получает с фракции " + str(frakaBonus) + " pts в час. Вы можете установить его доход, пользуясь кнопками ниже."
        markup.add(InlineKeyboardButton("5", callback_data="playerFrakaPay:5:{}".format(username)), InlineKeyboardButton("10", callback_data="playerFrakaPay:10:{}".format(username)), InlineKeyboardButton("15", callback_data="playerFrakaPay:15:{}".format(username)), InlineKeyboardButton("20", callback_data="playerFrakaPay:20:{}".format(username)), InlineKeyboardButton("25", callback_data="playerFrakaPay:25:{}".format(username)))
        markup.add(InlineKeyboardButton("30", callback_data="playerFrakaPay:30:{}".format(username)), InlineKeyboardButton("35", callback_data="playerFrakaPay:35:{}".format(username)), InlineKeyboardButton("40", callback_data="playerFrakaPay:40:{}".format(username)), InlineKeyboardButton("45", callback_data="playerFrakaPay:45:{}".format(username)), InlineKeyboardButton("50", callback_data="playerFrakaPay:50:{}".format(username)))
        markup.add(InlineKeyboardButton("55", callback_data="playerFrakaPay:55:{}".format(username)), InlineKeyboardButton("60", callback_data="playerFrakaPay:60:{}".format(username)), InlineKeyboardButton("65", callback_data="playerFrakaPay:65:{}".format(username)), InlineKeyboardButton("70", callback_data="playerFrakaPay:75:{}".format(username)), InlineKeyboardButton("75", callback_data="playerFrakaPay:75:{}".format(username)))
        markup.add(InlineKeyboardButton("80", callback_data="playerFrakaPay:80:{}".format(username)),  InlineKeyboardButton("90", callback_data="playerFrakaPay:90:{}".format(username)), InlineKeyboardButton("95", callback_data="playerFrakaPay:95:{}".format(username)), InlineKeyboardButton("100", callback_data="playerFrakaPay:100:{}".format(username)))
        markup.add(InlineKeyboardButton("0", callback_data="playerFrakaPay:0:{}".format(username)))
        gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data.startswith('playerFrakaPay:'))
def playerFrakaPay(call):
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    pays = call.data.split(':')
    pay_to = pays[1]
    payWho = pays[2]
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `users` SET `frakaBonus` = %s WHERE `username` = %s"
        cursor.execute(sql, (pay_to, payWho))
        db.commit()
        db.close()
        print(str(pay_to))
        print(str(payWho))
    text = "Доход пользователя {} установлен. Теперь игрок получает {} pts в час.".format(str(payWho), str(pay_to))
    gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    return



@bot.callback_query_handler(func=lambda call: call.data.startswith('invite'))
def f_invite(call): 
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `username`, `id`, `lvl` FROM `users` WHERE `frakaStatus` = 0"
        cursor.execute(sql)
        result = cursor.fetchall()
        markup = InlineKeyboardMarkup()
        markup.row_width = 5
        text = "\nПриглашение во фракцию осуществляется путем нажатия на кнопку с ником игрока. \nСписок игроков без фракции:"
        for dict in result:
            markup.add(InlineKeyboardButton(str(dict['username']), callback_data="playerinvite_{}".format(str(dict['id']))))
            text += "\n" + str(dict['username']) + "- " + str(dict['lvl']) + "lvl"
        gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
        
        
        
@bot.callback_query_handler(func=lambda call: call.data.startswith('playerinvite_'))
def finvite(call): 
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    userj = call.data.split('_')
    user = userj[1]
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaStatus` FROM `users` WHERE `id` = %s"
        cursor.execute(sql, (str(user)))
        check = cursor.fetchone()
        check1 = int(check['frakaStatus'])
        sql = "SELECT `frakaName` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
        result = cursor.fetchone()
        frakaNam = result['frakaName']
        if int(check1) == 0:
            pass
        elif int(check1) == 3:
            text = "У игрока уже активно одно приглашение."
            gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
            db.close()
            return
        else:
            text = "Игрок состоит во фракции."
            gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
            db.close()
            return
        sql = "SELECT `lvl`, `players` FROM `fraks` WHERE `name` = %s"
        cursor.execute(sql, (frakaNam))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        players = int(result['players'])
        maxPlayers = lvl * 2
        if (players + 1) >= int(maxPlayers):
            text = "Игроков в вашей фракции не может быть выше допустимого."
            gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
            db.close()
            return
        else:
            pass
        sql = "SELECT `frakaName` FROM `users` WHERE `id` = %s"
        cursor.execute(sql, (user))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        if frakaName != "":
            text = "Игрок уже состоит во фракции."
            gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
            db.close()
            return
        else:
            pass
        sql = "UPDATE `users` SET `frakaName` = %s WHERE `id` = %s"
        cursor.execute(sql, (str(frakaNam), user))
        db.commit()
        sql = "UPDATE `users` SET `frakaStatus` = 3 WHERE `id` = %s"
        cursor.execute(sql, (user))
        db.commit()
        text = "Вы успешно пригласили игрока в вашу фракцию."
        gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
        db.close()
        return
    
    
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('funinvite'))
def f_uninvite(call): 
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        sql = "SELECT `username`, `id` FROM `users` WHERE `frakaName` = %s"
        cursor.execute(sql, (frakaName))
        result = cursor.fetchall()
        markup = InlineKeyboardMarkup()
        markup.row_width = 5
        db.close()
        text = "\nКик участника фракции осуществляется путем нажатия на кнопку с ником игрока. \nСписок игроков в вашей фракции:"
        for dict in result:
            markup.add(InlineKeyboardButton(str(dict['username']), callback_data="playeruninvite_{}".format(str(dict['id']))))
            text += "\n" + str(dict['username'])
        gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data.startswith('playeruninvite_'))
def funinvite(call): 
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    userj = call.data.split('_')
    user = userj[1]
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus` FROM `users` WHERE user_id = %s"
        cursor.execute(sql, (call.message.reply_to_message.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = int(result['frakaStatus'])
        cancel = None
        if frakaStatus == 1:
            sql = "SELECT `frakaName` , `username`, `frakaStatus` FROM `users` WHERE `id` = %s"
            cursor.execute(sql, (str(user)))
            result = cursor.fetchone()
            frakaN = result['frakaName']
            userFraka = result['username']
            frakaStatus = result['frakaStatus']
            if frakaN == frakaName:
                pass
            else:
                 text = "Игрок не состоит в вашей фракции."
                 gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
                 db.close()
                 return
            sql = "UPDATE `users` SET `frakaStatus` = 0 WHERE `id` = %s"
            cursor.execute(sql, (str(user)))
            db.commit()
            sql = "UPDATE `users` SET `frakaName` = %s WHERE id = %s"
            cursor.execute(sql, (cancel, str(user)))
            db.commit()
            sql = "UPDATE `users` SET `frakaBonus` = 0 WHERE id = %s"
            cursor.execute(sql, (str(user)))
            db.commit()
            sql = "UPDATE `users` SET `frakaFond` = 0 WHERE id = %s"
            cursor.execute(sql, (str(user)))
            db.commit()
            if (int(frakaStatus) == 3):
                pass
            else:
                sql = "UPDATE `fraks` SET `players` = players - 1 WHERE name = %s"
                cursor.execute(sql, (str(frakaName)))
                db.commit()
            text = "Вы выгнали игрока " + str(userFraka) + " из своей фракции."
            gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
            db.close()
            return
        else:
            text = "Исключать из фракции может только основатель."
            gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
            db.close()
            return




@bot.callback_query_handler(func=lambda call: call.data.startswith('sellfraka'))
def sellfraka(call): 
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus` FROM `users` WHERE user_id = %s"
        cursor.execute(sql, (call.message.reply_to_message.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = result['frakaStatus']
        if frakaStatus == 3:
            pass
        else:
            bot.reply_to(call.message, "Вы не являетесь создателем фракции.")
            return
        sql = "SELECT `lvl`, `fond`, `players` FROM `fraks` WHERE `name` = %s"
        cursor.execute(sql, (frakaName))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        fond = int(result['fond'])
        players = int(result['players'])
        countFraka = 3500 + (lvl * 250) + (fond * 0.25) + (players * 150)
        text = "В данный момент ваша фракция стоит {} pts. Выберите, кому из игроков вы хотите продать фракцию".format(str(countFraka))
        sql = "SELECT `username`, `id` FROM `users` WHERE `points` > %s"
        cursor.execute(sql, (countFraka))
        result = cursor.fetchall()
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("ЗАКРЫТЬ", callback_data="cancel"))
        for dict in result:
            markup.add(InlineKeyboardButton(str(dict['username']), callback_data="sellFraka_{}".format(str(dict['id']))))
        gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
        db.close()
            




#@bot.callback_query_handler(func=lambda call: call.data.startswith('sellFraka_'))
#def sellfraka(call): 
  #  db = pymysql.connect(host='localhost',
   #                      user='root',
   #                      password='maz1aan16v',                             
  #                       db='Megumin',
  #                       charset='utf8mb4',
  #                       cursorclass=pymysql.cursors.DictCursor)
#    with db.cursor() as cursor:
   #     sql = "UPDATE 
    







@bot.callback_query_handler(func=lambda call: call.data.startswith('cancel'))
def cancel(call): 
    text = "Отменено."
    gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
	
	
	



@bot.callback_query_handler(func=lambda call: call.data.startswith('f_players'))
def f_players(call): 
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus` FROM `users` WHERE user_id = %s"
        cursor.execute(sql, (call.message.reply_to_message.from_user.id))
        result = cursor.fetchone()
        frakaName = (result['frakaName'])
        sql = "SELECT `username`, `frakaFond`, `lvl` FROM `users` WHERE `frakaName` = %s" 
        cursor.execute(sql, (frakaName))
        result = cursor.fetchall()
        frakaList = "Список игроков во фракции и их взносы: \n"
        for dict in result:
            frakaUser = str(dict['username'])
            frakaFond = int(dict['frakaFond'])
            lvl = int(dict['lvl'])
            frakaList += str(frakaUser) + " - " + str(int(frakaFond)) + " pts, " + str(lvl) + "lvl \n"
        gg = bot.edit_message_text(frakaList, call.message.chat.id, call.message.message_id)
        db.close()






@bot.message_handler(commands=['fpay'])
def frakaPay(m):
    if len(m.text.split(' ')) > 1:
        pass
    else:
        bot.reply_to(m, "/fpay [количество поинтов]")
        return
    fpay = m.text.replace('/fpay ', '', 1)
    if int(fpay) > 0:
        pass
    else:
        bot.reply_to(m, "🌚")
        return
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `points`, `frakaName`, `frakaStatus` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        points = int(result['points'])
        frakaName = result['frakaName']
        frakaStatus = result['frakaStatus']
        if frakaName:
            pass
        else:
            bot.reply_to(m, "Вы не состоите во фракции.")
            db.close()
            return
        if frakaStatus == 3:
            bot.reply_to (m, "Вы получили приглашение во фракцию, однако все еще не состоите в ней")
            db.close()
            return
        else:
            pass
        if int(fpay) <= points:
            sql = "SELECT `lvl`, `fond` FROM `fraks` WHERE `name` = %s"
            cursor.execute(sql, (frakaName))
            result = cursor.fetchone()
            lvl = int(result['lvl'])
            fond = int(result['fond'])
            maxFond = lvl * 1500
            if (fond + int(fpay)) > maxFond:
                bot.reply_to(m, "Выше лимита пополнять счет фракции нельзя.")
                db.close()
                return
            else:
                pass
            sql = "UPDATE `users` SET `points` = points - %s WHERE `user_id` = %s"
            cursor.execute(sql, (int(fpay), str(m.from_user.id)))
            db.commit()
            sql = "UPDATE `fraks` SET `fond` = fond + %s WHERE `name` = %s"
            cursor.execute(sql, (int(fpay), str(frakaName)))
            db.commit()
            sql = "UPDATE `users` SET `frakaFond` = frakaFond + %s WHERE `user_id` = %s"
            cursor.execute(sql, (int(fpay), str(m.from_user.id)))
            db.commit()
            db.close()
            bot.reply_to(m, "Вы успешно инвестировали " + str(fpay) + " pts в фонд своей фракции.")
        else:
            bot.reply_to(m, "Недостаточно поинтов.")
            db.close()
            return
            
            
            
            
            
            
@bot.message_handler(commands=['fedit_name'])
def feditName(m):
    if len(m.text.split(' ')) > 1:
        pass
    else:
        bot.reply_to(m, "Введите /fedit_name [имя фракции]")
        return
    fname = m.text.replace('/fedit_name ', '', 1)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaNams` , `frakaStatus` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = int(result['frakaStatus'])
        if frakaName:
            pass
        else:
            bot.reply_to(m, "Вы не состоите во фракции.")
            db.close()
            return
        if frakaStatus == 1:
            sql = "SELECT `fond` FROM `fraks` WHERE `name` = %s"
            cursor.execute(sql, (str(frakaName)))
            result = cursor.fetchone()
            fond = int(result['fond'])
            if fond <= 10000:
                sql = "UPDATE `fraks` SET `fond` = fond - 10000 WHERE `name` = %s"
                cursor.execute(sql, (str(frakaName)))
                db.commit()
                sql = "UPDATE `fraks` SET `name` = %s WHERE `name` = %s"
                cursor.execute(sql, (str(fname), str(frakaName)))
                db.commit()
                bot.reply_to(m, "Вы успешно сменили название фракции.")
                db.close()
                return
            else:
                bot.reply_to(m, "В фонде фракции недостаточно средств.")
                db.close()
                return
        else:
            bot.reply_to(m, "Вы не являетесь создателем данной фракции.")
            db.close()
            return
                
                
                
                
                
                
@bot.message_handler(commands=['fedit_desc'])
def feditDesc(m):
    if len(m.text.split(' ')) > 1:
        pass
    else:
        bot.reply_to(m, "Введите /fedit_desc [описание фракции]")
        return
    fdesc = m.text.replace('/fedit_desc ', '', 1)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName` , `frakaStatus` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = int(result['frakaStatus'])
        if frakaName:
            pass
        else:
            bot.reply_to(m, "Вы не состоите во фракции.")
            db.close()
            return
        if frakaStatus == 1:
            sql = "UPDATE `fraks` SET `desc` = %s WHERE `name` = %s"
            cursor.execute(sql, (str(fdesc), str(frakaName)))
            db.commit()
            bot.reply_to(m, "Вы успешно изменили описание фракции.")
            db.close()
            return
        else:
            bot.reply_to(m, "Вы не являетесь создателем данной фракции!")
            db.close()
            return
            
            
            
            
            






@bot.message_handler(commands=['f_accept'])
def fAccept(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = int(result['frakaStatus'])
        if frakaStatus == 3:
            sql = "UPDATE `users` SET `frakaStatus` = 2 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE `fraks` SET `players` = players + 1 WHERE `name` = %s"
            cursor.execute(sql, (str(frakaName)))
            db.commit()
            bot.reply_to(m, "Вы успешно вступили во фракцию ''" + str(frakaName) + " '' !")
            db.close()
            return
        else:
            bot.reply_to(m, "Вы не приглашены во фракцию.")
            db.close()
            return
           
           
           
           
           
@bot.message_handler(commands=['f_cancel'])
def fCancel(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus` FROM `users` WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = int(result['frakaStatus'])
        cancel = ""
        if frakaStatus == 3:
            sql = "UPDATE `users` SET `frakaStatus` = 0 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE `users` SET `frakaName` = %s WHERE user_id = %s"
            cursor.execute(sql, (str(cancel), str(m.from_user.id)))
            db.commit()
            bot.reply_to(m, "Вы отказались от вступления во фракцию ''" + str(frakaName) + " '' .")
            db.close()
            return
        else:
            bot.reply_to(m, "Вы не приглашены во фракцию.")
            db.close()
            return
            
            
       
@bot.message_handler(commands=['fw_cancel'])
def fwCancel(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus` FROM `users` WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = int(result['frakaStatus'])
        cancel = ""
        if frakaStatus == 1:
            pass
        else:
            bot.reply_to(m, "Принимать такие решения может только основатель фракции.")
            db.close()
            return
        sql = "SELECT * FROM `fraks` WHERE `name` = %s"
        cursor.execute(sql, (frakaName))
        result = cursor.fetchone()
        warStatus = int(result['warStatus'])
        warFraka = result['warFraka']
        if warStatus == 3:
            sql = "UPDATE `fraks` SET `warStatus` = 0 AND `warFraka` = %s AND `warPts` = 0 WHERE `name` = %s AND `name` = %s"
            cursor.execute(sql, (str(cancel), frakaName, warFraka))
            db.commit()
            bot.reply_to(m, "Вы отказались от сражения.")
            db.close()
        else:
            bot.reply_to(m, "У вас нет активных приглашений.")
            return





@bot.message_handler(commands=['fw_accept'])
def fwAccept(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus` FROM `users` WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = int(result['frakaStatus'])
        cancel = ""
        if frakaStatus == 1:
            pass
        else:
            bot.reply_to(m, "Принимать такие решения может только основатель фракции.")
            db.close()
            return
        sql = "SELECT * FROM `fraks` WHERE `name` = %s"
        cursor.execute(sql, (frakaName))
        result = cursor.fetchone()
        warStatus = int(result['warStatus'])
        warFraka = result['warFraka']
        if warStatus == 3:
            sql = "UPDATE `fraks` SET `warStatus` = 1 WHERE `name` = %s"
            cursor.execute(sql, (frakaName))
            db.commit()
            sql = "UPDATE `fraks` SET `warPts` = 0 WHERE `name` = %s"
            cursor.execute(sql, (frakaName))
            db.commit()
            sql = "UPDATE `fraks` SET `warStatus` = 1 WHERE `name` = %s"
            cursor.execute(sql, (warFraka))
            db.commit()
            sql = "UPDATE `fraks` SET `warPts` = 0 WHERE `name` = %s"
            cursor.execute(sql, (warFraka))
            db.commit()
            bot.reply_to(m, "Вы приняли предложение.")
            q = bot.send_message(chancechat, "Началась война между фракцией ''{}'' и ''{}''".format(frakaName, warFraka))
            bot.pin_chat_message(chancechat, q.message_id)
            db.close()
        else:
            bot.reply_to(m, "У вас нет активных предложений.")
            return
        
        
        
        
        
        
@bot.message_handler(commands=['f_lvlup'])
def fLvlup(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `frakaName`, `frakaStatus` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        frakaName = result['frakaName']
        frakaStatus = result['frakaStatus']
        if frakaStatus == 1:
            pass
        else:
            bot.reply_to(m, "Вы не являетесь основателем фракции.")
            db.close()
            return
        sql = "SELECT `lvl` , `fond` FROM `fraks` WHERE `name` = %s"
        cursor.execute(sql, (str(frakaName)))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        fond = int(result['fond'])
        needfond = lvl * 750
        if int(needfond) <= fond:
            sql = "UPDATE `fraks` SET `lvl` = lvl + 1 WHERE `name` = %s"
            cursor.execute(sql, (frakaName))
            db.commit()
            sql = "UPDATE `fraks` SET `fond` = fond - %s WHERE `name` = %s"
            cursor.execute(sql, (int(needfond), frakaName))
            db.commit()
            db.close()
            bot.reply_to(m, "Уровень фракции успешно повышен.")
            return
        else:
            db.close()
            bot.reply_to(m, "В фонде вашей фракции недостаточно средств для повышения уровня.")
            return
            
            
            
            
            
            
            
            
            
            
            
            
            
