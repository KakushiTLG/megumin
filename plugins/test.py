import datetime
import math
import time
import os
folder = 'mquotes'
format = '.txt'
nick = []
#@bot.message_handler(commands=['list'])
def list(m):
    nick = []
    enabled_points = [f for f in os.listdir(folder) if f.endswith(format)]
    for points in enabled_points:
        try:
            f = open("./mquotes/" + points , encoding="utf-8")
            rec = f.read().splitlines()
            print ("Подключен " + points)
            nn = rec
            nick.append(nn)
      #  max_num = max(int(rec[0]) for points in enabled_points)
        except Exception as e:
            print("Ошибка подключения " + points) 
            print (e)
    time.sleep(10)
    bot.reply_to(m, 'Список: ' + str(nick) )