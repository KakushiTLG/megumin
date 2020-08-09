@bot.message_handler(commands=['wipetemp'])
def wipeTemp(m):
    if str(m.from_user.id) in owner:
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
        sql = "UPDATE `users` SET `tempPts` = 0 WHERE `tempPts` > 0"
        cursor.execute(sql)
        db.commit()
        db.close()
        bot.reply_to(m, "Ивент-поинты обнулены.")



startgame1 = []
def startgame(m):
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        db.close()
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('Камень', callback_data="KAM"))
    markup.add(InlineKeyboardButton('Ножницы', callback_data="NOZH"))
    markup.add(InlineKeyboardButton('Бумага', callback_data="BUM"))
    startgame = bot.reply_to(m, "Ну что, хочешь сыграть со мной? Ну давай. Выбирай...", reply_markup=markup)
    global startgame1
    startgame1 = startgame
@bot.callback_query_handler(func=lambda call: call.data.startswith('KAM'))
def KAM_click_inline(call):
    global startgame1
    BOT_CHOICE = random.randrange(1, 4, 1)
    choice = 1
    if (BOT_CHOICE == 3) and (call.message.reply_to_message.from_user.id == call.from_user.id):
        text = "Ты выбрал камень, но у меня бумага. Я победила!"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    elif (BOT_CHOICE == 2) and (call.message.reply_to_message.from_user.id == call.from_user.id):
        text = "Ты выбрал камень, а я - ножницы. Я проиграла :("
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
        db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `exp` = exp + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
            db.commit()
            sql = "UPDATE `users` SET `points` = points + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
            db.commit()
            sql = "SELECT `exp`, `lvl` FROM `users` WHERE user_id = %s"
            cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
            result = cursor.fetchone()
            needexp = int(result['lvl']) * 100
            plustats = int(needexp) / 50
            if (int(result['exp']) >= needexp):
                ex2p = 0
                sql = "UPDATE `users` SET `exp` = %s WHERE user_id = %s"
                cursor.execute(sql, (int(ex2p), str(call.message.reply_to_message.from_user.id)))
                sql = "UPDATE `users` SET `lvl` = lvl + 1 WHERE user_id = %s"
                cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
                sql = "UPDATE `users` SET `atk` = atk + %s WHERE user_id = %s"
                cursor.execute(sql, (plustats, str(call.message.reply_to_message.from_user.id)))
                sql = "UPDATE `users` SET `hp` = hp + %s WHERE user_id = %s"
                cursor.execute(sql, (plustats, str(call.message.reply_to_message.from_user.id)))
                bot.send_message(id, "LVL UP. Статы повышены на +{0}.".format(str(plustats)))
                db.commit()
                sql = "SELECT `ref` FROM `users` WHERE user_id = %s"
                cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
                isref = cursor.fetchone()
                if isref != None:
                    try:
                        refer = isref['ref']
                        sql = "SELECT `lvl` FROM `users` WHERE username = %s"
                        cursor.execute(sql, str(refer))
                        refer_by = cursor.fetchone()
                        needExpRef = int(refer_by['lvl']) * 100
                        refplus = int(needExpRef) / 5
                        sql = "UPDATE `users` SET `exp` = `exp` + %s WHERE `username` = %s"
                        cursor.execute(sql, (int(refplus), str(refer)))
                        db.commit()
                        db.close()
                        return
                    except:
                        bot.send_message(id, "Не смогли начислить реферальные очки @" + str(isref['ref']))
                        db.close()
                        return
                    else:
                        pass
                    db.close()
    elif (BOT_CHOICE == 1) and (call.message.reply_to_message.from_user.id == call.from_user.id):
        text = "У нас у обоих камень. Ничья."
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    else:
        bot.send_message(call.message.chat.id, "@" + str(call.from_user.username) + ", Зачем ты лезешь играть, если играем не с тобой?")

