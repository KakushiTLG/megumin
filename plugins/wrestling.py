import threading
eventTitles = ["быкануть на администратора", "спрыгнуть с Чиллиада", "поймать бизнес Майорова", "подать объявление в /adv", "стать лидером фракции", "оплатить дом в банке", "купить туризмо у Линка", "узнать, когда закончится срок Саска", "устроить РП", "провести Character Kill", "слетать в деморган на вертолёте", "убить Kotomi"]
enemyMobsName = [" таксист из гетто", " первый лидер ФБР", " багоюзер", " обладатель НонРп ника", " лидер мафии", " улетевший на вертолете из деморгана читер", " гражданский вертолетчик", " подозрительный человек, представившийся как пожилой арангутан", " англичанин", "и разработчики", " арестованный у притона бандит", " полицейский в костюме медика", "о обновление Chance", "а Анна Антипова", " турист с АК-47", " Винтер Фокс", " шелдонлёт", " водитель автобуса", "а Ваша шизофрения", "а Kotomi"]
battleTitles = ["сказав, что вызывает ментов", "попросив вас написать /q", "предлагая вам деньги", "явно со злыми намерениями посмотрев на вас", "предлагая отойти за угол", "спрашивая, что такое МГ", "используя пауэр гейминг", "демонстрируя техники из Наруто", "приглашая через /d перевестись в ФБР", "вызывая на гачи-борьбу", "устанавливая вам постороннее ПО", "устроив кошмар в душевой LSPD", "собираясь отправить вас в бан", "кидая инвайт в LVA", "начав эпическое сражение", "предлагая оплатить налог на паспорт", "закидывая на мобилку 100к", "делающий подозрительный /time", "доставая ствол", "выбивающий налог на паспорт", "вводя вашу рефералку"]

