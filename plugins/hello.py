@bot.message_handler(content_types=['new_chat_members'])
def bot_join(m):
    bot.send_message(m.chat.id, 'Привет, *{0}*, Я _Мегумин_ - самый лучший Архимаг. Выбери свой никнейм командой /changenick \nТак же, крайне советую прочесть руководство по игре - https://telegra.ph/Kotomi-Rukovodstvo-09-30'.format(m.from_user.username), None, m.message_id, None, 'markdown',  None)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(sql, (str(m.from_user.id)))
        result = cursor.fetchone()
        if result:
            return
        else:
            pass
        sql = "INSERT INTO users (username, user_id, lvl, points, atk, hp) VALUES ('None', %s, '1', '0', '8', '8')"
        cursor.execute(sql, (str(m.from_user.id)))
        db.commit()
        db.close()
            
            
@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Привет, *{0}*, Я _Мегумин_ - самый лучший Архимаг. Выбери свой никнейм командой /changenick \nТак же, крайне советую прочесть руководство по игре - https://telegra.ph/Kotomi-Rukovodstvo-09-30'.format(m.from_user.username), None, m.message_id, None, 'markdown',  None)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
        sql = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(sql, (str(m.from_user.id)))
        result = cursor.fetchone()
        if result:
            return
        else:
            pass
        sql = "INSERT INTO users (username, user_id, lvl, points, atk, hp) VALUES ('None', %s, '1', '0', '8', '8')"
        cursor.execute(sql, (str(m.from_user.id)))
        db.commit()
        db.close()
		
		
	
@bot.message_handler(content_types=['left_chat_member'])
def bot_leave(m):
    bot.send_message(m.chat.id, 'Ну и ладно! Он мне всё-равно не нравился...' , None, m.message_id, None, 'markdown',  None)