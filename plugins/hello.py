@bot.message_handler(content_types=['new_chat_members'])
def bot_join(m):
    bot.send_message(m.chat.id, 'Привет, *{0}*, Я _Мегумин_ - главный архимаг этого чата! Выбери свой никнейм командой /changenick'.format(m.from_user.username), None, m.message_id, None, 'markdown',  None)
    bot.send_video(m.chat.id, open('./media/hello/new.mp4', 'rb'), reply_to_message_id = m.message_id)
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='maz1aan16v',                             
                         db='Megumin',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    with db.cursor() as cursor:
            sql = "INSERT INTO users (username, user_id, lvl, points, atk, hp) VALUES ('None', %s, '1', '0', '0', '0')"
            cursor.execute(sql, (str(m.from_user.id)))
            db.commit()
            db.close()
            
            
          
		
@bot.message_handler(content_types=['left_chat_member'])
def bot_leave(m):
    bot.send_message(m.chat.id, 'Ну и ладно. Он все равно мне не нравился.' , None, m.message_id, None, 'markdown',  None)
    bot.send_video(m.chat.id, open('./media/hello/left.mp4', 'rb'), reply_to_message_id = m.message_id)