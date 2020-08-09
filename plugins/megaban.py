def megabanadm(m):
    bot_whoami = bot.get_chat_member(m.chat.id, m.from_user.id).status
    bot_time_timeban = random.randrange(30, 60, 1)
    bot_timeban = int(bot_time_timeban) * 60
    bot2_timeban = time.time()
    bot3_timeban = math.ceil(bot2_timeban)
    timebanbot = bot3_timeban + bot_timeban
    bot_whoare = m.reply_to_message.from_user.id
    megagif = random.randrange(1, 5, 1)
    if(m.chat.id != m.from_user.id):
        if(bot_whoami == 'administrator') or (bot_whoami == 'creator') or (bot_whoami in owner):
			#bot.reply_to(m, "Debug : " + str(bot_timeban))
            try:
                bot.restrict_chat_member(m.chat.id, bot_whoare, timebanbot, False)
                bot.reply_to(m, 'О, тьма, что темнее темного, лиши этого смертного голоса на ' + str(bot_time_timeban) + ' минут, высвободив всю свою мощь')
   #рандомную гиф взрыва и сюды
            except :
                bot.reply_to(m, 'Не смогла его взорвать. Но хоть побью.')
		
def megabanana(m):
	unbanbonus = random.randrange(10, 41, 1)
	unbanbonussec = unbanbonus * 60
	unbandata = time.time()
	unbandata2 = math.ceil(unbandata)
	unbandata3 = unbandata2 + unbanbonussec
	textunbandata = 'Ты че, забыл кто тут мать конфы? Полежи ка минут ' + str(unbanbonus)
	#добвь сюда время мута(1-10 мин)
	try : 
		bot.restrict_chat_member(m.chat.id, m.from_user.id, unbandata3, False)
		bot.reply_to(m, textunbandata)
	except :
		pass
		
def megatempban(m):
	if(m.chat.id != m.from_user.id) :
		unbanbonus = random.randrange(1, 21, 1)
		unbanbonussec = unbanbonus * 60
		unbandata = time.time()
		unbandata2 = math.ceil(unbandata)
		unbandata3 = unbandata2 + unbanbonussec
		textunbandata = 'Ты точно этого хочешь? Ну ладно, я лишу тебя голоса на ' + str(unbanbonus) + ' минут.'
		try :
			bot.restrict_chat_member(m.chat.id, m.from_user.id, unbandata3, False)
			bot.reply_to(m, textunbandata)
		except :
			pass
    
    
    
  