timesleep = 0
pvpBattle = False
def startWresling(message):
    global timesleep
    global pvpBattle
    if message.chat.id != chancechat:
        bot.reply_to(message, "Прости, я работаю только в @chance_estate")
        return
    if int(timesleep) < math.ceil(time.time()): 
        
        db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='maz1aan16v',                             
                                 db='Megumin',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "SELECT * FROM `users` WHERE `user_id` = %s"
            cursor.execute(sql, (message.from_user.id))
            result = cursor.fetchone()
            playerHealth = result['hp'] # ебани связь мускула с этой хуйней
            playerAttack = result['atk'] #и с этой
            firstAttackChance = result['fatk'] # и с этой
            critAttackChance = result['creet'] # и с этоi
            location = result['local']
            lvl = result['lvl']
            location = int(result['local'])
            player = result['username']
            nowhp = result['nowhp']
            if player:
                pass #это чето Линка
            else:
                bot.reply_to(m, "Нужно зарегистрироваться.")
                return
            db.close()
        if int(lvl) < 3 :
            bot.reply_to(message, "У тебя нет третьего уровня для доступа к игре")
            return
        else:
            pass
        if int(nowhp) < int(playerHealth):
            bot.reply_to(message, "Ты еще не до конца поправился. Пойди еще отдохни. \n У тебя {}/{} ❤️ здоровья".format(str(nowhp), str(playerHealth)))
            return
        else:
            pass
        uFN = player
        uC = " " #message.chat.id
        m = message
        randomGojiraSpawn = random.randint (1, 300) #шанс спавна годзиллы
        
        pFA = False 
        minHpMob = int(playerHealth) / 1.5 # для радиуса поиска
        maxHpMob = int(playerHealth) * 1.5 # для радиуса поиска
        minAtkMob = int(playerAttack) / 1.5 # для радиуса поиска
        maxAtkMob = int(playerAttack) * 1.5 # для радиуса поиска
        BMplayer = int(playerAttack + playerHealth + ((firstAttackChance/100) * 10))
        BMmobMin = int(BMplayer + (BMplayer * 0.15))
        BMmobMax = int(BMplayer - (BMplayer * 0.15))
        try:
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='maz1aan16v',                             
                                 db='Megumin',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "SELECT * FROM wrestling WHERE atk > %s AND atk < %s AND hp > %s AND hp < %s AND localspawn = %s"
                cursor.execute(sql, (minAtkMob, maxAtkMob, minHpMob, maxHpMob, location))
                mobchar = cursor.fetchall()
                mobchar1 = random.choice(mobchar)
                mobAtk = mobchar1['atk'] # поменяй названия переменных на свои
                mobHp = mobchar1['hp'] # и тут
                mobName = mobchar1['mobname'] # и тут
            db.close()
        except:
            bot.reply_to(m, "В твоей локации кончились мобы")
            return
        enemyMob = mobName #это эта херня отвечает жа имя врага
        eventTitle = random.choice(eventTitles)
        battleTitle = random.choice(battleTitles) #это сценарий, см списки в самом верху
        
        enemyMobRandomHealth = mobHp
        enemyMobRandomAttack = mobAtk #тут понятно
        enemyMobStackHp = enemyMobRandomHealth
        playerStackHp = playerHealth
        
        critStr = " "
    #    firstAttackChance = 2
        randomFirstAttack = random.randint (1, 100) #для решения, кто первый атакует
        critStack = 0
        if randomGojiraSpawn == 1: #это ставит мобу статы годзиллы если рандом сработает
            enemyMobRandomAttack = 666
            enemyMobStackHp = 9999
            enemyMobRandomHealth = 9999       
        winner = -1
        #print("Сгенерированные значения: ", playerHealth, playerAttack, enemyMobRandomHealth, enemyMobRandomAttack, "\nИзменения здоровья: ", playerStackHp, enemyMobStackHp)    
        eMSA = 0 #суммарный урон врага
        pSA = 0 #и игрока
        enemyFirstAttack = 0
        enemyCrit = 0
        enemyCritStack = 0
        randomFirstAttacker = random.randint(0, 1)
        if m.reply_to_message: #если сообщение ответом то
            if int(lvl) >= 4 :
                pass
            else:
                bot.reply_to(m, "У вас нет 4 уровня для открытия мультиплеера")
                return
            player2 = m.reply_to_message.from_user.id # получении айди второго игрока
            if str(player2) == str(message.from_user.id):
                bot.reply_to(m, "Играй сам с собой в своем воображении.")
                return
            if str(player2) == str('710957371'):
                enemyMobStackHp = 1000000
                enemyMobRandomHealth = 1000000
                enemyMobRandomAttack = 1000
                enemyFirstAttack = 100
                enemyCrit = 100 #это всё Линк
                enemyMob = " МЕГУМИН"
                bot.reply_to(m, "Зря ты, " + uFN + ", быкануть решил...")
                time.sleep(5)
            else:
                db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='maz1aan16v',                             
                                 db='Megumin',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
                with db.cursor() as cursor:
                    sql = "SELECT * FROM `users` WHERE `user_id` = %s"                
                    cursor.execute(sql, (player2))   
                    result = cursor.fetchone()
                    enemyMobStackHp = result['hp']  # выставляем переменные мобу
                    enemyMobRandomHealth = result['hp']
                    enemyMobRandomAttack = result['atk'] 
                    enemyMob = result['username'] # имя моба.
                    enemyFirstAttack = int(result['fatk'])
                    enemyCrit = int(result['creet'])         
                    enemyLvl = int(result['lvl'])
                    enemylocation = int(result['local'])               
                db.close()
                if (location == enemylocation):
                    pass
                else:
                    bot.reply_to(m, "Вы с противником находитесь в разных локациях.")
                    return
                if enemyLvl >= 4:
                    db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='maz1aan16v',                             
                                 db='Megumin',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
                    with db.cursor() as cursor:
                        sql = "UPDATE `users` SET `points` = points - 4 WHERE user_id = %s"
                        cursor.execute(sql, (m.from_user.id))
                        db.commit()
                        db.close()
                else:
                    bot.reply_to(message, "У противника нет 4 уровня")
                    return
                pvpBattle = True
                enemyCritStack = 0
          

              
                
                
        critStrEnemy = "\n"
        while True:  
            randomCritAttack = random.randint (1, 100)
    
      #      bot.reply_to(message, str(randomFirstAttack))
      #тут идёт чек кто первый атакует
            if pvpBattle == True and firstAttackChance == enemyFirstAttack:
                if randomFirstAttacker == 0: 
                    firstAttackChance = firstAttackChance - 1
                else: enemyFirstAttack = enemyFirstAttack - 1
            if pvpBattle == False and firstAttackChance <= randomFirstAttack or pvpBattle == True and firstAttackChance < enemyFirstAttack:
                playerStackHp = playerStackHp - enemyMobRandomAttack
                if enemyCrit > critAttackChance:
                    enemyCritStack = enemyCritStack + 1
                    eMSA = eMSA + enemyMobRandomAttack
                enemyMobStackHp = enemyMobStackHp - playerAttack
                pFA = True
                if pvpBattle == False and critAttackChance >= randomCritAttack or pvpBattle == True and critAttackChance > enemyCrit:
                    enemyMobStackHp = enemyMobStackHp - playerAttack
                    critStack = critStack + 1
                    pSA = pSA + playerAttack
 
                   
            else:
                enemyMobStackHp = enemyMobStackHp - playerAttack
                #тут идёт чек крита и сам поединок
                if critAttackChance >= randomCritAttack:
                    enemyMobStackHp = enemyMobStackHp - playerAttack
                    critStack = critStack + 1
                    pSA = pSA + playerAttack
                playerStackHp = playerStackHp - enemyMobRandomAttack   
                if enemyCrit > critAttackChance and pvpBattle == True:
                    enemyCritStack = enemyCritStack + 1
                    eMSA = eMSA + enemyMobRandomAttack 
            eMSA = eMSA + enemyMobRandomAttack
            pSA = pSA + playerAttack
            if playerStackHp > enemyMobStackHp:
                if playerStackHp >= 1:
                    if enemyMobStackHp <= 0:
                        winner = 0
                        enemyMobStackHp = 0
                elif playerStackHp < 1:
                    winner = 6 #не ебу откуда тут 6
                    playerStackHp = 0
                    enemyMobStackHp = 1
                else:
                    print("Ошибка\#1")
                    bot.reply_to(m, "Ошибка. FA:" + str(randomFirstAttack) + " " + uC + uFN + " Здоровье и атака: " + playerHealth + " " + playerAttack + " Моб :" + enemyMobRandomHealth + " " + enemyMobRandomAttack + " Стэки: " + playerStackHp + " " + enemyMobStackHp)
                    break #тут высчет победителя
            elif enemyMobStackHp > playerStackHp:
                if enemyMobStackHp >= 1:
                    if playerStackHp <=0:
                        playerStackHp = 0
                        winner = 1 #враг вин
                        if randomGojiraSpawn <= 1:
                            winner = 3
                elif enemyMobStackHp < 1:
                    winner = 5
                    playerStackHp = 1
                    enemyMobStackHp = 0
            elif enemyMobStackHp == playerStackHp:
                if playerStackHp <=0:
                    winner = 2 #ничья
                    playerStackHp = 0
                    enemyMobStackHp = 0
                else:
                    continue
            if winner != -1:
                if critStack >= 1:
                    critStr = str("За бой ты смог нанести критический удар " + str(critStack) + " раз. ")
                if enemyCritStack >= 1:
                    critStrEnemy = "\nВраг нанес вам критический удар " + str(enemyCritStack) + " раз.\n"

