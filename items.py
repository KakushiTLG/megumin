import math
import random
import pymysql
import pymysql.cursors

def item(itemNow):
    if itemNow == 1:
        item = "Топор"
        desc = "Топор очень пригодится в процессе колки дров... или людей... +5 atk +10 creet"
        har = "1_5_0_0_10"
    elif itemNow == 2:
        item = "Булыжник"
        desc = "Булыжник очень поможет тебе, если ты хочешь нанести первый удар. +15 FA"
        har = "2_0_0_15_0"
    elif itemNow == 3:
        item = "Разбитая бутылка"
        desc = "Такой только людей колоть...+10 atk&FA, +5 creet"
        har = "3_10_0_10_5"
    elif itemNow == 4:
        item = "Нож"
        desc = "Обычный кухонный нож. +20 atk, +15 creet"
        har = "4_20_0_0_15"
    elif itemNow == 5:
        item = "Булочка с пекарни Фурукавы"
        desc = "Молись, чтобы это была булочка, испечённая не Санае..."
        har = "5_0_20_0_0"
    elif itemNow == 6:
        item = "Фруктошарик"
        desc = "Достаточно вкусно... +20hp"
        har = "5_0_20_0_0"
    elif itemNow == 7:
        item = "Булочка с пекарни Фурукавы"
        desc = "Молись, чтобы это была булочка, испечённая не Санае..."
        har = "5_0_-50_0_0"
    elif itemNow == 100:
        item = "Палка"
        desc = "Время выкалывать глаза.+1atk&hp&FA&creet"
        har = "100_1_1_1_1"
    elif itemNow == 999:
        item = "Хуй"
        desc = "+3 к пидорству"
        har = "999_0_0_0_0"
    else:
        item = None
        desc = None
        har = None
    return item
def items(item, player):
    if item == 1: # топор
        db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor:
            sql = "UPDATE `users` SET `atk` = atk - 5 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            sql = "UPDATE `users` SET `creet` = creet - 10 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            sql = "UPDATE `users` SET `item` = 0 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            db.close()
        return player
    elif item == 2: #булыжник
        db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor: 
            sql = "UPDATE `users` SET `fatk` = fatk - 15 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            sql = "UPDATE `users` SET `item` = 0 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            db.close()
        return player
    elif item == 3: #бутылка
        db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor: 
            sql = "UPDATE `users` SET `fatk` = fatk - 10 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            sql = "UPDATE `users` SET `atk` = atk - 10 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            sql = "UPDATE `users` SET `creet` = creet - 5 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            sql = "UPDATE `users` SET `item` = 0 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            db.close()
        return player
    elif item == 4: # нож
        db = pymysql.connect(host='localhost',
                        user='root',
                        password='maz1aan16v',                             
                        db='Megumin',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
        with db.cursor() as cursor: 
            sql = "UPDATE `users` SET `atk` = atk - 20 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            sql = "UPDATE `users` SET `creet` = creet - 15 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            sql = "UPDATE `users` SET `item` = 0 WHERE `username` = %s"
            cursor.execute(sql, (player['nick']))
            db.commit()
            db.close()
        return player
    else:
        return player

def itemsdrop():
    rando = random.randint(1, 100)
    #1 - id _ 5 - atk _ 0 - hp _ 0 - fatk _ 10 - creet
    if rando == 1:
        item = "Топор"
        desc = "Топор очень пригодится в процессе колки дров... или людей... +5 atk +10 creet"
        har = "1_5_0_0_10"
    elif rando == 2:
        item = "Булыжник"
        desc = "Булыжник очень поможет тебе, если ты хочешь нанести первый удар. +15 FA"
        har = "2_0_0_15_0"
    elif rando == 3:
        item = "Разбитая бутылка"
        desc = "Такой только людей колоть...+10 atk&FA, +5 creet"
        har = "3_10_0_10_5"
    elif rando == 4:
        item = "Нож"
        desc = "Обычный кухонный нож. +20 atk, +15 creet"
        har = "4_20_0_0_15"
    elif rando == 5:
        item = "Булочка с пекарни Фурукавы"
        desc = "Молись, чтобы это была булочка, испечённая не Санае..."
        har = "5_0_20_0_0"
    elif (rando >= 95):
        item = "Палка"
        desc = "Время выкалывать глаза.+1atk&hp&FA&creet. Мало, зато навсегда."
        har = "100_1_1_1_1"
    else:
        item = None
        desc = None
        har = None
    return item, desc, har