@bot.message_handler(commands=['buy_atk'])
def buyAtk(m):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT lvl, atk, points FROM users WHERE user_id = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        atk = int(result['atk'])
        points = int(result['points'])
        priceAtk = int(10 * ((atk - 19) / 6))
        if lvl >= 3 :
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
        sql = "SELECT `lvl`, `hp`, `points` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        hp = int(result['hp'])
        points = int(result['points'])
        priceHp = int(10 * ((hp - 19) / 6))
        if lvl >= 3 :
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
        sql = "SELECT `lvl`, `fatk`, `points` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        fatk = int(result['fatk'])
        points = int(result['points'])
        priceFatk = int(15 * ((fatk - 9) / 6))
        if lvl >= 3 :
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
        sql = "SELECT `lvl`, `creet`, `points` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        lvl = int(result['lvl'])
        creet = int(result['creet'])
        points = int(result['points'])
        priceCreet = int(20 * ((creet - 4) / 3))
        if lvl >= 3 :
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
        if lvl >= 3 :
            pass
        else:
            bot.reply_to(m, "Магазин откроется на 3 уровне.")
            db.close()
            return        
        if points >= priceNick:
            sql = "UPDATE `users` SET `username` = None WHERE `user_id` = %s"
            cursor.execute(sql, (m.from_user.id))
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
        if lvl >= 3 :
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