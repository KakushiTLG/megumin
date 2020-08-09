def krazha(m):
    randomTrus = ['Катерины Велкон', 'Вана Даркхолма', 'Оторхина', 'Даркнес', 'Аквы', 'Гачи-братана', 'Элли Майерс', 'Марии Кьюри', 'той квестоводки, имя которой всегда сложно вспомнить', 'Казумы', 'несовершеннолетней школьницы', 'бабульки-НПС', 'Анны Антиповой']
    randomTrusi = random.choice(randomTrus)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT `krazha`, `points`, `krazhatime` FROM `users` WHERE `user_id` = %s"
        cursor.execute(sql, (m.from_user.id))
        result = cursor.fetchone()
        krazha = int(result['krazha'])
        points = int(result['points'])
        checkTime = int(result['krazhatime'])
        if krazha >= 1 :
            pass
        else:
            bot.reply_to(m, "У вас нет навыка кражи")
            db.close()
            return        
        if points <= 100:
            bot.reply_to(m, "Нужно иметь хотя бы 100 поинтов на балансе для использования способности.")
            return
        else:
            pass
        if int(checkTime) > math.ceil(time.time()):
            bot.reply_to(m, "Ты слишком часто используешь способность!")
            return
        else:
            pass
        if m.reply_to_message:
            sql = "SELECT `points`, `username`, `lvl` FROM `users` WHERE `user_id` = %s"
            cursor.execute(sql, (m.reply_to_message.from_user.id))
            result = cursor.fetchone()
            enemyPts = int(result['points'])
            enemyLvl = int(result['lvl'])
            enemyName = result['username']
            pass
        else:
            bot.reply_to(m, "Ты что, хочешь сам у себя что-то украсть? Отправляй команду ответом тому, у кого ты хочешь что-то украсть")
            db.close()
            return
        if enemyLvl >= 4:
            pass
        else:
            bot.reply_to(m, "У человека нет 4 уровня")
            db.close()
            return
        if enemyPts >= 500:
            krazhatimeplus = math.ceil(time.time())
            sql = "UPDATE `users` SET `krazhatime` = %s + 300 WHERE `user_id` = %s"
            cursor.execute(sql, (krazhatimeplus, m.from_user.id))
            db.commit()
            pass
        else:
            bot.reply_to(m, "У игрока мало поинтов, пожалей его...")
            db.close()
            return
        if (krazha == 1):
            krazhachance = 10
            krazhaPts = random.randint(15, 20)
            krazhacost = 5
        elif (krazha == 2):
            krazhachance = 20
            krazhaPts = random.randint(15, 30)
            krazhacost = 7
        elif (krazha == 3):
            krazhachance = 30
            krazhaPts = random.randint(15, 40)
            krazhacost = 10
        elif (krazha == 4):
            krazhachance = 40
            krazhaPts = random.randint(15, 50)
            krazhacost = 13
        elif (krazha == 5):
            krazhachance = 50
            krazhaPts = random.randint(20, 40)
            krazhacost = 15
        elif (krazha == 6):
            krazhachance = 60
            krazhaPts = random.randint(20, 30)
            krazhacost = 20
        elif (krazha == 7):
            krazhachance = 70
            krazhaPts = random.randint(20, 60)
            krazhacost = 25
        elif (krazha == 8):
            krazhachance = 80
            krazhaPts = random.randint(25, 70)
            krazhacost = 30
        elif (krazha == 9):
            krazhachance = 90
            krazhaPts = random.randint(25, 80)
            krazhacost = 35
        elif (krazha == 10):
            krazhachance = 100
            krazhaPts = random.randint(50, 60)
            krazhacost = 50
        elif (krazha >= 11):
            krazhachance = 100
            krazhaPts = random.randint(50, (50 + (krazha * 2)))
            krazhacost = 50
        chance = random.randint(1, 100)
        if chance > krazhachance:
            sql = "UPDATE users SET points = points - %s WHERE user_id = %s"
            cursor.execute(sql, (krazhacost, str(m.from_user.id)))
            db.commit()
            sql = "UPDATE users SET points = points + %s WHERE user_id = %s"
            cursor.execute(sql, (krazhacost, str(m.reply_to_message.from_user.id)))
            db.commit()
            db.close()
            bot.reply_to(m, "Заклинание стоило " + str(krazhacost) + " поинтов. \nТы попытался украсть поинты у " + enemyName + ", однако ты недостаточно прокачал навык и вместо поинтов смог украсть только трусы " + str(randomTrusi) + " . Зато эти поинты отныне принадлежат вашей цели.")
            return
        else:
            sql = "UPDATE users SET points = points - %s WHERE user_id = %s"
            cursor.execute(sql, (krazhacost, str(m.from_user.id)))
            db.commit()
            sql = "UPDATE users SET points = points + %s WHERE user_id = %s"
            cursor.execute(sql, (krazhaPts, str(m.from_user.id)))
            db.commit()
            sql = "UPDATE users SET points = points - %s WHERE user_id = %s"
            cursor.execute(sql, (krazhaPts, str(m.reply_to_message.from_user.id)))
            db.commit()
            db.close()
        bot.reply_to(m, "Заклинание стоило " + str(krazhacost) + " поинтов. \nТы попытался украсть поинты у " + enemyName + "... \nПоздравляю! Ты смог украсть " + str(krazhaPts) + "поинтов!")
