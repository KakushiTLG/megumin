def parse(message):
    try:
        t=message.split()
        cmd=t[0]
        par=''
    except:
        return ['','']
    if len(t)>1:
        par=' '.join(t[1:])
    return [cmd,par]   
megu_words = ['Да пошла ты, Kotomi', 'Kotomi шлюха', 'Да ты охуела', 'Ебал я в рот Kotomi']
ReadyUsers()
sleepflood = {}
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе 
    # Чекушов пидор, ня :3
    t=parse(message.text)
    bot.send_message(otorhinid, " Сообщение в " + str(message.chat.id) + " \nText: " + str(t) + "\nBy: @" + str(message.from_user.username))
    if message.from_user.id not in sleepflood:
    	sleepflood[message.from_user.id] = 0
    else:
        pass
    if int(sleepflood[message.from_user.id]) <= time.time():
        if message.text.lower() in ['взрыв!','!взрыв']:
            dig(message.chat.id,message.from_user.id, message.message_id)
        if message.text.lower() in ['!маг','лучший!']:
            trophy(message.chat.id)
        if message.text.lower() in ['!взорви'] :
            megabanadm(message)
        if message.text.lower() in ['!суицид'] :
            megatempban(message)
        if message.text.lower() in ['!профиль'] :
            profileBeta (message)
        if message.text.lower() in ['!кнб'] :
            startgame (message)
        if message.text.lower() in ['!битва'] :
            m = message
            otrh_battle (m)
        if message.text.lower() in ['!кража'] :
            krazha (message)
        if message.text.lower() in ['!рулетка'] :
            m = message
            roulette (message)
        if message.text.lower() in ['!кости','кости!']:
            m = message
            kosti(m)
            
    else:
        print('Anti-Flood')
    
    sleepflood[message.from_user.id] = round(time.time()) + 2
 #   meggban = 0 
 #   for megubanner in megu_words :
    #    megubanner = message.text.lower()
    #    megbanner = megubanner.count(megubanner)
   #     if megbanner != 0 :
   #         meggban += 1
#    if (meggban != 0) :
   #      megabanana(message) 
#    if message.text.lower() in megu_words :
    #    megabanana(message) 


      
