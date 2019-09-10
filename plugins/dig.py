import datetime


qdir='quotes'
mdir='mquotes'
		
		
		



#def hotet(m):
 #   try:
 #       bot.send_message(m.chat.id,"*{0}* чего-то хочет".format(m.from_user.username), None, None, None,'markdown')
 #   except:
 #       pass
		
	
def getdigrecord(id):
    try:
        f=open(qdir+'\quotes{0}digr.txt'.format(id),encoding='utf-8')
        rec=f.read().splitlines()
        f.close()
        maxweight=int(rec[0])
        recname=rec[1]
        recart=rec[2]
    except:
        f=open(qdir+'\quotes{0}digr.txt'.format(id),'w',encoding='utf-8')
        f.write(u'\n'.join(['0','Мегумин','Лучший взрыв']))
        f.close()        
        recname="Мегумин"
        maxweight=0
        recart="Лучший взрыв"
    return [maxweight,recname,recart]

def trophy(id):
        [weight,player,recart]=getdigrecord(id)
        bot.send_message(id,"*{0}* стал лучшим архимагом, взорвав *{1}*! сила взрыва - *{2}*.".format(player,recart,weight), None, None, None,'markdown')
    
def putdigrecord(id,w,p,a):
    try:
        f=open(qdir+'\quotes{0}digr.txt'.format(id),'w',encoding='utf-8')
        f.write(u'\n'.join([str(w),str(p),str(a)]))
        f.close()   
    except:
        pass
 
timesleepdig = 0

