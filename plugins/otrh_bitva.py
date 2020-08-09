import items
import random
import dogs
eventTitles = ["быкануть на администратора", "спрыгнуть с Чиллиада", "поймать бизнес Майорова", "подать объявление в /adv", "стать лидером фракции", "оплатить дом в банке", "купить туризмо у Линка", "узнать, когда закончится срок Саска", "устроить РП", "провести Character Kill", "слетать в деморган на вертолёте", "убить Kotomi"]
enemyMobsName = [" таксист из гетто", " первый лидер ФБР", " багоюзер", " обладатель НонРп ника", " лидер мафии", " улетевший на вертолете из деморгана читер", " гражданский вертолетчик", " подозрительный человек, представившийся как пожилой арангутан", " англичанин", "и разработчики", " арестованный у притона бандит", " полицейский в костюме медика", "о обновление Chance", "а Анна Антипова", " турист с АК-47", " Винтер Фокс", " шелдонлёт", " водитель автобуса", "а Ваша шизофрения", "а Kotomi"]
battleTitles = ["сказав, что вызывает ментов", "попросив вас написать /q", "предлагая вам деньги", "явно со злыми намерениями посмотрев на вас", "предлагая отойти за угол", "спрашивая, что такое МГ", "используя пауэр гейминг", "демонстрируя техники из Наруто", "приглашая через /d перевестись в ФБР", "вызывая на гачи-борьбу", "устанавливая вам постороннее ПО", "устроив кошмар в душевой LSPD", "собираясь отправить вас в бан", "кидая инвайт в LVA", "начав эпическое сражение", "предлагая оплатить налог на паспорт", "закидывая на мобилку 100к", "делающий подозрительный /time", "доставая ствол", "выбивающий налог на паспорт", "вводя вашу рефералку"]

class otrh_cost():

    @staticmethod
    def init_db():
        db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
        return db

    @staticmethod
    def get_user(user_id):
        db = otrh_cost.init_db()
        with db.cursor() as cursor:
            sql = "SELECT * FROM `users` WHERE `user_id` = %s"
            cursor.execute(sql, user_id)
            result = cursor.fetchone()
        db.close()
        return result


class OtrhBattle:

    @staticmethod
    def fight(player, enemy):
        _player = player
        _enemy = enemy
        eventTitle = random.choice(eventTitles)
        battleTitle = random.choice(battleTitles)

        text = '*{}*, вы решили {}'.format(_player['nick'], eventTitle)

        bYS = ", но на вас напал"
        fA = "Враг атаковал вас первым."

        moves = 1
        first = False
        if _player['fatk'] > random.randint(1, 130):
            first = True
            fA = "Враг вкусил вашей первой атаки."
            bYS = ", но вас встретил"

        text = '*{}*, вы решили {} {} {}, {}\n'.format(_player['nick'], eventTitle, bYS, enemy['nick'], battleTitle)
        PAt = 0
        EAt = 0
        PCr = 0
        ECr = 0
        if _player['tempPts'] > 0:
            randomSneg = random.randint(0, 100)
            if randomSneg > 95:
                _enemy['hp'] = (_enemy['hp'] - int((_enemy['hp'] * 0.95)))
                text += "\n\n\n❄Кинув во врага снежок, вы оставили ему {} HP. Бой продолжается.🤜\n\n\n".format(_enemy['hp'])
                db = otrh_cost.init_db()
                with db.cursor() as cursor:
                    sql = "UPDATE users SET tempPts = tempPts - 1 WHERE `username` = %s"
                    cursor.execute(sql, (_player['nick']))
                    db.commit()
                    db.close()
        while _player['hp'] > 0 and _enemy['hp'] > 0:
            if (moves == 1 and first) or moves > 1:
                atk = random.randint(round(_player['atk'] * 0.8), round(_player['atk'] * 1.2))
                if _player['crit'] / 2 > random.randint(1, 70):
                    atk *= 1.5
                    PCr += 1
                atk = round(atk)
                if random.random() < 0.95:
               	    _enemy['hp'] -= atk
                    PAt += atk
                    text += '\n{} нанес удар 💥{}'.format(_player['nick'], atk)
                else:
                    text += '\n{} подскользнулся на льду❄️ во время удара {}'.format(_enemy['nick'], _player['nick'])

            if _enemy['hp'] > 0:
                atk = random.randint(round(_enemy['atk'] * 0.8), round(_enemy['atk'] * 1.2))
                if _enemy['crit'] / 2 > random.randint(1, 70):
                    atk *= 1.5
                    ECr += 1
                atk = round(atk)
                if random.random() < 0.95:
                    _player['hp'] -= atk
                    EAt += atk
                    text += '\n{} нанес удар 💥{}'.format(_enemy['nick'], atk)
                else:
                    text += '\n{} увернулся💨 от удара {}'.format(_player['nick'], _enemy['nick'])

            moves += 1

        winner = 'player'
        if enemy['hp'] < 1:
            enemy['hp'] = 0
        if player['hp'] < 1:
            winner = 'enemy'
            player['hp'] = 0

        text += '\n\nРезультаты боя: '
        text += '\nУ вас осталось {}❤️ и вы нанесли {} урона, за бой вы нанесли {} крит. ударов'.format(_player['hp'], PAt, PCr)
        text += '\nУ врага осталось {}💜 и он насес вам {} урона, за бой он нанес {} крит. ударов'.format(_enemy['hp'], EAt, ECr)

        return [text, winner]


