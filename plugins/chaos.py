def chaos(m):
    try :
        bot.send_video(m.chat.id, open('./media/chaos/start.mp4', 'rb'), reply_to_message_id = m.message_id)
    except Exception as e:
        print (e)
    bot.reply_to(m, 'Ты сейчас про меня что-то вякнул?!')
        
        
        
@bot.message_handler(['stopchaos'])
def bot_stopchaos(m):
    if (m.from_user.id == otorhinid):
        bot.send_video(m.chat.id, open('./media/chaos/stop.mp4', 'rb'), reply_to_message_id = m.message_id)
        bot.reply_to(m, 'Хорошо что этот ад закончился')