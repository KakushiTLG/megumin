def getpoints(m,p):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT points FROM `users` WHERE `user_id` = '" + str(m.from_user.id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            print(result)
        else:
            sql = "INSERT INTO users (username, user_id, lvl, points, atk, hp) VALUES (%s, %s, '1', '0', '0', '0')"
            cursor.execute(sql, (str(m.from_user.username), str(m.from_user.id)))
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
        cursor.execute(sql, (w, str(m.from_user.id)))
        db.commit()
        db.close()
        


@bot.message_handler(commands=['help'])
def megacom(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT lvl, local FROM `users` WHERE `user_id` = '" + str(m.from_user.id) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        local = int(result['local'])
        db.close()
    if lvl >= 1:
        text = "\nУровень 1: \n!кнб\n !профиль \n /giveaway"
    if lvl >= 2:
        text += "\nУровень 2: \n !битва \n /shop \n Обновлённый !профиль"
    if lvl >= 3 :
        text += "\nУровень 3: \n !битва \n !кнб - недоступен\n!битва (мультиплеер, отправлять команду ответом своему противнику)"
    if (lvl == 7) and (local == 3):
        text += "\nУровень 7: \n/wrestling"
    bot.reply_to(m, 'Megumin, v.' + __version__ + '\n Команды: ' + text)





@bot.message_handler(commands=['donate'])
def donate(m):
    donateText = "Йоу, если ты тут, значит хочешь помочь разработчикам. Вообще, у меня есть договоренность, поэтому разработчикам твои деньги точно не пойдут в карман - на эти деньги ты продливаешь мою жизнь."
    donateText += "\nВ общем, 1 рубль = 50 pts. При донате от 50руб ты заодно и получаешь донат-статус. Что такое донат-статус?"
    donateText += "\nА это уже интересная штука, которая снизит шанс на проигрыш во взрыве (до 5%) и даст скидку в магазине на покупку статов. Ну и красивая зелёная галочка в профиле обеспечена"
    donateText += "\n''Да знаю я это все, дайте уже данные, куда отправлять деньги!!!''\nДеньги отправляются на QIWI-кошелёк владельца => 380957502014 \nНе забудь после всего этого написать в /report свой ник и сумму пожертвования для зачисления поинтов"
    donateText += "\nЕсли есть возможность - можно просто в примечание платежа написать свой ID в Kotomi."
    bot.reply_to(m, donateText)
    
    
    
    
    
@bot.message_handler(commands=['report'])
def report(m):
    if len(m.text.split(' ')) > 1:
        text = m.text.replace('/report ', '', 1)
        bot.reply_to(m, '@' + m.from_user.username + ' , спасибо за сообщение!')
        bot.forward_message(FOO, m.chat.id, m.message_id)
    else:
        bot.reply_to(m, 'Данная команда позволяет сообщить разработчикам о найденом баге или же о предложении по улучшению бота. Вводи /report и текст')
#

     

	
@bot.message_handler(commands=['unmute'])
def bot_ban(m):
	bot_whoami = bot.get_chat_member(m.chat.id, m.from_user.id).status
	bot_whoare = m.reply_to_message.from_user.id
	if(m.chat.id != m.from_user.id):
		if(bot_whoami == 'administrator') or (bot_whoami == 'creator'):
			try :
				bot.restrict_chat_member(m.chat.id, bot_whoare, 666, True, True, True, True)
				bot.reply_to(m, 'Надеюсь, он будет хорошо себя вести... ')
			except :
				pass
		
@bot.message_handler(commands=["leave"])
def leave(message):
    if str(message.from_user.id) in owner:
        text = message.text.replace('/leave ', '', 1)
        try:
            bot.send_message(text, "Пока-пока")
            bot.leave_chat(str(text))
        except:
            bot.reply_to(message, "Ошибочка")
    else:
        return
     

@bot.message_handler(commands=["w"])
def leave(m):
    if str(m.from_user.id) in owner:
        text = m.text.replace('/w ', '', 1)   
        if m.reply_to_message:
            text1 = m.reply_to_message.text
            text2 = text1.split(' ')
            text3 = text2[2]
            bot.send_message(text3, str(text))
        else:
            return
        
        
#@bot.message_handler(commands=["getuser"])
#def answer(message):
#    if str(message.from_user.id) in owner:
 #       userid = int(message.text.split(maxsplit=1)[1])
  #      UsrInfo = bot.get_chat_member(userid, userid).user
#        bot.reply_to(message, "Id: " + str(UsrInfo.id) + "\nFirst Name: " + str(UsrInfo.first_name) + "\nLast Name: " + str(UsrInfo.last_name) + "\nUsername: @" + str(UsrInfo.username))

@bot.message_handler(commands=["reboot"])
def rebootBot(message):
    if str(message.from_user.id) in owner:
        bot.reply_to(message, "Restarted")
        os.system("service megumin restart")
    else:
        return



		
@bot.message_handler(commands=['rp'])
def reply(m):
    if str(m.from_user.id) in owner:
        text = m.text.replace('/rp ', '', 1)
        report = bot.send_message(chancechat, text)
        bot.pin_chat_message(chancechat, report.message_id)
        
		
		
temp_data = {}
class ReadyUsers:
    voting = {}
    def __init__(self):
        bot.message_handler(commands=['ready'])(self.mainready)
        bot.callback_query_handler(func=lambda call: call.data.startswith('ready_'))(self.callback)

    def mainready(self, m):
        if str(m.from_user.id) not in owner:
            return
        msg = bot.reply_to(m, 'Генерирую кнопку.')
        text = 'Готовы к обновлению?'
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(telebot.types.InlineKeyboardButton("⚔️Готов(а)!",
                                                      callback_data="ready_" + str(msg.message_id) + '_' + str(
                                                          m.chat.id)))
        bot.edit_message_text(text, msg.chat.id, msg.message_id, reply_markup=markup)
        self.voting[str(msg.message_id) + str(m.chat.id)] = []
        temp_data[str(msg.message_id) + str(m.chat.id)] = text
        print (temp_data)
        try:
            bot.pin_chat_message(m.chat.id, msg.message_id)
        except:
            pass

    def callback(self, call):
        _data = call.data.split('_')
        try:
            if str(call.from_user.id) in self.voting[_data[1] + _data[2]]:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text="Ты уже отмечался о готовности.")
                return
            msg_text = temp_data[_data[1] + _data[2]]
            if 'Готовы?' in msg_text:
                msg_text = 'Готовые: \n'
            msg_text = msg_text + '\n<a href = "tg://user?id={}">{}</a>'.format(call.from_user.id,
                                                                                call.from_user.first_name)
            self.voting[_data[1] + _data[2]].append(str(call.from_user.id))
            temp_data[_data[1] + _data[2]] = msg_text
            markup = telebot.types.InlineKeyboardMarkup()
            markup.row_width = 1
            markup.add(telebot.types.InlineKeyboardButton("⚔️Готов(а)!", callback_data=call.data))
            bot.edit_message_text(msg_text, _data[2], _data[1], reply_markup=markup, parse_mode='Html')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Ты отметился о готовности.")
        except:
            bot.edit_message_text('Сообщение неактуально. ', _data[2], _data[1])
		
		



            
            
            
            
            
#@bot.message_handler(commands=['meme'])
#def send_rand_photo(message):
#    folder = 'img'
# format = '.jpg'
# enabled_plugins = [f for f in os.listdir(folder) if f.endswith(format)]