#                if winner > 0 and critStack >= 1:
#                    critStr = str("За бой ты смог нанести критический удар " + str(critStack) + " раз. Но это не помогло одержать верх в битве...\n ")
                searchMob = bot.reply_to(m, "Подготовка к бою...")
                timesleep = math.ceil(time.time()) + 2
                timersearch = random.randint(2, 6) #тут снова Линк
                t = Timer(timersearch, battleResult, [m, lvl, searchMob, critStrEnemy, pFA, critStr, randomFirstAttack, eMSA, pSA, enemyMob, eventTitle, battleTitle, randomGojiraSpawn, uC, uFN, winner, playerHealth, playerAttack, enemyMobRandomAttack, enemyMobRandomHealth, playerStackHp, enemyMobStackHp])
                t.start()
          #      battleResult(m, searchMob critStrEnemy, pFA, critStr, randomFirstAttack, eMSA, pSA, enemyMob, eventTitle, battleTitle, randomGojiraSpawn, uC, uFN, winner, playerHealth, playerAttack, enemyMobRandomAttack, enemyMobRandomHealth, playerStackHp, enemyMobStackHp)
                break
    else:
        bot.reply_to(message, "Прости, " + str(message.from_user.username) + ", не смогла подобрать тебе врага.")
    #функция подсчёта результатов ниже    
