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

megu_words = ['Да пошла ты, Мегумин', 'Мегумин шлюха', 'Да ты охуела', 'Ебал я в рот Мегумин']
ReadyUsers()
sleepflood = 0
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    global sleepflood
    t=parse(message.text)
    if int(sleepflood) < math.ceil(time.time()): 
        sleepflood = math.ceil(time.time()) + 1
        if message.text.lower() in ['взрыв!','!взрыв']:
            dig(message.chat.id,message.from_user.username,message.from_user.id, message.message_id)
        if message.text.lower() in ['!маг','лучший!']:
            trophy(message.chat.id)
        if message.text.lower() in ['!взорви'] :
            megabanadm(message)
        if message.text.lower() in ['!суицид'] :
            megatempban(message)
        if message.text.lower() in ['!профиль'] :
            profileBeta (message)
        if message.text.lower() in ['!битва'] :
            startWresling (message)
        if message.text.lower() in ['!рулетка'] :
            roulleteBeta (message)
    else:
        print('Anti-Flood')
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


      
