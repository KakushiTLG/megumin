@bot.message_handler(['help'])
def megacom(m):
	bot.reply_to(m, 'Взрыв!(!взрыв) !суицид /banme \n!игры /meme')
	
	
	
	
	
	
@bot.message_handler(['unmute'])
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
		
 
		
		
		
#@bot.message_handler(commands=['meme'])
#def send_rand_photo(message):
 #   filename = './media/memes/' + random.choice(['file1', 'file2', 'file3', 'file4', 'file5', 'file6', 'file7', 'file8', 'file9', 'file10', 'file11', 'file12', 'file13', 'file14', 'file15', 'file16', 'file17', 'file18', 'file19', 'file20', 'file21', 'file22', 'file23']) + '.jpg' # Simply select random file's name
 #   with open (filename, "rb") as file: # open it as binary file
  #      bot.send_photo(message.chat.id, file)