def dig(id,playerid,meesa):
    record=getdigrecord(id)
    nump=random.randint(0,len(digp)-1)
    numt=random.randint(0,len(digt)-1)
    nume=random.randint(1,len(dige)-1)
    weight=random.randint(0,record[0]+100)
    megaro = random.randint(0,100)
    timebanbot = math.ceil(time.time()) + 60
    freepoint = random.randint(0,100)
    exprec = random.randint(2,15)
    randomexp = random.randint(2, 8)
    randomdig = random.randint(0, 300)
    global timesleepdig
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl`, `username` FROM `users` WHERE user_id = %s"
        cursor.execute(sql, (playerid))
        result = cursor.fetchone()
        player = result['username']
        if player:
            pass
        else:
            bot.reply_to(m, "Зарегистрируйтесь, введя команду !профиль")
            return
        lvl = int(result['lvl'])
    if (lvl >= 3) :
        bot.send_message(id, "Взрывы доступны до третьего уровня.")
        return
    else:
        pass
    if int(timesleepdig) < math.ceil(time.time()): 
        pass
    else:
        dig = bot.send_message(id, "Оглянувшись по сторонам,*@{0}* не нашел что можно взорвать.".format(player), None, None, None,'markdown')
        return
    if (randomdig == 1) :
        botdig = bot.send_message(id,"Неправильно произнеся заклинание, *{0}* призвал *Мегумин*, которая взорвала 💥*ВСЕ ВОКРУГ*💥! Восстановление после таких погромов займет около часа".format(player), None, None, None,'markdown')
        timesleepdig = math.ceil(time.time()) + 3600
        return
    else:
        pass
    #bot.send_message(id,"Вы начали раскопки *{0}* и усиленно роете лопатами, экскаватором... Вам кажется что ваш совочек ударился обо что-то твердое. Може это клад?!".format(digp[nump]), None, None, None,'markdown')
    if random.randint(0,1) :
        if (freepoint<70) and (id == chancechat):
            randompoint = random.randint(2, 6)
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "UPDATE `users` SET `points` = points + %s WHERE user_id = %s"
                cursor.execute(sql, (int(randompoint), playerid))
                db.commit()
                sql = "UPDATE `users` SET `exp` = exp + %s WHERE user_id = %s"
                cursor.execute(sql, (int(randomexp), playerid))
                db.commit()
                botdig = bot.send_message(id,"Начав использовать заклинание *{0}* , *{1}*  только что взорвал *{2}*, сила взрыва - *{3}*! Такой взрыв я оценила в *{4}* поинта. Начислено *{5} опыта*".format(digp[nump],player,digt[numt],weight, str(randompoint), str(randomexp)), None, None, None,'markdown')
                sql = "SELECT `lvl`, `exp` FROM `users` WHERE `user_id` = %s"
                cursor.execute(sql, (playerid))
                result = cursor.fetchone()
            db.close()
            needexp = int(result['lvl']) * 100
            plustats = int(needexp) / 50
            if (int(result['exp']) >= needexp):
                ex2p = 0
                db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
                with db.cursor() as cursor:
                    sql = "UPDATE `users` SET `exp` = %s WHERE user_id = %s"
                    cursor.execute(sql, (int(ex2p), playerid))
                    sql = "UPDATE `users` SET `lvl` = lvl + 1 WHERE user_id = %s"
                    cursor.execute(sql, (playerid))
                    sql = "UPDATE `users` SET `atk` = atk + %s WHERE user_id = %s"
                    cursor.execute(sql, (plustats, playerid))
                    sql = "UPDATE `users` SET `hp` = hp + %s WHERE user_id = %s"
                    cursor.execute(sql, (plustats, playerid))
                    bot.send_message(id, "LVL UP. Статы повышены на +{0}.".format(str(plustats)))
                    db.commit()
                    sql = "SELECT `ref` FROM `users` WHERE user_id = %s"
                    cursor.execute(sql, (str(playerid)))
                    isref = cursor.fetchone()
                    if isref:
                        try:
                            refer = isref['ref']
                            sql = "SELECT `lvl` FROM `users` WHERE username = %s"
                            cursor.execute(sql, str(refer))
                            refer_by = cursor.fetchone()
                            needExpRef = int(refer_by['lvl']) * 100
                            refplus = int(needExpRef) / 5
                            sql = "UPDATE `users` SET `exp` = `exp` + %s WHERE `username` = %s"
                            cursor.execute(sql, (int(plustats), str(refer)))
                            db.commit()
                            db.close()
                            return
                        except:
                            bot.send_message(id, "Не смогли начислить реферальные очки " + str(isref['ref']))
                            db.close()
                            return
                    else:
                        pass
                db.close()
        else:
            botdig = bot.send_message(id,"Начав использовать заклинание *{0}* , *{1}*  только что взорвал *{2}*, сила взрыва - *{3}*!".format(digp[nump],player,digt[numt],weight), None, None, None,'markdown')
        if weight>int(record[0]):
            putdigrecord(id,weight,player,digt[numt])
            botdig = bot.send_message(id,"*Ого!!! Это новый рекорд! Похоже ты сильнейший волшебник здесь, после меня конечно же, {0}. Напиши лучший! чтобы это увидеть!*\nПолучено {1} опыта".format(player, str(exprec)), None, None, None,'markdown')
            bot.send_video(id, open('./media/best.mp4', 'rb'))
            if (id == chancechat):
                db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                with db.cursor() as cursor:
                    sql = "UPDATE `users` SET `exp` = exp + %s WHERE user_id = %s"
                    cursor.execute(sql, (int(exprec), playerid))
                    db.commit()
                    sql = "SELECT `exp`, `lvl` FROM `users` WHERE user_id = %s"
                    cursor.execute(sql, (playerid))
                    result = cursor.fetchone()
                    needexp = int(result['lvl']) * 100
                    plustats = int(needexp) / 50
                    if (int(result['exp']) >= needexp):
                        ex2p = 0
                        sql = "UPDATE `users` SET `exp` = %s WHERE user_id = %s"
                        cursor.execute(sql, (int(ex2p), playerid))
                        sql = "UPDATE `users` SET `lvl` = lvl + 1 WHERE user_id = %s"
                        cursor.execute(sql, (playerid))
                        sql = "UPDATE `users` SET `atk` = atk + %s WHERE user_id = %s"
                        cursor.execute(sql, (plustats, playerid))
                        sql = "UPDATE `users` SET `hp` = hp + %s WHERE user_id = %s"
                        cursor.execute(sql, (plustats, playerid))
                        bot.send_message(id, "LVL UP. Статы повышены на +{0}.".format(str(plustats)))
                        db.commit()
                        sql = "SELECT `ref` FROM `users` WHERE user_id = %s"
                        cursor.execute(sql, (str(playerid)))
                        isref = cursor.fetchone()
                        if isref:
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
         #   except:
          #  	print("Не вышло с дига")
    else:
        if str(playerid) in donators:
            if (megaro <=10):
                try:
                    bot.restrict_chat_member(id, playerid, timebanbot, False)
                    botdig = bot.send_message(id, " *{0}*, я видела галочку в твоем профиле, но твое везение на этом кончено. Лишаю тебя голоса на минуту!".format(player), None, None, None, 'markdown')
                    bot.send_video(id, open('./media/ololo.mp4', 'rb'))
                    return
                except:
                    botdig = bot.send_message(id,"Начиная использовать заклинание *{0}*, *{1}*, вы ничего не взорвали! Но *{2}*. Может, попробуешь еще раз?".format(digp[nump],player,dige[nume]), None, None, None,'markdown')
                    return
            else :
                botdig = bot.send_message(id,"Начиная использовать заклинание *{0}*, *{1}*, вы ничего не взорвали! Но *{2}*.Может, попробуешь еще раз?".format(digp[nump],player,dige[nume]), None, None, None,'markdown')
                return
        if (megaro <= 30):
            try:
                bot.restrict_chat_member(id, playerid, timebanbot, False)
                botdig = bot.send_message(id, "Кажется *{0}* неправильно произнес заклинание и лишил себя голоса на минуту.".format(player), None, None, None, 'markdown')
                bot.send_video(id, open('./media/ololo.mp4', 'rb'))
            except:
                botdig = bot.send_message(id,"Начиная использовать заклинание *{0}*, *{1}*, вы ничего не взорвали! Но *{2}*. Может, попробуешь еще раз?".format(digp[nump],player,dige[nume]), None, None, None,'markdown')
        else :
            botdig = bot.send_message(id,"Начиная использовать заклинание *{0}*, *{1}*, вы ничего не взорвали! Но *{2}*.Может, попробуешь еще раз?".format(digp[nump],player,dige[nume]), None, None, None,'markdown')
    try :
        pass
    except:
        pass
   # tt = Timer(360.0 , bot.delete_message , [id, botdig.message_id])
  #  tt.start()
 #   bot.delete_message(id, botdig.message_id)
    
    
def wlog(name,text):
    try:
        log=open(name,'a',encoding='utf-8')
        today = datetime.datetime.today()
        log.write(today.strftime("[%Y.%m.%d %H:%M:%S] ") +text+"\n")
        log.close()
    except:
        log=open(name,'w',encoding='utf-8')
        today = datetime.datetime.today()
        log.write(today.strftime("[%Y.%m.%d %H:%M:%S] ") +text+"\n")
        log.close()