import random

@bot.message_handler(['banme'])
def bot_banme(m):
	if(m.chat.id != m.from_user.id) and (m.chat.id != otorhinchat) :
		unbanbonus = random.randrange(1, 101, 1)
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
			
		
		
@bot.message_handler(['ban'])
def bot_ban(m):
	bot_whoami = bot.get_chat_member(m.chat.id, m.from_user.id).status
	bot_whoare = m.reply_to_message.from_user.id
	if(m.chat.id != m.from_user.id):
		if(bot_whoami == 'administrator') or (bot_whoami == 'creator'):
			try :
				bot.restrict_chat_member(m.chat.id, bot_whoare, 666, False)
				bot.reply_to(m, 'О, тьма, что темнее темного, лиши этого смертного голоса на ' + str(bot_time_timeban) + ' минут, высвободив всю свою мощь')
			except :
				pass