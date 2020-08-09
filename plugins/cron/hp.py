import pymysql
import pymysql.cursors

def change_stamina():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "UPDATE `users` SET `nowhp` = nowhp + 10 WHERE `nowhp` < `hp`"
        cursor.execute(sql)
    db.commit()
    db.close()

change_stamina()
