import pymysql
import pymysql.cursors

def dogEat():
    dog = "умер"
    dogAtk = 0
    dogHp = 0
    dogFatk = 0
    dogCreet = 0
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `users` SET `dogEat` = dogEat - 5 WHERE `dogLvl` > 0"
        cursor.execute(sql)
        db.commit()
        sql = "UPDATE `users` SET `dogLvl` = 0 WHERE `dogEat` = 0"
        cursor.execute(sql)
        db.commit()
        sql = "UPDATE `users` SET `dog` = %s WHERE `dogEat` = 0"
        cursor.execute(sql, (dog))
        db.commit()
        sql = "UPDATE `users` SET `dogAtk` = %s WHERE `dogEat` = 0"
        cursor.execute(sql, (dogAtk))
        db.commit()
        sql = "UPDATE `users` SET `dogHp` = %s WHERE `dogEat` = 0"
        cursor.execute(sql, (dogHp))
        db.commit()
        sql = "UPDATE `users` SET `dogFatk` = %s WHERE `dogEat` = 0"
        cursor.execute(sql, (dogFatk))
        db.commit()
        sql = "UPDATE `users` SET `dogCreet` = %s WHERE `dogEat` = 0"
        cursor.execute(sql, (dogCreet))
        db.commit()
    db.close()

dogEat()