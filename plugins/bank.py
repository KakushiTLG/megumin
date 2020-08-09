@bot.message_handler(commands=['bank'])
def bank(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT bankNo, bankInv FROM users WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        bankNo = int(result['bankNo'])
        bankInv = int(result['bankInv'])
        db.close()
    if bankNo != 0:
        pass
    else:
        bot.reply_to(m, "У вас отстуствует банковская ячейка. Приобрести её можно в /shop.")
        return
    text = "Добро пожаловать в банк. Тут вы можете внести депозит или же вывести деньги с депозита.\nВаш текущий депозит: {} pts".format(str(bankInv))
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('Внести депозит', callback_data="makeInv"))
    markup.add(InlineKeyboardButton('Вывести деньги с счёта', callback_data="takeInv"))
    bot.reply_to(m, text, reply_markup=markup)
    



@bot.callback_query_handler(func=lambda call: call.data.startswith('makeInv'))
def makeInv(call): 
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    username = call.from_user.id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("50", callback_data="playerMakeInv:50:{}".format(username)), InlineKeyboardButton("100", callback_data="playerMakeInv:100:{}".format(username)), InlineKeyboardButton("250", callback_data="playerMakeInv:250:{}".format(username)), InlineKeyboardButton("500", callback_data="playerMakeInv:500:{}".format(username)), InlineKeyboardButton("1000", callback_data="playerMakeInv:1000:{}".format(username)))
    text = "Выберите сумму, которую хотите внести в депозит."
    gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
    
    
    
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('playerMakeInv:'))
def playerMakeInv(call):
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    Inv = call.data.split(':')
    InvSum = int(Inv[1])
    InvWho = Inv[2]
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT points FROM users WHERE user_id = %s"
        cursor.execute(sql, (call.from_user.id))
        result = cursor.fetchone()
        points = int(result['points'])
        if points >= InvSum:
            pass
        else:
            text = "У вас недостаточно поинтов."
            gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
            db.close()
            return
        sql = "UPDATE `users` SET `points` = points - %s WHERE `user_id` = %s"
        cursor.execute(sql, (InvSum, InvWho))
        db.commit()
        sql = "UPDATE `users` SET `bankInv` = bankInv + %s WHERE `user_id` = %s"
        cursor.execute(sql, (InvSum, InvWho))
        db.commit()
        db.close()
    text = "Вы успешно внесли депозит в размере {} pts.".format(str(InvSum))
    gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    return





@bot.callback_query_handler(func=lambda call: call.data.startswith('takeInv'))
def takeInv(call): 
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    username = call.from_user.id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("50", callback_data="playerTakeInv:50:{}".format(username)), InlineKeyboardButton("100", callback_data="playerTakeInv:100:{}".format(username)), InlineKeyboardButton("250", callback_data="playerMakeInv:250{}".format(username)), InlineKeyboardButton("500", callback_data="playerTakeInv:500:{}".format(username)), InlineKeyboardButton("1000", callback_data="playerTakeInv:1000:{}".format(username)))
    text = "Выберите сумму, которую хотите вывести с депозит-счёта."
    gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
    
    
    
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('playerTakeInv:'))
def playerTakeInv(call):
    if (call.from_user.id == call.message.reply_to_message.from_user.id):
        pass
    else:
        return
    Inv = call.data.split(':')
    InvSum = int(Inv[1])
    InvWho = Inv[2]
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT bankInv FROM users WHERE user_id = %s"
        cursor.execute(sql, (call.from_user.id))
        result = cursor.fetchone()
        bankInv = int(result['bankInv'])
        if bankInv >= InvSum:
            pass
        else:
            bot.reply_to(m, "У вас недостаточно средств на банковском счёте.")
            db.close()
            return
        sql = "UPDATE `users` SET `points` = points + %s WHERE `user_id` = %s"
        cursor.execute(sql, (InvSum, InvWho))
        db.commit()
        sql = "UPDATE `users` SET `bankInv` = bankInv - %s WHERE `user_id` = %s"
        cursor.execute(sql, (InvSum, InvWho))
        db.commit()
        db.close()
    text = "Вы успешно вывели из депозит-счёта {} pts.".format(str(InvSum))
    gg = bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    return
