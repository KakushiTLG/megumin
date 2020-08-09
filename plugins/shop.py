@bot.message_handler(commands=['shop'])
def shop(m):
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
        lvl = int(result['lvl'])
        atk = int(result['atk'])
        hp = int(result['hp'])
        fatk = int(result['fatk'])
        creet = int(result['creet'])
        krazha = int(result['krazha'])
        azart = int(result['azart'])
        dogLvl = int(result['dogLvl'])
        dog = result['dog']
        db.close()
    if azart == 0:
        needAzart = 5000
    elif azart == 1:
        needAzart = 5500
    elif azart == 2:
        needAzart = 6000
    elif azart == 3:
        needAzart = 6500
    elif azart == 4:
        needAzart = 7000
    elif azart == 5:
        needAzart = "Навык прокачан"
    if lvl >= 2 :
        pass
    else:
        bot.reply_to(m, "Магазин откроется на 2 уровне.")
        return
    if str(m.from_user.id) in donators:
        needAtk = int(6 * ((atk - 19) / 6))
        needHp = int(6 * ((hp - 19) / 6))
        needFatk = int(12 * ((fatk - 9) / 6))
        needCreet = int(15 * ((creet - 4) / 3))
    elif str(dog) == "Чарли":
        needAtk = int((10 * ((atk - 19) / 6)) * 0.9)
        needHp = int((10 * ((hp - 19) / 6)) * 0.9)
        needFatk = int((15 * ((fatk - 9) / 6)) * 0.9)
        needCreet = int((20 * ((creet - 4) / 3)) * 0.9)
    else:
        needAtk = int(10 * ((atk - 19) / 6))
        needHp = int(10 * ((hp - 19) / 6))
        needFatk = int(15 * ((fatk - 9) / 6))
        needCreet = int(20 * ((creet - 4) / 3))
    needHilka = int(hp * 0.5)
    if azart == 0:
        needAzart = 5000
    elif azart == 1:
        needAzart = 5500
    elif azart == 2:
        needAzart = 6000
    elif azart == 3:
        needAzart = 6500
    elif azart == 4:
        needAzart = 7000
    if krazha >= 1:
        textKrazha = "Навык кражи"
        needKrazha = int(krazha * 150)
    else:
        textKrazha = "Способность кражи"
        needKrazha = 100
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `lot`"
        cursor.execute(sql)
        result = cursor.fetchone()
        db.close()
        if result:
            name = result['name']
            desc = result['desc']
            price = result['price']
            text = "\n⛔️Особый Предмет В ПРОДАЖЕ⛔️\n{} \nОписание: {} \nСтоимость: {}pts\n /buy_lot для покупки".format(name, desc, str(price))
            pass
        else:
            text = ""
            pass
    if dogLvl == 0:
        bot.reply_to(m, "Магазин: \n Команда - описание - стоимость. \n💢/buy_atk - +1 ед.атаки - {0} pts \n❤️/buy_hp +1 ед. здоровья - {1} pts \n🦀/buy_fatk - +1% шанс первой атаки - {2} pts \n💥/buy_crt - +1% шанс крита - {3} pts\n🔴/buy_nick - Смена никнейма - 500 pts \n🤛/buy_krazha - {4} - {5} pts \n💚/buy_heal - Восстановление здоровья - {6} pts \n🎰/buy_azart - +1 навык азарта - {7} \n/buy_bankNo - покупка ячейки в банке - 1000pts \n\n\n\n      Меню покупки помощников:\n/buy_charlie - С Чарли вы сможете покупать предметы в магазине дешевле \n/buy_jack - Джек поможет вам в битве своей силой атаки \n/buy_james - С Джеймсом ваша выносливость будет больше \n/buy_andrew - Эндрю - тот талисман, о котором мечтает каждый боец. Благодаря его помощи, увеличивается шанс на критический урон.".format(str(needAtk), str(needHp), str(needFatk), str(needCreet), str(textKrazha), str(needKrazha), str(needHilka), str(needAzart)) + str(text))
    else:
        bot.reply_to(m, "Магазин: \n Команда - описание - стоимость. \n💢/buy_atk - +1 ед.атаки - {0} pts \n❤️/buy_hp +1 ед. здоровья - {1} pts \n🦀/buy_fatk - +1% шанс первой атаки - {2} pts \n💥/buy_crt - +1% шанс крита - {3} pts\n🔴/buy_nick - Смена никнейма - 500 pts \n🤛/buy_krazha - {4} - {5} pts \n💚/buy_heal - Восстановление здоровья - {6} pts \n🎰/buy_azart - +1 навык азарта - {7} \n/buy_bankNo - покупка ячейки в банке - 1000pts \n\n\n /h_rest - восстановление энергии помощника (1000 pts)".format(str(needAtk), str(needHp), str(needFatk), str(needCreet), str(textKrazha), str(needKrazha), str(needHilka), str(needAzart)) + str(text))




        
        