@bot.callback_query_handler(func=lambda call: call.data == 'NOZH')
def NOZH_click_inline(call):
    global startgame1
    BOT_CHOICE = random.randrange(1, 4, 1)
    choice = 2
    if (BOT_CHOICE == 1) and (call.message.reply_to_message.from_user.id == call.from_user.id):
        text = "Ты выбрал ножницы, но у меня камень. Я победила!"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    elif (BOT_CHOICE == 3) and (call.message.reply_to_message.from_user.id == call.from_user.id):
        text = "Ты выбрал ножницы, а я - бумагу. Я проиграла :("
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
        db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `exp` = exp + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
            db.commit()
            sql = "UPDATE `users` SET `points` = points + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
            db.commit()
            sql = "SELECT `exp`, `lvl` FROM `users` WHERE user_id = %s"
            cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
            result = cursor.fetchone()
            needexp = int(result['lvl']) * 100
            plustats = int(needexp) / 50
            if (int(result['exp']) >= needexp):
                ex2p = 0
                sql = "UPDATE `users` SET `exp` = %s WHERE user_id = %s"
                cursor.execute(sql, (int(ex2p), str(call.message.reply_to_message.from_user.id)))
                sql = "UPDATE `users` SET `lvl` = lvl + 1 WHERE user_id = %s"
                cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
                sql = "UPDATE `users` SET `atk` = atk + %s WHERE user_id = %s"
                cursor.execute(sql, (plustats, str(call.message.reply_to_message.from_user.id)))
                sql = "UPDATE `users` SET `hp` = hp + %s WHERE user_id = %s"
                cursor.execute(sql, (plustats, str(call.message.reply_to_message.from_user.id)))
                bot.send_message(id, "LVL UP. Статы повышены на +{0}.".format(str(plustats)))
                db.commit()
                sql = "SELECT `ref` FROM `users` WHERE user_id = %s"
                cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
                isref = cursor.fetchone()
                if isref != None:
                    try:
                        refer = isref['ref']
                        sql = "SELECT `lvl` FROM `users` WHERE username = %s"
                        cursor.execute(sql, str(refer))
                        refer_by = cursor.fetchone()
                        needExpRef = int(refer_by['lvl']) * 100
                        refplus = int(needExpRef) / 5
                        sql = "UPDATE `users` SET `exp` = `exp` + %s WHERE `username` = %s"
                        cursor.execute(sql, (int(refplus), str(refer)))
                        db.commit()
                        db.close()
                        return
                    except:
                        bot.send_message(id, "Не смогли начислить реферальные очки @" + str(isref['ref']))
                        db.close()
                        return
                    else:
                        pass
                    db.close()
    elif (BOT_CHOICE == 2) and (call.message.reply_to_message.from_user.id == call.from_user.id):
        text = "У нас у обоих ножницы. Ничья."
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    else:
        bot.send_message(call.message.chat.id, "@" + str(call.from_user.username) + ", Зачем ты лезешь играть, если играем не с тобой?")

    
   
@bot.callback_query_handler(func=lambda call: call.data == 'BUM')
def BUM_click_inline(call):
    global startgame1
    BOT_CHOICE = random.randrange(1, 4, 1)
    choice = 3
    if (BOT_CHOICE == 2) and (call.message.reply_to_message.from_user.id == call.from_user.id):
        text = "Ты выбрал бумагу, но у меня ножницы. Я победила!"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    elif (BOT_CHOICE == 1) and (call.message.reply_to_message.from_user.id == call.from_user.id):
        text = "Ты выбрал бумагу, а я - камень Я проиграла :("
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
        db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `exp` = exp + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
            db.commit()
            sql = "UPDATE `users` SET `points` = points + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
            db.commit()
            sql = "SELECT `exp`, `lvl` FROM `users` WHERE user_id = %s"
            cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
            result = cursor.fetchone()
            needexp = int(result['lvl']) * 100
            plustats = int(needexp) / 50
            if (int(result['exp']) >= needexp):
                ex2p = 0
                sql = "UPDATE `users` SET `exp` = %s WHERE user_id = %s"
                cursor.execute(sql, (int(ex2p), str(call.message.reply_to_message.from_user.id)))
                sql = "UPDATE `users` SET `lvl` = lvl + 1 WHERE user_id = %s"
                cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
                sql = "UPDATE `users` SET `atk` = atk + %s WHERE user_id = %s"
                cursor.execute(sql, (plustats, str(call.message.reply_to_message.from_user.id)))
                sql = "UPDATE `users` SET `hp` = hp + %s WHERE user_id = %s"
                cursor.execute(sql, (plustats, str(call.message.reply_to_message.from_user.id)))
                bot.send_message(id, "LVL UP. Статы повышены на +{0}.".format(str(plustats)))
                db.commit()
                sql = "SELECT `ref` FROM `users` WHERE user_id = %s"
                cursor.execute(sql, (str(call.message.reply_to_message.from_user.id)))
                isref = cursor.fetchone()
                if isref != None:
                    try:
                        refer = isref['ref']
                        sql = "SELECT `lvl` FROM `users` WHERE username = %s"
                        cursor.execute(sql, str(refer))
                        refer_by = cursor.fetchone()
                        needExpRef = int(refer_by['lvl']) * 100
                        refplus = int(needExpRef) / 5
                        sql = "UPDATE `users` SET `exp` = `exp` + %s WHERE `username` = %s"
                        cursor.execute(sql, (int(refplus), str(refer)))
                        db.commit()
                        db.close()
                        return
                    except:
                        bot.send_message(id, "Не смогли начислить реферальные очки @" + str(isref['ref']))
                        db.close()
                        return
                    else:
                        pass
                    db.close()
    elif (BOT_CHOICE == 3) and (call.message.reply_to_message.from_user.id == call.from_user.id):
        text = "У нас у обоих бумага. Ничья."
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    else:
        bot.send_message(call.message.chat.id, "@" + str(call.from_user.username) + ", Зачем ты лезешь играть, если играем не с тобой?")