def otrh_battle(m):
    otrh_battle1(m)

def otrh_battle1(m):
    player = otrh_cost.get_user(m.from_user.id)
    username = player['username']

    if not player:
        bot.reply_to(m, 'Нужно зарегистироваться')
        return

    if player['lvl'] < 2:
        bot.reply_to(m, 'Ты ещё не достиг высот для битв.')
        return

    if player['nowhp'] < player['hp']:
        text = 'Ты еще не до конца поправился. Пойди еще отдохни. \n У тебя {}/{} ❤️ здоровья'
        bot.reply_to(m, text.format(player['nowhp'], player['hp']))
        return

    BM = int(player['atk'] + player['hp'] + (((player['fatk']/100) + (player['creet']/100)) * 10))

    _id_p = None
    if m.reply_to_message:
        _id_p = m.reply_to_message.from_user.id
        db = otrh_cost.init_db()
        with db.cursor() as cursor:
            sql = "SELECT `frakaName` FROM `users` WHERE `user_id` = %s"
            cursor.execute(sql, (str(m.from_user.id)))
            result = cursor.fetchone()
            frakaName = result['frakaName']
            if not result:
                frakaName = "."
                warStatus = 0
                frakaEnemy = " "
                db.close()
            else:
                sql = "SELECT `warFraka` FROM `fraks` WHERE `name` = %s"
                cursor.execute(sql, (frakaName))
                result = cursor.fetchone()
                if result:
                    frakaEnemy = result['warFraka']
                else:
                    frakaEnemy = None
                sql = "SELECT `warStatus` FROM `fraks` WHERE `name` = %s"
                cursor.execute(sql, (frakaName))
                result = cursor.fetchone()
                if result:
                	warStatus = result['warStatus']
                else:
                	warStatus = None
                sql = "SELECT `frakaName` FROM `users` WHERE `user_id` = %s"
                cursor.execute(sql, (m.reply_to_message.from_user.id))
                result = cursor.fetchone()
                if not result:
                    frakaEnemyNow =" "
                    warStatus = 0
                else:
                    frakaEnemyNow = result['frakaName']
                    pass
                db.close()
                print(str(frakaName))
                print(str(frakaEnemy))
                print(str(frakaEnemyNow))
                print(str(warStatus))
        if player['lvl'] < 3:
            bot.reply_to(m, 'Ты ещё не достиг высот для битв с другими игроками.')
            return 

        if _id_p == m.from_user.id:
            bot.reply_to(m, 'Ты не можешь убивать сам себя.')
            return

        _p_data = otrh_cost.get_user(_id_p)
        if _p_data:

            if _p_data['lvl'] < 3:
                bot.reply_to(m, 'Пользователь не достиг уровня для битв с другими игроками')
                return

            if _p_data['local'] != player['local']:
                bot.reply_to(m, 'Вы находитесь в разных локациях')
                return

            if _p_data['nowhp'] < _p_data['hp']:
                bot.reply_to(m, 'Игрок отдыхает от прошлого боя. Не трожь его')
                return

            _p_bm = int(_p_data['atk'] + _p_data['hp'] + (((_p_data['fatk']/100) + (_p_data['creet']/100)) * 10))
            _p_bm_frame = [round(_p_bm / 1.5), round(_p_bm * 1.5)]

            if BM > _p_bm_frame[1] or BM < _p_bm_frame[0]:
                bot.reply_to(m, 'Ты не равносильный противник игроку')
                return

            player = {'nick': player['username'], 'hp': player['hp'], 'atk': player['atk'], 'fatk': player['fatk'], 'crit': player['creet'], 'tempPts': player['tempPts']}
            enemy = {'nick': _p_data['username'], 'hp': _p_data['hp'], 'atk': _p_data['atk'], 'fatk': _p_data['fatk'], 'crit': _p_data['creet']}
            test = OtrhBattle.fight(player, enemy)

        else:
            bot.reply_to(m, 'Выбери игрока, который зарегистрирован')
            return

    else:
        db = otrh_cost.init_db()
        with db.cursor() as cursor:
            sql = "SELECT * FROM `wrestling` WHERE localspawn = %s"
            cursor.execute(sql, player['local'])
            mobchar = cursor.fetchall()
            frakaName = " "
            frakaEnemy = "."
            frakaEnemyNow =" "

        db.close()

        if not mobchar:
            bot.reply_to(m, 'В твоей локации кончились мобы, {}'.format(BM))
            return

        mobchar = random.choice(mobchar)

        player = {'nick': player['username'], 'hp': player['hp'], 'atk': player['atk'], 'fatk': player['fatk'], 'crit': player['creet'], 'item': player['item'], 'tempPts': player['tempPts']}
        mob_hp = random.randint(round(player['atk'] * 1.5), round(player['atk'] * 2))
        mob_atk = random.randint(round(player['hp'] * 0.5), round(player['hp'] * 0.9))
        enemy = {'nick': mobchar['mobname'], 'hp': mob_hp, 'atk': mob_atk, 'fatk': player['fatk'], 'crit': player['crit']}
        db = otrh_cost.init_db()
        print(str(player))
        with db.cursor() as cursor:
            sql = "SELECT dogAtk , dogHp , dogFatk , dogCreet, dog, dogLvl, tempPts FROM users WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            dogResult = cursor.fetchone()
            if dogResult:
                dogAtk = dogResult['dogAtk']
                dog = dogResult['dog']
                dogLvl = dogResult['dogLvl']
                dogHp = dogResult['dogHp']
                dogFatk = dogResult['dogFatk']
                dogCreet = dogResult['dogCreet']
                nowAtk = player['atk'] + dogAtk
                nowHp = player['hp'] + dogHp
                nowFatk = player['fatk'] + dogFatk
                nowCreet = player['crit'] + dogCreet
                tempPts = dogResult['tempPts'] # пизда я костылю
                player = {'nick': player['nick'], 'hp': nowHp, 'atk': nowAtk, 'fatk': nowFatk, 'crit': nowCreet, 'item': player['item'], 'dog': dog, 'dogLvl': dogLvl, 'tempPts': player['tempPts']}
                print(str(player))
             #   test[0] += "Ваш помощник {} поможет вам 
                db.close()
            else:
                db.close()
                pass
        test = OtrhBattle.fight(player, enemy)

    if test[1] == 'enemy':
        db = otrh_cost.init_db()
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `nowhp` = 0 WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            db.commit()
            if (frakaEnemy == frakaEnemyNow) and (warStatus == 1):
                randPtsFraka = random.randint(2, 5)
                sql = "UPDATE `fraks` SET `warPts` = warPts + %s WHERE `name` = %s"
                cursor.execute(sql, (randPtsFraka, frakaEnemy))
                db.commit()
                test[0] += "\nЗа проигрыш перед врагом фракции, во вражескую фракцию начислены фракционные очки."
                pass
            else:
                pass
            db.close()

            if _id_p:
                db = otrh_cost.init_db()
                cursor = db.cursor()
                sql = "SELECT `lvl` FROM `users` WHERE user_id = %s"
                cursor.execute(sql, _id_p)
                result = cursor.fetchone()
                lvl = result['lvl']
                randPoint = random.randint(7, 15)
                givePts = (int(lvl) / 2) * randPoint
                sql = "UPDATE `users` SET `points` = points + %s WHERE user_id = %s"
                cursor.execute(sql, (int(randPoint), _id_p))
                db.commit()
                chanceexp = 1
                if chanceexp == 1:
                    sql = "SELECT `lvl` FROM `users` WHERE user_id = %s"
                    cursor.execute(sql, _id_p)
                    result = cursor.fetchone()
                    randExp = random.randint(2, 3)
                    expgive_count = int(result['lvl']) * randExp
                    expgive = int(expgive_count)
                    db.commit()
                    sql = "UPDATE `users` SET `exp` = exp + %s WHERE user_id = %s"
                    cursor.execute(sql, (int(expgive), _id_p))
                    db.commit()
                    sql = "SELECT `exp`, `lvl` FROM `users` WHERE user_id = %s"
                    cursor.execute(sql, _id_p)
                    result = cursor.fetchone()
                    needexp = int(result['lvl']) * 100
                    plustats = int(needexp) / 50
                    if (int(result['exp']) >= needexp):
                        ex2p = 0
                        sql = "UPDATE `users` SET `exp` = %s WHERE user_id = %s"
                        cursor.execute(sql, (int(ex2p), _id_p))
                        db.commit()
                        sql = "UPDATE `users` SET `lvl` = lvl + 1 WHERE user_id = %s"
                        cursor.execute(sql, _id_p)
                        sql = "UPDATE `users` SET `atk` = atk + %s WHERE user_id = %s"
                        cursor.execute(sql, (plustats, _id_p))
                        sql = "UPDATE `users` SET `hp` = hp + %s WHERE user_id = %s"
                        cursor.execute(sql, (plustats, _id_p))
                        bot.send_message(m.chat.id, "LVL UP. Статы противника повышены на +{0}.".format(str(plustats)))
                        db.commit()
                db.close()

        bot.send_message(chancechat, '{} одержал победу над {}'.format(enemy['nick'], player['nick']))
    elif test[1] == 'player':
        db = otrh_cost.init_db()
        with db.cursor() as cursor:
            sql = "SELECT dogLvl FROM users WHERE username = %s"
            cursor.execute(sql, (player['nick']))
            res = cursor.fetchone()
            dogLvl = res['dogLvl']
            if dogLvl >= 1:
                test[0] += "\n{} помог вам в битве!".format(dog)
            else:
                pass
            item = int(player['item'])
            items.items(item, player)
            item, desc, har = items.itemsdrop()
            if item:
                print(har)
                itemGet = har.split('_')
                id = int(itemGet[0])
                atk = int(itemGet[1])
                hp = int(itemGet[2])
                fatk = int(itemGet[3])
                creet = int(itemGet[4])
                print(int(id))
                print(str(atk))
                print(str(m.from_user.id))
                test[0] += "\nОсмотрев местность, ты нашел что-то неподалёку... хмм...{}! {}".format(item, desc)
                sql = "UPDATE `users` SET `item` = %s WHERE `user_id` = %s"
                cursor.execute(sql, (id, m.from_user.id))
                db.commit()
                sql = "UPDATE `users` SET `atk` = atk + %s WHERE `user_id` = %s"
                cursor.execute(sql, (atk, m.from_user.id))
                db.commit()
                sql = "UPDATE `users` SET `hp` = hp + %s WHERE `user_id` = %s"
                cursor.execute(sql, (hp, m.from_user.id))
                db.commit()
                sql = "UPDATE `users` SET `fatk` = fatk + %s WHERE `user_id` = %s"
                cursor.execute(sql, (fatk, m.from_user.id))
                db.commit()
                sql = "UPDATE `users` SET `creet` = creet + %s WHERE `user_id` = %s"
                cursor.execute(sql, (creet, m.from_user.id))
                db.commit()
                sql = "UPDATE `users` SET `nowhp` = hp WHERE `user_id` = %s"
                cursor.execute(sql, (m.from_user.id))
                db.commit()
            else:
                pass
            if _id_p:
                sql = "UPDATE `users` SET `nowhp` = 0 WHERE user_id = %s"
                cursor.execute(sql, (_id_p))
                db.commit()
            if (frakaEnemy == frakaEnemyNow) and (warStatus == 1):
                randPtsFraka = random.randint(1,3)
                sql = "UPDATE `fraks` SET `warPts` = warPts + %s WHERE `name` = %s"
                cursor.execute(sql, (randPtsFraka, frakaName))
                db.commit()
                test[0] += "\nЗа победу над врагом фракции начислены фракционные очки."
                pass
            else:
                pass
            sql = "SELECT `lvl` FROM `users` WHERE user_id = %s"
            cursor.execute(sql, (m.from_user.id))
            result = cursor.fetchone()
            lvl = result['lvl']
            randPoint = random.randint(6, 14)
            givePts = (int(lvl) / 2) * randPoint
            sql = "UPDATE `users` SET `points` = points + %s WHERE user_id = %s"
            cursor.execute(sql, (int(randPoint), m.from_user.id))
            db.commit()
            chanceexp = 1
            if chanceexp == 1:
                sql = "SELECT `lvl` FROM `users` WHERE user_id = %s"
                cursor.execute(sql, (m.from_user.id))
                result = cursor.fetchone()
                randExp = random.randint(2, 3)
                expgive_count = int(result['lvl']) * randExp
                expgive = int(expgive_count)
                db.commit()
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
                    db.close()
            else:
                db.close()
    else:
        bot.send_message(m, "Ошибка определителя")
        return
    text = test[0]
    bot.reply_to(m, text)