@bot.message_handler(commands=['h_rest'])
def h_rest(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT dogLvl, dogEat, points FROM users WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        dogEat = int(result['dogEat'])
        dogLvl = int(result['dogLvl'])
        points = int(result['points'])
        if dogLvl == 0:
            bot.reply_to(m, "У тебя еще нет помощника.")
            db.close()
            return
        elif points < 1000:
            bot.reply_to(m, "У тебя не хватает поинтов.")
            db.close()
            return
        else:
            sql = "UPDATE users SET dogEat = 100 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET points = points - 1000 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            db.close()
        bot.reply_to(m, "Энергия помощника восстановлена.")
        return
    



@bot.message_handler(commands=['buy_charlie'])
def buy_charlie(m):
    dogName = "Чарли"
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT dog, points FROM users WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        dog = result['dog']
        points = int(result['points']) 
        if points >= 7500:
            sql = "UPDATE users SET points = points - 7500 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dog = %s WHERE user_id = %s"
            cursor.execute(sql, (dogName, m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dogLvl = 1 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            if dog:
                bot.reply_to(m, "Вы заменили своего старого помощника на Чарли")
            else:
                bot.reply_to(m, "Вы успешно приобрели Чарли.")
                pass
        else:
            bot.reply_to(m, "Чарли стоит 7500 поинтов. У тебя столько нет.")
            db.close()
            return
        db.close()
        return
            
@bot.message_handler(commands=['buy_jack'])
def buy_jack(m):
    dogName = "Джек"
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT dog, points FROM users WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        dog = result['dog']
        points = int(result['points'])
        if points >= 10000:
            sql = "UPDATE users SET points = points - 10000 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dog = %s WHERE user_id = %s"
            cursor.execute(sql, (dogName, m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dogAtk = 5 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dogLvl = 1 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            if dog:
                bot.reply_to(m, "Вы заменили своего старого помощника на Джека")
            else:
                bot.reply_to(m, "Вы успешно приобрели Джек.")
                pass
        else:
            bot.reply_to(m, "Джек стоит 10000 поинтов. У тебя столько нет.")
            db.close()
            return
        db.close()
        return


@bot.message_handler(commands=['buy_james'])
def buy_james(m):
    dogName = "Джеймс"
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT dog, points FROM users WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        dog = result['dog']
        points = int(result['points'])
        if points >= 8000:
            sql = "UPDATE users SET points = points - 8000 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dog = %s WHERE user_id = %s"
            cursor.execute(sql, (dogName, m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dogHp = 5 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dogLvl = 1 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            if dog:
                bot.reply_to(m, "Вы заменили своего старого помощника на Джеймса")
            else:
                bot.reply_to(m, "Вы успешно приобрели Джеймса.")
                pass
        else:
            bot.reply_to(m, "Джеймс стоит 8000 поинтов. У тебя столько нет.")
            db.close()
            return
        db.close()
        return


@bot.message_handler(commands=['buy_andrew'])
def buy_andrew(m):
    dogName = "Эндрю"
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT dog, points FROM users WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        dog = result['dog']
        points = int(result['points'])
        if points >= 9000:
            sql = "UPDATE users SET points = points - 9000 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dog = %s WHERE user_id = %s"
            cursor.execute(sql, (dogName, m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dogCreet = 5 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET dogLvl = 1 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            if dog:
                bot.reply_to(m, "Вы заменили своего старого помощника на Эндрю")
            else:
                bot.reply_to(m, "Вы успешно приобрели Эндрю.")
                pass
        else:
            bot.reply_to(m, "Эндрю стоит 9000 поинтов. У тебя столько нет.")
            db.close()
            return
        db.close()
        return







@bot.message_handler(commands=['buy_lot'])
def buyLot(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM `lot`"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            price = int(result['price'])
            name = result['name']
            sql = "SELECT `points` FROM `users` WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            resultBal = cursor.fetchone()
            points = int(resultBal['points'])
            if points >= price:
                pass
            else:
                bot.reply_to(m, "Недостаточно денег на балансе.")
                db.close()
                return
            sql = "UPDATE `users` SET `points` = points - %s WHERE `user_id` = %s"
            cursor.execute(sql, (price, m.from_user.id))
            db.commit()
            sql = "DELETE FROM `lot` WHERE `price` = %s LIMIT 1"
            cursor.execute(sql, (price))
            db.commit()
            db.close()
        bot.reply_to(m, "Поздравляю с покупкой! Зачисление будет проведено в ближайшее время.")
        bot.send_message(FOO, "Купили {} за {} птс. Покупатель: @{} Начислите, @kakushigoto".format(name, str(price), str(m.from_user.username)))


@bot.message_handler(commands=['buy_atk'])
def buyAtk(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT lvl, atk, points, dog FROM users WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        atk = int(result['atk'])
        points = int(result['points'])
        dog = result['dog']
        if str(m.from_user.id) in donators:
            priceAtk = int(6 * ((atk - 19) / 6))
        elif str(dog) == "Чарли":
            priceAtk = int((10 * ((atk - 19) / 6)) * 0.9)
        else:
            priceAtk = int(10 * ((atk - 19) / 6))
        if lvl >= 2 :
            pass
        else:
            bot.reply_to(m, "Магазин откроется на 3 уровне.")
            db.close()
            return        
        if points >= priceAtk:
            sql = "UPDATE users SET atk = atk + 1 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET points = points - %s WHERE user_id = %s"
            cursor.execute(sql, (int(priceAtk), m.from_user.id))
            db.commit()
            db.close()
            bot.reply_to(m, "Вы успешно купили 1 ед. атаки за {0} поинтов".format(str(priceAtk)))
        else:
            bot.reply_to(m, "У вас недостаточно поинтов для покупки.")
            db.close()
            
            
            





            
@bot.message_handler(commands=['buy_hp'])
def buyHp(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl`, `hp`, `points`, `dog` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        hp = int(result['hp'])
        dog = result['dog']
        points = int(result['points'])
        if str(m.from_user.id) in donators:
            priceHp = int(6 * ((hp - 19) / 6))
        elif dog == "Чарли":
            priceHp = int((10 * ((hp - 19) / 6)) * 0.9)
        else:
            priceHp = int(10 * ((hp - 19) / 6))
        if lvl >= 2 :
            pass
        else:
            bot.reply_to(m, "Магазин откроется на 3 уровне.")
            db.close()
            return        
        if points >= priceHp:
            sql = "UPDATE `users` SET `hp` = hp + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET points = points - %s WHERE user_id = %s"
            cursor.execute(sql, (priceHp, m.from_user.id))
            db.commit()
            db.close()
            bot.reply_to(m, "Вы успешно купили 1 ед. здоровья за {0} поинтов".format(str(priceHp)))
        else:
            bot.reply_to(m, "У вас недостаточно поинтов для покупки.")
            db.close()
            
            
            
            




            
@bot.message_handler(commands=['buy_fatk'])
def buyFatk(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl`, `fatk`, `points`, `dog` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        fatk = int(result['fatk'])
        points = int(result['points'])
        dog = result['dog']
        if str(m.from_user.id) in donators:
            priceFatk = int(12 * ((fatk - 9) / 6))
        elif dog == "Чарли":
            priceFatk = int((15 * ((fatk - 9) / 6)) * 0.9)
        else:
            priceFatk = int(15 * ((fatk - 9) / 6))
        if lvl >= 2 :
            pass
        else:
            bot.reply_to(m, "Магазин откроется на 3 уровне.")
            db.close()
            return        
        if points >= priceFatk:
            sql = "UPDATE `users` SET `fatk` = fatk + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET points = points - %s WHERE user_id = %s"
            cursor.execute(sql, (priceFatk, m.from_user.id))
            db.commit()
            db.close()
            bot.reply_to(m, "Вы успешно купили +1% шанса на первую атаку за {0} поинтов".format(str(priceFatk)))
        else:
            bot.reply_to(m, "У вас недостаточно поинтов для покупки.")
            db.close()
            
            
            
            
            
@bot.message_handler(commands=['buy_crt'])
def buyCreet(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl`, `creet`, `points`, `dog` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        creet = int(result['creet'])
        points = int(result['points'])
        dog = result['dog']
        if str(m.from_user.id) in donators:
            priceCreet = int(15 * ((creet - 4) / 3))
        elif dog == "Чарли":
            priceCreet = int((20 * ((creet - 4) / 3)) * 0.9)
        else:
            priceCreet = int(20 * ((creet - 4) / 3))
        if lvl >= 2 :
            pass
        else:
            bot.reply_to(m, "Магазин откроется на 3 уровне.")
            db.close()
            return        
        if points >= priceCreet:
            sql = "UPDATE `users` SET `creet` = creet + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET points = points - %s WHERE user_id = %s"
            cursor.execute(sql, (priceCreet, m.from_user.id))
            db.commit()
            db.close()
            bot.reply_to(m, "Вы успешно купили +1% к шансу на критический урон за {0} поинтов".format(str(priceCreet)))
        else:
            bot.reply_to(m, "У вас недостаточно поинтов для покупки.")
            db.close()
            
            
            
            
            
            
            
            
@bot.message_handler(commands=['buy_nick'])
def buyNick(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl`, `points` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        points = int(result['points'])
        priceNick = 500
        if lvl >= 2 :
            pass
        else:
            bot.reply_to(m, "Магазин откроется на 3 уровне.")
            db.close()
            return        
        if points >= priceNick:
            none = "None"
            sql = "UPDATE `users` SET `username` = %s WHERE `user_id` = %s"
            cursor.execute(sql, (none, m.from_user.id))
            db.commit()
            sql = "UPDATE users SET points = points - 500 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            db.close()
            bot.reply_to(m, "Вы успешно купили смену никнейма. Воспользуйтесь командой /changenick")
        else:
            bot.reply_to(m, "У вас недостаточно поинтов для покупки.")
            db.close()
            
            
            
            
            
@bot.message_handler(commands=['buy_krazha'])
def buyKrazha(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `lvl`, `points`, `krazha` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        points = int(result['points'])
        krazha = int(result['krazha'])
        krazhaCost = krazha * 150
        if lvl >= 2 :
            pass
        else:
            bot.reply_to(m, "Магазин откроется на 3 уровне.")
            db.close()
            return
        if krazha == 0:
            krazhaCost = 100
            if points < krazhaCost:
                bot.reply_to(m, "Недостаточно поинтов.")
                db.close()
                return
            else:
                pass
            sql = "UPDATE `users` SET `points` = `points` - 100 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE `users` SET `krazha` = 1 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            bot.reply_to(m, "Вы успешно приобрели навык кражи. Используйте команду !кража ответом игроку, у которого хотите украсть поинты.")
            db.close()
            return
        else:
            if points < krazhaCost:
                bot.reply_to(m, "Недостаточно поинтов.")
                db.close()
                return
            else:
                pass
            sql = "UPDATE `users` SET `points` = `points` - %s WHERE `user_id` = %s"
            cursor.execute(sql, (krazhaCost, m.from_user.id))
            db.commit()
            sql = "UPDATE `users` SET `krazha` = krazha + 1 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            bot.reply_to(m, "Вы улучшили навык кражи за " + str(krazhaCost) + " поинтов.")
            db.close()
            
            
            
            
@bot.message_handler(commands=['buy_heal'])
def buyHeal(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `hp`, `points` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        hp = int(result['hp'])
        points = int(result['points'])
        needHilka = hp * 0.5
        if points >= needHilka:
            sql = "UPDATE `users` SET `points` = points - %s WHERE `user_id` = %s"
            cursor.execute(sql, (needHilka, m.from_user.id))
            db.commit()
            sql = "UPDATE `users` SET `nowhp` = hp WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            db.close()
            bot.reply_to(m, "Здоровье успешно восстановлено.")
            return
        else:
            db.close()
            bot.reply_to(m, "У вас недостаточно поинтов для покупки зелья восстановления.")
            return
            
            




@bot.message_handler(commands=['buy_azart'])
def buyAzart(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT azart, lvl, points FROM users WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        azart = int(result['azart'])
        lvl = int(result['lvl'])
        points = int(result['points'])
        if azart == 0:
            needAzart = 5000
        elif azart == 1:
            needAzart = 5500
        elif azart == 2:
            needAzart = 6000
        elif azart == 3:
            needAzart = 6500
        elif azart == 4:
            needAzart = 7000
        elif azart == 5:
            bot.reply_to(m, "Навык прокачан.")
            db.close()
            return
        if lvl >= 2 :
            pass
        else:
            bot.reply_to(m, "Магазин откроется на 3 уровне.")
            db.close()
            return        
        if points >= needAzart:
            sql = "UPDATE users SET azart = azart + 1 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE users SET points = points - %s WHERE user_id = %s"
            cursor.execute(sql, (int(needAzart), m.from_user.id))
            db.commit()
            db.close()
            bot.reply_to(m, "Вы успешно улучшили навык кражи за {0} поинтов".format(str(needAzart)))
        else:
            bot.reply_to(m, "У вас недостаточно поинтов для покупки.")
            db.close()
            
            
            
            
@bot.message_handler(commands=['buy_bankNo'])
def buyBankNo(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `points`, `bankNo` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        bankNo = int(result['bankNo'])
        points = int(result['points'])
        if points >= 1000:
            sql = "UPDATE `users` SET `points` = points - 1000 WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            sql = "UPDATE `users` SET `bankNo` = id WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            db.close()
            bot.reply_to(m, "Вы успешно приобрели банковскую ячейку.")
            return
        else:
            db.close()
            bot.reply_to(m, "У вас недостаточно поинтов для покупки ячейки в банке.")
            return