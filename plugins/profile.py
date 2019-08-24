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
            sql = "SELECT `status`, `count` FROM `promo` WHERE `promo` = %s"
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
                    bot.reply_to(m, "Промокод уже активирован.")
                    db.close()
                    return
            else:
                bot.reply_to(m, "Такого промокода не существует.")
                db.close()
                return
    else:
        bot.reply_to(m, "Если у вас есть промокод - введите его после /promo")
        return
        
        
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
        print(referal)
        if referal:
            pass
        else:
            referals = 'У вас нет рефералов'
    db.close()
    referals = "\n"
    for dict in referal:
        referals += dict['username'] + " - " + str(dict['lvl']) + ' lvl \n'
        print(referals)
    bot.reply_to(m, "Список ваших рефералов, " + str(refer) + ": \n" + str(referals))

@bot.message_handler(commands=['promolist'])
def promoList(m):
    if str(m.from_user.id) in owner:
        db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "SELECT `promo` FROM `promo` WHERE `status` = 0"
            cursor.execute(sql)
            result = cursor.fetchall()
            bot.reply_to(m, str(result))
            db.close()
    else:
        bot.reply_to(m, ":(")
@bot.message_handler(commands=['pay'])
def pay(m):
    if len(m.text.split(' ')) > 1:
        text = m.text.replace('/pay ', '', 1).split(':')
        payfrom = m.from_user.id
        payto = str(text[0])
        paySum = int(text[1])
        pass
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
                        sql = "UPDATE `users` SET `points` = points + 50 WHERE `user_id` = %s"
                        cursor.execute(sql, (m.from_user.id))
                        db.commit()
                        sql = "UPDATE `users` SET `points` = points + 50 WHERE `username` = %s"
                        cursor.execute(sql, (text))
                        db.commit()
                        db.close()
                        bot.reply_to(m, "Ты стал рефералом " + text + ". Реферал и рефер получили по 50 поинтов.")
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
            lvl = result['lvl']
            points = result['points']
            atk = result['atk']
            hp = result['hp']
            fatk = result['fatk']
            creet = result['creet']
            local = int(result['local'])
            ref = result['ref']
            if ref:
                ref = result['ref']
            else:
                ref = 'Отсуствует'
        else:
            sql = "INSERT INTO users (username, user_id, lvl, points, atk, hp) VALUES (%s, %s, '1', '0', '5', '10')"
            cursor.execute(sql, (m.from_user.username, m.from_user.id))
            db.commit()
            db.close()
            user_id = 'Момент регистрации. Повторите запрос.'
            username = m.from_user.username
            lvl = int('1')
            points = int('0')
            atk = 5
            hp = 10
            exp = 0
            fatk = 10
            creet = 5
            local = 1
            ref = 'Отсутствует'
            print('net')
    needexp = int(lvl) * 100
    if str(m.from_user.id) in donators:
        donate = '✅Активен'
    else:
        donate = '❌'
    if local == 1:
        location = "Respawn"
    if local == 2:
        location = "Таксопарк"
    if local == 3:
        location = "Dungeon"
    if (lvl >= 6) and (local == 1):
        locinfo = "\n🆕Вам доступна локация ''Таксопарк''! Используйте /next_location для перехода🆕"
    else:
        locinfo = ""
    if lvl >= 3 :
        stats = "🕴Профиль🕴 \n \n📘Ваш никнейм - " + str(username) + "\n📕Ваш ID - " + str(user_id) + "\n🔰Донат-статус - " + str(donate) + "\n📒Количество поинтов - " + str(points) + "\n⭐️Опыт: " + str(exp) + " / {0} \n📗Ваш уровень - " + str(lvl) + "\n◻️Ваш реферер: " + str(ref) + "\n📡Локация - " + str(location) + "\n💢Ваша атака - " + str(atk) + "\n❤️Ваше здоровье - " + str(hp) + "\n🦀Шанс первой атаки - " + str(fatk) + "% \n💥Шанс крита - " + str(creet) + "%" + "\n        /myrefs              /shop" + str(locinfo)
        profilemsg = bot.reply_to(m, stats.format(str(needexp)))
    else:
        stats = "🕴Профиль🕴 \n \n📘Ваш никнейм - " + str(username) + "\n📕Ваш ID - " + str(user_id) + "\n🔰Донат-статус - " + str(donate) + "\n📒Количество поинтов - " + str(points) + "\n⭐️Опыт: " + str(exp) + " / {0} \n📗Ваш уровень - " + str(lvl) + "\n◻️Ваш реферер: " + str(ref) + "\n               /myrefs"
        profilemsg = bot.reply_to(m, stats.format(str(needexp)))
    
    
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
        
        
@bot.message_handler(commands=['shop'])
def shop(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        db.close()
    if lvl >= 3 :
        pass
    else:
        bot.reply_to(m, "Магазин откроется на 3 уровне.")
        return
    bot.reply_to(m, "Добро пожаловать в магазин. Список предметов для покупки ниже. \nЧтобы купить предмет, нужно воспользоваться командой /buy id предмета:количество. Удачных покупок.")
    text = "Магазин: \n Название - ID - стоимость. \n+1💢 ед.атаки - 1ID - 20points \n+1❤️ ед. здоровья - 2ID - 20points \n+1% 🦀шанс первой атаки - 3ID - 30points \n+1% 💥шанс крита - 4ID - 50points \n 🔴Смена никнейма - 5ID - 500 points"
    bot.reply_to(m, text)



@bot.message_handler(commands=['buy'])
def buy(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        db.close()
    if lvl >= 3 :
        pass
    else:
        bot.reply_to(m, "Магазин откроется на 3 уровне.")
        return
    if len(m.text.split(' ')) > 1:
        item = m.text.replace('/buy ', '', 1).split(':')
        if int(item[0]) == 1:
            sum = int(item[1]) * 20
            count = int(item[1])
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "SELECT `points` FROM `users` WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                result = cursor.fetchone()
                balance = result['points']
                if int(balance) >= int(sum):
                    sql = "UPDATE `users` SET `points` = points - %s WHERE user_id = %s"
                    cursor.execute(sql, (sum, m.from_user.id))
                    db.commit()
                    sql = "UPDATE `users` SET `atk` = atk + %s WHERE user_id = %s"
                    cursor.execute(sql, (count, m.from_user.id))
                    db.commit()
                    db.close()
                    bot.reply_to(m, "Покупка успешна. Вам добавлено {0} очков атаки💢 за {1} поинтов.".format(str(count),str(sum)))
                else:
                    bot.reply_to(m, "Недостаточно поинтов") 
        if int(item[0]) == 2:
            sum = int(item[1]) * 20
            count = int(item[1])
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "SELECT `points` FROM `users` WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                result = cursor.fetchone()
                balance = result['points']
                if int(balance) >= int(sum):
                    sql = "UPDATE `users` SET `points` = points - %s WHERE user_id = %s"
                    cursor.execute(sql, (sum, m.from_user.id))
                    db.commit()
                    sql = "UPDATE `users` SET `hp` = hp + %s WHERE user_id = %s"
                    cursor.execute(sql, (count, m.from_user.id))
                    db.commit()
                    db.close()
                    bot.reply_to(m, "Покупка успешна. Вам добавлено {0} очков здоровья❤️ за {1} поинтов.".format(str(count),str(sum)))
                else:
                    bot.reply_to(m, "Недостаточно поинтов")
        if int(item[0]) == 3:
            sum = int(item[1]) * 30
            count = int(item[1])
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "SELECT `points` FROM `users` WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                result = cursor.fetchone()
                balance = result['points']
                if int(balance) >= int(sum):
                    sql = "UPDATE `users` SET `points` = points - %s WHERE user_id = %s"
                    cursor.execute(sql, (sum, m.from_user.id))
                    db.commit()
                    sql = "UPDATE `users` SET `fatk` = fatk + %s WHERE user_id = %s"
                    cursor.execute(sql, (count, m.from_user.id))
                    db.commit()
                    db.close()
                    bot.reply_to(m, "Покупка успешна. Вам добавлено {0} % шанс на первую атаку🦀 за {1} поинтов.".format(str(count),str(sum)))
                else:
                    bot.reply_to(m, "Недостаточно поинтов") 
        if int(item[0]) == 4:
            sum = int(item[1]) * 50
            count = int(item[1])
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "SELECT `points` FROM `users` WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                result = cursor.fetchone()
                balance = result['points']
                if int(balance) >= int(sum):
                    sql = "UPDATE `users` SET `points` = points - %s WHERE user_id = %s"
                    cursor.execute(sql, (sum, m.from_user.id))
                    db.commit()
                    sql = "UPDATE `users` SET `creet` = creet + %s WHERE user_id = %s"
                    cursor.execute(sql, (count, m.from_user.id))
                    db.commit()
                    db.close()
                    bot.reply_to(m, "Покупка успешна. Вам добавлено {0} % шанс на крит💥 за {1} поинтов.".format(str(count),str(sum)))
                else:
                    bot.reply_to(m, "Недостаточно поинтов") 
        if int(item[0]) == 5:
            sum = int(item[1]) * 500
            db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
            with db.cursor() as cursor:
                sql = "SELECT `points` FROM `users` WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                result = cursor.fetchone()
                balance = result['points']
                if int(balance) >= int(sum):
                    sql = "UPDATE `users` SET `points` = points - %s WHERE user_id = %s"
                    cursor.execute(sql, (sum, m.from_user.id))
                    db.commit()
                    sql = "UPDATE `users` SET `username` = 'None' WHERE user_id = %s"
                    cursor.execute(sql, (m.from_user.id))
                    db.commit()
                    db.close()
                    bot.reply_to(m, "Покупка успешна. Теперь вы можете сменить никнейм, введя команду /changenick .")
                else:
                    bot.reply_to(m, "Недостаточно поинтов") 
    else:
        bot.reply_to(m, "Используйте /shop")
        



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
        nick = m.text.replace('/changenick ', '', 1)
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
        if (location == 1) and (lvl >= 6):
            go = bot.reply_to(m, "Переходим в локацию ''Таксопарк''... Это займет некоторое время...")
            time.sleep(5)
            sql = "UPDATE `users` SET `local` = 2 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            complete = "Вы успешно перешли в локацию ''таксопарк''."
            bot.edit_message_text(complete, go.chat.id, go.message_id)
        else:
            bot.reply_to(m, "Сначала закончите свои дела в этой локации!")
            
        db.close()