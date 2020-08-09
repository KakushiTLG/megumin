import items
import dogs
@bot.message_handler(commands=['top'])
def topLvl(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT lvl, username FROM users ORDER BY lvl DESC Limit 5"
        cursor.execute(sql)
        result = cursor.fetchall()
        top = ""
        count = 0
        for dict in result:
            count += 1
            if count == 1:
                id = "🥇"
            elif count == 2:
                id = "🥈"
            elif count == 3:
                id = "🥉"
            elif count == 4:
                id = "4⃣"
            elif count == 5:
                id = "5⃣"
            top += str(id) + str(dict['username']) + " - " + str(dict['lvl']) + ' lvl' + str(id) + '\n'
        sql = "SELECT points, username FROM users ORDER BY points DESC Limit 5"
        cursor.execute(sql)
        pointres = cursor.fetchall()
        topPoints = ""
        countPoints = 0
        for dict in pointres:
            countPoints += 1
            if countPoints == 1:
                idp = "🥇"
            elif countPoints == 2:
                idp = "🥈"
            elif countPoints == 3:
                idp = "🥉"
            elif countPoints == 4:
                idp = "4⃣"
            elif countPoints == 5:
                idp = "5⃣"
            topPoints += str(idp) + str(dict['username']) + " - " + str(dict['points']) + ' points' + str(idp) + '\n'
        sql = "SELECT tempPts, username FROM users ORDER BY tempPts DESC Limit 5"
        cursor.execute(sql)
        temppts = cursor.fetchall()
        topPts = ""
        countPts = 0
        for dict in temppts:
            countPts += 1
            if countPts == 1:
                idpts = "🥇"
            elif countPts == 2:
                idpts = "🥈"
            elif countPts == 3:
                idpts = "🥉"
            elif countPts == 4:
                idpts = "4⃣"
            elif countPts == 5:
                idpts = "5⃣"
            topPts += str(idpts) + str(dict['username']) + " - " + str(dict['tempPts']) + '❄ \n'
        
        
        db.close()
    bot.reply_to(m, "❄ТОП игроков по уровню❄\n" + str(top) + "\n \n❄ТОП игроков по поинтам❄\n" + str(topPoints) + "\n❄ТОП игроков по снежинкам❄\n" + str(topPts))
    
        #(fond * 0.3) + (lvl * 1.5) + (players * 0.5)
        
        
@bot.message_handler(commands=['promo'])
def promo(m):
    if len(m.text.split(' ')) > 1:
        text = m.text.replace('/promo ', '', 1)
        db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "SELECT `status`, `count` FROM `promo` WHERE `promo` = %s AND `status` = 0"
            cursor.execute(sql, (str(text)))
            result = cursor.fetchone()
            if result:
                status = result['status']
                count = result['count']
                if status == 0:
                    sql = "UPDATE `promo` SET `status` = 1 WHERE `promo` = %s"
                    cursor.execute(sql, (text))
                    db.commit()
                    sql = "UPDATE `users` SET `points` = points + %s WHERE `user_id` = %s"
                    cursor.execute(sql, (int(count), str(m.from_user.id)))
                    db.commit()
                    bot.reply_to(m, "Вы успешно активировали промокод на сумму " + str(count) + " поинтов.")
                    db.close()
                else:
                    bot.reply_to(m, "Неверный промокод.")
                    db.close()
                    return
            else:
                bot.reply_to(m, "Неверный промокод.")
                db.close()
                return
    else:
        bot.reply_to(m, "Если у вас есть промокод - введите его после /promo")
        return
        
@bot.message_handler(commands=['gpromo'])
def genPromo(m):
    if str(m.from_user.id) in owner:
        pass
    else:
        bot.reply_to(m, "Да нет, дружок, так не пойдет...")
        return
    symbol = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    text = ''
    for i in range(10):
        text += random.choice(symbol)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "INSERT INTO promo (promo, count, status) VALUES (%s, 100, '0')" 
        cursor.execute(sql, (str(text)))
        db.commit()
        db.close()
    gpromo = bot.send_message(chancechat, "❄Cold promo❄\n*{}*".format(str(text)), None, None, None,'markdown')
    bot.pin_chat_message(chancechat, gpromo.message_id)
@bot.message_handler(commands=['createpromo'])
def createPromo(m):
    if str(m.from_user.id) in owner:
        pass
    else:
        bot.reply_to(m, "Да нет, дружок, так не пойдет...")
        return
    if len(m.text.split(' ')) > 1:
        try:
            text = m.text.replace('/createpromo ', '', 1).split(':')
            promo = text[0]
            count = text[1]
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "INSERT INTO promo (promo, count, status) VALUES (%s, %s, '0')" 
                cursor.execute(sql, (str(promo), int(count)))
                db.commit()
                db.close()
            bot.reply_to(m, "Promo created.")
        except:
            bot.reply_to(m, "Что-то пошло не так.")
    else:
        bot.reply_to(m, "Введите /createpromo text:count")
        
        
@bot.message_handler(commands=['myrefs'])
def referals(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `username` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        refer = str(result['username'])
        sql = "SELECT `username`, `lvl` FROM `users` WHERE `ref` = %s"
        cursor.execute(sql, (refer))
        referal = cursor.fetchall()
    db.close()
    if referal:
        pass
    else:
        bot.reply_to(m, "У вас нет рефералов.")
        return
    referals = "\n"
    for dict in referal:
        referals += dict['username'] + " - " + str(dict['lvl']) + ' lvl \n'
        print(referals)
    if referals:
        bot.reply_to(m, "Список ваших рефералов, " + str(refer) + ": \n" + str(referals))
    else:
        referals = 'У вас нет рефералов'
        
        
        
@bot.message_handler(commands=['pay'])
def pay(m):
    if len(m.text.split(' ')) > 1:
        text = m.text.replace('/pay ', '', 1).split(':')
        payfrom = m.from_user.id
        payto = str(text[0])
        paySum = int(text[1])
        if paySum >= 1:
            pass
        else:
            bot.reply_to(m, "^=^")
            return
    else:
        bot.reply_to(m, "Используйте /pay [никнейм игрока] [сумма]")
        return
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `points` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (payfrom))
        result = cursor.fetchone()
        currentPoint = str(result['points'])
        if int(currentPoint) > int (paySum):
            sql = "SELECT `points` FROM `users` WHERE `username` = %s"
            cursor.execute(sql, (str(payto)))
            paytoCheck = cursor.fetchone()
            if paytoCheck:
                pass
            else:
                bot.reply_to(m, "Нет игрока с таким никнеймом")
                return
            try:
                sql = "UPDATE `users` SET `points` = points - %s WHERE `user_id` = %s"
                cursor.execute(sql, (int(paySum), payfrom))
                db.commit()
                sql = "UPDATE `users` SET `points` = points + %s WHERE `username` = %s"
                cursor.execute(sql, (int(paySum), str(payto)))
                db.commit()
                db.close()
            except:
                bot.reply_to(m, "Ошибка 2")
                db.close()
                return
            bot.reply_to(m, "Вы успешно передали " + str(paySum) + " поинтов игроку с ником " + str(payto) + ".")
        else:
            bot.reply_to(m, "Недостаточно поинтов.")
                
                

@bot.message_handler(commands=['ref'])
def ref(m):
    if len(m.text.split(' ')) > 1:
        text = m.text.replace('/ref ', '', 1)
        db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "SELECT * FROM `users` WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            result = cursor.fetchone()
            ref = result['ref']
            if ref:
                bot.reply_to(m, "Ты уже выбирал себе реферала")
                db.close()
                return
            else:
                if text == result['username']:
                    bot.reply_to(m, "Нехорошо делать себя своим же рефералом")
                    db.close()
                    return
                else:
                    try:
                        sql = "SELECT username FROM users WHERE username = %s"
                        cursor.execute(sql, (text))
                        usern = cursor.fetchone()
                        if usern:
                            pass
                        else:
                            bot.reply_to(m, "Ошибка. Неправильный никнейм рефера.")
                            db.close()
                            return
                        sql = "UPDATE `users` SET `ref` = %s WHERE `user_id` = %s"
                        cursor.execute(sql, (str(text), m.from_user.id))
                        db.commit()
                        sql = "UPDATE `users` SET `points` = points + 100 WHERE `user_id` = %s"
                        cursor.execute(sql, (m.from_user.id))
                        db.commit()
                        sql = "UPDATE `users` SET `points` = points + 200 WHERE `username` = %s"
                        cursor.execute(sql, (text))
                        db.commit()
                        db.close()
                        bot.reply_to(m, "Ты стал рефералом " + text + ". Реферал и рефер получили 100 и 200 поинтов.")
                    except:
                        bot.reply_to(m, "Ошибка.")
    else:
        bot.reply_to(m, "Введите /ref [никнейм рефера]")
                    

def profileBeta(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        if result:
            print(result)
            user_id = result['id']
            username = result['username']
            exp = result['exp']
            lvl = int(result['lvl'])
            points = result['points']
            atk = result['atk']
            hp = result['hp']
            fatk = result['fatk']
            creet = result['creet']
            local = int(result['local'])
            ref = result['ref']
            krazha = result['krazha']
            nowhp = int(result['nowhp'])
            frakaName = result['frakaName']
            frakaStatus = int(result['frakaStatus'])
            tempPts = int(result['tempPts'])
            frakaBonus = int(result['frakaBonus'])
            itemNow = int(result['item'])
            itemn = items.item(itemNow)
            bankNo = int(result['bankNo'])
            bankInv = int(result['bankInv'])
            if itemn:
                pass
            else:
                itemn = "Ничего"
            if frakaStatus == 3:
                notif = "⚠️Вы были приглашены во фракцию " + str(frakaName) + "!\n Для принятия запроса - /f_accept .\n Для отказа - /f_cancel⚠️"
            else:
                notif = ""
            if ref:
                ref = result['ref']
            else:
                ref = 'Отсуствует'
            if frakaBonus > 0:
                frakabonus = str(frakaBonus) + "pts/h"
            else:
                frakabonus = "0"
        else:
            sql = "INSERT INTO users (username, user_id, lvl, points, atk, hp) VALUES (%s, %s, '1', '0', '25', '25')"
            cursor.execute(sql, (m.from_user.username, m.from_user.id))
            db.commit()
            db.close()
            user_id = 'Момент регистрации. Повторите запрос.'
            username = m.from_user.username
            lvl = int('1')
            points = int('0')
            atk = 12
            hp = 12
            exp = 0
            fatk = 10
            creet = 5
            local = 1
            nowhp = 12
            tempPts = 0
            frakabonus = "Отсутствует"
            ref = 'Отсутствует'
    needexp = int(lvl) * 100
    if str(m.from_user.id) in donators:
        donate = '✅Активен'
    else:
        donate = '❌'
    if bankNo != user_id:
        bankNo = "Отсутствует"
    elif bankNo == user_id:
        bankNo = "Есть"
    if local == 1:
        location = "Respawn"
        if (lvl >= 5):
            locinfo = "\n🆕Вам доступна локация ''Таксопарк''! Используйте /next_location для перехода🆕"
        else:
            locinfo = ""
    elif local == 2:
        location = "Таксопарк"
        if (lvl >= 7):
            locinfo = "\n🆕Вам доступна локация ''Dungeon''! Используйте /next_location для перехода🆕"
        else:
            locinfo = ""
    elif local == 3:
        location = "Dungeon"
        if (lvl >= 8):
            locinfo = "\n🆕Вам доступна локация ''Мэрия''! Используйте /next_location для перехода🆕"
        else:
            locinfo = ""
    elif local == 4:
        location = "Мэрия"
        locinfo = ""
    elif local == 5:
        location = "Заснеженная кавайня"
        #if (lvl >= 10):
            #locinfo = "\n🆕Вам доступна локация ''заснеженная кавайня''! Используйте /next_location для перехода🆕"
        #else:
        locinfo = ""
        if (int(frakaStatus) == 1) or (int(frakaStatus) == 2):
            frakaName = frakaName
        else:
            frakaName = "Отсутствует"
        if itemNow == 999:
            stats = "❄Профиль❄ \n \n📘Ваша кликуха - " + str(username) + "\n📕Порядковый номер - " + str(user_id) + "\n🔰Пидор-статус -  ✅Активен"
            profilemsg = bot.reply_to(m, stats)
            return
    if lvl >= 2 :
        stats = "ℹ️Профильℹ️ \n \n📘Ваш никнейм - " + str(username) + "\n📕Ваш ID - " + str(user_id) + "\n🔰Донат-статус - " + str(donate) + "\n📒Количество поинтов - " + str(points) + "" + "\n⭐️Опыт: " + str(exp) + " / {0} \n📗Ваш уровень - " + str(lvl) + "\n◻️Ваш реферер: " + str(ref) + "\n📡Локация - " + str(location) + "\n📓Фракция: " + str(frakaName) + "\n💸Доход с фракции: " + str(frakabonus) + "\n🔑Банковская ячейка: " + str(bankNo) + "\n💴Текущий депозит: " + str(bankInv) + "\n" + str(locinfo) + "\n" + str(notif) + "\n    /myrefs        /shop        /stats"
        profilemsg = bot.reply_to(m, stats.format(str(needexp)))
    else:
        stats = "ℹ️Профильℹ️ \n \n📘Ваш никнейм - " + str(username) + "\n📕Ваш ID - " + str(user_id) + "\n🔰Донат-статус - " + str(donate) + "\n📒Количество поинтов - " + str(points) + " \n⭐️Опыт: " + str(exp) + " / {0} \n📗Ваш уровень - " + str(lvl) + "\n◻️Ваш реферер: " + str(ref) + "\n" + str(notif) + "\n          /myrefs              /giveaway"
        profilemsg = bot.reply_to(m, stats.format(str(needexp)))
    
    
    



@bot.message_handler(commands=['stats'])
def stats(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        if result:
            print(result)
            user_id = result['id']
            username = result['username']
            exp = result['exp']
            lvl = int(result['lvl'])
            points = result['points']
            atk = result['atk']
            hp = result['hp']
            fatk = result['fatk']
            creet = result['creet']
            local = int(result['local'])
            ref = result['ref']
            krazha = result['krazha']
            nowhp = int(result['nowhp'])
            frakaName = result['frakaName']
            frakaStatus = int(result['frakaStatus'])
            tempPts = int(result['tempPts'])
            frakaBonus = int(result['frakaBonus'])
            itemNow = int(result['item'])
            itemn = items.item(itemNow)
            azart = int(result['azart'])
            dog = result['dog']
            dogLvl = int(result['dogLvl'])
            dogAtk = int(result['dogAtk'])
            dogHp = int(result['dogHp'])
            dogFatk = int(result['dogFatk'])
            dogCreet = int(result['dogCreet'])
            dogEat = int(result['dogEat'])
            db.close()
            if lvl >= 2:
                pass
            else:
                bot.reply_to(m, "Тебе сюда рано")
                return
            if lvl >= 2 :
                if nowhp > hp:
                    nowhp = hp
            else:
                pass
            BM = int(atk + hp + (((fatk/100) + (creet/100)) * 10))
            stats = bot.reply_to(m, "\n💪Очки Боевой Мощи - " + str(BM) + "\n✊В руке - " + str(itemn) + "\n💢Ваша атака - " + str(atk) + "\n❤️Ваше здоровье - " + str(nowhp) + "/" + str(hp) + "\n🦀Шанс первой атаки - " + str(fatk) + "% \n💥Шанс крита - " + str(creet) + "% \n🤛Навык кражи - " + str(krazha) + "\n🎰Навык азарта - " + str(azart) + "/5 lvl \nПомощник: " + str(dog) + "\nЭнергия помощника: " + str(dogEat) + "/100\nУровень помощника: " + str(dogLvl) + "\n+{}Atk \n+{}Hp \n+{}%Fatk \n+{}%Creet".format(dogAtk, dogHp, dogFatk, dogCreet))
            return










@bot.message_handler(commands=['seeprofile'])
def profileAdm(m):
    if str(m.from_user.id) in owner:
        if len(m.text.split(' ')) > 1:
            nickn = m.text.replace('/seeprofile ', '', 1)
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "SELECT * FROM `users` WHERE `username` = %s"
                cursor.execute(sql, (nickn))
                result = cursor.fetchone()
                if result:
                    user_id = result['id']
                    username = result['username']
                    exp = result['exp']
                    lvl = result['lvl']
                    points = result['points']
                    atk = result['atk']
                    hp = result['hp']
                    needexp = int(lvl) * 100
                    statsAdm = "🕴Профиль🕴 \n \n📘Ваш никнейм - " + str(username) + "\n📕Ваш ID - " + str(user_id) + "\n📒Количество поинтов - " + str(points) + "\n⭐️Опыт: " + str(exp) + " / {0} \n📗Ваш уровень - " + str(lvl)
                    profileAdm = bot.reply_to(m, statsAdm.format(str(needexp)))
                    db.close()
                else:
                    bot.reply_to(m, "Игрок не найден.")
        else:
            bot.reply_to(m, "Введите /seeprofile [nickname]")
    else:
        bot.reply_to(m, "Команда доступна только разработчикам.")
        
        



@bot.message_handler(commands=['changenick'])
def changeNick(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `username` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        if result:
            now = result['username']
            if now == 'None':
                db.close()
                pass
            else:
                bot.reply_to(m, "У вас не куплена смена ника")
                db.close()
                return
        else:
            bot.reply_to(m, "Вы не зарегистрированы. Используйте !профиль для регистрации.")
            db.close()
            return
    if len(m.text.split(' ')) > 1:
        nick = m.text.replace('/changenick ', '', 1).replace('@ne_dlt_bot', '', 1)
        db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `username` = %s WHERE `user_id` = %s"
            cursor.execute(sql, (str(nick), m.from_user.id))
            db.commit()
        db.close()
        bot.reply_to(m, "Вы успешно сменили ник.")
    else:
        bot.reply_to(m, "Используйте /changenick [Никнейм]")
        return
        
        
        
        
        
        
        
@bot.message_handler(commands=['next_location'])
def nextLoc(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl`, `local` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        location = int(result['local'])
        lvl = int(result['lvl'])
        if (location == 1) and (lvl >= 5):
            go = bot.reply_to(m, "Переходим в локацию ''Таксопарк''... Это займет некоторое время...")
            time.sleep(5)
            sql = "UPDATE `users` SET `local` = 2 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            complete = "Таксопарк - один из тех немногих районов, где обитает куча бандитов, которые разгуливают в масках, туристы дерутся за свободное такси, а еще тут попадается оживший банкомат. Сможешь выбраться отсюда живым?"
            bot.edit_message_text(complete, go.chat.id, go.message_id)
        elif (location == 2) and (lvl >= 7):
            go = bot.reply_to(m, "Переходим в локацию ''Dungeon''... Это займет некоторое время...")
            time.sleep(5)
            sql = "UPDATE `users` SET `local` = 3 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            complete = "Вы успешно перешли в локацию ''Dungeon''."
            bot.edit_message_text(complete, go.chat.id, go.message_id)
        elif (location == 3) and (lvl >= 8):
            go = bot.reply_to(m, "Переходим в локацию ''Мэрия''... Это займет некоторое время...")
            time.sleep(5)
            sql = "UPDATE `users` SET `local` = 4 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            complete = "Мэрия... Казалось бы, центр города, какие тут могут быть опасности? Могут, еще как. Неадекватный губернатор, кучка бывших губернаторов, немало влиятельных людей в разных сферах - все это тут. Ребята тут серьёзнее чем в таксопарке, ибо тут - самые влиятельные люди штата."
            bot.edit_message_text(complete, go.chat.id, go.message_id)
        elif (location == 4) and (lvl >= 10):
            go = bot.reply_to(m, "Переходим в локацию ''казино''... Это займет некоторое время...")
            time.sleep(5)
            sql = "UPDATE `users` SET `local` = 5 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            complete = "Если ты считаешь, что весь кошмар позади - добро пожаловать в казино! Здесь на кон ставят не деньги - жизнь. Проституция, криминал и деньги - все это тут."
            bot.edit_message_text(complete, go.chat.id, go.message_id)
        else:
            bot.reply_to(m, "Сначала закончите свои дела в этой локации!")
        db.close()