def battleResult(m, lvl, searchMob, critStrEnemy, pFA, critStr, randomFirstAttack, eMSA, pSA, enemyMob, eventTitle, battleTitle, randomGojiraSpawn, uC, uFN, winner, playerHealth, playerAttack, enemyMobRandomAttack, enemyMobRandomHealth, playerStackHp, enemyMobStackHp):
    global timesleep
    global pvpBattle
    #говнокод с дублированием переменных
    pH = str(playerHealth)
    pA = str(playerAttack)
    eMRH = str(enemyMobRandomHealth)
    eMRA = str(enemyMobRandomAttack)
    pSH = "*" + str(playerStackHp) + "*"
    eMSH = "*" + str(enemyMobStackHp) + "*"
    uC = str(uC)
    uFN = str(uFN)
    pSA = str(pSA)
    eMSA = str(eMSA)
    mTrue = " "
    winnerStr = "Победила Kotomi"
    eM = enemyMob
    bT = battleTitle
    fA = randomFirstAttack
    
    bYS = ", но на вас напал"
    
    if pFA == True:
        fA = "Враг вкусил вашей первой атаки."
        bYS = ", но вас встретил"
    else:
        fA = "Враг атаковал вас первым."
    
   # print("Функция battleResult работает")
    if randomGojiraSpawn <= 1:
        eM = "а 🐲ГОДЗИЛЛА🐲"
        #сам подсчёт ниже
    if pvpBattle == True:
        eM = " игрок *" + str(enemyMob) + "*"
        enemyMob = eM
        bT = "с которым вы завязали битву"
    if winner == 0:
        if str(m.chat.id) == str(chancechat):
            randPointr = random.randint(3, 6)
            randPoint = int(lvl) * randPointr
            
            winnerStr = "К счастью, победа на твоей стороне! Ты получаешь " + str(randPoint) + " поинтов."
            db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "UPDATE `users` SET `points` = points + %s WHERE user_id = %s"
                cursor.execute(sql, (int(randPoint), m.from_user.id))
                db.commit()
                db.close()
            chanceexp = 1
            if chanceexp == 1:
                db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                with db.cursor() as cursor:
                    sql = "SELECT `lvl` FROM `users` WHERE user_id = %s"
                    cursor.execute(sql, (m.from_user.id))
                    result = cursor.fetchone()
                    randExp = random.randint(3, 6)
                    expgive_count = int(result['lvl']) * 0.5 * randExp
                    expgive = int(expgive_count)
                    db.commit()
                db.close()
                winnerStr += "В дополнение, " + str(expgive) + " ед. опыта."
                db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                with db.cursor() as cursor:
                    sql = "UPDATE `users` SET `exp` = exp + %s WHERE user_id = %s"
                    cursor.execute(sql, (int(expgive), m.from_user.id))
                    db.commit()
                    sql = "SELECT `exp`, `lvl` FROM `users` WHERE user_id = %s"
                    cursor.execute(sql, (m.from_user.id))
                    result = cursor.fetchone()
                    needexp = int(result['lvl']) * 100
                    plustats = int(needexp) / 50
                    if (int(result['exp']) >= needexp):
                        ex2p = 0
                        sql = "UPDATE `users` SET `exp` = %s WHERE user_id = %s"
                        cursor.execute(sql, (int(ex2p), m.from_user.id))
                        db.commit()
                        sql = "UPDATE `users` SET `lvl` = lvl + 1 WHERE user_id = %s"
                        cursor.execute(sql, (m.from_user.id))
                        sql = "UPDATE `users` SET `atk` = atk + %s WHERE user_id = %s"
                        cursor.execute(sql, (plustats, m.from_user.id))
                        sql = "UPDATE `users` SET `hp` = hp + %s WHERE user_id = %s"
                        cursor.execute(sql, (plustats, m.from_user.id))
                        bot.send_message(m.chat.id, "LVL UP. Статы повышены на +{0}.".format(str(plustats)))
                        db.commit()
                    db.close()
    elif winner == 1:
        winnerStr = "К несчастью, победил*" + str(enemyMob) + "*. "
        try:
            bot_time_timeban = 5
            bot_timeban = int(bot_time_timeban) * 60
            bot2_timeban = time.time()
            bot3_timeban = math.ceil(bot2_timeban)
            timebanbot = bot3_timeban + bot_timeban
            bot.restrict_chat_member(m.chat.id, m.from_user.id, timebanbot, False)            
            db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "UPDATE `users` SET `nowhp` = 0 WHERE user_id = %s"
                cursor.execute(sql, (m.from_user.id))
                db.commit()
                db.close()
            mTrue = " Отдохни пять минут, восстанови силы и возвращайся."
        except:
            mTrue = " Надо бы подлатать раны. Но, так как у тебя активирована аура восстановления, отдых тебе не нужен."
    elif winner == 2:
        winnerStr = "Это было так сложно, что в итоге пришлось отступить обоим. Ничья."
    elif winner == 3:
        winnerStr = "К сожалению, победила 🐲*ГОДЗИЛЛА*🐲,* УНИЧТОЖИВ ТЕБЯ В ПУХ И ПРАХ!!!*..."
        mTrue = " Никто не способен противостоять такой мощи... В локации пали все, до единого... Но они восстанут через час, я буду ждать."
        bT = "*РАЗРУШАЯ ВСЁ И ВСЕХ ВОКРУГ!*"
        timesleep = math.ceil(time.time()) + 3600
    elif winner == 5:
        winnerStr = "К несчастью, победил*" + str(enemyMob) + "*. "
        try: #это выдает мут
            bot_time_timeban = 5
            bot_timeban = int(bot_time_timeban) * 60
            bot2_timeban = time.time()
            bot3_timeban = math.ceil(bot2_timeban)
            timebanbot = bot3_timeban + bot_timeban
            bot.restrict_chat_member(m.chat.id, m.from_user.id, timebanbot, False)            
            db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "UPDATE `users` SET `nowhp` = 0 WHERE user_id = %s"
                cursor.execute(sql, (m.from_user.id))
                db.commit()
                db.close()
            mTrue = " Отдохни пять минут, восстанови силы и возвращайся."
        except:
            mTrue = "Но так как у тебя активирована аура выносливости, отдых тебе не нужен."
            return
    if winner == 6: #не ебу че это
        if str(m.chat.id) == str(chancechat):
            randPointr = random.randint(1, 3)
            randPoint = int(lvl) * randPointr
            
            winnerStr = "К счастью, удача тебе улыбнулась и победа на твоей стороне! Ты получаешь " + str(randPoint) + " поинтов."
            db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "UPDATE `users` SET `points` = points + %s WHERE user_id = %s"
                cursor.execute(sql, (int(randPoint), m.from_user.id))
                db.commit()
                db.close()
            chanceexp = random.randint(1,2)
            if chanceexp == 1:
                db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                with db.cursor() as cursor:
                    sql = "SELECT `lvl` FROM `users` WHERE user_id = %s"
                    cursor.execute(sql, (m.from_user.id))
                    result = cursor.fetchone()
                    randExp = random.randint(2, 3)
                    expgive_count = int(result['lvl']) * 0.5 * randExp
                    expgive = int(expgive_count)
                    db.commit()
                db.close()
                winnerStr += "В дополнение, " + str(expgive) + " ед. опыта."
                db = pymysql.connect(host='localhost',
                             user='root',
                             password='maz1aan16v',                             
                             db='Megumin',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                with db.cursor() as cursor:
                    sql = "UPDATE `users` SET `exp` = exp + %s WHERE user_id = %s"
                    cursor.execute(sql, (int(expgive), m.from_user.id))
                    db.commit()
                    sql = "SELECT `exp`, `lvl` FROM `users` WHERE user_id = %s"
                    cursor.execute(sql, (m.from_user.id))
                    result = cursor.fetchone()
                    needexp = int(result['lvl']) * 100
                    plustats = int(needexp) / 50
                    if (int(result['exp']) >= needexp):
                        ex2p = 0
                        sql = "UPDATE `users` SET `exp` = %s WHERE user_id = %s"
                        cursor.execute(sql, (int(ex2p), m.from_user.id))
                        db.commit()
                        sql = "UPDATE `users` SET `lvl` = lvl + 1 WHERE user_id = %s"
                        cursor.execute(sql, (m.from_user.id))
                        sql = "UPDATE `users` SET `atk` = atk + %s WHERE user_id = %s"
                        cursor.execute(sql, (plustats, m.from_user.id))
                        sql = "UPDATE `users` SET `hp` = hp + %s WHERE user_id = %s"
                        cursor.execute(sql, (plustats, m.from_user.id))
                        bot.send_message(m.chat.id, "LVL UP. Статы повышены на +{0}.".format(str(plustats)))
                        db.commit()
                    db.close()
    else:
        pass
    
   # bot.reply_to(m, "FIRST ATTACK:" + str(randomFirstAttack) + " " + uC + uFN + " Здоровье и атака: " + pH + " " + pA + " Моб :" + eMRH + " " + eMRA + " Стэки: " + pSH + " " + eMSH + str(uC+uFN))
    bot.edit_message_text("*" + uFN + "*" + ", вы решили " + eventTitle + bYS + eM + ", " + bT + ". Характеристики боя:\n \n❤️Твое здоровье: " + pH + " ед.   \n💢Атака: " + pA + " ед. \n💜Здоровье врага: " + eMRH + " ед.   \n💢Атака: " + eMRA + " ед. \n\n" + fA + "\nБой был затяжным... " + winnerStr + "\n" + critStr + critStrEnemy + "\nТы оставил врагу 💜" + eMSH + " ед. здоровья, и он тебе ❤️" + pSH + " ед. \nЗа весь бой вы нанесли " + pSA + " ед. урона, а враг " + eMSA + " ед." + mTrue, searchMob.chat.id, searchMob.message_id, parse_mode="markdown")
    if pvpBattle == True: pvpBattle = False
    #сам вывод результата