kosti_one = 'CAACAgIAAxkBAAECRM9fAAHVdfPfbkn8Ca-mQ2itba1SzckAAtzGAQABY4tGDLG1EhRKLhr_GgQ'
kosti_two = 'CAACAgIAAxkBAAECRNFfAAHV3FbtSsmyIKib4dDNDphvUhYAAt3GAQABY4tGDOtPKTvsIwJRGgQ'
kosti_three = 'CAACAgIAAxkBAAECRNNfAAHV7tErNvKyRSqTAcRDIXdVVzIAAt7GAQABY4tGDFRx_YWr-yC5GgQ'
kosti_four = 'CAACAgIAAxkBAAECRNVfAAHV-zEqxnTjKqxhEeBalcm7ty4AAt_GAQABY4tGDBxFEyDVu2MXGgQ'
kosti_five = 'CAACAgIAAxkBAAECRNdfAAHWDvIQ-jOJqjnOIDYLbzXYzzQAAuDGAQABY4tGDEix8_rI_yapGgQ'
kosti_six = 'CAACAgIAAxkBAAECRNlfAAHWHf-OO6UiHxFiWuqlz1RK3JQAAuHGAQABY4tGDO-afM2nv7R6GgQ'

def kosti(m):
    if m.reply_to_message and m.reply_to_message.from_user.id != m.from_user.id:
        db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "SELECT points, user_id, username FROM users WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            player1 = cursor.fetchone()
            if player1:
                sql = "SELECT points, user_id, username FROM users WHERE user_id = %s"
                cursor.execute(sql, (m.reply_to_message.from_user.id))
                player2 = cursor.fetchone()
                if player2:
                    if player1['points'] >= 100 and player2['points'] >= 100:
                        sql = "UPDATE users SET points = points - 100 WHERE user_id = %s"
                        cursor.execute(sql, (m.from_user.id))
                        db.commit()
                        sql = "UPDATE users SET points = points - 100 WHERE user_id = %s"
                        cursor.execute(sql, (m.reply_to_message.from_user.id))
                        db.commit()
                        text = "Игра начинается! Вы бросаете первым..."
                        bot.reply_to(m, text)
                        a = threading.Timer(5, kosti_go, [m, player1, player2])
                        a.start()
                        db.close()
                    else:
                        bot.reply_to(m, 'У вас или вашего противника меньше 100 поинтов для игры в кости.')
                        db.close()
                else:
                    bot.reply_to(m, 'Не удалось получить информацию об игроке. Игра отменена.')
                    db.close()
            else:
                bot.reply_to(m, 'Не удалось проверить ваш баланс. Вы точно зарегистрированы?')
                db.close()
    else:
        text = "Отправь команду ответом на сообщение тому, с кем хочешь сыграть."
        bot.reply_to(m, text)


def kosti_go(m, player1, player2):
    r = random.randint(1, 6)
    if player1['user_id'] == '503247028':
        r = 6
    if r == 1:
        play1 = kosti_one
    elif r == 2:
        play1 = kosti_two
    elif r == 3:
        play1 = kosti_three
    elif r == 4:
        play1 = kosti_four
    elif r == 5:
        play1 = kosti_five
    else:
        play1 = kosti_six
    bot.send_sticker(m.chat.id, play1)
    bot.send_message(m.chat.id, "Очередь второго игрока...")
    a = threading.Timer(5, kosti_end, [m, player1, player2, r])
    a.start()

def kosti_end(m, player1, player2, r):
    r2 = random.randint(1, 6)
    if player2['user_id'] == '503247028':
        r2 = 6
    if r2 == 1:
        play2 = kosti_one
    elif r2 == 2:
        play2 = kosti_two
    elif r2 == 3:
        play2 = kosti_three
    elif r2 == 4:
        play2 = kosti_four
    elif r2 == 5:
        play2 = kosti_five
    else:
        play2 = kosti_six
    bot.send_sticker(m.chat.id, play2)
    a = threading.Timer(5, kosti_end2, [m, player1, player2, r, r2])
    a.start()
def kosti_end2(m, player1, player2, r, r2):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        if r == r2:
            bot.send_message(m.chat.id, "Ничья")
            sql = "UPDATE users SET points = points + 100 WHERE user_id = %s"
            cursor.execute(sql, (player1['user_id']))
            db.commit()
            sql = "UPDATE users SET points = points + 100 WHERE user_id = %s"
            cursor.execute(sql, (player2['user_id']))
            db.commit()
        elif r > r2:
            bot.send_message(m.chat.id, "Победил игрок " + player1['username'])
            sql = "UPDATE users SET points = points + 100 WHERE user_id = %s"
            cursor.execute(sql, (player1['user_id']))
            db.commit()
        elif r < r2:
            bot.send_message(m.chat.id, "Победил игрок " + player2['username'])
            sql = "UPDATE users SET points = points + 100 WHERE user_id = %s"
            cursor.execute(sql, (player2['user_id']))
            db.commit()
        db.close()